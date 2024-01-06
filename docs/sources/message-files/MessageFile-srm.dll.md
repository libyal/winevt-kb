## srm.dll

Path: %SystemRoot%\System32\srm.dll

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x00045304 | At least one failure occurred in a batch operation.\r\n
0x00045305 | The file may only have partial classification because a failure occurred while loading or classifying the file properties.\r\n
0x00045306 | Classification failed on one or more volumes. Check the application event log for more information.\r\n
0x0004531b | Auto apply quota configuration for one or more folders failed.  Check the application event log for more information.\r\n
0x80040002 | File Server Resource Manager Service information: Volume '%1' appears as disconnected and it is\r\nignored by the service.  You may want to rescan disks.   Error: %2.\r\n%3\r\n
0x80040003 | File Server Resource Manager Service information: The COM Server with CLSID %1 and name '%2' cannot be started on machine '%3'.\r\nMost likely the CPU is under heavy load.  Error: %4.\r\n%5\r\n
0x80040004 | File Server Resource Manager Service information: The COM Server with CLSID %1 and name '%2' cannot be started on machine '%3'.  Error: %4.\r\n%5\r\n
0x80040005 | File Server Resource Manager Service error: The COM Server with CLSID %1 and name '%2' cannot be started on machine '%3' during Safe Mode.\r\nThe File Server Resource Manager service cannot start while in safe mode.  Error: %4.\r\n%5\r\n
0x80040006 | File Server Resource Manager Service error: A critical component required by the File Server Resource Manager Service is not registered.\r\nThis might happen if an error occurred during Windows setup, or if the computer does not have the Windows Server 2008 or later version of FSRM installed.\r\nThe error returned from CoCreateInstance on class with CLSID %1 and Name '%2' on machine '%3' is %4.\r\n%5\r\n
0x80040007 | File Server Resource Manager Service error: The FSRM event log source EventMessageFile '%1' found in registry key '%2' is not correct. \r\nThis might happen if an error occurred during Windows setup.\r\n%3\r\n
0x80042001 | File Server Resource Manager Service error: Unexpected error calling routine %1.  hr = %2.\r\n%3\r\n
0x80042002 | File Server Resource Manager failed to initialize its WMI event provider component. Therefore, WMI events will not be sent during quota and screening notification processing.\r\nIn order to receive WMI events, check the status of the WMI service and WMI event logs, correct the WMI errors, and restart the File Server Resource Manager service.\r\n%1\r\n
0x80042003 | File Server Resource Manager failed to initialize its shadow copy writer component. Therefore, backup and restore of the File Server Resource Manager stores may not be done correctly.\r\nIn order to properly perform backup and restore of File Server Resource Manager, check the status of the COM+ Event System service and VSS and COM+ event logs, correct the errors, and restart the File Server Resource Manager service.\r\n%1\r\n
0x80042004 | The storage reports repository will not be included in the File Server Resource Manager backup because the service failed to retrieve the repository locations.\r\n%1\r\n
0x80042005 | File Server Resource Manager Service error: Unexpected error.\r\n%1\r\n
0x80042006 | File Server Resource Manager Service warning: %1.  Error: %2.\r\n%3\r\n
0x80042007 | Error occurred during file screen configuration.  File screening will not be enforced for directory '%1' on volume '%2' until the error is corrected and the volume is remounted.\r\n%3\r\n
0x80042008 | FSRM Assert Failure: %1\r\n
0x80042009 | File Server Resource Manager Service error: Unexpected COM error %1: %2.  Error code: %3.\r\n%4\r\n
0x8004200a | Communication port '%1' to the '%2' filter driver was established.\r\n
0x8004200b | Communication port '%1' to the '%2' filter driver was disconnected.\r\nThe '%2' filter driver may need to be started.  Retrying...\r\n
0x8004200c | The File Server Resource Manager detected %1 unprocessed quota or screening notifications when the service or system was stopping.  Administrators or end-users may not have received notification of quota or screening violations.  Running a quota report can help identify quotas that are in a critical state.\r\n
0x8004200d | The required '%1' property of the action '%2' is missing.\r\n%3\r\n
0x8004200e | The required '%1' property of the action '%2' at threshold %3%% is missing.\r\n
0x8004200f | The required '%1' property of the action '%2' at the limit is missing.\r\n
0x80042010 | The '%1' property of the action '%2' is not within the legal range.\r\n%3\r\n
0x80042011 | The '%1' property of the action '%2' at threshold %3%% is not within the legal range.\r\n
0x80042012 | The '%1' property of the action '%2' at the limit is not within the legal range.\r\n
0x80042013 | The properties of the action '%2' specify an illegal combination.\r\n%3\r\n
0x80042014 | The properties of the action '%2' at threshold %3%% specify an illegal combination.\r\n
0x80042015 | The properties of the action '%2' at the limit specify an illegal combination.\r\n
0x80042016 | Multiple actions were found sharing the same action name: '%1'.\r\n
0x80042017 | %1\r\n
0x80042018 | This command was initiated by the File Server Resource Manager service.  It belongs to the action '%1' of the file screen on path '%2'.\r\n
0x8004201a | This command was initiated by the File Server Resource Manager service.  It belongs to the action '%1' on the %2%% threshold on the quota on path '%3'.\r\n
0x8004201b | This command was initiated by the File Server Resource Manager service.  It belongs to the action '%1' on the %2%% threshold on the quota on path '%3' for user '%4'.\r\n
0x8004201c | This command was initiated by the File Server Resource Manager service.  It belongs to the action '%1' on the limit on the quota on path '%3'.\r\n
0x8004201d | This command was initiated by the File Server Resource Manager service.  It belongs to the action '%1' on the limit on the quota on '%3' for user '%4'.\r\n
0x8004201f | File Server Resource Manager will no longer monitor the following FSRM-initiated command-line programs because the service is shutting down: '%1'\r\n
0x80042020 | File Server Resource Manager killed the following FSRM-initiated command-line program because it exceeded its %1-minute run time limit setting: '%2'\r\n
0x80042021 | File Server Resource Manager was unable to terminate the following FSRM-initiated command-line program: '%1'\r\n
0x80042022 | The following FSRM-initiated command-line program exited with return code %1\r\n
0x80042023 | File Server Resource Manager was unable to access the following directory: '%1'.  You must give Local System access to this directory to do further operations on it.\r\n
0x80042024 | File Server Resource Manager was unable to access the following file or volume: '%1'.  This file or volume might be locked by another application right now, or you might need to give Local System access to it.\r\n
0x80042025 | The path '%1' does not exist. This path will be ignored for now. The directory was probably deleted and will not be included in reporting or classification. Please reconfigure reporting or classification settings appropriately.\r\n
0x80042026 | Invalid namespace root specified for reporting or classification: the path '%1' is not a valid directory (for example - it might be a file). Please reconfigure reporting or classification settings appropriately.\r\n
0x80042027 | The volume mounted at '%1' ('%2') for namespace root '%3' is not a valid volume for reporting or classification. Make sure that you include only paths on fixed NTFS volumes in the report. This path will be ignored for now. Please reconfigure reporting or classification settings appropriately.\r\n
0x80042028 | File Server Resource Manager failed to retrieve the mount points under the volume mounted at '%1'. Make sure the volume mounted at this location is not offline or unavailable. This path will be ignored for now.\r\n
0x80042029 | File Server Resource Manager failed to register all reporting and classification consumers.\r\n
0x8004202a | File Server Resource Manager failed to register all classification rules.\r\n
0x8004202b | File Server Resource Manager failed to initialize the volume scanner.\r\n
0x8004202c | File Server Resource Manager encountered an unexpected error while initializing modules in the classification pipeline.\r\n
0x8004202d | File Server Resource Manager failed to initialize all consumers in the classification pipeline.\r\n
0x8004202e | File Server Resource Manager encountered an unexpected error during volume scan of volumes mounted at '%1' ('%2'). To find out more information about the root cause for this error please consult the Application/System event log for other FSRM, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:\r\n
0x8004202f | File Server Resource Manager was unable to create or access the shadow copy for volumes mounted at '%1' ('%2'). Possible causes include an improper Shadow Copy configuration, insufficient disk space, or extreme memory, I/O or CPU load of the system. To find out more information about the root cause for this error please consult the Application/System event log for other FSRM, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:\r\n
0x80042030 | File Server Resource Manager was unable to access volumes mounted at '%1' ('%2'). Make sure that dismount or format operations do not happen while running classification or generating reports.\r\n
0x80042031 | Classification module '%1' has failed.\r\n
0x80042032 | Reporting or classification consumer '%1' has failed.\r\n
0x80042033 | Scanning statistics on volume mounted at '%1' ('%2'):%n\r\n- File count: %3%n\r\n- Milliseconds elapsed: %4%n\r\n- Files per second: %5%n\r\n- Resident stream count: %6%n\r\n
0x80042034 | %1\r\n
0x80042035 | %1\r\n
0x80042036 | Scanning statistics on pipeline running on '%1':%n\r\n%2%n\r\n
0x80042037 | A fatal error has occurred in the classification pipeline. All currently running reporting, classification, and file management jobs will be aborted.\r\n
0x80042038 | Performance statistics for module '%1':%n\r\n- Total file count: %2%n\r\n- Total time spent (s): %3%n\r\n- Average time spent per file (ms): %4%n\r\n- Maximum time spent on a file (ms): %5%n\r\n- File that caused maximum time: %6%n\r\n- Files processing for longer than 10 seconds: %7%n\r\n- Files processing for longer than 1 minute: %8%n\r\n- Files processing for longer than 10 minutes: %9%n\r\n- Files processing for longer than 1 hour: %10%n\r\n
0x80042039 | File Server Resource Manager was unable to access a file or volume. Details:%n\r\n%1%n\r\nThe volume may be inaccessible for I/O operations or marked read-only. In case of a cluster volume, this may be a transient failure during failover.\r\n
0x8004203a | The File Server Resource Manager configuration file '%1' is not found. It is required that the system or volume be restored from backup.\r\n%2\r\n
0x8004203b | A File Server Resource Manager module encountered an invalid parameter or a valid parameter with an invalid value or an expected module parameter is not found. Parameter: '%1'\r\n
0x8004203c | File Server Resource Manager was unable to scan volume  '%1' ('%2'). \r\n
0x8004203d | File Server Resource Manager failed to schedule auto apply quota rebuilding on volume '%1'.\r\n
0x8004203e | File Server Resource Manager encountered an error during a classification operation.%n\r\nHRESULT = %1%n%n\r\nDetails:%n\r\n%2\r\n
0x8004203f | File Server Resource Manager set a property on a file outside of automatic classification.\r\n%1\r\n
0x80042040 | File Server Resource Manager cleared a property on a file outside of automatic classification.\r\n%1\r\n
0x80042041 | File Server Resource Manager set properties on a file outside of automatic classification. This can occur if a file is manually classified. No user action is required.\r\n%1\r\n
0x80043001 | File Server Resource Manager detected an invalid SID, %1, for the quota on directory, '%2'.\r\n
0x80043002 | File Server Resource Manager failed to automatically upgrade its configuration on volume %1. The volume cannot be added to the upgrade queue.\r\n
0x80043003 | The File Server Resource Manager Reports service is shutting down due to idle timeout.\r\n%1\r\n
0x80043004 | The File Server Resource Manager Reports service is shutting down due to shutdown event from the Service Control Manager.\r\n%1\r\n
0x80043005 | The File Server Resource Manager configuration file or import-export file '%1' is corrupted.  If the corrupt file is a configuration file, it is required that the system or volume be restored from backup.  If the file is an import-export file, export the items again and retry the operation without editing the file contents.\r\n%2\r\n
0x80043006 | File Server Resource Manager has received a configuration request from the file screen filter driver for volume '%1'.\r\n
0x80043007 | File Server Resource Manager has completed a configuration request from the file screen filter driver for volume '%1'.\r\n
0x80043008 | File Server Resource Manager failed to configure auto apply quota settings on path '%1'.\r\n%2\r\n
0x80043009 | File Server Resource Manager regenerated one or more records for configuration database '%1'.  The new records contain no quota or screening notification configuration, so it is recommended that the system or volume be restored from backup.\r\n%2\r\n
0x8004300a | A File Server Resource Manager Service command line action was not run because command line actions are disabled on this machine.  Use the FSRM management console to enable command line notifications on this system.\r\n%1\r\n
0x8004300b | A File Server Resource Manager Service command line action was not run because the last person who saved it is no longer an administrator on this machine.  Use the FSRM management console to save again the quota, screening or file management configuration.\r\n%1\r\n
0x8004300c | A File Server Resource Manager Service command line action specifies an insecure path because it gives write access to '%1' on path '%2'.  Move the program to a directory that permits write access only to privileged users.\r\n%3\r\n
0x8004300d | A File Server Resource Manager Service command line action could not be run.\r\n%1\r\n
0x8004300e | A File Server Resource Manager Service event log action could not be run.\r\n%1\r\n
0x8004300f | A File Server Resource Manager Service email action could not be run because there is no SMTP server set.  Use the FSRM management console to specify the SMTP server to use.\r\n%1\r\n
0x80043011 | A File Server Resource Manager Service email action could not be run because the specified TO or FROM address is invalid.  Use the FSRM management console to add valid TO and FROM e-mail addresses to the quota, screening or file management configuration.\r\n%1\r\n
0x80043012 | A File Server Resource Manager Service email action could not be run.\r\n%1\r\n
0x80043013 | The File Server Resource Manager configuration file '%1' is out of sync or missing records.  This could have been caused by inadvertent administrator action, or by incomplete backup/restore.  FSRM will attempt to regenerate default records for interim use, but there may be some missing functionality.  For example, quota or screening configurations may be missing notifications.  It is recommended that the system or volume be restored from backup.  \r\n%2\r\n
0x80043014 | The File Server Resource Manager configuration file '%1' is missing.  This could have been caused by inadvertent administrator action, or by incomplete backup/restore.  An empty configuration file has been created for interim use.  It is recommended that the system or volume be restored from backup.  \r\n%2\r\n
0x80043015 | A File Server Resource Manager configuration file or import-export file is corrupted.  If the corrupt file is a configuration file, it is required that the system or volume be restored from backup.  If the file is an import-export file, export the items again and retry the operation without editing the file contents.\r\n%1\r\n
0x80043016 | Shadow copy '%1' was deleted during storage report generation.  Volume '%2' might be configured with inadequate shadow copy storage area.  Storage reports may be temporarily unavailable for this volume.\r\n%3\r\n
0x80043017 | Shadow copy creation failed for volume '%1' with error %2.  The volume might be configured with inadequate shadow copy storage area.  Storage reports may be temporarily unavailable for this volume.\r\n%3\r\n
0x80043018 | File Server Resource Manager encountered an error while attempting to find the network share and DFS paths that expose the local path '%1'.  The remote paths may be temporarily unavailable to FSRM quota and screening notifications.\r\n%2\r\n
0x80043019 | The File Server Resource Manager global configuration data store has been created.\r\n
0x8004301a | File Server Resource Manager encountered an error while initializing local-to-remote path mapping.  Mappings from local file paths to share and DFS paths will not be available until the FSRM service is restarted or the system reboots.\r\n%1\r\n
0x8004301b | File Server Resource Manager encountered an error when uninitializing local-to-remote path mapping.\r\n%1\r\n
0x8004301c | Volume '%1' is not supported for shadow copy.  It is possible that the volume was removed from the system.  Storage reports will not be available for this volume.\r\n%2\r\n
0x8004301d | File Server Resource Manager failed to enumerate share paths or DFS paths.  Mappings from local file paths to share and DFS paths may be incomplete or temporarily unavailable.  FSRM will retry the operation at a later time.\r\n%1\r\n
0x8004301e | Failed saving one of the configuration stores on volume '%1' due to a disk-full error:\r\nIf the disk is full, please clean it up (extend the volume or delete some files).\r\nIf the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.\r\n%2\r\n
0x8004301f | Shadow copy creation failed for volume '%1' because other shadow copies were being created.\r\n%3\r\n
0x80043020 | The volume '%1' has been deleted or removed from the system.\r\n%2\r\n
0x80043021 | The file system on volume '%1' is potentially corrupted.  Please run the CHKDSK utility to verify and fix the file system.\r\n%2\r\n
0x80043022 | Error occurred during default template setup.  Template '%1', could not be installed and will not be available on the system until the system is reinstalled.\r\n%2\r\n
0x80043023 | Error occurred during file screen configuration.  File screening will not be enforced on volume '%1' until the error is corrected and the volume is remounted.\r\n%2\r\n
0x80043024 | %1\r\n
0x80043025 | %1\r\n
0x80043026 | File Server Resource Manager global configuration cannot be accessed since the cluster service is not running. Please start the cluster service and retry the operation.\r\n%1\r\n
0x80043027 | The File Server Resource Manager global configuration cannot be accessed since the cluster service is not running. Please start the cluster service.\r\n%1\r\n
0x80043028 | File Server Resource Manager cannot start file screening on this system since the cluster service is not running. Screening will start once the cluster service is running.\r\n%1\r\n
0x80043029 | Failed writing the file screen audit log on volume '%1' due to a disk-full error:\r\nIf the disk is full, please clean it up (extend the volume or delete some files).\r\nIf the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.\r\n%2\r\n
0x8004302a | File Server Resource Manager successfully created a cluster resource for the reports scheduled task '%1', but failed to bring the resource online. Please check the resource status in the cluster administration console.\r\n%2\r\n
0x8004302b | File Server Resource Manager failed to take a cluster resource offline for the reports scheduled task '%1'. The report task cannot be deleted if the resource remains online. Please check the resource status in the cluster administration console.\r\n%2\r\n
0x8004302c | File Server Resource Manager had a failure when invoking an COM call on an external component:%n\r\nThis might be a problem with this specific COM component that supplies this functionality.%n\r\nYou might want to follow up the error with the vendor implementing this module.%n\r\n
0x8004302d | File Server Resource Manager attempted to load a disabled module.%n\r\nPlease ensure that all enabled modules in use (by FSRM classification rules and policies) are enabled.%n\r\n
0x8004302e | An error occurred while File Server Resource Manager attempted to impersonate user %1 to load module %2.%n\r\nPlease check the security policies on this machine. (GetLastError = %3)%n\r\n
0x8004302f | An error occurred while File Server Resource Manager attempted to install a default module.%n\r\n%1\r\n
0x80043030 | Rule '%1' refers to module definition '%2', which could not be found; rule will not be used for classification.\r\n
0x80043031 | Rule '%1' refers to a property '%2' that has no property definition; rule will not be used for classification.\r\n
0x80043032 | The Continuous scanner encountered an unexpected error.\r\n%1\r\n
0x80043033 | File Server Resource Manager failed to find the claim list '%1' in Active Directory (ADsPath: %2). Please check that the claims list configured for this machine in Group Policy exists in Active Directory.\r\n
0x80043034 | File Server Resource Manager encountered a malformed claim in Active Directory Domain Services (AD DS). Please reconfigure the claim in AD DS.%n\r\n%n\r\nDetails:%n\r\nDomain controller: %1%n\r\nResource property list: %2%n\r\nResource property name: %3%n\r\n
0x80043035 | File Server Resource Manager encountered the claim %1 in Active Directory with the same name as a local property definition.  The local property definition is being marked as deprecated.\r\n
0x80043037 | File Server Resource Manager finished syncing claims from Active Directory Domain Services with no errors.%n\r\n%n\r\nDetails:%n\r\nDomain controller: %1%n\r\nResource property list: %2%n\r\nProperties created: %3%n\r\nProperties modified: %4%n\r\nProperties deleted: %5%n\r\n
0x80043038 | File Server Resource Manager finished syncing claims from Active Directory and encountered errors during the sync (%1).  Please check previous event logs for details.\r\n
0x80043039 | File Server Resource Manager failed to update property definition '%1' with data from Active Directory.  The error is: %2.\r\n
0x8004303a | File Server Resource Manager failed to change or delete property definition '%1'.  Please check previous event logs for details.\r\n
0x8004303b | File Server Resource Manager failed to create the predefined property definition '%1' with the error %2.\r\n
0x8004303c | File Server Resource Manager could not add the Access-Denied Assistance Users group to the Remote Management Users group. Try manually adding the Access-Denied Assistance Users group to the Remote Management Users group.\r\n
0x8004303d | File Server Resource Manager could not remove the Access-Denied Assistance Users group from the Remote Management Users group. Try manually removing the Access-Denied Assistance Users group from the Remote Management Users group.\r\n
0x8004303e | File Server Resource Manager could not add '%1' group to '%2' group. Try adding this group manually to enable Access-Denied Assistance for users.\r\n
0x80044001 | File Server Resource Manager Service added a quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044002 | File Server Resource Manager Service modified a quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044003 | File Server Resource Manager Service deleted a quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044004 | File Server Resource Manager Service added an auto apply quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044005 | File Server Resource Manager Service modified an auto apply quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044006 | File Server Resource Manager Service deleted an auto apply quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044007 | File Server Resource Manager Service derived a quota from an auto apply quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044008 | File Server Resource Manager set a property on a file during automatic classification.%n\r\n%n\r\nFile: %1%n\r\nProperty Changed: %2%n\r\nProperty Value: %3%n\r\nRetrieved From Storage: %4%n\r\nRule Applied: %5%n\r\n
0x80044009 | File Server Resource Manager applied a file management job expiration action to a file.%n\r\n%n\r\nFile Management Job Name: %1%n\r\nExpiration Action: %2%n\r\n
0x8004400a | File Server Resource Manager applied a file management job custom action to a file.%n\r\n%n\r\nFile Management Job Name: %1%n\r\nCustom Action: %2%n\r\n
0x8004400b | File Server Resource Manager performed the following file management job notification:%n\r\n%n\r\nFile Management Job Name: %1%n\r\nNotification Days: %2%n\r\nActions Taken: %3%n\r\n
0x8004400c | File Server Resource Manager encountered an error while classifying a file during automatic classification.%n\r\n%n\r\nFile: %1%n\r\nModule: %2%n\r\nMessage: %3%n\r\n
0x8004400d | The following property definition was %1:%n\r\n%n\r\nName: %2%n\r\nType: %3%n\r\nGlobal: %4%n\r\nSecure: %5%n\r\nDeprecated: %6%n\r\nApplies To: %7%n\r\nPossible Values: %8%n\r\n
0x8004400e | The following classification rule was %1:%n\r\n%n\r\nName: %2%n\r\nEnabled: %3%n\r\nValid: %4%n\r\nScope: %5%n\r\nProperty Assignment Method: %6%n\r\nProperty Assigned: %7%n\r\nValue: %8%n\r\nRe-evaluation Option: %9%n\r\nParameters: %10%n\r\n
0x8004400f | The following classifier module definition was %1:%n\r\n%n\r\nName: %2%n\r\nCOM CLSID: %3%n\r\nProperties Set: %4%n\r\nNeeds Explicit Value: %5%n\r\nParameters: %6%n\r\n
0x80044010 | The following storage module definition was %1:%n\r\n%n\r\nName: %2%n\r\nCOM CLSID: %3%n\r\nSupported Extensions: %4%n\r\nParameters: %5%n\r\n
0x80044011 | The following access-denied assistance error configuration was %1:%n\r\n%n\r\nError: %2%n\r\nEnabled: %3%n\r\nClient Display Flags: %4%n\r\nError Message: %5%n\r\nEmail Flags: %6%n\r\nAdditional To Emails: %7%n\r\nEmail Message: %8%n\r\n
0x80044012 | A request for assistance with an error was sent.%n\r\n%n\r\nDetails:%n\r\nError: %1%n\r\nEmail sent to: %2%n\r\nEmail subject: %3%n\r\nUser: %4\%5%n\r\nFile path: %6%n\r\nParent folder: %7%n\r\nMessage from administrator: %8%n\r\nMessage from %4\%5: %9%n\r\n
0x80044013 | A request for assistance with an error could not be sent because the email address of the recipient is blank.%n\r\n%n\r\nDetails:%n\r\nError: %1%n\r\nEmail subject: %2%n\r\nUser: %3\%4%n\r\nFile path: %5%n\r\nParent folder: %6%n\r\nMessage from administrator: %7%n\r\nMessage from %3\%4: %8%n\r\n
0x80044014 | An access-denied assistance error is configured to send email to the file server administrator, but no email address is specified in the Default Administrator Recipients box in the Options dialog box of File Server Resource Manager.%n\r\n
0x80044015 | File Server Resource Manager applied a file management task RMS Encryption action to a file.%n\r\n%n\r\nFile management task name: %1%n\r\nCustom action: %2%n\r\n
0x80044016 | File Server Resource Manager encountered an error while contacting the RMS server. The error can be caused by any of the following issues:%n\r\n%n\r\n* Server unreachable: The RMS server was not reachable.%n\r\n* Not authorized: The file server is not authorized to encrypt files by using the RMS server. Verify that the file server has Read and Execute access to the following file on the RMS server: <wwwroot>\_wmcs\certification\ServerCertification.asmx%n\r\n* Predefined template is not valid: The template requested is not valid for encryption.%n\r\n* Custom template is not valid: The custom template provided is not valid for encryption.\r\n%1\r\n
0x80044017 | File Server Resource Manager failed to create a pipeline module object. The error is: %1\r\nSee below for additional details.\r\n%2\r\n
0x80044018 | This computer has case sensitive lookup enabled for file systems and the kernel, which is not supported by File Server Resource Manager.%n\r\nTo disable case sensitivity, set the "obcaseinsensitive" value to 1 in the following registry subkey, HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\kernel.\r\n
0x80044019 | The computer has been joined to a failover cluster. The File Server Resource Manager service (SRMSVC) must be restarted to work correctly on a failover cluster.%n\r\nTo restart the service, open a Windows PowerShell command prompt as an administrator, and then type the following command: restart-service srmsvc -force\r\n
0x8004401a | A debugger has been attached to an FSRM process:%n\r\nCommand: '%1'%n\r\nModule Name: '%2'\r\n
0x8004401b | The debugger command is invalid or a debugger process could not be attached to an FSRM process. Please make sure the command contains at least one instance of the string '[pid]', which will be replaced with the process ID.%n\r\nIf you do not want to attach a debugger process, please delete the corresponding registry entry. See below for details:%n\r\nCommand: '%1'%n\r\nModule Name: '%2'%n\r\nProcess ID: %3%n\r\nRegistry path: '%4'\r\n
0x80045301 | The requested object was not found.\r\n
0x80045302 | One or more of the arguments supplied to the task scheduler are not valid.\r\n
0x80045303 | The specified object already exists.\r\n
0x80045304 | The specified path was not found.\r\n
0x80045305 | The specified user is invalid.\r\n
0x80045306 | The specified path is invalid.\r\n
0x80045307 | The specified limit is invalid.\r\n
0x80045308 | The specified name is invalid.\r\n
0x80045309 | All items in a batch operation failed.\r\n
0x8004530a | The specified text is invalid.\r\n
0x8004530b | The version of the configuration file you are trying to import is not supported. You cannot import configuration files with database versions earlier than 2.0.\r\n
0x8004530d | The specified property is out of range.\r\n
0x8004530e | The specified required property is missing.\r\n
0x8004530f | The specified property combination is invalid.\r\n
0x80045310 | Duplicate names were detected for the same object.\r\n
0x80045311 | The operation or the specified combination of parameters is not supported.\r\n
0x80045313 | A required filter driver is not installed, loaded or ready for service.\r\n
0x80045314 | There is insufficient disk space to perform the requested operation.\r\n
0x80045315 | The specified volume is unsupported.\r\n
0x80045316 | The File Server Resource Manager service encountered an unexpected error.\r\nCheck the application event log for more information.\r\n
0x80045317 | The specified path is insecure.\r\n
0x80045318 | The SMTP server is invalid.\r\n
0x8004531c | The File Server Resource Manager service could not send email due to an error.\r\nCheck the application event log for more information.\r\n
0x8004531e | The specified email address is invalid.\r\n
0x8004531f | The file system might be corrupted.  Please run the CHKDSK utility.\r\n
0x80045320 | The specified command-line executable path is longer than MAX_PATH.\r\n
0x80045321 | The specified file group definition is invalid.\r\n
0x80045324 | The specified file screen is invalid.\r\n
0x80045328 | The specified report format is invalid.\r\n
0x80045329 | The specified report description is invalid.\r\n
0x8004532a | The specified file name is invalid.\r\n
0x8004532c | A volume shadow copy could not be created or was unexpectedly deleted.\r\n
0x8004532d | A File Server Resource Manager XML configuration file or import-export file is corrupted.\r\n
0x8004532e | File Server Resource Manager global configuration cannot be accessed since the cluster service is not running.\r\n
0x8004532f | File Server Resource Manager global configuration cannot be accessed since it is not installed yet.\r\n
0x80045330 | The volume does not reside on a cluster shared disk with an associated cluster resource.\r\n
0x80045331 | There are at least two paths which reside on different cluster shared disks which are not in the same cluster resource group.\r\n
0x80045332 | A report of the specified type already exists in the report job.\r\n
0x80045333 | The report job is already running or queued for running.\r\n
0x80045334 | An error occurred during report generation.\r\n
0x80045335 | The task contains zero or unsupported triggers.\r\n
0x80045336 | A rule or policy attempted to load/use a disabled module.\r\n
0x80045337 | File Server Resource Manager cannot aggregate the value for the specified file property.\r\n
0x80045338 | The limit of the number of messages that the current pipeline context can add to the property bag has been reached.\r\n
0x80045339 | The object is in use and cannot be deleted.\r\n
0x8004533a | Cannot change the name of a property definition once it is set.\r\n
0x8004533b | Cannot change the type of a property definition once it is set.\r\n
0x8004533c | A new property definition cannot be created.  The maximum number of property definitions, {0}, has been reached.\r\n
0x8004533d | A classification job is currently running.  Only one classification job can be running at a time.\r\n
0x8004533e | Classification is not currently running.\r\n
0x8004533f | The file management task is already running or queued for running.\r\n
0x80045340 | Cannot expire a file while running a file management task.\r\n
0x80045341 | Cannot perform a custom action on a file while running a file management task.\r\n
0x80045342 | Cannot send a notification for a file management task.\r\n
0x80045343 | File Server Resource Manager cannot open the file.\r\n
0x80045344 | File Server Resource Manager failed to perform a secure link with a hosted module process.\r\n
0x80045345 | The property cache for the file is invalid and could not be read.\r\n
0x80045346 | A cache storage module already exists.\r\n
0x80045347 | The expiration directory cannot be within the file management scope.\r\n
0x80045348 | A file management task of the specified name already exists.\r\n
0x80045349 | The specified file property has been deleted.\r\n
0x80045350 | The updating of last access times is disabled on this server.  To create a report or file management task that uses the last access time the updating of last access time must be enabled.\r\n
0x80045351 | The specified file property should not be assigned a value.\r\n
0x80045352 | An unknown module cannot be run inside the service process.\r\n
0x80045353 | File Server Resource Manager failed to enumerate file properties because a failure occurred while loading or classifying the file properties.\r\n
0x80045354 | File Server Resource Manager failed to set a file property to the file because a failure occurred while saving the file properties.\r\n
0x80045355 | Classification properties will not be stored because a failure occurred while loading or classifying the file properties.\r\n
0x80045356 | Classification is not supported on the specified reparse point. File Server Resource Manager does not recognize the reparse point's identifier tag for the purposes of classification.\r\n
0x80045357 | The requested property was not found. The file may only have partial classification because a failure occurred while loading or classifying the file properties.\r\n
0x80045358 | The File Server Resource Manager text reader was not initialized.\r\n
0x80045359 | There is no IFilter registered for this extension.\r\n
0x8004535a | File Server Resource Manager failed to write the properties to the file because the file is either corrupt or protected by Rights Management Services.\r\n
0x80045360 | The IFilter for this extension is not registered correctly.\r\n
0x80045361 | There was an error obtaining the file's streaming interface.\r\n
0x80045362 | The file name's extension is too long.\r\n
0x80045363 | The module will not process the specified file because it is unable to determine a compatible file format.\r\n
0x80045364 | File Server Resource Manager could not access the file because it is encrypted.\r\n
0x80045365 | File Server Resource Manager failed to persist the properties to the file.\r\n
0x80045366 | File Server Resource Manager failed to access the volume. It may be offline.\r\n
0x80045367 | The file management action command timed out.\r\n
0x80045368 | The file management action completed successfully, but the exit code cannot be obtained.\r\n
0x80045369 | The module encountered an invalid parameter or a valid parameter with an invalid value or an expected module parameter is not found. Check the application event log for more information.\r\n
0x8004536a | The module initialization failed. Check the application event log for more information.\r\n
0x8004536b | The module session initialization failed. Check the application event log for more information.\r\n
0x8004536c | Classification failed on all volumes. Check the application event log for more information.\r\n
0x8004536d | The file management task cannot be accessed because task conditions were modified by using WMI or Windows PowerShell interfaces. To access or edit the file management task, use the WMI or Windows PowerShell interfaces.\r\n
0x8004536e | The file management task has reached its maximum number of conditions.\r\n
0x8004536f | This object uses a property definition that is deprecated.  You must change it to use a non-deprecated property definition.\r\n
0x80045370 | The property definition sync task timed out.\r\n
0x80045371 | This object uses a property definition that doesn't exist.  You must change it to use an existing property definition.\r\n
0x80045372 | File Server Resource Manager encountered an invalid resource claim in Active Directory.\r\n
0x80045373 | The classification operation was canceled.\r\n
0x80045374 | File Server Resource Manager encountered an invalid folder property store.\r\n
0x80045375 | File Server Resource Manager is rebuilding the index of Folder Usage property values.\r\n
0x80045376 | The specified property definition doesn't apply to files.\r\n
0x80045377 | The classification request timed out.\r\n
0x80045378 | Classification failed on one or more files in the batch operation.\r\n
0x80045379 | This property is a system property and cannot be deleted.\r\n
0x8004537a | The file is being used by another application and cannot be accessed at this time.\r\n
0x8004537b | Access-denied assistance is not enabled for this error.\r\n
0x8004537c | File Server Resource Manager could not create a temporary file copy.\r\n
0x8004537d | Access-denied assistance cannot send an email because an email address could not be found for the path specified, and sending email to the administrator is not enabled. \r\n
0x8004537e | The current user has sent the maximum number of requests for access-denied assistance. \r\n
0x8004537f | The path is not included in a classification rule.\r\n
0x80045380 | The RMS template used to configure the file management task no longer exists.  Please select another template.\r\n
0x80045381 | The computer hosting the file or folder does not support setting secure properties. This can occur if the computer is running Windows Server 2008 R2, Windows 7, or earlier, or if the computer is not running Windows.\r\n
0x80045382 | File Server Resource Manager cannot run the file management task because no RMS protectors are installed.\r\n
0x80045383 | File Server Resource Manager cannot protect the file because an RMS protector for the file type is not installed.\r\n
0x80045384 | The specified property definition doesn't apply to folders.\r\n
0x80045385 | The specified property definition type is not secure.\r\n
0x80045386 | The specified property definition type is not global.\r\n
0x80045387 | Unexpected failure from a WMI call.\r\n
0x80045388 | Cannot protect a file while running a file management task.\r\n
0x80045389 | The property definition sync task encountered errors.\r\nCheck the application event log for more information.\r\n
0x80045390 | The server does not provide access-denied assistance.\r\n
0x80045391 | Access-denied assistance cannot be provided for local paths.\r\n
0x80045392 | Access-denied assistance requires that the server be joined to a domain.\r\n
0x80045393 | File Server Resource Manager could not remove the read-only attribute from a file.\r\n
0x80045394 | A continuous file management job cannot have conditions based on the file's last accessed/modified or created times and cannot define any notifications.\r\n
0x80045395 | The object contains a schedule that was created by using an earlier version of File Server Resource Manager and that is incompatible with the current version of Windows Server. Edit the schedule on this computer to update it.\r\n
0x80045396 | This operation is not supported for paths on which Offline Files is enabled.\r\n
0x80045397 | Cannot write to the specified expiration directory. Confirm that the permissions of the expiration directory grant Write permission to the computer account of the server performing the file expiration task.\r\n
0x80045398 | The expiration path must be 150 characters or shorter.\r\n
0x80045399 | The expiration directory must be on a volume formatted with the NTFS file system.\r\n
0x8004539a | This file management job is deprecated. Please check the configuration of the file management job and verify that it is up-to-date.\r\n

### 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x00045304 | At least one failure occurred in a batch operation.\r\n
0x00045305 | The file may only have partial classification because a failure occurred while loading or classifying the file properties.\r\n
0x00045306 | Classification failed on one or more volumes. Check the application event log for more information.\r\n
0x0004531b | Auto apply quota configuration for one or more folders failed.  Check the application event log for more information.\r\n
0x80040002 | File Server Resource Manager Service information: Volume '%1' appears as disconnected and it is\r\nignored by the service.  You may want to rescan disks.   Error: %2.\r\n%3\r\n
0x80040003 | File Server Resource Manager Service information: The COM Server with CLSID %1 and name '%2' cannot be started on machine '%3'.\r\nMost likely the CPU is under heavy load.  Error: %4.\r\n%5\r\n
0x80040004 | File Server Resource Manager Service information: The COM Server with CLSID %1 and name '%2' cannot be started on machine '%3'.  Error: %4.\r\n%5\r\n
0x80040005 | File Server Resource Manager Service error: The COM Server with CLSID %1 and name '%2' cannot be started on machine '%3' during Safe Mode.\r\nThe File Server Resource Manager service cannot start while in safe mode.  Error: %4.\r\n%5\r\n
0x80040006 | File Server Resource Manager Service error: A critical component required by the File Server Resource Manager Service is not registered.\r\nThis might happen if an error occurred during Windows setup, or if the computer does not have the Windows Server 2008 or later version of FSRM installed.\r\nThe error returned from CoCreateInstance on class with CLSID %1 and Name '%2' on machine '%3' is %4.\r\n%5\r\n
0x80040007 | File Server Resource Manager Service error: The FSRM event log source EventMessageFile '%1' found in registry key '%2' is not correct. \r\nThis might happen if an error occurred during Windows setup.\r\n%3\r\n
0x80042001 | File Server Resource Manager Service error: Unexpected error calling routine %1.  hr = %2.\r\n%3\r\n
0x80042002 | File Server Resource Manager failed to initialize its WMI event provider component. Therefore, WMI events will not be sent during quota and screening notification processing.\r\nIn order to receive WMI events, check the status of the WMI service and WMI event logs, correct the WMI errors, and restart the File Server Resource Manager service.\r\n%1\r\n
0x80042003 | File Server Resource Manager failed to initialize its shadow copy writer component. Therefore, backup and restore of the File Server Resource Manager stores may not be done correctly.\r\nIn order to properly perform backup and restore of File Server Resource Manager, check the status of the COM+ Event System service and VSS and COM+ event logs, correct the errors, and restart the File Server Resource Manager service.\r\n%1\r\n
0x80042004 | The storage reports repository will not be included in the File Server Resource Manager backup because the service failed to retrieve the repository locations.\r\n%1\r\n
0x80042005 | File Server Resource Manager Service error: Unexpected error.\r\n%1\r\n
0x80042006 | File Server Resource Manager Service warning: %1.  Error: %2.\r\n%3\r\n
0x80042007 | Error occurred during file screen configuration.  File screening will not be enforced for directory '%1' on volume '%2' until the error is corrected and the volume is remounted.\r\n%3\r\n
0x80042008 | FSRM Assert Failure: %1\r\n
0x80042009 | File Server Resource Manager Service error: Unexpected COM error %1: %2.  Error code: %3.\r\n%4\r\n
0x8004200a | Communication port '%1' to the '%2' filter driver was established.\r\n
0x8004200b | Communication port '%1' to the '%2' filter driver was disconnected.\r\nThe '%2' filter driver may need to be started.  Retrying...\r\n
0x8004200c | The File Server Resource Manager detected %1 unprocessed quota or screening notifications when the service or system was stopping.  Administrators or end-users may not have received notification of quota or screening violations.  Running a quota report can help identify quotas that are in a critical state.\r\n
0x8004200d | The required '%1' property of the action '%2' is missing.\r\n%3\r\n
0x8004200e | The required '%1' property of the action '%2' at threshold %3%% is missing.\r\n
0x8004200f | The required '%1' property of the action '%2' at the limit is missing.\r\n
0x80042010 | The '%1' property of the action '%2' is not within the legal range.\r\n%3\r\n
0x80042011 | The '%1' property of the action '%2' at threshold %3%% is not within the legal range.\r\n
0x80042012 | The '%1' property of the action '%2' at the limit is not within the legal range.\r\n
0x80042013 | The properties of the action '%2' specify an illegal combination.\r\n%3\r\n
0x80042014 | The properties of the action '%2' at threshold %3%% specify an illegal combination.\r\n
0x80042015 | The properties of the action '%2' at the limit specify an illegal combination.\r\n
0x80042016 | Multiple actions were found sharing the same action name: '%1'.\r\n
0x80042017 | %1\r\n
0x80042018 | This command was initiated by the File Server Resource Manager service.  It belongs to the action '%1' of the file screen on path '%2'.\r\n
0x8004201a | This command was initiated by the File Server Resource Manager service.  It belongs to the action '%1' on the %2%% threshold on the quota on path '%3'.\r\n
0x8004201b | This command was initiated by the File Server Resource Manager service.  It belongs to the action '%1' on the %2%% threshold on the quota on path '%3' for user '%4'.\r\n
0x8004201c | This command was initiated by the File Server Resource Manager service.  It belongs to the action '%1' on the limit on the quota on path '%3'.\r\n
0x8004201d | This command was initiated by the File Server Resource Manager service.  It belongs to the action '%1' on the limit on the quota on '%3' for user '%4'.\r\n
0x8004201f | File Server Resource Manager will no longer monitor the following FSRM-initiated command-line programs because the service is shutting down: '%1'\r\n
0x80042020 | File Server Resource Manager killed the following FSRM-initiated command-line program because it exceeded its %1-minute run time limit setting: '%2'\r\n
0x80042021 | File Server Resource Manager was unable to terminate the following FSRM-initiated command-line program: '%1'\r\n
0x80042022 | The following FSRM-initiated command-line program exited with return code %1\r\n
0x80042023 | File Server Resource Manager was unable to access the following directory: '%1'.  You must give Local System access to this directory to do further operations on it.\r\n
0x80042024 | File Server Resource Manager was unable to access the following file or volume: '%1'.  This file or volume might be locked by another application right now, or you might need to give Local System access to it.\r\n
0x80042025 | The path '%1' does not exist. This path will be ignored for now. The directory was probably deleted and will not be included in reporting or classification. Please reconfigure reporting or classification settings appropriately.\r\n
0x80042026 | Invalid namespace root specified for reporting or classification: the path '%1' is not a valid directory (for example - it might be a file). Please reconfigure reporting or classification settings appropriately.\r\n
0x80042027 | The volume mounted at '%1' ('%2') for namespace root '%3' is not a valid volume for reporting or classification. Make sure that you include only paths on fixed NTFS volumes in the report. This path will be ignored for now. Please reconfigure reporting or classification settings appropriately.\r\n
0x80042028 | File Server Resource Manager failed to retrieve the mount points under the volume mounted at '%1'. Make sure the volume mounted at this location is not offline or unavailable. This path will be ignored for now.\r\n
0x80042029 | File Server Resource Manager failed to register all reporting and classification consumers.\r\n
0x8004202a | File Server Resource Manager failed to register all classification rules.\r\n
0x8004202b | File Server Resource Manager failed to initialize the volume scanner.\r\n
0x8004202c | File Server Resource Manager encountered an unexpected error while initializing modules in the classification pipeline.\r\n
0x8004202d | File Server Resource Manager failed to initialize all consumers in the classification pipeline.\r\n
0x8004202e | File Server Resource Manager encountered an unexpected error during volume scan of volumes mounted at '%1' ('%2'). To find out more information about the root cause for this error please consult the Application/System event log for other FSRM, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:\r\n
0x8004202f | File Server Resource Manager was unable to create or access the shadow copy for volumes mounted at '%1' ('%2'). Possible causes include an improper Shadow Copy configuration, insufficient disk space, or extreme memory, I/O or CPU load of the system. To find out more information about the root cause for this error please consult the Application/System event log for other FSRM, VSS or VOLSNAP errors related with these volumes. Also, you might want to make sure that you can create shadow copies on these volumes by using the VSSADMIN command like this: VSSADMIN CREATE SHADOW /For=C:\r\n
0x80042030 | File Server Resource Manager was unable to access volumes mounted at '%1' ('%2'). Make sure that dismount or format operations do not happen while running classification or generating reports.\r\n
0x80042031 | Classification module '%1' has failed.\r\n
0x80042032 | Reporting or classification consumer '%1' has failed.\r\n
0x80042033 | Scanning statistics on volume mounted at '%1' ('%2'):%n\r\n- File count: %3%n\r\n- Milliseconds elapsed: %4%n\r\n- Files per second: %5%n\r\n- Resident stream count: %6%n\r\n
0x80042034 | %1\r\n
0x80042035 | %1\r\n
0x80042036 | Scanning statistics on pipeline running on '%1':%n\r\n%2%n\r\n
0x80042037 | A fatal error has occurred in the classification pipeline. All currently running reporting, classification, and file management jobs will be aborted.\r\n
0x80042038 | Performance statistics for module '%1':%n\r\n- Total file count: %2%n\r\n- Total time spent (s): %3%n\r\n- Average time spent per file (ms): %4%n\r\n- Maximum time spent on a file (ms): %5%n\r\n- File that caused maximum time: %6%n\r\n- Files processing for longer than 10 seconds: %7%n\r\n- Files processing for longer than 1 minute: %8%n\r\n- Files processing for longer than 10 minutes: %9%n\r\n- Files processing for longer than 1 hour: %10%n\r\n
0x80042039 | File Server Resource Manager was unable to access a file or volume. Details:%n\r\n%1%n\r\nThe volume may be inaccessible for I/O operations or marked read-only. In case of a cluster volume, this may be a transient failure during failover.\r\n
0x8004203a | The File Server Resource Manager configuration file '%1' is not found. It is required that the system or volume be restored from backup.\r\n%2\r\n
0x8004203b | A File Server Resource Manager module encountered an invalid parameter or a valid parameter with an invalid value or an expected module parameter is not found. Parameter: '%1'\r\n
0x8004203c | File Server Resource Manager was unable to scan volume  '%1' ('%2'). \r\n
0x8004203d | File Server Resource Manager failed to schedule auto apply quota rebuilding on volume '%1'.\r\n
0x8004203e | File Server Resource Manager encountered an error during a classification operation.%n\r\nHRESULT = %1%n%n\r\nDetails:%n\r\n%2\r\n
0x8004203f | File Server Resource Manager set a property on a file outside of automatic classification.\r\n%1\r\n
0x80042040 | File Server Resource Manager cleared a property on a file outside of automatic classification.\r\n%1\r\n
0x80042041 | File Server Resource Manager set properties on a file outside of automatic classification. This can occur if a file is manually classified. No user action is required.\r\n%1\r\n
0x80043001 | File Server Resource Manager detected an invalid SID, %1, for the quota on directory, '%2'.\r\n
0x80043002 | File Server Resource Manager failed to automatically upgrade its configuration on volume %1. The volume cannot be added to the upgrade queue.\r\n
0x80043003 | The File Server Resource Manager Reports service is shutting down due to idle timeout.\r\n%1\r\n
0x80043004 | The File Server Resource Manager Reports service is shutting down due to shutdown event from the Service Control Manager.\r\n%1\r\n
0x80043005 | The File Server Resource Manager configuration file or import-export file '%1' is corrupted.  If the corrupt file is a configuration file, it is required that the system or volume be restored from backup.  If the file is an import-export file, export the items again and retry the operation without editing the file contents.\r\n%2\r\n
0x80043006 | File Server Resource Manager has received a configuration request from the file screen filter driver for volume '%1'.\r\n
0x80043007 | File Server Resource Manager has completed a configuration request from the file screen filter driver for volume '%1'.\r\n
0x80043008 | File Server Resource Manager failed to configure auto apply quota settings on path '%1'.\r\n%2\r\n
0x80043009 | File Server Resource Manager regenerated one or more records for configuration database '%1'.  The new records contain no quota or screening notification configuration, so it is recommended that the system or volume be restored from backup.\r\n%2\r\n
0x8004300a | A File Server Resource Manager Service command line action was not run because command line actions are disabled on this machine.  Use the FSRM management console to enable command line notifications on this system.\r\n%1\r\n
0x8004300b | A File Server Resource Manager Service command line action was not run because the last person who saved it is no longer an administrator on this machine.  Use the FSRM management console to save again the quota, screening or file management configuration.\r\n%1\r\n
0x8004300c | A File Server Resource Manager Service command line action specifies an insecure path because it gives write access to '%1' on path '%2'.  Move the program to a directory that permits write access only to privileged users.\r\n%3\r\n
0x8004300d | A File Server Resource Manager Service command line action could not be run.\r\n%1\r\n
0x8004300e | A File Server Resource Manager Service event log action could not be run.\r\n%1\r\n
0x8004300f | A File Server Resource Manager Service email action could not be run because there is no SMTP server set.  Use the FSRM management console to specify the SMTP server to use.\r\n%1\r\n
0x80043011 | A File Server Resource Manager Service email action could not be run because the specified TO or FROM address is invalid.  Use the FSRM management console to add valid TO and FROM e-mail addresses to the quota, screening or file management configuration.\r\n%1\r\n
0x80043012 | A File Server Resource Manager Service email action could not be run.\r\n%1\r\n
0x80043013 | The File Server Resource Manager configuration file '%1' is out of sync or missing records.  This could have been caused by inadvertent administrator action, or by incomplete backup/restore.  FSRM will attempt to regenerate default records for interim use, but there may be some missing functionality.  For example, quota or screening configurations may be missing notifications.  It is recommended that the system or volume be restored from backup.  \r\n%2\r\n
0x80043014 | The File Server Resource Manager configuration file '%1' is missing.  This could have been caused by inadvertent administrator action, or by incomplete backup/restore.  An empty configuration file has been created for interim use.  It is recommended that the system or volume be restored from backup.  \r\n%2\r\n
0x80043015 | A File Server Resource Manager configuration file or import-export file is corrupted.  If the corrupt file is a configuration file, it is required that the system or volume be restored from backup.  If the file is an import-export file, export the items again and retry the operation without editing the file contents.\r\n%1\r\n
0x80043016 | Shadow copy '%1' was deleted during storage report generation.  Volume '%2' might be configured with inadequate shadow copy storage area.  Storage reports may be temporarily unavailable for this volume.\r\n%3\r\n
0x80043017 | Shadow copy creation failed for volume '%1' with error %2.  The volume might be configured with inadequate shadow copy storage area.  Storage reports may be temporarily unavailable for this volume.\r\n%3\r\n
0x80043018 | File Server Resource Manager encountered an error while attempting to find the network share and DFS paths that expose the local path '%1'.  The remote paths may be temporarily unavailable to FSRM quota and screening notifications.\r\n%2\r\n
0x80043019 | The File Server Resource Manager global configuration data store has been created.\r\n
0x8004301a | File Server Resource Manager encountered an error while initializing local-to-remote path mapping.  Mappings from local file paths to share and DFS paths will not be available until the FSRM service is restarted or the system reboots.\r\n%1\r\n
0x8004301b | File Server Resource Manager encountered an error when uninitializing local-to-remote path mapping.\r\n%1\r\n
0x8004301c | Volume '%1' is not supported for shadow copy.  It is possible that the volume was removed from the system.  Storage reports will not be available for this volume.\r\n%2\r\n
0x8004301d | File Server Resource Manager failed to enumerate share paths or DFS paths.  Mappings from local file paths to share and DFS paths may be incomplete or temporarily unavailable.  FSRM will retry the operation at a later time.\r\n%1\r\n
0x8004301e | Failed saving one of the configuration stores on volume '%1' due to a disk-full error:\r\nIf the disk is full, please clean it up (extend the volume or delete some files).\r\nIf the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.\r\n%2\r\n
0x8004301f | Shadow copy creation failed for volume '%1' because other shadow copies were being created.\r\n%3\r\n
0x80043020 | The volume '%1' has been deleted or removed from the system.\r\n%2\r\n
0x80043021 | The file system on volume '%1' is potentially corrupted.  Please run the CHKDSK utility to verify and fix the file system.\r\n%2\r\n
0x80043022 | Error occurred during default template setup.  Template '%1', could not be installed and will not be available on the system until the system is reinstalled.\r\n%2\r\n
0x80043023 | Error occurred during file screen configuration.  File screening will not be enforced on volume '%1' until the error is corrected and the volume is remounted.\r\n%2\r\n
0x80043024 | %1\r\n
0x80043025 | %1\r\n
0x80043026 | File Server Resource Manager global configuration cannot be accessed since the cluster service is not running. Please start the cluster service and retry the operation.\r\n%1\r\n
0x80043027 | The File Server Resource Manager global configuration cannot be accessed since the cluster service is not running. Please start the cluster service.\r\n%1\r\n
0x80043028 | File Server Resource Manager cannot start file screening on this system since the cluster service is not running. Screening will start once the cluster service is running.\r\n%1\r\n
0x80043029 | Failed writing the file screen audit log on volume '%1' due to a disk-full error:\r\nIf the disk is full, please clean it up (extend the volume or delete some files).\r\nIf the disk is not full, but there is a hard quota on the volume root, please delete, disable or increase this quota.\r\n%2\r\n
0x8004302a | File Server Resource Manager successfully created a cluster resource for the reports scheduled task '%1', but failed to bring the resource online. Please check the resource status in the cluster administration console.\r\n%2\r\n
0x8004302b | File Server Resource Manager failed to take a cluster resource offline for the reports scheduled task '%1'. The report task cannot be deleted if the resource remains online. Please check the resource status in the cluster administration console.\r\n%2\r\n
0x8004302c | File Server Resource Manager had a failure when invoking an COM call on an external component:%n\r\nThis might be a problem with this specific COM component that supplies this functionality.%n\r\nYou might want to follow up the error with the vendor implementing this module.%n\r\n
0x8004302d | File Server Resource Manager attempted to load a disabled module.%n\r\nPlease ensure that all enabled modules in use (by FSRM classification rules and policies) are enabled.%n\r\n
0x8004302e | An error occurred while File Server Resource Manager attempted to impersonate user %1 to load module %2.%n\r\nPlease check the security policies on this machine. (GetLastError = %3)%n\r\n
0x8004302f | An error occurred while File Server Resource Manager attempted to install a default module.%n\r\n%1\r\n
0x80043030 | Rule '%1' refers to module definition '%2', which could not be found; rule will not be used for classification.\r\n
0x80043031 | Rule '%1' refers to a property '%2' that has no property definition; rule will not be used for classification.\r\n
0x80043032 | The Continuous scanner encountered an unexpected error.\r\n%1\r\n
0x80043033 | File Server Resource Manager failed to find the claim list '%1' in Active Directory (ADsPath: %2). Please check that the claims list configured for this machine in Group Policy exists in Active Directory.\r\n
0x80043034 | File Server Resource Manager encountered a malformed claim in Active Directory Domain Services (AD DS). Please reconfigure the claim in AD DS.%n\r\n%n\r\nDetails:%n\r\nDomain controller: %1%n\r\nResource property list: %2%n\r\nResource property name: %3%n\r\n
0x80043035 | File Server Resource Manager encountered the claim %1 in Active Directory with the same name as a local property definition.  The local property definition is being marked as deprecated.\r\n
0x80043037 | File Server Resource Manager finished syncing claims from Active Directory Domain Services with no errors.%n\r\n%n\r\nDetails:%n\r\nDomain controller: %1%n\r\nResource property list: %2%n\r\nProperties created: %3%n\r\nProperties modified: %4%n\r\nProperties deleted: %5%n\r\n
0x80043038 | File Server Resource Manager finished syncing claims from Active Directory and encountered errors during the sync (%1).  Please check previous event logs for details.\r\n
0x80043039 | File Server Resource Manager failed to update property definition '%1' with data from Active Directory.  The error is: %2.\r\n
0x8004303a | File Server Resource Manager failed to change or delete property definition '%1'.  Please check previous event logs for details.\r\n
0x8004303b | File Server Resource Manager failed to create the predefined property definition '%1' with the error %2.\r\n
0x8004303c | File Server Resource Manager could not add the Access-Denied Assistance Users group to the Remote Management Users group. Try manually adding the Access-Denied Assistance Users group to the Remote Management Users group.\r\n
0x8004303d | File Server Resource Manager could not remove the Access-Denied Assistance Users group from the Remote Management Users group. Try manually removing the Access-Denied Assistance Users group from the Remote Management Users group.\r\n
0x8004303e | File Server Resource Manager could not add '%1' group to '%2' group. Try adding this group manually to enable Access-Denied Assistance for users.\r\n
0x8004303f | File Server Resource Manager module '%1' took too long processing file '%2'. The module was restarted and the file skipped. The file will be processed by a future classification attempt.\r\n
0x80044001 | File Server Resource Manager Service added a quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044002 | File Server Resource Manager Service modified a quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044003 | File Server Resource Manager Service deleted a quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044004 | File Server Resource Manager Service added an auto apply quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044005 | File Server Resource Manager Service modified an auto apply quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044006 | File Server Resource Manager Service deleted an auto apply quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044007 | File Server Resource Manager Service derived a quota from an auto apply quota.%n\r\n%n\r\nQuota ID: %1%n\r\nAuto apply quota ID: %2%n\r\nPath: %3%n\r\n
0x80044008 | File Server Resource Manager set a property on a file during automatic classification.%n\r\n%n\r\nFile: %1%n\r\nProperty Changed: %2%n\r\nProperty Value: %3%n\r\nRetrieved From Storage: %4%n\r\nRule Applied: %5%n\r\n
0x80044009 | File Server Resource Manager applied a file management job expiration action to a file.%n\r\n%n\r\nFile Management Job Name: %1%n\r\nExpiration Action: %2%n\r\n
0x8004400a | File Server Resource Manager applied a file management job custom action to a file.%n\r\n%n\r\nFile Management Job Name: %1%n\r\nCustom Action: %2%n\r\n
0x8004400b | File Server Resource Manager performed the following file management job notification:%n\r\n%n\r\nFile Management Job Name: %1%n\r\nNotification Days: %2%n\r\nActions Taken: %3%n\r\n
0x8004400c | File Server Resource Manager encountered an error while classifying a file during automatic classification.%n\r\n%n\r\nFile: %1%n\r\nModule: %2%n\r\nMessage: %3%n\r\n
0x8004400d | The following property definition was %1:%n\r\n%n\r\nName: %2%n\r\nType: %3%n\r\nGlobal: %4%n\r\nSecure: %5%n\r\nDeprecated: %6%n\r\nApplies To: %7%n\r\nPossible Values: %8%n\r\n
0x8004400e | The following classification rule was %1:%n\r\n%n\r\nName: %2%n\r\nEnabled: %3%n\r\nValid: %4%n\r\nScope: %5%n\r\nProperty Assignment Method: %6%n\r\nProperty Assigned: %7%n\r\nValue: %8%n\r\nRe-evaluation Option: %9%n\r\nParameters: %10%n\r\n
0x8004400f | The following classifier module definition was %1:%n\r\n%n\r\nName: %2%n\r\nCOM CLSID: %3%n\r\nProperties Set: %4%n\r\nNeeds Explicit Value: %5%n\r\nParameters: %6%n\r\n
0x80044010 | The following storage module definition was %1:%n\r\n%n\r\nName: %2%n\r\nCOM CLSID: %3%n\r\nSupported Extensions: %4%n\r\nParameters: %5%n\r\n
0x80044011 | The following access-denied assistance error configuration was %1:%n\r\n%n\r\nError: %2%n\r\nEnabled: %3%n\r\nClient Display Flags: %4%n\r\nError Message: %5%n\r\nEmail Flags: %6%n\r\nAdditional To Emails: %7%n\r\nEmail Message: %8%n\r\n
0x80044012 | A request for assistance with an error was sent.%n\r\n%n\r\nDetails:%n\r\nError: %1%n\r\nEmail sent to: %2%n\r\nEmail subject: %3%n\r\nUser: %4\%5%n\r\nFile path: %6%n\r\nParent folder: %7%n\r\nMessage from administrator: %8%n\r\nMessage from %4\%5: %9%n\r\n
0x80044013 | A request for assistance with an error could not be sent because the email address of the recipient is blank.%n\r\n%n\r\nDetails:%n\r\nError: %1%n\r\nEmail subject: %2%n\r\nUser: %3\%4%n\r\nFile path: %5%n\r\nParent folder: %6%n\r\nMessage from administrator: %7%n\r\nMessage from %3\%4: %8%n\r\n
0x80044014 | An access-denied assistance error is configured to send email to the file server administrator, but no email address is specified in the Default Administrator Recipients box in the Options dialog box of File Server Resource Manager.%n\r\n
0x80044015 | File Server Resource Manager applied a file management task RMS Encryption action to a file.%n\r\n%n\r\nFile management task name: %1%n\r\nCustom action: %2%n\r\n
0x80044016 | File Server Resource Manager encountered an error while contacting the RMS server. The error can be caused by any of the following issues:%n\r\n%n\r\n* Server unreachable: The RMS server was not reachable.%n\r\n* Not authorized: The file server is not authorized to encrypt files by using the RMS server. Verify that the file server has Read and Execute access to the following file on the RMS server: <wwwroot>\_wmcs\certification\ServerCertification.asmx%n\r\n* Predefined template is not valid: The template requested is not valid for encryption.%n\r\n* Custom template is not valid: The custom template provided is not valid for encryption.\r\n%1\r\n
0x80044017 | File Server Resource Manager failed to create a pipeline module object. The error is: %1\r\nSee below for additional details.\r\n%2\r\n
0x80044018 | This computer has case sensitive lookup enabled for file systems and the kernel, which is not supported by File Server Resource Manager.%n\r\nTo disable case sensitivity, set the "obcaseinsensitive" value to 1 in the following registry subkey, HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\kernel.\r\n
0x80044019 | The computer has been joined to a failover cluster. The File Server Resource Manager service (SRMSVC) must be restarted to work correctly on a failover cluster.%n\r\nTo restart the service, open a Windows PowerShell command prompt as an administrator, and then type the following command: restart-service srmsvc -force\r\n
0x8004401a | A debugger has been attached to an FSRM process:%n\r\nCommand: '%1'%n\r\nModule Name: '%2'\r\n
0x8004401b | The debugger command is invalid or a debugger process could not be attached to an FSRM process. Please make sure the command contains at least one instance of the string '[pid]', which will be replaced with the process ID.%n\r\nIf you do not want to attach a debugger process, please delete the corresponding registry entry. See below for details:%n\r\nCommand: '%1'%n\r\nModule Name: '%2'%n\r\nProcess ID: %3%n\r\nRegistry path: '%4'\r\n
0x80045301 | The requested object was not found.\r\n
0x80045302 | One or more of the arguments supplied to the task scheduler are not valid.\r\n
0x80045303 | The specified object already exists.\r\n
0x80045304 | The specified path was not found.\r\n
0x80045305 | The specified user is invalid.\r\n
0x80045306 | The specified path is invalid.\r\n
0x80045307 | The specified limit is invalid.\r\n
0x80045308 | The specified name is invalid.\r\n
0x80045309 | All items in a batch operation failed.\r\n
0x8004530a | The specified text is invalid.\r\n
0x8004530b | The version of the configuration file you are trying to import is not supported. You cannot import configuration files with database versions earlier than 2.0.\r\n
0x8004530d | The specified property is out of range.\r\n
0x8004530e | The specified required property is missing.\r\n
0x8004530f | The specified property combination is invalid.\r\n
0x80045310 | Duplicate names were detected for the same object.\r\n
0x80045311 | The operation or the specified combination of parameters is not supported.\r\n
0x80045313 | A required filter driver is not installed, loaded or ready for service.\r\n
0x80045314 | There is insufficient disk space to perform the requested operation.\r\n
0x80045315 | The specified volume is unsupported.\r\n
0x80045316 | The File Server Resource Manager service encountered an unexpected error.\r\nCheck the application event log for more information.\r\n
0x80045317 | The specified path is insecure.\r\n
0x80045318 | The SMTP server is invalid.\r\n
0x8004531c | The File Server Resource Manager service could not send email due to an error.\r\nCheck the application event log for more information.\r\n
0x8004531e | The specified email address is invalid.\r\n
0x8004531f | The file system might be corrupted.  Please run the CHKDSK utility.\r\n
0x80045320 | The specified command-line executable path is longer than MAX_PATH.\r\n
0x80045321 | The specified file group definition is invalid.\r\n
0x80045324 | The specified file screen is invalid.\r\n
0x80045328 | The specified report format is invalid.\r\n
0x80045329 | The specified report description is invalid.\r\n
0x8004532a | The specified file name is invalid.\r\n
0x8004532c | A volume shadow copy could not be created or was unexpectedly deleted.\r\n
0x8004532d | A File Server Resource Manager XML configuration file or import-export file is corrupted.\r\n
0x8004532e | File Server Resource Manager global configuration cannot be accessed since the cluster service is not running.\r\n
0x8004532f | File Server Resource Manager global configuration cannot be accessed since it is not installed yet.\r\n
0x80045330 | The volume does not reside on a cluster shared disk with an associated cluster resource.\r\n
0x80045331 | There are at least two paths which reside on different cluster shared disks which are not in the same cluster resource group.\r\n
0x80045332 | A report of the specified type already exists in the report job.\r\n
0x80045333 | The report job is already running or queued for running.\r\n
0x80045334 | An error occurred during report generation.\r\n
0x80045335 | The task contains zero or unsupported triggers.\r\n
0x80045336 | A rule or policy attempted to load/use a disabled module.\r\n
0x80045337 | File Server Resource Manager cannot aggregate the value for the specified file property.\r\n
0x80045338 | The limit of the number of messages that the current pipeline context can add to the property bag has been reached.\r\n
0x80045339 | The object is in use and cannot be deleted.\r\n
0x8004533a | Cannot change the name of a property definition once it is set.\r\n
0x8004533b | Cannot change the type of a property definition once it is set.\r\n
0x8004533c | A new property definition cannot be created.  The maximum number of property definitions, {0}, has been reached.\r\n
0x8004533d | A classification job is currently running.  Only one classification job can be running at a time.\r\n
0x8004533e | Classification is not currently running.\r\n
0x8004533f | The file management task is already running or queued for running.\r\n
0x80045340 | Cannot expire a file while running a file management task.\r\n
0x80045341 | Cannot perform a custom action on a file while running a file management task.\r\n
0x80045342 | Cannot send a notification for a file management task.\r\n
0x80045343 | File Server Resource Manager cannot open the file.\r\n
0x80045344 | File Server Resource Manager failed to perform a secure link with a hosted module process.\r\n
0x80045345 | The property cache for the file is invalid and could not be read.\r\n
0x80045346 | A cache storage module already exists.\r\n
0x80045347 | The expiration directory cannot be within the file management scope.\r\n
0x80045348 | A file management task of the specified name already exists.\r\n
0x80045349 | The specified file property has been deleted.\r\n
0x80045350 | The updating of last access times is disabled on this server.  To create a report or file management task that uses the last access time the updating of last access time must be enabled.\r\n
0x80045351 | The specified file property should not be assigned a value.\r\n
0x80045352 | An unknown module cannot be run inside the service process.\r\n
0x80045353 | File Server Resource Manager failed to enumerate file properties because a failure occurred while loading or classifying the file properties.\r\n
0x80045354 | File Server Resource Manager failed to set a file property to the file because a failure occurred while saving the file properties.\r\n
0x80045355 | Classification properties will not be stored because a failure occurred while loading or classifying the file properties.\r\n
0x80045356 | Classification is not supported on the specified reparse point. File Server Resource Manager does not recognize the reparse point's identifier tag for the purposes of classification.\r\n
0x80045357 | The requested property was not found. The file may only have partial classification because a failure occurred while loading or classifying the file properties.\r\n
0x80045358 | The File Server Resource Manager text reader was not initialized.\r\n
0x80045359 | There is no IFilter registered for this extension.\r\n
0x8004535a | File Server Resource Manager failed to write the properties to the file because the file is either corrupt or protected by Rights Management Services.\r\n
0x80045360 | The IFilter for this extension is not registered correctly.\r\n
0x80045361 | There was an error obtaining the file's streaming interface.\r\n
0x80045362 | The file name's extension is too long.\r\n
0x80045363 | The module will not process the specified file because it is unable to determine a compatible file format.\r\n
0x80045364 | File Server Resource Manager could not access the file because it is encrypted.\r\n
0x80045365 | File Server Resource Manager failed to persist the properties to the file.\r\n
0x80045366 | File Server Resource Manager failed to access the volume. It may be offline.\r\n
0x80045367 | The file management action command timed out.\r\n
0x80045368 | The file management action completed successfully, but the exit code cannot be obtained.\r\n
0x80045369 | The module encountered an invalid parameter or a valid parameter with an invalid value or an expected module parameter is not found. Check the application event log for more information.\r\n
0x8004536a | The module initialization failed. Check the application event log for more information.\r\n
0x8004536b | The module session initialization failed. Check the application event log for more information.\r\n
0x8004536c | Classification failed on all volumes. Check the application event log for more information.\r\n
0x8004536d | The file management task cannot be accessed because task conditions were modified by using WMI or Windows PowerShell interfaces. To access or edit the file management task, use the WMI or Windows PowerShell interfaces.\r\n
0x8004536e | The file management task has reached its maximum number of conditions.\r\n
0x8004536f | This object uses a property definition that is deprecated.  You must change it to use a non-deprecated property definition.\r\n
0x80045370 | The property definition sync task timed out.\r\n
0x80045371 | This object uses a property definition that doesn't exist.  You must change it to use an existing property definition.\r\n
0x80045372 | File Server Resource Manager encountered an invalid resource claim in Active Directory.\r\n
0x80045373 | The classification operation was canceled.\r\n
0x80045374 | File Server Resource Manager encountered an invalid folder property store.\r\n
0x80045375 | File Server Resource Manager is rebuilding the index of Folder Usage property values.\r\n
0x80045376 | The specified property definition doesn't apply to files.\r\n
0x80045377 | The classification request timed out.\r\n
0x80045378 | Classification failed on one or more files in the batch operation.\r\n
0x80045379 | This property is a system property and cannot be deleted.\r\n
0x8004537a | The file is being used by another application and cannot be accessed at this time.\r\n
0x8004537b | Access-denied assistance is not enabled for this error.\r\n
0x8004537c | File Server Resource Manager could not create a temporary file copy.\r\n
0x8004537d | Access-denied assistance cannot send an email because an email address could not be found for the path specified, and sending email to the administrator is not enabled. \r\n
0x8004537e | The current user has sent the maximum number of requests for access-denied assistance. \r\n
0x8004537f | The path is not included in a classification rule.\r\n
0x80045380 | The RMS template used to configure the file management task no longer exists.  Please select another template.\r\n
0x80045381 | The computer hosting the file or folder does not support setting secure properties. This can occur if the computer is running Windows Server 2008 R2, Windows 7, or earlier, or if the computer is not running Windows.\r\n
0x80045382 | File Server Resource Manager cannot run the file management task because no RMS protectors are installed.\r\n
0x80045383 | File Server Resource Manager cannot protect the file because an RMS protector for the file type is not installed.\r\n
0x80045384 | The specified property definition doesn't apply to folders.\r\n
0x80045385 | The specified property definition type is not secure.\r\n
0x80045386 | The specified property definition type is not global.\r\n
0x80045387 | Unexpected failure from a WMI call.\r\n
0x80045388 | Cannot protect a file while running a file management task.\r\n
0x80045389 | The property definition sync task encountered errors.\r\nCheck the application event log for more information.\r\n
0x80045390 | The server does not provide access-denied assistance.\r\n
0x80045391 | Access-denied assistance cannot be provided for local paths.\r\n
0x80045392 | Access-denied assistance requires that the server be joined to a domain.\r\n
0x80045393 | File Server Resource Manager could not remove the read-only attribute from a file.\r\n
0x80045394 | A continuous file management job cannot have conditions based on the file's last accessed/modified or created times and cannot define any notifications.\r\n
0x80045395 | The object contains a schedule that was created by using an earlier version of File Server Resource Manager and that is incompatible with the current version of Windows Server. Edit the schedule on this computer to update it.\r\n
0x80045396 | This operation is not supported for paths on which Offline Files is enabled.\r\n
0x80045397 | Cannot write to the specified expiration directory. Confirm that the permissions of the expiration directory grant Write permission to the computer account of the server performing the file expiration task.\r\n
0x80045398 | The expiration path must be 150 characters or shorter.\r\n
0x80045399 | The expiration directory must be on a volume formatted with the NTFS file system.\r\n
0x8004539a | This file management job is deprecated. Please check the configuration of the file management job and verify that it is up-to-date.\r\n
0x8004539b | A module was restarted due to excessive processing time of a file. Check the application event log for more information.\r\n
