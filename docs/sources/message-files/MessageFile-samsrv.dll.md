## samsrv.dll

Path: %SystemRoot%\System32\samsrv.dll

### 5.0.2195.6697

Message identifier | Message string
--- | ---
0x00001fff | SAMP_UNUSED_MESSAGE\r\n
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users possess most administrative powers with some restrictions.  Thus, Power Users can run legacy applications in addition to certified applications\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes.  Thus, Users can run certified applications, but not most legacy applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer domain printers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Enterprise certification and renewal agents\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to\r\na memory or disk-space shortage. The SAM database will be restored to\r\nan earlier state. Recent changes will be lost. Check the disk-space\r\navailable and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown.\r\nYou must reboot the machine to re-enable SAM.\r\n
0x00003002 | SAM failed to update the SAM database. It will try again next time you\r\nreboot the machine.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003004 | There are two or more objects that have the same account name attribute\r\nin the SAM database. The Distinguished Name of the account is %1. Please \r\ncontact your system administrator to have all duplicate accounts deleted, \r\nbut ensure that the original account remains. For computer accounts, the \r\nmost recent account should be retained. In all the other cases, the older \r\naccount should be kept.\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM\r\ndatatbase. The Distinguished Name of the account is %1. All duplicate \r\naccounts have been deleted. Check the event log for additional Duplicates\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource\r\nerror, such as a hard disk write failure (the specific error code is in the\r\nerror data) . Accounts are locked after a certain number of bad passwords are\r\nprovided so please consider resetting the password of the account mentioned\r\nabove.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account \r\ninformation that is no longer used.  The error is in the record data. Please\r\nhave an admin delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files\r\nthat were once used by the Directory Service. The error is in record data. \r\nPlease have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as\r\nits object class attribute in the directory is not computer or is not \r\nderived from computer.If this is caused by an attempt to install a pre windows \r\n2000 domain controller in a windows 2000 domain, then you should precreate the \r\naccount for the domain controller with the correct object class. \r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an\r\nequivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to added\r\nmanually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to added\r\nmanually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to added\r\nmanually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have\r\nto added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have\r\nto added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the\r\ndirectory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400d | Setting the administrator's password to the string you specified failed.\r\nUpon reboot the password will be blank; please reset once logged on.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters \r\nattribute. The following Notification Package DLL might be the possible \r\noffender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user \r\nThis operation is failed. Check the record data of this event for the NT\r\nerror code.        \r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1.\r\nWe will try to continue upgrading this user. But it might contain inconsistant data. \r\nCheck the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2.  \r\nThe problem, "%3", occurred when trying to open the group. Please add the member manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. \r\nThe problem, "%3", occurred when trying to add the account to the group.  Please add the member manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to\r\nrecover.\r\n
0x00004014 | The Security Accounts Manager failed to add the Enterprise Admins group to the local Administrators alias.\r\nTo ensure proper functioning of the domain, please add the member manually.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004100 | The account-identifier allocator finished initializing. The allocator was\r\ninitialized with the following identifier values: %1 %2 %3 %4 %5 %6 %7 %8.\r\nCheck the record data of this event for the initialization status. Zero\r\nindicates successful initialization, otherwise the record data contains\r\nthe NT error code.\r\n
0x00004101 | The account-identifier pool for this domain controller could not be updated.\r\nA possible reason for this is that the domain controller may be too busy with\r\nother update operations. Subsequent account creations will attempt to update\r\nthe ID pool until successful.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The\r\nidentifier pool for this domain controller may have been depleted. If this\r\nproblem persists, restart the domain controller and view the initialization\r\nstatus of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain\r\ncontroller. A possible reason for this is that the domain controller has been\r\nunable to contact the master domain controller, possibly due to connectivity\r\nor network problems. Account creation will fail on this domain controller\r\nuntil the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further\r\naccount-identifier pools can be allocated to domain controllers in this\r\ndomain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been\r\nassigned. The domain controller has failed to obtain a new identifier pool.\r\nA possible reason for this is that the domain controller has been unable to\r\ncontact the master domain controller. Account creation on this controller will\r\nfail until a new pool has been allocated. There may be network or connectivity\r\nproblems in the domain, or the master domain controller may be offline or\r\nmissing from the domain. Verify that the master domain controller is running\r\nand connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of\r\nthe current account-identifier pool belonging to this domain controller. %1.\r\nTry invalidating the account identifier pool owned by this domain controller.\r\nThis will make the domain controller acquire a fresh account identifier pool\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data\r\nfor this event has the value zero, the manager object was created. Otherwise,\r\nthe record data will contain the NT error code indicating the failure. The\r\nfailure to create the object may be due to low system resources, insufficient\r\nmemory, or disk space.\r\n
0x0000410a | The account-identifier allocator failed to initialize properly.  The record data\r\ncontains the NT error code that caused the failure.  Windows 2000 will retry the\r\ninitialization until it succeeds; until that time, account creation will be\r\ndenied on this Domain Controller.  Please look for other SAM event logs that\r\nmay indicate the exact reason for the failure.\r\n
0x0000410b | The request for a new account-identifier pool failed because %1. Windows 2000 \r\nwill retry the request until it succeeds. \r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disbled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.  \r\n
0x00004218 | Account Disabled.  \r\n
0x00004219 | Account Locked.  \r\n
0x0000421a | Account Unlocked.  \r\n
0x0000421b | Account Name Changed.  \r\n
0x0000421c | Password Policy \r\n
0x0000421d | Logoff Policy \r\n
0x0000421e | Oem Information \r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x00001fff | SAMP_UNUSED_MESSAGE\r\n
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users possess most administrative powers with some restrictions.  Thus, Power Users can run legacy applications in addition to certified applications\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes.  Thus, Users can run certified applications, but not most legacy applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer domain printers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the Active Directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to\r\na memory or disk-space shortage. The SAM database will be restored to\r\nan earlier state. Recent changes will be lost. Check the disk-space\r\navailable and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown.\r\nYou must reboot the machine to re-enable SAM.\r\n
0x00003002 | SAM failed to update the SAM database. It will try again next time you\r\nreboot the machine.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003004 | There are two or more objects that have the same account name attribute\r\nin the SAM database. The Distinguished Name of the account is %1. Please \r\ncontact your system administrator to have all duplicate accounts deleted, \r\nbut ensure that the original account remains. For computer accounts, the \r\nmost recent account should be retained. In all the other cases, the older \r\naccount should be kept.\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM\r\ndatabase. The Distinguished Name of the account is %1. All duplicate \r\naccounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource\r\nerror, such as a hard disk write failure (the specific error code is in the\r\nerror data) . Accounts are locked after a certain number of bad passwords are\r\nprovided so please consider resetting the password of the account mentioned\r\nabove.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account \r\ninformation that is no longer used.  The error is in the record data. Please\r\nhave an admin delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files\r\nthat were once used by the Directory Service. The error is in record data. \r\nPlease have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as\r\nits object class attribute in the directory is not computer or is not \r\nderived from computer.If this is caused by an attempt to install a pre windows \r\n2000 domain controller in a windows 2000 domain, then you should precreate the \r\naccount for the domain controller with the correct object class. \r\n
0x0000300b | The attempt to check whether group caching has been enabled in the \r\nSecurity Accounts Manager has failed, most likely due to lack of resources.  \r\nThis task has been rescheduled to run in one minute. \r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly\r\nupdated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly\r\nupdated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error\r\ncode is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in \r\nthe SAM database. The Distinguished Name of the duplicate account is %1. The \r\nnewest account will be kept, all older duplicate accounts have been deleted. \r\nCheck the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute\r\nin the SAM database. The system has automatically renamed object %1\r\nto a system assgined account name %2.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an\r\nequivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to added\r\nmanually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to added\r\nmanually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to added\r\nmanually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have\r\nto added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have\r\nto added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the\r\ndirectory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400d | Setting the administrator's password to the string you specified failed.\r\nUpon reboot the password will be blank; please reset once logged on.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters \r\nattribute. The following Notification Package DLL might be the possible \r\noffender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user \r\nThis operation is failed. Check the record data of this event for the NT\r\nerror code.        \r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1.\r\nWe will try to continue upgrading this user. But it might contain inconsistant data. \r\nCheck the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2.  \r\nThe problem, "%3", occurred when trying to open the group. Please add the member manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. \r\nThe problem, "%3", occurred when trying to add the account to the group.  Please add the member manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to\r\nrecover.\r\n
0x00004014 | The Security Accounts Manager failed to add the Enterprise Admins group to the local Administrators alias.\r\nTo ensure proper functioning of the domain, please add the member manually.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist.\r\nThe account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or localgroup %1 does not exist.\r\nThe group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004100 | The account-identifier allocator finished initializing. The allocator was\r\ninitialized with the following identifier values: %1 %2 %3 %4 %5 %6 %7 %8.\r\nCheck the record data of this event for the initialization status. Zero\r\nindicates successful initialization, otherwise the record data contains\r\nthe NT error code.\r\n
0x00004101 | The account-identifier pool for this domain controller could not be updated.\r\nA possible reason for this is that the domain controller may be too busy with\r\nother update operations. Subsequent account creations will attempt to update\r\nthe ID pool until successful.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The\r\nidentifier pool for this domain controller may have been depleted. If this\r\nproblem persists, restart the domain controller and view the initialization\r\nstatus of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain\r\ncontroller. A possible reason for this is that the domain controller has been\r\nunable to contact the master domain controller, possibly due to connectivity\r\nor network problems. Account creation will fail on this domain controller\r\nuntil the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further\r\naccount-identifier pools can be allocated to domain controllers in this\r\ndomain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been\r\nassigned. The domain controller has failed to obtain a new identifier pool.\r\nA possible reason for this is that the domain controller has been unable to\r\ncontact the master domain controller. Account creation on this controller will\r\nfail until a new pool has been allocated. There may be network or connectivity\r\nproblems in the domain, or the master domain controller may be offline or\r\nmissing from the domain. Verify that the master domain controller is running\r\nand connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of\r\nthe current account-identifier pool belonging to this domain controller. The computed RID value is %1. \r\nTry invalidating the account identifier pool owned by this domain controller.\r\nThis will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data\r\nfor this event has the value zero, the manager object was created. Otherwise,\r\nthe record data will contain the NT error code indicating the failure. The\r\nfailure to create the object may be due to low system resources, insufficient\r\nmemory, or disk space.\r\n
0x0000410a | The account-identifier allocator failed to initialize properly.  The record data\r\ncontains the NT error code that caused the failure.  Windows 2000 will retry the\r\ninitialization until it succeeds; until that time, account creation will be\r\ndenied on this Domain Controller.  Please look for other SAM event logs that\r\nmay indicate the exact reason for the failure.\r\n
0x0000410b | The request for a new account-identifier pool failed. Windows 2000 \r\nwill retry the request until it succeeds. The error is %n " %1 " \r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disbled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00001fff | SAMP_UNUSED_MESSAGE\r\n
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users possess most administrative powers with some restrictions.  Thus, Power Users can run legacy applications in addition to certified applications\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes.  Thus, Users can run certified applications, but not most legacy applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer domain printers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the Active Directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group have remote access to monitor this computer\r\n
0x0000211d | Members of this group have remote access to schedule logging of performance counters on this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Terminal Server License Servers\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to\r\na memory or disk-space shortage. The SAM database will be restored to\r\nan earlier state. Recent changes will be lost. Check the disk-space\r\navailable and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown.\r\nYou must reboot the machine to re-enable SAM.\r\n
0x00003002 | SAM failed to update the SAM database. It will try again next time you\r\nreboot the machine.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003004 | There are two or more objects that have the same account name attribute\r\nin the SAM database. The Distinguished Name of the account is %1. Please \r\ncontact your system administrator to have all duplicate accounts deleted, \r\nbut ensure that the original account remains. For computer accounts, the \r\nmost recent account should be retained. In all the other cases, the older \r\naccount should be kept.\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM\r\ndatabase. The Distinguished Name of the account is %1. All duplicate \r\naccounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource\r\nerror, such as a hard disk write failure (the specific error code is in the\r\nerror data) . Accounts are locked after a certain number of bad passwords are\r\nprovided so please consider resetting the password of the account mentioned\r\nabove.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account \r\ninformation that is no longer used.  The error is in the record data. Please\r\nhave an admin delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files\r\nthat were once used by the Directory Service. The error is in record data. \r\nPlease have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as\r\nits object class attribute in the directory is not computer or is not \r\nderived from computer. If this is caused by an attempt to install a pre Windows \r\n2000 domain controller in a Windows 2000 domain or later, then you should \r\nprecreate the account for the domain controller with the correct object class. \r\n
0x0000300b | The attempt to check whether group caching has been enabled in the \r\nSecurity Accounts Manager has failed, most likely due to lack of resources.  \r\nThis task has been rescheduled to run in one minute. \r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly\r\nupdated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly\r\nupdated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error\r\ncode is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in \r\nthe SAM database. The Distinguished Name of the duplicate account is %1. The \r\nnewest account will be kept, all older duplicate accounts have been deleted. \r\nCheck the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute\r\nin the SAM database. The system has automatically renamed object %1\r\nto a system assigned account name %2.\r\n
0x00003011 | An error occured while creating new default accounts for this domain.  This\r\nmaybe due to a transient error condition. The task will retry \r\nperiodically until success and will log this message again in a week if the\r\nproblem persists.                \r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an\r\nequivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to added\r\nmanually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to added\r\nmanually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to added\r\nmanually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have\r\nto added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have\r\nto added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the\r\ndirectory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400d | Setting the administrator's password to the string you specified failed.\r\nUpon reboot the password will be blank; please reset once logged on.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters \r\nattribute. The following Notification Package DLL might be the possible \r\noffender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user \r\nThis operation is failed. Check the record data of this event for the NT\r\nerror code.        \r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1.\r\nWe will try to continue upgrading this user. But it might contain inconsistant data. \r\nCheck the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2.  \r\nThe problem, "%3", occurred when trying to open the group. Please add the member manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. \r\nThe problem, "%3", occurred when trying to add the account to the group.  Please add the member manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to\r\nrecover.\r\n
0x00004014 | The Security Accounts Manager failed to add the Enterprise Admins group to the local Administrators alias.\r\nTo ensure proper functioning of the domain, please add the member manually.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist.\r\nThe account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or localgroup %1 does not exist.\r\nThe group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory failed to add a security principal to well known security principals container. Please\r\nhave an administrator add this security principal if needed.\r\nSecurity principal name: %1\r\n
0x0000401a | Active Directory failed to add all of the new security principals to well known security principals container. Please\r\nhave an administrator add these security principals if needed.\r\n
0x00004100 | The account-identifier allocator finished initializing. The allocator was\r\ninitialized with the following identifier values: %1 %2 %3 %4 %5 %6 %7 %8.\r\nCheck the record data of this event for the initialization status. Zero\r\nindicates successful initialization, otherwise the record data contains\r\nthe NT error code.\r\n
0x00004101 | The account-identifier pool for this domain controller could not be updated.\r\nA possible reason for this is that the domain controller may be too busy with\r\nother update operations. Subsequent account creations will attempt to update\r\nthe ID pool until successful.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The\r\nidentifier pool for this domain controller may have been depleted. If this\r\nproblem persists, restart the domain controller and view the initialization\r\nstatus of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain\r\ncontroller. A possible reason for this is that the domain controller has been\r\nunable to contact the master domain controller, possibly due to connectivity\r\nor network problems. Account creation will fail on this domain controller\r\nuntil the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further\r\naccount-identifier pools can be allocated to domain controllers in this\r\ndomain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been\r\nassigned. The domain controller has failed to obtain a new identifier pool.\r\nA possible reason for this is that the domain controller has been unable to\r\ncontact the master domain controller. Account creation on this controller will\r\nfail until a new pool has been allocated. There may be network or connectivity\r\nproblems in the domain, or the master domain controller may be offline or\r\nmissing from the domain. Verify that the master domain controller is running\r\nand connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of\r\nthe current account-identifier pool belonging to this domain controller. The computed RID value is %1. \r\nTry invalidating the account identifier pool owned by this domain controller.\r\nThis will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data\r\nfor this event has the value zero, the manager object was created. Otherwise,\r\nthe record data will contain the NT error code indicating the failure. The\r\nfailure to create the object may be due to low system resources, insufficient\r\nmemory, or disk space.\r\n
0x0000410a | The account-identifier allocator failed to initialize properly.  The record data\r\ncontains the NT error code that caused the failure.  The initialization will be\r\nretried until it succeeds; until that time, account creation will be\r\ndenied on this Domain Controller.  Please look for other SAM event logs that\r\nmay indicate the exact reason for the failure.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation  \r\nwill be retried until the request succeeds. The error is %n " %1 " \r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disbled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove\r\nthe builtin\account operators full control ace from the security descriptor\r\non this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have \r\nan administrator verify the builtin\account operators full control ace was removed \r\nfrom the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators \r\nfull control ace was removed from the security descriptor on this object.\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Domain RODC Password Replication Allowed Group\r\n
0x0000202e | Domain RODC Password Replication Denied Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer domain printers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Terminal Server License Servers\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | All read-only domain controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003002 | SAM failed to update the SAM database. It will try again next time you reboot the machine.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003004 | There are two or more objects that have the same account name attribute in the SAM database. The Distinguished Name of the account is %1. Please contact your system administrator to have all duplicate accounts deleted, but ensure that the original account remains. For computer accounts, the newest account should be retained. In all the other cases, the older account should be kept.\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should precreate the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occured while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400d | Setting the administrator's password to the string you specified failed. Upon reboot the password will be blank; please reset once logged on.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistant data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004014 | The Security Accounts Manager failed to add the Enterprise Admins group to the local Administrators alias. To ensure proper functioning of the domain, please add the account manually.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or localgroup %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004100 | The account-identifier allocator finished initializing. The allocator was initialized with the following identifier values: %1 %2 %3 %4 %5 %6 %7 %8. Check the record data of this event for the initialization status. Zero indicates successful initialization, otherwise the record data contains the NT error code.\r\n
0x00004101 | The account-identifier pool for this domain controller could not be updated. A possible reason for this is that the domain controller may be too busy with other update operations. Subsequent account creations will attempt to update the ID pool until successful.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410a | The account-identifier allocator failed to initialize properly.  The record data contains the NT error code that caused the failure.  The initialization will be retried until it succeeds; until that time, account creation will be denied on this Domain Controller.  Please look for other SAM event logs that may indicate the exact reason for the failure.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disbled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer domain printers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should precreate the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occured while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistant data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or localgroup %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disbled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002033 | RDS Remote Access Servers\r\n
0x00002034 | RDS Endpoint Servers\r\n
0x00002035 | RDS Management Servers\r\n
0x00002036 | Hyper-V Administrators\r\n
0x00002037 | Cloneable Domain Controllers\r\n
0x00002038 | Access Control Assistance Operators\r\n
0x00002039 | Remote Management Users\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer domain printers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x0000212d | Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.\r\n
0x0000212f | Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.\r\n
0x00002130 | Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.\r\n
0x00002131 | Members of this group have complete and unrestricted access to all features of Hyper-V.\r\n
0x00002132 | Members of this group that are domain controllers may be cloned.\r\n
0x00002133 | Members of this group can remotely query authorization attributes and permissions for resources on this computer.\r\n
0x00002134 | Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should pre-create the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occurred while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistent data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or local group %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x0000410d | A pool size for account-identifiers (RIDs) that was configured by an Administrator is greater than the supported maximum. The maximum value of %1 will be used when the domain controller is the RID master. %nSee http://go.microsoft.com/fwlink/?LinkId=225963 for more information.\r\n
0x0000410e | A pool of account-identifiers (RIDs) has been invalidated. This may occur in the following expected cases:%n1. A domain controller is restored from backup. %n2. A domain controller running on a virtual machine is restored from snapshot. %n3. An administrator has manually invalidated the pool. %nSee http://go.microsoft.com/fwlink/?LinkId=226247 for more information.\r\n
0x0000410f | The global maximum for account-identifiers (RIDs) has been increased to %1. %n See http://go.microsoft.com/fwlink/?LinkId=233329 for more information including important operating system interoperability requirements.\r\n
0x00004110 | Action required! An account-identifier (RID) pool was allocated to this domain controller. The pool value indicates this domain has consumed a considerable portion of the total available account-identifiers. %n%nA protection mechanism will be activated when the domain reaches the following threshold of total available account-identifiers remaining: %1.  The protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain. The mechanism will remain active until the Administrator manually re-enables account-identifier allocation on the RID master domain controller. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004111 | Action required! This domain has consumed a considerable portion of the total available account-identifiers (RIDs). A protection mechanism has been activated because the total available account-identifiers remaining is approximately: %1. %n%nThe protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain.  The mechanism will remain active until the Administrator manually re-enables account-identifier (RID) allocation on the RID master domain controller. %n%nIt is extremely important that certain diagnostics be performed prior to re-enabling account creation to ensure this domain is not consuming account-identifiers at an abnormally high rate. Any issues identified should be resolved prior to re-enabling account creation. %n%nFailure to diagnose and fix any underlying issue causing an abnormally high rate of account-identifier consumption can lead to account-identifier (RID) pool exhaustion in the domain after which account creation will be permanently disabled in this domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004112 | This event is a periodic update on the remaining total quantity of available account-identifiers (RIDs). The number of remaining account-identifiers is approximately: %1. %n%nAccount-identifiers are used as accounts are created, when they are exhausted no new accounts may be created in the domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228745 for more information.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disabled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x00004236 | The following invalid claims issued to user %1 have been dropped: %2.\r\n
0x00004237 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004238 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004239 | The password notification DLL %1 failed to load with error %4. Please verify that the notification DLL path defined in the registry, %2%3, refers to a correct and absolute path (<drive>:\<path>\<filename>.<ext>) and not a relative or invalid path. If the DLL path is correct, please validate that any supporting files are located in the same directory, and that the system account has read access to both the DLL path and any supporting files.  Contact the provider of the notification DLL for additional support. Further details can be found on the web at http://go.microsoft.com/fwlink/?LinkId=245898.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002033 | RDS Remote Access Servers\r\n
0x00002034 | RDS Endpoint Servers\r\n
0x00002035 | RDS Management Servers\r\n
0x00002036 | Hyper-V Administrators\r\n
0x00002037 | Cloneable Domain Controllers\r\n
0x00002038 | Access Control Assistance Operators\r\n
0x00002039 | Remote Management Users\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer printers installed on domain controllers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x0000212d | Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.\r\n
0x0000212f | Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.\r\n
0x00002130 | Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.\r\n
0x00002131 | Members of this group have complete and unrestricted access to all features of Hyper-V.\r\n
0x00002132 | Members of this group that are domain controllers may be cloned.\r\n
0x00002133 | Members of this group can remotely query authorization attributes and permissions for resources on this computer.\r\n
0x00002134 | Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.\r\n
0x00002135 | Protected Users\r\n
0x00002136 | Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should pre-create the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occurred while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistent data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or local group %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x0000410d | A pool size for account-identifiers (RIDs) that was configured by an Administrator is greater than the supported maximum. The maximum value of %1 will be used when the domain controller is the RID master. %nSee http://go.microsoft.com/fwlink/?LinkId=225963 for more information.\r\n
0x0000410e | A pool of account-identifiers (RIDs) has been invalidated. This may occur in the following expected cases:%n1. A domain controller is restored from backup. %n2. A domain controller running on a virtual machine is restored from snapshot. %n3. An administrator has manually invalidated the pool. %nSee http://go.microsoft.com/fwlink/?LinkId=226247 for more information.\r\n
0x0000410f | The global maximum for account-identifiers (RIDs) has been increased to %1. %n See http://go.microsoft.com/fwlink/?LinkId=233329 for more information including important operating system interoperability requirements.\r\n
0x00004110 | Action required! An account-identifier (RID) pool was allocated to this domain controller. The pool value indicates this domain has consumed a considerable portion of the total available account-identifiers. %n%nA protection mechanism will be activated when the domain reaches the following threshold of total available account-identifiers remaining: %1.  The protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain. The mechanism will remain active until the Administrator manually re-enables account-identifier allocation on the RID master domain controller. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004111 | Action required! This domain has consumed a considerable portion of the total available account-identifiers (RIDs). A protection mechanism has been activated because the total available account-identifiers remaining is approximately: %1. %n%nThe protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain.  The mechanism will remain active until the Administrator manually re-enables account-identifier (RID) allocation on the RID master domain controller. %n%nIt is extremely important that certain diagnostics be performed prior to re-enabling account creation to ensure this domain is not consuming account-identifiers at an abnormally high rate. Any issues identified should be resolved prior to re-enabling account creation. %n%nFailure to diagnose and fix any underlying issue causing an abnormally high rate of account-identifier consumption can lead to account-identifier (RID) pool exhaustion in the domain after which account creation will be permanently disabled in this domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004112 | This event is a periodic update on the remaining total quantity of available account-identifiers (RIDs). The number of remaining account-identifiers is approximately: %1. %n%nAccount-identifiers are used as accounts are created, when they are exhausted no new accounts may be created in the domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228745 for more information.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disabled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x00004236 | The following invalid claims issued to user %1 have been dropped: %2.\r\n
0x00004237 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004238 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004239 | The password notification DLL %1 failed to load with error %4. Please verify that the notification DLL path defined in the registry, %2%3, refers to a correct and absolute path (<drive>:\<path>\<filename>.<ext>) and not a relative or invalid path. If the DLL path is correct, please validate that any supporting files are located in the same directory, and that the system account has read access to both the DLL path and any supporting files.  Contact the provider of the notification DLL for additional support. Further details can be found on the web at http://go.microsoft.com/fwlink/?LinkId=245898.\r\n
0x00004240 | SAM was configured to not listen on the TCP protocol.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n

### 6.3.9600.18621

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002033 | RDS Remote Access Servers\r\n
0x00002034 | RDS Endpoint Servers\r\n
0x00002035 | RDS Management Servers\r\n
0x00002036 | Hyper-V Administrators\r\n
0x00002037 | Cloneable Domain Controllers\r\n
0x00002038 | Access Control Assistance Operators\r\n
0x00002039 | Remote Management Users\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer printers installed on domain controllers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x0000212d | Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.\r\n
0x0000212f | Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.\r\n
0x00002130 | Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.\r\n
0x00002131 | Members of this group have complete and unrestricted access to all features of Hyper-V.\r\n
0x00002132 | Members of this group that are domain controllers may be cloned.\r\n
0x00002133 | Members of this group can remotely query authorization attributes and permissions for resources on this computer.\r\n
0x00002134 | Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.\r\n
0x00002135 | Protected Users\r\n
0x00002136 | Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should pre-create the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occurred while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistent data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or local group %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x0000410d | A pool size for account-identifiers (RIDs) that was configured by an Administrator is greater than the supported maximum. The maximum value of %1 will be used when the domain controller is the RID master. %nSee http://go.microsoft.com/fwlink/?LinkId=225963 for more information.\r\n
0x0000410e | A pool of account-identifiers (RIDs) has been invalidated. This may occur in the following expected cases:%n1. A domain controller is restored from backup. %n2. A domain controller running on a virtual machine is restored from snapshot. %n3. An administrator has manually invalidated the pool. %nSee http://go.microsoft.com/fwlink/?LinkId=226247 for more information.\r\n
0x0000410f | The global maximum for account-identifiers (RIDs) has been increased to %1. %n See http://go.microsoft.com/fwlink/?LinkId=233329 for more information including important operating system interoperability requirements.\r\n
0x00004110 | Action required! An account-identifier (RID) pool was allocated to this domain controller. The pool value indicates this domain has consumed a considerable portion of the total available account-identifiers. %n%nA protection mechanism will be activated when the domain reaches the following threshold of total available account-identifiers remaining: %1.  The protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain. The mechanism will remain active until the Administrator manually re-enables account-identifier allocation on the RID master domain controller. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004111 | Action required! This domain has consumed a considerable portion of the total available account-identifiers (RIDs). A protection mechanism has been activated because the total available account-identifiers remaining is approximately: %1. %n%nThe protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain.  The mechanism will remain active until the Administrator manually re-enables account-identifier (RID) allocation on the RID master domain controller. %n%nIt is extremely important that certain diagnostics be performed prior to re-enabling account creation to ensure this domain is not consuming account-identifiers at an abnormally high rate. Any issues identified should be resolved prior to re-enabling account creation. %n%nFailure to diagnose and fix any underlying issue causing an abnormally high rate of account-identifier consumption can lead to account-identifier (RID) pool exhaustion in the domain after which account creation will be permanently disabled in this domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004112 | This event is a periodic update on the remaining total quantity of available account-identifiers (RIDs). The number of remaining account-identifiers is approximately: %1. %n%nAccount-identifiers are used as accounts are created, when they are exhausted no new accounts may be created in the domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228745 for more information.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disabled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x00004236 | The following invalid claims issued to user %1 have been dropped: %2.\r\n
0x00004237 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004238 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004239 | The password notification DLL %1 failed to load with error %4. Please verify that the notification DLL path defined in the registry, %2%3, refers to a correct and absolute path (<drive>:\<path>\<filename>.<ext>) and not a relative or invalid path. If the DLL path is correct, please validate that any supporting files are located in the same directory, and that the system account has read access to both the DLL path and any supporting files.  Contact the provider of the notification DLL for additional support. Further details can be found on the web at http://go.microsoft.com/fwlink/?LinkId=245898.\r\n
0x00004240 | SAM was configured to not listen on the TCP protocol.\r\n
0x00004242 | Remote calls to the SAM database are being restricted using the default security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004243 | Remote calls to the SAM database are being restricted using the configured registry security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004244 | The registry security descriptor is malformed: %1.%nRemote calls to the SAM database are being restricted using the default security descriptor: %2.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004245 | A remote call to the SAM database has been denied.%nClient SID: %1%nNetwork address: %2%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004246 | Audit only mode is now enabled for remote calls to the SAM database. SAM will log an event for clients who would have been denied access in normal mode. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004247 | Audit only mode is now disabled for remote calls to the SAM database.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004248 | Audit only mode is currently enabled for remote calls to the SAM database.%nThe following client would have been normally denied access:%nClient SID: %1 from network address: %2. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004249 | %2 remote calls to the SAM database have been denied in the past %1 seconds throttling window.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002033 | RDS Remote Access Servers\r\n
0x00002034 | RDS Endpoint Servers\r\n
0x00002035 | RDS Management Servers\r\n
0x00002036 | Hyper-V Administrators\r\n
0x00002037 | Cloneable Domain Controllers\r\n
0x00002038 | Access Control Assistance Operators\r\n
0x00002039 | Remote Management Users\r\n
0x0000203a | DefaultAccount\r\n
0x0000203b | System Managed Accounts Group\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer printers installed on domain controllers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x0000212d | Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.\r\n
0x0000212f | Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.\r\n
0x00002130 | Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.\r\n
0x00002131 | Members of this group have complete and unrestricted access to all features of Hyper-V.\r\n
0x00002132 | Members of this group that are domain controllers may be cloned.\r\n
0x00002133 | Members of this group can remotely query authorization attributes and permissions for resources on this computer.\r\n
0x00002134 | Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.\r\n
0x00002135 | Protected Users\r\n
0x00002136 | Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.\r\n
0x00002137 | A user account managed by the system.\r\n
0x00002138 | Members of this group are managed by the system.\r\n
0x00002139 | Storage Replica Administrators\r\n
0x0000213a | Members of this group have complete and unrestricted access to all features of Storage Replica.\r\n
0x0000213b | Key Admins\r\n
0x0000213c | Members of this group can perform administrative actions on key objects within the domain.\r\n
0x0000213d | Enterprise Key Admins\r\n
0x0000213e | Members of this group can perform administrative actions on key objects within the forest.\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should pre-create the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occurred while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistent data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or local group %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x0000410d | A pool size for account-identifiers (RIDs) that was configured by an Administrator is greater than the supported maximum. The maximum value of %1 will be used when the domain controller is the RID master. %nSee http://go.microsoft.com/fwlink/?LinkId=225963 for more information.\r\n
0x0000410e | A pool of account-identifiers (RIDs) has been invalidated. This may occur in the following expected cases:%n1. A domain controller is restored from backup. %n2. A domain controller running on a virtual machine is restored from snapshot. %n3. An administrator has manually invalidated the pool. %nSee http://go.microsoft.com/fwlink/?LinkId=226247 for more information.\r\n
0x0000410f | The global maximum for account-identifiers (RIDs) has been increased to %1. %n See http://go.microsoft.com/fwlink/?LinkId=233329 for more information including important operating system interoperability requirements.\r\n
0x00004110 | Action required! An account-identifier (RID) pool was allocated to this domain controller. The pool value indicates this domain has consumed a considerable portion of the total available account-identifiers. %n%nA protection mechanism will be activated when the domain reaches the following threshold of total available account-identifiers remaining: %1.  The protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain. The mechanism will remain active until the Administrator manually re-enables account-identifier allocation on the RID master domain controller. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004111 | Action required! This domain has consumed a considerable portion of the total available account-identifiers (RIDs). A protection mechanism has been activated because the total available account-identifiers remaining is approximately: %1. %n%nThe protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain.  The mechanism will remain active until the Administrator manually re-enables account-identifier (RID) allocation on the RID master domain controller. %n%nIt is extremely important that certain diagnostics be performed prior to re-enabling account creation to ensure this domain is not consuming account-identifiers at an abnormally high rate. Any issues identified should be resolved prior to re-enabling account creation. %n%nFailure to diagnose and fix any underlying issue causing an abnormally high rate of account-identifier consumption can lead to account-identifier (RID) pool exhaustion in the domain after which account creation will be permanently disabled in this domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004112 | This event is a periodic update on the remaining total quantity of available account-identifiers (RIDs). The number of remaining account-identifiers is approximately: %1. %n%nAccount-identifiers are used as accounts are created, when they are exhausted no new accounts may be created in the domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228745 for more information.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disabled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x00004236 | The following invalid claims issued to user %1 have been dropped: %2.\r\n
0x00004237 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004238 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004239 | The password notification DLL %1 failed to load with error %4. Please verify that the notification DLL path defined in the registry, %2%3, refers to a correct and absolute path (<drive>:\<path>\<filename>.<ext>) and not a relative or invalid path. If the DLL path is correct, please validate that any supporting files are located in the same directory, and that the system account has read access to both the DLL path and any supporting files.  Contact the provider of the notification DLL for additional support. Further details can be found on the web at http://go.microsoft.com/fwlink/?LinkId=245898.\r\n
0x00004240 | SAM was configured to not listen on the TCP protocol.\r\n
0x00004241 | Legacy password validation mode has been enabled on this machine. If an Exchange ActiveSync policy is configured it will not be enforced for password validation requests.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002033 | RDS Remote Access Servers\r\n
0x00002034 | RDS Endpoint Servers\r\n
0x00002035 | RDS Management Servers\r\n
0x00002036 | Hyper-V Administrators\r\n
0x00002037 | Cloneable Domain Controllers\r\n
0x00002038 | Access Control Assistance Operators\r\n
0x00002039 | Remote Management Users\r\n
0x0000203a | DefaultAccount\r\n
0x0000203b | System Managed Accounts Group\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer printers installed on domain controllers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x0000212d | Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.\r\n
0x0000212f | Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.\r\n
0x00002130 | Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.\r\n
0x00002131 | Members of this group have complete and unrestricted access to all features of Hyper-V.\r\n
0x00002132 | Members of this group that are domain controllers may be cloned.\r\n
0x00002133 | Members of this group can remotely query authorization attributes and permissions for resources on this computer.\r\n
0x00002134 | Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.\r\n
0x00002135 | Protected Users\r\n
0x00002136 | Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.\r\n
0x00002137 | A user account managed by the system.\r\n
0x00002138 | Members of this group are managed by the system.\r\n
0x00002139 | Storage Replica Administrators\r\n
0x0000213a | Members of this group have complete and unrestricted access to all features of Storage Replica.\r\n
0x0000213b | Key Admins\r\n
0x0000213c | Members of this group can perform administrative actions on key objects within the domain.\r\n
0x0000213d | Enterprise Key Admins\r\n
0x0000213e | Members of this group can perform administrative actions on key objects within the forest.\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should pre-create the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occurred while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistent data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or local group %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x0000410d | A pool size for account-identifiers (RIDs) that was configured by an Administrator is greater than the supported maximum. The maximum value of %1 will be used when the domain controller is the RID master. %nSee http://go.microsoft.com/fwlink/?LinkId=225963 for more information.\r\n
0x0000410e | A pool of account-identifiers (RIDs) has been invalidated. This may occur in the following expected cases:%n1. A domain controller is restored from backup. %n2. A domain controller running on a virtual machine is restored from snapshot. %n3. An administrator has manually invalidated the pool. %nSee http://go.microsoft.com/fwlink/?LinkId=226247 for more information.\r\n
0x0000410f | The global maximum for account-identifiers (RIDs) has been increased to %1. %n See http://go.microsoft.com/fwlink/?LinkId=233329 for more information including important operating system interoperability requirements.\r\n
0x00004110 | Action required! An account-identifier (RID) pool was allocated to this domain controller. The pool value indicates this domain has consumed a considerable portion of the total available account-identifiers. %n%nA protection mechanism will be activated when the domain reaches the following threshold of total available account-identifiers remaining: %1.  The protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain. The mechanism will remain active until the Administrator manually re-enables account-identifier allocation on the RID master domain controller. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004111 | Action required! This domain has consumed a considerable portion of the total available account-identifiers (RIDs). A protection mechanism has been activated because the total available account-identifiers remaining is approximately: %1. %n%nThe protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain.  The mechanism will remain active until the Administrator manually re-enables account-identifier (RID) allocation on the RID master domain controller. %n%nIt is extremely important that certain diagnostics be performed prior to re-enabling account creation to ensure this domain is not consuming account-identifiers at an abnormally high rate. Any issues identified should be resolved prior to re-enabling account creation. %n%nFailure to diagnose and fix any underlying issue causing an abnormally high rate of account-identifier consumption can lead to account-identifier (RID) pool exhaustion in the domain after which account creation will be permanently disabled in this domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004112 | This event is a periodic update on the remaining total quantity of available account-identifiers (RIDs). The number of remaining account-identifiers is approximately: %1. %n%nAccount-identifiers are used as accounts are created, when they are exhausted no new accounts may be created in the domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228745 for more information.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disabled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x00004236 | The following invalid claims issued to user %1 have been dropped: %2.\r\n
0x00004237 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004238 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004239 | The password notification DLL %1 failed to load with error %4. Please verify that the notification DLL path defined in the registry, %2%3, refers to a correct and absolute path (<drive>:\<path>\<filename>.<ext>) and not a relative or invalid path. If the DLL path is correct, please validate that any supporting files are located in the same directory, and that the system account has read access to both the DLL path and any supporting files.  Contact the provider of the notification DLL for additional support. Further details can be found on the web at http://go.microsoft.com/fwlink/?LinkId=245898.\r\n
0x00004240 | SAM was configured to not listen on the TCP protocol.\r\n
0x00004241 | Legacy password validation mode has been enabled on this machine. If an Exchange ActiveSync policy is configured it will not be enforced for password validation requests.\r\n
0x00004242 | Remote calls to the SAM database are being restricted using the default security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004243 | Remote calls to the SAM database are being restricted using the configured registry security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004244 | The registry security descriptor is malformed: %1.%nRemote calls to the SAM database are being restricted using the default security descriptor: %2.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004245 | A remote call to the SAM database has been denied.%nClient SID: %1%nNetwork address: %2%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004246 | Audit only mode is now enabled for remote calls to the SAM database. SAM will log an event for clients who would have been denied access in normal mode. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004247 | Audit only mode is now disabled for remote calls to the SAM database.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004248 | Audit only mode is currently enabled for remote calls to the SAM database.%nThe following client would have been normally denied access:%nClient SID: %1 from network address: %2. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004249 | %2 remote calls to the SAM database have been denied in the past %1 seconds throttling window.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002033 | RDS Remote Access Servers\r\n
0x00002034 | RDS Endpoint Servers\r\n
0x00002035 | RDS Management Servers\r\n
0x00002036 | Hyper-V Administrators\r\n
0x00002037 | Cloneable Domain Controllers\r\n
0x00002038 | Access Control Assistance Operators\r\n
0x00002039 | Remote Management Users\r\n
0x0000203a | DefaultAccount\r\n
0x0000203b | System Managed Accounts Group\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer printers installed on domain controllers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x0000212d | Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.\r\n
0x0000212f | Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.\r\n
0x00002130 | Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.\r\n
0x00002131 | Members of this group have complete and unrestricted access to all features of Hyper-V.\r\n
0x00002132 | Members of this group that are domain controllers may be cloned.\r\n
0x00002133 | Members of this group can remotely query authorization attributes and permissions for resources on this computer.\r\n
0x00002134 | Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.\r\n
0x00002135 | Protected Users\r\n
0x00002136 | Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.\r\n
0x00002137 | A user account managed by the system.\r\n
0x00002138 | Members of this group are managed by the system.\r\n
0x00002139 | Storage Replica Administrators\r\n
0x0000213a | Members of this group have complete and unrestricted access to all features of Storage Replica.\r\n
0x0000213b | Key Admins\r\n
0x0000213c | Members of this group can perform administrative actions on key objects within the domain.\r\n
0x0000213d | Enterprise Key Admins\r\n
0x0000213e | Members of this group can perform administrative actions on key objects within the forest.\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should pre-create the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occurred while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistent data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or local group %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x0000410d | A pool size for account-identifiers (RIDs) that was configured by an Administrator is greater than the supported maximum. The maximum value of %1 will be used when the domain controller is the RID master. %nSee http://go.microsoft.com/fwlink/?LinkId=225963 for more information.\r\n
0x0000410e | A pool of account-identifiers (RIDs) has been invalidated. This may occur in the following expected cases:%n1. A domain controller is restored from backup. %n2. A domain controller running on a virtual machine is restored from snapshot. %n3. An administrator has manually invalidated the pool. %nSee http://go.microsoft.com/fwlink/?LinkId=226247 for more information.\r\n
0x0000410f | The global maximum for account-identifiers (RIDs) has been increased to %1. %n See http://go.microsoft.com/fwlink/?LinkId=233329 for more information including important operating system interoperability requirements.\r\n
0x00004110 | Action required! An account-identifier (RID) pool was allocated to this domain controller. The pool value indicates this domain has consumed a considerable portion of the total available account-identifiers. %n%nA protection mechanism will be activated when the domain reaches the following threshold of total available account-identifiers remaining: %1.  The protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain. The mechanism will remain active until the Administrator manually re-enables account-identifier allocation on the RID master domain controller. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004111 | Action required! This domain has consumed a considerable portion of the total available account-identifiers (RIDs). A protection mechanism has been activated because the total available account-identifiers remaining is approximately: %1. %n%nThe protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain.  The mechanism will remain active until the Administrator manually re-enables account-identifier (RID) allocation on the RID master domain controller. %n%nIt is extremely important that certain diagnostics be performed prior to re-enabling account creation to ensure this domain is not consuming account-identifiers at an abnormally high rate. Any issues identified should be resolved prior to re-enabling account creation. %n%nFailure to diagnose and fix any underlying issue causing an abnormally high rate of account-identifier consumption can lead to account-identifier (RID) pool exhaustion in the domain after which account creation will be permanently disabled in this domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004112 | This event is a periodic update on the remaining total quantity of available account-identifiers (RIDs). The number of remaining account-identifiers is approximately: %1. %n%nAccount-identifiers are used as accounts are created, when they are exhausted no new accounts may be created in the domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228745 for more information.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disabled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x00004236 | The following invalid claims issued to user %1 have been dropped: %2.\r\n
0x00004237 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004238 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004239 | The password notification DLL %1 failed to load with error %4. Please verify that the notification DLL path defined in the registry, %2%3, refers to a correct and absolute path (<drive>:\<path>\<filename>.<ext>) and not a relative or invalid path. If the DLL path is correct, please validate that any supporting files are located in the same directory, and that the system account has read access to both the DLL path and any supporting files.  Contact the provider of the notification DLL for additional support. Further details can be found on the web at http://go.microsoft.com/fwlink/?LinkId=245898.\r\n
0x00004240 | SAM was configured to not listen on the TCP protocol.\r\n
0x00004241 | Legacy password validation mode has been enabled on this machine. If an Exchange ActiveSync policy is configured it will not be enforced for password validation requests.\r\n
0x00004242 | Remote calls to the SAM database are being restricted using the default security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004243 | Remote calls to the SAM database are being restricted using the configured registry security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004244 | The registry security descriptor is malformed: %1.%nRemote calls to the SAM database are being restricted using the default security descriptor: %2.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004245 | A remote call to the SAM database has been denied.%nClient SID: %1%nNetwork address: %2%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004246 | Audit only mode is now enabled for remote calls to the SAM database. SAM will log an event for clients who would have been denied access in normal mode. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004247 | Audit only mode is now disabled for remote calls to the SAM database.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004248 | Audit only mode is currently enabled for remote calls to the SAM database.%nThe following client would have been normally denied access:%nClient SID: %1 from network address: %2. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004249 | %2 remote calls to the SAM database have been denied in the past %1 seconds throttling window.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004250 | An error occurred while configuring one or more well-known accounts for this domain.  This may be due to a transient error condition. The task will retry periodically until successful. For more information please see https://go.microsoft.com/fwlink/?linkid=832473.%nStatus: %1\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002033 | RDS Remote Access Servers\r\n
0x00002034 | RDS Endpoint Servers\r\n
0x00002035 | RDS Management Servers\r\n
0x00002036 | Hyper-V Administrators\r\n
0x00002037 | Cloneable Domain Controllers\r\n
0x00002038 | Access Control Assistance Operators\r\n
0x00002039 | Remote Management Users\r\n
0x0000203a | DefaultAccount\r\n
0x0000203b | System Managed Accounts Group\r\n
0x0000203c | WDAGUtilityAccount\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer printers installed on domain controllers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x0000212d | Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.\r\n
0x0000212f | Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.\r\n
0x00002130 | Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.\r\n
0x00002131 | Members of this group have complete and unrestricted access to all features of Hyper-V.\r\n
0x00002132 | Members of this group that are domain controllers may be cloned.\r\n
0x00002133 | Members of this group can remotely query authorization attributes and permissions for resources on this computer.\r\n
0x00002134 | Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.\r\n
0x00002135 | Protected Users\r\n
0x00002136 | Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.\r\n
0x00002137 | A user account managed by the system.\r\n
0x00002138 | Members of this group are managed by the system.\r\n
0x00002139 | Storage Replica Administrators\r\n
0x0000213a | Members of this group have complete and unrestricted access to all features of Storage Replica.\r\n
0x0000213b | Key Admins\r\n
0x0000213c | Members of this group can perform administrative actions on key objects within the domain.\r\n
0x0000213d | Enterprise Key Admins\r\n
0x0000213e | Members of this group can perform administrative actions on key objects within the forest.\r\n
0x0000213f | A user account managed and used by the system for Windows Defender Application Guard scenarios.\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should pre-create the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occurred while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistent data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or local group %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x0000410d | A pool size for account-identifiers (RIDs) that was configured by an Administrator is greater than the supported maximum. The maximum value of %1 will be used when the domain controller is the RID master. %nSee http://go.microsoft.com/fwlink/?LinkId=225963 for more information.\r\n
0x0000410e | A pool of account-identifiers (RIDs) has been invalidated. This may occur in the following expected cases:%n1. A domain controller is restored from backup. %n2. A domain controller running on a virtual machine is restored from snapshot. %n3. An administrator has manually invalidated the pool. %nSee http://go.microsoft.com/fwlink/?LinkId=226247 for more information.\r\n
0x0000410f | The global maximum for account-identifiers (RIDs) has been increased to %1. %n See http://go.microsoft.com/fwlink/?LinkId=233329 for more information including important operating system interoperability requirements.\r\n
0x00004110 | Action required! An account-identifier (RID) pool was allocated to this domain controller. The pool value indicates this domain has consumed a considerable portion of the total available account-identifiers. %n%nA protection mechanism will be activated when the domain reaches the following threshold of total available account-identifiers remaining: %1.  The protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain. The mechanism will remain active until the Administrator manually re-enables account-identifier allocation on the RID master domain controller. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004111 | Action required! This domain has consumed a considerable portion of the total available account-identifiers (RIDs). A protection mechanism has been activated because the total available account-identifiers remaining is approximately: %1. %n%nThe protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain.  The mechanism will remain active until the Administrator manually re-enables account-identifier (RID) allocation on the RID master domain controller. %n%nIt is extremely important that certain diagnostics be performed prior to re-enabling account creation to ensure this domain is not consuming account-identifiers at an abnormally high rate. Any issues identified should be resolved prior to re-enabling account creation. %n%nFailure to diagnose and fix any underlying issue causing an abnormally high rate of account-identifier consumption can lead to account-identifier (RID) pool exhaustion in the domain after which account creation will be permanently disabled in this domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004112 | This event is a periodic update on the remaining total quantity of available account-identifiers (RIDs). The number of remaining account-identifiers is approximately: %1. %n%nAccount-identifiers are used as accounts are created, when they are exhausted no new accounts may be created in the domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228745 for more information.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disabled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x00004236 | The following invalid claims issued to user %1 have been dropped: %2.\r\n
0x00004237 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004238 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004239 | The password notification DLL %1 failed to load with error %4. Please verify that the notification DLL path defined in the registry, %2%3, refers to a correct and absolute path (<drive>:\<path>\<filename>.<ext>) and not a relative or invalid path. If the DLL path is correct, please validate that any supporting files are located in the same directory, and that the system account has read access to both the DLL path and any supporting files.  Contact the provider of the notification DLL for additional support. Further details can be found on the web at http://go.microsoft.com/fwlink/?LinkId=245898.\r\n
0x00004240 | SAM was configured to not listen on the TCP protocol.\r\n
0x00004241 | Legacy password validation mode has been enabled on this machine. If an Exchange ActiveSync policy is configured it will not be enforced for password validation requests.\r\n
0x00004242 | Remote calls to the SAM database are being restricted using the default security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004243 | Remote calls to the SAM database are being restricted using the configured registry security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004244 | The registry security descriptor is malformed: %1.%nRemote calls to the SAM database are being restricted using the default security descriptor: %2.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004245 | A remote call to the SAM database has been denied.%nClient SID: %1%nNetwork address: %2%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004246 | Audit only mode is now enabled for remote calls to the SAM database. SAM will log an event for clients who would have been denied access in normal mode. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004247 | Audit only mode is now disabled for remote calls to the SAM database.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004248 | Audit only mode is currently enabled for remote calls to the SAM database.%nThe following client would have been normally denied access:%nClient SID: %1 from network address: %2. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004249 | %2 remote calls to the SAM database have been denied in the past %1 seconds throttling window.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004250 | An error occurred while configuring one or more well-known accounts for this domain.  This may be due to a transient error condition. The task will retry periodically until successful. For more information please see https://go.microsoft.com/fwlink/?linkid=832473.%nStatus: %1\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n

### 10.0.17134.1, 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002033 | RDS Remote Access Servers\r\n
0x00002034 | RDS Endpoint Servers\r\n
0x00002035 | RDS Management Servers\r\n
0x00002036 | Hyper-V Administrators\r\n
0x00002037 | Cloneable Domain Controllers\r\n
0x00002038 | Access Control Assistance Operators\r\n
0x00002039 | Remote Management Users\r\n
0x0000203a | DefaultAccount\r\n
0x0000203b | System Managed Accounts Group\r\n
0x0000203c | WDAGUtilityAccount\r\n
0x0000203d | Device Owners\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer printers installed on domain controllers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x0000212d | Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.\r\n
0x0000212f | Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.\r\n
0x00002130 | Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.\r\n
0x00002131 | Members of this group have complete and unrestricted access to all features of Hyper-V.\r\n
0x00002132 | Members of this group that are domain controllers may be cloned.\r\n
0x00002133 | Members of this group can remotely query authorization attributes and permissions for resources on this computer.\r\n
0x00002134 | Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.\r\n
0x00002135 | Protected Users\r\n
0x00002136 | Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.\r\n
0x00002137 | A user account managed by the system.\r\n
0x00002138 | Members of this group are managed by the system.\r\n
0x00002139 | Storage Replica Administrators\r\n
0x0000213a | Members of this group have complete and unrestricted access to all features of Storage Replica.\r\n
0x0000213b | Key Admins\r\n
0x0000213c | Members of this group can perform administrative actions on key objects within the domain.\r\n
0x0000213d | Enterprise Key Admins\r\n
0x0000213e | Members of this group can perform administrative actions on key objects within the forest.\r\n
0x0000213f | A user account managed and used by the system for Windows Defender Application Guard scenarios.\r\n
0x00002140 | Members of this group can change system-wide settings.\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should pre-create the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occurred while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistent data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or local group %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x0000410d | A pool size for account-identifiers (RIDs) that was configured by an Administrator is greater than the supported maximum. The maximum value of %1 will be used when the domain controller is the RID master. %nSee http://go.microsoft.com/fwlink/?LinkId=225963 for more information.\r\n
0x0000410e | A pool of account-identifiers (RIDs) has been invalidated. This may occur in the following expected cases:%n1. A domain controller is restored from backup. %n2. A domain controller running on a virtual machine is restored from snapshot. %n3. An administrator has manually invalidated the pool. %nSee http://go.microsoft.com/fwlink/?LinkId=226247 for more information.\r\n
0x0000410f | The global maximum for account-identifiers (RIDs) has been increased to %1. %n See http://go.microsoft.com/fwlink/?LinkId=233329 for more information including important operating system interoperability requirements.\r\n
0x00004110 | Action required! An account-identifier (RID) pool was allocated to this domain controller. The pool value indicates this domain has consumed a considerable portion of the total available account-identifiers. %n%nA protection mechanism will be activated when the domain reaches the following threshold of total available account-identifiers remaining: %1.  The protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain. The mechanism will remain active until the Administrator manually re-enables account-identifier allocation on the RID master domain controller. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004111 | Action required! This domain has consumed a considerable portion of the total available account-identifiers (RIDs). A protection mechanism has been activated because the total available account-identifiers remaining is approximately: %1. %n%nThe protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain.  The mechanism will remain active until the Administrator manually re-enables account-identifier (RID) allocation on the RID master domain controller. %n%nIt is extremely important that certain diagnostics be performed prior to re-enabling account creation to ensure this domain is not consuming account-identifiers at an abnormally high rate. Any issues identified should be resolved prior to re-enabling account creation. %n%nFailure to diagnose and fix any underlying issue causing an abnormally high rate of account-identifier consumption can lead to account-identifier (RID) pool exhaustion in the domain after which account creation will be permanently disabled in this domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004112 | This event is a periodic update on the remaining total quantity of available account-identifiers (RIDs). The number of remaining account-identifiers is approximately: %1. %n%nAccount-identifiers are used as accounts are created, when they are exhausted no new accounts may be created in the domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228745 for more information.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disabled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x00004236 | The following invalid claims issued to user %1 have been dropped: %2.\r\n
0x00004237 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004238 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004239 | The password notification DLL %1 failed to load with error %4. Please verify that the notification DLL path defined in the registry, %2%3, refers to a correct and absolute path (<drive>:\<path>\<filename>.<ext>) and not a relative or invalid path. If the DLL path is correct, please validate that any supporting files are located in the same directory, and that the system account has read access to both the DLL path and any supporting files.  Contact the provider of the notification DLL for additional support. Further details can be found on the web at http://go.microsoft.com/fwlink/?LinkId=245898.\r\n
0x00004240 | SAM was configured to not listen on the TCP protocol.\r\n
0x00004241 | Legacy password validation mode has been enabled on this machine. If an Exchange ActiveSync policy is configured it will not be enforced for password validation requests.\r\n
0x00004242 | Remote calls to the SAM database are being restricted using the default security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004243 | Remote calls to the SAM database are being restricted using the configured registry security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004244 | The registry security descriptor is malformed: %1.%nRemote calls to the SAM database are being restricted using the default security descriptor: %2.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004245 | A remote call to the SAM database has been denied.%nClient SID: %1%nNetwork address: %2%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004246 | Audit only mode is now enabled for remote calls to the SAM database. SAM will log an event for clients who would have been denied access in normal mode. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004247 | Audit only mode is now disabled for remote calls to the SAM database.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004248 | Audit only mode is currently enabled for remote calls to the SAM database.%nThe following client would have been normally denied access:%nClient SID: %1 from network address: %2. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004249 | %2 remote calls to the SAM database have been denied in the past %1 seconds throttling window.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004250 | An error occurred while configuring one or more well-known accounts for this domain.  This may be due to a transient error condition. The task will retry periodically until successful. For more information please see https://go.microsoft.com/fwlink/?linkid=832473.%nStatus: %1\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002033 | RDS Remote Access Servers\r\n
0x00002034 | RDS Endpoint Servers\r\n
0x00002035 | RDS Management Servers\r\n
0x00002036 | Hyper-V Administrators\r\n
0x00002037 | Cloneable Domain Controllers\r\n
0x00002038 | Access Control Assistance Operators\r\n
0x00002039 | Remote Management Users\r\n
0x0000203a | DefaultAccount\r\n
0x0000203b | System Managed Accounts Group\r\n
0x0000203c | WDAGUtilityAccount\r\n
0x0000203d | Device Owners\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer printers installed on domain controllers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x0000212d | Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.\r\n
0x0000212f | Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.\r\n
0x00002130 | Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.\r\n
0x00002131 | Members of this group have complete and unrestricted access to all features of Hyper-V.\r\n
0x00002132 | Members of this group that are domain controllers may be cloned.\r\n
0x00002133 | Members of this group can remotely query authorization attributes and permissions for resources on this computer.\r\n
0x00002134 | Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.\r\n
0x00002135 | Protected Users\r\n
0x00002136 | Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.\r\n
0x00002137 | A user account managed by the system.\r\n
0x00002138 | Members of this group are managed by the system.\r\n
0x00002139 | Storage Replica Administrators\r\n
0x0000213a | Members of this group have complete and unrestricted access to all features of Storage Replica.\r\n
0x0000213b | Key Admins\r\n
0x0000213c | Members of this group can perform administrative actions on key objects within the domain.\r\n
0x0000213d | Enterprise Key Admins\r\n
0x0000213e | Members of this group can perform administrative actions on key objects within the forest.\r\n
0x0000213f | A user account managed and used by the system for Windows Defender Application Guard scenarios.\r\n
0x00002140 | Members of this group can change system-wide settings.\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should pre-create the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occurred while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistent data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or local group %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x0000410d | A pool size for account-identifiers (RIDs) that was configured by an Administrator is greater than the supported maximum. The maximum value of %1 will be used when the domain controller is the RID master. %nSee http://go.microsoft.com/fwlink/?LinkId=225963 for more information.\r\n
0x0000410e | A pool of account-identifiers (RIDs) has been invalidated. This may occur in the following expected cases:%n1. A domain controller is restored from backup. %n2. A domain controller running on a virtual machine is restored from snapshot. %n3. An administrator has manually invalidated the pool. %nSee http://go.microsoft.com/fwlink/?LinkId=226247 for more information.\r\n
0x0000410f | The global maximum for account-identifiers (RIDs) has been increased to %1. %n See http://go.microsoft.com/fwlink/?LinkId=233329 for more information including important operating system interoperability requirements.\r\n
0x00004110 | Action required! An account-identifier (RID) pool was allocated to this domain controller. The pool value indicates this domain has consumed a considerable portion of the total available account-identifiers. %n%nA protection mechanism will be activated when the domain reaches the following threshold of total available account-identifiers remaining: %1.  The protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain. The mechanism will remain active until the Administrator manually re-enables account-identifier allocation on the RID master domain controller. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004111 | Action required! This domain has consumed a considerable portion of the total available account-identifiers (RIDs). A protection mechanism has been activated because the total available account-identifiers remaining is approximately: %1. %n%nThe protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain.  The mechanism will remain active until the Administrator manually re-enables account-identifier (RID) allocation on the RID master domain controller. %n%nIt is extremely important that certain diagnostics be performed prior to re-enabling account creation to ensure this domain is not consuming account-identifiers at an abnormally high rate. Any issues identified should be resolved prior to re-enabling account creation. %n%nFailure to diagnose and fix any underlying issue causing an abnormally high rate of account-identifier consumption can lead to account-identifier (RID) pool exhaustion in the domain after which account creation will be permanently disabled in this domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004112 | This event is a periodic update on the remaining total quantity of available account-identifiers (RIDs). The number of remaining account-identifiers is approximately: %1. %n%nAccount-identifiers are used as accounts are created, when they are exhausted no new accounts may be created in the domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228745 for more information.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disabled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x00004236 | The following invalid claims issued to user %1 have been dropped: %2.\r\n
0x00004237 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004238 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004239 | The password notification DLL %1 failed to load with error %4. Please verify that the notification DLL path defined in the registry, %2%3, refers to a correct and absolute path (<drive>:\<path>\<filename>.<ext>) and not a relative or invalid path. If the DLL path is correct, please validate that any supporting files are located in the same directory, and that the system account has read access to both the DLL path and any supporting files.  Contact the provider of the notification DLL for additional support. Further details can be found on the web at http://go.microsoft.com/fwlink/?LinkId=245898.\r\n
0x00004240 | SAM was configured to not listen on the TCP protocol.\r\n
0x00004241 | Legacy password validation mode has been enabled on this machine. If an Exchange ActiveSync policy is configured it will not be enforced for password validation requests.\r\n
0x00004242 | Remote calls to the SAM database are being restricted using the default security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004243 | Remote calls to the SAM database are being restricted using the configured registry security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004244 | The registry security descriptor is malformed: %1.%nRemote calls to the SAM database are being restricted using the default security descriptor: %2.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004245 | A remote call to the SAM database has been denied.%nClient SID: %1%nNetwork address: %2%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004246 | Audit only mode is now enabled for remote calls to the SAM database. SAM will log an event for clients who would have been denied access in normal mode. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004247 | Audit only mode is now disabled for remote calls to the SAM database.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004248 | Audit only mode is currently enabled for remote calls to the SAM database.%nThe following client would have been normally denied access:%nClient SID: %1 from network address: %2. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004249 | %2 remote calls to the SAM database have been denied in the past %1 seconds throttling window.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004250 | An error occurred while configuring one or more well-known accounts for this domain.  This may be due to a transient error condition. The task will retry periodically until successful. For more information please see https://go.microsoft.com/fwlink/?linkid=832473.%nStatus: %1\r\n
0x00004251 | The domain is configured with the following minimum password length-related settings.%n%nMinimumPasswordLength: %1%n%nRelaxMinimumPasswordLengthLimits: %2%n%nMinimumPasswordLengthAudit: %3%n%nFor more information see https://go.microsoft.com/fwlink/?LinkId=2097191.%n\r\n
0x00004252 | The following account has been configured with a password whose length is shorter than the current MinimumPasswordLengthAudit setting.%n%nAccountName: %1%n%nMinimumPasswordLength: %2%n%nMinimumPasswordLengthAudit: %3%n%nFor more information see https://go.microsoft.com/fwlink/?LinkId=2097191.%n\r\n
0x00004253 | The domain is incorrectly configured with a MinimumPasswordLength setting that is greater than 14 while RelaxMinimumPasswordLengthLimits is either undefined or disabled.%n%nNOTE: until this is corrected, the domain will enforce a smaller MinimumPasswordLength setting of 14.%n%nCurrently configured MinimumPasswordLength value: %1%n%nFor more information see https://go.microsoft.com/fwlink/?LinkId=2097191.%n\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n

### 10.0.22000.1

Message identifier | Message string
--- | ---
0x00002000 | Administrator\r\n
0x00002001 | Guest\r\n
0x00002002 | Domain Admins\r\n
0x00002003 | Domain Users\r\n
0x00002004 | None\r\n
0x00002005 | Administrators\r\n
0x00002006 | Server Operators\r\n
0x00002007 | Power Users\r\n
0x00002008 | Users\r\n
0x00002009 | Guests\r\n
0x0000200a | Account Operators\r\n
0x0000200b | Print Operators\r\n
0x0000200c | Backup Operators\r\n
0x0000200d | Replicator\r\n
0x0000200e | Domain Guests\r\n
0x0000200f | $AccountNameConflict%1\r\n
0x00002010 | krbtgt\r\n
0x00002011 | Domain Computers\r\n
0x00002012 | Domain Controllers\r\n
0x00002013 | Schema Admins\r\n
0x00002014 | Cert Publishers\r\n
0x00002015 | Enterprise Admins\r\n
0x00002016 | RAS and IAS Servers\r\n
0x00002017 | Group Policy Creator Owners\r\n
0x00002018 | Pre-Windows 2000 Compatible Access\r\n
0x00002019 | Everyone\r\n
0x0000201a | Remote Desktop Users\r\n
0x0000201b | Administrators\r\n
0x0000201c | Anonymous Logon\r\n
0x0000201d | Network Configuration Operators\r\n
0x0000201e | Incoming Forest Trust Builders\r\n
0x0000201f | Performance Monitor Users\r\n
0x00002020 | Performance Log Users\r\n
0x00002021 | Windows Authorization Access Group\r\n
0x00002022 | Network Service\r\n
0x00002023 | Enterprise Domain Controllers\r\n
0x00002024 | Terminal Server License Servers\r\n
0x00002025 | Trusted Installers\r\n
0x00002026 | Distributed COM Users\r\n
0x00002027 | IIS_IUSRS\r\n
0x0000202a | Cryptographic Operators\r\n
0x0000202b | INTERNET USER\r\n
0x0000202d | Allowed RODC Password Replication Group\r\n
0x0000202e | Denied RODC Password Replication Group\r\n
0x0000202f | Read-only Domain Controllers\r\n
0x00002030 | Enterprise Read-only Domain Controllers\r\n
0x00002031 | Event Log Readers\r\n
0x00002032 | Certificate Service DCOM Access\r\n
0x00002033 | RDS Remote Access Servers\r\n
0x00002034 | RDS Endpoint Servers\r\n
0x00002035 | RDS Management Servers\r\n
0x00002036 | Hyper-V Administrators\r\n
0x00002037 | Cloneable Domain Controllers\r\n
0x00002038 | Access Control Assistance Operators\r\n
0x00002039 | Remote Management Users\r\n
0x0000203a | DefaultAccount\r\n
0x0000203b | System Managed Accounts Group\r\n
0x0000203c | WDAGUtilityAccount\r\n
0x0000203d | Device Owners\r\n
0x00002100 | Built-in account for administering the computer/domain\r\n
0x00002101 | Built-in account for guest access to the computer/domain\r\n
0x00002102 | Designated administrators of the domain\r\n
0x00002103 | All domain users\r\n
0x00002104 | Ordinary users\r\n
0x00002105 | Administrators have complete and unrestricted access to the computer/domain\r\n
0x00002106 | Members can administer domain servers\r\n
0x00002107 | Power Users are included for backwards compatibility and possess limited administrative powers\r\n
0x00002108 | Users are prevented from making accidental or intentional system-wide changes and can run most applications\r\n
0x00002109 | Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted\r\n
0x0000210a | Members can administer domain user and group accounts\r\n
0x0000210b | Members can administer printers installed on domain controllers\r\n
0x0000210c | Backup Operators can override security restrictions for the sole purpose of backing up or restoring files\r\n
0x0000210d | Supports file replication in a domain\r\n
0x0000210e | All domain guests\r\n
0x0000210f | Key Distribution Center Service Account\r\n
0x00002110 | All workstations and servers joined to the domain\r\n
0x00002111 | All domain controllers in the domain\r\n
0x00002112 | Designated administrators of the schema\r\n
0x00002113 | Members of this group are permitted to publish certificates to the directory\r\n
0x00002114 | Designated administrators of the enterprise\r\n
0x00002115 | Servers in this group can access remote access properties of users\r\n
0x00002116 | Members in this group can modify group policy for the domain\r\n
0x00002117 | A backward compatibility group which allows read access on all users and groups in the domain\r\n
0x00002118 | Members in this group are granted the right to logon remotely\r\n
0x00002119 | Administrators have complete and unrestricted access to the computer\r\n
0x0000211a | Members in this group can have some administrative privileges to manage configuration of networking features\r\n
0x0000211b | Members of this group can create incoming, one-way trusts to this forest\r\n
0x0000211c | Members of this group can access performance counter data locally and remotely\r\n
0x0000211d | Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer\r\n
0x0000211e | Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects\r\n
0x0000211f | Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage\r\n
0x00002120 | Members in this group are granted the right to install software\r\n
0x00002121 | Members are allowed to launch, activate and use Distributed COM objects on this machine.\r\n
0x00002122 | Built-in group used by Internet Information Services.\r\n
0x00002125 | Members are authorized to perform cryptographic operations.\r\n
0x00002127 | Members in this group can have their passwords replicated to all read-only domain controllers in the domain\r\n
0x00002128 | Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain\r\n
0x00002129 | Members of this group are Read-Only Domain Controllers in the domain\r\n
0x0000212a | Members of this group can read event logs from local machine\r\n
0x0000212b | Members of this group are Read-Only Domain Controllers in the enterprise\r\n
0x0000212c | Members of this group are allowed to connect to Certification Authorities in the enterprise\r\n
0x0000212d | Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.\r\n
0x0000212f | Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.\r\n
0x00002130 | Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.\r\n
0x00002131 | Members of this group have complete and unrestricted access to all features of Hyper-V.\r\n
0x00002132 | Members of this group that are domain controllers may be cloned.\r\n
0x00002133 | Members of this group can remotely query authorization attributes and permissions for resources on this computer.\r\n
0x00002134 | Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.\r\n
0x00002135 | Protected Users\r\n
0x00002136 | Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.\r\n
0x00002137 | A user account managed by the system.\r\n
0x00002138 | Members of this group are managed by the system.\r\n
0x00002139 | Storage Replica Administrators\r\n
0x0000213a | Members of this group have complete and unrestricted access to all features of Storage Replica.\r\n
0x0000213b | Key Admins\r\n
0x0000213c | Members of this group can perform administrative actions on key objects within the domain.\r\n
0x0000213d | Enterprise Key Admins\r\n
0x0000213e | Members of this group can perform administrative actions on key objects within the forest.\r\n
0x0000213f | A user account managed and used by the system for Windows Defender Application Guard scenarios.\r\n
0x00002140 | Members of this group can change system-wide settings.\r\n
0x00003000 | SAM failed to write changes to the database. This is most likely due to a memory or disk-space shortage. The SAM database will be restored to an earlier state. Recent changes will be lost. Check the disk-space available and maximum pagefile size setting.\r\n
0x00003001 | SAM failed to restore the database to an earlier state. SAM has shutdown. You must reboot the machine to re-enable SAM.\r\n
0x00003003 | SAM failed to start the TCP/IP or SPX/IPX listening thread\r\n
0x00003005 | There are two or more objects that have the same SID attribute in the SAM database. The Distinguished Name of the account is %1. All duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003006 | The SAM database was unable to lockout the account of %1 due to a resource error, such as a hard disk write failure (the specific error code is in the error data) . Accounts are locked after a certain number of bad passwords are provided so please consider resetting the password of the account mentioned above.\r\n
0x00003007 | The SAM database attempted to delete the file %1 as it contains account information that is no longer used.  The error is in the record data. Please have an administrator delete this file.\r\n
0x00003008 | The SAM database attempted to clear the directory %1 in order to remove files that were once used by the Directory Service. The error is in record data. Please have an admin delete these files.\r\n
0x00003009 | %1 is now the primary domain controller for the domain.\r\n
0x0000300a | The account %1 cannot be converted to be a domain controller account as its object class attribute in the directory is not computer or is not derived from computer. If this is caused by an attempt to install a pre Windows 2000 domain controller in a Windows 2000 domain or later, then you should pre-create the account for the domain controller with the correct object class.\r\n
0x0000300b | The attempt to check whether group caching has been enabled in the Security Accounts Manager has failed, most likely due to lack of resources. This task has been rescheduled to run in one minute.\r\n
0x0000300c | The group caching option in the Security Accounts Manager has now been properly updated.  Group caching is enabled.\r\n
0x0000300d | The group caching option in the Security Accounts Manager has now been properly updated. Group caching is disabled.\r\n
0x0000300e | The %1 package failed to update additional credentials for user %2.  The error code is in the data of the event log message.\r\n
0x0000300f | There are two or more well known objects that have the same SID attribute in the SAM database. The Distinguished Name of the duplicate account is %1. The newest account will be kept, all older duplicate accounts have been deleted. Check the event log for additional duplicates.\r\n
0x00003010 | There are two or more objects that have the same account name attribute in the SAM database. The system has automatically renamed object %1 to a system assigned account name %2.\r\n
0x00003011 | An error occurred while creating new default accounts for this domain.  This maybe due to a transient error condition. The task will retry periodically until success and will log this message again in a week if the problem persists.\r\n
0x00004000 | The account %1 could not be upgraded since there is an account with an equivalent name.\r\n
0x00004001 | An error occurred upgrading user %1.  This account will have to be added manually upon reboot.\r\n
0x00004002 | An error occurred trying to read a user object from the old database.\r\n
0x00004003 | An error occurred upgrading alias %1. This account will have to be added manually upon reboot.\r\n
0x00004004 | An error occurred trying to read an alias object from the old database.\r\n
0x00004005 | An error occurred upgrading group %1. This account will have to be added manually upon reboot.\r\n
0x00004006 | An error occurred trying to read a group object from the old database.\r\n
0x00004007 | An error occurred trying to add account %1 to alias %2.  This account will have to be added manually upon reboot.\r\n
0x00004008 | The account with the sid %1 could not be added to group %2.\r\n
0x00004009 | An error occurred trying to add account %1 to group %2.  This account will have to be added manually upon reboot.\r\n
0x0000400a | The account with the rid %1 could not be added to group %2.\r\n
0x0000400b | A fatal error occurred trying to transfer the SAM account database into the directory service. A possible reason is the SAM account database is corrupt.\r\n
0x0000400c | The account krbtgt was renamed to %1 to allow the Kerberos security package to install.\r\n
0x0000400e | An error occurred trying to upgrade a SAM user's User_Parameters attribute. The following Notification Package DLL might be the possible offender: %1. Check the record data of this event for the NT error code.\r\n
0x0000400f | An error occured trying to set User Parameters attribute for this user This operation is failed. Check the record data of this event for the NT error code.\r\n
0x00004010 | An error occured trying to upgrade the following SAM User Object - %1. We will try to continue upgrading this user. But it might contain inconsistent data. Check the record data of this event for the NT error code.\r\n
0x00004011 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to open the group. Please add the account manually.\r\n
0x00004012 | An error occurred when trying to add the account %1 to the group %2. The problem, "%3", occurred when trying to add the account to the group.  Please add the account manually.\r\n
0x00004013 | The error "%2" occurred when trying to create the well known account %1. Please contact PSS to recover.\r\n
0x00004015 | During the installation of the Directory Service, this server's machine account was deleted hence preventing this Domain Controller from starting up.\r\n
0x00004016 | The Security Account Database detected that the well known account %1 does not exist. The account has been recreated.  Please reset the password for the account.\r\n
0x00004017 | The Security Account Database detected that the well known group or local group %1 does not exist. The group has been recreated.\r\n
0x00004018 | Domain operation mode has been changed to Native Mode. The change cannot be reversed.\r\n
0x00004019 | Active Directory Domain Services failed to add a security principal to well known security principals container. Please have an administrator add this security principal if needed. Security principal name: %1\r\n
0x0000401a | Active Directory Domain Services failed to add all of the new security principals to well known security principals container. Please have an administrator add these security principals if needed.\r\n
0x0000401b | Active Directory Domain Services failed to rename a security principal in well known security principals container. Please have an administrator rename this security principal if needed. Security principal name: %1\r\n
0x0000401c | Active Directory Domain Services failed to rename some of the security principals in well known security principals container. Please have an administrator rename these security principals if needed.\r\n
0x0000401d | An error occurred when trying to remove the account %1 from the group %2. The problem, "%3", occurred when trying to remove the account from the group.  Please remove the member manually.\r\n
0x00004102 | The account-identifier allocator was unable to assign a new identifier. The identifier pool for this domain controller may have been depleted. If this problem persists, restart the domain controller and view the initialization status of the allocator in the event log.\r\n
0x00004103 | An initial account-identifier pool has not yet been allocated to this domain controller. A possible reason for this is that the domain controller has been unable to contact the master domain controller, possibly due to connectivity or network problems. Account creation will fail on this domain controller until the pool is obtained.\r\n
0x00004104 | The maximum domain account identifier value has been reached. No further account-identifier pools can be allocated to domain controllers in this domain.\r\n
0x00004105 | The maximum account identifier allocated to this domain controller has been assigned. The domain controller has failed to obtain a new identifier pool. A possible reason for this is that the domain controller has been unable to contact the master domain controller. Account creation on this controller will fail until a new pool has been allocated. There may be network or connectivity problems in the domain, or the master domain controller may be offline or missing from the domain. Verify that the master domain controller is running and connected to the domain.\r\n
0x00004106 | The computed account identifier is invalid because it is out of the range of the current account-identifier pool belonging to this domain controller. The computed RID value is %1. Try invalidating the account identifier pool owned by this domain controller. This will make the domain controller acquire a fresh account identifier pool.\r\n
0x00004107 | The domain controller is starting a request for a new account-identifier pool.\r\n
0x00004108 | The request for a new account-identifier pool has completed successfully.\r\n
0x00004109 | The account-identifier-manager object creation completed. If the record data for this event has the value zero, the manager object was created. Otherwise, the record data will contain the NT error code indicating the failure. The failure to create the object may be due to low system resources, insufficient memory, or disk space.\r\n
0x0000410b | The request for a new account-identifier pool failed. The operation will be retried until the request succeeds. The error is %n " %1 "\r\n
0x0000410c | The domain controller is booting to directory services restore mode.\r\n
0x0000410d | A pool size for account-identifiers (RIDs) that was configured by an Administrator is greater than the supported maximum. The maximum value of %1 will be used when the domain controller is the RID master. %nSee http://go.microsoft.com/fwlink/?LinkId=225963 for more information.\r\n
0x0000410e | A pool of account-identifiers (RIDs) has been invalidated. This may occur in the following expected cases:%n1. A domain controller is restored from backup. %n2. A domain controller running on a virtual machine is restored from snapshot. %n3. An administrator has manually invalidated the pool. %nSee http://go.microsoft.com/fwlink/?LinkId=226247 for more information.\r\n
0x0000410f | The global maximum for account-identifiers (RIDs) has been increased to %1. %n See http://go.microsoft.com/fwlink/?LinkId=233329 for more information including important operating system interoperability requirements.\r\n
0x00004110 | Action required! An account-identifier (RID) pool was allocated to this domain controller. The pool value indicates this domain has consumed a considerable portion of the total available account-identifiers. %n%nA protection mechanism will be activated when the domain reaches the following threshold of total available account-identifiers remaining: %1.  The protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain. The mechanism will remain active until the Administrator manually re-enables account-identifier allocation on the RID master domain controller. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004111 | Action required! This domain has consumed a considerable portion of the total available account-identifiers (RIDs). A protection mechanism has been activated because the total available account-identifiers remaining is approximately: %1. %n%nThe protection mechanism prevents the allocation of account-identifier (RID) pools needed to allow existing DCs to create additional users, computers and groups, or promote new DCs into the domain.  The mechanism will remain active until the Administrator manually re-enables account-identifier (RID) allocation on the RID master domain controller. %n%nIt is extremely important that certain diagnostics be performed prior to re-enabling account creation to ensure this domain is not consuming account-identifiers at an abnormally high rate. Any issues identified should be resolved prior to re-enabling account creation. %n%nFailure to diagnose and fix any underlying issue causing an abnormally high rate of account-identifier consumption can lead to account-identifier (RID) pool exhaustion in the domain after which account creation will be permanently disabled in this domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228610 for more information.\r\n
0x00004112 | This event is a periodic update on the remaining total quantity of available account-identifiers (RIDs). The number of remaining account-identifiers is approximately: %1. %n%nAccount-identifiers are used as accounts are created, when they are exhausted no new accounts may be created in the domain. %n%nSee http://go.microsoft.com/fwlink/?LinkId=228745 for more information.\r\n
0x00004200 | Security Enabled Local Group Changed to Security Enabled Universal Group.\r\n
0x00004201 | Security Enabled Local Group Changed to Security Disabled Local Group.\r\n
0x00004202 | Security Enabled Local Group Changed to Security Disabled Universal Group.\r\n
0x00004203 | Security Enabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004204 | Security Enabled Global Group Changed to Security Disabled Global Group.\r\n
0x00004205 | Security Enabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004206 | Security Enabled Universal Group Changed to Security Enabled Local Group.\r\n
0x00004207 | Security Enabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004208 | Security Enabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004209 | Security Enabled Universal Group Changed to Security Disabled Global Group.\r\n
0x0000420a | Security Enabled Universal Group Changed to Security Disabled Universal Group.\r\n
0x0000420b | Security Disabled Local Group Changed to Security Enabled Local Group.\r\n
0x0000420c | Security Disabled Local Group Changed to Security Enabled Universal Group.\r\n
0x0000420d | Security Disabled Local Group Changed to Security Disabled Universal Group.\r\n
0x0000420e | Security Disabled Global Group Changed to Security Enabled Global Group.\r\n
0x0000420f | Security Disabled Global Group Changed to Security Enabled Universal Group.\r\n
0x00004210 | Security Disabled Global Group Changed to Security Disabled Universal Group.\r\n
0x00004211 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004212 | Security Disabled Universal Group Changed to Security Enabled Global Group.\r\n
0x00004213 | Security Disabled Universal Group Changed to Security Enabled Universal Group.\r\n
0x00004214 | Security Disabled Universal Group Changed to Security Disabled Local Group.\r\n
0x00004215 | Security Disabled Universal Group Changed to Security Disabled Global Group.\r\n
0x00004216 | Member Account Name Is Not Available.\r\n
0x00004217 | Account Enabled.\r\n
0x00004218 | Account Disabled.\r\n
0x00004219 | Certain Bit(s) in User Account Control Field Has Been Changed.\r\n
0x0000421b | Account Name Changed.\r\n
0x0000421c | Password Policy\r\n
0x0000421d | Logoff Policy\r\n
0x0000421e | Oem Information\r\n
0x0000421f | Replication Information\r\n
0x00004220 | Domain Server Role\r\n
0x00004221 | Domain Server State\r\n
0x00004222 | Lockout Policy\r\n
0x00004223 | Modified Count\r\n
0x00004224 | Domain Mode\r\n
0x00004225 | Basic Application Group Changed to Ldap Query Application Group.\r\n
0x00004226 | Ldap Query Application Group Changed to Basic Application Group.\r\n
0x00004227 | Failed to secure the machine account %1.  Have an administrator remove the builtin\account operators full control Access Control Entry from the security descriptor on this object.\r\n
0x00004228 | Failed to secure the machine account %1.  This operation will be retried. Have an administrator verify the builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004229 | Secured the machine account %1.  The builtin\account operators full control Access Control Entry was removed from the security descriptor on this object.\r\n
0x00004230 | The certificate that is used for authentication does not have an issuance policy descriptor corresponding to OID %1 in the Active Directory database. This certificate will not be associated with a corresponding security identifier (SID), and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy. The error is %2.\r\n
0x00004231 | The certificate issuance policy that is represented by OID %2 does not have a link to a security identifier (SID), or this link cannot be read. The link is represented by the attribute msDS-OIDToGroupLink on the msPKI-Enterprise-Oid object that represents the issuance policy. This certificate will not be associated with a corresponding SID, and the user may be denied access to some resources if you have resources whose access is restricted based on this issuance policy.\r\n
0x00004232 | Multiple certificate issuance policy descriptors were found in the Active Directory database. The attribute msPKI-Cert-Template-OID of these descriptors contains string %1.  This attribute should be able to uniquely identify an issuance policy descriptor; you should resolve this conflict. The issuance policies that are affected will not be associated with security identifiers (SIDs), and users who are authenticating using certificates that are issued by the corresponding policy may be denied access to some resources.\r\n
0x00004233 | The certificate issuance policy descriptor %2 is linked through its attribute msDS-OIDToGroupLink to a group that is not a security group, has members, or is not universal. The error is %6.%nAn issuance policy should be linked to a security identifier (SID) of a group that is security enabled, does not have members, and is universal. Users who are authenticating using certificates that are issued according to this policy may be denied access to some resources. The distinguished name (also known as DN) of the group that does not meet these requirements is %3.\r\n
0x00004234 | The requested modification for group %1 could not be performed. This is because this group is linked through msDS-OIDToGroupLinkBl to a certificate issuance policy descriptor. Such groups should be security enabled, they should not have any members, and they should be universal.%nThe requested operation was %4.%nThe error is %5.\r\n
0x00004235 | The certificate issuance policy descriptor %1 cannot be linked to group %2. Issuance policies can be linked through the attribute msDS-OIDToGroupLink only to universal, security-enabled groups that have an empty membership. You should ensure that this group meets these requirements.%nThe error is %5.\r\n
0x00004236 | The following invalid claims issued to user %1 have been dropped: %2.\r\n
0x00004237 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004238 | Claims issued to user %1 could not be validated and have been dropped. Error: %2.\r\n
0x00004239 | The password notification DLL %1 failed to load with error %4. Please verify that the notification DLL path defined in the registry, %2%3, refers to a correct and absolute path (<drive>:\<path>\<filename>.<ext>) and not a relative or invalid path. If the DLL path is correct, please validate that any supporting files are located in the same directory, and that the system account has read access to both the DLL path and any supporting files.  Contact the provider of the notification DLL for additional support. Further details can be found on the web at http://go.microsoft.com/fwlink/?LinkId=245898.\r\n
0x00004240 | SAM was configured to not listen on the TCP protocol.\r\n
0x00004241 | Legacy password validation mode has been enabled on this machine. If an Exchange ActiveSync policy is configured it will not be enforced for password validation requests.\r\n
0x00004242 | Remote calls to the SAM database are being restricted using the default security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004243 | Remote calls to the SAM database are being restricted using the configured registry security descriptor: %1.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004244 | The registry security descriptor is malformed: %1.%nRemote calls to the SAM database are being restricted using the default security descriptor: %2.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004245 | A remote call to the SAM database has been denied.%nClient SID: %1%nNetwork address: %2%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004246 | Audit only mode is now enabled for remote calls to the SAM database. SAM will log an event for clients who would have been denied access in normal mode. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004247 | Audit only mode is now disabled for remote calls to the SAM database.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004248 | Audit only mode is currently enabled for remote calls to the SAM database.%nThe following client would have been normally denied access:%nClient SID: %1 from network address: %2. %nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004249 | %2 remote calls to the SAM database have been denied in the past %1 seconds throttling window.%nFor more information please see http://go.microsoft.com/fwlink/?LinkId=787651.\r\n
0x00004250 | An error occurred while configuring one or more well-known accounts for this domain.  This may be due to a transient error condition. The task will retry periodically until successful. For more information please see https://go.microsoft.com/fwlink/?linkid=832473.%nStatus: %1\r\n
0x00004251 | The domain is configured with the following minimum password length-related settings.%n%nMinimumPasswordLength: %1%n%nRelaxMinimumPasswordLengthLimits: %2%n%nMinimumPasswordLengthAudit: %3%n%nFor more information see https://go.microsoft.com/fwlink/?LinkId=2097191.%n\r\n
0x00004252 | The following account has been configured with a password whose length is shorter than the current MinimumPasswordLengthAudit setting.%n%nAccountName: %1%n%nMinimumPasswordLength: %2%n%nMinimumPasswordLengthAudit: %3%n%nFor more information see https://go.microsoft.com/fwlink/?LinkId=2097191.%n\r\n
0x00004253 | The domain is incorrectly configured with a MinimumPasswordLength setting that is greater than 14 while RelaxMinimumPasswordLengthLimits is either undefined or disabled.%n%nNOTE: until this is corrected, the domain will enforce a smaller MinimumPasswordLength setting of 14.%n%nCurrently configured MinimumPasswordLength value: %1%n%nFor more information see https://go.microsoft.com/fwlink/?LinkId=2097191.%n\r\n
0x00004254 | The security account manager has detected the use of a ROCA-vulnerable Windows Hello for Business key during authentication by the following account. The policy is currently configured for audit so the authentication was allowed to proceed.%n%nAccount DN: %1%n%nAccount SID: %2%n%nKeyHash: %3%n%nFor more information see https://go.microsoft.com/fwlink/?linkid=2116430.%n\r\n
0x00004255 | The security account manager has detected and blocked the use of a ROCA-vulnerable Windows Hello for Business key during authentication by the following account.%n%nAccount DN: %1%n%nAccount SID: %2%n%nKeyHash: %3%n%nFor more information see https://go.microsoft.com/fwlink/?linkid=2116430.%n\r\n
0x00004256 | The security account manager is now logging verbose events for remote clients that call legacy password change or set RPC methods. This setting may cause large number of messages and should only be used for a short period time to diagnose problems.%n%nFor more information please see https://go.microsoft.com/fwlink/?linkid=2150956.%n\r\n
0x00004257 | The security account manager is now logging periodic summary events for remote clients that call legacy password change or set RPC methods.%n%nFor more information please see https://go.microsoft.com/fwlink/?linkid=2150956.%n\r\n
0x00004258 | The security account manager detected %1 legacy password change or set RPC method calls in the past %2 minutes.%n%nFor more information please see https://go.microsoft.com/fwlink/?linkid=2150956.%n\r\n
0x00004259 | The security account manager detected the use of a legacy password change or set RPC method from a network client.%nConsider upgrading the client operating system or application to use the latest and more secure version of this method.%n%nDetails:%n%nRPC Method: %1%nClient Network Address: %4%nClient SID: %3%nUsername: %2%n%nFor more information please see https://go.microsoft.com/fwlink/?linkid=2150956.%n\r\n
0x0000425a | The security account manager has detected one or more duplicated names for a local account. This inconsistency was remediated by keeping one account name and deleting the remaining names.%n%nRID=%1(%2)%n%nRetained account name: %3%n%nDeleted account name(s): %4%n%nFor more information see https://go.microsoft.com/fwlink/?linkid=2134956.%n\r\n
0x0000425b | The security account manager has detected one or more duplicated names for a local account. This inconsistency may cause application failures and\or system instability. No changes were made since the policy is in detect-only mode.%n%nDetails:%n%nRID=%1(%2)%n%nDuplicate account names: %3%n%nIf the policy had been set to repair mode, the following account name would have been retained and all others deleted:%n%nAccount name to retain: %4%n%nFor more information see https://go.microsoft.com/fwlink/?linkid=2134956.%n\r\n
0x0000425c | The security account manager encountered one or more fatal errors on startup which will not allow the machine to start.%n%nService startup error status:%1%n%nMore details may be found in the event data.%n%nFor more information see https://go.microsoft.com/fwlink/?linkid=2157228.%n\r\n
0x0000425d | The security account manager encountered one or more non-fatal errors on startup.%n%nMore details may be found in the event data.%n%nFor more information see https://go.microsoft.com/fwlink/?linkid=2157228.%n\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x90000001 | Microsoft-Windows-Directory-Services-SAM\r\n
0x90000002 | System\r\n
