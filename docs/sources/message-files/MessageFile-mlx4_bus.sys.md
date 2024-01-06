## mlx4_bus.sys

Path: %SystemRoot%\System32\drivers\mlx4_bus.sys

### 4.4.13905.0

Message identifier | Message string
--- | ---
0x40080006 | %2 has got:%n\r\n   vendor_id      %t%3%n\r\n   device_id      %t%4%n\r\n   subvendor_id   %t%5%n\r\n   subsystem_id   %t%6%n\r\n   HW revision    %t%7%n\r\n   FW version     %t%8.%9.%10%n\r\n   HCA guid       %t%11:%12%n\r\n   port number    %t%13%n\r\n   req types      %t%14,%15%n\r\n   final types    %t%16,%17\r\n
0x4008000e | %2: Performing HCA restart ...\r\n
0x4008000f | %2: HCA restart finished. Notifying the clients ...\r\n
0x40080034 | Port Link Speed.%n\r\n%2: Port %3 is going to start with link speed of %4.%n\r\n
0x40080037 | %2: Ecn adapter attributes:%n\r\nEcnExpectVlanTagged = %3%n\r\nEcnExpectIpv6 = %4%n\r\nEcnCatchRateLimitEn = %5%n\r\nEcnMaxTimeBetweenCatches = %6%n\r\nEcnMinLosslessBufferForCatches = %7%n\r\nEcnMinLossyBufferForCatches = %8%n\r\n
0x40080038 | %2: Ecn RP attributes (1) for port %3:%n\r\nEcnForceRcTos = %4%n\r\nEcnForceUcTos = %5%n\r\nEcnCnpRecEn = %6%n\r\nEcnFastRise = %7%n\r\nEcnClampTgtRate = %8%n\r\nEcnClampTgtRateAfterTimeInc = %9%n\r\nEcnRpgTimeReset = %10%n\r\nEcnRpgByteReset = %11%n\r\nEcnRpgThreshold = %12%n\r\nEcnRpgMaxRate = %13%n\r\nEcnRpgAiRate = %14%n\r\nEcnRpgHaiRate = %15%n\r\nEcnAlphaToRateShift = %16%n\r\nEcnRpgMinDecFac = %17%n\r\n
0x40080039 | %2: Ecn RP attributes (2) for port %3:%n\r\nEcnRpgMinRate = %4%n\r\nEcnMaxTimeRise = %5%n\r\nEcnMaxByteRise = %6%n\r\nEcnAlphaToRateCoeff = %7%n\r\nEcnMarkedRatioMultiplier = %8%n\r\nEcnMarkedRatioShift = %9%n\r\nEcnRateToSetOnFirstCnp = %10%n\r\nEcnDceTcpG = %11%n\r\nEcnDceTcpRtt = %12%n\r\n
0x40080040 | %2: Ecn NP attributes for port %3:%n\r\nEcnNpRecEn = %4%n\r\nEcnCompnRateLimit = %5%n\r\nEcnNumInjector = %6%n\r\nEcnCnpTimer = %7%n\r\nEcnCnpDscp = %8%n\r\nEcnCnp802pPrio = %9%n\r\n
0x8008000a | Found PF (non-primary physical function) at '%2'.\r\n
0x80080013 | %2 failed on %3 with status %4.\r\n
0x80080014 | WdfDeviceOpenRegistryKey failed on opening SW (=driver) key for mlx4_bus with status %2.\r\n
0x80080015 | Port type registry value for device %2 contains invalid value (PortType = %3). Default value will be set.\r\n
0x80080018 | %2:%n \r\nProblem - The port was configured to use auto sensing for deciding the port type. The port #%3 failed to detect the port type automatically.%n\r\nImpact  - As a result the port is started as IB port (unless the port is ETH only). This may cause a connection problem if the other side is ETH port.%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nFor solving this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x80080019 | %2:%n \r\nProblem - The port was configured to use auto sensing for deciding the port type. The port #2 failed to detect the port type automatically.%n\r\nImpact  - Since the first port is configured to be ETH the second port is started as ETH port.  This may cause a connection problem if the other side is IB port%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nFor solving this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x8008001c | %2:%n \r\nProblem - The port was configured to use auto sensing to decide the port type.\tBoth ports were detected as Ethernet but RoCE was enabled only for port#2.%n\r\nThus creating an illegal ETH-RoCE port configuration. To resolve the problem, we have enabled RoCE on Port#1 as well.\r\n
0x8008001d | %2:%n \r\nProblem - FW sense command could not be run on port#%3. We recommend upgrading your FW image. For further details, please refer to the README file in the documentation folder.\r\n
0x8008001e | %2:%n \r\nProblem - The port was configured to use auto sensing for deciding the port type. The port #1 failed to detect the port type automatically.%n\r\nImpact  - Since the second port is configured to be IB the first port is started as IB port.  This may cause a connection problem if the other side is ETH port%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nFor solving this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x80080021 | %2:%n \r\nWarning - IB configuration on Multi Protocol is prohibited. Forcing port#%3 to be ETH. \r\n
0x80080023 | %2:%n \r\nWarning - RoCE configuration on Multi Protocol is prohibited. Forcing RoCE off.\r\n
0x80080025 | %2: The BUS driver started working in Legacy mode, which may affect network performance. This can be caused due to resource limitation.%n\r\n(CPUs: %3, HW EQs: %4, SW EQs: %5, Eternert EQs: %6).\r\n
0x80080026 | %2: The number of alloacted MSI-X vectors is less than required. As a result, multiple EQs will share the same MSI-X vectore. This may decrease network performance.%n\r\nThe number of requested MSI-X vectors is: %3 while the number of alloacted MSI-X vectors is: %4.\r\n
0x80080027 | %2: The requested port type for port %3 is unsupported on this HCA. The driver was configured to use the supported type.\r\n
0x80080031 | %2: SL change is unsupported on this HCA. QoS is partly operational.\r\n
0x80080032 | Too many IPs in-use for RRoCE.%n\r\n%2: RRoCE support only %3  IPs per port.%n\r\nPlease Reduce Number of IPs to use the new IPs.%n\r\n
0x80080033 | Failed To Set Ethernet Port Link Speed.%n\r\n%2: The driver failed to set the link speed of %3 to Port %4 error %5.%n\r\nThe driver will start with the default link speed.%n\r\n
0x80080035 | All ports must be configured either to RoCE or RRoCE.%n\r\nDisabling RoCE and enabling RRoCE for port %2.%n\r\n
0xc0080004 | %2 has started in non-operational mode. \r\n
0xc0080007 | %2: MAP_FA command failed with error %3.%n \r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc0080008 | %2: RUN_FW command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc0080009 | %2: QUERY_FW command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000b | %2: QUERY_DEV_CAP command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000c | QUERY_ADAPTER command failed with error %2.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000d | Too few QPs were requested (requested %2, reserved for FW %3).%n\r\nThe adapter card is non-functional.%n\r\nPlease increase the Registry LogNumQp parameter under HKLM\System\CurrentControlSet\Services\mlx4_bus\Parameters.\r\n
0xc0080010 | Are you using SRIOV-enabled firmware?\r\n
0xc0080011 | Failed to move location string '%2', status %3.\r\n
0xc0080012 | WdfDeviceAllocAndQueryProperty failed,  status %2.\r\n
0xc0080016 | %2: Only same port types supported on this HCA.%n \r\nPlease go to the Port Protocol UI, and change the port types to be Either as ETH or IB\r\n
0xc0080017 | %2: Your port type configuration has led to not supported port types configuration (eth,ib).%n\r\nIf you have connected the ports to Ethernet and InfiniBand switches please replace between the ports. \r\n
0xc008001f | Error, Allocating memory for device driver failed (memory size %3).%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc0080020 | Error, Allocating memory for device driver failed (memory size %3).%n\r\nThe miniport driver cannot start.%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc0080022 | %2:%n \r\nProblem - On port#%3 device capabilities indicate IB only, which is not supported on a multi protocol machine. \r\n
0xc0080024 | %2:Driver startup failed due to system call WdfDeviceAddQueryInterface function failure. Error=%3.\r\n
0xc0080028 | %2:Driver startup failed due to failure in creation of the child device, IB or ETH. Error=%3.\r\n
0xc0080029 | %2: Creation of %3 device failed. Error=%4.\r\n
0xc0080030 | %2: Execution of FW command failed.op %3, status %4, errno %5, token %6.\r\n
0xc0080036 | %2: Illegal ETH-IB/RoCE port configuration.%n\r\nPort#1 is configured as Ethernet without RoCE/RRoCE enabled.%n\r\nPort#2 is either configured as IB or configured as Ethernet with RoCE/RRoCE enabled.%n\r\nTo resolve the problem, either enable RoCE/RRoCE on Port#1 or use ETH on port#2.%n\r\n

### 4.91.10730.0

Message identifier | Message string
--- | ---
0x40080006 | %2 has got:%n\r\n   vendor_id      %t%3%n\r\n   device_id      %t%4%n\r\n   subvendor_id   %t%5%n\r\n   subsystem_id   %t%6%n\r\n   HW revision    %t%7%n\r\n   FW version     %t%8%n\r\n   HCA guid       %t%9:%10%n\r\n   port number    %t%11%n\r\n   req types      %t%12,%13%n\r\n   final types    %t%14,%15\r\n
0x4008000e | %2: Performing HCA restart ...\r\n
0x4008000f | %2: HCA restart finished. Notifying the clients ...\r\n
0x40080034 | Port Link Speed.%n\r\n%2: Port %3 is going to start with link speed of %4.%n\r\n
0x4008003b | %2: Ecn adapter attributes:%n\r\nEcnExpectVlanTagged = %3%n\r\nEcnExpectIpv6 = %4%n\r\nEcnCatchRateLimitEn = %5%n\r\nEcnMaxTimeBetweenCatches = %6%n\r\nEcnMinLosslessBufferForCatches = %7%n\r\nEcnMinLossyBufferForCatches = %8%n\r\n
0x4008003c | %2: Ecn RP attributes (1) for port %3:%n\r\nEcnForceRcTos = %4%n\r\nEcnForceUcTos = %5%n\r\nEcnCnpRecEn = %6%n\r\nEcnFastRise = %7%n\r\nEcnClampTgtRate = %8%n\r\nEcnClampTgtRateAfterTimeInc = %9%n\r\nEcnRpgTimeReset = %10%n\r\nEcnRpgByteReset = %11%n\r\nEcnRpgThreshold = %12%n\r\nEcnRpgMaxRate = %13%n\r\nEcnRpgAiRate = %14%n\r\nEcnRpgHaiRate = %15%n\r\nEcnAlphaToRateShift = %16%n\r\nEcnRpgMinDecFac = %17%n\r\n
0x4008003d | %2: Ecn RP attributes (2) for port %3:%n\r\nEcnRpgMinRate = %4%n\r\nEcnMaxTimeRise = %5%n\r\nEcnMaxByteRise = %6%n\r\nEcnAlphaToRateCoeff = %7%n\r\nEcnMarkedRatioMultiplier = %8%n\r\nEcnMarkedRatioShift = %9%n\r\nEcnRateToSetOnFirstCnp = %10%n\r\nEcnDceTcpG = %11%n\r\nEcnDceTcpRtt = %12%n\r\nEcnDceTcpRttDelay = %13%n\r\nEcnInitialAlphaValue = %14%n\r\nEcnSupportIBStandardCnp = %15%n\r\nEcnCoalesceCnpInRp = %16%n\r\n
0x4008003e | %2: Ecn NP attributes for port %3:%n\r\nEcnNpRecEn = %4%n\r\nEcnUseIBStandardCnp = %5%n\r\nEcnCompnRateLimit = %6%n\r\nEcnNumInjector = %7%n\r\nEcnCnpTimer = %8%n\r\nEcnCnpDscp = %9%n\r\nEcnCnp802pPrio = %10%n\r\nEcnNoCongestionCyclesToKeep = %11%n\r\n
0x40080042 | %2: Port %3 is an IB port.\r\n
0x40080043 | %2: Port %3 is an Ethernet port with RRoCE v1.5.\r\n
0x40080044 | %2: Port %3 is an Ethernet port with RRoCE v2.0 (dport=%4).\r\n
0x40080045 | %2: Port %3 is an Ethernet port with RoCE.\r\n
0x40080046 | %2: Port %3 is an Ethernet port only (RoCE/RRoCE disabled).\r\n
0x40080055 | %2: VF command execution in interrupt mode is not possible. Commands will be executed in polling mode.\r\n
0x40080056 | %2: Dropless mode entered on port %3.  Packets will not be dropped.\r\n
0x40080057 | %2: Dropless mode exited on port %3.  Drop mode entered; packets may now be dropped.\r\n
0x8008000a | Found PF (non-primary physical function) at '%2'.\r\n
0x80080013 | %2 failed on %3 with status %4.\r\n
0x80080014 | WdfDeviceOpenRegistryKey failed on opening SW (=driver) key for mlx4_bus with status %2.\r\n
0x80080015 | Port type registry value for device %2 contains invalid value (PortType = %3). Default value will be set.\r\n
0x80080018 | %2:%n\r\nProblem - The port was configured to use auto sensing for deciding the port type. Port %3 failed to detect the port type automatically.%n\r\nImpact  - As a result the port is being started as an IB port (unless the port is ETH only). This may cause a connection problem if the other side is an ETH port.%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nTo solve this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x80080019 | %2:%n\r\nProblem - The port was configured to use auto sensing for deciding the port type. Port 2 failed to detect the port type automatically.%n\r\nImpact  - Since the first port is configured to be ETH the second port is started as an ETH port.  This may cause a connection problem if the other side is an IB port.%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nTo solve this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x8008001d | %2:%n\r\nProblem - FW sense command could not be run on port %3. We recommend upgrading your FW image. For further details, please refer to the README file in the documentation folder.\r\n
0x8008001e | %2:%n\r\nProblem - The port was configured to use auto sensing for deciding the port type. Port 1 failed to detect the port type automatically.%n\r\nImpact  - Since the second port is configured to be IB the first port is started as an IB port.  This may cause a connection problem if the other side is an ETH port.%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nTo solve this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x80080021 | %2:%n\r\nWarning - IB configuration on Multi Protocol is prohibited. Forcing port %3 to be ETH.\r\n
0x80080023 | %2:%n\r\nWarning - RoCE configuration on Multi Protocol is prohibited. Forcing RoCE off.\r\n
0x80080025 | %2: The BUS driver started working in Legacy mode, which may affect network performance. This can be caused by a resource limitation.%n\r\n(CPUs: %3, HW EQs: %4, SW EQs: %5, Eternert EQs: %6).\r\n
0x80080026 | %2: The number of allocated MSI-X vectors is less than required. As a result, multiple EQs will share the same MSI-X vector. This may decrease network performance.%n\r\nThe number of requested MSI-X vectors is: %3 while the number of allocated MSI-X vectors is: %4.\r\n
0x80080027 | %2: The requested port type for port %3 is unsupported on this HCA. The driver was configured to use the supported type.\r\n
0x80080031 | %2: SL change is unsupported on this HCA. QoS is partly operational.\r\n
0x80080032 | Too many IPs in-use for RRoCE.%n\r\n%2: RRoCE supports only %3 IPs per port.%n\r\nPlease Reduce Number of IPs to use the new IPs.%n\r\n
0x80080033 | Failed To Set Ethernet Port Link Speed.%n\r\n%2: The driver failed to set a link speed of %3 on port %4. Error=%5.%n\r\nThe driver will start with the default link speed.%n\r\n
0x80080035 | %2: SRIOV was successfully enabled. Running in master mode.\r\n
0x80080036 | %2: SRIOV cannot be enabled. Running in single-function mode.\r\n
0x80080039 | %2: mstdump %3 was created after command timeout or fw fatal error.\r\n
0x8008003a | %2: Trace %3 was created.\r\n
0x8008003f | %2: RRoCE is not supported for ConnectX«-2 device; as a result, RRoCE is disabled and the NIC starts in RoCE mode. %n\r\nNOTE: If your environment contains a mix of different NIC types, you need to make sure that the whole environment is configured to use RoCE; %n\r\notherwise the traffic between the different NICs will not work.\r\n
0x80080040 | %2: %3 mode was requested, but it is not supported. The NIC starts in %4 mode. %n\r\nNOTE: If your environment contains mix of different NIC types, you need to make sure that the whole environment is configured to use the same RoCE mode, %n\r\notherwise the traffic between the different NICs does not work.\r\n
0x80080051 | %2: The link on port %3 is down. Bad cable was detected. Please replace the cable to continue working.\r\n
0x80080052 | %2: The link on port %3 is down. Unsupported cable was detected. Please replace the cable to continue working.\r\n
0x80080054 | %2: SR-IOV cannot be enabled. The device does not support SR-IOV in InfiniBand mode and cannot be used when one of the ports is configured to use InfiniBand.  In order to resolve this issue please set the port type of the HCA to Ethernet.  %nFor more details please refer to product user manual.\r\n
0x80080058 | %2: Delay drop timeout occured on port %3.  Drop mode entered; packets may now be dropped.\r\n
0x80080059 | %2: SR-IOV cannot be enabled. the device does not support SR-IOV in InfiniBand mode, it cannot be used when one of the ports is auto-sensed to be connected to InfiniBand switch. To resolve this issue please set the port type of the HCA to Ethernet or connect the port to an Ethernet switch.  %nFor further details please refer to product user manual.\r\n
0x8008005a | %2: bus: EQ 0x%x was stuck. We inserted DPC for polling it which was expected to solve the problem.\r\n
0x8008005d | %2: Cmd timeout. %3 eqn %4, cons_index %5,  type %6, subtype %7, owner %8,  token %9, status %10, out_param %11.\r\n
0xc0080004 | %2 has started in non-operational mode.\r\n
0xc0080007 | %2: MAP_FA command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc0080008 | %2: RUN_FW command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc0080009 | %2: QUERY_FW command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000b | %2: QUERY_DEV_CAP command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000c | QUERY_ADAPTER command failed with error %2.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000d | Too few QPs were requested (requested %2, reserved for FW %3).%n\r\nThe adapter card is non-functional.%n\r\nPlease increase the Registry LogNumQp parameter under HKLM\System\CurrentControlSet\Services\mlx4_bus\Parameters.\r\n
0xc0080010 | Are you using SRIOV-enabled firmware?\r\n
0xc0080011 | Failed to move location string '%2', status %3.\r\n
0xc0080012 | WdfDeviceAllocAndQueryProperty failed,  status %2.\r\n
0xc0080016 | %2: Only same port types supported on this HCA.%n\r\nPlease go to the Port Protocol UI, and change the port types to be either ETH or IB.\r\n
0xc0080017 | %2: Your port type configuration (eth,ib) is not supported.%n\r\nIf you have connected the ports to Ethernet and InfiniBand switches please switch the ports, connecting the Infiniband switch to port 1.\r\n
0xc008001f | Error, Allocating memory for device driver failed (memory size %3).%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc0080020 | Error, Allocating memory for device driver failed (memory size %3).%n\r\nThe miniport driver cannot start.%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc0080022 | %2:%n\r\nProblem - On port %3 device capabilities indicate IB only, which is not supported on a multi protocol machine.\r\n
0xc0080024 | %2:Driver startup failed due to system call WdfDeviceAddQueryInterface function failure. Error=%3.\r\n
0xc0080028 | %2:Driver startup failed due to failure in creation of the child device, IB or ETH. Error=%3.\r\n
0xc0080029 | %2: Creation of %3 device failed. Error=%4.\r\n
0xc0080030 | %2: Execution of FW command failed. op %3, status %4, errno %5, token %6.\r\n
0xc0080038 | %2: Illegal ETH-IB port configuration.%n\r\nPort 1 is configured as Ethernet without RoCE/RRoCE enabled.%n\r\nPort 2 is configured as IB.%n\r\nTo resolve the conflict, the driver enables RoCE on Port 1.%n\r\n
0xc0080047 | %2: Driver startup failed because %3.\r\n
0xc0080048 | %2: Driver startup failed because %3. (status %4)\r\n
0xc0080049 | %2: Driver startup failed because %3 could not be initialized.\r\n
0xc008004a | %2: Driver startup failed because the pci device with vendor id %3/device id %4 could not be found.\r\n
0xc008004b | %2: Driver startup failed because %3 bytes of memory could not be allocated for %4.%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc008004c | %2: Driver startup failed because the driver could not take ownership of the device after %3 tries.\r\n
0xc008004d | %2: Driver startup failed because of an unsupported feature:  %3.\r\n
0xc008004e | %2: Driver startup failed because slave is not allowed by customer or disallowed because IB is not supported by Flex10 slaves.%n\r\n(max_allowed_slaves %3, cur %4)\r\n
0xc008004f | %2: Driver startup failed because insufficient Event Queues (EQs) are available.%n\r\n(%d are required, %d are available)\r\n
0xc0080050 | %2: Driver startup failed because port %3 could not %4.\r\n
0xc0080053 | %2: SR-IOV cannot be enabled as an old firmware (%3) that does not supports SR-IOV is burned on the HCA. Please upgrade your firmware. %nFor more details please refer to product user manual.\r\n
0xc008005b | %2: CA GUID value received from hypervisor after reset is unexpected. To resolve the issue, please restart the %3 device.\r\nExpected CA GUID Value: %4, Received CA GUID Value: %5.\r\n
0xc008005c | %2: Failed to add extension to Eth hardware_id, status %3.\r\n

### 5.1.11548.0

Message identifier | Message string
--- | ---
0x40080006 | %2 has got:%n\r\n   vendor_id      %t%3%n\r\n   device_id      %t%4%n\r\n   subvendor_id   %t%5%n\r\n   subsystem_id   %t%6%n\r\n   HW revision    %t%7%n\r\n   FW version     %t%8%n\r\n   HCA guid       %t%9:%10%n\r\n   port number    %t%11%n\r\n   req types      %t%12,%13%n\r\n   final types    %t%14,%15\r\n
0x4008000e | %2: Performing HCA restart ...\r\n
0x4008000f | %2: HCA restart finished. Notifying the clients ...\r\n
0x4008003b | %2: Ecn adapter attributes:%n\r\nEcnExpectVlanTagged = %3%n\r\nEcnExpectIpv6 = %4%n\r\nEcnCatchRateLimitEn = %5%n\r\nEcnMaxTimeBetweenCatches = %6%n\r\nEcnMinLosslessBufferForCatches = %7%n\r\nEcnMinLossyBufferForCatches = %8%n\r\n
0x4008003c | %2: Ecn RP attributes (1) for port %3:%n\r\nEcnForceRcTos = %4%n\r\nEcnForceUcTos = %5%n\r\nEcnCnpRecEn = %6%n\r\nEcnFastRise = %7%n\r\nEcnClampTgtRate = %8%n\r\nEcnClampTgtRateAfterTimeInc = %9%n\r\nEcnRpgTimeReset = %10%n\r\nEcnRpgByteReset = %11%n\r\nEcnRpgThreshold = %12%n\r\nEcnRpgMaxRate = %13%n\r\nEcnRpgAiRate = %14%n\r\nEcnRpgHaiRate = %15%n\r\nEcnAlphaToRateShift = %16%n\r\nEcnRpgMinDecFac = %17%n\r\n
0x4008003d | %2: Ecn RP attributes (2) for port %3:%n\r\nEcnRpgMinRate = %4%n\r\nEcnMaxTimeRise = %5%n\r\nEcnMaxByteRise = %6%n\r\nEcnAlphaToRateCoeff = %7%n\r\nEcnMarkedRatioMultiplier = %8%n\r\nEcnMarkedRatioShift = %9%n\r\nEcnRateToSetOnFirstCnp = %10%n\r\nEcnDceTcpG = %11%n\r\nEcnDceTcpRtt = %12%n\r\nEcnDceTcpRttDelay = %13%n\r\nEcnInitialAlphaValue = %14%n\r\nEcnSupportIBStandardCnp = %15%n\r\nEcnCoalesceCnpInRp = %16%n\r\n
0x4008003e | %2: Ecn NP attributes for port %3:%n\r\nEcnNpRecEn = %4%n\r\nEcnUseIBStandardCnp = %5%n\r\nEcnCompnRateLimit = %6%n\r\nEcnNumInjector = %7%n\r\nEcnCnpTimer = %8%n\r\nEcnCnpDscp = %9%n\r\nEcnCnp802pPrio = %10%n\r\nEcnNoCongestionCyclesToKeep = %11%n\r\n
0x40080042 | %2: Port %3 is an IB port.\r\n
0x40080043 | %2: Port %3 is an Ethernet port with RRoCE v1.5.\r\n
0x40080044 | %2: Port %3 is an Ethernet port with RRoCE v2.0 (dport=%4).\r\n
0x40080045 | %2: Port %3 is an Ethernet port with RoCE.\r\n
0x40080046 | %2: Port %3 is an Ethernet port only (RoCE/RRoCE disabled).\r\n
0x40080055 | %2: VF command execution in interrupt mode is not possible. Commands will be executed in polling mode.\r\n
0x40080056 | %2: Dropless mode entered on port %3.  Packets will not be dropped.\r\n
0x40080057 | %2: Dropless mode exited on port %3.  Drop mode entered; packets may now be dropped.\r\n
0x40080074 | %2: file %3 was created due to port state change.\r\n
0x40080075 | %2: file %3 was created due to user request.\r\n
0x40080078 | %2: VF allowed TX ether types feature - the following ether types are the only allowed types (0xFFFFFFFF indicates that ether type is not set):%n\r\n%t1. %3%n\r\n%t2. %4%n\r\n%t3. %5%n\r\n%t4. %6%n\r\n%t5. %7%n\r\n%t6. %8%n\r\n%t7. %9%n\r\n%t8. %10%n\r\n
0x8008000a | Found PF (non-primary physical function) at '%2'.\r\n
0x80080013 | %2 failed on %3 with status %4.\r\n
0x80080014 | WdfDeviceOpenRegistryKey failed on opening SW (=driver) key for mlx4_bus with status %2.\r\n
0x80080015 | Port type registry value for device %2 contains invalid value (PortType = %3). Default value will be set.\r\n
0x80080018 | %2:%n\r\nProblem - The port was configured to use auto sensing for deciding the port type. Port %3 failed to detect the port type automatically.%n\r\nImpact  - As a result the port is being started as an IB port (unless the port is ETH only). This may cause a connection problem if the other side is an ETH port.%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nTo solve this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x80080019 | %2:%n\r\nProblem - The port was configured to use auto sensing for deciding the port type. Port 2 failed to detect the port type automatically.%n\r\nImpact  - Since the first port is configured to be ETH the second port is started as an ETH port.  This may cause a connection problem if the other side is an IB port.%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nTo solve this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x8008001d | %2:%n\r\nProblem - FW sense command could not be run on port %3. We recommend upgrading your FW image. For further details, please refer to the README file in the documentation folder.\r\n
0x8008001e | %2:%n\r\nProblem - The port was configured to use auto sensing for deciding the port type. Port 1 failed to detect the port type automatically.%n\r\nImpact  - Since the second port is configured to be IB the first port is started as an IB port.  This may cause a connection problem if the other side is an ETH port.%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nTo solve this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x80080021 | %2:%n\r\nWarning - IB configuration on Multi Protocol is prohibited. Forcing port %3 to be ETH.\r\n
0x80080023 | %2:%n\r\nWarning - RoCE configuration on Multi Protocol is prohibited. Forcing RoCE off.\r\n
0x80080025 | %2: The BUS driver started working in Legacy mode, which may affect network performance. This can be caused by a resource limitation.%n\r\n(CPUs: %3, HW EQs: %4, SW EQs: %5, Eternert EQs: %6).\r\n
0x80080026 | %2: The number of allocated MSI-X vectors is less than required. As a result, multiple EQs will share the same MSI-X vector. This may decrease network performance.%n\r\nThe number of requested MSI-X vectors is: %3 while the number of allocated MSI-X vectors is: %4.\r\n
0x80080027 | %2: The requested port type for port %3 is unsupported on this HCA. The driver was configured to use the supported type.\r\n
0x80080031 | %2: SL change is unsupported on this HCA. QoS is partly operational.\r\n
0x80080032 | Too many IPs in-use for RRoCE.%n\r\n%2: RRoCE supports only %3 IPs per port.%n\r\nPlease Reduce Number of IPs to use the new IPs.%n\r\n
0x80080035 | %2: SRIOV was successfully enabled. Running in master mode.\r\n
0x80080036 | %2: SRIOV cannot be enabled. Running in single-function mode.\r\n
0x8008003f | %2: RRoCE is not supported for ConnectX«-2 device; as a result, RRoCE is disabled and the NIC starts in RoCE mode. %n\r\nNOTE: If your environment contains a mix of different NIC types, you need to make sure that the whole environment is configured to use RoCE; %n\r\notherwise the traffic between the different NICs will not work.\r\n
0x80080040 | %2: %3 mode was requested, but it is not supported. The NIC starts in %4 mode. %n\r\nNOTE: If your environment contains mix of different NIC types, you need to make sure that the whole environment is configured to use the same RoCE mode, %n\r\notherwise the traffic between the different NICs does not work.\r\n
0x80080051 | %2: The link on port %3 is down. Bad cable was detected. Please replace the cable to continue working.\r\n
0x80080052 | %2: The link on port %3 is down. Unsupported cable was detected. Please replace the cable to continue working.\r\n
0x80080054 | %2: SR-IOV cannot be enabled. The device does not support SR-IOV in InfiniBand mode and cannot be used when one of the ports is configured to use InfiniBand.  In order to resolve this issue please set the port type of the HCA to Ethernet.  %nFor more details please refer to product user manual.\r\n
0x80080058 | %2: Delay drop timeout occured on port %3.  Drop mode entered; packets may now be dropped.\r\n
0x80080059 | %2: SR-IOV cannot be enabled. the device does not support SR-IOV in InfiniBand mode, it cannot be used when one of the ports is auto-sensed to be connected to InfiniBand switch. To resolve this issue please set the port type of the HCA to Ethernet or connect the port to an Ethernet switch.  %nFor further details please refer to product user manual.\r\n
0x8008005a | %2: bus: EQ 0x%x was stuck. We inserted DPC for polling it which was expected to solve the problem.\r\n
0x8008005d | %2: Cmd timeout. %3 eqn %4, cons_index %5,  type %6, subtype %7, owner %8,  token %9, status %10, out_param %11.\r\n
0x80080067 | %2: Port #%3 is configured to Ethernet. Since Ethernet is not supported in this device, it will automatically be configured to IB instead. Check PortType registry key.\r\n
0x80080068 | %2: Port #%3 is configured to IB. Since IB is not supported in this device, it will automatically be configured to Ethernet instead. Check PortType registry key.\r\n
0x80080076 | %2: VF allowed TX ether types feature is not supported by FW.%n\r\nPlease burn the last FW and restart the driver.\r\n
0x80080077 | %2: VF allowed TX ether types feature - %3 ether types requested but only %4 ether types are supported by FW.%n\r\nOnly the first %5 ether types will be set.\r\n
0x80080079 | %2: Virtual Function (VF) #%3 issued an invalid or out-of-sequence device-command (channel=%4, fragment=%5, cmd=%6, status=%7) - command blocked.%n\r\n%n\r\nTo prevent the guest VM from flooding the Event Log, this event will not be logged again from this VF until the host driver is restarted.\r\n
0xc0080004 | %2 has started in non-operational mode.\r\n
0xc0080007 | %2: MAP_FA command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc0080008 | %2: RUN_FW command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc0080009 | %2: QUERY_FW command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000b | %2: QUERY_DEV_CAP command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000c | QUERY_ADAPTER command failed with error %2.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000d | Too few QPs were requested (requested %2, reserved for FW %3).%n\r\nThe adapter card is non-functional.%n\r\nPlease increase the Registry LogNumQp parameter under HKLM\System\CurrentControlSet\Services\mlx4_bus\Parameters.\r\n
0xc0080010 | Are you using SRIOV-enabled firmware?\r\n
0xc0080011 | Failed to move location string '%2', status %3.\r\n
0xc0080012 | WdfDeviceAllocAndQueryProperty failed,  status %2.\r\n
0xc0080016 | %2: Only same port types supported on this HCA.%n\r\nPlease go to the Port Protocol UI, and change the port types to be either ETH or IB.\r\n
0xc0080017 | %2: Your port type configuration (eth,ib) is not supported.%n\r\nIf you have connected the ports to Ethernet and InfiniBand switches please switch the ports, connecting the Infiniband switch to port 1.\r\n
0xc008001f | Error, Allocating memory for device driver failed (memory size %3).%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc0080020 | Error, Allocating memory for device driver failed (memory size %3).%n\r\nThe miniport driver cannot start.%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc0080022 | %2:%n\r\nProblem - On port %3 device capabilities indicate IB only, which is not supported on a multi protocol machine.\r\n
0xc0080024 | %2:Driver startup failed due to system call WdfDeviceAddQueryInterface function failure. Error=%3.\r\n
0xc0080028 | %2:Driver startup failed due to failure in creation of the child device, IB or ETH. Error=%3.\r\n
0xc0080029 | %2: Creation of %3 device failed. Error=%4.\r\n
0xc0080030 | %2: Execution of FW command failed. op %3, status %4, errno %5, token %6.\r\n
0xc0080038 | %2: Illegal ETH-IB port configuration.%n\r\nPort 1 is configured as Ethernet without RoCE/RRoCE enabled.%n\r\nPort 2 is configured as IB.%n\r\nTo resolve the conflict, the driver enables RoCE on Port 1.%n\r\n
0xc0080047 | %2: Driver startup failed because %3.\r\n
0xc0080048 | %2: Driver startup failed because %3. (status %4)\r\n
0xc0080049 | %2: Driver startup failed because %3 could not be initialized.\r\n
0xc008004a | %2: Driver startup failed because the pci device with vendor id %3/device id %4 could not be found.\r\n
0xc008004b | %2: Driver startup failed because %3 bytes of memory could not be allocated for %4.%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc008004c | %2: Driver startup failed because the driver could not take ownership of the device after %3 tries.\r\n
0xc008004d | %2: Driver startup failed because of an unsupported feature:  %3.\r\n
0xc008004e | %2: Driver startup failed because slave is not allowed by customer or disallowed because IB is not supported by Flex10 slaves.%n\r\n(max_allowed_slaves %3, cur %4)\r\n
0xc008004f | %2: Driver startup failed because insufficient Event Queues (EQs) are available.%n\r\n(%d are required, %d are available)\r\n
0xc0080050 | %2: Driver startup failed because port %3 could not %4.\r\n
0xc0080053 | %2: SR-IOV cannot be enabled as an old firmware (%3) that does not supports SR-IOV is burned on the HCA. Please upgrade your firmware. %nFor more details please refer to product user manual.\r\n
0xc008005b | %2: CA GUID value received from hypervisor after reset is unexpected. To resolve the issue, please restart the %3 device.\r\nExpected CA GUID Value: %4, Received CA GUID Value: %5.\r\n
0xc008005c | %2: Failed to add extension to Eth hardware_id, status %3.\r\n
0xc008005e | %2: __check_mtt_before_free: MTT is already free, n_mtt %3, p_mtt %4, val %5.\r\n
0xc008005f | %2:__check_mtt_before_free: want release %2:%3, expected %4:%5, p_mtt %6.\r\n
0xc0080060 | %2: __check_mtt_before_write: MTT is already used, n_mtt %3, p_mtt %4, val %5.\r\n
0xc0080061 | %2: SRIOV can't be enabled due to error on PCI virtualization. Possible reason - the machine is not supporting SRIOV.\r\n
0xc0080070 | %2: file %3 was created due to fw fatal error.\r\n
0xc0080071 | %2: file %3 was created due to command timeout.\r\n
0xc0080072 | %2: file %3 was created due to EQ error.\r\n
0xc0080073 | %2: file %3 was created due to TXCQ error.\r\n

### 5.50.14643.0, 5.50.14695.0

Message identifier | Message string
--- | ---
0x10000001 | Sensor report\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x40080006 | %2 has got:%n\r\n   vendor_id      %t%3%n\r\n   device_id      %t%4%n\r\n   subvendor_id   %t%5%n\r\n   subsystem_id   %t%6%n\r\n   HW revision    %t%7%n\r\n   FW version     %t%8%n\r\n   SW version     %t%9%n\r\n   PSID           %t%10%n\r\n   HCA guid       %t%11:%12%n\r\n   port number    %t%13%n\r\n   req types      %t%14,%15%n\r\n   final types    %t%16,%17\r\n
0x4008003b | %2: Ecn adapter attributes:%n\r\nEcnExpectVlanTagged = %3%n\r\nEcnExpectIpv6 = %4%n\r\nEcnCatchRateLimitEn = %5%n\r\nEcnMinLosslessBufferForCatches = %6%n\r\nEcnMinLossyBufferForCatches = %7%n\r\nEcnTrapDisablePeriod = %8%n\r\nEcnTrapDisablePendingCnpThreshold = %9%n\r\n
0x4008003c | %2: Ecn RP attributes (1) for port %3 (%4):%n\r\nEcnForceRcTos = %5%n\r\nEcnForceUcTos = %6%n\r\nEcnCnpRecEn = %7%n\r\nEcnFastRise = %8%n\r\nEcnClampTgtRate = %9%n\r\nEcnClampTgtRateAfterTimeInc = %10%n\r\nEcnRpgTimeReset = %11%n\r\nEcnRpgByteReset = %12%n\r\nEcnRpgThreshold = %13%n\r\nEcnRpgMaxRate = %14%n\r\nEcnRpgAiRate = %15%n\r\nEcnRpgHaiRate = %16%n\r\nEcnAlphaToRateShift = %17%n\r\nEcnRpgMinDecFac = %18%n\r\nEcnEnable = %19%n\r\n
0x4008003d | %2: Ecn RP attributes (2) for port %3 (%4):%n\r\nEcnRpgMinRate = %5%n\r\nEcnMaxTimeRise = %6%n\r\nEcnMaxByteRise = %7%n\r\nEcnAlphaToRateCoeff = %8%n\r\nEcnMarkedRatioMultiplier = %9%n\r\nEcnMarkedRatioShift = %10%n\r\nEcnRateToSetOnFirstCnp = %11%n\r\nEcnDceTcpG = %12%n\r\nEcnDceTcpRtt = %13%n\r\nEcnDceTcpRttDelay = %14%n\r\nEcnInitialAlphaValue = %15%n\r\nEcnSupportIBStandardCnp = %16%n\r\nEcnCoalesceCnpInRp = %17%n\r\nEcnBurstSize = %18%n\r\nEcnPriorityEnable = %19%n\r\n
0x4008003e | %2: Ecn NP attributes for port %3 (%4):%n\r\nEcnNpRecEn = %5%n\r\nEcnUseIBStandardCnp = %6%n\r\nEcnCompnRateLimit = %7%n\r\nEcnNumInjector = %8%n\r\nEcnCnpTimer = %9%n\r\nEcnCnpDscp = %10%n\r\nEcnCnp802pPrio = %11%n\r\nEcnNoCongestionCyclesToKeep = %12%n\r\n
0x40080042 | %2: Port %3 is an IB port.\r\n
0x40080043 | %2: Port %3 is an Ethernet port with RRoCE v1.5.\r\n
0x40080044 | %2: Port %3 is an Ethernet port with RRoCE v2.0 (dport=%4).\r\n
0x40080045 | %2: Port %3 is an Ethernet port with RoCE.\r\n
0x40080046 | %2: Port %3 is an Ethernet port only (RoCE/RRoCE disabled).\r\n
0x40080055 | %2: VF command execution in interrupt mode is not possible. Commands will be executed in polling mode.\r\n
0x40080056 | %2: Dropless mode entered on port %3.  Packets will not be dropped.\r\n
0x40080057 | %2: Dropless mode exited on port %3.  Drop mode entered; packets may now be dropped.\r\n
0x40080065 | %2: RX Port bandwidth allocation ratio: %3:%4%n\r\n
0x40080066 | %2: Invalid RX Port bandwidth allocation ratio: %3:%4, default settings will be applied%n.\r\nFor valid combinations please refer to user manual.\r\n
0x40080074 | %2: file %3 was created due to port state change.\r\n
0x40080075 | %2: file %3 was created due to user request.\r\n
0x40080078 | %2: VF allowed TX ether types feature - the following ether types are the only allowed types (0xFFFFFFFF indicates that ether type is not set):%n\r\n%t1. %3%n\r\n%t2. %4%n\r\n%t3. %5%n\r\n%t4. %6%n\r\n%t5. %7%n\r\n%t6. %8%n\r\n%t7. %9%n\r\n%t8. %10%n\r\n
0x40080086 | %2: Dual port device was configured to work in single port mode.\r\n
0x40080087 | %2: FW was loaded successfully from FW Image File (%3)\r\n
0x40080088 | %2: FW image was successfully saved into a FW Image File (%3)\r\n
0x40080104 | %2: Device dynamic Registry configuration updated: %3 changed from %4 to %5.\r\n
0x40080110 | %2: HW Trap: EQ_ix %3 EQN %4 type %5 subtype %6 slave_id %7 dw0 %8 dw1 %9 dw2 %10 dw4 %11\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x80080003 | %2: Self Healing feature is disabled as it is not supported %3.\r\n
0x80080005 | %2: Self Healing - Bus device mode (recovery from Bus errors) was requested, but it is not supported, as the %3. The feature starts in Miniport mode (recovery only from Miniport errors).\r\n
0x8008000a | Found PF (non-primary physical function) at '%2'.\r\n
0x8008000e | %2: Failed to generate an event (0x%3) for slave %4 as eq 0x%5 is full.\r\n
0x80080013 | %2 failed on %3 with status %4.\r\n
0x80080014 | WdfDeviceOpenRegistryKey failed on opening SW (=driver) key for mlx4_bus with status %2.\r\n
0x80080015 | Port type registry value for device %2 contains invalid value (PortType = %3). Default value will be set.\r\n
0x80080018 | %2:%n\r\nProblem - The port was configured to use auto sensing for deciding the port type. Port %3 failed to detect the port type automatically.%n\r\nImpact  - As a result the port is being started as an IB port (unless the port is ETH only). This may cause a connection problem if the other side is an ETH port.%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nTo solve this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x80080019 | %2:%n\r\nProblem - The port was configured to use auto sensing for deciding the port type. Port 2 failed to detect the port type automatically.%n\r\nImpact  - Since the first port is configured to be ETH the second port is started as an ETH port.  This may cause a connection problem if the other side is an IB port.%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nTo solve this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x8008001d | %2:%n\r\nProblem - FW sense command could not be run on port %3. We recommend upgrading your FW image. For further details, please refer to the README file in the documentation folder.\r\n
0x8008001e | %2:%n\r\nProblem - The port was configured to use auto sensing for deciding the port type. Port 1 failed to detect the port type automatically.%n\r\nImpact  - Since the second port is configured to be IB the first port is started as an IB port.  This may cause a connection problem if the other side is an ETH port.%n\r\nReason and suggestion to fix - This problem may happen since the computer is connected back to back or the cable is unplugged.%n\r\nTo solve this issue connect the port to a switch or define the port type explicitly (IB or ETH) instead of auto.\r\n
0x80080021 | %2:%n\r\nWarning - IB configuration on Multi Protocol is prohibited. Forcing port %3 to be ETH.\r\n
0x80080023 | %2:%n\r\nWarning - RoCE configuration on Multi Protocol is prohibited. Forcing RoCE off.\r\n
0x80080025 | %2: The BUS driver started working in Legacy mode, which may affect network performance. This can be caused by a resource limitation.%n\r\n(CPUs: %3, HW EQs: %4, SW EQs: %5, Eternert EQs: %6).\r\n
0x80080026 | %2: The number of allocated MSI-X vectors is less than required. As a result, multiple EQs will share the same MSI-X vector. This may decrease network performance.%n\r\nThe number of requested MSI-X vectors is: %3 while the number of allocated MSI-X vectors is: %4.\r\n
0x80080027 | %2: The requested port type for port %3 is unsupported on this HCA. The driver was configured to use the supported type.\r\n
0x80080031 | %2: SL change is unsupported on this HCA. QoS is partly operational.\r\n
0x80080032 | Too many IPs in-use for RRoCE.%n\r\n%2: RRoCE supports only %3 IPs per port.%n\r\nPlease Reduce Number of IPs to use the new IPs.%n\r\n
0x80080035 | %2: SRIOV was successfully enabled. Running in master mode.\r\n
0x80080036 | %2: SRIOV cannot be enabled. Running in single-function mode.\r\n
0x8008003f | %2: RRoCE is not supported for ConnectX®-2 device; as a result, RRoCE is disabled and the NIC starts in RoCE mode. %n\r\nNOTE: If your environment contains a mix of different NIC types, you need to make sure that the whole environment is configured to use RoCE; %n\r\notherwise the traffic between the different NICs will not work.\r\n
0x80080040 | %2: %3 mode was requested, but it is not supported. The NIC starts in %4 mode. %n\r\nNOTE: If your environment contains mix of different NIC types, you need to make sure that the whole environment is configured to use the same RoCE mode, %n\r\notherwise the traffic between the different NICs does not work.\r\n
0x80080051 | %2: The link on port %3 is down. Bad cable was detected. Please replace the cable to continue working.\r\n
0x80080052 | %2: The link on port %3 is down. Unsupported cable was detected. Please replace the cable to continue working.\r\n
0x80080054 | %2: SR-IOV cannot be enabled. The device does not support SR-IOV in InfiniBand mode and cannot be used when one of the ports is configured to use InfiniBand.  In order to resolve this issue please set the port type of the HCA to Ethernet.  %nFor more details please refer to product user manual.\r\n
0x80080058 | %2: Delay drop timeout occured on port %3.  Drop mode entered; packets may now be dropped.\r\n
0x80080059 | %2: SR-IOV cannot be enabled. the device does not support SR-IOV in InfiniBand mode, it cannot be used when one of the ports is auto-sensed to be connected to InfiniBand switch. To resolve this issue please set the port type of the HCA to Ethernet or connect the port to an Ethernet switch.  %nFor further details please refer to product user manual.\r\n
0x8008005a | %2: bus: EQ 0x%3 was stuck. We inserted DPC for polling it which was expected to solve the problem.\r\n
0x8008005d | %2: Cmd timeout. %3 eqn %4, cons_index %5,  type %6, subtype %7, owner %8,  token %9, status %10, out_param %11.\r\n
0x80080067 | %2: Port #%3 is configured to Ethernet. Since Ethernet is not supported in this device, it will automatically be configured to IB instead. Check PortType registry key.\r\n
0x80080068 | %2: Although Port #%3 is configured as IB, the software sets it to Ethernet only. %n\r\nThis occurs when the Ethernet link is already up due to one of the following: BMC is enabled or the firmware version installed in not up-to-date.\r\n
0x80080076 | %2: VF allowed TX ether types feature is not supported by FW.%n\r\nPlease burn the last FW and restart the driver.\r\n
0x80080077 | %2: VF allowed TX ether types feature - %3 ether types requested but only %4 ether types are supported by FW.%n\r\nOnly the first %5 ether types will be set.\r\n
0x80080079 | %2: Virtual Function (VF) #%3 issued an invalid or out-of-sequence device-command (channel=%4, fragment=%5, cmd=%6, status=%7) - command blocked.%n\r\n
0x8008007a | %2: SR-IOV cannot be enabled because FW does not support SR-IOV.  In order to resolve this issue please re-burn FW, having added parameters related to SR-IOV support.\r\n
0x8008007b | %2: FW doesn't support Multi Protocol. Setting port %3 to IB.\r\n
0x8008007f | %2: Adjusting of QP1 for ECN Burst Control failed for port %3 with error %4.\r\n
0x80080080 | %2: RDMA is disabled as a part of the healing policy.%n\r\nFor more details, please refer to the Self-Healing section in the WinOF User Manual.\r\n
0x80080081 | %2: Illegal ETH-IB port configuration.%n\r\nPort 1 is configured as Ethernet without RoCE/RRoCE enabled.%n\r\nPort 2 is configured as IB.%n\r\nTo resolve the conflict, the driver enables RoCE on Port 1.%n\r\n
0x80080082 | %2: Illegal ETH-IB port configuration.%n\r\nPort 1 is configured as Ethernet without RoCE/RRoCE enabled.%n\r\nPort 2 is configured as AUTO.%n\r\nTo resolve the conflict, the driver enables RoCE on Port 2.%n\r\n
0x80080090 | Port type registry value for device %2 could not be modified to value (PortType = %3). Previous value will be set.\r\n
0x80080091 | Manual VF per port allocation (p1=%2, p2=%3) was auto-truncated to (p1=%4, p2=%5) to fit the max supported by the adapter (%6)\r\n
0x80080092 | %2:%n\r\nProblem - RDMA in VF: Temporary this facility is allowed only for one VF in VM. RDMA is disabled for this VF.\r\n
0x80080094 | %2: A VM (or the host) attempted to set one or more gids on a vf (%3) which were already in use by another vf.\r\n
0x80080098 | %2: MAP_ICM_AUX %3 CMPT %4 EQC %5 MTT %6 DMPT %7 QPC %8 AUXC %9 ALTC %10 RDMARC %11 CQC %12 SRQC %13 MCG %14.\r\n
0x80080099 | %2 will be unloaded while %3 applications are still active.\r\n
0x8008009c | %2: Lost interrupt was detected, inserting DPC to process EQE.%n\r\nEQE found on EQ index: %3%n\r\nNumber of ETH EQs: %4%n\r\nLast consumer index: 0x%5\r\n
0x80080100 | %2: dump was created at folder (%3) due to dump-me-now request.%n\r\n%tDump-me-now dumps are placed by default in folder %SystemRoot%\temp\Mlx4_Dump_Me_Now%n\r\n%tor folder that was set by registry keyword HKLM\SYSTEM\CurrentControlSet\Services\mlx4_bus\Parameters\DumpMeNowDirectory\r\n
0x80080102 | %2: Device dynamic Registry update initialization failure. Dynamic Registry parameters won't updated in run-time.\r\n
0x80080103 | %2: Device dynamic Registry configuration: %3 invalid value, refer to user manual for acceptable values.\r\n
0x80080105 | %2 has detected that the NIC resiliency feature is not supported by this firmware. It is recommended to update the firmware in order to prevent the system from hanging.%n\r\nFor more details, please refer to the WinOF User Manual.\r\n
0x80080106 | %2 has detected that the NIC resiliency feature is disabled. It is recommended to enable it in order to prevent the system from hanging.%n\r\nFor more details, please refer to the WinOF User Manual.\r\n
0x80080108 | %2: Device has been reset and is now dysfunctional. To activate it, restart the Bus driver.\r\n
0x8008010d | %2: ExtraVFsQuotas registry key value (%3) is greater than the ExtraVFsQuotasScale registry key value (%4). The ExtraVFsQuotas value will be set to %4.%n\r\nFor more details, please refer to the Mellanox WinOF User Manual.\r\n
0x8008010f | %2: Virtual Function (VF) #%3 issued an invalid or out-of-sequence device-command (channel=%4, fragment=%5, cmd=%6, status=%7) - command blocked.%n\r\n%n\r\nTo prevent the guest VM from flooding the Event Log, this event will not be logged again from this VF until the host driver is restarted.\r\n
0x80080111 | %2: %3 registry key value (0x%4) is insufficient for physical function (PF) and %5 virtual functions (VFs). The initialization of the PF or the VFs may fail as the configured limit of the resources is insufficient.\r\n
0x80080112 | %2: EXT_QP_MAX_RETRY_LIMIT/EXT_QP_MAX_RETRY_PERIOD registry keys were requested by user but FW does not support this feature. Please upgrade your firmware to support it.%n\r\nFor more details, please refer to WinOF User Manual.\r\n
0xb0007531 | Driver Loaded ID %1 version %2 status %3\r\n
0xb0007532 | Driver Unloaded ID %1\r\n
0xb0007533 | %5: Device Created, BDF %2:%3.%4\r\n
0xb0007534 | %5: Device Closed, BDF %2:%3.%4\r\n
0xb0007535 | Device %2:%3.%4.%5: Miniport reset simulation\r\n
0xb0007536 | Device %2:%3.%4.%5: %9 function %10: Firmware command timeout sensor detected an error\r\n
0xb0007537 | Device %2:%3.%4.%5: %9 function %10: Resource close firmware command failure sensor detected an error\r\n
0xb0007538 | Device %2:%3.%4.%5: %9 function %10: Post firmware command failure sensor detected an error\r\n
0xb0007539 | Device %2:%3.%4.%5: Lack of progress in HW for Ethernet driver send queues sensor detected an error\r\n
0xb000753a | Device %2:%3.%4.%5: Lack of progress in SW wait list for Ethernet driver send queues sensor detected an error\r\n
0xb000753b | Device %2:%3.%4.%5: Lack of progress in SW for Ethernet driver receive queues sensor detected an error\r\n
0xb000753c | Device %2:%3.%4.%5: Catastrophic error sensor detected an error\r\n
0xb000753d | Device %2:%3.%4.%5: VF communication channel error sensor detected an error\r\n
0xb000753e | Device %2:%3.%4.%5: Recoverable internal memory error sensor detected an error\r\n
0xb0007540 | Device %2:%3.%4.%5: PCI channel offline sensor detected an error\r\n
0xb0007541 | Device %2:%3.%4.%5: CQ error events sensor detected an error\r\n
0xb0007542 | Device %2:%3.%4.%5: SRQ error events sensor detected an error\r\n
0xb0007543 | Device %2:%3.%4.%5: RQP error events sensor detected an error\r\n
0xb0007544 | Device %2:%3.%4.%5: SQP error events sensor detected an error\r\n
0xb0007545 | Device %2:%3.%4.%5: Receive completion error sensor detected an error\r\n
0xb0007546 | Device %2:%3.%4.%5: Send completion error sensor detected an error\r\n
0xb0007547 | Device %2:%3.%4.%5: RSS configuration errors sensor detected an error\r\n
0xb0007548 | Device %2:%3.%4.%5: Packet filter configuration errors sensor detected an error\r\n
0xb0007549 | Device %2:%3.%4.%5: Miniport insufficient resources sensor detected an error\r\n
0xb000754a | Device %2:%3.%4.%5: Lack of progress in HW for special send RDMA queues (network management QPs) sensor detected an error\r\n
0xb000754b | Device %2:%3.%4.%5: Lack of progress in SW for special send RDMA queues (network management QPs) sensor detected an error\r\n
0xb000754c | Device %2:%3.%4.%5: Lack of progress in SW for special receive RDMA queues (network management QPs) sensor detected an error\r\n
0xb000754d | Device %2:%3.%4.%5: Lack of progress in SW for Ethernet driver send queues sensor detected an error\r\n
0xb000754e | Device %2:%3.%4.%5: Stalled receive queues sensor detected an error\r\n
0xb000754f | Device %2:%3.%4.%5: Hung send engine sensor detected an error\r\n
0xb0007550 | Device %2:%3.%4.%5: Firmware health check – unknown subtype of event sensor detected and error\r\n
0xc0080004 | %2 has started in non-operational mode.\r\n
0xc0080007 | %2: MAP_FA command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc0080008 | %2: RUN_FW command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc0080009 | %2: QUERY_FW command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000b | %2: QUERY_DEV_CAP command failed with error %3.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000c | QUERY_ADAPTER command failed with error %2.%n\r\nThe adapter card is non-functional.%n\r\nMost likely a FW problem.%n\r\nPlease burn the last FW and restart the mlx4_bus driver.\r\n
0xc008000d | Too few QPs were requested (requested %2, reserved for FW %3).%n\r\nThe adapter card is non-functional.%n\r\nPlease increase the Registry LogNumQp parameter under HKLM\System\CurrentControlSet\Services\mlx4_bus\Parameters.\r\n
0xc0080010 | Are you using SRIOV-enabled firmware?\r\n
0xc0080011 | Failed to move location string '%2', status %3.\r\n
0xc0080012 | WdfDeviceAllocAndQueryProperty failed,  status %2.\r\n
0xc0080016 | %2: Only same port types supported on this HCA.%n\r\nPlease go to the Port Protocol UI, and change the port types to be either ETH or IB.\r\n
0xc0080017 | %2: Your port type configuration (eth,ib) is not supported.%n\r\nIf you have connected the ports to Ethernet and InfiniBand switches please switch the ports, connecting the Infiniband switch to port 1.\r\n
0xc008001f | Error, Allocating memory for device driver failed (memory size %3).%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc0080020 | Error, Allocating memory for device driver failed (memory size %3).%n\r\nThe miniport driver cannot start.%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc0080022 | %2:%n\r\nProblem - On port %3 device capabilities indicate IB only, which is not supported on a multi protocol machine.\r\n
0xc0080024 | %2:Driver startup failed due to system call WdfDeviceAddQueryInterface function failure. Error=%3.\r\n
0xc0080028 | %2:Driver startup failed due to failure in creation of the child device, IB or ETH. Error=%3.\r\n
0xc0080029 | %2: Creation of %3 device failed. Error=%4.\r\n
0xc0080030 | %2: %3 FW command failed. op %4, status %5, errno %6, token %7, in_modifier %8, op_modifier %9, in_param %10.\r\n
0xc0080038 | %2: Illegal ETH-IB port configuration.%n\r\nPort 1 is configured as Ethernet without RoCE/RRoCE enabled.%n\r\nPort 2 is configured as IB.%n\r\nThe driver will fail.%n\r\nIf you insist on this configuration, configure it manually from Device Manager.%n\r\n
0xc0080047 | %2: Driver startup failed because %3.\r\n
0xc0080048 | %2: Driver startup failed because %3. (status %4)\r\n
0xc0080049 | %2: Driver startup failed because %3 could not be initialized.\r\n
0xc008004a | %2: Driver startup failed because the pci device with vendor id %3/device id %4 could not be found.\r\n
0xc008004b | %2: Driver startup failed because %3 bytes of memory could not be allocated for %4.%n\r\nEither close any running applications, or reboot your computer or add additional memory.\r\n
0xc008004c | %2: Driver startup failed because the driver could not take ownership of the device after %3 tries.\r\n
0xc008004d | %2: Driver startup failed because of an unsupported feature:  %3.\r\n
0xc008004e | %2: Driver startup failed because slave is not allowed by customer or disallowed because IB is not supported by Flex10 slaves.%n\r\n(max_allowed_slaves %3, cur %4)\r\n
0xc008004f | %2: Driver startup failed because insufficient Event Queues (EQs) are available.%n\r\n(%d are required, %d are available)\r\n
0xc0080050 | %2: Driver startup failed because port %3 could not %4.\r\n
0xc0080053 | %2: SR-IOV cannot be enabled as an old firmware (%3) that does not supports SR-IOV is burned on the HCA. Please upgrade your firmware. %nFor more details please refer to product user manual.\r\n
0xc008005c | %2: Failed to add extension to Eth hardware_id, status %3.\r\n
0xc008005e | %2: __check_mtt_before_free: MTT is already free, n_mtt %3, p_mtt %4, val %5.\r\n
0xc008005f | %2:__check_mtt_before_free: want release %2:%3, expected %4:%5, p_mtt %6.\r\n
0xc0080060 | %2: __check_mtt_before_write: MTT is already used, n_mtt %3, p_mtt %4, val %5.\r\n
0xc0080063 | %2: Failed to reserve QP Range for VF %3, Consider increasing LogNumQP. For more information, please refer to the Troubleshooting section in the User Manual.\r\n
0xc0080064 | %2: SR-IOV cannot be enabled due to an error in the PCI_VIRTUALIZATION_INTERFACE. Possible reason, the machine does not support SR-IOV.\r\n
0xc0080070 | %2: file %3 was created due to fw fatal error.\r\n
0xc0080071 | %2: file %3 was created due to command timeout.\r\n
0xc0080072 | %2: file %3 was created due to EQ error.\r\n
0xc0080073 | %2: file %3 was created due to TXCQ error.\r\n
0xc0080083 | Failed to install %1 performance counters. %2.\r\n
0xc0080084 | Failed to remove %1 performance counters. %2.\r\n
0xc0080085 | %2: Failed to set Eth port type for port %3  with roce_mode %4, error %5.\r\n
0xc0080089 | %2: Fast FW Load: %3\r\n
0xc008008a | %2: Self Healing - Ignores error that was reported by sensors 0x%3 as a result of reaching the maximum number of Self-Healing resets (%4). Please clear the counters of the Self-Healing feature.%n\r\nFor more details, please refer to WinOF User Manual.\r\n
0xc008008b | %2: Self Healing - Failed to activate the resiliency flow as a result of a SW reset failure, error=%3.%n\r\nThe error was reported by the sensors 0x%4.\r\n
0xc008008c | Restart %2 as a result of error that was reported by sensors 0x%3%n\r\nSelf healing state:%n\r\n%tRestarts count: %4%n\r\n
0xc008008d | Stopped %2 activity as a result of an error that was reported by sensors 0x%3.\r\n
0xc0080093 | %2: Can't get unloaded. %3 applications are still active.\r\n
0xc0080095 | Restart %2 as a result of error that was reported by sensors 0x%3%n\r\nSelf healing state:%n\r\n%tRestarts count: %4%n\r\n%tMax restarts count: %5%n\r\n
0xc0080096 | Stopped %2 activity as a result of exceeding the maximum amount of allowed restarts (%3).\r\n
0xc0080097 | %2: Failed to initialize self-healing mechanisim as a result of error %3.\r\n
0xc008009a | Restart %2 as a result of error that was reported by sensors 0x%3%n\r\nSelf healing state:%n\r\n%tRestarts count: %4%n\r\n%tRestart time: %5%n\r\n%tMax restarts count in time interval %6 seconds: %7%n\r\n
0xc008009b | Stopped %2 activity as a result of exceeding the maximum amount of allowed restarts (%3) in time interval of %4 seconds.\r\n
0xc0080101 | %2: Failed to create full dump me now.%n\r\n%tDump me now root directory: %3%n\r\n%tFailure: %4%n\r\n%tStatus: %5\r\n
0xc0080107 | %2: file %3 was created due to dump-me-now request.\r\n
0xc0080109 | %2: Self-Healing second tier policy was activated on Virtual Function (VF) #%3 with sensors #%4, and Bus driver restart is needed on the VF. Please restart the Bus driver.\r\n
0xc008010a | %2: Failed to create full dump me now.%n\r\n%tStatus: %3\r\n
0xc008010b | %2: QP was moved from error state to hibernation state.%n\r\nQP number: %3%n\r\nIs SQ: %4%n\r\nIs RQ: %5\r\n
0xc008010c | %2: A virtual function's QP was moved from error state to hibernation state.%n\r\nPort number: %3%n\r\nFunction id: %4%n\r\nQP number: %5%n\r\nIs SQ: %6%n\r\nIs RQ: %7\r\n
0xc008010e | %2: Command from Virtual Function (VF) #%3: was blocked as it failed to wait for the previous command to complete.\r\n
0xc0080113 | %2: %3 QPs were not released !!%n\r\n
0xd0000001 | Mlx4 OpenFabrics Windows\r\n
0xd0000002 | Mlx5 OpenFabrics Windows\r\n
0xd0000003 | None\r\n
0xd0000004 | IB\r\n
0xd0000005 | Ethernet\r\n
0xd0000006 | Auto\r\n
