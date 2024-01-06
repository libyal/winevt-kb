## ntmsevt.dll

Path: %SystemRoot%\System32\NTMSEVT.DLL

### 5.0.2187.1

Message identifier | Message string
--- | ---
0x40040000 | /***********************************************************************/\r\n/** Library Manager Event Definitions...                              **/\r\n/***********************************************************************/\r\n
0x40040035 | The RSM Library Manager for %1 was started.\r\n
0x40040049 | Enabled library: %1.\r\n
0x4004004b | Enabled drive : %1 in library: %2.\r\n
0x40040053 | RSM is rebuilding its database file(s).\r\n
0x4004005a | RSM database is recovering the index file.\r\n
0x4004005b | RSM database is building the index file.\r\n
0x4004005c | RSM database is reconstructing the data file.\r\n
0x40040062 | RSM was stopped.\r\n
0x40040063 | RSM was started.\r\n
0x4004007a | RSM/NTMS extension successfully loaded.\r\n
0x40040081 | The RSM service is delaying its start for %1 seconds to assist with boot time\r\nperformance .  Modify the registry value "DelayStart" in the registry key \r\n"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\NTMS" to modify the \r\nstart delay.  This registry value denotes the number of milliseconds to wait \r\nbefore starting the service.\r\n
0x40040086 | Received a device interface ARRIVAL notification for device:%n\r\n\r\n%1\r\n
0x40040087 | Received a device interface REMOVAL notification for device:%n\r\n\r\n%1\r\n
0x40040090 | Received notification for a handle object.  This particular\r\nnotification was not relevant to RSM and was ignored.\r\n
0x40040091 | Received Handle Volume Lock notification for a volume RSM manages. \r\nThe volume was locked.\r\n
0x40040092 | Received Handle Volume Lock notification for a volume RSM does not manage. \r\nNo action was taken.\r\n
0x40040093 | Received Handle Volume Unlock notification for a volume RSM manages. \r\nAll handles were closed.\r\n
0x40040094 | Received Handle Volume Unlock notification for a volume RSM does not manage. \r\nNo action was taken.\r\n
0x40040095 | Received Handle Volume Change notification for a volume RSM manages. \r\nRSM has updated its information for this volume.\r\n
0x40040096 | Received Handle Volume Change notification for a volume RSM does not manage. \r\nNo action was taken.\r\n
0x400400a0 | Received Handle Query Remove notification.\r\n%nRSM approved the query remove request.\r\n
0x400400a2 | Received Handle Query Remove Failure notification.\r\n%nRSM successfully acknowledged the event.\r\n
0x400400a4 | Received Handle Query Remove Pending notification.\r\n%nRSM successfully acknowledged the event.\r\n
0x400400a6 | Received Handle Query Remove Complete notification.\r\n%nRSM successfully acknowledged the event.\r\n
0x80040013 | RSM mounted medium %1 in library %2 and there was an On-Medium Id mismatch.\r\n
0x8004003a | Unable to control the front panel.\r\n
0x80040044 | Unable to determine the number of drives in library %1 because the device is not ready.\r\n
0x80040045 | Can not update the drive configuration of drive %1 in library %2 because\r\nanother process has the drive open. Setting drive configuration from the\r\nDatabase.\r\n
0x8004004c | Reset the state on media %1.\r\n
0x8004004d | Reset the state on drive %1.\r\n
0x80040051 | The physical media %x has been disabled.\r\n
0x80040056 | RSM database has determined that the disk is full (file=%1).\r\n
0x80040058 | RSM database has entered read only mode due to write errors.\r\n
0x80040059 | RSM database has entered disabled mode to to i/o errors.\r\n
0x8004005d | Neither copy of the RSM database is consistent: Reconstructing using the main datafile.\r\n
0x8004005e | RSM database IMPORT failed.  The import files might not exist or there may not be enough disk space.\r\n
0x8004005f | This RSM database has been relocated from server %1.\r\n
0x80040060 | The RSM database has detected an internal inconsistency problem and has scheduled a rebuild (file=%1).\r\n
0x80040064 | RSM was called by the service controller with an unknown request.\r\n
0x8004006d | This RSM database has rejected an update using a stale record.\r\n
0x80040079 | Unable to manage the removable disk in drive %1. \r\nThere are system files (paging files, RSM database files, and/or system/windows directories)\r\non this disk which are needed for system operation. The drive will be disabled for RSM\r\noperations. This drive can be re-enabled via the Removable Storage Manager snap-in when there are no longer\r\nsystem files present. \r\n
0x8004007b | Write Scratch operation on Media %1 was cancelled.  Media was left\r\nin the UNPREPARED state and must prepared via the Removable Storage\r\nManager snap-in in order to be used by an application.\r\n
0x8004007c | Failed to set the "%1" database attribute on the partition for\r\nside %2 of physical media "%3" during the %4 operation.\r\n
0x8004007d | Failed to delete the "%1" database attribute from the partition for\r\nside %2 of physical media "%3" during the %4 operation.\r\n
0x8004007f | RSM mounted medium %1 in library %2 and verification of the On-Medium Id failed.\r\n
0x80040080 | The device number of a(n) %1 cannot be determined.  This device failed to configure.  \r\nThis event may be logged several times for the same device.\r\n
0x80040088 | Denied a removal notification for device:%n\r\n\r\n%1%n%nRSM is currently initializing or configuring new devices.\r\n
0x800400a1 | Received Handle Query Remove notification.\r\n%nRSM refused the request and prohibited this action.\r\n
0x800400a3 | Received Handle Query Remove Failure notification.\r\n%nRSM failed to acknowledged the event.\r\n
0x800400a5 | Received Handle Query Remove Pending notification.\r\n%nRSM failed to acknowledged the event.\r\n
0x800400a7 | Received Handle Query Remove Complete notification.\r\n%nRSM failed to acknowledged the event.\r\n
0x800400a9 | Drive "%1" in library "%2" needs cleaning.\r\n
0x800400aa | The drive "%1" in library "%2" still needs cleaning after the last cleaning.  Try a new cleaner next time.\r\n
0xc0040001 | Unable to auto-configure library unit %1.  The current setup of the library\r\nunit does not support automatic configuration.  You will either have to\r\nmodify the current setup of the library to adhere to automatic\r\nconfiguration guidelines (if possible) or manually configure the device.\r\n
0xc0040002 | Unable to configure library unit %1.  The manual configuration information\r\nprovided for this changer does not exist or conflicts with other devices\r\non the system.  This usually occurs when the same drive device is reported\r\nas belonging to more than one library unit or a drive is listed in the\r\nconfiguration that was not found on the system.\r\n
0xc0040003 | Library %1 failed to write a Free media label on media %2 because of an\r\ninternal database error.\r\n
0xc0040004 | Library %1 failed to write a Free media label on media %2 because the\r\nmedia is not located in this library.\r\n
0xc0040005 | Library %1 failed to write a Free media label on media %2 because it is\r\nread only media.\r\n
0xc0040006 | Library %1 failed to write a Free media label on media %2 because the\r\nmedia is not located in a slot or drive.\r\n
0xc0040007 | Library %1 failed to write a Free media label on media %2 because an\r\nerror occured trying to move the media to a drive.\r\n
0xc0040008 | Library %1 failed to write a Free media label on media %2 because\r\nthe media is write protected.\r\n
0xc0040009 | Library %1 failed to write a Free media label on media %2 because\r\nan I/O error occured while writing the label.\r\n
0xc004000a | Library %1 failed to write a Free media label on media %2 because\r\nRSM found a different piece of media in the library than was\r\nselected for the move to Free pool operation.\r\n
0xc004000b | Library %1 failed to write a Free media label on media %2 because\r\nRSM does not support writing Free media labels on this type of media.\r\n
0xc004000c | Library %1 failed to write a Free media label on media %2 because\r\nthis media is located in a disabled drive.  You must enable the\r\ndrive before moving this media to the Free pool.  If the media\r\nis in a standalone drive, eject the media (manually) and use a\r\ndifferent drive.\r\n
0xc004000d | Library %1 failed to write a Free media label on side 2 of media\r\n%2.  RSM attempted to flip the media to access the second side\r\nbut the media is in use by another process.  RSM must have a\r\nFree media label on both sides of the media.  Thus, this media is\r\nnot valid Free media.\r\n
0xc004000e | RSM cannot manage library %1. Another process is using the device.\r\n
0xc004000f | RSM cannot manage library %1. The database is corrupt.\r\n
0xc0040010 | RSM cannot manage library %1.  The library did not become ready in time.\r\n
0xc0040011 | RSM cannot manage library %1.  It encountered an unspecified error.\r\nThis can be caused by a number of problems including, but not limited\r\nto, database corruption, failure communicating with the library, or\r\ninsufficient system resources.\r\n
0xc0040012 | RSM cannot manage library %1.  The initial inventory of the library\r\nfailed.\r\n
0xc0040014 | Unable to acquire the computer name from the system.\r\n
0xc0040015 | Unable to access the required registry key: %1.\r\n
0xc0040016 | The library device: %1, is not ready.\r\n
0xc0040017 | Unable to determine if the drive: %1 needs to be cleaned.\r\n
0xc0040018 | The timeout period has expired for cleaning drive: %1.\r\n
0xc0040019 | Please remove the piece of media from the picker in library: %1.\r\n
0xc004001a | Please remove the piece of media from the ieport in library: %1.\r\n
0xc004001b | There is a drive missing in library: %1.\r\n
0xc004001c | Unable to obtain the state of the drive: %1 in library: %2.\r\n
0xc004001d | Unable to fetch database object: %1.\r\n
0xc004001e | Unable to open drive: %1 in library: %2.\r\n
0xc004001f | Unable to close drive: %1 in library: %2.\r\n
0xc0040020 | Unable to open library: %1.\r\n
0xc0040021 | Unable to close library: %1.\r\n
0xc0040022 | Unable to load media into drive: %1 in library: %2.\r\n
0xc0040023 | Unable to unload media from drive: %1 in library: %2.\r\n
0xc0040024 | Unable to lock drive: %1 in library: %2.\r\n
0xc0040025 | Unable to unlock drive: %1 in library: %2.\r\n
0xc0040026 | Unable to obtain operating characteristics from drive: %1 in library: %2.\r\n
0xc0040027 | The device: %1, is not ready.\r\n
0xc0040028 | Unable to obtain product data from drive: %1 in library: %2.\r\n
0xc0040029 | Unable to obtain extended operating characteristics from drive: %1 in library: %2.\r\n
0xc004002a | Unable to obtain extended characteristics from media in drive: %1.\r\n
0xc004002b | Unable to obtain statistics from %1.\r\n
0xc004002c | Unable to obtain security information for the %1.\r\n
0xc004002d | Unable to set security for the %1.\r\n
0xc004002e | The door to library %2 has been open or unlocked for more than %1 seconds. \r\nPlease close and lock the door to enable the library.\r\n
0xc004002f | Unable to extend/retract the import/export element.\r\n
0xc0040030 | Unable to take inventory for %1 in %2.\r\n
0xc0040031 | Unable to retrieve inventory information from: %1.\r\n
0xc0040032 | Unable to obtain operating characteristics from library: %1.\r\n
0xc0040033 | Unable to move medium from drive %1 to slot %2 in library: %3. Please manually\r\neject the media.\r\n
0xc0040034 | Unable to move medium from drive %1 in library: %3. Please manually\r\nremove the media.\r\n
0xc0040036 | The RSM Library Manager was started with invalid arguments (%1).\r\n
0xc0040037 | A SCSI configuration error has been detected for library.\r\n
0xc0040038 | Unable to obtain characteristics from media in drive: %1 in library %2.\r\n
0xc0040039 | Unable to obtain the status of the import/export element.\r\n
0xc004003b | Unable to obtain characteristics from drive: %1.\r\n
0xc004003c | Unable to attach to the Database, error = %1.\r\n
0xc004003d | Unable to move medium from slot %1 to drive %2 in library: %3. Please check that the\r\nmedia is in the slot and that the drive is accessable.\r\n
0xc004003e | Unable to move medium from IEPort %1 to slot %2 in library: %3. Please check that the media\r\nis in the IEPort and the slot is accessable.\r\n
0xc004003f | Unable to move medium from slot %1 to IEPort %2 in library: %3. Please check that the media\r\nis in the slot is accessable and the IEPort is retracted.\r\n
0xc0040040 | Unable to move medium from the picker %1 to slot %2 in library: %3. Please check\r\nthat the media is in the picker is accessable and the slot is accessable.\r\n
0xc0040041 | Unable to determine the SCSI configuration of the drives in library %1.\r\n
0xc0040042 | Unable to set the SCSI configuration of the drives in library %1.\r\n
0xc0040043 | Unable to configure the RSM to start the Library manager for library %1.\r\n
0xc0040046 | Unable to determine the configuration of drive %1 in library %2 from the\r\nDatabase. Please close the drive and restart the Removable Storage\r\nService.\r\n
0xc0040047 | Unable to obtain environmental data from drive : %1 in library: %2.\r\n
0xc0040048 | Disabled library: %1.\r\n
0xc004004a | Disabled drive : %1 in library: %2.\r\n
0xc004004e | The IE-Port in library %1 cannot be retracted.\r\n
0xc004004f | The IE-Port in library %1 cannot be EXTENDED.\r\n
0xc0040050 | Library %1 is full and cannot accept any more media.\r\n
0xc0040052 | Communication with the RSM database failed.\r\n
0xc0040054 | RSM database is not compatible with the Removable Storage Service binary.\r\n
0xc0040055 | RSM database is corrupt and cannot be rebuilt.\r\n
0xc0040057 | RSM database has received an i/o error from its storage device (file=%1)(code=%2).\r\n
0xc0040061 | RSM could not register with service control manager.\r\n
0xc0040065 | Unable to set COM security level.\r\n
0xc0040066 | Unable to register COM class objects.\r\n
0xc0040067 | Unable to load RSM extension.\r\n
0xc0040068 | New media named "%1" was detected in library %2 having at least one unrecognized side\r\nand at least one recognized side.  This media may be damaged.\r\n
0xc0040069 | The contents of at least one side of media "%1" have changed.  This media\r\nmay be damaged and has thus been disabled.  To ignore this error and\r\ncontinue to use the media anyway, re-enable it using the Removable Storage\r\nManager snap-in for the Microsoft Management Console (MMC).\r\n
0xc004006a | Multisided media %1 could not be identified in library %2.  RSM attempted\r\nto flip the media to identify the second side but could not because the\r\nmedia was in use by another process.  This media has been forced into the\r\nUnrecognized pool and left in the disabled state.  Perform a full inventory or\r\neject the media and re-insert it into the library to fix this situation.\r\n
0xc004006b | The transport (a.k.a. robot or picker) of library %1 contains a piece of\r\nmedia and is unable to place the media back to a slot.  The media must be\r\nremoved from the transport manually.  If the library has a door, perform\r\na door access and remove the media from the transport.  Otherwise, if the\r\nlibrary has no door, contact the library manufacturer's techinal support.\r\n
0xc004006c | When RSM attempted to eject the media in drive %1 of library %2, the drive\r\nreported that it contained no media.  Most likely, the drive rejected the\r\nmedia when RSM originally placed the media into it.  This situation is\r\nusually caused when incompatible media or a cleaner cartridge is placed in\r\na library with a door access or inject operation.\r\n
0xc004006e | Automatic configuration for library %1 failed to configure %2. \r\nThe driver for the device in this bay is not properly loaded.\r\n
0xc004006f | RSM could not load media in drive %1 of library %2.\r\n
0xc0040070 | RSM could not open a handle to %1 (drive %2 of library %3).\r\n
0xc0040071 | RSM detected an internal error.\r\n
0xc0040072 | RSM has run out of memory.\r\n
0xc0040073 | RSM cannot identify media because a fatal error occured while trying to\r\nload the Media Label Libraries.\r\n
0xc0040074 | RSM could not identify the media in drive %1 of library %2.  An error was\r\nencountered while attempting to read data from the media.\r\n
0xc0040075 | RSM could not close its handle to %1 (drive %2 of library %3).\r\n
0xc0040076 | RSM could not verify the media in drive %1 of library %2 because the partition\r\nID supplied was invalid.\r\n
0xc0040077 | RSM could not Verify the media in drive %1 of library %2\r\nbecause the on-media-identifier did not match what was expected.\r\n
0xc0040078 | RSM could not Verify the media in drive %1 of library %2 because the\r\non-media-identifier did not match what was expected.\r\n
0xc004007e | Failed to perform a software load of the media "%2" in a drive of library "%1".\r\n
0xc0040082 | The RSM service has stopped because it cannot load the DLL "%1".  \r\nInstall or replace this DLL and restart the service.\r\n
0xc0040083 | Cannot find the procedure "%1" in DLL %2.  Most likely, the version of\r\nthis DLL is incompatible with the RSM service.  \r\n
0xc0040084 | Cannot find the procedure "%1" in DLL %2.  Most likely, the version of\r\nthis DLL is incompatible with the RSM service.  \r\n
0xc0040085 | Refused request to hibernate/suspend.\r\n%nOne or more applications have active connections open to this service.\r\nClose all applications that are using this service (including the\r\n"Removable Storage Manager" MMC snap-in) before attempting to hibernate/suspend\r\nthe system.\r\n
0xc0040097 | Error encountered in Media Label Library "%1".  The registry values were not properly installed.\r\n
0xc0040098 | Error encountered when attempting to execute Media Label Library "%1". \r\nThe DLL could not be loaded.  Make sure the file exists and the path\r\nis correctly noted in the registry.\r\n
0xc00400a8 | RSM cannot manage library %1. Failed to communicate with device or obtain device setup information.\r\n

### 5.1.2600.0

Message identifier | Message string
--- | ---
0x40040000 | /***********************************************************************/\r\n/** Library Manager Event Definitions...                              **/\r\n/***********************************************************************/\r\n
0x40040035 | The RSM Library Manager for %1 was started.\r\n
0x40040049 | Enabled library: %1.\r\n
0x4004004b | Enabled drive : %1 in library: %2.\r\n
0x40040053 | RSM is rebuilding its database file(s).\r\n
0x4004005a | RSM database is recovering the index file.\r\n
0x4004005b | RSM database is building the index file.\r\n
0x4004005c | RSM database is reconstructing the data file.\r\n
0x40040062 | RSM was stopped.\r\n
0x40040063 | RSM was started.\r\n
0x4004007a | RSM/NTMS extension successfully loaded.\r\n
0x40040081 | The RSM service is delaying its start for %1 seconds to assist with boot time\r\nperformance .  Modify the registry value "DelayStart" in the registry key \r\n"HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\NTMS" to modify the \r\nstart delay.  This registry value denotes the number of milliseconds to wait \r\nbefore starting the service.\r\n
0x40040087 | Received a device interface ARRIVAL notification for device:%n\r\n\r\n%1\r\n
0x40040088 | Received a device interface REMOVAL notification for device:%n\r\n\r\n%1\r\n
0x40040090 | Received notification for a handle object.  This particular\r\nnotification was not relevant to RSM and was ignored.\r\n
0x40040091 | Received Handle Volume Lock notification for a volume RSM manages. \r\nThe volume was locked.\r\n
0x40040092 | Received Handle Volume Lock notification for a volume RSM does not manage. \r\nNo action was taken.\r\n
0x40040093 | Received Handle Volume Unlock notification for a volume RSM manages. \r\nAll handles were closed.\r\n
0x40040094 | Received Handle Volume Unlock notification for a volume RSM does not manage. \r\nNo action was taken.\r\n
0x40040095 | Received Handle Volume Change notification for a volume RSM manages. \r\nRSM has updated its information for this volume.\r\n
0x40040096 | Received Handle Volume Change notification for a volume RSM does not manage. \r\nNo action was taken.\r\n
0x400400a0 | Received Handle Query Remove notification.\r\n%nRSM approved the query remove request.\r\n
0x400400a2 | Received Handle Query Remove Failure notification.\r\n%nRSM successfully acknowledged the event.\r\n
0x400400a4 | Received Handle Query Remove Pending notification.\r\n%nRSM successfully acknowledged the event.\r\n
0x400400a6 | Received Handle Query Remove Complete notification.\r\n%nRSM successfully acknowledged the event.\r\n
0x80040013 | RSM mounted medium %1 in library %2 and there was an On-Medium Id mismatch.\r\n
0x8004003a | Unable to control the front panel.\r\n
0x80040044 | Unable to determine the number of drives in library %1 because the device is not ready.\r\n
0x80040045 | Can not update the drive configuration of drive %1 in library %2 because\r\nanother process has the drive open. Setting drive configuration from the\r\nDatabase.\r\n
0x8004004c | Reset the state on media %1.\r\n
0x8004004d | Reset the state on drive %1.\r\n
0x80040051 | The physical media %x has been disabled.\r\n
0x80040056 | RSM database has determined that the disk is full (file=%1).\r\n
0x80040058 | RSM database has entered read only mode due to write errors.\r\n
0x80040059 | RSM database has entered disabled mode to to i/o errors.\r\n
0x8004005d | Neither copy of the RSM database is consistent: Reconstructing using the main datafile.\r\n
0x8004005e | RSM database IMPORT failed.  The import files might not exist or there may not be enough disk space.\r\n
0x8004005f | This RSM database has been relocated from server %1.\r\n
0x80040060 | The RSM database has detected an internal inconsistency problem and has scheduled a rebuild (file=%1).\r\n
0x80040064 | RSM was called by the service controller with an unknown request.\r\n
0x8004006d | This RSM database has rejected an update using a stale record.\r\n
0x80040079 | Unable to manage the removable disk in drive %1. \r\nThere are system files (paging files, RSM database files, and/or system/windows directories)\r\non this disk which are needed for system operation. The drive will be disabled for RSM\r\noperations. This drive can be re-enabled via the Removable Storage Manager snap-in when there are no longer\r\nsystem files present. \r\n
0x8004007b | Write Scratch operation on Media %1 was cancelled.  Media was left\r\nin the UNPREPARED state and must prepared via the Removable Storage\r\nManager snap-in in order to be used by an application.\r\n
0x8004007c | Failed to set the "%1" database attribute on the partition for\r\nside %2 of physical media "%3" during the %4 operation.\r\n
0x8004007d | Failed to delete the "%1" database attribute from the partition for\r\nside %2 of physical media "%3" during the %4 operation.\r\n
0x8004007f | RSM mounted medium %1 in library %2 and verification of the On-Medium Id failed.\r\n
0x80040080 | The device number of a(n) %1 cannot be determined.  This device failed to configure.  \r\nThis event may be logged several times for the same device.\r\n
0x80040085 | %1%n%nThis drive is located on %2.\r\n
0x80040089 | Denied a removal notification for device:%n\r\n\r\n%1%n%nRSM is currently initializing or configuring new devices.\r\n
0x800400a1 | Received Handle Query Remove notification.\r\n%nRSM refused the request and prohibited this action.\r\n
0x800400a3 | Received Handle Query Remove Failure notification.\r\n%nRSM failed to acknowledged the event.\r\n
0x800400a5 | Received Handle Query Remove Pending notification.\r\n%nRSM failed to acknowledged the event.\r\n
0x800400a7 | Received Handle Query Remove Complete notification.\r\n%nRSM failed to acknowledged the event.\r\n
0x800400a9 | Drive "%1" in library "%2" needs cleaning.\r\n
0x800400aa | The drive "%1" in library "%2" still needs cleaning after the last cleaning.  Try a new cleaner next time.\r\n
0xc0040001 | Unable to auto-configure library unit %1.  The current setup of the library\r\nunit does not support automatic configuration.  You will either have to\r\nmodify the current setup of the library to adhere to automatic\r\nconfiguration guidelines (if possible) or manually configure the device.\r\n
0xc0040002 | Unable to configure library unit %1.  The manual configuration information\r\nprovided for this changer does not exist or conflicts with other devices\r\non the system.  This usually occurs when the same drive device is reported\r\nas belonging to more than one library unit or a drive is listed in the\r\nconfiguration that was not found on the system.\r\n
0xc0040003 | Library %1 failed to write a Free media label on media %2 because of an\r\ninternal database error.\r\n
0xc0040004 | Library %1 failed to write a Free media label on media %2 because the\r\nmedia is not located in this library.\r\n
0xc0040005 | Library %1 failed to write a Free media label on media %2 because it is\r\nread only media.\r\n
0xc0040006 | Library %1 failed to write a Free media label on media %2 because the\r\nmedia is not located in a slot or drive.\r\n
0xc0040007 | Library %1 failed to write a Free media label on media %2 because an\r\nerror occured trying to move the media to a drive.\r\n
0xc0040008 | Library %1 failed to write a Free media label on media %2 because\r\nthe media is write protected.\r\n
0xc0040009 | Library %1 failed to write a Free media label on media %2 because\r\nan I/O error occured while writing the label.\r\n
0xc004000a | Library %1 failed to write a Free media label on media %2 because\r\nRSM found a different piece of media in the library than was\r\nselected for the move to Free pool operation.\r\n
0xc004000b | Library %1 failed to write a Free media label on media %2 because\r\nRSM does not support writing Free media labels on this type of media.\r\n
0xc004000c | Library %1 failed to write a Free media label on media %2 because\r\nthis media is located in a disabled drive.  You must enable the\r\ndrive before moving this media to the Free pool.  If the media\r\nis in a standalone drive, eject the media (manually) and use a\r\ndifferent drive.\r\n
0xc004000d | Library %1 failed to write a Free media label on side 2 of media\r\n%2.  RSM attempted to flip the media to access the second side\r\nbut the media is in use by another process.  RSM must have a\r\nFree media label on both sides of the media.  Thus, this media is\r\nnot valid Free media.\r\n
0xc004000e | RSM cannot manage library %1. Another process is using the device.\r\n
0xc004000f | RSM cannot manage library %1. The database is corrupt.\r\n
0xc0040010 | RSM cannot manage library %1.  The library did not become ready in time.\r\n
0xc0040011 | RSM cannot manage library %1.  It encountered an unspecified error.\r\nThis can be caused by a number of problems including, but not limited\r\nto, database corruption, failure communicating with the library, or\r\ninsufficient system resources.\r\n
0xc0040012 | RSM cannot manage library %1.  The initial inventory of the library\r\nfailed.\r\n
0xc0040014 | Unable to acquire the computer name from the system.\r\n
0xc0040015 | Unable to access the required registry key: %1.\r\n
0xc0040016 | The library device: %1, is not ready.\r\n
0xc0040017 | Unable to determine if the drive: %1 needs to be cleaned.\r\n
0xc0040018 | The timeout period has expired for cleaning drive: %1.\r\n
0xc0040019 | Please remove the piece of media from the picker in library: %1.\r\n
0xc004001a | Please remove the piece of media from the ieport in library: %1.\r\n
0xc004001b | There is a drive missing in library: %1.\r\n
0xc004001c | Unable to obtain the state of the drive: %1 in library: %2.\r\n
0xc004001d | Unable to fetch database object: %1.\r\n
0xc004001e | Unable to open drive: %1 in library: %2.\r\n
0xc004001f | Unable to close drive: %1 in library: %2.\r\n
0xc0040020 | Unable to open library: %1.\r\n
0xc0040021 | Unable to close library: %1.\r\n
0xc0040022 | Unable to load media into drive: %1 in library: %2.\r\n
0xc0040023 | Unable to unload media from drive: %1 in library: %2.\r\n
0xc0040024 | Unable to lock drive: %1 in library: %2.\r\n
0xc0040025 | Unable to unlock drive: %1 in library: %2.\r\n
0xc0040026 | Unable to obtain operating characteristics from drive: %1 in library: %2.\r\n
0xc0040027 | The device: %1, is not ready.\r\n
0xc0040028 | Unable to obtain product data from drive: %1 in library: %2.\r\n
0xc0040029 | Unable to obtain extended operating characteristics from drive: %1 in library: %2.\r\n
0xc004002a | Unable to obtain extended characteristics from media in drive: %1.\r\n
0xc004002b | Unable to obtain statistics from %1.\r\n
0xc004002c | Unable to obtain security information for the %1.\r\n
0xc004002d | Unable to set security for the %1.\r\n
0xc004002e | The door to library %2 has been open or unlocked for more than %1 seconds. \r\nPlease close and lock the door to enable the library.\r\n
0xc004002f | Unable to extend/retract the import/export element.\r\n
0xc0040030 | Unable to take inventory for %1 in %2.\r\n
0xc0040031 | Unable to retrieve inventory information from: %1.\r\n
0xc0040032 | Unable to obtain operating characteristics from library: %1.\r\n
0xc0040033 | Unable to move medium from drive %1 to slot %2 in library: %3. Please manually\r\neject the media.\r\n
0xc0040034 | Unable to move medium from drive %1 in library: %3. Please manually\r\nremove the media.\r\n
0xc0040036 | The RSM Library Manager was started with invalid arguments (%1).\r\n
0xc0040037 | A SCSI configuration error has been detected for library.\r\n
0xc0040038 | Unable to obtain characteristics from media in drive: %1 in library %2.\r\n
0xc0040039 | Unable to obtain the status of the import/export element.\r\n
0xc004003b | Unable to obtain characteristics from drive: %1.\r\n
0xc004003c | Unable to attach to the Database, error = %1.\r\n
0xc004003d | Unable to move medium from slot %1 to drive %2 in library: %3. Please check that the\r\nmedia is in the slot and that the drive is accessable.\r\n
0xc004003e | Unable to move medium from IEPort %1 to slot %2 in library: %3. Please check that the media\r\nis in the IEPort and the slot is accessable.\r\n
0xc004003f | Unable to move medium from slot %1 to IEPort %2 in library: %3. Please check that the media\r\nis in the slot is accessable and the IEPort is retracted.\r\n
0xc0040040 | Unable to move medium from the picker %1 to slot %2 in library: %3. Please check\r\nthat the media is in the picker is accessable and the slot is accessable.\r\n
0xc0040041 | Unable to determine the SCSI configuration of the drives in library %1.\r\n
0xc0040042 | Unable to set the SCSI configuration of the drives in library %1.\r\n
0xc0040043 | Unable to configure the RSM to start the Library manager for library %1.\r\n
0xc0040046 | Unable to determine the configuration of drive %1 in library %2 from the\r\nDatabase. Please close the drive and restart the Removable Storage\r\nService.\r\n
0xc0040047 | Unable to obtain environmental data from drive : %1 in library: %2.\r\n
0xc0040048 | Disabled library: %1.\r\n
0xc004004a | Disabled drive : %1 in library: %2.\r\n
0xc004004e | The IE-Port in library %1 cannot be retracted.\r\n
0xc004004f | The IE-Port in library %1 cannot be EXTENDED.\r\n
0xc0040050 | Library %1 is full and cannot accept any more media.\r\n
0xc0040052 | Communication with the RSM database failed.\r\n
0xc0040054 | RSM database is not compatible with the Removable Storage Service binary.\r\n
0xc0040055 | RSM database is corrupt and cannot be rebuilt.\r\n
0xc0040057 | RSM database has received an i/o error from its storage device (file=%1)(code=%2).\r\n
0xc0040061 | RSM could not register with service control manager.\r\n
0xc0040065 | Unable to set COM security level.\r\n
0xc0040066 | Unable to register the RSM service COM class objects. The error code is %n.  \r\n
0xc0040067 | Unable to load RSM extension.\r\n
0xc0040068 | New media named "%1" was detected in library %2 having at least one unrecognized side\r\nand at least one recognized side.  This media may be damaged.\r\n
0xc0040069 | The contents of at least one side of media "%1" have changed.  This media\r\nmay be damaged and has thus been disabled.  To ignore this error and\r\ncontinue to use the media anyway, re-enable it using the Removable Storage\r\nManager snap-in for the Microsoft Management Console (MMC).\r\n
0xc004006a | Multisided media %1 could not be identified in library %2.  RSM attempted\r\nto flip the media to identify the second side but could not because the\r\nmedia was in use by another process.  This media has been forced into the\r\nUnrecognized pool and left in the disabled state.  Perform a full inventory or\r\neject the media and re-insert it into the library to fix this situation.\r\n
0xc004006b | The transport (a.k.a. robot or picker) of library %1 contains a piece of\r\nmedia and is unable to place the media back to a slot.  The media must be\r\nremoved from the transport manually.  If the library has a door, perform\r\na door access and remove the media from the transport.  Otherwise, if the\r\nlibrary has no door, contact the library manufacturer's techinal support.\r\n
0xc004006c | When RSM attempted to eject the media in drive %1 of library %2, the drive\r\nreported that it contained no media.  Most likely, the drive rejected the\r\nmedia when RSM originally placed the media into it.  This situation is\r\nusually caused when incompatible media or a cleaner cartridge is placed in\r\na library with a door access or inject operation.\r\n
0xc004006e | Automatic configuration for library %1 failed to configure %2. \r\nThe driver for the device in this bay is not properly loaded.\r\n
0xc004006f | RSM could not load media in drive %1 of library %2.\r\n
0xc0040070 | RSM could not open a handle to %1 (drive %2 of library %3).\r\n
0xc0040071 | RSM detected an internal error.\r\n
0xc0040072 | RSM has run out of memory.\r\n
0xc0040073 | RSM cannot identify media because a fatal error occured while trying to\r\nload the Media Label Libraries.\r\n
0xc0040074 | RSM could not identify the media in drive %1 of library %2.  An error was\r\nencountered while attempting to read data from the media.\r\n
0xc0040075 | RSM could not close its handle to %1 (drive %2 of library %3).\r\n
0xc0040076 | RSM could not verify the media in drive %1 of library %2 because the partition\r\nID supplied was invalid.\r\n
0xc0040077 | RSM could not Verify the media in drive %1 of library %2\r\nbecause the on-media-identifier did not match what was expected.\r\n
0xc0040078 | RSM could not Verify the media in drive %1 of library %2 because the\r\non-media-identifier did not match what was expected.\r\n
0xc004007e | Failed to perform a software load of the media "%2" in a drive of library "%1".\r\n
0xc0040082 | The RSM service has stopped because it cannot load the DLL "%1".  \r\nInstall or replace this DLL and restart the service.\r\n
0xc0040083 | Cannot find the procedure "%1" in DLL %2.  Most likely, the version of\r\nthis DLL is incompatible with the RSM service.  \r\n
0xc0040084 | Cannot find the procedure "%1" in DLL %2.  Most likely, the version of\r\nthis DLL is incompatible with the RSM service.  \r\n
0xc0040086 | %1%n%nThis drive is located on %2.\r\n
0xc0040097 | Error encountered in Media Label Library "%1".  The registry values were not properly installed.\r\n
0xc0040098 | Error encountered when attempting to execute Media Label Library "%1". \r\nThe DLL could not be loaded.  Make sure the file exists and the path\r\nis correctly noted in the registry.\r\n
0xc00400a8 | RSM cannot manage library %1. Failed to communicate with device or obtain device setup information.\r\n
