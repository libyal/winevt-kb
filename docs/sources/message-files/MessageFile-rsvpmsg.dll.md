## rsvpmsg.dll

Path: %SystemRoot%\System32\rsvpmsg.dll

### 5.0.2167.1

Message identifier | Message string
--- | ---
0x00002711 | QoS RSVP service started.\r\n
0x00002712 | QoS RSVP service stopped.\r\n
0x00002713 | QoS RSVP service failed to start with error %1.\r\n
0x00002714 | QoS RSVP service key in registry is missing or corrupted. Need to reinstall QoS RSVP service to correct this problem.\r\n
0x00002715 | Error %1 while opening QoS RSVP service parameters key, using default values for all RSVP configuration parameters.\r\n
0x00002716 | Received I_AM_DSBM from another DSBM with IP address %1 and priority %2.\r\n
0x00002717 | Received I_AM_DSBM message from another DSBM with priority %1 higher than this DSBM's, hence stopping.\r\n
0x00002718 | Unable to Load DLL IPHLPAPI.DLL, RSVP will not be able to function without this DLL.\r\n
0x00002719 | Error %1 while registering for changes to RSVP service key in registry. RSVP will not be able to respond to changes to registry values.\r\n
0x0000271a | Error %1 while creating the tracefile, hence RSVP will not write RSVP message details to the trace files.\r\n
0x0000271b | Currently allocated bandwidth %1 by QoS ACS is more than the new upper limit %2 set via QoS ACS management console on interface %3. Changes made using QoS ACS management console does not affect existing reservations.\r\n
0x0000271c | There is no upper bound on the amount of bandwidth available for RSVP reservations on interface %1.\r\n
0x0000271d | This host became DSBM for the subnet with %1 IP address.\r\n
0x0000271e | This host is no longer the DSBM on subnet with %1 IP address.\r\n
0x0000271f | Changed maximum peak data rate per flow to be same as maximum data rate per flow as the peak data rate is lower than data rate on subnet %1.\r\n
0x00002720 | Can not send a Reservation Confirm message because RSVP can not find a route to the host with %1 IP address.\r\n
0x00002721 | Unable to allocate sufficient memory to start RSVP service.\r\n
0x00002722 | Encountered %1 error while loading the LPM %2.\r\n
0x00002723 | The LPM %1 is missing one of the necessary functions.\r\n
0x00002724 | Initialization of LPM %1 failed with error %2, ACS will continue to function without this LPM.\r\n
0x00002725 | Initialization of LPM %1 returned invalid Policy Element type %2, ACS will continue to function without this LPM.\r\n
0x00002726 | LPM %1 initialized successfully and handles policy element of type %2.\r\n
0x00002727 | Policy Control Module initialized successfully and there are %1 active LPMs.\r\n
0x00002728 | Policy Control Module failed to initialize with error (%1).\r\n
0x00002729 | PCM received results from an LPM with invalid handle, ignoring the results.\r\n
0x0000272a | PCM received results from an %1 LPM with invalid request handle, ignoring the results.\r\n
0x0000272b | Dropping results for GetPolicyData request from LPM %1 for reasons other than invalid handle and multiple results.\r\n
0x0000272c | PCM received results from an %1 LPM multiple times, ignoring the results.\r\n
0x0000272d | Error %1 while loading the ADSI library required to access directory.\r\n
0x0000272e | This host can not be DSBM on %1 interface as this DSBM is supported only on NT server.\r\n
0x0000272f | Using registry value of %1 from %2 registry key.\r\n
0x00002730 | Using registry value of %1 from %2 registry key in %3 subnet.\r\n
0x00002731 | This host %1 is not in server list of %2 subnet. Add this server to list via QoS ACS management console.\r\n
0x00002732 | This host %1 can not be ACS on any of the subnets as this host has not been added to the ACS server lists in the Directory. Add this server to the list of valid servers for ACS via QoS ACS management console.\r\n
0x00002733 | This host can not be ACS since the Active Directory has not been properly configured via the QoS ACS management console. Please configure the subnets via the QoS ACS mangement console.\r\n
0x00002734 | Restarting ACS as the admission control mode has changed from service specific mode to aggregate mode.\r\n
0x00002735 | Restarting ACS as the admission control mode has changed from aggregate mode to service specific mode.\r\n
0x00002736 | Unloaded all LPMs other than %1, as %1 LPM makes policy decisions using all types of policy elements.\r\n
0x00002737 | The WSAIoctl to snoop RSVP messages failed with %1 error, hence unable to receive RSVP messages on interface %2.\r\n
0x00002738 | This ACS has been configured to manage PPP interfaces but no PPP lines are detected on this host. So the ACS service is not functioning. Enable PPP lines or configure the ACS to manage shared media.\r\n
0x00002739 | QoS RSVP supports IPSEC flows.\r\n
0x0000273a | QoS RSVP fails to register for SPI event notification -> abandon ipsec support.\r\n
0x0000273b | Shutting QoS RSVP service due to system failure.\r\n
0x0000273c | Shutting QoS RSVP service due to a system failure.\r\n
0x0000273d | QoS RSVP fails to open a signaling socket (TCP) to communicate with clients due to a system failure.\r\n
0x0000273e | QoS RSVP fails to load TRAFFIC.DLL, so traffic control is not functional on this machine. Check %systemroot%\system32 directory for TRAFFIC.DLL.\r\n
0x0000273f | QoS RSVP has failed to find any interfaces with traffic control enabled. Install QoS traffic control services via network and dial-up connections.\r\n
0x00002740 | QoS RSVP fails to register as a traffic control client. Check for the presence of QoS packet scheduler, the classical IP over ATM provider, or another traffic control provider.\r\n
0x00002741 | QoS RSVP fails to install a network control flow for RSVP packets. On a congested network, RSVP message could be dropped.\r\n
0x00002742 | QoS RSVP fails to uninstall a flow for RSVP packets.\r\n
0x00002743 | No traffic control capability on the specific interface with %1 IP address.\r\n
0x00002744 | Interface is not available from TC.\r\n
0x00002745 | This host will not function as ACS on the subnet with %1 IP address, as ACS is not enabled on this subnet.\r\n
0x00002746 | ACS has not been configured for %1 subnet. Please add ACS configuration data using the QoS ACS management console.\r\n
0x00002747 | QoS RSVP fails to engage with the IPSEC Policy Agent\r\n
0x00002748 | Rogue server detection is disabled via registry.\r\n
0x00002749 | DSBM found per service limits in the configuration data of %1 subnet, hence operating in DiffServ mode.\r\n
0x0000274a | QoS RSVP failure in the initialization of memory debugging functions.\r\n
0x0000274b | Found another DSBM with IP address %1 on the %2 interface, hence this host will not attempt to be DSBM on this interface.\r\n
0x0000274c | ACS will not do policy admission control as this ACS is configured to do Resource admission control only.\r\n
0x0000274d | Version number %1 returned by %2 LPM is unsupported by the Policy Control Module in ACS.\r\n
0x0000274e | PCM received invalid results from an %1 LPM, ignoring the results.\r\n
0x0000274f | ACS on this host is managing the non-shared media interface with %1 IP address.\r\n
0x00002750 | There are no non-shared media interfaces on this host which are manageable by this ACS.\r\n
0x00002751 | This host is no longer the DSBM on interface %1 as this interface disappeared.\r\n
0x00002752 | QoS Admission Control Service started.\r\n
0x00002753 | QoS Admission Control Service stopped.\r\n
0x00002754 | QoS Admission Control Service failed to start with error %1.\r\n
0x00002af9 | Error (%1) while retrieving the AcsService account name, password and domain name. Enter this data using the QoS ACS management console.\r\n
0x00002afa | Error (%1) while validating AcsService account user name, password. Enter the correct account user name, password using the QoS ACS management console.\r\n
0x00002afb | MSIDLPM could not logon to Kerberos KeyDistribution Center using the supplied account name, password. Hence MSIDLPM will not initialize.\r\n
0x00002afc | Error (%1) while cracking the Kerberos ticket in the Identity Policy element. One of the possible reason could be that ACS is configured with a bad password. Enter the correct password using the QoS ACS management console.\r\n
0x00002afd | Error (%1) while decrypting the policy locator in the Identity Policy element. One of the possible reason could be that ACS is configured with a bad password. Enter the correct password using the QoS ACS management console.\r\n
0x00002afe | ACS was not able to get the Domain Controller name to access the Active Directory, and failed with (%1) error.\r\n
0x00002aff | Error (%1) while opening the root container in DS. ACS configuration parameters are stored under the root container.\r\n
0x00002b00 | Error (%1) while opening the Enterprise policy container in DS. Enterprise level ACS configuration parameters are stored in this DS container.\r\n
0x00002b01 | Error (%1) while opening the %2 subnet container in DS. Configuration data for this subnet are stored in this container. Enter this data using the QoS ACS management console.\r\n
0x00002b02 | Error (%1) while searching for ACS policies in the subnet container with IP address %2. Enter ACS policies using the QoS ACS management console.\r\n
0x00002b03 | Error (%1) while reading ACS policies in the subnet container with IP address %2. Enter ACS policies using the QoS ACS management console.\r\n
0x00002b04 | Error (%1) while obtaining the credential handle for AcsService account. This handle is used to decode Kerberos tickets. Enter correct account user name, password using the QoS ACS management console.\r\n
0x00002b05 | Error (%1) encountered while writing to accounting file. MSIDLPM will stop writing to the accounting file, due to the error, and will restart after the next policy cache timeout.\r\n

### 5.1.2600.0

Message identifier | Message string
--- | ---
0x00002711 | QoS RSVP service started.\r\n
0x00002712 | QoS RSVP service stopped.\r\n
0x00002713 | QoS RSVP service failed to start with error %1.\r\n
0x00002714 | Error (%1) while opening QoS RSVP service key in registry. Need to reinstall QoS RSVP service to correct this problem.\r\n
0x00002715 | Error (%1) while opening QoS RSVP service parameters key, using default values for all RSVP configuration parameters.\r\n
0x00002716 | Received I_AM_DSBM from another DSBM with IP address %1 and priority %2.\r\n
0x00002717 | Received I_AM_DSBM message from another DSBM with priority %1 higher than this DSBM's, hence stopping.\r\n
0x00002718 | Unable to Load DLL IPHLPAPI.DLL and find the required IP helper functions, RSVP will not be able to function without this DLL.\r\n
0x00002719 | Error (%1) while registering for changes to RSVP service key in registry. RSVP will not be able to respond to changes to registry values.\r\n
0x0000271a | Error (%1) while creating the tracefile, hence RSVP will not write RSVP message details to the trace files.\r\n
0x0000271b | Currently allocated bandwidth %1 by QoS ACS is more than the new upper limit %2 set via QoS ACS management console on interface %3. Changes made using QoS ACS management console does not affect existing reservations.\r\n
0x0000271c | There is no upper bound on the amount of bandwidth available for RSVP reservations on interface %1.\r\n
0x0000271d | This host became DSBM for the subnet with %1 IP address.\r\n
0x0000271e | This host is no longer the DSBM on subnet with %1 IP address.\r\n
0x0000271f | Changed maximum peak data rate per flow to be same as maximum data rate per flow as the peak data rate is lower than data rate on subnet %1.\r\n
0x00002720 | Can not send a Reservation Confirm message because RSVP can not find a route to the host with %1 IP address.\r\n
0x00002721 | Unable to allocate sufficient memory to start RSVP service.\r\n
0x00002722 | Error (%1) while loading the LPM %2.\r\n
0x00002723 | The LPM %1 is missing one of the necessary functions.\r\n
0x00002724 | Initialization of LPM %1 failed with error %2, ACS will continue to function without this LPM.\r\n
0x00002725 | Initialization of LPM %1 returned invalid Policy Element type %2, ACS will continue to function without this LPM.\r\n
0x00002726 | LPM %1 initialized successfully and handles policy element of type %2.\r\n
0x00002727 | Policy Control Module initialized successfully and there are %1 active LPMs.\r\n
0x00002728 | Policy Control Module failed to initialize with error (%1).\r\n
0x00002729 | PCM received results from an LPM with invalid handle, ignoring the results.\r\n
0x0000272a | PCM received results from an %1 LPM with invalid request handle, ignoring the results.\r\n
0x0000272b | Dropping results for GetPolicyData request from LPM %1 for reasons other than invalid handle and multiple results.\r\n
0x0000272c | PCM received results from an %1 LPM multiple times, ignoring the results.\r\n
0x0000272d | Error (%1) while loading the ADSI library required to access directory.\r\n
0x0000272e | This host can not be DSBM on %1 interface as this DSBM is supported only on NT server.\r\n
0x0000272f | Using registry value of %1 from %2 registry key.\r\n
0x00002730 | Using registry value of %1 from %2 registry key in %3 subnet.\r\n
0x00002731 | This host %1 is not in server list of %2 subnet. Add this server to list via QoS ACS management console.\r\n
0x00002732 | This host %1 can not be ACS on any of the subnets as this host has not been added to the ACS server lists in the Directory, will continue to look for ACS configuration data at regular intervals. Add this server to the list of valid servers for ACS via QoS ACS management console.\r\n
0x00002733 | This host can not be ACS since the Active Directory has not been properly configured via the QoS ACS management console. Please configure the subnets via the QoS ACS mangement console.\r\n
0x00002734 | Restarting ACS as the admission control mode has changed from service specific mode to aggregate mode for %1 subnet.\r\n
0x00002735 | Restarting ACS as the admission control mode has changed from aggregate mode to service specific mode for %1 subnet.\r\n
0x00002736 | Unloaded all LPMs other than %1, as %1 LPM makes policy decisions using all types of policy elements.\r\n
0x00002737 | The WSAIoctl to snoop RSVP messages failed with %1 error, hence unable to receive RSVP messages on interface %2.\r\n
0x00002738 | This ACS has been configured to manage PPP interfaces but no PPP lines are detected on this host. So the ACS service is not functioning. Enable PPP lines or configure the ACS to manage shared media.\r\n
0x00002739 | QoS RSVP supports IPSEC flows.\r\n
0x0000273a | QoS RSVP failed to register for SPI event notification -> abandon ipsec support.\r\n
0x0000273b | Shutting QoS RSVP service due to system failure.\r\n
0x0000273c | Shutting QoS RSVP service due to a system failure.\r\n
0x0000273d | QoS RSVP failed with error (%1) while opening a signaling socket (TCP) to communicate with clients.\r\n
0x0000273e | Error (%1) when QoS RSVP tried to load TRAFFIC.DLL, so traffic control is not functional on this machine. Check %systemroot%\system32 directory for TRAFFIC.DLL.\r\n
0x0000273f | QoS RSVP has failed to find any interfaces with traffic control enabled. Install QoS traffic control services via Network connections.\r\n
0x00002740 | Error (%1) when QoS RSVP tried to register as a traffic control client. Check for the presence of QoS packet scheduler, the classical IP over ATM provider, or another traffic control provider.\r\n
0x00002741 | QoS RSVP failed to install a network control flow for RSVP packets. On a congested network, RSVP message could be dropped.\r\n
0x00002742 | Error (%1) when QoS RSVP tried to uninstall a flow for RSVP packets.\r\n
0x00002743 | No traffic control capability on the specific interface with %1 IP address.\r\n
0x00002744 | Interface is not available from TC.\r\n
0x00002745 | This host will not function as ACS on the subnet with %1 IP address, as ACS is not enabled on this subnet.\r\n
0x00002746 | ACS has not been configured for %1 subnet. Please add ACS configuration data using the QoS ACS management console.\r\n
0x00002747 | QoS RSVP failed to engage with the IPSEC Policy Agent\r\n
0x00002748 | Rogue server detection is disabled via registry.\r\n
0x00002749 | DSBM found per service limits in the configuration data of %1 subnet, hence operating in DiffServ mode.\r\n
0x0000274a | QoS RSVP failure in the initialization of memory debugging functions.\r\n
0x0000274b | Found another DSBM with IP address %1 on the %2 interface, hence this host will not attempt to be DSBM on this interface.\r\n
0x0000274c | ACS will not do policy admission control as this ACS is configured to do Resource admission control only.\r\n
0x0000274d | Version number %1 returned by %2 LPM is unsupported by the Policy Control Module in ACS.\r\n
0x0000274e | PCM received invalid results from an %1 LPM, ignoring the results.\r\n
0x0000274f | ACS on this host is managing the non-shared media interface with %1 IP address.\r\n
0x00002750 | There are no non-shared media interfaces on this host which are manageable by this ACS.\r\n
0x00002751 | This host is no longer the DSBM on interface %1 as this interface disappeared.\r\n
0x00002752 | QoS Admission Control Service started.\r\n
0x00002753 | QoS Admission Control Service stopped.\r\n
0x00002754 | QoS Admission Control Service failed to start with error %1.\r\n
0x00002755 | Unable to use registry value of %1 as it it is too long.\r\n
0x00002756 | This host could not join the DSBMLogicalMulticast group to act as the DSBM for the subnet with %1 IP address.\r\n
0x00002757 | This host has %1 IP addresses, RSVP will function only on the first 31 IP addresses.\r\n
0x00002758 | Unable to initialize Winsock 2 and find RAW IP and TCP providers, which are required for the RSVP service to operate.\r\n
0x00002759 | Error (%1) while initializing Perfmon counters.\r\n
0x0000275a | Error (%1) while initializing interface list.\r\n
0x0000275b | QoS RSVP service stopped with exception %1.\r\n
0x0000275c | QoS Admission Control Service stopped with exception %1.\r\n
0x0000275d | Error (%1) while opening the %2 subnet container in DS. ACS resource configuration data for this subnet are stored in this container. Enter this data using the QoS ACS management console.\r\n
0x0000275e | QoS Admission Control Service restarting as the IP addresses on this server have changed.\r\n
0x0000275f | Error (%1) while starting thread to refresh DS configuration data. ACS resource configuration data will not be refreshed.\r\n
0x00002af9 | Error (%1) while retrieving the AcsService account name, password and domain name. Enter this data using the QoS ACS management console.\r\n
0x00002afa | Error (%1) while validating AcsService account user name, password. Enter the correct account user name, password using the QoS ACS management console.\r\n
0x00002afb | MSIDLPM could not logon to Kerberos KeyDistribution Center using the supplied account name, password. Hence MSIDLPM will not initialize.\r\n
0x00002afc | Error (%1) while cracking the Kerberos ticket in the user Identity Policy element received from system with %2 IP address.\r\n
0x00002afd | Error (%1) while decrypting the policy locator in the user Identity Policy element.\r\n
0x00002afe | ACS was not able to get the Domain Controller name to access the Active Directory, and failed with (%1) error.\r\n
0x00002aff | Error (%1) while opening the root container in DS. ACS configuration parameters are stored under the root container.\r\n
0x00002b00 | Error (%1) while opening the Enterprise policy container in DS. Enterprise level ACS configuration parameters are stored in this DS container.\r\n
0x00002b01 | Error (%1) while opening the %2 subnet container in DS. QoS policy data for this subnet are stored in this container. Enter this data using the QoS ACS management console.\r\n
0x00002b02 | Error (%1) while searching for ACS policies in the subnet container with IP address %2. Enter ACS policies using the QoS ACS management console.\r\n
0x00002b03 | Error (%1) while reading ACS policies in the subnet container with IP address %2. Enter ACS policies using the QoS ACS management console.\r\n
0x00002b04 | Error (%1) while obtaining the credential handle for AcsService account. This handle is used to decode Kerberos tickets. Enter correct account user name, password using the QoS ACS management console.\r\n
0x00002b05 | Error (%1) encountered while writing to accounting file. MSIDLPM will stop writing to the accounting file, due to the error, and will restart after the next policy cache timeout.\r\n
0x00002b06 | Error (%1) while cracking the Kerberos ticket in the Identity Policy element received from system with %2 IP address. One of the possible reason could be that ACS is configured with a bad password. Enter the correct password using the QoS ACS management console.\r\n
0x00002ee0 | Error (%1) while creating the security descriptor used to protect the RSVP statistics shared memory.\r\n
0x00002ee1 | Error (%1) while opening the shared memory containing the RSVP statistics.\r\n
0x00002ee2 | Error (%1) while opening the shared memory containing the MSIDLPM statistics.\r\n
0x00002ee3 | Error (%1) while opening the RSVP performance key (HKLM\\SYSTEM\CurrentControlSet\Services\RSVP\Performance) in registry.\r\n
0x00002ee4 | Error (%1) while reading the FirstCounter value under RSVP performance key (HKLM\\SYSTEM\CurrentControlSet\Services\RSVP\Performance) in registry.\r\n
0x00002ee5 | Error (%1) while reading the FirstHelp value under RSVP performance key (HKLM\\SYSTEM\CurrentControlSet\Services\RSVP\Performance) in registry.\r\n
