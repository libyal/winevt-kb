## hvservice.sys

Path: %SystemRoot%\system32\drivers\hvservice.sys

### 10.0.17134.766

Message identifier | Message string
--- | ---
0x00000001 | Hypervisor successfully started.\r\n
0x00000002 | Hypervisor scheduler type is %1.\r\n
0x00000003 | Hypervisor Eventlog for global system events could not be created!\r\n
0x00000005 | Hypervisor launch has been disabled through the hypervisorlaunchtype bcdedit setting.\r\n
0x0000000d | Hypervisor fails to start ETW tracing session.\r\n
0x00000014 | Hypervisor launch failed; sleep and hibernate could not be disabled (status %1).\r\n
0x0000001a | Hypervisor launch failed; the hypervisor boot loader's internal logic failed (BalStatus %1, sub-status %2).\r\n
0x0000001b | Hypervisor launch failed; the hypervisor boot loader was unable to allocate sufficient resources to perform the launch.\r\n
0x0000001c | Hypervisor launch failed; the hypervisor boot loader does not support the vendor of at least one of the processors in the system.\r\n
0x0000001d | Hypervisor launch failed; at least one of the processors in the system does not appear to support the features required by the hypervisor.  (leaf: %1, required features: %2, features available: %3)\r\n
0x0000001f | Hyper-V launch failed; the system does not appear to have a sufficient level of ACPI support to launch the hypervisor.\r\n
0x00000020 | Hypervisor launch failed; at least one of the processors in the system does not appear to provide a virtualization platform supported by the hypervisor.\r\n
0x00000021 | Hyper-V launch failed; the image %1 could not be accessed (status %2).\r\n
0x00000022 | Hyper-V launch failed; the image %1 could not be loaded (status %2).\r\n
0x00000023 | Hyper-V launch failed; the image %1 could not be read (status %2).\r\n
0x00000024 | Hypervisor launch failed; the image %1 failed code integrity checks, and cannot be used.\r\n
0x00000025 | Hypervisor launch failed; the image %1 does not contain the image description datastructures, and cannot be used.\r\n
0x00000026 | Hyper-V launch failed; at least one of the processors in the system was unable to launch the hypervisor (status %1).\r\n
0x00000028 | Hypervisor launch failed; the hypervisor image is revision %1, but the currently installed virtualization software only supports launching revision %2 hypervisor images.\r\n
0x00000029 | Hypervisor launch failed; Either VMX not present or not enabled in BIOS.\r\n
0x0000002a | Hypervisor launch failed; Either SVM not present or not enabled in BIOS.\r\n
0x0000002c | Hypervisor launch failed; Either No Execute feature (NX) not present or not enabled in BIOS.\r\n
0x0000002d | Hypervisor launch failed; at least one of the processors in the system is incompatible with the others.\r\n
0x0000002e | Hypervisor launch failed; Processor does not support the minimum features required to run the hypervisor (MSR index %1, allowed bits %2, required bits %3).\r\n
0x0000002f | Hypervisor launch failed; Processor does not provide the features necessary to run the hypervisor (BalStatus %1, leaf1 EAX %2, VMCR MS EAX %3, SVM CPUID features %4, has working SMM %5).\r\n
0x00000030 | Hypervisor launch failed; Processor does not provide the features necessary to run the hypervisor (leaf %1, register %2: features needed %3, features supported %4).\r\n
0x00000036 | Hypervisor launch failed; Hypervisor image does not match the platform being run on.\r\n
0x00000037 | Hypervisor launch failed; Required firmware table not found.\r\n
0x00000038 | Hypervisor launch failed; Encountered invalid firmware information.\r\n
0x00000039 | Hypervisor launch failed; Incompatible SVM features present.\r\n
0x0000003a | Hypervisor launch failed; Incompatible VMX features present.\r\n
0x0000003b | Hypervisor launch failed; Second Level Address Translation is required to launch the hypervisor.\r\n
0x0000003c | Hypervisor launch failed; Secure Mode Extensions have been enabled by the BIOS. Please disable Secure Mode Extensions in the BIOS to launch Hyper-V.\r\n
0x0000003d | Hypervisor launch failed; Minimum CPUID leaves required by the hypervisor are not supported on the system.\r\n
0x0000003e | Hypervisor launch failed; The physical address limit supported has been exceeded.\r\n
0x0000003f | Hypervisor launch failed; The hypervisor was unable to initialize successfully (phase %1), and was not started.  This initialization failure may be the result of a platform configuration or firmware issue.  Contact your system vendor for more information or updated firmware.\r\n
0x00000040 | Hypervisor launch failed; Too many runtime services memory ranges described by firmware.\r\n
0x00000050 | Hypervisor launch failed; The operating systems boot loader failed with error %1.\r\n
0x00000051 | Hypervisor launch failed; The operating system boot loader was unable to locate a required resource.\r\n
0x00000052 | Hypervisor launch failed; The operating system boot loader detected a persistent memory failure.\r\n
0x00000053 | Hypervisor launch failed; The operating system boot loader was unable to allocate sufficient memory to complete the operation.\r\n
0x00000054 | Hypervisor launch failed; The operating system boot loader was unable to allocate sufficient resources to complete the operation.\r\n
0x00000055 | Hypervisor launch failed; The operating system boot loader detected a memory map conflict.\r\n
0x00000060 | Hypervisor processor startup failed (APIC ID %1, status %2). Further processors in the system were not started.\r\n
0x00000061 | Hypervisor processor startup failed (APIC ID %1) due to CPUID feature validation error. Further processors in the system were not started. Leaf %2, register %3 feature mismatch: BSP has features %5; AP has features %4\r\n
0x00000081 | Hypervisor initialized I/O remapping.%n%nHardware present: %1%nHardware enabled: %2%nPolicy: %3%nEnabled features: %4%nInternal information: %5%nProblems: %6%nAdditional information: %7\r\n
0x00000082 | Hypervisor I/O remapping is forcibly enabled by policy (the hypervisoriommupolicy BCD option is set to enable). If the system exhibits instability or reduced performance, consider restoring the default policy.\r\n
0x00000090 | A device is operating with reduced performance because of a problem with the system BIOS.%n%nThe device is not reported under the scope of a unique I/O remapping unit.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000091 | A device will not work correctly because of a problem with the system BIOS.%n%nThe Requester IDs reported for the device overlap with those reported for another device.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000092 | A device will not work correctly because the hypervisor does not have enough resources.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000093 | A device will not work correctly because of a problem with the system BIOS.%n%nAn IOAPIC is not correctly reported.%n%nIOAPIC ID: %1\r\n
0x00000094 | A device could not be used by a child partition because of a limitation of the system hardware and BIOS.%n%nThe I/O remapping unit that controls the device does not have sufficient capabilities.%n%nDevice ID: %1%nI/O remapping unit base address: %2%nPartition ID: %3\r\n
0x00000095 | A device could not be used by a child partition because of a limitation of the system hardware and BIOS.%n%nThe device cannot be securely used by a child partition.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000096 | The image %1 could not be accessed (status %2).\r\n
0x00000097 | The image %1 could not be loaded (status %2).\r\n
0x00000098 | The image %1 could not be read (status %2).\r\n
0x00000099 | The image %1 failed code integrity checks, and cannot be used.\r\n
0x0000009a | Hypervisor failed to properly synchronize TSC across logical processors (Max delta: %1, Min delta: %2).\r\n
0x0000009c | Hypervisor configured mitigations for CVE-2018-3646 for virtual machines.%n%nProcessor not affected: %1%nProcessor family not affected: %2%nProcessor supports cache flush: %3%nHyperThreading enabled: %4%nParent hypervisor applies mitigations: %5%nMitigations disabled by bcdedit: %6%nMitigations enabled: %7%nCache flush needed: %8%n\r\n
0x0000009d | The hypervisor did not enable mitigations for CVE-2018-3646 for virtual machines because HyperThreading is enabled and the hypervisor core scheduler is not enabled. To enable mitigations for CVE-2018-3646 for virtual machines, enable the core scheduler by running "bcdedit /set hypervisorschedulertype core" from an elevated command prompt and reboot.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Hyper-V-Hypervisor\r\n
0x90000002 | System\r\n
0xb000000a | Hypervisor Eventlog creation failed!\r\n
0xb000000b | Hypervisor Eventlog deletion failed!\r\n
0xb0000027 | Hypervisor System Start Options!\r\n
0xb0002103 | Hyper-V failed creating a new partition (status %1)!\r\n
0xb0003106 | Hyper-V detected access to a restricted MSR (Msr: %1, IsWrite: %2, MsrValue: %3, AccessStatus: %4, Pc: %5, ImageBase: %6, ImageChecksum: %7, ImageTimestamp: %8, ImageName: %9).\r\n
0xb0004101 | Hyper-V successfully created a new partition (partition %1).\r\n
0xb0004102 | Hyper-V successfully deleted a partition (partition %1).\r\n

### 10.0.17763.504, 10.0.17763.557

Message identifier | Message string
--- | ---
0x00000001 | Hypervisor successfully started.\r\n
0x00000002 | Hypervisor scheduler type is %1.\r\n
0x00000003 | Hypervisor Eventlog for global system events could not be created!\r\n
0x00000005 | Hypervisor launch has been disabled through the hypervisorlaunchtype bcdedit setting.\r\n
0x0000000d | Hypervisor fails to start ETW tracing session.\r\n
0x00000014 | Hypervisor launch failed; sleep and hibernate could not be disabled (status %1).\r\n
0x0000001a | Hypervisor launch failed; the hypervisor boot loader's internal logic failed (BalStatus %1, sub-status %2).\r\n
0x0000001b | Hypervisor launch failed; the hypervisor boot loader was unable to allocate sufficient resources to perform the launch.\r\n
0x0000001c | Hypervisor launch failed; the hypervisor boot loader does not support the vendor of at least one of the processors in the system.\r\n
0x0000001d | Hypervisor launch failed; at least one of the processors in the system does not appear to support the features required by the hypervisor.  (leaf: %1, required features: %2, features available: %3)\r\n
0x0000001f | Hyper-V launch failed; the system does not appear to have a sufficient level of ACPI support to launch the hypervisor.\r\n
0x00000020 | Hypervisor launch failed; at least one of the processors in the system does not appear to provide a virtualization platform supported by the hypervisor.\r\n
0x00000021 | Hyper-V launch failed; the image %1 could not be accessed (status %2).\r\n
0x00000022 | Hyper-V launch failed; the image %1 could not be loaded (status %2).\r\n
0x00000023 | Hyper-V launch failed; the image %1 could not be read (status %2).\r\n
0x00000024 | Hypervisor launch failed; the image %1 failed code integrity checks, and cannot be used.\r\n
0x00000025 | Hypervisor launch failed; the image %1 does not contain the image description datastructures, and cannot be used.\r\n
0x00000026 | Hyper-V launch failed; at least one of the processors in the system was unable to launch the hypervisor (status %1).\r\n
0x00000028 | Hypervisor launch failed; the hypervisor image is revision %1, but the currently installed virtualization software only supports launching revision %2 hypervisor images.\r\n
0x00000029 | Hypervisor launch failed; Either VMX not present or not enabled in BIOS.\r\n
0x0000002a | Hypervisor launch failed; Either SVM not present or not enabled in BIOS.\r\n
0x0000002c | Hypervisor launch failed; Either No Execute feature (NX) not present or not enabled in BIOS.\r\n
0x0000002d | Hypervisor launch failed; at least one of the processors in the system is incompatible with the others.\r\n
0x0000002e | Hypervisor launch failed; Processor does not support the minimum features required to run the hypervisor (MSR index %1, allowed bits %2, required bits %3).\r\n
0x0000002f | Hypervisor launch failed; Processor does not provide the features necessary to run the hypervisor (BalStatus %1, leaf1 EAX %2, VMCR MS EAX %3, SVM CPUID features %4, has working SMM %5).\r\n
0x00000030 | Hypervisor launch failed; Processor does not provide the features necessary to run the hypervisor (leaf %1, register %2: features needed %3, features supported %4).\r\n
0x00000036 | Hypervisor launch failed; Hypervisor image does not match the platform being run on.\r\n
0x00000037 | Hypervisor launch failed; Required firmware table not found.\r\n
0x00000038 | Hypervisor launch failed; Encountered invalid firmware information.\r\n
0x00000039 | Hypervisor launch failed; Incompatible SVM features present.\r\n
0x0000003a | Hypervisor launch failed; Incompatible VMX features present.\r\n
0x0000003b | Hypervisor launch failed; Second Level Address Translation is required to launch the hypervisor.\r\n
0x0000003c | Hypervisor launch failed; Secure Mode Extensions have been enabled by the BIOS. Please disable Secure Mode Extensions in the BIOS to launch Hyper-V.\r\n
0x0000003d | Hypervisor launch failed; Minimum CPUID leaves required by the hypervisor are not supported on the system.\r\n
0x0000003e | Hypervisor launch failed; The physical address limit supported has been exceeded.\r\n
0x0000003f | Hypervisor launch failed; The hypervisor was unable to initialize successfully (phase %1), and was not started.  This initialization failure may be the result of a platform configuration or firmware issue.  Contact your system vendor for more information or updated firmware.\r\n
0x00000040 | Hypervisor launch failed; Too many runtime services memory ranges described by firmware.\r\n
0x00000050 | Hypervisor launch failed; The operating systems boot loader failed with error %1.\r\n
0x00000051 | Hypervisor launch failed; The operating system boot loader was unable to locate a required resource.\r\n
0x00000052 | Hypervisor launch failed; The operating system boot loader detected a persistent memory failure.\r\n
0x00000053 | Hypervisor launch failed; The operating system boot loader was unable to allocate sufficient memory to complete the operation.\r\n
0x00000054 | Hypervisor launch failed; The operating system boot loader was unable to allocate sufficient resources to complete the operation.\r\n
0x00000055 | Hypervisor launch failed; The operating system boot loader detected a memory map conflict.\r\n
0x00000060 | Hypervisor processor startup failed (APIC ID %1, status %2). Further processors in the system were not started.\r\n
0x00000061 | Hypervisor processor startup failed (APIC ID %1) due to CPUID feature validation error. Further processors in the system were not started. Leaf %2, register %3 feature mismatch: BSP has features %5; AP has features %4\r\n
0x00000081 | Hypervisor initialized I/O remapping.%n%nHardware present: %1%nHardware enabled: %2%nPolicy: %3%nEnabled features: %4%nInternal information: %5%nProblems: %6%nAdditional information: %7\r\n
0x00000082 | Hypervisor I/O remapping is forcibly enabled by policy (the hypervisoriommupolicy BCD option is set to enable). If the system exhibits instability or reduced performance, consider restoring the default policy.\r\n
0x00000090 | A device is operating with reduced performance because of a problem with the system BIOS.%n%nThe device is not reported under the scope of a unique I/O remapping unit.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000091 | A device will not work correctly because of a problem with the system BIOS.%n%nThe Requester IDs reported for the device overlap with those reported for another device.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000092 | A device will not work correctly because the hypervisor does not have enough resources.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000093 | A device will not work correctly because of a problem with the system BIOS.%n%nAn IOAPIC is not correctly reported.%n%nIOAPIC ID: %1\r\n
0x00000094 | A device could not be used by a child partition because of a limitation of the system hardware and BIOS.%n%nThe I/O remapping unit that controls the device does not have sufficient capabilities.%n%nDevice ID: %1%nI/O remapping unit base address: %2%nPartition ID: %3\r\n
0x00000095 | A device could not be used by a child partition because of a limitation of the system hardware and BIOS.%n%nThe device cannot be securely used by a child partition.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000096 | The image %1 could not be accessed (status %2).\r\n
0x00000097 | The image %1 could not be loaded (status %2).\r\n
0x00000098 | The image %1 could not be read (status %2).\r\n
0x00000099 | The image %1 failed code integrity checks, and cannot be used.\r\n
0x0000009a | Hypervisor failed to properly synchronize TSC across logical processors (Max delta: %1, Min delta: %2).\r\n
0x0000009c | Hypervisor configured mitigations for CVE-2018-3646 for virtual machines.%n%nProcessor not affected: %1%nProcessor family not affected: %2%nProcessor supports cache flush: %3%nHyperThreading enabled: %4%nParent hypervisor applies mitigations: %5%nMitigations disabled by bcdedit: %6%nMitigations enabled: %7%nCache flush needed: %8%n\r\n
0x0000009d | The hypervisor did not enable mitigations for CVE-2018-3646 for virtual machines because HyperThreading is enabled and the hypervisor core scheduler is not enabled. To enable mitigations for CVE-2018-3646 for virtual machines, enable the core scheduler by running "bcdedit /set hypervisorschedulertype core" from an elevated command prompt and reboot.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Hyper-V-Hypervisor\r\n
0x90000002 | System\r\n
0xb000000a | Hypervisor Eventlog creation failed!\r\n
0xb000000b | Hypervisor Eventlog deletion failed!\r\n
0xb0000027 | Hypervisor System Start Options!\r\n
0xb000009b | Host processor features mask: %1%n%nHost xsave features mask: %2%n%nHost cache line flush size: %3 bytes\r\n
0xb0002103 | Hyper-V failed creating a new partition (status %1)!\r\n
0xb0003106 | Hyper-V detected access to a restricted MSR (Msr: %1, IsWrite: %2, MsrValue: %3, AccessStatus: %4, Pc: %5, ImageBase: %6, ImageChecksum: %7, ImageTimestamp: %8, ImageName: %9).\r\n
0xb0004101 | Hyper-V successfully created a new partition (partition %1).\r\n
0xb0004102 | Hyper-V successfully deleted a partition (partition %1).\r\n

### 10.0.18362.1, 10.0.18362.752

Message identifier | Message string
--- | ---
0x00000001 | Hypervisor successfully started.\r\n
0x00000002 | Hypervisor scheduler type is %1.\r\n
0x00000003 | Hypervisor Eventlog for global system events could not be created!\r\n
0x00000005 | Hypervisor launch has been disabled through the hypervisorlaunchtype bcdedit setting.\r\n
0x0000000d | Hypervisor fails to start ETW tracing session.\r\n
0x00000014 | Hypervisor launch failed; sleep and hibernate could not be disabled (status %1).\r\n
0x0000001a | Hypervisor launch failed; the hypervisor boot loader's internal logic failed (BalStatus %1, sub-status %2).\r\n
0x0000001b | Hypervisor launch failed; the hypervisor boot loader was unable to allocate sufficient resources to perform the launch.\r\n
0x0000001c | Hypervisor launch failed; the hypervisor boot loader does not support the vendor of at least one of the processors in the system.\r\n
0x0000001f | Hyper-V launch failed; the system does not appear to have a sufficient level of ACPI support to launch the hypervisor.\r\n
0x00000020 | Hypervisor launch failed; at least one of the processors in the system does not appear to provide a virtualization platform supported by the hypervisor.\r\n
0x00000022 | Hyper-V launch failed; the image %1 could not be loaded (status %2).\r\n
0x00000024 | Hypervisor launch failed; the image %1 failed code integrity checks, and cannot be used.\r\n
0x00000025 | Hypervisor launch failed; the image %1 does not contain the image description datastructures, and cannot be used.\r\n
0x00000026 | Hyper-V launch failed; at least one of the processors in the system was unable to launch the hypervisor (status %1).\r\n
0x00000028 | Hypervisor launch failed; the hypervisor image is revision %1, but the currently installed virtualization software only supports launching revision %2 hypervisor images.\r\n
0x00000029 | Hypervisor launch failed; Either VMX not present or not enabled in BIOS.\r\n
0x0000002a | Hypervisor launch failed; Either SVM not present or not enabled in BIOS.\r\n
0x0000002c | Hypervisor launch failed; Either No Execute feature (NX) not present or not enabled in BIOS.\r\n
0x0000002e | Hypervisor launch failed; Processor does not support the minimum features required to run the hypervisor (MSR index %1, allowed bits %2, required bits %3).\r\n
0x00000030 | Hypervisor launch failed; Processor does not provide the features necessary to run the hypervisor (leaf %1, register %2: features needed %3, features supported %4).\r\n
0x00000036 | Hypervisor launch failed; Hypervisor image does not match the platform being run on.\r\n
0x00000037 | Hypervisor launch failed; Required firmware table not found.\r\n
0x00000038 | Hypervisor launch failed; Encountered invalid firmware information.\r\n
0x0000003b | Hypervisor launch failed; Second Level Address Translation is required to launch the hypervisor.\r\n
0x0000003c | Hypervisor launch failed; Secure Mode Extensions have been enabled by the BIOS. Please disable Secure Mode Extensions in the BIOS to launch Hyper-V.\r\n
0x0000003d | Hypervisor launch failed; Minimum CPUID leaves required by the hypervisor are not supported on the system.\r\n
0x0000003e | Hypervisor launch failed; The physical address limit supported has been exceeded.\r\n
0x0000003f | Hypervisor launch failed; The hypervisor was unable to initialize successfully (phase %1), and was not started.  This initialization failure may be the result of a platform configuration or firmware issue.  Contact your system vendor for more information or updated firmware.\r\n
0x00000040 | Hypervisor launch failed; Too many runtime services memory ranges described by firmware.\r\n
0x00000050 | Hypervisor launch failed; The operating systems boot loader failed with error %1.\r\n
0x00000051 | Hypervisor launch failed; The operating system boot loader was unable to locate a required resource.\r\n
0x00000052 | Hypervisor launch failed; The operating system boot loader detected a persistent memory failure.\r\n
0x00000053 | Hypervisor launch failed; The operating system boot loader was unable to allocate sufficient memory to complete the operation.\r\n
0x00000054 | Hypervisor launch failed; The operating system boot loader was unable to allocate sufficient resources to complete the operation.\r\n
0x00000055 | Hypervisor launch failed; The operating system boot loader detected a memory map conflict.\r\n
0x00000056 | Hypervisor launch failed; the version of the microcode update dll does not match the current operating system.\r\n
0x00000060 | Hypervisor processor startup failed (APIC ID %1, status %2). Further processors in the system were not started.\r\n
0x00000061 | Hypervisor processor startup failed (APIC ID %1) due to CPUID feature validation error. Further processors in the system were not started. Leaf %2, register %3 feature mismatch: BSP has features %5; AP has features %4\r\n
0x00000081 | Hypervisor initialized I/O remapping.%n%nHardware present: %1%nHardware enabled: %2%nPolicy: %3%nEnabled features: %4%nInternal information: %5%nProblems: %6%nAdditional information: %7\r\n
0x00000082 | Hypervisor I/O remapping is forcibly enabled by policy (the hypervisoriommupolicy BCD option is set to enable). If the system exhibits instability or reduced performance, consider restoring the default policy.\r\n
0x00000090 | A device is operating with reduced performance because of a problem with the system BIOS.%n%nThe device is not reported under the scope of a unique I/O remapping unit.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000091 | A device will not work correctly because of a problem with the system BIOS.%n%nThe Requester IDs reported for the device overlap with those reported for another device.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000092 | A device will not work correctly because the hypervisor does not have enough resources.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000093 | A device will not work correctly because of a problem with the system BIOS.%n%nAn IOAPIC is not correctly reported.%n%nIOAPIC ID: %1\r\n
0x00000094 | A device could not be used by a child partition because of a limitation of the system hardware and BIOS.%n%nThe I/O remapping unit that controls the device does not have sufficient capabilities.%n%nDevice ID: %1%nI/O remapping unit base address: %2%nPartition ID: %3\r\n
0x00000095 | A device could not be used by a child partition because of a limitation of the system hardware and BIOS.%n%nThe device cannot be securely used by a child partition.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000098 | The image %1 could not be read (status %2).\r\n
0x00000099 | The image %1 failed code integrity checks, and cannot be used.\r\n
0x0000009a | Hypervisor failed to properly synchronize TSC across logical processors (Max delta: %1, Min delta: %2).\r\n
0x0000009c | Hypervisor configured mitigations for CVE-2018-3646 for virtual machines.%n%nProcessor not affected: %1%nProcessor family not affected: %2%nProcessor supports cache flush: %3%nHyperThreading enabled: %4%nParent hypervisor applies mitigations: %5%nMitigations disabled by bcdedit: %6%nMitigations enabled: %7%nCache flush needed: %8%n\r\n
0x0000009d | The hypervisor did not enable mitigations for CVE-2018-3646 for virtual machines because HyperThreading is enabled and the hypervisor core scheduler is not enabled. To enable mitigations for CVE-2018-3646 for virtual machines, enable the core scheduler by running "bcdedit /set hypervisorschedulertype core" from an elevated command prompt and reboot.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Hyper-V-Hypervisor\r\n
0x90000002 | System\r\n
0xb000000a | Hypervisor Eventlog creation failed!\r\n
0xb000000b | Hypervisor Eventlog deletion failed!\r\n
0xb0000027 | Hypervisor Load Options - %1.\r\n
0xb000009b | Host processor features mask: %1%n%nHost xsave features mask: %2%n%nHost cache line flush size: %3 bytes\r\n
0xb0002103 | Hyper-V failed creating a new partition (status %1)!\r\n
0xb0003106 | Hyper-V detected access to a restricted MSR (Msr: %1, IsWrite: %2, MsrValue: %3, AccessStatus: %4, Pc: %5, ImageBase: %6, ImageChecksum: %7, ImageTimestamp: %8, ImageName: %9).\r\n
0xb0004101 | Hyper-V successfully created a new partition (partition %1).\r\n
0xb0004102 | Hyper-V successfully deleted a partition (partition %1).\r\n

### 10.0.19041.1, 10.0.19041.610

Message identifier | Message string
--- | ---
0x00000001 | Hypervisor successfully started.\r\n
0x00000002 | Hypervisor scheduler type is %1.\r\n
0x00000003 | Hypervisor Eventlog for global system events could not be created!\r\n
0x00000005 | Hypervisor launch has been disabled through the hypervisorlaunchtype bcdedit setting.\r\n
0x0000000d | Hypervisor fails to start ETW tracing session.\r\n
0x00000014 | Hypervisor launch failed; sleep and hibernate could not be disabled (status %1).\r\n
0x0000001a | Hypervisor launch failed; the hypervisor boot loader's internal logic failed (BalStatus %1, sub-status %2).\r\n
0x0000001b | Hypervisor launch failed; the hypervisor boot loader was unable to allocate sufficient resources to perform the launch.\r\n
0x0000001c | Hypervisor launch failed; the hypervisor boot loader does not support the vendor of at least one of the processors in the system.\r\n
0x0000001f | Hyper-V launch failed; the system does not appear to have a sufficient level of ACPI support to launch the hypervisor.\r\n
0x00000020 | Hypervisor launch failed; at least one of the processors in the system does not appear to provide a virtualization platform supported by the hypervisor.\r\n
0x00000022 | Hyper-V launch failed; the image %1 could not be loaded (status %2).\r\n
0x00000024 | Hypervisor launch failed; the image %1 failed code integrity checks, and cannot be used.\r\n
0x00000025 | Hypervisor launch failed; the image %1 does not contain the image description datastructures, and cannot be used.\r\n
0x00000026 | Hyper-V launch failed; at least one of the processors in the system was unable to launch the hypervisor (status %1).\r\n
0x00000028 | Hypervisor launch failed; the hypervisor image is revision %1, but the currently installed virtualization software only supports launching revision %2 hypervisor images.\r\n
0x00000029 | Hypervisor launch failed; Either VMX not present or not enabled in BIOS.\r\n
0x0000002a | Hypervisor launch failed; Either SVM not present or not enabled in BIOS.\r\n
0x0000002c | Hypervisor launch failed; Either No Execute feature (NX) not present or not enabled in BIOS.\r\n
0x0000002e | Hypervisor launch failed; Processor does not support the minimum features required to run the hypervisor (MSR index %1, allowed bits %2, required bits %3).\r\n
0x00000030 | Hypervisor launch failed; Processor does not provide the features necessary to run the hypervisor (leaf %1, register %2: features needed %3, features supported %4).\r\n
0x00000036 | Hypervisor launch failed; Hypervisor image does not match the platform being run on.\r\n
0x00000037 | Hypervisor launch failed; Required firmware table not found.\r\n
0x00000038 | Hypervisor launch failed; Encountered invalid firmware information.\r\n
0x0000003b | Hypervisor launch failed; Second Level Address Translation is required to launch the hypervisor.\r\n
0x0000003c | Hypervisor launch failed; Secure Mode Extensions have been enabled by the BIOS. Please disable Secure Mode Extensions in the BIOS to launch Hyper-V.\r\n
0x0000003d | Hypervisor launch failed; Minimum CPUID leaves required by the hypervisor are not supported on the system.\r\n
0x0000003e | Hypervisor launch failed; The physical address limit supported has been exceeded.\r\n
0x0000003f | Hypervisor launch failed; The hypervisor was unable to initialize successfully (phase %1), and was not started.  This initialization failure may be the result of a platform configuration or firmware issue.  Contact your system vendor for more information or updated firmware.\r\n
0x00000040 | Hypervisor launch failed; Too many runtime services memory ranges described by firmware.\r\n
0x00000050 | Hypervisor launch failed; The operating systems boot loader failed with error %1.\r\n
0x00000051 | Hypervisor launch failed; The operating system boot loader was unable to locate a required resource.\r\n
0x00000052 | Hypervisor launch failed; The operating system boot loader detected a persistent memory failure.\r\n
0x00000053 | Hypervisor launch failed; The operating system boot loader was unable to allocate sufficient memory to complete the operation.\r\n
0x00000054 | Hypervisor launch failed; The operating system boot loader was unable to allocate sufficient resources to complete the operation.\r\n
0x00000055 | Hypervisor launch failed; The operating system boot loader detected a memory map conflict.\r\n
0x00000056 | Hypervisor launch failed; the version of the microcode update dll does not match the current operating system.\r\n
0x00000060 | Hypervisor processor startup failed (APIC ID %1, status %2). Further processors in the system were not started.\r\n
0x00000061 | Hypervisor processor startup failed (APIC ID %1) due to CPUID feature validation error. Further processors in the system were not started. Leaf %2, register %3 feature mismatch: BSP has features %5; AP has features %4\r\n
0x00000081 | Hypervisor initialized I/O remapping.%n%nHardware present: %1%nHardware enabled: %2%nPolicy: %3%nEnabled features: %4%nInternal information: %5%nProblems: %6%nAdditional information: %7\r\n
0x00000082 | Hypervisor I/O remapping is forcibly enabled by policy (the hypervisoriommupolicy BCD option is set to enable). If the system exhibits instability or reduced performance, consider restoring the default policy.\r\n
0x00000090 | A device is operating with reduced performance because of a problem with the system BIOS.%n%nThe device is not reported under the scope of a unique I/O remapping unit.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000091 | A device will not work correctly because of a problem with the system BIOS.%n%nThe Requester IDs reported for the device overlap with those reported for another device.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000092 | A device will not work correctly because the hypervisor does not have enough resources.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000093 | A device will not work correctly because of a problem with the system BIOS.%n%nAn IOAPIC is not correctly reported.%n%nIOAPIC ID: %1\r\n
0x00000094 | A device could not be used by a child partition because of a limitation of the system hardware and BIOS.%n%nThe I/O remapping unit that controls the device does not have sufficient capabilities.%n%nDevice ID: %1%nI/O remapping unit base address: %2%nPartition ID: %3\r\n
0x00000095 | A device could not be used by a child partition because of a limitation of the system hardware and BIOS.%n%nThe device cannot be securely used by a child partition.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000098 | The image %1 could not be read (status %2).\r\n
0x00000099 | The image %1 failed code integrity checks, and cannot be used.\r\n
0x0000009a | Hypervisor failed to properly synchronize TSC across logical processors (Max delta: %1, Min delta: %2).\r\n
0x0000009d | The hypervisor did not enable mitigations for CVE-2018-3646 for virtual machines because HyperThreading is enabled and the hypervisor core scheduler is not enabled. To enable mitigations for CVE-2018-3646 for virtual machines, enable the core scheduler by running "bcdedit /set hypervisorschedulertype core" from an elevated command prompt and reboot.\r\n
0x0000009e | The queried interface version %1 is not supported (Min : %2, Max : %3).\r\n
0x0000009f | The queried interface is incomplete.\r\n
0x000000a0 | Partition persistence services will be unavailable.\r\n
0x000000a1 | The configured Minroot settings are not compatible with the hypervisor core scheduler and have been overriden. This may expose a different number of logical processors to the root partition.\r\n
0x000000a2 | Failed to unregister the remote hypercall interface (status %1).\r\n
0x000000a5 | Hypervisor configured mitigations for CVE-2019-11091, CVE-2018-12126, CVE-2018-12127, CVE-2018-12130 for virtual machines.%n%nProcessor not affected: %1%nProcessor family not affected: %2%nProcessor supports microarchitectural buffer flush: %3%nBuffer flush needed: %4%n\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Hyper-V-Hypervisor\r\n
0x90000002 | System\r\n
0xb000000a | Hypervisor Eventlog creation failed!\r\n
0xb000000b | Hypervisor Eventlog deletion failed!\r\n
0xb0000027 | Hypervisor Load Options - %1.\r\n
0xb000009b | Host processor features mask: %1%n%nHost xsave features mask: %2%n%nHost cache line flush size: %3 bytes\r\n
0xb000009c | Hypervisor configured mitigations for CVE-2018-3646 for virtual machines.%n%nProcessor not affected: %1%nProcessor family not affected: %2%nProcessor supports cache flush: %3%nHyperThreading enabled: %4%nParent hypervisor applies mitigations: %5%nMitigations disabled by bcdedit: %6%nMitigations enabled: %7%nCache flush needed: %8%n\r\n
0xb00000a3 | The hypervisor encountered an internal error: nested NMI (processor %1).\r\n
0xb00000a4 | The hypervisor encountered an internal error: IPI timeout (processor %1).\r\n
0xb0002103 | Hyper-V failed creating a new partition (status %1)!\r\n
0xb0003106 | Hyper-V detected access to a restricted MSR (Msr: %1, IsWrite: %2, MsrValue: %3, AccessStatus: %4, Pc: %5, ImageBase: %6, ImageChecksum: %7, ImageTimestamp: %8, ImageName: %9).\r\n
0xb0004101 | Hyper-V successfully created a new partition (partition %1).\r\n
0xb0004102 | Hyper-V successfully deleted a partition (partition %1).\r\n
0xb001009b | Host processor features mask: %2%n%nHost xsave features mask: %3%n%nHost cache line flush size: %4 bytes\r\n
0xb001009c | Hypervisor initial page allocation NUMA policy: %1\r\n
0xd0000001 | Connect IOCTL failed when registering interface.\r\n
0xd0000002 | Registering remote hypercall interface failed.\r\n
0xd0000003 | Library initialization failed when registering interface.\r\n
0xd0000004 | NUMA distribution disabled\r\n
0xd0000005 | Even NUMA distribution\r\n
0xd0000006 | Proportional NUMA distribution\r\n

### 10.0.22000.100

Message identifier | Message string
--- | ---
0x00000001 | Hypervisor successfully started.\r\n
0x00000002 | Hypervisor scheduler type is %1.\r\n
0x00000003 | Hypervisor Eventlog for global system events could not be created!\r\n
0x00000005 | Hypervisor launch has been disabled through the hypervisorlaunchtype bcdedit setting.\r\n
0x0000000d | Hypervisor fails to start ETW tracing session.\r\n
0x00000014 | Hypervisor launch failed; sleep and hibernate could not be disabled (status %1).\r\n
0x0000001a | Hypervisor launch failed; the hypervisor boot loader's internal logic failed (BalStatus %1, sub-status %2).\r\n
0x0000001b | Hypervisor launch failed; the hypervisor boot loader was unable to allocate sufficient resources to perform the launch.\r\n
0x0000001c | Hypervisor launch failed; the hypervisor boot loader does not support the vendor of at least one of the processors in the system.\r\n
0x0000001f | Hyper-V launch failed; the system does not appear to have a sufficient level of ACPI support to launch the hypervisor.\r\n
0x00000020 | Hypervisor launch failed; at least one of the processors in the system does not appear to provide a virtualization platform supported by the hypervisor.\r\n
0x00000022 | Hyper-V launch failed; the image %1 could not be loaded (status %2).\r\n
0x00000024 | Hypervisor launch failed; the image %1 failed code integrity checks, and cannot be used.\r\n
0x00000025 | Hypervisor launch failed; the image %1 does not contain the image description datastructures, and cannot be used.\r\n
0x00000026 | Hyper-V launch failed; at least one of the processors in the system was unable to launch the hypervisor (status %1).\r\n
0x00000028 | Hypervisor launch failed; the hypervisor image is revision %1, but the currently installed virtualization software only supports launching revision %2 hypervisor images.\r\n
0x00000029 | Hypervisor launch failed; Either VMX not present or not enabled in BIOS.\r\n
0x0000002a | Hypervisor launch failed; Either SVM not present or not enabled in BIOS.\r\n
0x0000002b | Hypervisor launch failed; EL2 not present.\r\n
0x0000002c | Hypervisor launch failed; Either No Execute feature (NX) not present or not enabled in BIOS.\r\n
0x0000002e | Hypervisor launch failed; Processor does not support the minimum features required to run the hypervisor (MSR index %1, allowed bits %2, required bits %3).\r\n
0x00000030 | Hypervisor launch failed; Processor does not provide the features necessary to run the hypervisor (leaf %1, register %2: features needed %3, features supported %4).\r\n
0x00000036 | Hypervisor launch failed; Hypervisor image does not match the platform being run on.\r\n
0x00000037 | Hypervisor launch failed; Required firmware table not found.\r\n
0x00000038 | Hypervisor launch failed; Encountered invalid firmware information.\r\n
0x0000003b | Hypervisor launch failed; Second Level Address Translation is required to launch the hypervisor.\r\n
0x0000003c | Hypervisor launch failed; Secure Mode Extensions have been enabled by the BIOS. Please disable Secure Mode Extensions in the BIOS to launch Hyper-V.\r\n
0x0000003d | Hypervisor launch failed; Minimum CPUID leaves required by the hypervisor are not supported on the system.\r\n
0x0000003e | Hypervisor launch failed; The physical address limit supported has been exceeded.\r\n
0x0000003f | Hypervisor launch failed; The hypervisor was unable to initialize successfully (phase %1), and was not started.  This initialization failure may be the result of a platform configuration or firmware issue.  Contact your system vendor for more information or updated firmware.\r\n
0x00000040 | Hypervisor launch failed; Too many runtime services memory ranges described by firmware.\r\n
0x00000050 | Hypervisor launch failed; The operating systems boot loader failed with error %1.\r\n
0x00000051 | Hypervisor launch failed; The operating system boot loader was unable to locate a required resource.\r\n
0x00000052 | Hypervisor launch failed; The operating system boot loader detected a persistent memory failure.\r\n
0x00000053 | Hypervisor launch failed; The operating system boot loader was unable to allocate sufficient memory to complete the operation.\r\n
0x00000054 | Hypervisor launch failed; The operating system boot loader was unable to allocate sufficient resources to complete the operation.\r\n
0x00000055 | Hypervisor launch failed; The operating system boot loader detected a memory map conflict.\r\n
0x00000056 | Hypervisor launch failed; the version of the microcode update dll does not match the current operating system.\r\n
0x00000060 | Hypervisor processor startup failed (APIC ID %1, status %2). Further processors in the system were not started.\r\n
0x00000061 | Hypervisor processor startup failed (APIC ID %1) due to CPUID feature validation error. Further processors in the system were not started. Leaf %2, register %3 feature mismatch: BSP has features %5; AP has features %4\r\n
0x00000081 | Hypervisor initialized I/O remapping.%n%nHardware present: %1%nHardware enabled: %2%nPolicy: %3%nEnabled features: %4%nInternal information: %5%nProblems: %6%nAdditional information: %7\r\n
0x00000082 | Hypervisor I/O remapping is forcibly enabled by policy (the hypervisoriommupolicy BCD option is set to enable). If the system exhibits instability or reduced performance, consider restoring the default policy.\r\n
0x00000083 | There is an I/O remapping problem with the sytem BIOS.%n%nProblems: %1\r\n
0x00000090 | A device is operating with reduced performance because of a problem with the system BIOS.%n%nThe device is not reported under the scope of a unique I/O remapping unit.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000091 | A device will not work correctly because of a problem with the system BIOS.%n%nThe Requester IDs reported for the device overlap with those reported for another device.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000092 | A device will not work correctly because the hypervisor does not have enough resources.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000093 | A device will not work correctly because of a problem with the system BIOS.%n%nAn IOAPIC is not correctly reported.%n%nIOAPIC ID: %1\r\n
0x00000094 | A device could not be used by a child partition because of a limitation of the system hardware and BIOS.%n%nThe I/O remapping unit that controls the device does not have sufficient capabilities.%n%nDevice ID: %1%nI/O remapping unit base address: %2%nPartition ID: %3\r\n
0x00000095 | A device could not be used by a child partition because of a limitation of the system hardware and BIOS.%n%nThe device cannot be securely used by a child partition.%n%nDevice ID: %1%nPartition ID: %2\r\n
0x00000098 | The image %1 could not be read (status %2).\r\n
0x00000099 | The image %1 failed code integrity checks, and cannot be used.\r\n
0x0000009a | Hypervisor failed to properly synchronize TSC across logical processors (Max delta: %1, Min delta: %2).\r\n
0x0000009d | The hypervisor did not enable mitigations for CVE-2018-3646, CVE-2019-11091, CVE-2018-12126, CVE-2018-12127, and CVE-2018-12130 for virtual machines because HyperThreading is enabled and the hypervisor core scheduler is not enabled. To enable mitigations for virtual machines, enable the core scheduler by running "bcdedit /set hypervisorschedulertype core" from an elevated command prompt and reboot.\r\n
0x0000009e | The queried interface version %1 is not supported (Min : %2, Max : %3).\r\n
0x0000009f | The queried interface is incomplete.\r\n
0x000000a0 | Partition persistence services will be unavailable.\r\n
0x000000a1 | The configured Minroot settings are not compatible with the hypervisor core scheduler and have been overriden. This may expose a different number of logical processors to the root partition.\r\n
0x000000a2 | Failed to unregister the remote hypercall interface (status %1).\r\n
0x000000a5 | Hypervisor configured mitigations for CVE-2019-11091, CVE-2018-12126, CVE-2018-12127, CVE-2018-12130 for virtual machines.%n%nProcessor not affected: %1%nProcessor family not affected: %2%nProcessor supports microarchitectural buffer flush: %3%nBuffer flush needed: %4%n\r\n
0x000000a7 | The hypervisor did not enable mitigations for CVE-2018-3646, CVE-2019-11091, CVE-2018-12126, CVE-2018-12127, and CVE-2018-12130 for virtual machines because HyperThreading is enabled. To enable mitigations for virtual machines, disable HyperThreading.\r\n
0x000000a8 | AMD PSP PCI device discovered. Segment: %1, bus: %2, device: %3, function: %4.\r\n
0x000000a9 | Secure firmware update status: %1.\r\n
0x000000aa | Secure firmware image invalid.\r\n
0x000000ab | Secure firmware version: %1.\r\n
0x000000ad | On the prior boot session, the root partition did not respond to the synthetic watchdog in time, triggering a hardware watchdog reboot.\r\n
0x30000000 | Info\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Hyper-V-Hypervisor\r\n
0x90000002 | System\r\n
0xb000000a | Hypervisor Eventlog creation failed!\r\n
0xb000000b | Hypervisor Eventlog deletion failed!\r\n
0xb000000e | Hypervisor Eventlog flush failed!\r\n
0xb0000027 | Hypervisor Load Options - %1.\r\n
0xb000009b | Host processor features mask: %1%n%nHost xsave features mask: %2%n%nHost cache line flush size: %3 bytes\r\n
0xb000009c | Hypervisor configured mitigations for CVE-2018-3646 for virtual machines.%n%nProcessor not affected: %1%nProcessor family not affected: %2%nProcessor supports cache flush: %3%nHyperThreading enabled: %4%nParent hypervisor applies mitigations: %5%nMitigations disabled by bcdedit: %6%nMitigations enabled: %7%nCache flush needed: %8%n\r\n
0xb00000a6 | Hypervisor Load Options are conflicting - %1, %2.\r\n
0xb00000ac | Features are enabled that require all processors be started. %1 of %2 processors currently running.\r\n
0xb0002103 | Hyper-V failed creating a new partition (status %1)!\r\n
0xb0003106 | Hyper-V detected access to a restricted MSR (Msr: %1, IsWrite: %2, MsrValue: %3, AccessStatus: %4, Pc: %5, ImageBase: %6, ImageChecksum: %7, ImageTimestamp: %8, ImageName: %9).\r\n
0xb0004101 | Hyper-V successfully created a new partition (partition %1).\r\n
0xb0004102 | Hyper-V successfully deleted a partition (partition %1).\r\n
0xb001009b | Host processor features mask: %2%n%nHost xsave features mask: %3%n%nHost cache line flush size: %4 bytes\r\n
0xb001009c | Hypervisor initial page allocation NUMA policy: %1\r\n
0xd0000001 | Connect IOCTL failed when registering interface.\r\n
0xd0000002 | Registering remote hypercall interface failed.\r\n
0xd0000003 | Library initialization failed when registering interface.\r\n
0xd0000004 | NUMA distribution disabled\r\n
0xd0000005 | Even NUMA distribution\r\n
0xd0000006 | Proportional NUMA distribution\r\n
