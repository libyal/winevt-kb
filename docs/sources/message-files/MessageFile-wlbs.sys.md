## wlbs.sys

Path: %SystemRoot%\System32\drivers\wlbs.sys

### 5.2.3790.3959

Message identifier | Message string
--- | ---
0x40070001 | NLB Cluster %2 %1: %3. %4 \r\n
0x40070004 | NLB Cluster %2 %1: %3 started. %4 \r\n
0x40070005 | NLB Cluster %2 %1: Cluster mode started with host ID %3. %4 \r\n
0x40070006 | NLB Cluster %2 %1: Cluster mode stopped. %3 %4 \r\n
0x40070017 | NLB Cluster %2 %1: Enabled traffic handling for rule containing port %3. %4 \r\n
0x40070018 | NLB Cluster %2 %1: Disabled ALL traffic handling for rule containing port %3. %4 \r\n
0x4007001b | NLB Cluster %2 %1: Host %3 is converging with host(s) %4 as part of the cluster.\r\n
0x4007001c | NLB Cluster %2 %1: Host %3 converged with host(s) %4 as part of the cluster.\r\n
0x4007001d | NLB Cluster %2 %1: Host %3 converged as DEFAULT host with host(s) %4 as part of the cluster.\r\n
0x40070024 | NLB Cluster %2 %1: Registry parameters successfully reloaded. %3 %4 \r\n
0x40070026 | NLB Cluster %2 %1: Adjusted traffic handling for rule containing port %3. %4 \r\n
0x40070027 | NLB Cluster %2 %1: Disabled NEW traffic handling for rule containing port %3. %4 \r\n
0x40070028 | NLB Cluster %2 %1: Adjusted traffic handling for all port rules. %3 %4 \r\n
0x40070029 | NLB Cluster %2 %1: Disabled NEW traffic handling for all port rules. %3 %4 \r\n
0x4007002a | NLB Cluster %2 %1: Enabled traffic handling for all port rules. %3 %4 \r\n
0x4007002b | NLB Cluster %2 %1: Disabled ALL traffic handling for all port rules. %3 %4 \r\n
0x4007002c | NLB Cluster %2 %1: Connection draining started. %3 %4 \r\n
0x4007002d | NLB Cluster %2 %1: Connection draining interrupted. %3 %4 \r\n
0x4007002e | NLB Cluster %2 %1: %3 remote control request received from %4. \r\n
0x4007002f | NLB Cluster %2 %1: Cluster mode control resumed. %3 %4 \r\n
0x40070030 | NLB Cluster %2 %1: Cluster mode control suspended. %3 %4 \r\n
0x40070034 | NLB Cluster %2 %1: Registry parameters successfully reloaded without resetting the driver. %3 %4 \r\n
0x4007003a | NLB Cluster %2 %1: Consistent bi-directional affinity (BDA) teaming configuration detected again.  The team in which this cluster participates has been re-activated. %3 %4 \r\n
0x4007003d | NLB Cluster %2 %1: This cluster has joined a bi-directional affinity (BDA) team as the designated master.  If the rest of the team has been consistently configured, the team will be activated. %3 %4 \r\n
0x4007003f | NLB Cluster %2 %1: Initiating convergence on host %3.  Reason: Host %4 is joining the cluster. \r\n
0x40070040 | NLB Cluster %2 %1: Initiating convergence on host %3.  Reason: Host %4 has conflicting configuration. \r\n
0x40070041 | NLB Cluster %2 %1: Initiating convergence on host %3.  Reason: Host %4 is converging for an unknown reason. \r\n
0x40070042 | NLB Cluster %2 %1: Initiating convergence on host %3.  Reason: Host %4 is configured with the same host ID. \r\n
0x40070043 | NLB Cluster %2 %1: Initiating convergence on host %3.  Reason: Host %4 is configured with a conflicting number of port rules. \r\n
0x40070044 | NLB Cluster %2 %1: Initiating convergence on host %3.  Reason: Host %4 has changed its port rule configuration. \r\n
0x40070045 | NLB Cluster %2 %1: Initiating convergence on host %3.  Reason: Host %4 is leaving the cluster.\r\n
0x40070046 | NLB Cluster %2 %1: Host %3 is converging with %4 host(s) as part of the cluster.  Note: The list of cluster members was too large to fit in this event log - see the first data dump entry for a binary map of the cluster membership or run 'wlbs query' to see a list of cluster members.\r\n
0x40070047 | NLB Cluster %2 %1: Host %3 converged with %4 host(s) as part of the cluster.  Note: The list of cluster members was too large to fit in this event log - see the first data dump entry for a binary map of the cluster membership or run 'wlbs query' to see a list of cluster members.\r\n
0x40070048 | NLB Cluster %2 %1: Host %3 converged as DEFAULT host with %4 host(s) as part of the cluster.  Note: The list of cluster members was too large to fit in this event log - see the first data dump entry for a binary map of the cluster membership or run 'wlbs query' to see a list of cluster members.\r\n
0x4007004b | NLB Cluster %2 %1: Current NLB host state successfully updated in the registry.\r\n
0x4007004d | NLB Cluster %2 %1: This host is configured to persist 'Started' states across reboots.  Because the last known state of this host was started, the host will be re-started regardless of the user-specified preferred initial host state.  To stop the host, use 'wlbs stop' or 'wlbs suspend'. %3 %4\r\n
0x4007004e | NLB Cluster %2 %1: This host is configured to persist 'Stopped' states across reboots.  Because the last known state of this host was stopped, the host will remain stopped regardless of the user-specified preferred initial host state.  To start the host, use 'wlbs start'. %3 %4\r\n
0x4007004f | NLB Cluster %2 %1: This host is configured to persist 'Suspended' states across reboots.  Because the last known state of this host was suspended, the host will remain suspended regardless of the user-specified preferred initial host state.  To start the host, use 'wlbs resume' followed by 'wlbs start'. %3 %4\r\n
0x80070002 | NLB Cluster %2 %1: %3. %4 \r\n
0x8007000d | NLB Cluster %2 %1: Driver temporarily ran out of resources.  Increase the %3 value under HKLM\SYSTEM\CurrentControlSet\Services\WLBS\Parameters\{GUID} key in the registry. %4 \r\n
0x8007000f | NLB Cluster %2 %1: Dedicated IP address %3 is invalid.  The driver will proceed assuming that there is no dedicated IP address.  Please check the NLB configuration and make sure that the dedicated IP address consists of four decimal byte values separated by dots. %4 \r\n
0x80070012 | NLB Cluster %2 %1: Duplicate cluster subnets detected.  The network may have been inadvertently partitioned. %3 %4 \r\n
0x80070013 | NLB Cluster %2 %1: Could not allocate additional connection descriptors.  Increase the %3 value under HKLM\SYSTEM\CurrentControlSet\Services\WLBS\Parameters\{GUID} key in the registry. %4 \r\n
0x80070016 | NLB Cluster %2 %1: There are more port rules defined than you are licensed to use.  Some rules will be disabled.  Please check the NLB configuration to ensure that you are using the proper number of rules. %3 %4 \r\n
0x80070019 | NLB Cluster %2 %1: Port %3 not found in any of the valid port rules. %4 \r\n
0x8007001a | NLB Cluster %2 %1: Port rules cannot be enabled/disabled while cluster operations are stopped. %3 %4 \r\n
0x8007001e | NLB Cluster %2 %1: Dedicated network mask %3 is invalid.  The driver will ignore the dedicated IP address and network mask.  Please check the NLB configuration and make sure that the dedicated network mask consists of four decimal byte values separated by dots. %4 \r\n
0x80070020 | NLB Cluster %2 %1: Both the dedicated IP address and network mask must be specified.  The driver will ignore the dedicated IP address and network mask. %3 %4 \r\n
0x80070021 | NLB Cluster %2 %1: Remote control request rejected from %3 due to an incorrect password. %4\r\n
0x80070025 | NLB Cluster %2 %1: Version mismatch between the driver and control programs.  Please make sure that you are running the same version of all NLB components. %3 %4 \r\n
0x80070036 | NLB Cluster %2 %1: Host %3 MAY be a Windows 2000 or NT 4.0 host participating in a cluster utilizing virtual cluster support.  Virtual Clusters are only supported in a homogeneous Windows Server 2003 cluster. %4\r\n
0x8007003c | NLB Cluster %2 %1: The bi-directional affinity (BDA) team in which this cluster participates has no designated master.  The team is inactive and will remain inactive until a master for the team is designated and consistent BDA teaming configuration is detected. %3 %4 \r\n
0x8007003e | NLB Cluster %2 %1: This cluster has left a bi-directional affinity (BDA) team in which it was the designated master.  If other adapters are still participating in the team, the team will be marked inactive and will remain inactive until a master for the team is designated and consistent BDA teaming configuration is detected. %3 %4 \r\n
0x8007004a | NLB Cluster %2 %1: Unable to update the NLB host state in the registry.  This will affect the ability of NLB to persist the current state across a reboot if NLB has been configured to do so.  To predict the state of NLB at the next reboot, please delete the HKLM\SYSTEM\CurrentControlSet\Services\WLBS\Parameters\{GUID}\%3 registry value, which will cause the state at the next reboot to revert to the user-specified preferred initial host state. %4\r\n
0x8007004c | NLB Cluster %2 %1: Last known NLB host state not found in the registry.  The state of this host will revert to the user-specified preferred initial host state. %3 %4\r\n
0x80070050 | NLB Cluster %2 %1: Windows 2000 or NT 4.0 host(s) are participating in this cluster.  Consult the relevant NLB documentation concerning the potential limitations of operating a mixed cluster. %3 %4\r\n
0x80070051 | NLB Cluster %2 %1: NLB was unable to open the TCP connection callback object and will therefore be unable to track TCP connections. %3 %4\r\n
0x80070054 | NLB Cluster %2 %1: NLB was unable to open the NLB public connection callback object and will therefore be unable to track connections. %3 %4\r\n
0xc0070003 | NLB Cluster %2 %1: %3. %4 \r\n
0xc0070007 | NLB Cluster %2 %1: Internal error.  Please contact technical support. %3 %4 \r\n
0xc0070008 | NLB Cluster %2 %1: Error registering driver with NDIS. %3 %4 \r\n
0xc0070009 | NLB Cluster %2 %1: Driver does not support the media type that was requested by TCP/IP.  NLB will not bind to this adapter.  %3 %4 \r\n
0xc007000a | NLB Cluster %2 %1: Driver could not allocate a required memory pool. %3 %4 \r\n
0xc007000b | NLB Cluster %2 %1: Driver could not open device \DEVICE\%3. %4 \r\n
0xc007000c | NLB Cluster %2 %1: Driver could not announce virtual NIC \DEVICE\%3 to TCP/IP. %4 \r\n
0xc007000e | NLB Cluster %2 %1: Cluster network address %3 is invalid.  Please check the NLB configuration and make sure that the cluster network address consists of six hexadecimal byte values separated by dashes. %4 \r\n
0xc0070010 | NLB Cluster %2 %1: Cluster IP address %3 is invalid.  Please check the NLB configuration and make sure that the cluster IP address consists of four decimal byte values separated by dots. %4 \r\n
0xc0070011 | NLB Cluster %2 %1: Duplicate host priority %3 was discovered on the network.  Please check the NLB configuration on all hosts that belong to the cluster and make sure that they all contain unique host priorities between 1 and 32. %4 \r\n
0xc0070014 | NLB Cluster %2 %1: Port rules with duplicate single host priority %3 detected on the network.  Please check the NLB configuration on all hosts that belong to the cluster and make sure that they do not contain single host rules with duplicate priorities for the same port range. %4 \r\n
0xc0070015 | NLB Cluster %2 %1: Host %3 does not have the same number or type of port rules as this host.  Please check the NLB configuration on all hosts that belong to the cluster and make sure that they all contain the same number and type of port rules. %4 \r\n
0xc007001f | NLB Cluster %2 %1: Cluster network mask %3 is invalid.  Please check the NLB configuration and make sure that the cluster network mask consists of four decimal byte values separated by dots. %4 \r\n
0xc0070022 | NLB Cluster %2 %1: Error querying parameters from the registry key \HKLM\SYSTEM\CurrentControlSet\Services\WLBS\Parameters\%3.  Please fix the NLB configuration and run 'wlbs reload' followed by 'wlbs start'. %4 \r\n
0xc0070023 | NLB Cluster %2 %1: Cluster mode cannot be enabled due to parameter errors.  All traffic will be passed through to TCP/IP.  Restart cluster operations after fixing the problem by running 'wlbs reload' followed by 'wlbs start'. %3 %4 \r\n
0xc0070031 | NLB Cluster %2 %1: Network Load Balancing can only be installed on systems running Windows Server 2003. %3 %4 \r\n
0xc0070032 | NLB Cluster %2 %1: Cannot add cluster MAC address.  The maximum number of multicast MAC addresses are already assigned to the NIC. %3 %4 \r\n
0xc0070033 | NLB Cluster %2 %1: Cannot bind NLB to this adapter due to memory allocation failure. %3 %4 \r\n
0xc0070035 | NLB Cluster %2 %1: The adapter to which NLB is bound does not support dynamically changing the MAC address.  NLB will not bind to this adapter. %3 %4 \r\n
0xc0070037 | NLB Cluster %2 %1: Inconsistent bi-directional affinity (BDA) teaming configuration detected on host %3.  The team in which this cluster participates will be marked inactive and this cluster will remain in the converging state until consistent teaming configuration is detected. %4 \r\n
0xc0070038 | NLB Cluster %2 %1: Invalid bi-directional affinity (BDA) team ID detected.  Team IDs must be a GUID of the form {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}.  To add this cluster to a team, correct the team ID and run 'wlbs reload' followed by 'wlbs start'. %3 %4 \r\n
0xc0070039 | NLB Cluster %2 %1: Invalid bi-directional affinity (BDA) teaming port rules detected.  Each member of a BDA team may have no more than one port rule whose affinity must be single or class C if multiple host filtering is specified.  To add this cluster to a team, correct the port rules and run 'wlbs reload' followed by 'wlbs start'. %3 %4 \r\n
0xc007003b | NLB Cluster %2 %1: The bi-directional affinity (BDA) team which this cluster has attempted to join already has a designated master.  This cluster will not join the team and will remain in the stopped state until the parameter errors are corrected and the cluster is restarted by running 'wlbs reload' followed by 'wlbs start'. %3 %4 \r\n
0xc0070049 | NLB Cluster %2 %1: Cluster IGMP multicast IP address %3 is invalid.  Please check the NLB configuration and make sure that the cluster IGMP multicast IP address consists of four decimal byte values separated by dots. %4 \r\n
0xc0070052 | NLB Cluster %2 %1: The network adapter to which NLB is bound does not support NDIS packet indications, which is commonly caused by outdated NIC hardware and/or drivers.  In order to properly load-balance incoming load, NLB requires that adapters support NDIS packet indications. %3 %4\r\n
0xc0070053 | NLB Cluster %2 %1: Duplicate dedicated IP address %3 was discovered on the network.  Please check the NLB configuration on all hosts that belong to the cluster and make sure that they all contain unique dedicated IP addresses. %4 \r\n
