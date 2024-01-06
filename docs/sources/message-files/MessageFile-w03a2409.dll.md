## w03a2409.dll

Path: %SystemRoot%\system32\W03A2409.dll

### 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00000133 | (Ext Maintenance, Internal State '%1!s!')%0\r\n
0x00000134 | Setting extended maintenance mode for resource '%1!s!'\r\n
0x00000135 | Clearing extended maintenance mode for resource '%1!s!'\r\n
0x00000136 | The syntax of this command is:\r\n\r\nCLUSTER [[/CLUSTER:]cluster-name] RES[OURCE] <options>\r\n\r\n<options> =\r\n  [resource-name] [/STAT[US]]\r\n  /NODE:node-name\r\n  /PROP[ERTIES]\r\n  /PRIV[PROPERTIES]\r\n  resource-name /PROP[ERTIES] [<prop-list>]\r\n  resource-name /PRIV[PROPERTIES] [<prop-list>]\r\n  resource-name /PROP[ERTIES][:propname[,propname ...] /USEDEFAULT]\r\n  resource-name /PRIV[PROPERTIES][:propname[,propname ...] /USEDEFAULT]\r\n  resource-name /CREATE /GROUP:group-name /TYPE:res-type [/SEPARATE]\r\n  resource-name /DELETE\r\n  resource-name /REN[AME]:new-name\r\n  resource-name /ADDOWNER:node-name\r\n  resource-name /REMOVEOWNER:node-name\r\n  resource-name /LISTOWNERS\r\n  resource-name /MOVE[TO]:group\r\n  resource-name /FAIL\r\n  resource-name /ON[LINE] [/WAIT[:timeout-seconds]]\r\n  resource-name /OFF[LINE] [/WAIT[:timeout-seconds]]\r\n  resource-name /LISTDEP[ENDENCIES]\r\n  resource-name /ADDDEP[ENDENCY]:resource\r\n  resource-name /REMOVEDEP[ENDENCY]:resource\r\n  resource-name /ADDCHECK[POINTS]:key[\subkey...][,key[\subkey...]...]\r\n  resource-name /REMOVECHECK[POINTS]:key[\subkey...][,key[\subkey...]...]\r\n  [resource-name] /CHECK[POINTS]\r\n  resource-name /ADDCRYPTOCHECK[POINTS]:type\name\key[,type\name\key...]\r\n  resource-name /REMOVECRYPTOCHECK[POINTS]:type\name\key[,type\name\key...]\r\n  [resource-name] /CRYPTOCHECK[POINTS]\r\n  resource-name /MAINT[ENANCEMODE][:<maintenance-mode-settings>]\r\n  resource-name /EXTMAINT[ENANCEMODE][:<maintenance-mode-settings>]\r\n  resource-name /WAITMAINT[PENDING]\r\n\r\nFor Network Name resources:\r\n  resource-name /REGISTERDNS[RECORDS]\r\n\r\n<prop-list> =\r\n  name=value[,value ...][:<format>] [name=value[,value ...][:<format>] ...]\r\n\r\n<format> =\r\n  BINARY|DWORD|STR[ING]|EXPANDSTR[ING]|MULTISTR[ING]|SECURITY|ULARGE\r\n\r\n<maintenance-mode-settings> =\r\n  0|1|ON|OFF\r\n\r\nCLUSTER RESOURCE /?\r\nCLUSTER RESOURCE /HELP\r\n
0x00000600 | Application %1 (process id %2) received a very large RPC allocation request on interface %3, \r\nprocedure number %4. Request size is %5, which is over the limit of %6. The request came from user \r\n%7 from network address %8. If problem persists, please contact the system administrator.\r\n
0x00001f40 | CertVerifyRevocation fails for the certificate.\r\nsubject=%1; URL=%2; Reason = %3\r\n
0x00001f41 | CertVerifyRevocation fails for the certificate.\r\nsubject=%1; URL=%2; Error code = %3\r\n
0x400003e8 | The average call duration has exceeded the configured threshold.%1%0\r\n
0x40006664 | Chkdsk was executed in read-only mode on a volume snapshot.\r\n
0x40006665 | Chkdsk was executed in read-only mode.  A volume snapshot was not used.\r\nExtra errors and warnings may be reported as the volume may have\r\nchanged during the chkdsk run.\r\n
0x40006666 | Chkdsk was executed in read/write mode.\r\n
0x40006667 | %1 percent complete. (%2 of %3 file records processed)        %r%0\r\n
0x40006668 | %1 percent complete. (%2 of %3 large file records processed)  %r%0\r\n
0x40006669 | %1 percent complete. (%2 of %3 bad file records processed)    %r%0\r\n
0x4000666a | %1 percent complete. (%2 of %3 EA records processed)          %r%0\r\n
0x4000666b | %1 percent complete. (%2 of %3 reparse records processed)     %r%0\r\n
0x4000666c | %1 percent complete. (%2 of %3 index entries processed)       %r%0\r\n
0x4000666d | %1 percent complete. (%2 of %3 unindexed files processed)     %r%0\r\n
0x4000666e | %1 percent complete. (%2 of %3 SD bytes processed)            %r%0\r\n
0x4000666f | %1 percent complete. (%2 of %3 descriptors processed)         %r%0\r\n
0x40006670 | %1 percent complete. (%2 of %3 data files processed)          %r%0\r\n
0x40006671 | %1 percent complete. (%2 of %3 USN bytes processed)           %r%0\r\n
0x40006672 | %1 percent complete. (%2 of %3 files processed)               %r%0\r\n
0x40006673 | %1 percent complete. (%2 of %3 free clusters processed)       %r%0\r\n
0x40006674 | %1 file records processed.                                  %r%0\r\n
0x40006675 | %1 large file records processed.                            %r%0\r\n
0x40006676 | %1 bad file records processed.                              %r%0\r\n
0x40006677 | %1 EA records processed.                                    %r%0\r\n
0x40006678 | %1 reparse records processed.                               %r%0\r\n
0x40006679 | %1 index entries processed.                                 %r%0\r\n
0x4000667a | %1 unindexed files processed.                               %r%0\r\n
0x4000667b | %1 security descriptor bytes processed.                     %r%0\r\n
0x4000667c | %1 security descriptors processed.                          %r%0\r\n
0x4000667d | %1 data files processed.                                    %r%0\r\n
0x4000667e | %1 USN bytes processed.                                     %r%0\r\n
0x4000667f | %1 files processed.                                         %r%0\r\n
0x40006680 | %1 free clusters processed.                                 %r%0\r\n
0x40006681 | %1%2%3                                                        %r%0\r\n
0x40250825 | Started evaluating transitive filter.\r\n%n\r\n%n Additional Data\r\n%n Base link id: %n%1\r\n%n Link type:%n%2\r\n%n Attribute:%n%3\r\n
0x40250826 | Finished evaluating transitive filter.\r\n%n\r\n%n Additional Data\r\n%n Objects visited: %n%1\r\n
0x800003e9 | The average call duration has exceeded 10 minutes. If this is not the expected behavior, please see article 910904 in the Microsoft Knowledge Base at http://support.microsoft.com for details on how to use the COM+ AutoDump feature to automatically generate dump files and/or terminate the process if the problem occurs again.%1%0\r\n
0x800011a8 | The DNS server encountered error %1 building the zone list from Active\r\nDirectory. The DNS server will sleep for %2 seconds and try again.\r\nThis can be caused by high Active Directory load and may be a\r\ntransient condition.\r\n
0x800011a9 | The DNS server encountered error %1 attempting to load zone %2 from\r\nActive Directory. The DNS server will attempt to load this zone again\r\non the next timeout cycle. This can be caused by high Active Directory\r\nload and may be a transient condition.\r\n
0x800011ab | Majority Node Set resource has failed a status check for file share '%1'. The error code was '%2'. Please\r\nensure that the file share is configured properly and that the cluster service account has write permission on the file\r\nshare.\r\n
0x80001b84 | The following service is taking more than %2 minutes to start and may be hung: %1%n%nContact your system administrator or service vendor for approximate startup times for this service.%n%nIf you think this service might be slowing system response or logon time, talk to your system administrator about whether the service should be disabled until the problem is identified.%n%nYou may have to restart the computer in safe mode before you can disable the service.\r\n
0x80002787 | \r\nActive Connections\r\n\r\n  Proto  Local Address          Foreign Address        State           Offload State\r\n\r\n
0x80002788 |   %1!-5s!  %2!-21s!  %3!-21s!  %4!-12s!    %5!-12s!\r\n
0x80002789 | InHost%0\r\n
0x8000278a | Offloading%0\r\n
0x8000278b | Offloaded%0\r\n
0x8000278c | Uploading%0\r\n
0x8000278d | \r\nActive Connections\r\n\r\n  Proto  Local Address          Foreign Address        State           PID      Offload State\r\n\r\n
0x8000278e |   %1!-5s!  %2!-21s!  %3!-21s!  %4!-12s!    %5!u!\t%6!-12s!\r\n
0x8000278f | \r\nDisplays protocol statistics and current TCP/IP network connections.\r\n\r\nNETSTAT [-a] [-b] [-e] [-n] [-o] [-p proto] [-r] [-s] [-t] [-v] [interval]\r\n\r\n  -a            Displays all connections and listening ports.\r\n  -b            Displays the executable involved in creating each connection or\r\n                listening port. In some cases well-known executables host\r\n                multiple independent components, and in these cases the\r\n                sequence of components involved in creating the connection\r\n                or listening port is displayed. In this case the executable\r\n                name is in [] at the bottom, on top is the component it called,\r\n                and so forth until TCP/IP was reached. Note that this option\r\n                can be time-consuming and will fail unless you have sufficient\r\n                permissions.\r\n  -e            Displays Ethernet statistics. This may be combined with the -s\r\n                option.\r\n  -n            Displays addresses and port numbers in numerical form.\r\n  -o            Displays the owning process ID associated with each connection.\r\n  -p proto      Shows connections for the protocol specified by proto; proto\r\n                may be any of: TCP, UDP, TCPv6, or UDPv6.  If used with the -s\r\n                option to display per-protocol statistics, proto may be any of:\r\n                IP, IPv6, ICMP, ICMPv6, TCP, TCPv6, UDP, or UDPv6.\r\n  -r            Displays the routing table.\r\n  -s            Displays per-protocol statistics.  By default, statistics are\r\n                shown for IP, IPv6, ICMP, ICMPv6, TCP, TCPv6, UDP, and UDPv6;\r\n                the -p option may be used to specify a subset of the default.\r\n  -t            Displays the current connection offload state.\r\n  -v            When used in conjunction with -b, will display sequence of\r\n                components involved in creating the connection or listening\r\n                port for all executables.\r\n  interval      Redisplays selected statistics, pausing interval seconds\r\n                between each display.  Press CTRL+C to stop redisplaying\r\n                statistics.  If omitted, netstat will print the current\r\n                configuration information once.\r\n
0x800038cd | DFS link %1 was marked incorrectly as a DFS root. The DFS namespace is operational on this server. If this namespace is hosted on servers running Windows Server 2003 prior to Service Pack 2 (SP2), or if the server is running Windows 2000 Server, the namespace might not be fully functional on those servers.\r\n\r\nPlease consult the Microsoft Knowledge Base for more information on correcting this issue.\r\n
0x800038ce | DFS metadata object %1 is empty in the metadata for DFS root %2. The DFS namespace is operational on this server. If this namespace is hosted on servers running Windows Server 2003 prior to Service Pack 2 (SP2), or if the server is running Windows 2000 Server, the namespace might not be fully functional on those servers.\r\n\r\nPlease consult the Microsoft Knowledge Base for more information on correcting this issue.\r\n
0xc00004d7 | The Cluster service account does not have the following required user\r\nrights:%n\r\n%n%1\r\n%nThese user rights were granted to the Cluster service account during cluster\r\nsetup and must not be removed.%n\r\n%nFind detailed recovery steps in the knowledge base article:\r\n%nhttp://go.microsoft.com/fwlink/?LinkId=59968%n\r\n(you may need to manually copy&paste the link above to your web browser)%n\r\n%nUser Action%n\r\n%nAssign these rights to the Cluster service account. One way to do this is to\r\n use Local Security Settings (Scepol.msc).%n\r\n%nIf these user rights are already granted to the Cluster service account in \r\nSecpol.msc under Local Policies\User Rights Assignment, a Group Policy object \r\nmight be overriding local settings and removing the rights.%n\r\n%nIf your organization implements Group Policy objects that override the local\r\n security policies that remove a user right from the Cluster service by \r\nchanging the effective user rights, you can work around this problem and get \r\nthe cluster service to start again by following these steps: (You may need \r\nhelp from your organizationÆs domain administrators to complete these steps.)%n\r\n1) Create a new organizational unit (OU) in the domain or in the forest, and \r\nthen block policy inheritance on that OU.%n\r\n2) Move the cluster nodes into the OU.%n\r\n3) Start the Cluster service on each node.%n\r\n4) Resolve the issues with the security policies that are restricting server \r\ncluster operation so that the cluster nodes can be moved back to its original\r\n location in the Active Directory.%n\r\n
0xc0000500 | XML file %1 has an invalid file format.\r\n
0xc0000501 | XML file %1 cannot be loaded.\r\n
0xc00011aa | Majority Node Set resource has failed to come online. The resource has detected that it\r\ndoes not have the latest copy of server cluster database. If this is a two node cluster, try\r\nstarting cluster service on the other node, and let this node join the cluster. If that does not work,\r\nuse /forcequorum startup option to start cluster service. See KB article KB258078 for details on\r\ncluster service startup options.\r\n
