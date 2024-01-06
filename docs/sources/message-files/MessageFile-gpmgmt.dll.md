## gpmgmt.dll

Path: %SystemRoot%\System32\gpmgmt.dll

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x400007d1 | Import from backup is successful. %r\r\nDetails - %r\r\n    Backup%r\r\n        Directory: %1%r\r\n        Instance : %2%r\r\n        Comment  : %3%r\r\n%r\r\n        Source GPO:%r\r\n            DisplayName: %4%r\r\n            ID: %5%r\r\n            Domain: %6%r\r\n%r\r\n%r\r\n    Destination GPO:%r\r\n            DisplayName: %7%r\r\n            ID: %8%r\r\n            Domain: %9%r        \r\n%r\r\n
0x400007d3 | Backup of GPO successful.%r\r\nDetails -%r\r\n    Source GPO:%r\r\n         DisplayName: %1%r\r\n         ID: %2%r\r\n         Domain: %3%r \r\n%r \r\n    Backup:%r\r\n        Directory: %4%r\r\n        Instance : %5%r\r\n        Comment  : %6%r\r\n%r   \r\n
0x400007d5 | Restore of GPO successful.%r\r\nDetails - %r\r\n    Backup%r\r\n        Directory: %1%r\r\n        Instance : %2%r\r\n        Comment  : %3%r\r\n%r\r\n    Destination GPO:%r\r\n        DisplayName: %4%r\r\n        ID: %5%r\r\n        Domain: %6%r\r\n%r    \r\n
0x400007d7 | Copy of GPO successful.%r\r\nDetails:%r\r\n    Source GPO:%r\r\n        DisplayName: %1%r\r\n        ID: %2%r\r\n        Domain: %3%r\r\n%r\r\n    Destination GPO:%r\r\n        DisplayName: %4%r\r\n        ID: %5%r\r\n        Domain: %6%r\r\n%r    \r\n
0x40230afc | The link to the WMI filter [%2] will not be preserved during the copy (or import) task. \r\n
0x40230b04 | Because the original and new GPOs are in different domains, the GPO will be copied (or imported) without the cross-GPO upgrade settings for any applications that have been deployed in this GPO. \r\n
0x40230b08 | Because the original and destination GPOs are in different domains, the categories for software installation will not be copied (or imported).\r\n
0x40230b09 | Because the original and new GPOs are in different domains, the GPO will be copied (or imported) without IP security policy [%2].\r\n
0x40230b23 | The source GPO contains settings from extension [%3] which are not valid in Windows 2000 domain. The task will continue but these settings will be dropped.\r\n
0x802309c5 | Link information for this site, domain, or organization unit is out of date. Refresh and try again.\r\n
0x802309c6 | Backups taken prior to a domain rename cannot be used after the rename. You must either restore by using a more recent backup, or you can import the settings.\r\n
0x802309c8 | The system administrator has disabled this feature unless you are running locally on the domain controller that the console is using for this domain. To restore (or import) this GPO, log on to a domain controller and make sure the console is using that domain controller, or contact an administrator with privileges to do this.\r\n
0x802309c9 | The restoration could not be completed because the domain controller you are using is running Windows 2000, and the GPO you selected contains application installation settings. Either restore this GPO using a domain controller running Windows Server 2003, or do not specify validation during the restore.\r\n
0x80230af5 | The security principal [%2] referenced in extension [%3] cannot be resolved, but the task will continue. In the future, you can use a migration table to map or remove this security principal.\r\nDetails: %1 %0\r\n
0x80230af7 | %5 %0\r\n
0x80230afd | The WMI filter [%2] cannot be found. The task will continue without linking GPO to the WMI filter.\r\nDetails: %1 %0\r\n
0x80230b0a | IP Security Policy [%2] specified in the source cannot be found. The Policy will be dropped but the operation will continue. \r\nDetails: %1 %0\r\n
0x80230b0b | At Line : %1, Description : %2\r\n
0x80230b0e | Based on the specified migration table, all security principals used in the security descriptor for one of the settings [%2] in the [%4] section in [%3] were mapped to nothing. To avoid specifying an empty security descriptor, this section will not be copied or imported.\r\n
0x80230b10 | An error occurred with the service configuration setting for [%2] in [%3]. The task will continue but this service configuration setting will not be copied (or imported).\r\n
0x80230b11 | A report for this GPO could not be created. The backup will not contain any report of the settings.\r\nDetails: %1 %0\r\n
0x80230b12 | The security principal [%2] cannot be resolved. The task will continue; however there may be unresolved security principals in the destination GPO.\r\n
0x80230b13 | The security principal [%2] is a local domain group. Domain local groups can only be used in the domain in which the group is defined. The task will continue and copy this setting, but you won't be able to use this group in a new domain. Consider using a migration table instead to map this group to a new group in the destination domain.\r\n
0x80230b1b | Destination [%2]: The path specified is not accessible. This path might need to be accessible during import/copy tasks. \r\nDetails: %1 %0\r\n
0x80230b1d | The security principal [%2] can not be resolved, but the task will continue. In the future, you can use a migration table to map or remove this security principal.\r\nDetails: %1 %0\r\n
0x80230b1e | Source [%1] and destination [%2] are of different group types. \r\nSource [%1] is of type [%3] and destination [%2] is of type [%4]. \r\nThe task will continue, but review Help documents to fully understand the effect of this mapping.\r\n
0x80230b1f | Source [%2] : The destination is a well known group which is not allowed. Correct the migration table and try again.\r\n
0x80230b21 | The software distribution path [%2] is not accessible but the task will continue. Make sure that the path is accessible at the time when GPO is applied to clients. \r\nDetails: %1 %0\r\n
0x80230b22 | The type of the security principal [%2] could not be determined, but the task will continue. In the future, you can use a migration table to map or remove this security principal.\r\n
0x80230b24 | The domain of the security principal [%2] can not be contacted to determine the type of this security principal which is referenced in extension [%3], but the task will continue. In the future, you can use a migration table to map or remove this security principal.\r\nDetails: %1\r\n
0x80230b25 | The deployment object in Active Directory for the software application [%2] in the backup could not be undeleted, but the task will continue. This software deployment will be created with a new deployment object in Active Directory. Any cross GPO upgrade relationships with this application will not be preserved. The undelete of the deployment object may have failed because you do not have sufficient privileges to perform the undelete operation, or the time elapsed between the deletion and restoration of the GPO has exceeded the tombstone lifetime.\r\n
0x80230b26 | Source [%2]: This entry could not be validated because SameAsSource option for the destination was set and the source security principal cannot be resolved. \r\nDetails: %1 %0\r\n
0x80230b27 | Source [%2]: This entry could not be validated because SameAsSource option for the destination was set and the source path is not accessible. \r\nDetails: %1 %0\r\n
0x80230b28 | Source [%2]: The security principal in the destination cannot be resolved. The domain of the security principal may not be accessible or it might be an externally trusted domain. This entry needs to be resolvable during import/copy tasks.\r\nDetails: %1 %0\r\n
0x80230b29 | The application deployment script (.aas file) for [%2] cannot be regenerated but the task will continue.\r\nDetails: %1 %0\r\n
0xc00007d0 | %1\r\n
0xc00007d2 | Import of backup failed. Error [%1]. %r\r\nDetails - %r\r\n    Backup%r\r\n        Directory: %1%r\r\n        Instance : %2%r\r\n        Comment  : %3%r\r\n%r\r\n        Source GPO:%r\r\n            DisplayName: %4%r\r\n            ID: %5%r\r\n            Domain: %6%r\r\n%r\r\n%r\r\n    Destination GPO:%r\r\n            DisplayName: %7%r\r\n            ID: %8%r\r\n            Domain: %9%r        \r\n%r \r\n
0xc00007d4 | Backup of GPO failed. Error [%1].%r\r\nDetails -%r\r\n    Source GPO:%r\r\n         DisplayName: %2%r\r\n         ID: %3%r\r\n         Domain: %4%r \r\n%r \r\n    Backup:%r\r\n        Directory: %5%r\r\n        Instance : %6%r\r\n        Comment  : %7%r\r\n%r \r\n
0xc00007d6 | Restore of GPO failed. Error [%1]%r\r\nDetails - %r\r\n    Backup%r\r\n        Directory: %2%r\r\n        Instance : %3%r\r\n        Comment  : %4%r\r\n%r\r\n    Destination GPO:%r\r\n        DisplayName: %5%r\r\n        ID: %6%r\r\n        Domain: %7%r\r\n%r\r\n
0xc00007d8 | Copy of GPO failed. Error [%1]%r\r\nDetails:%r\r\n    Source GPO:%r\r\n        DisplayName: %2%r\r\n        ID: %3%r\r\n        Domain: %4%r\r\n%r\r\n    Destination GPO:%r\r\n        DisplayName: %5%r\r\n        ID: %6%r\r\n        Domain: %7%r\r\n%r \r\n
0xc0230af1 | The file [%2] cannot be opened. The task will not continue.\r\nThe following error occurred:\r\n%5 %0 \r\n
0xc0230af2 | The backup configuration file [%2] cannot be saved. \r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230af8 | The task cannot continue because the migration table contains duplicate entries for security principal [%2]. Correct the migration table, and then try again.\r\n
0xc0230afa | The task cannot be completed. There was an error with extension [%3]. The attributes of Directory Services object [%2] cannot be accessed. \r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230afb | The task cannot be completed. There was an error with extension [%3]. The attributes on the Directory Services object [%2] cannot be set. \r\nThe following error occurred: \r\n%1 %0\r\n
0xc0230afe | The task cannot be completed. There was an error with extension [%3]. The security permissions on the folder [%2] cannot be set.\r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230aff | The task cannot be completed. There was an error with extension [%3]. The security permissions on the Directory Services object [%2] cannot be set. \r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230b00 | The task cannot be completed. There was an error with extension [%3]. The security permissions on the folder [%2] cannot be accessed. \r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230b01 | The task cannot be completed. There was an error with extension [%3]. The security permissions on the Directory Services object [%2] cannot be accessed. \r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230b02 | The task cannot be completed. There was an error with extension [%3]. The file [%2] cannot be accessed. \r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230b03 | An error occurred during the restore task, and the GPO [%2] could not be rolled back to its original state. You should reattempt the restore.\r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230b05 | The task cannot be completed. There was an error with extension [%3]. The setting [%4] from file [%2] cannot be accessed. \r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230b06 | The task cannot be completed. There was an error with extension [%3]. The setting [%4] cannot be transferred to the new GPO. \r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230b07 | The task cannot be completed. The application deployment script (.aas file) for [%2] cannot be regenerated.\r\nThe following error occurred:\r\n%1 %0\r\n
0xc0230b0d | The task could not be completed. The XML file is not valid according to the schema. Invalid namespace: [%1].\r\n
0xc0230b0f | The task could not be completed. The backed up GPO is incompatible with the schema. Use a newer back up and try again.\r\n
0xc0230b14 | Source [%2]: The entry type in the migration table differs from the type in the original GPO. Correct the migration table and try again.\r\n
0xc0230b15 | The file path entry [%2] does not have a destination. Correct the migration table and try again. \r\n
0xc0230b17 | Source [%2]: The security principal in the destination cannot be resolved. Correct the migration table and try again.\r\nThe following error occurred: \r\n%1 %0\r\n
0xc0230b18 | Source [%2]: The destination is invalid. Correct the migration table and try again. \r\n
0xc0230b19 | Source [%2]: DestinationByRelativeName is not a valid option for this source type. Correct the migration table and try again. \r\n
0xc0230b1a | Source [%2]: Source is not a valid path. Correct the migration table and try again.\r\n
0xc0230b1c | Source [%2]: No migration table entry was found for this source.\r\n
0xc0230b1d | The task will not continue because the migration table caused all security principals in the security descriptor for either the GPO or one or more of the application deployment objects in the GPO to be mapped to nothing. \r\n
0xc0230b20 | Source [%2]: The destination is not valid path. Correct the migration table and try again.\r\n
0xc0230bb8 | Group Policy Management could not contact any domain controllers in the domain that contains your user account. This may be either because of a network problem, or because your user account is not in Active Directory and trust detection is enabled. If your user account is not in Active Directory, you should turn off trust detection using the Options dialog from the View menu.\r\n
0xc0230bb9 | The backup template file could not be loaded. The task will not continue.\r\nThe following error occurred:\r\n%5 %0 \r\n
