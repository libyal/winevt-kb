## vssvc.exe

Path: %SystemRoot%\System32\VSSVC.EXE

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x00000001 | Volume Shadow Copy Service initialization error: the control dispatcher cannot be started [%1].\r\n
0x00000002 | Volume Shadow Copy Service initialization error: the control handler cannot be registered [%1].\r\n
0x00000003 | Volume Shadow Copy Service initialization error: the COM library cannot be initialized [%1].\r\n
0x00000004 | Volume Shadow Copy Service initialization error: the COM security cannot be initialized [%1].\r\n
0x00000005 | Volume Shadow Copy Service initialization error: the COM classes cannot be registered [%1].\r\n
0x00000006 | Volume Shadow Copy Service initialization error: [%1].\r\n
0x00000007 | Unexpected error when changing the SCM status of the Volume Shadow Copy Service: [%1, %2].\r\n
0x00000008 | Volume Shadow Copy Service information: Service starting at request of process '%1'. [%2]\r\n
0x00000fa1 | Volume Shadow Copy Service error: Cannot find diff areas for creating shadow copies.\r\nPlease add at least one NTFS drive to the system with enough free space.\r\nThe free space needed is at least 100 Mb for each volume to be backed up/shadowed.\r\n
0x00000fa2 | Volume Shadow Copy Service error: Cannot create multiple shadow copies on the same volume (%1)\r\n
0x00001001 | Volume Shadow Copy Service error: The COM+ Admin catalog instance cannot be created [%1].\r\n
0x00001002 | Volume Shadow Copy Service error: Cannot install the event class %1 into the COM+ application '%2' [%3].\r\n
0x00001003 | Volume Shadow Copy Service error: Cannot install the component %1 into the COM+ application '%2' [%3].\r\n
0x00001004 | Volume Shadow Copy Service error: Cannot create service '%1' for the COM+ application '%2' [%3].\r\n
0x00001005 | Volume Shadow Copy Service error: Cannot obtain the collection '%1' from the COM+ catalog [%2].\r\n
0x00001006 | Volume Shadow Copy Service error: Cannot populate the COM+ collection '%1' [%2].\r\n
0x00001007 | Volume Shadow Copy Service error: Cannot get the COM+ collection key [%1].\r\n
0x00001008 | Volume Shadow Copy Service error: Cannot get the COM+ collection '%1' from parent [%2].\r\n
0x00001009 | Volume Shadow Copy Service error: Cannot save the changes for the COM+ collection [%1].\r\n
0x0000100a | Volume Shadow Copy Service error: Cannot create a subscription (%1,%2,%3) [%4].\r\n
0x0000100b | Volume Shadow Copy Service error: Cannot attach to the subscription with name (%1) [%2].\r\n
0x0000100c | Volume Shadow Copy Service error: Cannot remove the subscription with index %1 [%2].\r\n
0x0000100d | Volume Shadow Copy Service error: Cannot insert the new object into the COM+ catalog  [%1].\r\n
0x0000100e | Volume Shadow Copy Service error: Cannot attach the catalog object to the COM+ application [%1].\r\n
0x0000100f | Volume Shadow Copy Service error: Cannot attach to the subscription with name (%1) [%2].\r\n
0x00001010 | Volume Shadow Copy Service error: Error getting current directory [%2].\r\n
0x00001011 | Volume Shadow Copy Service error: Error Removing COM+ application (%1) [%2].\r\n
0x00001389 | Volume Shadow Copy Service error: The system shadow copy writers are already initialised.\r\n
0x0000138a | Volume Shadow Copy Service error: Insufficient memory to allocate writer instance for the %1 writer.\r\n
0x0000138b | Volume Shadow Copy Service error: Unable to start worker thread for the %1 writer due to pre-existing handles for the thread, the mutex or the events.\r\n
0x0000138c | Volume Shadow Copy Service error: Unable to construct the mutex security attributes for the mutex %3 in the %4 writer due to status %1 (converted to %2).\r\n
0x0000138d | Volume Shadow Copy Service error: Unable to create mutex %3 for the %4 writer due to status %1 (converted to %2).\r\n
0x0000138e | Volume Shadow Copy Service error: Unable to create worker thread operation request event for the %3 writer due to status %1 (converted to %2).\r\n
0x0000138f | Volume Shadow Copy Service error: Unable to create worker thread operation completion event for the %3 writer due to status %1 (converted to %2).\r\n
0x00001390 | Volume Shadow Copy Service error: Unable to create worker thread for the %3 writer due to status %1 (converted to %2).\r\n
0x00001391 | Volume Shadow Copy Service error: Illegal initialization type (%1) requested.\r\n
0x00001392 | Volume Shadow Copy Service error: Shadow Copy shim failed with status %1 (converted to %2).\r\n
0x00001393 | Volume Shadow Copy Service error: Shadow Copy writer %3 failed with status %1 (converted to %2).\r\n
0x00001394 | Volume Shadow Copy Service error: Shadow Copy shim called routine %3 which failed with status %1 (converted to %2).\r\n
0x00001395 | Volume Shadow Copy Service error: Shadow Copy writer %3 called routine %4 which failed with status %1 (converted to %2).\r\n
0x00001396 | Volume Shadow Copy Service error: Unable to request operation %2 as no worker thread for writer %1.\r\n
0x00001397 | Volume Shadow Copy Service error: Unable to change from state %1 to state %2 in writer %3 (Status %4).\r\n
0x00001398 | Volume Shadow Copy Service error: Unable to process requested operation %4 in writer %3 due to status %1 (Converted to %2).\r\n
0x00001771 | Sqllib error: Cannot create an event due to error %1.\r\n
0x00001772 | Sqllib error: Database %1 is not in sysdatabases.\r\n
0x00001773 | Sqllib error: sysaltfiles is empty.\r\n
0x00001774 | Sqllib error: Database %1 is not simple.\r\n
0x00001775 | Sqllib error: Database %1 is stored on multiple volumes, only some of\r\nwhich are being shadowed.\r\n
0x00001776 | Sqllib error: Error thawing server %1.\r\n
0x00001777 | Sqllib error: sysdatabases is empty.\r\n
0x00001778 | Sqllib error: Failed to create VDS object. hr = %1.\r\n
0x00001779 | Sqllib error: Unsupported MDAC stack major version=%1 minor version=%2\r\n
0x0000177a | Sqllib error: Unsupported Sql Server version %1.\r\n
0x0000177b | Sqllib error: ODBC SQLAllocHandle failed.\r\n
0x0000177c | Sqllib error: ODBC Error encountered calling %1.\r\n%2\r\n
0x0000177d | Sqllib error: OLEDB Error encountered calling %1. hr = %2.\r\n%3\r\n
0x0000177e | Sqllib error: Final GetCommand from IClientVirtualDevice did not return VD_E_CLOSE.\r\nIt returned hr = %1 instead.\r\n
0x00002001 | Volume Shadow Copy Service error: Unexpected error calling routine %1.  hr = %2.\r\n
0x00002002 | Volume Shadow Copy Service error: Unexpected error querying for the IVssWriterCallback interface.  hr = %1.\r\n
0x00002003 | Volume Shadow Copy Service error: Internally transferred WRITER_COMPONENTS document is invalid.\r\n
0x00002004 | Volume Shadow Copy Service error: No volumes in the shadow copy set.\r\n
0x00002005 | Volume Shadow Copy Service error: ERROR_INSUFFICIENT_BUFFER expected error.  Actual Error was [%1].\r\n
0x00002006 | Volume Shadow Copy Service error: Unexpected error. Final buffer for call to GetTokenInformation was size = %1, original size was %2.\r\n
0x00002007 | Volume Shadow Copy Service error: Unexpected error performing QueryInterface from IXMLDOMNode to IXMLDOMElement.  hr = %1.\r\n
0x00002008 | Volume Shadow Copy Service error: An unexpected error was encountered examining the XML document.  The document is missing the %1 element.\r\n
0x00002009 | Volume Shadow Copy Service error: An unexpected error was encountered examining the XML document.  The document is missing the %1 attribute.\r\n
0x0000200a | Volume Shadow Copy Service error: An unexpected error was encountered when QueryInterface for IDispatch was called.  hr = %1 attribute.\r\n
0x0000200b | Volume Shadow Copy Service error: An unexpected error was encountered cloning a document.  The cloned document has no children.\r\n
0x0000200c | Volume Shadow Copy Service error: An invalid XML document was returned from writer %1.\r\n
0x0000200d | Volume Shadow Copy Service error: An error occured calling QueryInterface from IVssCoordinator to IVssShim.  hr = %1.\r\n
0x0000200e | Volume Shadow Copy Service error: There are two writers with the identical instance id %1.\r\n
0x0000200f | Volume Shadow Copy Service error: An unexpected error was encountered when calling QueryInterface for IVssAsync.  hr = %1.\r\n
0x00002010 | Volume Shadow Copy Service error: The backup components document is NULL.\r\n
0x00002011 | Volume Shadow Copy Service error: The thread handle for the asynchronous thread is NULL.\r\n
0x00002012 | Volume Shadow Copy Service error: Unexpected error %1 was returned from WaitForSingleObject.\r\n
0x00003001 | Volume Shadow Copy Service error: Unexpected error %1.  hr = %2.\r\n
0x00003002 | Volume Shadow Copy Service warning: %1.  hr = %2.\r\n
0x00003003 | Volume Shadow Copy Service error: Error on creating/using the COM+ Writers publisher interface: %1 [%2].\r\n
0x00003004 | Volume Shadow Copy Service error: Error creating the Shadow Copy Provider COM class with CLSID %1 [%2].\r\n
0x00003005 | Volume Shadow Copy Service error: Error calling a routine on the Shadow Copy Provider %1. Routine details %2 [hr = %3].\r\n
0x00003006 | Volume Shadow Copy Service error: Error calling a routine on the Shadow Copy Provider %1. Routine returned E_INVALIDARG.\r\nRoutine details %2.\r\n
0x00003007 | Volume Shadow Copy Service error: Wrong type %1 (should be %2) for the\r\nRegistry value %3 under the key %4.\r\n
0x00003008 | Volume Shadow Copy Service error: The system may be low on resources.\r\nUnexpected error at background thread creation\r\n(_beginthreadex returns %1, errno = %2).\r\n
0x00003009 | Volume Shadow Copy Service error: The I/O writes cannot be flushed during the shadow copy creation period on volume %1.\r\nThe volume index in the shadow copy set is %2. Error details: Flush[%3], Release[%4], OnRun[%5].\r\n
0x0000300a | Volume Shadow Copy Service error: The I/O writes cannot be held during the shadow copy creation period on volume %1.\r\nThe volume index in the shadow copy set is %2. Error details: Flush[%3], Release[%4], OnRun[%5].\r\n
0x0000300b | Volume Shadow Copy Service error: One of the shadow copy providers returned an invalid number of committed shadow copies.\r\nThe expected number of committed shadow copy is %1. The detected number of committed shadow copies is %2.\r\n
0x0000300c | Volume Shadow Copy Service error: Writer %1 called CVssWriter::Initialize during Setup.\r\n
0x0000300d | Volume Shadow Copy Service error: Writer %1 did not respond to a GatherWriterStatus call.\r\n
0x0000300e | Volume Shadow Copy Service error: An internal inconsistency was detected in trying\r\nto contact shadow copy service writers.  Please check to see that the Event Service\r\nand Volume Shadow Copy Service are operating properly.\r\n
0x0000300f | An error occurred calling CoSetProxyBlanket.  hr = %1\r\n
0x00003010 | An error occurred trying to QI the IVssWriter event object for\r\nIMultiInterfaceEventControl.  hr = %1\r\n
0x00003011 | Volume Shadow Copy Service error: Volume/disk not connected or not found.\r\nError context: %1.\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00000001 | Volume Shadow Copy Service initialization error: the control dispatcher cannot be started [%1].\r\n
0x00000002 | Volume Shadow Copy Service initialization error: the control handler cannot be registered [%1].\r\n
0x00000003 | Volume Shadow Copy Service initialization error: the COM library cannot be initialized [%1].\r\n
0x00000004 | Volume Shadow Copy Service initialization error: the COM security cannot be initialized [%1].\r\n
0x00000005 | Volume Shadow Copy Service initialization error: the COM classes cannot be registered [%1].\r\n
0x00000006 | Volume Shadow Copy Service initialization error: [%1].\r\n
0x00000007 | Unexpected error when changing the SCM status of the Volume Shadow Copy Service: [%1, %2].\r\n
0x00000008 | Volume Shadow Copy Service information: Service starting at request of process '%1'. [%2]\r\n
0x00000009 | Volume Shadow Copy Service information: Volume '%1' appears as disconnected and it is\r\nignored by the service. You may want to rescan disks. [%2]\r\n
0x0000000a | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started.\r\nMost likely the CPU is under heavy load. [%3]\r\n
0x0000000b | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started. [%3]\r\n
0x0000000c | Volume Shadow Copy Service information: A database of hardware snapshots was created.\r\n
0x0000000d | The user name %1 specified in registry (%2) does not map to a real user name. The entry is ignored.\r\n
0x0000000e | The value with name %1 specified in registry (%2) is not of type REG_DWORD. The entry is ignored.\r\n
0x0000000f | The value with name %1 specified in registry (%2) must be either '0' or '1'. \r\nThe current value (%3) cannot be interpreted. The entry is ignored.\r\n
0x00000010 | Volume Shadow Copy Service error: The COM Server with CLSID %1 and name %2 cannot be started during Safe Mode. \r\nThe Volume Shadow Copy service cannot start while in safe mode. [%3]\r\n
0x00000011 | Volume Shadow Copy Service error: The EventSystem service is disabled or is attempting to start during Safe Mode. \r\nThe Volume Shadow Copy service cannot start while in safe mode.\r\nIf not in safe mode, make sure that EventSystem service is enabled.\r\nCLSID:%1 Name:%2 [%3]\r\n
0x00000012 | Volume Shadow Copy Service error: The Volume Shadow Copy infrastructure cannot be used during Safe Mode.\r\n
0x00000013 | Volume Shadow Copy Service error: Writers will not receive events since the COM+ database is corrupted. \r\nThis might happened if an error occurred during Windows setup. \r\nThe error returned from CoCreateInstance on class with CLSID %1 and Name %2 is [%3]\r\n
0x00000014 | Volume Shadow Copy Service error: A critical component required by the Volume Shadow Copy service is not registered. \r\nThis might happened if an error occurred during Windows setup or during installation of a Shadow Copy provider. \r\nThe error returned from CoCreateInstance on class with CLSID %1 and Name %2 is [%3].\r\n
0x00000fa1 | Volume Shadow Copy Service error: Cannot find diff areas for creating shadow copies.\r\nPlease add at least one NTFS drive to the system with enough free space.\r\nThe free space needed is at least 100 Mb for each volume to be shadow copied.\r\n
0x00000fa2 | Volume Shadow Copy Service error: Cannot create multiple shadow copies on the same volume (%1)\r\n
0x00001001 | Volume Shadow Copy Service error: The COM+ Admin catalog instance cannot be created [%1].\r\n
0x00001002 | Volume Shadow Copy Service error: Cannot install the event class %1 into the COM+ application '%2' [%3].\r\n
0x00001003 | Volume Shadow Copy Service error: Cannot install the component %1 into the COM+ application '%2' [%3].\r\n
0x00001004 | Volume Shadow Copy Service error: Cannot create service '%1' for the COM+ application '%2' [%3].\r\n
0x00001005 | Volume Shadow Copy Service error: Cannot obtain the collection '%1' from the COM+ catalog [%2].\r\n
0x00001006 | Volume Shadow Copy Service error: Cannot populate the COM+ collection '%1' [%2].\r\n
0x00001007 | Volume Shadow Copy Service error: Cannot get the COM+ collection key [%1].\r\n
0x00001008 | Volume Shadow Copy Service error: Cannot get the COM+ collection '%1' from parent [%2].\r\n
0x00001009 | Volume Shadow Copy Service error: Cannot save the changes for the COM+ collection [%1].\r\n
0x0000100a | Volume Shadow Copy Service error: Cannot create a subscription (%1,%2,%3) [%4].\r\n
0x0000100b | Volume Shadow Copy Service error: Cannot attach to the subscription with name (%1) [%2].\r\n
0x0000100c | Volume Shadow Copy Service error: Cannot remove the subscription with index %1 [%2].\r\n
0x0000100d | Volume Shadow Copy Service error: Cannot insert the new object into the COM+ catalog  [%1].\r\n
0x0000100e | Volume Shadow Copy Service error: Cannot attach the catalog object to the COM+ application [%1].\r\n
0x0000100f | Volume Shadow Copy Service error: Cannot attach to the subscription with name (%1) [%2].\r\n
0x00001010 | Volume Shadow Copy Service error: Error getting current directory [%2].\r\n
0x00001011 | Volume Shadow Copy Service error: Error Removing COM+ application (%1) [%2].\r\n
0x00001389 | Volume Shadow Copy Service error: The system shadow copy writers are already initialized.\r\n
0x0000138a | Volume Shadow Copy Service error: Insufficient memory to allocate writer instance for the %1 writer.\r\n
0x0000138b | Volume Shadow Copy Service error: Unable to start worker thread for the %1 writer due to pre-existing handles for the thread, the mutex or the events.\r\n
0x0000138c | Volume Shadow Copy Service error: Unable to construct the mutex security attributes for the mutex %3 in the %4 writer due to status %1 (converted to %2).\r\n
0x0000138d | Volume Shadow Copy Service error: Unable to create mutex %3 for the %4 writer due to status %1 (converted to %2).\r\n
0x0000138e | Volume Shadow Copy Service error: Unable to create worker thread operation request event for the %3 writer due to status %1 (converted to %2).\r\n
0x0000138f | Volume Shadow Copy Service error: Unable to create worker thread operation completion event for the %3 writer due to status %1 (converted to %2).\r\n
0x00001390 | Volume Shadow Copy Service error: Unable to create worker thread for the %3 writer due to status %1 (converted to %2).\r\n
0x00001391 | Volume Shadow Copy Service error: Illegal initialisation type (%1) requested.\r\n
0x00001392 | Volume Shadow Copy Service error: Shadow Copy shim failed with status %1 (converted to %2).\r\n
0x00001393 | Volume Shadow Copy Service error: Shadow Copy writer %3 failed with status %1 (converted to %2).\r\n
0x00001394 | Volume Shadow Copy Service error: Shadow Copy shim called routine %3 which failed with status %1 (converted to %2).\r\n
0x00001395 | Volume Shadow Copy Service error: Shadow Copy writer %3 called routine %4 which failed with status %1 (converted to %2).\r\n
0x00001396 | Volume Shadow Copy Service error: Unable to request operation %2 as no worker thread for writer %1.\r\n
0x00001397 | Volume Shadow Copy Service error: Unable to change from state %1 to state %2 in writer %3 (Status %4).\r\n
0x00001398 | Volume Shadow Copy Service error: Unable to process requested operation %4 in writer %3 due to status %1 (Converted to %2).\r\n
0x00001771 | Sqllib error: Cannot create an event due to error %1.\r\n
0x00001772 | Sqllib error: Database %1 is not in sysdatabases.\r\n
0x00001773 | Sqllib error: sysaltfiles is empty.\r\n
0x00001774 | Sqllib error: Database %1 is not simple.\r\n
0x00001775 | Sqllib error: Database %1 is stored on multiple volumes, only some of\r\nwhich are being shadowed.\r\n
0x00001776 | Sqllib error: Error thawing server %1.\r\n
0x00001777 | Sqllib error: sysdatabases is empty.\r\n
0x00001778 | Sqllib error: Failed to create VDS object. hr = %1.\r\n
0x00001779 | Sqllib error: Unsupported MDAC stack major version=%1 minor version=%2\r\n
0x0000177a | Sqllib error: Unsupported Sql Server version %1.\r\n
0x0000177b | Sqllib error: ODBC SQLAllocHandle failed.\r\n
0x0000177c | Sqllib error: ODBC Error encountered calling %1.\r\n%2\r\n
0x0000177d | Sqllib error: OLEDB Error encountered calling %1. hr = %2.\r\n%3\r\n
0x0000177e | Sqllib error: Final GetCommand from IClientVirtualDevice did not return VD_E_CLOSE.\r\nIt returned hr = %1 instead.\r\n
0x00001b59 | VssAdmin: %1: %2%nCommand-line: '%3'.\r\n
0x00002001 | Volume Shadow Copy Service error: Unexpected error calling routine %1.  hr = %2.\r\n
0x00002002 | Volume Shadow Copy Service error: Unexpected error querying for the IVssWriterCallback interface.  hr = %1.\r\n
0x00002003 | Volume Shadow Copy Service error: Internally transferred WRITER_COMPONENTS document is invalid.\r\n
0x00002004 | Volume Shadow Copy Service error: No volumes in the shadow copy set.\r\n
0x00002005 | Volume Shadow Copy Service error: ERROR_INSUFFICIENT_BUFFER expected error.  Actual Error was [%1].\r\n
0x00002006 | Volume Shadow Copy Service error: Unexpected error. Final buffer for call to GetTokenInformation was size = %1, original size was %2.\r\n
0x00002007 | Volume Shadow Copy Service error: Unexpected error performing QueryInterface from IXMLDOMNode to IXMLDOMElement.  hr = %1.\r\n
0x00002008 | Volume Shadow Copy Service error: An unexpected error was encountered examining the XML document.  The document is missing the %1 element.\r\n
0x00002009 | Volume Shadow Copy Service error: An unexpected error was encountered examining the XML document.  The document is missing the %1 attribute.\r\n
0x0000200a | Volume Shadow Copy Service error: An unexpected error was encountered when QueryInterface for IDispatch was called.  hr = %1 attribute.\r\n
0x0000200b | Volume Shadow Copy Service error: An unexpected error was encountered cloning a document.  The cloned document has no children.\r\n
0x0000200c | Volume Shadow Copy Service error: An invalid XML document was returned from writer %1.\r\n
0x0000200d | Volume Shadow Copy Service error: An error occured calling QueryInterface from IVssCoordinator to IVssShim.  hr = %1.\r\n
0x0000200e | Volume Shadow Copy Service error: There are two writers with the identical instance id %1.\r\n
0x0000200f | Volume Shadow Copy Service error: An unexpected error was encountered when calling QueryInterface for IVssAsync.  hr = %1.\r\n
0x00002010 | Volume Shadow Copy Service error: The backup components document is NULL.\r\n
0x00002011 | Volume Shadow Copy Service error: The thread handle for the asynchronous thread is NULL.\r\n
0x00002012 | Volume Shadow Copy Service error: Unexpected error %1 was returned from WaitForSingleObject.\r\n
0x00002013 | Volume Shadow Copy Service error: Writer with name %1 and ID %2 attempted to subscribe in safe mode.\r\n
0x00002014 | Volume Shadow Copy Service error: Writer with name %1 and ID %2 attempted to subscribe during setup.\r\n
0x00002015 | Volume Shadow Copy Service error: The process that hosts the writer with name %1 and ID %2 does not run under a user with sufficient access rights. \r\nConsider running this process under a local account which is either Local System, Administrator or Backup operator.\r\n
0x00002016 | Volume Shadow Copy Service error: The shadow copy writer could not communicate with the Shadow Copy publisher.\r\nThe shadow copy publisher (for example the backup application) might have terminated during the shadow copy process. \r\nhr = %1.\r\n
0x00003001 | Volume Shadow Copy Service error: Unexpected error %1.  hr = %2.\r\n
0x00003002 | Volume Shadow Copy Service warning: %1.  hr = %2.\r\n
0x00003003 | Volume Shadow Copy Service error: Error on creating/using the COM+ Writers publisher interface: %1 [%2].\r\n
0x00003004 | Volume Shadow Copy Service error: Error creating the Shadow Copy Provider COM class with CLSID %1 [%2].\r\n
0x00003005 | Volume Shadow Copy Service error: Error calling a routine on the Shadow Copy Provider %1. Routine details %2 [hr = %3].\r\n
0x00003006 | Volume Shadow Copy Service error: Error calling a routine on the Shadow Copy Provider %1. Routine returned E_INVALIDARG.\r\nRoutine details %2.\r\n
0x00003007 | Volume Shadow Copy Service error: Wrong type %1 (should be %2) for the\r\nRegistry value %3 under the key %4.\r\n
0x00003008 | Volume Shadow Copy Service error: The system may be low on resources.\r\nUnexpected error at background thread creation\r\n(_beginthreadex returns %1, errno = %2).\r\n
0x00003009 | Volume Shadow Copy Service error: The I/O writes cannot be flushed during the shadow copy creation period on volume %1.\r\nThe volume index in the shadow copy set is %2. Error details: Open[%3], Flush[%4], Release[%5], OnRun[%6].\r\n
0x0000300a | Volume Shadow Copy Service error: The I/O writes cannot be held during the shadow copy creation period on volume %1.\r\nThe volume index in the shadow copy set is %2. Error details: Open[%3], Flush[%4], Release[%5], OnRun[%6].\r\n
0x0000300b | Volume Shadow Copy Service error: One of the shadow copy providers returned an invalid number of committed shadow copies.\r\nThe expected number of committed shadow copies is %1. The detected number of committed shadow copies is %2.\r\n
0x0000300c | Volume Shadow Copy Service error: Writer %1 called CVssWriter::Initialize during Setup.\r\n
0x0000300d | Volume Shadow Copy Service error: Writer %1 did not respond to a GatherWriterStatus call.\r\n
0x0000300e | Volume Shadow Copy Service error: An internal inconsistency was detected in trying\r\nto contact shadow copy service writers.  Please check to see that the Event Service\r\nand Volume Shadow Copy Service are operating properly.\r\n
0x0000300f | An error occurred calling CoSetProxyBlanket.  hr = %1\r\n
0x00003010 | An error occurred trying to QI the IVssWriter event object for\r\nIMultiInterfaceEventControl.  hr = %1\r\n
0x00003011 | Volume Shadow Copy Service error: Volume/disk not connected or not found.\r\nError context: %1.\r\n
0x00003012 | Database of hardware shadow copy sets is not valid.  Contents are ignored.\r\n
0x00003013 | Cannot save database of hardware shadow copy sets: hr = %1.\r\n
0x00003014 | Volume %1 appears to be invalid or dismounted during shadow copy creation.\r\n
0x00003015 | VSS Assert Failure: %1\r\n
0x00003016 | Volume Shadow Copy Service error: The shadow copy could not be committed - operation timed out.\r\nError context: %1.\r\n
0x00003017 | Volume Shadow Copy Service error: Unexpected error %1: %2 hr = %3.\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x00000001 | Volume Shadow Copy Service initialization error: the control dispatcher cannot be started [%1].\r\n%2\r\n
0x00000002 | Volume Shadow Copy Service initialization error: the control handler cannot be registered [%1].\r\n%2\r\n
0x00000003 | Volume Shadow Copy Service initialization error: the COM library cannot be initialized [%1].\r\n%2\r\n
0x00000004 | Volume Shadow Copy Service initialization error: the COM security cannot be initialized [%1].\r\n%2\r\n
0x00000005 | Volume Shadow Copy Service initialization error: could not retrieve backup/restore privilege [%1].\r\n%2\r\n
0x00000006 | Volume Shadow Copy Service initialization error: the COM classes cannot be registered [%1].\r\n%2\r\n
0x00000007 | Volume Shadow Copy Service initialization error: [%1].\r\n%2\r\n
0x00000008 | Unexpected error when changing the SCM status of the Volume Shadow Copy Service: [%1, %2].\r\n%3\r\n
0x00000009 | Volume Shadow Copy Service information: Service starting at request of process '%1'. [%2]\r\n%3\r\n
0x0000000a | Volume Shadow Copy Service information: Volume '%1' appears as disconnected and it is\r\nignored by the service. You may want to rescan disks. [%2]\r\n%4\r\n
0x0000000b | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started.\r\nMost likely the CPU is under heavy load. [%3]\r\n%4\r\n
0x0000000c | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started.\r\nMost likely the server is in the process of shutting down or the system is out of memory. [%3]\r\n%4\r\n
0x0000000d | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started. [%3]\r\n%4\r\n
0x0000000e | Volume Shadow Copy Service information: A database of hardware snapshots was created.\r\n%1\r\n
0x0000000f | The user name %1 specified in registry (%2) does not map to a real user name. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\n%3\r\n
0x00000010 | The value with name %1 specified in registry (%2) is not of type REG_DWORD. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\nValue '0' denies the username from running any VSS writer.\r\nValue '1' is used to allow it.\r\n%3\r\n
0x00000011 | The value with name %1 specified in registry (%2) of value (%3) cannot be interpreted. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\nValue '0' denies the username from running any VSS writer.\r\nValue '1' is used to allow it.\r\n%4\r\n
0x00000012 | Volume Shadow Copy Service error: The COM Server with CLSID %1 and name %2 cannot be started during Safe Mode. \r\nThe Volume Shadow Copy service cannot start while in safe mode. [%3]\r\n%4\r\n
0x00000013 | Volume Shadow Copy Service error: The EventSystem service is disabled or is attempting to start during Safe Mode. \r\nThe Volume Shadow Copy service cannot start while in safe mode.\r\nIf not in safe mode, make sure that EventSystem service is enabled.\r\nCLSID:%1 Name:%2 [%3]\r\n%4\r\n
0x00000014 | Volume Shadow Copy Service error: The Volume Shadow Copy infrastructure cannot be used during Safe Mode.\r\n%1\r\n
0x00000015 | Volume Shadow Copy Service error: Writers will not receive events since the COM+ database is corrupted. \r\nThis might happened if an error occurred during Windows setup. \r\nThe error returned from CoCreateInstance on class with CLSID %1 and Name %2 is [%3]\r\n%4\r\n
0x00000016 | Volume Shadow Copy Service error: A critical component required by the Volume Shadow Copy service is not registered. \r\nThis might happened if an error occurred during Windows setup or during installation of a Shadow Copy provider. \r\nThe error returned from CoCreateInstance on class with CLSID %1 and Name %2 is [%3].\r\n%4\r\n
0x00000017 | The value specified in registry (%1) has no name. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\nValue '0' denies the username from running any VSS writer.\r\nValue '1' is used to allow it.\r\n%2\r\n
0x00000018 | Volume Shadow Copy Service Warning: The Volume Shadow Copy Service is shutting down \r\nand is experiencing delay while waiting for in-progress calls to complete.\r\n%1\r\n
0x00000019 | Volume Shadow Copy Service Warning: The Microsoft Shadow Copy Provider is shutting down \r\nand is experiencing delay while waiting for in-progress calls to complete.\r\n%1\r\n
0x0000001a | This machine is a Domain Controller with the Active Directory service (NTDS) stopped.\r\nBackup cannot be performed, nor can shadow copies be managed in this case.\r\nEither the NTDS must be started (net start ntds), or reboot in DSRM to enumerate shadow copies/providers/writers only.\r\n%1\r\n
0x0000001b | This machine is a Domain Controller but the Active Directory (NTDS) service is stopped.\r\nRestore cannot be performed while NTDS is stopped.\r\nEither the NTDS must be started (net start ntds), or reboot in DSRM.\r\n%1\r\n
0x0000001c | The given type for the ApplicationsBlockingRevert key (%1) is incorrect.\r\nIt must be a REG_MULTI_SZ containing a sequence of null-terminated volume GUID strings specifying volumes\r\nblocked from revert, followed by an extra null termination.\r\n%2\r\n
0x0000001d | This machine is a Domain Controller in Directory Service Restore Mode (DSRM).\r\nBackup cannot be performed in this case, please reboot out of DSRM.\r\n%1\r\n
0x0000001e | Fail to acquire Security Audit privilege.%n\r\nSecurity Audits for shadow copy creation and import will not be logged.\r\n%1\r\n
0x0000001f | Volume Shadow Copy Service Warning: A writer with name %1 and ID %2 waited %3 seconds\r\nfor in-progress calls to complete before shutting down.\r\n%4\r\n
0x00000020 | Volume Shadow Copy Service error: The VSS Coordinator class is not registered.  This may be caused\r\ndue to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000021 | Volume Shadow Copy Service error: The VSS management class is not registered.  This may be caused\r\ndue to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000022 | Volume Shadow Copy Service error: The VSS event class is not registered.  This will prevent any\r\nVSS writers from receiving events.  This may be caused due to a setup failure or as a result of an \r\napplication's installer or uninstaller.\r\n%1\r\n
0x00000023 | Volume Shadow Copy Service error: SQL VDI classes are not registered. This will prevent the built-in MSDE\r\nwriter from functioning properly.  This may be caused due to a setup failure or as a result of an application's \r\ninstaller or uninstaller.\r\n%1\r\n
0x00000024 | Volume Shadow Copy Service error: The MSXML classes are not registered.  This may be caused\r\ndue to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000025 | Volume Shadow Copy Service error: The Microsoft Shadow Copy Provider class is not registered..  \r\nThis may be caused due to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000026 | Volume Shadow Copy Service error:  Either the COM+ Event System service (EventSystem) or\r\nthe COM+ System Application service (COMSysApp) is disabled.  Please enable the service and try\r\nagain.\r\n%1\r\n
0x00000027 | Volume Shadow Copy Service error:  The Volume Shadow Copy service (VSS) is disabled.  Please \r\nenable the service and try again.\r\n%1\r\n
0x00000028 | Volume Shadow Copy Service error:  The Microsoft Software Shadow Copy Provider (SWPRV) service is \r\ndisabled.  Please enable the service and try again.\r\n%1\r\n
0x00000fa1 | Volume Shadow Copy Service error: Cannot find diff areas for creating shadow copies.\r\nPlease add at least one NTFS drive to the system with enough free space.\r\nThe free space needed is at least %1 Mb for each volume to be shadow copied.\r\n%2\r\n
0x00000fa2 | Volume Shadow Copy Service error: Cannot create multiple shadow copies on the same volume (%1)\r\n%2\r\n
0x00000fa3 | Volume Shadow Copy Service warning: Writer received a Freeze event more than two minutes ago.  \r\nThe writer is still waiting for either an Abort or a Thaw event.\r\n%1\r\n
0x00001001 | Volume Shadow Copy Service error: The COM+ Admin catalog instance cannot be created [%1].\r\n%2\r\n
0x00001002 | Volume Shadow Copy Service error: Cannot install the event class %1 into the COM+ application '%2' [%3].\r\n%4\r\n
0x00001003 | Volume Shadow Copy Service error: Cannot install the component %1 into the COM+ application '%2' [%3].\r\n%4\r\n
0x00001004 | Volume Shadow Copy Service error: Cannot create service '%1' for the COM+ application '%2' [%3].\r\n%4\r\n
0x00001005 | Volume Shadow Copy Service error: Cannot obtain the collection '%1' from the COM+ catalog [%2].\r\n%3\r\n
0x00001006 | Volume Shadow Copy Service error: Cannot populate the COM+ collection '%1' [%2].\r\n%3\r\n
0x00001007 | Volume Shadow Copy Service error: Cannot get the COM+ collection key [%1].\r\n%2\r\n
0x00001008 | Volume Shadow Copy Service error: Cannot get the COM+ collection '%1' from parent [%2].\r\n%3\r\n
0x00001009 | Volume Shadow Copy Service error: Cannot save the changes for the COM+ collection [%1].\r\n%2\r\n
0x0000100a | Volume Shadow Copy Service error: Cannot create a subscription (%1,%2,%3) [%4].\r\n%5\r\n
0x0000100b | Volume Shadow Copy Service error: Cannot attach to the subscription with name (%1) [%2].\r\n%3\r\n
0x0000100c | Volume Shadow Copy Service error: Cannot remove the subscription with index %1 [%2].\r\n%3\r\n
0x0000100d | Volume Shadow Copy Service error: Cannot insert the new object into the COM+ catalog  [%1].\r\n%2\r\n
0x0000100e | Volume Shadow Copy Service error: Cannot attach the catalog object to the COM+ application [%1].\r\n%2\r\n
0x0000100f | Volume Shadow Copy Service error: Cannot attach to the subscription with name (%1) [%2].\r\n%3\r\n
0x00001010 | Volume Shadow Copy Service error: Error getting current directory [%1].\r\n%2\r\n
0x00001011 | Volume Shadow Copy Service error: Error Removing COM+ application (%1) [%2].\r\n%3\r\n
0x00001389 | Volume Shadow Copy Service error: The system shadow copy writers are already initialized.\r\n
0x0000138a | Volume Shadow Copy Service error: Insufficient memory to allocate writer instance for the %1 writer.\r\n
0x0000138b | Volume Shadow Copy Service error: Unable to start worker thread for the %1 writer due to pre-existing handles for the thread, the mutex or the events.\r\n
0x0000138c | Volume Shadow Copy Service error: Unable to construct the mutex security attributes for the mutex %3 in the %4 writer due to status %1 (converted to %2).\r\n
0x0000138d | Volume Shadow Copy Service error: Unable to create mutex %3 for the %4 writer due to status %1 (converted to %2).\r\n
0x0000138e | Volume Shadow Copy Service error: Unable to create worker thread operation request event for the %3 writer due to status %1 (converted to %2).\r\n
0x0000138f | Volume Shadow Copy Service error: Unable to create worker thread operation completion event for the %3 writer due to status %1 (converted to %2).\r\n
0x00001390 | Volume Shadow Copy Service error: Unable to create worker thread for the %3 writer due to status %1 (converted to %2).\r\n
0x00001391 | Volume Shadow Copy Service error: Illegal initialisation type (%1) requested.\r\n
0x00001392 | Volume Shadow Copy Service error: Shadow Copy shim failed with status %1 (converted to %2).\r\n
0x00001393 | Volume Shadow Copy Service error: Shadow Copy writer %3 failed with status %1 (converted to %2).\r\n
0x00001394 | Volume Shadow Copy Service error: Shadow Copy shim called routine %3 which failed with status %1 (converted to %2).\r\n
0x00001395 | Volume Shadow Copy Service error: Shadow Copy writer %3 called routine %4 which failed with status %1 (converted to %2).\r\n
0x00001396 | Volume Shadow Copy Service error: Unable to request operation %2 as no worker thread for writer %1.\r\n
0x00001397 | Volume Shadow Copy Service error: Unable to change from state %1 to state %2 in writer %3 (Status %4).\r\n
0x00001398 | Volume Shadow Copy Service error: Unable to process requested operation %4 in writer %3 due to status %1 (Converted to %2).\r\n
0x00001771 | Sqllib error: Cannot create an event due to error %1.\r\n%2\r\n
0x00001772 | Sqllib error: Database %1 is not in sysdatabases.\r\n%2\r\n
0x00001773 | Sqllib error: sysaltfiles is empty.\r\n%1\r\n
0x00001774 | Sqllib error: Database %1 is not simple.\r\n
0x00001775 | Sqllib error: Database %1 is stored on multiple volumes, only some of\r\nwhich are included in the shadow-copy set.\r\n%2\r\n
0x00001776 | Sqllib error: Error thawing server %1.\r\n%2\r\n
0x00001777 | Sqllib error: sysdatabases is empty.\r\n%1\r\n
0x00001778 | Sqllib error: Failed to create VDS object. hr = %1.\r\n%2\r\n
0x00001779 | Sqllib error: Unsupported MDAC stack major version=%1 minor version=%2\r\n%3\r\n
0x0000177a | Sqllib error: Unsupported Sql Server version %1.\r\n%2\r\n
0x0000177b | Sqllib error: ODBC SQLAllocHandle failed.\r\n%1\r\n
0x0000177c | Sqllib error: ODBC Error encountered calling %1.\r\n%2\r\n%3\r\n
0x0000177d | Sqllib error: OLEDB Error encountered calling %1. hr = %2.\r\n%3\r\n%4\r\n
0x0000177e | Sqllib error: Final GetCommand from IClientVirtualDevice did not return VD_E_CLOSE.\r\nIt returned hr = %1 instead.\r\n%2\r\n
0x0000177f | Jetwriter error:  a call to Jet function %1 failed with status = %2.\r\n%3\r\n
0x00001780 | Sqllib error: The MSDE was denied access while trying to initialize OLEDB.  This can \r\nhappen when SQL security is set up to deny access to the Local Administrators group.\r\nChange the SQL security settings, and try again.\r\n%3\r\n%4\r\n
0x00001b59 | VssAdmin: %1: %2%nCommand-line: '%3'.\r\n%4\r\n
0x00002001 | Volume Shadow Copy Service error: Unexpected error calling routine %1.  hr = %2.\r\n%3\r\n
0x00002002 | Volume Shadow Copy Service error: Unexpected error querying for the IVssWriterCallback interface.  hr = %1.\r\nThis is often caused by incorrect security settings in either the writer or requestor process.\r\n%2\r\n
0x00002003 | Volume Shadow Copy Service error: Internally transferred WRITER_COMPONENTS document is invalid.\r\n%1\r\n
0x00002004 | Volume Shadow Copy Service error: No volumes in the shadow copy set.\r\n%1\r\n
0x00002005 | Volume Shadow Copy Service error: ERROR_INSUFFICIENT_BUFFER expected error.  Actual Error was [%1].\r\n%2\r\n
0x00002006 | Volume Shadow Copy Service error: Unexpected error. Final buffer for call to GetTokenInformation was size = %1, original size was %2.\r\n%3\r\n
0x00002007 | Volume Shadow Copy Service error: Unexpected error performing QueryInterface from IXMLDOMNode to IXMLDOMElement.  hr = %1.\r\n%2\r\n
0x00002008 | Volume Shadow Copy Service error: An unexpected error was encountered examining the XML document.  The document is missing the %1 element.\r\n%2\r\n
0x00002009 | Volume Shadow Copy Service error: An unexpected error was encountered examining the XML document.  The document is missing the %1 attribute.\r\n%2\r\n
0x0000200a | Volume Shadow Copy Service error: An unexpected error was encountered when QueryInterface for IDispatch was called.  hr = %1 attribute.\r\n%2\r\n
0x0000200b | Volume Shadow Copy Service error: An unexpected error was encountered cloning a document.  The cloned document has no children.\r\n%1\r\n
0x0000200c | Volume Shadow Copy Service error: An invalid XML document was returned from writer %1.\r\n%2\r\n
0x0000200d | Volume Shadow Copy Service error: An error occured calling QueryInterface from IVssCoordinator to IVssShim.  hr = %1.\r\n
0x0000200e | Volume Shadow Copy Service error: There are two writers with the identical instance id %1.\r\n%2\r\n
0x0000200f | Volume Shadow Copy Service error: An unexpected error was encountered when calling QueryInterface for IVssAsync.  hr = %1.\r\n%2\r\n
0x00002010 | Volume Shadow Copy Service error: The backup components document is NULL.\r\n%1\r\n
0x00002011 | Volume Shadow Copy Service error: The thread handle for the asynchronous thread is NULL.\r\n%1\r\n
0x00002012 | Volume Shadow Copy Service error: Unexpected error %1 was returned from WaitForSingleObject.\r\n%2\r\n
0x00002013 | Volume Shadow Copy Service error: Writer with name %1 and ID %2 attempted to subscribe in safe mode.\r\n%3\r\n
0x00002014 | Volume Shadow Copy Service: Writer with name %1 and ID %2 attempted to subscribe during setup.\r\n%3\r\n
0x00002015 | Volume Shadow Copy Service error: The process that hosts the writer with name %1 and ID %2 does not run under a user with sufficient access rights. \r\nConsider running this process under a local account which is either Local System, Administrator, Network Service, or Local Service.\r\n%3\r\n
0x00002016 | Volume Shadow Copy Service error: The shadow copy writer could not communicate with the Shadow Copy publisher.\r\nThe shadow copy publisher (for example the backup application) might have terminated during the shadow copy process. \r\nhr = %1.\r\n%2\r\n
0x00002017 | Volume Shadow Copy Service error: A component was added to the backup document that does not exist in any writer's metadata.\r\nEnsure that only actual writer components are added to the backup document.\r\n%1\r\n
0x00002018 | Volume Shadow Copy Service error: Internally transferred WRITER_METADATA document is invalid.\r\n%1\r\n
0x00002019 | Volume Shadow Copy Service error: VSS only supports multiple instances of writer\r\nwith class id %1 if the writer either does not require restore events or supplies an \r\ninstance name.\r\n%2\r\n
0x0000201a | Two instances of writer with class id %1 attempted to register with the same\r\ninstance name %2.\r\n%3\r\n
0x0000201b | Ran out of time while expanding file specification %1\%2.  This was being done\r\nfor the %3 subscriber.\r\n%4\r\n
0x0000201c | Ran out of time while deleting files.\r\n%1\r\n
0x0000201d | The Backup Components XML document was rejected. In this case the reason could be that\r\nit is not a Backup Components Document from a transportable shadow copy.\r\n%1\r\n
0x0000201e | Shadow copy has been created.%n\r\n%n\r\nUser SID:\t\t\t%1%n\r\nUser name:\t\t\t%2%n\r\nProcess ID:\t\t\t%3%n\r\n%n\r\nShadow Set ID:\t\t\t%4%n\r\nShadow ID:\t\t\t%5%n\r\nProvider ID:\t\t\t%6%n\r\nOriginal Machine:\t\t%7%n\r\nOriginal Volume:\t\t\t%8%n\r\nShadow device name:\t\t%9%n\r\n
0x0000201f | Hardware shadow copy imported.%n\r\n%n\r\nUser SID:\t\t\t%1%n\r\nUser name:\t\t\t%2%n\r\nProcess ID:\t\t\t%3%n\r\n%n\r\nShadow Set ID:\t\t\t%4%n\r\nShadow ID:\t\t\t%5%n\r\nProvider ID:\t\t\t%6%n\r\nOriginal Machine:\t\t%7%n\r\nOriginal Volume:\t\t\t%8%n\r\nShadow device name:\t\t%9%n\r\n
0x00002020 | The VSS service is shutting down due to idle timeout.\r\n%1\r\n
0x00002021 | The VSS service is shutting down due to shutdown event from the Service Control Manager.\r\n%1\r\n
0x00002022 | Ran out of time while expanding file specifications. Shadow copy optimization is partial.\r\n%1\r\n
0x00003001 | Volume Shadow Copy Service error: Unexpected error %1.  hr = %2.\r\n%3\r\n
0x00003002 | Volume Shadow Copy Service warning: %1.  hr = %2.\r\n%3\r\n
0x00003003 | Volume Shadow Copy Service error: Error on creating/using the COM+ Writers publisher interface: %1 [%2].\r\n%3\r\n
0x00003004 | Volume Shadow Copy Service error: Error creating the Shadow Copy Provider COM class with CLSID %1 [%2].\r\n%3\r\n
0x00003005 | Volume Shadow Copy Service error: Error calling a routine on a Shadow Copy Provider %1. Routine details %2 [hr = %3].\r\n%4\r\n
0x00003006 | Volume Shadow Copy Service error: Error calling a routine on the Shadow Copy Provider %1. Routine returned E_INVALIDARG.\r\nRoutine details %2.\r\n%3\r\n
0x00003007 | Volume Shadow Copy Service error: Wrong type %1 (should be %2) for the\r\nRegistry value %3 under the key %4.\r\n%5\r\n
0x00003008 | Volume Shadow Copy Service error: The system may be low on resources.\r\nUnexpected error at background thread creation\r\n(_beginthreadex returns %1, errno = %2).\r\n%3\r\n
0x00003009 | Volume Shadow Copy Service error: The I/O writes cannot be flushed during the shadow copy creation period on volume %1.\r\nThe volume index in the shadow copy set is %2. Error details: Open[%3], Flush[%4], Release[%5], OnRun[%6].\r\n%7\r\n
0x0000300a | Volume Shadow Copy Service error: The I/O writes cannot be held during the shadow copy creation period on volume %1.\r\nThe volume index in the shadow copy set is %2. Error details: Open[%3], Flush[%4], Release[%5], OnRun[%6].\r\n%7\r\n
0x0000300b | Volume Shadow Copy Service error: One of the shadow copy providers returned an invalid number of committed shadow copies.\r\nThe expected number of committed shadow copies is %1. The detected number of committed shadow copies is %2.\r\n%3\r\n
0x0000300c | Volume Shadow Copy Service error: Writer %1 called CVssWriter::Initialize during Setup.\r\n%2\r\n
0x0000300d | Volume Shadow Copy Service error: Writer %1 did not respond to a GatherWriterStatus call.\r\n%2\r\n
0x0000300e | Volume Shadow Copy Service error: An internal inconsistency was detected in trying\r\nto contact shadow copy service writers.  Please check to see that the Event Service\r\nand Volume Shadow Copy Service are operating properly.\r\n%1\r\n
0x0000300f | An error occurred calling CoSetProxyBlanket.  hr = %1\r\n%2\r\n
0x00003010 | An error occurred trying to QI the IVssWriter event object for\r\nIMultiInterfaceEventControl.  hr = %1\r\n%2\r\n
0x00003011 | Volume Shadow Copy Service error: Volume/disk not connected or not found.\r\nError context: %1.\r\n%2\r\n
0x00003012 | Database of hardware shadow copy sets is not valid.  Contents are ignored.\r\n%1\r\n
0x00003013 | Cannot save database of hardware shadow copy sets: hr = %1.\r\n%2\r\n
0x00003014 | Volume %1 appears to be invalid or dismounted during shadow copy creation.\r\n%2\r\n
0x00003015 | VSS Assert Failure: %1\r\n%2\r\n
0x00003016 | Volume Shadow Copy Service error: The shadow copy could not be committed - operation timed out.\r\nError context: %1.\r\n%2\r\n
0x00003017 | Volume Shadow Copy Service error: Unexpected error %1: %2 hr = %3.\r\n%4\r\n
0x00003018 | Database of remote shadow copy sets is not valid.  Contents are ignored.\r\n%1\r\n\r\n
0x00003019 | New database of remote shadow copy sets was created by the Volume Shadow Copy Service.\r\n%1\r\n
0x0000301a | Cannot save database of remote shadow copy sets: hr = %1.\r\n%2\r\n
0x0000301b | Database of remote shadow copies is not valid.  Contents are ignored.\r\n%1\r\n
0x0000301c | New database of remote shadow copies was created by the Volume Shadow Copy Service.\r\n%2\r\n
0x0000301d | Cannot save database of remote shadow copies: hr = %1.\r\n%2\r\n
0x0000301e | Failed to query machine %1 for shadow copies: hr = %2. Machine is skipped.\r\n%3\r\n
0x0000301f | Failed to connect to remote machine %1 for shadow copies management. Remote machine is unavailable: hr = %2.\r\nPlease make sure that this remote machine and the local machine are both on the network.\r\n%3\r\n
0x00003020 | Failed to connect to remote machine %1 for shadow copies management. Remote machine denies access: hr = %2.\r\nPlease make sure that the account running your local Volume Shadow Copy service is authorized for shadow copy management on the remote machine.\r\n%3\r\n
0x00003021 | Failed to connect to remote machine %1 for shadow copies management. Remote machine is unsupported: hr = %2.\r\nThis error indicates that the remote machine does not support shadow copies for shares. A common cause for this error \r\nis that the remote machine is running a Windows version which doesn't support this capability.\r\n%3\r\n
0x00003022 | Revert operation for volume %1 has begun.  Volume is being reverted to the shadow copy with id\r\n%2.\r\n%3\r\n
0x00003023 | Volume Shadow Copy Warning: A timeout was encountered while trying to freeze the Kernel Transaction Manager.\r\nThis means that one or more Resource Managers failed to commit within %1 seconds.  Please check the System\r\nevent log for more information.\r\n%2\r\n
0x00003024 | Volume Shadow Copy Warning: A timeout was encountered while trying to thaw the Kernel Transaction Manager.\r\nThis means that the shadow-copy creation process took longer than %1 seconds.\r\n%2\r\n
0x00003025 | Volume Shadow Copy Warning: A timeout was encountered while trying to freeze the Distributed Transaction Manager.\r\nThis means that one more more Transaction Managers failed to commit within %1 seconds.  Please check the event\r\nlogs for more information.\r\n%2\r\n
0x00003026 | Volume Shadow Copy Warning: A timeout was encountered while trying to thaw the Distributed Transaction Manager.\r\nThis means that the shadow-copy creation process took longer than %1 seconds.\r\n%2\r\n
0x00003027 | Volume Shadow Copy Warning: A timeout occured while trying to take the cluster resource %1 offline.\r\nThis means that taking the resource offline took longer than %2 seconds.\r\n%3\r\n
0x00003028 | Volume Shadow Copy Warning: A timeout occured while trying to bring  the cluster resource %1 online.\r\nThis means that tbringing the resource offline took longer than %2 seconds.\r\n%3\r\n
0x00003029 | Volume Shadow Copy Warning: A plug-and-play devnode could not be found for the volume while\r\nattempting to restart or remove the associated device.  The function GetHiddenVolumeDevinfo failed with %1.\r\nThe operation will be continue, however some state associated with this volume may not be cleaned up.\r\n%2\r\n
0x0000302a | Volume Shadow Copy Warning: The hardware shadow-copy volume %1 disappeared unexpectedly.   \r\nPlease check for any event logs reported by Plug And Play, by the hardware provider, or by volsnap.\r\n%2\r\n
0x0000302b | Volume Shadow Copy: Attempt to to dismount the volume failed with %1.  Please check the \r\nsystem event log for more information.\r\n%2\r\n
0x0000302c | Volume Shadow Copy Warning: The provider has reported an invalid Storage Device ID structure.\r\n%1\r\n
0x0000302d | Volume Shadow Copy Warning: The provider has reported a storage identifier that is not supported by VSS.\r\n                 Codeset:     %1\r\n                 Type:          %2\r\n                 Size:           %3\r\n                 NextOffset:  %4\r\n                 Association: %5\r\n\r\nThis identifier will be skipped by VSS.                 \r\n%6\r\n
0x0000302e | Volume Shadow Copy Warning: The provider failed to report any valid unique storage identifiers to VSS.\r\nVSS requires at least one storage identifier that has a non-zero size, a unique type, and an association of zero.\r\n%1\r\n
0x0000302f | Volume Shadow Copy Error: An error %1 was encountered while trying to get SCSI Page 80 information for the LUN %2.\r\n%3\r\n
0x00003030 | Volume Shadow Copy Error: An error %1 was encountered while trying to get SCSI Page 83 information for the LUN %2.\r\n%3\r\n
0x00003031 | Volume Shadow Copy Error: After restarting the device %1, Plug and Play reports that a reboot is required.  This is an \r\nunexpected situation.\r\n%3\r\n
0x00003032 | Volume Shadow Copy Error: VSS spent more than %1 seconds trying to open and flush all the volumes in the shadow-\r\ncopy set.  This caused volume %2 to timeout waiting for the hold-writes phase of shadow-copy creation.  Trying again when\r\ndisk activity is lower may solve this problem.\r\n%3\r\n
0x00003033 | Volume Shadow Copy Warning: VSS spent %1 seconds trying to open and flush the volume %2.  This might cause\r\ntimeouts while flushing other volumes in the shadow-copy set, causing the shadow-copy creation to fail.  Trying again when\r\ndisk activity is lower may solve this problem.\r\n%3\r\n
0x00003034 | Volume Shadow Copy Error: VSS waited more than %1 seconds for all voumes to be flushed.  This caused volume %2\r\nto timeout while waiting for the release-writes phase of shadow copy creation.  Trying again when disk activity is lower may \r\nsolve this problem.\r\n%3\r\n
0x00003035 | Volume Shadow Copy Warning: VSS spent %1 seconds trying to flush and hold the volume %2.  This might cause\r\nproblems when other volumes in the shadow-copy set timeout waiting for the release-writes phase, and it can cause \r\nthe shadow-copy creation to fail.  Trying again when disk activity is lower may solve this problem.\r\n%3\r\n
0x00003036 | Volume Shadow Copy Error: An error %1 was encountered while trying to initialize the Registry Writer.  This may cause\r\nfuture shadow-copy creations to fail.\r\n%2\r\n
0x00003037 | Volume Shadow Copy Error: An error %1 was encountered while Registry Writer was attempting to initialize itself.  This \r\nmay case a shadow-copy creation to fail.  Please check the Application event log for any related errors.\r\n%2\r\n
0x00003038 | Volume Shadow Copy Error: An error %1 was encountered while Registry Writer was preparing the registry for a shadow\r\ncopy.  Please check the Application and System event logs for any related errors.\r\n%2\r\n
0x00003039 | Volume Shadow Copy Error: The Registry Writer experienced an out-of-space condition while preparing the registry for\r\na Shadow Copy.  Please check the Application and System event logs for any related errors.\r\n%1\r\n
0x0000303a | Volume Shadow Copy Error: An error %1 was encountered while trying to initialize the Registry Writer.  This may cause\r\nfuture shadow-copy creations to fail.\r\n%2\r\n
0x0000303b | Volume Shadow Copy Service error: An internal inconsistency was detected in trying\r\nto contact shadow copy service writers.  The Registry Writer failed to respond to a query \r\nfrom VSS. Please check to see that the Event Service and Volume Shadow Copy Service \r\nare operating properly, and please check the Application event log for any other events.\r\n%1\r\n
0x0000303c | Volume Shadow Copy Service warning: VSS was denied access to the root of volume %1.\r\nDenying administrators from accessing volume roots can cause many unexpected failures,\r\nand will prevent VSS from functioning properly.  Check security on the volume, and try the\r\noperation again.\r\n%2\r\n
0x0000303d | Volume Shadow Copy Service warning: The writer spent too much time processing it's Freeze\r\nnotification.  This can cause this writer as well as other writers on the system time to time out \r\nand fail shadow-copy creation.\r\n%1\r\n
0x0000a001 | ASR Error: Failed to collect critical information for ASR Backup.\r\nReason:    Unable to obtain disk information for device %1 (Win32 error code %2).\r\n
0x0000a002 | ASR Error: Fail to exclude disk #%1.\r\nReason:    The disk contains a critical volume.\r\n
0x0000a003 | ASR Error: Fail to exclude dynamic pack.\r\nReason:    Some, but not all, dynamic disks in the pack have been marked excluded.\r\n
0x0000b001 | Select to include disk #%1 (of signature %2) for ASR restore.\r\n
0x0000b002 | Select to include disk #%1 (raw disk) for ASR restore.\r\n
0x0000b003 | Select this volume (%1) if it is a critical volume.\r\nCritical volumes are those which ASR must restore.\r\n
0x0000b004 | This is the path to the boot BCD store and the boot managers.\r\nAll the files in this directory need to be backed up.\r\n

### 6.1.7600.16385, 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0

Message identifier | Message string
--- | ---
0x00000001 | Volume Shadow Copy Service initialization error: the control dispatcher cannot be started [%1].\r\n%2\r\n
0x00000002 | Volume Shadow Copy Service initialization error: the control handler cannot be registered [%1].\r\n%2\r\n
0x00000003 | Volume Shadow Copy Service initialization error: the COM library cannot be initialized [%1].\r\n%2\r\n
0x00000004 | Volume Shadow Copy Service initialization error: the COM security cannot be initialized [%1].\r\n%2\r\n
0x00000005 | Volume Shadow Copy Service initialization error: could not retrieve backup/restore privilege [%1].\r\n%2\r\n
0x00000006 | Volume Shadow Copy Service initialization error: the COM classes cannot be registered [%1].\r\n%2\r\n
0x00000007 | Volume Shadow Copy Service initialization error: [%1].\r\n%2\r\n
0x00000008 | Unexpected error when changing the SCM status of the Volume Shadow Copy Service: [%1, %2].\r\n%3\r\n
0x00000009 | Volume Shadow Copy Service information: Service starting at request of process '%1'. [%2]\r\n%3\r\n
0x0000000a | Volume Shadow Copy Service information: Volume '%1' appears as disconnected and it is\r\nignored by the service. You may want to rescan disks. [%2]\r\n%3\r\n
0x0000000b | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started.\r\nMost likely the CPU is under heavy load. [%3]\r\n%4\r\n
0x0000000c | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started.\r\nMost likely the server is in the process of shutting down or the system is out of memory. [%3]\r\n%4\r\n
0x0000000d | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started. [%3]\r\n%4\r\n
0x0000000e | Volume Shadow Copy Service information: A database of hardware snapshots was created.\r\n%1\r\n
0x0000000f | The user name %1 specified in registry (%2) does not map to a real user name. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\n%3\r\n
0x00000010 | The value with name %1 specified in registry (%2) is not of type REG_DWORD. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\nValue '0' denies the username from running any VSS writer.\r\nValue '1' is used to allow it.\r\n%3\r\n
0x00000011 | The value with name %1 specified in registry (%2) of value (%3) cannot be interpreted. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\nValue '0' denies the username from running any VSS writer.\r\nValue '1' is used to allow it.\r\n%4\r\n
0x00000012 | Volume Shadow Copy Service error: The COM Server with CLSID %1 and name %2 cannot be started during Safe Mode.\r\nThe Volume Shadow Copy service cannot start while in safe mode. [%3]\r\n%4\r\n
0x00000013 | Volume Shadow Copy Service error: The EventSystem service is disabled or is attempting to start during Safe Mode.\r\nThe Volume Shadow Copy service cannot start while in safe mode.\r\nIf not in safe mode, make sure that EventSystem service is enabled.\r\nCLSID:%1 Name:%2 [%3]\r\n%4\r\n
0x00000014 | Volume Shadow Copy Service error: The Volume Shadow Copy infrastructure cannot be used during Safe Mode.\r\n%1\r\n
0x00000015 | Volume Shadow Copy Service error: Writers will not receive events since the COM+ database is corrupted.\r\nThis might happened if an error occurred during Windows setup.\r\nThe error returned from CoCreateInstance on class with CLSID %1 and Name %2 is [%3]\r\n%4\r\n
0x00000016 | Volume Shadow Copy Service error: A critical component required by the Volume Shadow Copy service is not registered.\r\nThis might happened if an error occurred during Windows setup or during installation of a Shadow Copy provider.\r\nThe error returned from CoCreateInstance on class with CLSID %1 and Name %2 is [%3].\r\n%4\r\n
0x00000017 | The value specified in registry (%1) has no name. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\nValue '0' denies the username from running any VSS writer.\r\nValue '1' is used to allow it.\r\n%2\r\n
0x00000018 | Volume Shadow Copy Service Warning: The Volume Shadow Copy Service is shutting down\r\nand is experiencing delay while waiting for in-progress calls to complete.\r\n%1\r\n
0x00000019 | Volume Shadow Copy Service Warning: The Microsoft Shadow Copy Provider is shutting down\r\nand is experiencing delay while waiting for in-progress calls to complete.\r\n%1\r\n
0x0000001a | This machine is a Domain Controller with the Active Directory service (NTDS) stopped.\r\nBackup cannot be performed, nor can shadow copies be managed in this case.\r\nEither the NTDS must be started (net start ntds), or reboot in DSRM to enumerate shadow copies/providers/writers only.\r\n%1\r\n
0x0000001b | This machine is a Domain Controller but the Active Directory (NTDS) service is stopped.\r\nRestore cannot be performed while NTDS is stopped.\r\nEither the NTDS must be started (net start ntds), or reboot in DSRM.\r\n%1\r\n
0x0000001c | The given type for the ApplicationsBlockingRevert key (%1) is incorrect.\r\nIt must be a REG_MULTI_SZ containing a sequence of null-terminated volume GUID strings specifying volumes\r\nblocked from revert, followed by an extra null termination.\r\n%2\r\n
0x0000001d | This machine is a Domain Controller in Directory Service Restore Mode (DSRM).\r\nBackup cannot be performed in this case, please reboot out of DSRM.\r\n%1\r\n
0x0000001e | Fail to acquire Security Audit privilege.%n\r\nSecurity Audits for shadow copy creation and import will not be logged.\r\n%1\r\n
0x0000001f | Volume Shadow Copy Service Warning: A writer with name %1 and ID %2 waited %3 seconds\r\nfor in-progress calls to complete before shutting down.\r\n%4\r\n
0x00000020 | Volume Shadow Copy Service error: The VSS Coordinator class is not registered.  This may be caused\r\ndue to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000021 | Volume Shadow Copy Service error: The VSS management class is not registered.  This may be caused\r\ndue to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000022 | Volume Shadow Copy Service error: The VSS event class is not registered.  This will prevent any\r\nVSS writers from receiving events.  This may be caused due to a setup failure or as a result of an\r\napplication's installer or uninstaller.\r\n%1\r\n
0x00000024 | Volume Shadow Copy Service error: The MSXML classes are not registered.  This may be caused\r\ndue to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000025 | Volume Shadow Copy Service error: The Microsoft Shadow Copy Provider class is not registered..\r\nThis may be caused due to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000026 | Volume Shadow Copy Service error:  Either the COM+ Event System service (EventSystem) or\r\nthe COM+ System Application service (COMSysApp) is disabled.  Enable the service and try\r\nagain.\r\n%1\r\n
0x00000027 | Volume Shadow Copy Service error:  The Volume Shadow Copy service (VSS) is disabled. Enable \r\nthe service and try again.\r\n%1\r\n
0x00000028 | Volume Shadow Copy Service error:  The Microsoft Software Shadow Copy Provider (SWPRV) service is\r\ndisabled.  Enable the service and try again.\r\n%1\r\n
0x0000002c | Volume Shadow Copy Service information: Disk '%1' appears as disconnected and it is\r\nrejected by the service. You may want to rescan disks. [%2]\r\n%3\r\n
0x0000002d | Volume Shadow Copy Service information: Volume '%1' appears as disconnected and it is\r\nignored by the service. You may want to rescan disks. [%2]\r\n%3\r\n
0x00000fa1 | Volume Shadow Copy Service error: Cannot find diff areas for creating shadow copies.\r\nAdd at least one NTFS drive to the system with enough free space.\r\nThe free space needed is at least %1 Mb for each volume to be shadow copied.\r\n%2\r\n
0x00000fa2 | Volume Shadow Copy Service error: Cannot create multiple shadow copies on the same volume (%1)\r\n%2\r\n
0x00000fa3 | Volume Shadow Copy Service warning: Writer received a Freeze event more than two minutes ago.\r\nThe writer is still waiting for either an Abort or a Thaw event.\r\n%1\r\n
0x00000fa4 | Volume Shadow Copy Service warning: The sector size of the diff area volume %1 cannot be larger than the sector size of the original volume %2\r\n%3\r\n
0x00001001 | Volume Shadow Copy Service error: The COM+ Admin catalog instance cannot be created [%1].\r\n%2\r\n
0x00001002 | Volume Shadow Copy Service error: Cannot install the event class %1 into the COM+ application '%2' [%3].\r\n%4\r\n
0x00001003 | Volume Shadow Copy Service error: Cannot install the component %1 into the COM+ application '%2' [%3].\r\n%4\r\n
0x00001004 | Volume Shadow Copy Service error: Cannot create service '%1' for the COM+ application '%2' [%3].\r\n%4\r\n
0x00001005 | Volume Shadow Copy Service error: Cannot obtain the collection '%1' from the COM+ catalog [%2].\r\n%3\r\n
0x00001006 | Volume Shadow Copy Service error: Cannot populate the COM+ collection '%1' [%2].\r\n%3\r\n
0x00001007 | Volume Shadow Copy Service error: Cannot get the COM+ collection key [%1].\r\n%2\r\n
0x00001008 | Volume Shadow Copy Service error: Cannot get the COM+ collection '%1' from parent [%2].\r\n%3\r\n
0x00001009 | Volume Shadow Copy Service error: Cannot save the changes for the COM+ collection [%1].\r\n%2\r\n
0x0000100a | Volume Shadow Copy Service error: Cannot create a subscription (%1,%2,%3) [%4].\r\n%5\r\n
0x0000100b | Volume Shadow Copy Service error: Cannot attach to the subscription with name (%1) [%2].\r\n%3\r\n
0x0000100c | Volume Shadow Copy Service error: Cannot remove the subscription with index %1 [%2].\r\n%3\r\n
0x0000100d | Volume Shadow Copy Service error: Cannot insert the new object into the COM+ catalog  [%1].\r\n%2\r\n
0x0000100e | Volume Shadow Copy Service error: Cannot attach the catalog object to the COM+ application [%1].\r\n%2\r\n
0x0000100f | Volume Shadow Copy Service error: Cannot attach to the subscription with name (%1) [%2].\r\n%3\r\n
0x00001010 | Volume Shadow Copy Service error: Error getting current directory [%1].\r\n%2\r\n
0x00001011 | Volume Shadow Copy Service error: Error Removing COM+ application (%1) [%2].\r\n%3\r\n
0x0000177f | Jetwriter error:  a call to Jet function %1 failed with status = %2.\r\n%3\r\n
0x00001780 | Express Writer error: failed while adding express writers from directory %1.\r\n%2\r\n
0x00001b59 | VssAdmin: %1: %2%nCommand-line: '%3'.\r\n%4\r\n
0x00002001 | Volume Shadow Copy Service error: Unexpected error calling routine %1.  hr = %2.\r\n%3\r\n
0x00002002 | Volume Shadow Copy Service error: Unexpected error querying for the IVssWriterCallback interface.  hr = %1.\r\nThis is often caused by incorrect security settings in either the writer or requestor process.\r\n%2\r\n
0x00002003 | Volume Shadow Copy Service error: Internally transferred WRITER_COMPONENTS document is invalid.\r\n%1\r\n
0x00002004 | Volume Shadow Copy Service error: No volumes in the shadow copy set.\r\n%1\r\n
0x00002005 | Volume Shadow Copy Service error: ERROR_INSUFFICIENT_BUFFER expected error.  Actual Error was [%1].\r\n%2\r\n
0x00002006 | Volume Shadow Copy Service error: Unexpected error. Final buffer for call to GetTokenInformation was size = %1, original size was %2.\r\n%3\r\n
0x00002007 | Volume Shadow Copy Service error: Unexpected error performing QueryInterface from IXMLDOMNode to IXMLDOMElement.  hr = %1.\r\n%2\r\n
0x00002008 | Volume Shadow Copy Service error: An unexpected error was encountered examining the XML document.  The document is missing the %1 element.\r\n%2\r\n
0x00002009 | Volume Shadow Copy Service error: An unexpected error was encountered examining the XML document.  The document is missing the %1 attribute.\r\n%2\r\n
0x0000200a | Volume Shadow Copy Service error: An unexpected error was encountered when QueryInterface for IDispatch was called.  hr = %1 attribute.\r\n%2\r\n
0x0000200b | Volume Shadow Copy Service error: An unexpected error was encountered cloning a document.  The cloned document has no children.\r\n%1\r\n
0x0000200c | Volume Shadow Copy Service error: An invalid XML document was returned from writer %1.\r\n%2\r\n
0x0000200d | Volume Shadow Copy Service error: An error occured calling QueryInterface from IVssCoordinator to IVssShim.  hr = %1.\r\n
0x0000200e | Volume Shadow Copy Service error: There are two writers with the identical instance id %1.\r\n%2\r\n
0x0000200f | Volume Shadow Copy Service error: An unexpected error was encountered when calling QueryInterface for IVssAsync.  hr = %1.\r\n%2\r\n
0x00002010 | Volume Shadow Copy Service error: The backup components document is NULL.\r\n%1\r\n
0x00002011 | Volume Shadow Copy Service error: The thread handle for the asynchronous thread is NULL.\r\n%1\r\n
0x00002012 | Volume Shadow Copy Service error: Unexpected error %1 was returned from WaitForSingleObject.\r\n%2\r\n
0x00002013 | Volume Shadow Copy Service error: Writer with name %1 and ID %2 attempted to subscribe in safe mode.\r\n%3\r\n
0x00002014 | Volume Shadow Copy Service: Writer with name %1 and ID %2 attempted to subscribe during setup.\r\n%3\r\n
0x00002015 | Volume Shadow Copy Service error: The process that hosts the writer with name %1 and ID %2 does not run under a user with sufficient access rights.\r\nConsider running this process under a local account which is either Local System, Administrator, Network Service, or Local Service.\r\n%3\r\n
0x00002016 | Volume Shadow Copy Service error: The shadow copy writer could not communicate with the Shadow Copy publisher.\r\nThe shadow copy publisher (for example the backup application) might have terminated during the shadow copy process.\r\nhr = %1.\r\n%2\r\n
0x00002017 | Volume Shadow Copy Service error: A component was added to the backup document that does not exist in any writer's metadata.\r\nEnsure that only actual writer components are added to the backup document.\r\n%1\r\n
0x00002018 | Volume Shadow Copy Service error: Internally transferred WRITER_METADATA document is invalid.\r\n%1\r\n
0x00002019 | Volume Shadow Copy Service error: VSS only supports multiple instances of writer\r\nwith class id %1 if the writer either does not require restore events or supplies an\r\ninstance name.\r\n%2\r\n
0x0000201a | Two instances of writer with class id %1 attempted to register with the same\r\ninstance name %2.\r\n%3\r\n
0x0000201b | Ran out of time while expanding file specification %1\%2.  This was being done\r\nfor the %3 subscriber.\r\n%4\r\n
0x0000201c | Ran out of time while deleting files.\r\n%1\r\n
0x0000201d | The Backup Components XML document was rejected. In this case the reason could be that\r\nit is not a Backup Components Document from a transportable shadow copy.\r\n%1\r\n
0x0000201e | Shadow copy has been created.%n\r\n%n\r\nUser SID:\t\t\t%1%n\r\nUser name:\t\t\t%2%n\r\nProcess ID:\t\t\t%3%n\r\n%n\r\nShadow Set ID:\t\t\t%4%n\r\nShadow ID:\t\t\t%5%n\r\nProvider ID:\t\t\t%6%n\r\nOriginal Machine:\t\t%7%n\r\nOriginal Volume:\t\t\t%8%n\r\nShadow device name:\t\t%9%n\r\n
0x0000201f | Hardware shadow copy imported.%n\r\n%n\r\nUser SID:\t\t\t%1%n\r\nUser name:\t\t\t%2%n\r\nProcess ID:\t\t\t%3%n\r\n%n\r\nShadow Set ID:\t\t\t%4%n\r\nShadow ID:\t\t\t%5%n\r\nProvider ID:\t\t\t%6%n\r\nOriginal Machine:\t\t%7%n\r\nOriginal Volume:\t\t\t%8%n\r\nShadow device name:\t\t%9%n\r\n
0x00002020 | The VSS service is shutting down due to idle timeout.\r\n%1\r\n
0x00002021 | The VSS service is shutting down due to shutdown event from the Service Control Manager.\r\n%1\r\n
0x00002022 | Ran out of time while expanding file specifications. Shadow copy optimization is partial.\r\n%1\r\n
0x00002023 | The user name %1 specified in registry (%2) is not valid, winerror %3. The entry is ignored.%n\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\n%4\r\n
0x00002024 | Fail to parse XML file.%n\r\nReason %1%n\r\nLine %2%n\r\nPosition %3%n\r\nErrorcode %4%n\r\nProblem text %5%n\r\n%6\r\n
0x00002025 | A VSS writer has rejected an event with error %1. Changes that the writer made to the writer components while handling the event will not be available to the requester.\r\nCheck the event log for related events from the application hosting the VSS writer.\r\n%2\r\n
0x00002026 | Volume Shadow Copy Service error: Failed resolving account %1 with status %2. Check connection to domain controller and VssAccessControl registry key.\r\n%3\r\n
0x00003001 | Volume Shadow Copy Service error: Unexpected error %1.  hr = %2.\r\n%3\r\n
0x00003002 | Volume Shadow Copy Service warning: %1.  hr = %2.\r\n%3\r\n
0x00003003 | Volume Shadow Copy Service error: Error on creating/using the COM+ Writers publisher interface: %1 [%2].\r\n%3\r\n
0x00003004 | Volume Shadow Copy Service error: Error creating the Shadow Copy Provider COM class with CLSID %1 [%2].\r\n%3\r\n
0x00003005 | Volume Shadow Copy Service error: Error calling a routine on a Shadow Copy Provider %1. Routine details %2 [hr = %3].\r\n%4\r\n
0x00003006 | Volume Shadow Copy Service error: Error calling a routine on the Shadow Copy Provider %1. Routine returned E_INVALIDARG.\r\nRoutine details %2.\r\n%3\r\n
0x00003007 | Volume Shadow Copy Service error: Wrong type %1 (should be %2) for the\r\nRegistry value %3 under the key %4.\r\n%5\r\n
0x00003008 | Volume Shadow Copy Service error: The system may be low on resources.\r\nUnexpected error at background thread creation\r\n(_beginthreadex returns %1, errno = %2).\r\n%3\r\n
0x00003009 | Volume Shadow Copy Service error: The I/O writes cannot be flushed during the shadow copy creation period on volume %1.\r\nThe volume index in the shadow copy set is %2. Error details: Open[%3], Flush[%4], Release[%5], OnRun[%6].\r\n%7\r\n
0x0000300a | Volume Shadow Copy Service error: The I/O writes cannot be held during the shadow copy creation period on volume %1.\r\nThe volume index in the shadow copy set is %2. Error details: Open[%3], Flush[%4], Release[%5], OnRun[%6].\r\n%7\r\n
0x0000300b | Volume Shadow Copy Service error: One of the shadow copy providers returned an invalid number of committed shadow copies.\r\nThe expected number of committed shadow copies is %1. The detected number of committed shadow copies is %2.\r\n%3\r\n
0x0000300c | Volume Shadow Copy Service error: Writer %1 called CVssWriter::Initialize during Setup.\r\n%2\r\n
0x0000300d | Volume Shadow Copy Service error: Writer %1 did not respond to a GatherWriterStatus call.\r\n%2\r\n
0x0000300e | Volume Shadow Copy Service error: An internal inconsistency was detected in trying\r\nto contact shadow copy service writers.  Check to see that the Event Service\r\nand Volume Shadow Copy Service are operating properly.\r\n%1\r\n
0x0000300f | An error occurred calling CoSetProxyBlanket.  hr = %1\r\n%2\r\n
0x00003010 | An error occurred trying to QI the IVssWriter event object for\r\nIMultiInterfaceEventControl.  hr = %1\r\n%2\r\n
0x00003011 | Volume Shadow Copy Service error: Volume/disk not connected or not found.\r\nError context: %1.\r\n%2\r\n
0x00003012 | Database of hardware shadow copy sets is not valid.  Contents are ignored.\r\n%1\r\n
0x00003013 | Cannot save database of hardware shadow copy sets: hr = %1.\r\n%2\r\n
0x00003014 | Volume %1 appears to be invalid or dismounted during shadow copy creation.\r\n%2\r\n
0x00003015 | VSS Assert Failure: %1\r\n%2\r\n
0x00003016 | Volume Shadow Copy Service error: The shadow copy could not be committed - operation timed out.\r\nError context: %1.\r\n%2\r\n
0x00003017 | Volume Shadow Copy Service error: Unexpected error %1: %2 hr = %3.\r\n%4\r\n
0x00003018 | Database of remote shadow copy sets is not valid.  Contents are ignored.\r\n%1\r\n\r\n
0x00003019 | New database of remote shadow copy sets was created by the Volume Shadow Copy Service.\r\n%1\r\n
0x0000301a | Cannot save database of remote shadow copy sets: hr = %1.\r\n%2\r\n
0x0000301b | Database of remote shadow copies is not valid.  Contents are ignored.\r\n%1\r\n
0x0000301c | New database of remote shadow copies was created by the Volume Shadow Copy Service.\r\n%2\r\n
0x0000301d | Cannot save database of remote shadow copies: hr = %1.\r\n%2\r\n
0x0000301e | Failed to query machine %1 for shadow copies: hr = %2. Machine is skipped.\r\n%3\r\n
0x0000301f | Failed to connect to remote machine %1 for shadow copies management. Remote machine is unavailable: hr = %2.\r\nMake sure that this remote machine and the local machine are both on the network.\r\n%3\r\n
0x00003020 | Failed to connect to remote machine %1 for shadow copies management. Remote machine denies access: hr = %2.\r\nMake sure that the account running your local Volume Shadow Copy service is authorized for shadow copy management on the remote machine.\r\n%3\r\n
0x00003021 | Failed to connect to remote machine %1 for shadow copies management. Remote machine is unsupported: hr = %2.\r\nThis error indicates that the remote machine does not support shadow copies for shares. A common cause for this error\r\nis that the remote machine is running a Windows version which doesn't support this capability.\r\n%3\r\n
0x00003022 | Revert operation for volume %1 has begun.  Volume is being reverted to the shadow copy with id\r\n%2.\r\n%3\r\n
0x00003023 | Volume Shadow Copy Warning: A timeout was encountered while trying to freeze the Kernel Transaction Manager.\r\nThis means that one or more Resource Managers failed to commit within %1 seconds.  Check the System\r\nevent log for more information.\r\n%2\r\n
0x00003024 | Volume Shadow Copy Warning: A timeout was encountered while trying to thaw the Kernel Transaction Manager.\r\nThis means that the shadow-copy creation process took longer than %1 seconds.\r\n%2\r\n
0x00003025 | Volume Shadow Copy Warning: A timeout was encountered while trying to freeze the Distributed Transaction Manager.\r\nThis means that one or more Transaction Managers failed to commit within %1 seconds.  Check the event\r\nlogs for more information.\r\n%2\r\n
0x00003026 | Volume Shadow Copy Warning: A timeout was encountered while trying to thaw the Distributed Transaction Manager.\r\nThis means that the shadow-copy creation process took longer than %1 seconds.\r\n%2\r\n
0x00003027 | Volume Shadow Copy Warning: A timeout occured while trying to take the cluster resource %1 offline.\r\nThis means that taking the resource offline took longer than %2 seconds.\r\n%3\r\n
0x00003028 | Volume Shadow Copy Warning: A timeout occurred while trying to bring the cluster resource %1 online.\r\nThis means that bringing the resource offline took longer than %2 seconds.\r\n%3\r\n
0x00003029 | Volume Shadow Copy Warning: A plug-and-play devnode could not be found for the volume while\r\nattempting to restart or remove the associated device.  The function GetHiddenVolumeDevinfo failed with %1.\r\nThe operation will be continue, however some state associated with this volume may not be cleaned up.\r\n%2\r\n
0x0000302a | Volume Shadow Copy Warning: The hardware shadow-copy volume %1 disappeared unexpectedly.\r\nCheck for any event logs reported by Plug And Play, by the hardware provider, or by volsnap.\r\n%2\r\n
0x0000302b | Volume Shadow Copy: Attempt to dismount the volume failed with %1.  Check the\r\nsystem event log for more information.\r\n%2\r\n
0x0000302c | Volume Shadow Copy Warning: The provider has reported an invalid Storage Device ID structure.\r\n%1\r\n
0x0000302d | Volume Shadow Copy Warning: The provider has reported a storage identifier that is not supported by VSS.\r\n                 Codeset:     %1\r\n                 Type:          %2\r\n                 Size:           %3\r\n                 NextOffset:  %4\r\n                 Association: %5\r\n\r\nThis identifier will be skipped by VSS.\r\n%6\r\n
0x00003031 | Volume Shadow Copy Error: After restarting the device %1, Plug and Play reports that a reboot is required.  This is an\r\nunexpected situation.\r\n%3\r\n
0x00003032 | Volume Shadow Copy Error: VSS spent more than %1 seconds trying to open and flush all the volumes in the shadow-\r\ncopy set.  This caused volume %2 to timeout waiting for the hold-writes phase of shadow-copy creation.  Trying again when\r\ndisk activity is lower may solve this problem.\r\n%3\r\n
0x00003033 | Volume Shadow Copy Warning: VSS spent %1 seconds trying to open and flush the volume %2.  This might cause\r\ntimeouts while flushing other volumes in the shadow-copy set, causing the shadow-copy creation to fail.  Trying again when\r\ndisk activity is lower may solve this problem.\r\n%3\r\n
0x00003034 | Volume Shadow Copy Error: VSS waited more than %1 seconds for all volumes to be flushed.  This caused volume %2\r\nto timeout while waiting for the release-writes phase of shadow copy creation.  Trying again when disk activity is lower may\r\nsolve this problem.\r\n%3\r\n
0x00003035 | Volume Shadow Copy Warning: VSS spent %1 seconds trying to flush and hold the volume %2.  This might cause\r\nproblems when other volumes in the shadow-copy set timeout waiting for the release-writes phase, and it can cause\r\nthe shadow-copy creation to fail.  Trying again when disk activity is lower may solve this problem.\r\n%3\r\n
0x00003036 | Volume Shadow Copy Error: An error %1 was encountered while trying to initialize the Registry Writer.  This may cause\r\nfuture shadow-copy creations to fail.\r\n%2\r\n
0x00003037 | Volume Shadow Copy Error: An error %1 was encountered while Registry Writer was attempting to initialize itself.  This\r\nmay case a shadow-copy creation to fail.  Check the Application event log for any related errors.\r\n%2\r\n
0x00003038 | Volume Shadow Copy Error: An error %1 was encountered while Registry Writer was preparing the registry for a shadow\r\ncopy.  Check the Application and System event logs for any related errors.\r\n%2\r\n
0x00003039 | Volume Shadow Copy Error: The Registry Writer experienced an out-of-space condition while preparing the registry for\r\na Shadow Copy.  Check the Application and System event logs for any related errors.\r\n%1\r\n
0x0000303a | Volume Shadow Copy Error: An error %1 was encountered while trying to initialize the Registry Writer.  This may cause\r\nfuture shadow-copy creations to fail.\r\n%2\r\n
0x0000303b | Volume Shadow Copy Service error: An internal inconsistency was detected in trying\r\nto contact shadow copy service writers.  The Registry Writer failed to respond to a query\r\nfrom VSS. Check to see that the Event Service and Volume Shadow Copy Service\r\nare operating properly, and please check the Application event log for any other events.\r\n%1\r\n
0x0000303c | Volume Shadow Copy Service warning: VSS was denied access to the root of volume %1.\r\nDenying administrators from accessing volume roots can cause many unexpected failures,\r\nand will prevent VSS from functioning properly.  Check security on the volume, and try the\r\noperation again.\r\n%2\r\n
0x0000303d | Volume Shadow Copy Service warning: The writer spent too much time processing it's Freeze\r\nnotification.  This can cause this writer as well as other writers on the system time to time out\r\nand fail shadow-copy creation.\r\n%1\r\n
0x0000303e | When snapshot volume %1 was restarted in the system, the restart failed. The volume is no longer found in the system.%n\r\nTry a rescan from Diskmgmt.msc and see if the volume appears.%n\r\nIf not, try restarting the disk device then rescan.\r\n%2\r\n
0x00003040 | Fail to revert the signature of %1 .\r\n%2\r\n
0x00003041 | Failed to set the mount point %1 for volume %2, winerror %3\r\n%4\r\n
0x00003042 | Failed to set the share %1 after break, netstatus %2.\r\n%3\r\n
0x00003043 | Cannot request the shadow copy volume to be made readwrite if mask is requested.\r\n%1\r\n
0x00003044 | Cannot force signature revert if no signature revert is requested.\r\n%1\r\n
0x00003045 | The BreaksnapshotSetEx method failed because the disk signature of one or more shadow copy LUNs could not \r\nbe reverted to those of the original LUNs. If one or more original LUNs are not masked on the computer, this\r\ncan cause a disk signature collision.  Disk signatures of dynamic disks cannot be reverted.\r\n%1\r\n
0x00003046 | The requester specified the VSS_ONLUNSTATECHANGE_DO_MASK_LUNS flag when calling the BreakSnaphsotSetEx method,\r\nbut the hardware provider for this shadow copy does not implement the IVssHardwareSnapshotProviderEx interface.\r\n%1\r\n
0x00003049 | Provider %1 failed BreakSnapshotSetEx for Snapshot Set %2 with %3.\r\n%4\r\n
0x0000304a | A Shadow Copy LUN was not detected in the system and did not arrive.%n\r\n%n\r\nLUN ID\t\t\t%1%n\r\n%n\r\nVersion\t\t\t%2%n\r\nDevice Type\t\t%3%n\r\nDevice TypeModifier\t%4%n\r\nCommand Queueing\t%5%n\r\nBus Type\t\t%6%n\r\nVendor Id\t\t%7%n\r\nProduct Id\t\t%8%n\r\nProduct Revision\t\t%9%n\r\nSerial Number\t\t%10%n\r\n%n\r\nStorage Identifiers%n\r\n%11%n\r\n%n\r\n%12\r\n
0x0000304b | An expected hidden volume arrival did not complete because this LUN was not detected.%n\r\n%n\r\nLUN ID\t\t\t%1%n\r\n%n\r\nVersion\t\t\t%2%n\r\nDevice Type\t\t%3%n\r\nDevice TypeModifier\t%4%n\r\nCommand Queueing\t%5%n\r\nBus Type\t\t%6%n\r\nVendor Id\t\t%7%n\r\nProduct Id\t\t%8%n\r\nProduct Revision\t\t%9%n\r\nSerial Number\t\t%10%n\r\n%n\r\nStorage Identifiers%n\r\n%11%n\r\n%n\r\n%12\r\n
0x0000304c | An expected volume arrival did not complete because this LUN was not detected.%n\r\n%n\r\nLUN ID\t\t\t%1%n\r\n%n\r\nVersion\t\t\t%2%n\r\nDevice Type\t\t%3%n\r\nDevice TypeModifier\t%4%n\r\nCommand Queueing\t%5%n\r\nBus Type\t\t%6%n\r\nVendor Id\t\t%7%n\r\nProduct Id\t\t%8%n\r\nProduct Revision\t\t%9%n\r\nSerial Number\t\t%10%n\r\n%n\r\nStorage Identifiers%n\r\n%11%n\r\n%n\r\n%12\r\n
0x0000304e | An unhandled exception was encountered while processing a VSS writer event callback method. The VSS\r\nwriter infrastructure is in an unstable state. Restart the service or application that hosts the writer.%n\r\n%n\r\nWriter name:            %1%n\r\nWriter id:              %2%n\r\nWriter instance:        %3%n\r\nProcess command line:   %4%n\r\nProcess ID:             %5%n\r\nWriter operation:       %6%n\r\nWriter state:           %7%n\r\nException code:         %8%n\r\nException location:     %9%n\r\n
0x00003052 | The hardware provider for this shadow copy does not support LUN resynchronization.%n\r\n%1\r\n
0x00003055 | The Volume Shadow Copy Service was unable to load the provider with identifier %1. Reinstall the provider\r\nand retry the operation. If the provider still fails to load, please contact the vendor responsible\r\nfor that provider.%n\r\n%2\r\n
0x00003056 | The destination LUN could not be resynchronized from the source volume because it did not report a\r\nunique SCSI storage storage identifier of type 1, 2, 3, or 8 and association 0.%n\r\nRetry the operation with a different destination LUN.%n\r\n%1\r\n
0x00003057 | The resynchronization operation failed because the MBR signature or GPT ID of one or more of the\r\ndestination LUNs could not be changed.%n\r\nIf the affected destination LUNs have incorrect signatures, this might cause associated disk cluster\r\nresources to remain offline.%n\r\n%1\r\n
0x00003059 | The following destination LUN could not be restarted after the LUN resynchronization operation.  Retry the operation.%n\r\n%n\r\nLUN ID\t\t\t%1%n\r\n%n\r\nVersion\t\t\t%2%n\r\nDevice Type\t\t%3%n\r\nDevice TypeModifier\t%4%n\r\nCommand Queueing\t%5%n\r\nBus Type\t\t%6%n\r\nVendor Id\t\t%7%n\r\nProduct Id\t\t%8%n\r\nProduct Revision\t\t%9%n\r\nSerial Number\t\t%10%n\r\n%n\r\nStorage Identifiers%n\r\n%11%n\r\n%n\r\n%12\r\n
0x0000305a | The LUN resynchronization operation failed because the destination disk could not be found or because\r\nanother application holds an exclusive handle to the destination LUN.%n\r\nMake sure that all applications have released their handles to the LUN and retry the operation.%n\r\n%1\r\n
0x0000305d | The LUN resynchronization operation failed because the Volume Shadow Copy Service was unable to enumerate \r\nthe cluster resources. The Cluster service returned the following error %1. Check the system event log for\r\nevents related to the Cluster service.%n\r\n%2\r\n
0x0000305f | The LUN resynchronization operation failed because one or more destination LUNs could not be\r\nplaced in maintenance mode. Check the system event log for events related to the Cluster service.%n\r\n%1\r\n
0x00003060 | The LUN resynchronization operation failed because one or more destination LUNs could not be\r\nremoved from maintenance mode. Check the system event log for events to the Cluster service.%n\r\n%1\r\n
0x00003062 | The LUN resynchronization operation failed because volume %1 on destination disk %2 is not included\r\nin the recovery set. %n\r\nInclude the missing volume and a corresponding shadow copy to the recovery set, or force the \r\nresynchronization by using the VSS_RECOVERY_NO_VOLUME_CHECK flag.%n\r\n%3\r\n
0x00003063 | Resynchronization of a Shadow Copy to a destination disk has completed.%n\r\n%n\r\nUser SID:\t\t\t%1%n\r\nUser name:\t\t\t%2%n\r\nProcess ID:\t\t\t%3%n\r\n%n\r\nProvider ID:\t\t\t%4%n\r\nSource Shadow Copy:\t\t%5%n\r\nPre-Resync Volume:\t\t%6%n\r\nPre-Resync Disk no:\t\t%7%n\r\nPost-Resync Volume:\t\t%8%n\r\nPost-Resync Disk no:\t\t%9%n\r\n
0x00003065 | The LUN resynchronization operation failed before calling the hardware provider.  As a result, some destination LUNs may be offline.  \r\nTo retry the resynchronization, bring the destination LUNs online and retry the operation.\r\n%1\r\n
0x00003066 | The LUN resynchronization operation failed during a call to the hardware provider.  The destination LUNs are in an unknown\r\nstate, and their contents should be discarded.  To retry the resynchronization, repair the destination LUNs if needed, bring\r\nthem online, and retry the operation.\r\n%1\r\n
0x00003067 | The LUN resynchronization operation failed after calling the hardware provider.  The data on the destination LUNs is\r\nprobably intact. However, the LUNs may have incorrect disk signatures.  To retry the resynchronization, recreate the destination LUNs\r\nand retry the operation.\r\n%1\r\n
0x0000a001 | ASR Warning: Failed to collect disk information for ASR Backup.\r\nReason:    Unable to obtain disk information for device %1 (Win32 error code %2).\r\n
0x0000a002 | ASR Error: Fail to exclude disk #%1.\r\nReason:    The disk contains a critical volume.\r\n
0x0000a003 | ASR Error: Fail to exclude dynamic pack.\r\nReason:    Some, but not all, dynamic disks in the pack have been marked excluded.\r\n
0x0000a004 | ASR Error: Fail to include critical Virtual Hard Disk (VHD) #%1.\r\nReason:    The specified VHD is hosted on another VHD.\r\n
0x0000a005 | ASR Error: Fail to include critical dynamic pack.\r\nReason:    The dynamic pack consists of a Virtual Hard Disk (VHD) #%1.\r\n
0x0000b001 | Select to include disk #%1 (of signature %2) for ASR restore.%0\r\n
0x0000b002 | Select to include disk #%1 (raw disk) for ASR restore.%0\r\n
0x0000b003 | Select this volume (%1) if it is a critical volume.\r\nCritical volumes are those which ASR must restore.\r\n
0x0000b004 | This is the path to the boot BCD store and the boot managers.\r\nAll the files in this directory need to be backed up.\r\n
0x0000b005 |  Disk #%1 is a virtual disk.%0\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x00000001 | Volume Shadow Copy Service initialization error: the control dispatcher cannot be started [%1].\r\n%2\r\n
0x00000002 | Volume Shadow Copy Service initialization error: the control handler cannot be registered [%1].\r\n%2\r\n
0x00000003 | Volume Shadow Copy Service initialization error: the COM library cannot be initialized [%1].\r\n%2\r\n
0x00000004 | Volume Shadow Copy Service initialization error: the COM security cannot be initialized [%1].\r\n%2\r\n
0x00000005 | Volume Shadow Copy Service initialization error: could not retrieve backup/restore privilege [%1].\r\n%2\r\n
0x00000006 | Volume Shadow Copy Service initialization error: the COM classes cannot be registered [%1].\r\n%2\r\n
0x00000007 | Volume Shadow Copy Service initialization error: [%1].\r\n%2\r\n
0x00000008 | Unexpected error when changing the SCM status of the Volume Shadow Copy Service: [%1, %2].\r\n%3\r\n
0x00000009 | Volume Shadow Copy Service information: Service starting at request of process '%1'. [%2]\r\n%3\r\n
0x0000000a | Volume Shadow Copy Service information: Volume '%1' appears as disconnected and it is\r\nignored by the service. You may want to rescan disks. [%2]\r\n%3\r\n
0x0000000b | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started.\r\nMost likely the CPU is under heavy load. [%3]\r\n%4\r\n
0x0000000c | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started.\r\nMost likely the server is in the process of shutting down or the system is out of memory. [%3]\r\n%4\r\n
0x0000000d | Volume Shadow Copy Service information: The COM Server with CLSID %1 and name %2 cannot be started. [%3]\r\n%4\r\n
0x0000000e | Volume Shadow Copy Service information: A database of hardware snapshots was created.\r\n%1\r\n
0x0000000f | The user name %1 specified in registry (%2) does not map to a real user name. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\n%3\r\n
0x00000010 | The value with name %1 specified in registry (%2) is not of type REG_DWORD. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\nValue '0' denies the username from running any VSS writer.\r\nValue '1' is used to allow it.\r\n%3\r\n
0x00000011 | The value with name %1 specified in registry (%2) of value (%3) cannot be interpreted. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\nValue '0' denies the username from running any VSS writer.\r\nValue '1' is used to allow it.\r\n%4\r\n
0x00000012 | Volume Shadow Copy Service error: The COM Server with CLSID %1 and name %2 cannot be started during Safe Mode.\r\nThe Volume Shadow Copy service cannot start while in safe mode. [%3]\r\n%4\r\n
0x00000013 | Volume Shadow Copy Service error: The EventSystem service is disabled or is attempting to start during Safe Mode.\r\nThe Volume Shadow Copy service cannot start while in safe mode.\r\nIf not in safe mode, make sure that EventSystem service is enabled.\r\nCLSID:%1 Name:%2 [%3]\r\n%4\r\n
0x00000014 | Volume Shadow Copy Service error: The Volume Shadow Copy infrastructure cannot be used during Safe Mode.\r\n%1\r\n
0x00000015 | Volume Shadow Copy Service error: Writers will not receive events since the COM+ database is corrupted.\r\nThis might happened if an error occurred during Windows setup.\r\nThe error returned from CoCreateInstance on class with CLSID %1 and Name %2 is [%3]\r\n%4\r\n
0x00000016 | Volume Shadow Copy Service error: A critical component required by the Volume Shadow Copy service is not registered.\r\nThis might happened if an error occurred during Windows setup or during installation of a Shadow Copy provider.\r\nThe error returned from CoCreateInstance on class with CLSID %1 and Name %2 is [%3].\r\n%4\r\n
0x00000017 | The value specified in registry (%1) has no name. The entry is ignored.\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\nValue '0' denies the username from running any VSS writer.\r\nValue '1' is used to allow it.\r\n%2\r\n
0x00000018 | Volume Shadow Copy Service Warning: The Volume Shadow Copy Service is shutting down\r\nand is experiencing delay while waiting for in-progress calls to complete.\r\n%1\r\n
0x00000019 | Volume Shadow Copy Service Warning: The Microsoft Shadow Copy Provider is shutting down\r\nand is experiencing delay while waiting for in-progress calls to complete.\r\n%1\r\n
0x0000001a | This machine is a Domain Controller with the Active Directory service (NTDS) stopped.\r\nBackup cannot be performed, nor can shadow copies be managed in this case.\r\nEither the NTDS must be started (net start ntds), or reboot in DSRM to enumerate shadow copies/providers/writers only.\r\n%1\r\n
0x0000001b | This machine is a Domain Controller but the Active Directory (NTDS) service is stopped.\r\nRestore cannot be performed while NTDS is stopped.\r\nEither the NTDS must be started (net start ntds), or reboot in DSRM.\r\n%1\r\n
0x0000001c | The given type for the ApplicationsBlockingRevert key (%1) is incorrect.\r\nIt must be a REG_MULTI_SZ containing a sequence of null-terminated volume GUID strings specifying volumes\r\nblocked from revert, followed by an extra null termination.\r\n%2\r\n
0x0000001d | This machine is a Domain Controller in Directory Service Restore Mode (DSRM).\r\nBackup cannot be performed in this case, please reboot out of DSRM.\r\n%1\r\n
0x0000001e | Fail to acquire Security Audit privilege.%n\r\nSecurity Audits for shadow copy creation and import will not be logged.\r\n%1\r\n
0x0000001f | Volume Shadow Copy Service Warning: A writer with name %1 and ID %2 waited %3 seconds\r\nfor in-progress calls to complete before shutting down.\r\n%4\r\n
0x00000020 | Volume Shadow Copy Service error: The VSS Coordinator class is not registered.  This may be caused\r\ndue to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000021 | Volume Shadow Copy Service error: The VSS management class is not registered.  This may be caused\r\ndue to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000022 | Volume Shadow Copy Service error: The VSS event class is not registered.  This will prevent any\r\nVSS writers from receiving events.  This may be caused due to a setup failure or as a result of an\r\napplication's installer or uninstaller.\r\n%1\r\n
0x00000024 | Volume Shadow Copy Service error: The MSXML classes are not registered.  This may be caused\r\ndue to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000025 | Volume Shadow Copy Service error: The Microsoft Shadow Copy Provider class is not registered..\r\nThis may be caused due to a setup failure or as a result of an application's installer or uninstaller.\r\n%1\r\n
0x00000026 | Volume Shadow Copy Service error:  Either the COM+ Event System service (EventSystem) or\r\nthe COM+ System Application service (COMSysApp) is disabled.  Enable the service and try\r\nagain.\r\n%1\r\n
0x00000027 | Volume Shadow Copy Service error:  The Volume Shadow Copy service (VSS) is disabled. Enable \r\nthe service and try again.\r\n%1\r\n
0x00000028 | Volume Shadow Copy Service error:  The Microsoft Software Shadow Copy Provider (SWPRV) service is\r\ndisabled.  Enable the service and try again.\r\n%1\r\n
0x0000002c | Volume Shadow Copy Service information: Disk '%1' appears as disconnected and it is\r\nrejected by the service. You may want to rescan disks. [%2]\r\n%3\r\n
0x0000002d | Volume Shadow Copy Service information: Volume '%1' appears as disconnected and it is\r\nignored by the service. You may want to rescan disks. [%2]\r\n%3\r\n
0x00000fa1 | Volume Shadow Copy Service error: Cannot find diff areas for creating shadow copies.\r\nAdd at least one NTFS drive to the system with enough free space.\r\nThe free space needed is at least %1 Mb for each volume to be shadow copied.\r\n%2\r\n
0x00000fa2 | Volume Shadow Copy Service error: Cannot create multiple shadow copies on the same volume (%1)\r\n%2\r\n
0x00000fa3 | Volume Shadow Copy Service warning: Writer received a Freeze event more than two minutes ago.\r\nThe writer is still waiting for either an Abort or a Thaw event.\r\n%1\r\n
0x00000fa4 | Volume Shadow Copy Service warning: The sector size of the diff area volume %1 cannot be larger than the sector size of the original volume %2\r\n%3\r\n
0x00001001 | Volume Shadow Copy Service error: The COM+ Admin catalog instance cannot be created [%1].\r\n%2\r\n
0x00001002 | Volume Shadow Copy Service error: Cannot install the event class %1 into the COM+ application '%2' [%3].\r\n%4\r\n
0x00001003 | Volume Shadow Copy Service error: Cannot install the component %1 into the COM+ application '%2' [%3].\r\n%4\r\n
0x00001004 | Volume Shadow Copy Service error: Cannot create service '%1' for the COM+ application '%2' [%3].\r\n%4\r\n
0x00001005 | Volume Shadow Copy Service error: Cannot obtain the collection '%1' from the COM+ catalog [%2].\r\n%3\r\n
0x00001006 | Volume Shadow Copy Service error: Cannot populate the COM+ collection '%1' [%2].\r\n%3\r\n
0x00001007 | Volume Shadow Copy Service error: Cannot get the COM+ collection key [%1].\r\n%2\r\n
0x00001008 | Volume Shadow Copy Service error: Cannot get the COM+ collection '%1' from parent [%2].\r\n%3\r\n
0x00001009 | Volume Shadow Copy Service error: Cannot save the changes for the COM+ collection [%1].\r\n%2\r\n
0x0000100a | Volume Shadow Copy Service error: Cannot create a subscription (%1,%2,%3) [%4].\r\n%5\r\n
0x0000100b | Volume Shadow Copy Service error: Cannot attach to the subscription with name (%1) [%2].\r\n%3\r\n
0x0000100c | Volume Shadow Copy Service error: Cannot remove the subscription with index %1 [%2].\r\n%3\r\n
0x0000100d | Volume Shadow Copy Service error: Cannot insert the new object into the COM+ catalog  [%1].\r\n%2\r\n
0x0000100e | Volume Shadow Copy Service error: Cannot attach the catalog object to the COM+ application [%1].\r\n%2\r\n
0x0000100f | Volume Shadow Copy Service error: Cannot attach to the subscription with name (%1) [%2].\r\n%3\r\n
0x00001010 | Volume Shadow Copy Service error: Error getting current directory [%1].\r\n%2\r\n
0x00001011 | Volume Shadow Copy Service error: Error Removing COM+ application (%1) [%2].\r\n%3\r\n
0x0000177f | Jetwriter error:  a call to Jet function %1 failed with status = %2.\r\n%3\r\n
0x00001780 | Express Writer error: failed while adding express writers from directory %1.\r\n%2\r\n
0x00001b59 | VssAdmin: %1: %2%nCommand-line: '%3'.\r\n%4\r\n
0x00002001 | Volume Shadow Copy Service error: Unexpected error calling routine %1.  hr = %2.\r\n%3\r\n
0x00002002 | Volume Shadow Copy Service error: Unexpected error querying for the IVssWriterCallback interface.  hr = %1.\r\nThis is often caused by incorrect security settings in either the writer or requestor process.\r\n%2\r\n
0x00002003 | Volume Shadow Copy Service error: Internally transferred WRITER_COMPONENTS document is invalid.\r\n%1\r\n
0x00002004 | Volume Shadow Copy Service error: No volumes in the shadow copy set.\r\n%1\r\n
0x00002005 | Volume Shadow Copy Service error: ERROR_INSUFFICIENT_BUFFER expected error.  Actual Error was [%1].\r\n%2\r\n
0x00002006 | Volume Shadow Copy Service error: Unexpected error. Final buffer for call to GetTokenInformation was size = %1, original size was %2.\r\n%3\r\n
0x00002007 | Volume Shadow Copy Service error: Unexpected error performing QueryInterface from IXMLDOMNode to IXMLDOMElement.  hr = %1.\r\n%2\r\n
0x00002008 | Volume Shadow Copy Service error: An unexpected error was encountered examining the XML document.  The document is missing the %1 element.\r\n%2\r\n
0x00002009 | Volume Shadow Copy Service error: An unexpected error was encountered examining the XML document.  The document is missing the %1 attribute.\r\n%2\r\n
0x0000200a | Volume Shadow Copy Service error: An unexpected error was encountered when QueryInterface for IDispatch was called.  hr = %1 attribute.\r\n%2\r\n
0x0000200b | Volume Shadow Copy Service error: An unexpected error was encountered cloning a document.  The cloned document has no children.\r\n%1\r\n
0x0000200c | Volume Shadow Copy Service error: An invalid XML document was returned from writer %1.\r\n%2\r\n
0x0000200d | Volume Shadow Copy Service error: An error occured calling QueryInterface from IVssCoordinator to IVssShim.  hr = %1.\r\n
0x0000200e | Volume Shadow Copy Service error: There are two writers with the identical instance id %1.\r\n%2\r\n
0x0000200f | Volume Shadow Copy Service error: An unexpected error was encountered when calling QueryInterface for IVssAsync.  hr = %1.\r\n%2\r\n
0x00002010 | Volume Shadow Copy Service error: The backup components document is NULL.\r\n%1\r\n
0x00002011 | Volume Shadow Copy Service error: The thread handle for the asynchronous thread is NULL.\r\n%1\r\n
0x00002012 | Volume Shadow Copy Service error: Unexpected error %1 was returned from WaitForSingleObject.\r\n%2\r\n
0x00002013 | Volume Shadow Copy Service error: Writer with name %1 and ID %2 attempted to subscribe in safe mode.\r\n%3\r\n
0x00002014 | Volume Shadow Copy Service: Writer with name %1 and ID %2 attempted to subscribe during setup.\r\n%3\r\n
0x00002015 | Volume Shadow Copy Service error: The process that hosts the writer with name %1 and ID %2 does not run under a user with sufficient access rights.\r\nConsider running this process under a local account which is either Local System, Administrator, Network Service, or Local Service.\r\n%3\r\n
0x00002016 | Volume Shadow Copy Service error: The shadow copy writer could not communicate with the Shadow Copy publisher.\r\nThe shadow copy publisher (for example the backup application) might have terminated during the shadow copy process.\r\nhr = %1.\r\n%2\r\n
0x00002017 | Volume Shadow Copy Service error: A component was added to the backup document that does not exist in any writer's metadata.\r\nEnsure that only actual writer components are added to the backup document.\r\n%1\r\n
0x00002018 | Volume Shadow Copy Service error: Internally transferred WRITER_METADATA document is invalid.\r\n%1\r\n
0x00002019 | Volume Shadow Copy Service error: VSS only supports multiple instances of writer\r\nwith class id %1 if the writer either does not require restore events or supplies an\r\ninstance name.\r\n%2\r\n
0x0000201a | Two instances of writer with class id %1 attempted to register with the same\r\ninstance name %2.\r\n%3\r\n
0x0000201b | Ran out of time while expanding file specification %1\%2.  This was being done\r\nfor the %3 subscriber.\r\n%4\r\n
0x0000201c | Ran out of time while deleting files.\r\n%1\r\n
0x0000201d | The Backup Components XML document was rejected. In this case the reason could be that\r\nit is not a Backup Components Document from a transportable shadow copy.\r\n%1\r\n
0x0000201e | Shadow copy has been created.%n\r\n%n\r\nUser SID:\t\t\t%1%n\r\nUser name:\t\t\t%2%n\r\nProcess ID:\t\t\t%3%n\r\nProcess image name:\t\t%4%n\r\n%n\r\nShadow Set ID:\t\t\t%5%n\r\nShadow ID:\t\t\t%6%n\r\nProvider ID:\t\t\t%7%n\r\nOriginal Machine:\t\t%8%n\r\nOriginal Volume:\t\t\t%9%n\r\nShadow device name:\t\t%10%n\r\n
0x0000201f | Hardware shadow copy imported.%n\r\n%n\r\nUser SID:\t\t\t%1%n\r\nUser name:\t\t\t%2%n\r\nProcess ID:\t\t\t%3%n\r\nProcess image name:\t\t%4%n\r\n%n\r\nShadow Set ID:\t\t\t%5%n\r\nShadow ID:\t\t\t%6%n\r\nProvider ID:\t\t\t%7%n\r\nOriginal Machine:\t\t%8%n\r\nOriginal Volume:\t\t\t%9%n\r\nShadow device name:\t\t%10%n\r\n
0x00002020 | The VSS service is shutting down due to idle timeout.\r\n%1\r\n
0x00002021 | The VSS service is shutting down due to shutdown event from the Service Control Manager.\r\n%1\r\n
0x00002022 | Ran out of time while expanding file specifications. Shadow copy optimization is partial.\r\n%1\r\n
0x00002023 | The user name %1 specified in registry (%2) is not valid, winerror %3. The entry is ignored.%n\r\nIt must have a valid username as name, be of type REG_DWORD, and value either '0' or '1'.\r\n%4\r\n
0x00002024 | Fail to parse XML file.%n\r\nReason %1%n\r\nLine %2%n\r\nPosition %3%n\r\nErrorcode %4%n\r\nProblem text %5%n\r\n%6\r\n
0x00002025 | A VSS writer has rejected an event with error %1. Changes that the writer made to the writer components while handling the event will not be available to the requester.\r\nCheck the event log for related events from the application hosting the VSS writer.\r\n%2\r\n
0x00002026 | Volume Shadow Copy Service error: Failed resolving account %1 with status %2. Check connection to domain controller and VssAccessControl registry key.\r\n%3\r\n
0x00003001 | Volume Shadow Copy Service error: Unexpected error %1.  hr = %2.\r\n%3\r\n
0x00003002 | Volume Shadow Copy Service warning: %1.  hr = %2.\r\n%3\r\n
0x00003003 | Volume Shadow Copy Service error: Error on creating/using the COM+ Writers publisher interface: %1 [%2].\r\n%3\r\n
0x00003004 | Volume Shadow Copy Service error: Error creating the Shadow Copy Provider COM class with CLSID %1 [%2].\r\n%3\r\n
0x00003005 | Volume Shadow Copy Service error: Error calling a routine on a Shadow Copy Provider %1. Routine details %2 [hr = %3].\r\n%4\r\n
0x00003006 | Volume Shadow Copy Service error: Error calling a routine on the Shadow Copy Provider %1. Routine returned E_INVALIDARG.\r\nRoutine details %2.\r\n%3\r\n
0x00003007 | Volume Shadow Copy Service error: Wrong type %1 (should be %2) for the\r\nRegistry value %3 under the key %4.\r\n%5\r\n
0x00003008 | Volume Shadow Copy Service error: The system may be low on resources.\r\nUnexpected error at background thread creation\r\n(_beginthreadex returns %1, errno = %2).\r\n%3\r\n
0x00003009 | Volume Shadow Copy Service error: The I/O writes cannot be flushed during the shadow copy creation period on volume %1.\r\nThe volume index in the shadow copy set is %2. Error details: Open[%3], Flush[%4], Release[%5], OnRun[%6].\r\n%7\r\n
0x0000300a | Volume Shadow Copy Service error: The I/O writes cannot be held during the shadow copy creation period on volume %1.\r\nThe volume index in the shadow copy set is %2. Error details: Open[%3], Flush[%4], Release[%5], OnRun[%6].\r\n%7\r\n
0x0000300b | Volume Shadow Copy Service error: One of the shadow copy providers returned an invalid number of committed shadow copies.\r\nThe expected number of committed shadow copies is %1. The detected number of committed shadow copies is %2.\r\n%3\r\n
0x0000300c | Volume Shadow Copy Service error: Writer %1 called CVssWriter::Initialize during Setup.\r\n%2\r\n
0x0000300d | Volume Shadow Copy Service error: Writer %1 did not respond to a GatherWriterStatus call.\r\n%2\r\n
0x0000300e | Volume Shadow Copy Service error: An internal inconsistency was detected in trying\r\nto contact shadow copy service writers.  Check to see that the Event Service\r\nand Volume Shadow Copy Service are operating properly.\r\n%1\r\n
0x0000300f | An error occurred calling CoSetProxyBlanket.  hr = %1\r\n%2\r\n
0x00003010 | An error occurred trying to QI the IVssWriter event object for\r\nIMultiInterfaceEventControl.  hr = %1\r\n%2\r\n
0x00003011 | Volume Shadow Copy Service error: Volume/disk not connected or not found.\r\nError context: %1.\r\n%2\r\n
0x00003012 | Database of hardware shadow copy sets is not valid.  Contents are ignored.\r\n%1\r\n
0x00003013 | Cannot save database of hardware shadow copy sets: hr = %1.\r\n%2\r\n
0x00003014 | Volume %1 appears to be invalid or dismounted during shadow copy creation.\r\n%2\r\n
0x00003015 | VSS Assert Failure: %1\r\n%2\r\n
0x00003016 | Volume Shadow Copy Service error: The shadow copy could not be committed - operation timed out.\r\nError context: %1.\r\n%2\r\n
0x00003017 | Volume Shadow Copy Service error: Unexpected error %1: %2 hr = %3.\r\n%4\r\n
0x00003018 | Database of remote shadow copy sets is not valid.  Contents are ignored.\r\n%1\r\n\r\n
0x00003019 | New database of remote shadow copy sets was created by the Volume Shadow Copy Service.\r\n%1\r\n
0x0000301a | Cannot save database of remote shadow copy sets: hr = %1.\r\n%2\r\n
0x0000301b | Database of remote shadow copies is not valid.  Contents are ignored.\r\n%1\r\n
0x0000301c | New database of remote shadow copies was created by the Volume Shadow Copy Service.\r\n%2\r\n
0x0000301d | Cannot save database of remote shadow copies: hr = %1.\r\n%2\r\n
0x0000301e | Failed to query machine %1 for shadow copies: hr = %2. Machine is skipped.\r\n%3\r\n
0x0000301f | Failed to connect to remote machine %1 for shadow copies management. Remote machine is unavailable: hr = %2.\r\nMake sure that this remote machine and the local machine are both on the network.\r\n%3\r\n
0x00003020 | Failed to connect to remote machine %1 for shadow copies management. Remote machine denies access: hr = %2.\r\nMake sure that the account running your local Volume Shadow Copy service is authorized for shadow copy management on the remote machine.\r\n%3\r\n
0x00003021 | Failed to connect to remote machine %1 for shadow copies management. Remote machine is unsupported: hr = %2.\r\nThis error indicates that the remote machine does not support shadow copies for shares. A common cause for this error\r\nis that the remote machine is running a Windows version which doesn't support this capability.\r\n%3\r\n
0x00003022 | Revert operation for volume %1 has begun.  Volume is being reverted to the shadow copy with id\r\n%2.\r\n%3\r\n
0x00003023 | Volume Shadow Copy Warning: A timeout was encountered while trying to freeze the Kernel Transaction Manager.\r\nThis means that one or more Resource Managers failed to commit within %1 seconds.  Check the System\r\nevent log for more information.\r\n%2\r\n
0x00003024 | Volume Shadow Copy Warning: A timeout was encountered while trying to thaw the Kernel Transaction Manager.\r\nThis means that the shadow-copy creation process took longer than %1 seconds.\r\n%2\r\n
0x00003025 | Volume Shadow Copy Warning: A timeout was encountered while trying to freeze the Distributed Transaction Manager.\r\nThis means that one or more Transaction Managers failed to commit within %1 seconds.  Check the event\r\nlogs for more information.\r\n%2\r\n
0x00003026 | Volume Shadow Copy Warning: A timeout was encountered while trying to thaw the Distributed Transaction Manager.\r\nThis means that the shadow-copy creation process took longer than %1 seconds.\r\n%2\r\n
0x00003027 | Volume Shadow Copy Warning: A timeout occured while trying to take the cluster resource %1 offline.\r\nThis means that taking the resource offline took longer than %2 seconds.\r\n%3\r\n
0x00003028 | Volume Shadow Copy Warning: A timeout occurred while trying to bring the cluster resource %1 online.\r\nThis means that bringing the resource offline took longer than %2 seconds.\r\n%3\r\n
0x00003029 | Volume Shadow Copy Warning: A plug-and-play devnode could not be found for the volume while\r\nattempting to restart or remove the associated device.  The function GetHiddenVolumeDevinfo failed with %1.\r\nThe operation will be continue, however some state associated with this volume may not be cleaned up.\r\n%2\r\n
0x0000302a | Volume Shadow Copy Warning: The hardware shadow-copy volume %1 disappeared unexpectedly.\r\nCheck for any event logs reported by Plug And Play, by the hardware provider, or by volsnap.\r\n%2\r\n
0x0000302b | Volume Shadow Copy: Attempt to dismount the volume failed with %1.  Check the\r\nsystem event log for more information.\r\n%2\r\n
0x0000302c | Volume Shadow Copy Warning: The provider has reported an invalid Storage Device ID structure.\r\n%1\r\n
0x0000302d | Volume Shadow Copy Warning: The provider has reported a storage identifier that is not supported by VSS.\r\n                 Codeset:     %1\r\n                 Type:          %2\r\n                 Size:           %3\r\n                 NextOffset:  %4\r\n                 Association: %5\r\n\r\nThis identifier will be skipped by VSS.\r\n%6\r\n
0x00003031 | Volume Shadow Copy Error: After restarting the device %1, Plug and Play reports that a reboot is required.  This is an\r\nunexpected situation.\r\n%3\r\n
0x00003032 | Volume Shadow Copy Error: VSS spent more than %1 seconds trying to open and flush all the volumes in the shadow-\r\ncopy set.  This caused volume %2 to timeout waiting for the hold-writes phase of shadow-copy creation.  Trying again when\r\ndisk activity is lower may solve this problem.\r\n%3\r\n
0x00003033 | Volume Shadow Copy Warning: VSS spent %1 seconds trying to open and flush the volume %2.  This might cause\r\ntimeouts while flushing other volumes in the shadow-copy set, causing the shadow-copy creation to fail.  Trying again when\r\ndisk activity is lower may solve this problem.\r\n%3\r\n
0x00003034 | Volume Shadow Copy Error: VSS waited more than %1 seconds for all volumes to be flushed.  This caused volume %2\r\nto timeout while waiting for the release-writes phase of shadow copy creation.  Trying again when disk activity is lower may\r\nsolve this problem.\r\n%3\r\n
0x00003035 | Volume Shadow Copy Warning: VSS spent %1 seconds trying to flush and hold the volume %2.  This might cause\r\nproblems when other volumes in the shadow-copy set timeout waiting for the release-writes phase, and it can cause\r\nthe shadow-copy creation to fail.  Trying again when disk activity is lower may solve this problem.\r\n%3\r\n
0x00003036 | Volume Shadow Copy Error: An error %1 was encountered while trying to initialize the Registry Writer.  This may cause\r\nfuture shadow-copy creations to fail.\r\n%2\r\n
0x00003037 | Volume Shadow Copy Error: An error %1 was encountered while Registry Writer was attempting to initialize itself.  This\r\nmay case a shadow-copy creation to fail.  Check the Application event log for any related errors.\r\n%2\r\n
0x00003038 | Volume Shadow Copy Error: An error %1 was encountered while Registry Writer was preparing the registry for a shadow\r\ncopy.  Check the Application and System event logs for any related errors.\r\n%2\r\n
0x00003039 | Volume Shadow Copy Error: The Registry Writer experienced an out-of-space condition while preparing the registry for\r\na Shadow Copy.  Check the Application and System event logs for any related errors.\r\n%1\r\n
0x0000303a | Volume Shadow Copy Error: An error %1 was encountered while trying to initialize the Registry Writer.  This may cause\r\nfuture shadow-copy creations to fail.\r\n%2\r\n
0x0000303b | Volume Shadow Copy Service error: An internal inconsistency was detected in trying\r\nto contact shadow copy service writers.  The Registry Writer failed to respond to a query\r\nfrom VSS. Check to see that the Event Service and Volume Shadow Copy Service\r\nare operating properly, and please check the Application event log for any other events.\r\n%1\r\n
0x0000303c | Volume Shadow Copy Service warning: VSS was denied access to the root of volume %1.\r\nDenying administrators from accessing volume roots can cause many unexpected failures,\r\nand will prevent VSS from functioning properly.  Check security on the volume, and try the\r\noperation again.\r\n%2\r\n
0x0000303d | Volume Shadow Copy Service warning: The writer spent too much time processing it's Freeze\r\nnotification.  This can cause this writer as well as other writers on the system time to time out\r\nand fail shadow-copy creation.\r\n%1\r\n
0x0000303e | When snapshot volume %1 was restarted in the system, the restart failed. The volume is no longer found in the system.%n\r\nTry a rescan from Diskmgmt.msc and see if the volume appears.%n\r\nIf not, try restarting the disk device then rescan.\r\n%2\r\n
0x00003040 | Fail to revert the signature of %1 .\r\n%2\r\n
0x00003041 | Failed to set the mount point %1 for volume %2, winerror %3\r\n%4\r\n
0x00003042 | Failed to set the share %1 after break, netstatus %2.\r\n%3\r\n
0x00003043 | Cannot request the shadow copy volume to be made readwrite if mask is requested.\r\n%1\r\n
0x00003044 | Cannot force signature revert if no signature revert is requested.\r\n%1\r\n
0x00003045 | The BreaksnapshotSetEx method failed because the disk signature of one or more shadow copy LUNs could not \r\nbe reverted to those of the original LUNs. If one or more original LUNs are not masked on the computer, this\r\ncan cause a disk signature collision.  Disk signatures of dynamic disks cannot be reverted.\r\n%1\r\n
0x00003046 | The requester specified the VSS_ONLUNSTATECHANGE_DO_MASK_LUNS flag when calling the BreakSnaphsotSetEx method,\r\nbut the hardware provider for this shadow copy does not implement the IVssHardwareSnapshotProviderEx interface.\r\n%1\r\n
0x00003049 | Provider %1 failed BreakSnapshotSetEx for Snapshot Set %2 with %3.\r\n%4\r\n
0x0000304a | A Shadow Copy LUN was not detected in the system and did not arrive.%n\r\n%n\r\nLUN ID\t\t\t%1%n\r\n%n\r\nVersion\t\t\t%2%n\r\nDevice Type\t\t%3%n\r\nDevice TypeModifier\t%4%n\r\nCommand Queueing\t%5%n\r\nBus Type\t\t%6%n\r\nVendor Id\t\t%7%n\r\nProduct Id\t\t%8%n\r\nProduct Revision\t\t%9%n\r\nSerial Number\t\t%10%n\r\n%n\r\nStorage Identifiers%n\r\n%11%n\r\n%n\r\n%12\r\n
0x0000304b | An expected hidden volume arrival did not complete because this LUN was not detected.%n\r\n%n\r\nLUN ID\t\t\t%1%n\r\n%n\r\nVersion\t\t\t%2%n\r\nDevice Type\t\t%3%n\r\nDevice TypeModifier\t%4%n\r\nCommand Queueing\t%5%n\r\nBus Type\t\t%6%n\r\nVendor Id\t\t%7%n\r\nProduct Id\t\t%8%n\r\nProduct Revision\t\t%9%n\r\nSerial Number\t\t%10%n\r\n%n\r\nStorage Identifiers%n\r\n%11%n\r\n%n\r\n%12\r\n
0x0000304c | An expected volume arrival did not complete because this LUN was not detected.%n\r\n%n\r\nLUN ID\t\t\t%1%n\r\n%n\r\nVersion\t\t\t%2%n\r\nDevice Type\t\t%3%n\r\nDevice TypeModifier\t%4%n\r\nCommand Queueing\t%5%n\r\nBus Type\t\t%6%n\r\nVendor Id\t\t%7%n\r\nProduct Id\t\t%8%n\r\nProduct Revision\t\t%9%n\r\nSerial Number\t\t%10%n\r\n%n\r\nStorage Identifiers%n\r\n%11%n\r\n%n\r\n%12\r\n
0x0000304e | An unhandled exception was encountered while processing a VSS writer event callback method. The VSS\r\nwriter infrastructure is in an unstable state. Restart the service or application that hosts the writer.%n\r\n%n\r\nWriter name:            %1%n\r\nWriter id:              %2%n\r\nWriter instance:        %3%n\r\nProcess command line:   %4%n\r\nProcess ID:             %5%n\r\nWriter operation:       %6%n\r\nWriter state:           %7%n\r\nException code:         %8%n\r\nException location:     %9%n\r\n
0x00003052 | The hardware provider for this shadow copy does not support LUN resynchronization.%n\r\n%1\r\n
0x00003055 | The Volume Shadow Copy Service was unable to load the provider with identifier %1. Reinstall the provider\r\nand retry the operation. If the provider still fails to load, please contact the vendor responsible\r\nfor that provider.%n\r\n%2\r\n
0x00003056 | The destination LUN could not be resynchronized from the source volume because it did not report a\r\nunique SCSI storage storage identifier of type 1, 2, 3, or 8 and association 0.%n\r\nRetry the operation with a different destination LUN.%n\r\n%1\r\n
0x00003057 | The resynchronization operation failed because the MBR signature or GPT ID of one or more of the\r\ndestination LUNs could not be changed.%n\r\nIf the affected destination LUNs have incorrect signatures, this might cause associated disk cluster\r\nresources to remain offline.%n\r\n%1\r\n
0x00003059 | The following destination LUN could not be restarted after the LUN resynchronization operation.  Retry the operation.%n\r\n%n\r\nLUN ID\t\t\t%1%n\r\n%n\r\nVersion\t\t\t%2%n\r\nDevice Type\t\t%3%n\r\nDevice TypeModifier\t%4%n\r\nCommand Queueing\t%5%n\r\nBus Type\t\t%6%n\r\nVendor Id\t\t%7%n\r\nProduct Id\t\t%8%n\r\nProduct Revision\t\t%9%n\r\nSerial Number\t\t%10%n\r\n%n\r\nStorage Identifiers%n\r\n%11%n\r\n%n\r\n%12\r\n
0x0000305a | The LUN resynchronization operation failed because the destination disk could not be found or because\r\nanother application holds an exclusive handle to the destination LUN.%n\r\nMake sure that all applications have released their handles to the LUN and retry the operation.%n\r\n%1\r\n
0x0000305d | The LUN resynchronization operation failed because the Volume Shadow Copy Service was unable to enumerate \r\nthe cluster resources. The Cluster service returned the following error %1. Check the system event log for\r\nevents related to the Cluster service.%n\r\n%2\r\n
0x0000305f | The LUN resynchronization operation failed because one or more destination LUNs could not be\r\nplaced in maintenance mode. Check the system event log for events related to the Cluster service.%n\r\n%1\r\n
0x00003060 | The LUN resynchronization operation failed because one or more destination LUNs could not be\r\nremoved from maintenance mode. Check the system event log for events to the Cluster service.%n\r\n%1\r\n
0x00003062 | The LUN resynchronization operation failed because volume %1 on destination disk %2 is not included\r\nin the recovery set. %n\r\nInclude the missing volume and a corresponding shadow copy to the recovery set, or force the \r\nresynchronization by using the VSS_RECOVERY_NO_VOLUME_CHECK flag.%n\r\n%3\r\n
0x00003063 | Resynchronization of a Shadow Copy to a destination disk has completed.%n\r\n%n\r\nUser SID:\t\t\t%1%n\r\nUser name:\t\t\t%2%n\r\nProcess ID:\t\t\t%3%n\r\nProcess image name:\t\t%4%n\r\n%n\r\nProvider ID:\t\t\t%5%n\r\nSource Shadow Copy:\t\t%6%n\r\nPre-Resync Volume:\t\t%7%n\r\nPre-Resync Disk no:\t\t%8%n\r\nPost-Resync Volume:\t\t%9%n\r\nPost-Resync Disk no:\t\t%10%n\r\n
0x00003065 | The LUN resynchronization operation failed before calling the hardware provider.  As a result, some destination LUNs may be offline.  \r\nTo retry the resynchronization, bring the destination LUNs online and retry the operation.\r\n%1\r\n
0x00003066 | The LUN resynchronization operation failed during a call to the hardware provider.  The destination LUNs are in an unknown\r\nstate, and their contents should be discarded.  To retry the resynchronization, repair the destination LUNs if needed, bring\r\nthem online, and retry the operation.\r\n%1\r\n
0x00003067 | The LUN resynchronization operation failed after calling the hardware provider.  The data on the destination LUNs is\r\nprobably intact. However, the LUNs may have incorrect disk signatures.  To retry the resynchronization, recreate the destination LUNs\r\nand retry the operation.\r\n%1\r\n
0x0000a001 | ASR Warning: Failed to collect disk information for ASR Backup.\r\nReason:    Unable to obtain disk information for device %1 (Win32 error code %2).\r\n
0x0000a002 | ASR Error: Fail to exclude disk #%1.\r\nReason:    The disk contains a critical volume.\r\n
0x0000a003 | ASR Error: Fail to exclude dynamic pack.\r\nReason:    Some, but not all, dynamic disks in the pack have been marked excluded.\r\n
0x0000a004 | ASR Error: Fail to include critical Virtual Hard Disk (VHD) #%1.\r\nReason:    The specified VHD is hosted on another VHD.\r\n
0x0000a005 | ASR Error: Fail to include critical dynamic pack.\r\nReason:    The dynamic pack consists of a Virtual Hard Disk (VHD) #%1.\r\n
0x0000b001 | Select to include disk #%1 (of signature %2) for ASR restore.%0\r\n
0x0000b002 | Select to include disk #%1 (raw disk) for ASR restore.%0\r\n
0x0000b003 | Select this volume (%1) if it is a critical volume.\r\nCritical volumes are those which ASR must restore.\r\n
0x0000b004 | This is the path to the boot BCD store and the boot managers.\r\nAll the files in this directory need to be backed up.\r\n
0x0000b005 |  Disk #%1 is a virtual disk.%0\r\n
