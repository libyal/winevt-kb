## ntdll.dll

Path: %SystemRoot%\System32\ntdll.dll

### 5.0.2195.6685

Message identifier | Message string
--- | ---
0x00000000 | STATUS_WAIT_0\r\n
0x00000001 | STATUS_WAIT_1\r\n
0x00000002 | STATUS_WAIT_2\r\n
0x00000003 | STATUS_WAIT_3\r\n
0x0000003f | STATUS_WAIT_63\r\n
0x00000080 | STATUS_ABANDONED_WAIT_0\r\n
0x000000bf | STATUS_ABANDONED_WAIT_63\r\n
0x000000c0 | STATUS_USER_APC\r\n
0x00000100 | STATUS_KERNEL_APC\r\n
0x00000101 | STATUS_ALERTED\r\n
0x00000102 | STATUS_TIMEOUT\r\n
0x00000103 | The operation that was requested is pending completion.\r\n
0x00000104 | A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.\r\n
0x00000105 | Returned by enumeration APIs to indicate more information is available to successive calls.\r\n
0x00000106 | Indicates not all privileges referenced are assigned to the caller.\r\nThis allows, for example, all privileges to be disabled without having to know exactly which privileges are assigned.\r\n
0x00000107 | Some of the information to be translated has not been translated.\r\n
0x00000108 | An open/create operation completed while an oplock break is underway.\r\n
0x00000109 | A new volume has been mounted by a file system.\r\n
0x0000010a | This success level status indicates that the transaction state already exists for the registry sub-tree,\r\nbut that a transaction commit was previously aborted.\r\nThe commit has now been completed.\r\n
0x0000010b | This indicates that a notify change request has been completed due to closing the handle\r\nwhich made the notify change request.\r\n
0x0000010c | This indicates that a notify change request is being completed and that the information\r\nis not being returned in the caller's buffer.\r\nThe caller now needs to enumerate the files to find the changes.\r\n
0x0000010d | {No Quotas}\r\nNo system quota limits are specifically set for this account.\r\n
0x0000010e | {Connect Failure on Primary Transport}\r\nAn attempt was made to connect to the remote server %hs on the primary transport, but the connection failed.\r\nThe computer WAS able to connect on a secondary transport.\r\n
0x00000110 | Page fault was a transition fault.\r\n
0x00000111 | Page fault was a demand zero fault.\r\n
0x00000112 | Page fault was a demand zero fault.\r\n
0x00000113 | Page fault was a demand zero fault.\r\n
0x00000114 | Page fault was satisfied by reading from a secondary storage device.\r\n
0x00000115 | Cached page was locked during operation.\r\n
0x00000116 | Crash dump exists in paging file.\r\n
0x00000117 | Specified buffer contains all zeros.\r\n
0x00000118 | A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.\r\n
0x00000119 | The device has succeeded a query-stop and its resource requirements have changed.\r\n
0x00000120 | The translator has translated these resources into the global space and no further translations should be performed.\r\n
0x00000121 | The directory service evaluated group memberships locally, as it was unable to contact a global catalog server.\r\n
0x00010001 | Debugger handled exception\r\n
0x00010002 | Debugger continued\r\n
0x40000000 | {Object Exists}\r\nAn attempt was made to create an object and the object name already existed.\r\n
0x40000001 | {Thread Suspended}\r\nA thread termination occurred while the thread was suspended. The thread was resumed, and termination proceeded.\r\n
0x40000002 | {Working Set Range Error}\r\nAn attempt was made to set the working set minimum or maximum to values which are outside of the allowable range.\r\n
0x40000003 | {Image Relocated}\r\nAn image file could not be mapped at the address specified in the image file. Local fixups must be performed on this image.\r\n
0x40000004 | This informational level status indicates that a specified registry sub-tree transaction state did not yet exist and had to be created.\r\n
0x40000005 | {Segment Load}\r\nA virtual DOS machine (VDM) is loading, unloading, or moving an MS-DOS or Win16 program segment image.\r\nAn exception is raised so a debugger can load, unload or track symbols and breakpoints within these 16-bit segments.\r\n
0x40000006 | {Local Session Key}\r\nA user session key was requested for a local RPC connection. The session key returned is a constant value and not unique to this connection.\r\n
0x40000007 | {Invalid Current Directory}\r\nThe process cannot switch to the startup current directory %hs.\r\nSelect OK to set current directory to %hs, or select CANCEL to exit.\r\n
0x40000008 | {Serial IOCTL Complete}\r\nA serial I/O operation was completed by another write to a serial port.\r\n(The IOCTL_SERIAL_XOFF_COUNTER reached zero.)\r\n
0x40000009 | {Registry Recovery}\r\nOne of the files containing the system's Registry data had to be recovered by use of a log or alternate copy.\r\nThe recovery was successful.\r\n
0x4000000a | {Redundant Read}\r\nTo satisfy a read request, the NT fault-tolerant file system successfully read the requested data from a redundant copy.\r\nThis was done because the file system encountered a failure on a member of the fault-tolerant volume,\r\nbut was unable to reassign the failing area of the device.\r\n
0x4000000b | {Redundant Write}\r\nTo satisfy a write request, the NT fault-tolerant file system successfully wrote a redundant copy of the information.\r\nThis was done because the file system encountered a failure on a member of the fault-tolerant volume,\r\nbut was not able to reassign the failing area of the device.\r\n
0x4000000c | {Serial IOCTL Timeout}\r\nA serial I/O operation completed because the time-out period expired.\r\n(The IOCTL_SERIAL_XOFF_COUNTER had not reached zero.)\r\n
0x4000000d | {Password Too Complex}\r\nThe Windows password is too complex to be converted to a LAN Manager password.\r\nThe LAN Manager password returned is a NULL string.\r\n
0x4000000e | {Machine Type Mismatch}\r\nThe image file %hs is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.\r\n
0x4000000f | {Partial Data Received}\r\nThe network transport returned partial data to its client. The remaining data will be sent later.\r\n
0x40000010 | {Expedited Data Received}\r\nThe network transport returned data to its client that was marked as expedited by the remote system.\r\n
0x40000011 | {Partial Expedited Data Received}\r\nThe network transport returned partial data to its client and this data was marked as expedited by the remote system. The remaining data will be sent later.\r\n
0x40000012 | {TDI Event Done}\r\nThe TDI indication has completed successfully.\r\n
0x40000013 | {TDI Event Pending}\r\nThe TDI indication has entered the pending state.\r\n
0x40000014 | Checking file system on %wZ\r\n
0x40000015 | {Fatal Application Exit}\r\n%hs\r\n
0x40000016 | The specified registry key is referenced by a predefined handle.\r\n
0x40000017 | {Page Unlocked}\r\nThe page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.\r\n
0x40000018 | %hs\r\n
0x40000019 | {Page Locked}\r\nOne of the pages to lock was already locked.\r\n
0x4000001a | Application popup: %1 : %2\r\n
0x4000001b | STATUS_ALREADY_WIN32\r\n
0x4000001c | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001d | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001e | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001f | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000020 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000021 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000022 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000023 | {Machine Type Mismatch}\r\nThe image file %hs is valid, but is for a machine type other than the current machine.\r\n
0x40000024 | A yield execution was performed and no thread was available to run.\r\n
0x40000025 | The resumable flag to a timer API was ignored.\r\n
0x40000026 | The arbiter has deferred arbitration of these resources to its parent\r\n
0x40000027 | The device "%hs" has detected a CardBus card in its slot, but the firmware on this system is not configured to allow the CardBus controller to be run in CardBus mode.\r\nThe operating system will currently accept only 16-bit (R2) pc-cards on this controller.\r\n
0x40000028 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000029 | The CPUs in this multiprocessor system are not all the same revision level.  To use all processors the operating system restricts itself to the features of the least capable processor in the system.  Should problems occur with this system, contact the CPU manufacturer to see if this mix of processors is supported. \r\n
0x40000294 | The system has awoken\r\n
0x40010001 | Debugger will reply later.\r\n
0x40010002 | Debugger can not provide handle.\r\n
0x40010003 | Debugger terminated thread.\r\n
0x40010004 | Debugger terminated process.\r\n
0x40010005 | Debugger got control C.\r\n
0x40010006 | Debugger printerd exception on control C.\r\n
0x40010007 | Debugger recevice RIP exception.\r\n
0x40010008 | Debugger received control break.\r\n
0x40020056 | A UUID that is valid only on this computer has been allocated.\r\n
0x400200af | Some data remains to be sent in the request buffer.\r\n
0x400a0004 | The Client Drive Mapping Service Has Connected on Terminal Connection.\r\n
0x400a0005 | The Client Drive Mapping Service Has Disconnected on Terminal Connection.\r\n
0x80000001 | {EXCEPTION}\r\nGuard Page Exception\r\nA page of memory that marks the end of a data structure, such as a stack or an array, has been accessed.\r\n
0x80000002 | {EXCEPTION}\r\nAlignment Fault\r\nA datatype misalignment was detected in a load or store instruction.\r\n
0x80000003 | {EXCEPTION}\r\nBreakpoint\r\nA breakpoint has been reached.\r\n
0x80000004 | {EXCEPTION}\r\nSingle Step\r\nA single step or trace operation has just been completed.\r\n
0x80000005 | {Buffer Overflow}\r\nThe data was too large to fit into the specified buffer.\r\n
0x80000006 | {No More Files}\r\nNo more files were found which match the file specification.\r\n
0x80000007 | {Kernel Debugger Awakened}\r\nthe system debugger was awakened by an interrupt.\r\n
0x8000000a | {Handles Closed}\r\nHandles to objects have been automatically closed as a result of the requested operation.\r\n
0x8000000b | {Non-Inheritable ACL}\r\nAn access control list (ACL) contains no components that can be inherited.\r\n
0x8000000c | {GUID Substitution}\r\nDuring the translation of a global identifier (GUID) to a Windows security ID (SID), no administratively-defined GUID prefix was found.\r\nA substitute prefix was used, which will not compromise system security.\r\nHowever, this may provide a more restrictive access than intended.\r\n
0x8000000d | {Partial Copy}\r\nDue to protection conflicts not all the requested bytes could be copied.\r\n
0x8000000e | {Out of Paper}\r\nThe printer is out of paper.\r\n
0x8000000f | {Device Power Is Off}\r\nThe printer power has been turned off.\r\n
0x80000010 | {Device Offline}\r\nThe printer has been taken offline.\r\n
0x80000011 | {Device Busy}\r\nThe device is currently busy.\r\n
0x80000012 | {No More EAs}\r\nNo more extended attributes (EAs) were found for the file.\r\n
0x80000013 | {Illegal EA}\r\nThe specified extended attribute (EA) name contains at least one illegal character.\r\n
0x80000014 | {Inconsistent EA List}\r\nThe extended attribute (EA) list is inconsistent.\r\n
0x80000015 | {Invalid EA Flag}\r\nAn invalid extended attribute (EA) flag was set.\r\n
0x80000016 | {Verifying Disk}\r\nThe media has changed and a verify operation is in progress so no reads or writes may be performed to the device, except those used in the verify operation.\r\n
0x80000017 | {Too Much Information}\r\nThe specified access control list (ACL) contained more information than was expected.\r\n
0x80000018 | This warning level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.\r\nThe commit has NOT been completed, but has not been rolled back either (so it may still be committed if desired).\r\n
0x8000001a | {No More Entries}\r\nNo more entries are available from an enumeration operation.\r\n
0x8000001b | {Filemark Found}\r\nA filemark was detected.\r\n
0x8000001c | {Media Changed}\r\nThe media may have changed.\r\n
0x8000001d | {I/O Bus Reset}\r\nAn I/O bus reset was detected.\r\n
0x8000001e | {End of Media}\r\nThe end of the media was encountered.\r\n
0x8000001f | Beginning of tape or partition has been detected.\r\n
0x80000020 | {Media Changed}\r\nThe media may have changed.\r\n
0x80000021 | A tape access reached a setmark.\r\n
0x80000022 | During a tape access, the end of the data written is reached.\r\n
0x80000023 | The redirector is in use and cannot be unloaded.\r\n
0x80000024 | The server is in use and cannot be unloaded.\r\n
0x80000025 | The specified connection has already been disconnected.\r\n
0x80000026 | A long jump has been executed.\r\n
0x80000288 | The device has indicated that cleaning is necessary.\r\n
0x80000289 | The device has indicated that it's door is open. Further operations require it closed and secured.\r\n
0x80010001 | Debugger did not handle the exception.\r\n
0xc0000001 | {Operation Failed}\r\nThe requested operation was unsuccessful.\r\n
0xc0000002 | {Not Implemented}\r\nThe requested operation is not implemented.\r\n
0xc0000003 | {Invalid Parameter}\r\nThe specified information class is not a valid information class for the specified object.\r\n
0xc0000004 | The specified information record length does not match the length required for the specified information class.\r\n
0xc0000005 | The instruction at "0x%08lx" referenced memory at "0x%08lx". The memory could not be "%s".\r\n
0xc0000006 | The instruction at "0x%08lx" referenced memory at "0x%08lx". The required data was not placed into memory because of an I/O error status of "0x%08lx".\r\n
0xc0000007 | The pagefile quota for the process has been exhausted.\r\n
0xc0000008 | An invalid HANDLE was specified.\r\n
0xc0000009 | An invalid initial stack was specified in a call to NtCreateThread.\r\n
0xc000000a | An invalid initial start address was specified in a call to NtCreateThread.\r\n
0xc000000b | An invalid Client ID was specified.\r\n
0xc000000c | An attempt was made to cancel or set a timer that has an associated APC and the subject thread is not the thread that originally set the timer with an associated APC routine.\r\n
0xc000000d | An invalid parameter was passed to a service or function.\r\n
0xc000000e | A device which does not exist was specified.\r\n
0xc000000f | {File Not Found}\r\nThe file %hs does not exist.\r\n
0xc0000010 | The specified request is not a valid operation for the target device.\r\n
0xc0000011 | The end-of-file marker has been reached. There is no valid data in the file beyond this marker.\r\n
0xc0000012 | {Wrong Volume}\r\nThe wrong volume is in the drive.\r\nPlease insert volume %hs into drive %hs.\r\n
0xc0000013 | {No Disk}\r\nThere is no disk in the drive.\r\nPlease insert a disk into drive %hs.\r\n
0xc0000014 | {Unknown Disk Format}\r\nThe disk in drive %hs is not formatted properly.\r\nPlease check the disk, and reformat if necessary.\r\n
0xc0000015 | {Sector Not Found}\r\nThe specified sector does not exist.\r\n
0xc0000016 | {Still Busy}\r\nThe specified I/O request packet (IRP) cannot be disposed of because the I/O operation is not complete.\r\n
0xc0000017 | {Not Enough Quota}\r\nNot enough virtual memory or paging file quota is available to complete the specified operation.\r\n
0xc0000018 | {Conflicting Address Range}\r\nThe specified address range conflicts with the address space.\r\n
0xc0000019 | Address range to unmap is not a mapped view.\r\n
0xc000001a | Virtual memory cannot be freed.\r\n
0xc000001b | Specified section cannot be deleted.\r\n
0xc000001c | An invalid system service was specified in a system service call.\r\n
0xc000001d | {EXCEPTION}\r\nIllegal Instruction\r\nAn attempt was made to execute an illegal instruction.\r\n
0xc000001e | {Invalid Lock Sequence}\r\nAn attempt was made to execute an invalid lock sequence.\r\n
0xc000001f | {Invalid Mapping}\r\nAn attempt was made to create a view for a section which is bigger than the section.\r\n
0xc0000020 | {Bad File}\r\nThe attributes of the specified mapping file for a section of memory cannot be read.\r\n
0xc0000021 | {Already Committed}\r\nThe specified address range is already committed.\r\n
0xc0000022 | {Access Denied}\r\nA process has requested access to an object, but has not been granted those access rights.\r\n
0xc0000023 | {Buffer Too Small}\r\nThe buffer is too small to contain the entry. No information has been written to the buffer.\r\n
0xc0000024 | {Wrong Type}\r\nThere is a mismatch between the type of object required by the requested operation and the type of object that is specified in the request.\r\n
0xc0000025 | {EXCEPTION}\r\nCannot Continue\r\nWindows cannot continue from this exception.\r\n
0xc0000026 | An invalid exception disposition was returned by an exception handler.\r\n
0xc0000027 | Unwind exception code.\r\n
0xc0000028 | An invalid or unaligned stack was encountered during an unwind operation.\r\n
0xc0000029 | An invalid unwind target was encountered during an unwind operation.\r\n
0xc000002a | An attempt was made to unlock a page of memory which was not locked.\r\n
0xc000002b | Device parity error on I/O operation.\r\n
0xc000002c | An attempt was made to decommit uncommitted virtual memory.\r\n
0xc000002d | An attempt was made to change the attributes on memory that has not been committed.\r\n
0xc000002e | Invalid Object Attributes specified to NtCreatePort or invalid Port Attributes specified to NtConnectPort\r\n
0xc000002f | Length of message passed to NtRequestPort or NtRequestWaitReplyPort was longer than the maximum message allowed by the port.\r\n
0xc0000030 | An invalid combination of parameters was specified.\r\n
0xc0000031 | An attempt was made to lower a quota limit below the current usage.\r\n
0xc0000032 | {Corrupt Disk}\r\nThe file system structure on the disk is corrupt and unusable.\r\nPlease run the Chkdsk utility on the volume %hs.\r\n
0xc0000033 | Object Name invalid.\r\n
0xc0000034 | Object Name not found.\r\n
0xc0000035 | Object Name already exists.\r\n
0xc0000037 | Attempt to send a message to a disconnected communication port.\r\n
0xc0000038 | An attempt was made to attach to a device that was already attached to another device.\r\n
0xc0000039 | Object Path Component was not a directory object.\r\n
0xc000003a | {Path Not Found}\r\nThe path %hs does not exist.\r\n
0xc000003b | Object Path Component was not a directory object.\r\n
0xc000003c | {Data Overrun}\r\nA data overrun error occurred.\r\n
0xc000003d | {Data Late}\r\nA data late error occurred.\r\n
0xc000003e | {Data Error}\r\nAn error in reading or writing data occurred.\r\n
0xc000003f | {Bad CRC}\r\nA cyclic redundancy check (CRC) checksum error occurred.\r\n
0xc0000040 | {Section Too Large}\r\nThe specified section is too big to map the file.\r\n
0xc0000041 | The NtConnectPort request is refused.\r\n
0xc0000042 | The type of port handle is invalid for the operation requested.\r\n
0xc0000043 | A file cannot be opened because the share access flags are incompatible.\r\n
0xc0000044 | Insufficient quota exists to complete the operation\r\n
0xc0000045 | The specified page protection was not valid.\r\n
0xc0000046 | An attempt to release a mutant object was made by a thread that was not the owner of the mutant object.\r\n
0xc0000047 | An attempt was made to release a semaphore such that its maximum count would have been exceeded.\r\n
0xc0000048 | An attempt to set a processes DebugPort or ExceptionPort was made, but a port already exists in the process.\r\n
0xc0000049 | An attempt was made to query image information on a section which does not map an image.\r\n
0xc000004a | An attempt was made to suspend a thread whose suspend count was at its maximum.\r\n
0xc000004b | An attempt was made to suspend a thread that has begun termination.\r\n
0xc000004c | An attempt was made to set the working set limit to an invalid value (minimum greater than maximum, etc).\r\n
0xc000004d | A section was created to map a file which is not compatible to an already existing section which maps the same file.\r\n
0xc000004e | A view to a section specifies a protection which is incompatible with the initial view's protection.\r\n
0xc000004f | An operation involving EAs failed because the file system does not support EAs.\r\n
0xc0000050 | An EA operation failed because EA set is too large.\r\n
0xc0000051 | An EA operation failed because the name or EA index is invalid.\r\n
0xc0000052 | The file for which EAs were requested has no EAs.\r\n
0xc0000053 | The EA is corrupt and non-readable.\r\n
0xc0000054 | A requested read/write cannot be granted due to a conflicting file lock.\r\n
0xc0000055 | A requested file lock cannot be granted due to other existing locks.\r\n
0xc0000056 | A non close operation has been requested of a file object with a delete pending.\r\n
0xc0000057 | An attempt was made to set the control attribute on a file. This attribute is not supported in the target file system.\r\n
0xc0000058 | Indicates a revision number encountered or specified is not one known by the service. It may be a more recent revision than the service is aware of.\r\n
0xc0000059 | Indicates two revision levels are incompatible.\r\n
0xc000005a | Indicates a particular Security ID may not be assigned as the owner of an object.\r\n
0xc000005b | Indicates a particular Security ID may not be assigned as the primary group of an object.\r\n
0xc000005c | An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.\r\n
0xc000005d | A mandatory group may not be disabled.\r\n
0xc000005e | There are currently no logon servers available to service the logon request.\r\n
0xc000005f | A specified logon session does not exist. It may already have been terminated.\r\n
0xc0000060 | A specified privilege does not exist.\r\n
0xc0000061 | A required privilege is not held by the client.\r\n
0xc0000062 | The name provided is not a properly formed account name.\r\n
0xc0000063 | The specified user already exists.\r\n
0xc0000064 | The specified user does not exist.\r\n
0xc0000065 | The specified group already exists.\r\n
0xc0000066 | The specified group does not exist.\r\n
0xc0000067 | The specified user account is already in the specified group account.\r\nAlso used to indicate a group cannot be deleted because it contains a member.\r\n
0xc0000068 | The specified user account is not a member of the specified group account.\r\n
0xc0000069 | Indicates the requested operation would disable or delete the last remaining administration account.\r\nThis is not allowed to prevent creating a situation in which the system cannot be administrated.\r\n
0xc000006a | When trying to update a password, this return status indicates that the value provided as the current password is not correct.\r\n
0xc000006b | When trying to update a password, this return status indicates that the value provided for the new password contains values that are not allowed in passwords.\r\n
0xc000006c | When trying to update a password, this status indicates that some password update rule has been violated. For example, the password may not meet length criteria.\r\n
0xc000006d | The attempted logon is invalid. This is either due to a bad username or authentication information.\r\n
0xc000006e | Indicates a referenced user name and authentication information are valid, but some user account restriction has prevented successful authentication (such as time-of-day restrictions).\r\n
0xc000006f | The user account has time restrictions and may not be logged onto at this time.\r\n
0xc0000070 | The user account is restricted such that it may not be used to log on from the source workstation.\r\n
0xc0000071 | The user account's password has expired.\r\n
0xc0000072 | The referenced account is currently disabled and may not be logged on to.\r\n
0xc0000073 | None of the information to be translated has been translated.\r\n
0xc0000074 | The number of LUIDs requested may not be allocated with a single allocation.\r\n
0xc0000075 | Indicates there are no more LUIDs to allocate.\r\n
0xc0000076 | Indicates the sub-authority value is invalid for the particular use.\r\n
0xc0000077 | Indicates the ACL structure is not valid.\r\n
0xc0000078 | Indicates the SID structure is not valid.\r\n
0xc0000079 | Indicates the SECURITY_DESCRIPTOR structure is not valid.\r\n
0xc000007a | Indicates the specified procedure address cannot be found in the DLL.\r\n
0xc000007b | {Bad Image}\r\nThe application or DLL %hs is not a valid Windows image. Please check this against your installation diskette.\r\n
0xc000007c | An attempt was made to reference a token that doesn't exist.\r\nThis is typically done by referencing the token associated with a thread when the thread is not impersonating a client.\r\n
0xc000007d | Indicates that an attempt to build either an inherited ACL or ACE was not successful.\r\nThis can be caused by a number of things. One of the more probable causes is the replacement of a CreatorId with an SID that didn't fit into the ACE or ACL.\r\n
0xc000007e | The range specified in NtUnlockFile was not locked.\r\n
0xc000007f | An operation failed because the disk was full.\r\n
0xc0000080 | The GUID allocation server is [already] disabled at the moment.\r\n
0xc0000081 | The GUID allocation server is [already] enabled at the moment.\r\n
0xc0000082 | Too many GUIDs were requested from the allocation server at once.\r\n
0xc0000083 | The GUIDs could not be allocated because the Authority Agent was exhausted.\r\n
0xc0000084 | The value provided was an invalid value for an identifier authority.\r\n
0xc0000085 | There are no more authority agent values available for the given identifier authority value.\r\n
0xc0000086 | An invalid volume label has been specified.\r\n
0xc0000087 | A mapped section could not be extended.\r\n
0xc0000088 | Specified section to flush does not map a data file.\r\n
0xc0000089 | Indicates the specified image file did not contain a resource section.\r\n
0xc000008a | Indicates the specified resource type cannot be found in the image file.\r\n
0xc000008b | Indicates the specified resource name cannot be found in the image file.\r\n
0xc000008c | {EXCEPTION}\r\nArray bounds exceeded.\r\n
0xc000008d | {EXCEPTION}\r\nFloating-point denormal operand.\r\n
0xc000008e | {EXCEPTION}\r\nFloating-point division by zero.\r\n
0xc000008f | {EXCEPTION}\r\nFloating-point inexact result.\r\n
0xc0000090 | {EXCEPTION}\r\nFloating-point invalid operation.\r\n
0xc0000091 | {EXCEPTION}\r\nFloating-point overflow.\r\n
0xc0000092 | {EXCEPTION}\r\nFloating-point stack check.\r\n
0xc0000093 | {EXCEPTION}\r\nFloating-point underflow.\r\n
0xc0000094 | {EXCEPTION}\r\nInteger division by zero.\r\n
0xc0000095 | {EXCEPTION}\r\nInteger overflow.\r\n
0xc0000096 | {EXCEPTION}\r\nPrivileged instruction.\r\n
0xc0000097 | An attempt was made to install more paging files than the system supports.\r\n
0xc0000098 | The volume for a file has been externally altered such that the opened file is no longer valid.\r\n
0xc0000099 | When a block of memory is allotted for future updates, such as the memory\r\nallocated to hold discretionary access control and primary group information, successive updates may exceed the amount of memory originally allotted.\r\nSince quota may already have been charged to several processes which have handles to the object, it is not reasonable to alter the size of the allocated memory.\r\nInstead, a request that requires more memory than has been allotted must fail and the STATUS_ALLOTED_SPACE_EXCEEDED error returned.\r\n
0xc000009a | Insufficient system resources exist to complete the API.\r\n
0xc000009b | An attempt has been made to open a DFS exit path control file.\r\n
0xc000009c | STATUS_DEVICE_DATA_ERROR\r\n
0xc000009d | STATUS_DEVICE_NOT_CONNECTED\r\n
0xc000009e | STATUS_DEVICE_POWER_FAILURE\r\n
0xc000009f | Virtual memory cannot be freed as base address is not the base of the region and a region size of zero was specified.\r\n
0xc00000a0 | An attempt was made to free virtual memory which is not allocated.\r\n
0xc00000a1 | The working set is not big enough to allow the requested pages to be locked.\r\n
0xc00000a2 | {Write Protect Error}\r\nThe disk cannot be written to because it is write protected.\r\nPlease remove the write protection from the volume %hs in drive %hs.\r\n
0xc00000a3 | {Drive Not Ready}\r\nThe drive is not ready for use; its door may be open.\r\nPlease check drive %hs and make sure that a disk is inserted and that the drive door is closed.\r\n
0xc00000a4 | The specified attributes are invalid, or incompatible with the attributes for the group as a whole.\r\n
0xc00000a5 | A specified impersonation level is invalid.\r\nAlso used to indicate a required impersonation level was not provided.\r\n
0xc00000a6 | An attempt was made to open an Anonymous level token.\r\nAnonymous tokens may not be opened.\r\n
0xc00000a7 | The validation information class requested was invalid.\r\n
0xc00000a8 | The type of a token object is inappropriate for its attempted use.\r\n
0xc00000a9 | The type of a token object is inappropriate for its attempted use.\r\n
0xc00000aa | An attempt was made to execute an instruction at an unaligned address and the host system does not support unaligned instruction references.\r\n
0xc00000ab | The maximum named pipe instance count has been reached.\r\n
0xc00000ac | An instance of a named pipe cannot be found in the listening state.\r\n
0xc00000ad | The named pipe is not in the connected or closing state.\r\n
0xc00000ae | The specified pipe is set to complete operations and there are current I/O operations queued so it cannot be changed to queue operations.\r\n
0xc00000af | The specified handle is not open to the server end of the named pipe.\r\n
0xc00000b0 | The specified named pipe is in the disconnected state.\r\n
0xc00000b1 | The specified named pipe is in the closing state.\r\n
0xc00000b2 | The specified named pipe is in the connected state.\r\n
0xc00000b3 | The specified named pipe is in the listening state.\r\n
0xc00000b4 | The specified named pipe is not in message mode.\r\n
0xc00000b5 | {Device Timeout}\r\nThe specified I/O operation on %hs was not completed before the time-out period expired.\r\n
0xc00000b6 | The specified file has been closed by another process.\r\n
0xc00000b7 | Profiling not started.\r\n
0xc00000b8 | Profiling not stopped.\r\n
0xc00000b9 | The passed ACL did not contain the minimum required information.\r\n
0xc00000ba | The file that was specified as a target is a directory and the caller specified that it could be anything but a directory.\r\n
0xc00000bb | The network request is not supported.\r\n
0xc00000bc | This remote computer is not listening.\r\n
0xc00000bd | A duplicate name exists on the network.\r\n
0xc00000be | The network path cannot be located.\r\n
0xc00000bf | The network is busy.\r\n
0xc00000c0 | This device does not exist.\r\n
0xc00000c1 | The network BIOS command limit has been reached.\r\n
0xc00000c2 | An I/O adapter hardware error has occurred.\r\n
0xc00000c3 | The network responded incorrectly.\r\n
0xc00000c4 | An unexpected network error occurred.\r\n
0xc00000c5 | The remote adapter is not compatible.\r\n
0xc00000c6 | The printer queue is full.\r\n
0xc00000c7 | Space to store the file waiting to be printed is not available on the server.\r\n
0xc00000c8 | The requested print file has been canceled.\r\n
0xc00000c9 | The network name was deleted.\r\n
0xc00000ca | Network access is denied.\r\n
0xc00000cb | {Incorrect Network Resource Type}\r\nThe specified device type (LPT, for example) conflicts with the actual device type on the remote resource.\r\n
0xc00000cc | {Network Name Not Found}\r\nThe specified share name cannot be found on the remote server.\r\n
0xc00000cd | The name limit for the local computer network adapter card was exceeded.\r\n
0xc00000ce | The network BIOS session limit was exceeded.\r\n
0xc00000cf | File sharing has been temporarily paused.\r\n
0xc00000d0 | No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept.\r\n
0xc00000d1 | Print or disk redirection is temporarily paused.\r\n
0xc00000d2 | A network data fault occurred.\r\n
0xc00000d3 | The number of active profiling objects is at the maximum and no more may be started.\r\n
0xc00000d4 | {Incorrect Volume}\r\nThe target file of a rename request is located on a different device than the source of the rename request.\r\n
0xc00000d5 | The file specified has been renamed and thus cannot be modified.\r\n
0xc00000d6 | {Network Request Timeout}\r\nThe session with a remote server has been disconnected because the time-out interval for a request has expired.\r\n
0xc00000d7 | Indicates an attempt was made to operate on the security of an object that does not have security associated with it.\r\n
0xc00000d8 | Used to indicate that an operation cannot continue without blocking for I/O.\r\n
0xc00000d9 | Used to indicate that a read operation was done on an empty pipe.\r\n
0xc00000da | Configuration information could not be read from the domain controller, either because the machine is unavailable, or access has been denied.\r\n
0xc00000db | Indicates that a thread attempted to terminate itself by default (called NtTerminateThread with NULL) and it was the last thread in the current process.\r\n
0xc00000dc | Indicates the Sam Server was in the wrong state to perform the desired operation.\r\n
0xc00000dd | Indicates the Domain was in the wrong state to perform the desired operation.\r\n
0xc00000de | This operation is only allowed for the Primary Domain Controller of the domain.\r\n
0xc00000df | The specified Domain did not exist.\r\n
0xc00000e0 | The specified Domain already exists.\r\n
0xc00000e1 | An attempt was made to exceed the limit on the number of domains per server for this release.\r\n
0xc00000e2 | Error status returned when oplock request is denied.\r\n
0xc00000e3 | Error status returned when an invalid oplock acknowledgment is received by a file system.\r\n
0xc00000e4 | This error indicates that the requested operation cannot be completed due to a catastrophic media failure or on-disk data structure corruption.\r\n
0xc00000e5 | An internal error occurred.\r\n
0xc00000e6 | Indicates generic access types were contained in an access mask which should already be mapped to non-generic access types.\r\n
0xc00000e7 | Indicates a security descriptor is not in the necessary format (absolute or self-relative).\r\n
0xc00000e8 | An access to a user buffer failed at an "expected" point in time.\r\nThis code is defined since the caller does not want to accept STATUS_ACCESS_VIOLATION in its filter.\r\n
0xc00000e9 | If an I/O error is returned which is not defined in the standard FsRtl filter, it is converted to the following error which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ea | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000eb | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ec | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ed | The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.\r\n
0xc00000ee | An attempt has been made to start a new session manager or LSA logon session with an ID that is already in use.\r\n
0xc00000ef | An invalid parameter was passed to a service or function as the first argument.\r\n
0xc00000f0 | An invalid parameter was passed to a service or function as the second argument.\r\n
0xc00000f1 | An invalid parameter was passed to a service or function as the third argument.\r\n
0xc00000f2 | An invalid parameter was passed to a service or function as the fourth argument.\r\n
0xc00000f3 | An invalid parameter was passed to a service or function as the fifth argument.\r\n
0xc00000f4 | An invalid parameter was passed to a service or function as the sixth argument.\r\n
0xc00000f5 | An invalid parameter was passed to a service or function as the seventh argument.\r\n
0xc00000f6 | An invalid parameter was passed to a service or function as the eighth argument.\r\n
0xc00000f7 | An invalid parameter was passed to a service or function as the ninth argument.\r\n
0xc00000f8 | An invalid parameter was passed to a service or function as the tenth argument.\r\n
0xc00000f9 | An invalid parameter was passed to a service or function as the eleventh argument.\r\n
0xc00000fa | An invalid parameter was passed to a service or function as the twelfth argument.\r\n
0xc00000fb | An attempt was made to access a network file, but the network software was not yet started.\r\n
0xc00000fc | An attempt was made to start the redirector, but the redirector has already been started.\r\n
0xc00000fd | A new guard page for the stack cannot be created.\r\n
0xc00000fe | A specified authentication package is unknown.\r\n
0xc00000ff | A malformed function table was encountered during an unwind operation.\r\n
0xc0000100 | Indicates the specified environment variable name was not found in the specified environment block.\r\n
0xc0000101 | Indicates that the directory trying to be deleted is not empty.\r\n
0xc0000102 | {Corrupt File}\r\nThe file or directory %hs is corrupt and unreadable.\r\nPlease run the Chkdsk utility.\r\n
0xc0000103 | A requested opened file is not a directory.\r\n
0xc0000104 | The logon session is not in a state that is consistent with the requested operation.\r\n
0xc0000105 | An internal LSA error has occurred. An authentication package has requested the creation of a Logon Session but the ID of an already existing Logon Session has been specified.\r\n
0xc0000106 | A specified name string is too long for its intended use.\r\n
0xc0000107 | The user attempted to force close the files on a redirected drive, but there were opened files on the drive, and the user did not specify a sufficient level of force.\r\n
0xc0000108 | The user attempted to force close the files on a redirected drive, but there were opened directories on the drive, and the user did not specify a sufficient level of force.\r\n
0xc0000109 | RtlFindMessage could not locate the requested message ID in the message table resource.\r\n
0xc000010a | An attempt was made to duplicate an object handle into or out of an exiting process.\r\n
0xc000010b | Indicates an invalid value has been provided for the LogonType requested.\r\n
0xc000010c | Indicates that an attempt was made to assign protection to a file system file or directory and one of the SIDs in the security descriptor could not be translated into a GUID that could be stored by the file system.\r\nThis causes the protection attempt to fail, which may cause a file creation attempt to fail.\r\n
0xc000010d | Indicates that an attempt has been made to impersonate via a named pipe that has not yet been read from.\r\n
0xc000010e | Indicates that the specified image is already loaded.\r\n
0xc000010f | STATUS_ABIOS_NOT_PRESENT\r\n
0xc0000110 | STATUS_ABIOS_LID_NOT_EXIST\r\n
0xc0000111 | STATUS_ABIOS_LID_ALREADY_OWNED\r\n
0xc0000112 | STATUS_ABIOS_NOT_LID_OWNER\r\n
0xc0000113 | STATUS_ABIOS_INVALID_COMMAND\r\n
0xc0000114 | STATUS_ABIOS_INVALID_LID\r\n
0xc0000115 | STATUS_ABIOS_SELECTOR_NOT_AVAILABLE\r\n
0xc0000116 | STATUS_ABIOS_INVALID_SELECTOR\r\n
0xc0000117 | Indicates that an attempt was made to change the size of the LDT for a process that has no LDT.\r\n
0xc0000118 | Indicates that an attempt was made to grow an LDT by setting its size, or that the size was not an even number of selectors.\r\n
0xc0000119 | Indicates that the starting value for the LDT information was not an integral multiple of the selector size.\r\n
0xc000011a | Indicates that the user supplied an invalid descriptor when trying to set up Ldt descriptors.\r\n
0xc000011b | The specified image file did not have the correct format. It appears to be NE format.\r\n
0xc000011c | Indicates that the transaction state of a registry sub-tree is incompatible with the requested operation.\r\nFor example, a request has been made to start a new transaction with one already in progress,\r\nor a request has been made to apply a transaction when one is not currently in progress.\r\n
0xc000011d | Indicates an error has occurred during a registry transaction commit.\r\nThe database has been left in an unknown, but probably inconsistent, state.\r\nThe state of the registry transaction is left as COMMITTING.\r\n
0xc000011e | An attempt was made to map a file of size zero with the maximum size specified as zero.\r\n
0xc000011f | Too many files are opened on a remote server.\r\nThis error should only be returned by the Windows redirector on a remote drive.\r\n
0xc0000120 | The I/O request was canceled.\r\n
0xc0000121 | An attempt has been made to remove a file or directory that cannot be deleted.\r\n
0xc0000122 | Indicates a name specified as a remote computer name is syntactically invalid.\r\n
0xc0000123 | An I/O request other than close was performed on a file after it has been deleted,\r\nwhich can only happen to a request which did not complete before the last handle was closed via NtClose.\r\n
0xc0000124 | Indicates an operation has been attempted on a built-in (special) SAM account which is incompatible with built-in accounts.\r\nFor example, built-in accounts cannot be deleted.\r\n
0xc0000125 | The operation requested may not be performed on the specified group because it is a built-in special group.\r\n
0xc0000126 | The operation requested may not be performed on the specified user because it is a built-in special user.\r\n
0xc0000127 | Indicates a member cannot be removed from a group because the group is currently the member's primary group.\r\n
0xc0000128 | An I/O request other than close and several other special case operations was attempted using a file object that had already been closed.\r\n
0xc0000129 | Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token may only be performed when a process has zero or one threads.\r\n
0xc000012a | An attempt was made to operate on a thread within a specific process, but the thread specified is not in the process specified.\r\n
0xc000012b | An attempt was made to establish a token for use as a primary token but the token is already in use. A token can only be the primary token of one process at a time.\r\n
0xc000012c | Page file quota was exceeded.\r\n
0xc000012d | {Out of Virtual Memory}\r\nYour system is low on virtual memory. To ensure that Windows runs properly, increase the size of your virtual memory paging file. For more information, see Help.\r\n
0xc000012e | The specified image file did not have the correct format, it appears to be LE format.\r\n
0xc000012f | The specified image file did not have the correct format, it did not have an initial MZ.\r\n
0xc0000130 | The specified image file did not have the correct format, it did not have a proper e_lfarlc in the MZ header.\r\n
0xc0000131 | The specified image file did not have the correct format, it appears to be a 16-bit Windows image.\r\n
0xc0000132 | The Netlogon service cannot start because another Netlogon service running in the domain conflicts with the specified role.\r\n
0xc0000133 | The time at the Primary Domain Controller is different than the time at the Backup Domain Controller or member server by too large an amount.\r\n
0xc0000134 | The SAM database on a Windows Server is significantly out of synchronization with the copy on the Domain Controller. A complete synchronization is required.\r\n
0xc0000135 | {Unable To Locate DLL}\r\nThe dynamic link library %hs could not be found in the specified path %hs.\r\n
0xc0000136 | The NtCreateFile API failed. This error should never be returned to an application, it is a place holder for the Windows Lan Manager Redirector to use in its internal error mapping routines.\r\n
0xc0000137 | {Privilege Failed}\r\nThe I/O permissions for the process could not be changed.\r\n
0xc0000138 | {Ordinal Not Found}\r\nThe ordinal %ld could not be located in the dynamic link library %hs.\r\n
0xc0000139 | {Entry Point Not Found}\r\nThe procedure entry point %hs could not be located in the dynamic link library %hs.\r\n
0xc000013a | {Application Exit by CTRL+C}\r\nThe application terminated as a result of a CTRL+C.\r\n
0xc000013b | {Virtual Circuit Closed}\r\nThe network transport on your computer has closed a network connection. There may or may not be I/O requests outstanding.\r\n
0xc000013c | {Virtual Circuit Closed}\r\nThe network transport on a remote computer has closed a network connection. There may or may not be I/O requests outstanding.\r\n
0xc000013d | {Insufficient Resources on Remote Computer}\r\nThe remote computer has insufficient resources to complete the network request. For instance, there may not be enough memory available on the remote computer to carry out the request at this time.\r\n
0xc000013e | {Virtual Circuit Closed}\r\nAn existing connection (virtual circuit) has been broken at the remote computer. There is probably something wrong with the network software protocol or the network hardware on the remote computer.\r\n
0xc000013f | {Virtual Circuit Closed}\r\nThe network transport on your computer has closed a network connection because it had to wait too long for a response from the remote computer.\r\n
0xc0000140 | The connection handle given to the transport was invalid.\r\n
0xc0000141 | The address handle given to the transport was invalid.\r\n
0xc0000142 | {DLL Initialization Failed}\r\nInitialization of the dynamic link library %hs failed. The process is terminating abnormally.\r\n
0xc0000143 | {Missing System File}\r\nThe required system file %hs is bad or missing.\r\n
0xc0000144 | {Application Error}\r\nThe exception %s (0x%08lx) occurred in the application at location 0x%08lx.\r\n
0xc0000145 | {Application Error}\r\nThe application failed to initialize properly (0x%lx). Click on OK to terminate the application.\r\n
0xc0000146 | {Unable to Create Paging File}\r\nThe creation of the paging file %hs failed (%lx). The requested size was %ld.\r\n
0xc0000147 | {No Paging File Specified}\r\nNo paging file was specified in the system configuration.\r\n
0xc0000148 | {Incorrect System Call Level}\r\nAn invalid level was passed into the specified system call.\r\n
0xc0000149 | {Incorrect Password to LAN Manager Server}\r\nYou specified an incorrect password to a LAN Manager 2.x or MS-NET server.\r\n
0xc000014a | {EXCEPTION}\r\nA real-mode application issued a floating-point instruction and floating-point hardware is not present.\r\n
0xc000014b | The pipe operation has failed because the other end of the pipe has been closed.\r\n
0xc000014c | {The Registry Is Corrupt}\r\nThe structure of one of the files that contains Registry data is corrupt, or the image of the file in memory is corrupt, or the file could not be recovered because the alternate copy or log was absent or corrupt.\r\n
0xc000014d | An I/O operation initiated by the Registry failed unrecoverably.\r\nThe Registry could not read in, or write out, or flush, one of the files that contain the system's image of the Registry.\r\n
0xc000014e | An event pair synchronization operation was performed using the thread specific client/server event pair object, but no event pair object was associated with the thread.\r\n
0xc000014f | The volume does not contain a recognized file system.\r\nPlease make sure that all required file system drivers are loaded and that the volume is not corrupt.\r\n
0xc0000150 | No serial device was successfully initialized. The serial driver will unload.\r\n
0xc0000151 | The specified local group does not exist.\r\n
0xc0000152 | The specified account name is not a member of the local group.\r\n
0xc0000153 | The specified account name is already a member of the local group.\r\n
0xc0000154 | The specified local group already exists.\r\n
0xc0000155 | A requested type of logon (e.g., Interactive, Network, Service) is not granted by the target system's local security policy.\r\nPlease ask the system administrator to grant the necessary form of logon.\r\n
0xc0000156 | The maximum number of secrets that may be stored in a single system has been exceeded. The length and number of secrets is limited to satisfy United States State Department export restrictions.\r\n
0xc0000157 | The length of a secret exceeds the maximum length allowed. The length and number of secrets is limited to satisfy United States State Department export restrictions.\r\n
0xc0000158 | The Local Security Authority (LSA) database contains an internal inconsistency.\r\n
0xc0000159 | The requested operation cannot be performed in fullscreen mode.\r\n
0xc000015a | During a logon attempt, the user's security context accumulated too many security IDs. This is a very unusual situation.\r\nRemove the user from some global or local groups to reduce the number of security ids to incorporate into the security context.\r\n
0xc000015b | A user has requested a type of logon (e.g., interactive or network) that has not been granted. An administrator has control over who may logon interactively and through the network.\r\n
0xc000015c | The system has attempted to load or restore a file into the registry, and the specified file is not in the format of a registry file.\r\n
0xc000015d | An attempt was made to change a user password in the security account manager without providing the necessary Windows cross-encrypted password.\r\n
0xc000015e | A Windows Server has an incorrect configuration.\r\n
0xc000015f | An attempt was made to explicitly access the secondary copy of information via a device control to the Fault Tolerance driver and the secondary copy is not present in the system.\r\n
0xc0000160 | A configuration registry node representing a driver service entry was ill-formed and did not contain required value entries.\r\n
0xc0000161 | An illegal character was encountered. For a multi-byte character set this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE.\r\n
0xc0000162 | No mapping for the Unicode character exists in the target multi-byte code page.\r\n
0xc0000163 | The Unicode character is not defined in the Unicode character set installed on the system.\r\n
0xc0000164 | The paging file cannot be created on a floppy diskette.\r\n
0xc0000165 | {Floppy Disk Error}\r\nWhile accessing a floppy disk, an ID address mark was not found.\r\n
0xc0000166 | {Floppy Disk Error}\r\nWhile accessing a floppy disk, the track address from the sector ID field was found to be different than the track address maintained by the controller.\r\n
0xc0000167 | {Floppy Disk Error}\r\nThe floppy disk controller reported an error that is not recognized by the floppy disk driver.\r\n
0xc0000168 | {Floppy Disk Error}\r\nWhile accessing a floppy-disk, the controller returned inconsistent results via its registers.\r\n
0xc0000169 | {Hard Disk Error}\r\nWhile accessing the hard disk, a recalibrate operation failed, even after retries.\r\n
0xc000016a | {Hard Disk Error}\r\nWhile accessing the hard disk, a disk operation failed even after retries.\r\n
0xc000016b | {Hard Disk Error}\r\nWhile accessing the hard disk, a disk controller reset was needed, but even that failed.\r\n
0xc000016c | An attempt was made to open a device that was sharing an IRQ with other devices.\r\nAt least one other device that uses that IRQ was already opened.\r\nTwo concurrent opens of devices that share an IRQ and only work via interrupts is not supported for the particular bus type that the devices use.\r\n
0xc000016d | {FT Orphaning}\r\nA disk that is part of a fault-tolerant volume can no longer be accessed.\r\n
0xc000016e | The system bios failed to connect a system interrupt to the device or bus for\r\nwhich the device is connected.\r\n
0xc0000172 | Tape could not be partitioned.\r\n
0xc0000173 | When accessing a new tape of a multivolume partition, the current blocksize is incorrect.\r\n
0xc0000174 | Tape partition information could not be found when loading a tape.\r\n
0xc0000175 | Attempt to lock the eject media mechanism fails.\r\n
0xc0000176 | Unload media fails.\r\n
0xc0000177 | Physical end of tape was detected.\r\n
0xc0000178 | {No Media}\r\nThere is no media in the drive.\r\nPlease insert media into drive %hs.\r\n
0xc000017a | A member could not be added to or removed from the local group because the member does not exist.\r\n
0xc000017b | A new member could not be added to a local group because the member has the wrong account type.\r\n
0xc000017c | Illegal operation attempted on a registry key which has been marked for deletion.\r\n
0xc000017d | System could not allocate required space in a registry log.\r\n
0xc000017e | Too many Sids have been specified.\r\n
0xc000017f | An attempt was made to change a user password in the security account manager without providing the necessary LM cross-encrypted password.\r\n
0xc0000180 | An attempt was made to create a symbolic link in a registry key that already has subkeys or values.\r\n
0xc0000181 | An attempt was made to create a Stable subkey under a Volatile parent key.\r\n
0xc0000182 | The I/O device is configured incorrectly or the configuration parameters to the driver are incorrect.\r\n
0xc0000183 | An error was detected between two drivers or within an I/O driver.\r\n
0xc0000184 | The device is not in a valid state to perform this request.\r\n
0xc0000185 | The I/O device reported an I/O error.\r\n
0xc0000186 | A protocol error was detected between the driver and the device.\r\n
0xc0000187 | This operation is only allowed for the Primary Domain Controller of the domain.\r\n
0xc0000188 | Log file space is insufficient to support this operation.\r\n
0xc0000189 | A write operation was attempted to a volume after it was dismounted.\r\n
0xc000018a | The workstation does not have a trust secret for the primary domain in the local LSA database.\r\n
0xc000018b | The SAM database on the Windows Server does not have a computer account for this workstation trust relationship.\r\n
0xc000018c | The logon request failed because the trust relationship between the primary domain and the trusted domain failed.\r\n
0xc000018d | The logon request failed because the trust relationship between this workstation and the primary domain failed.\r\n
0xc000018e | The Eventlog log file is corrupt.\r\n
0xc000018f | No Eventlog log file could be opened. The Eventlog service did not start.\r\n
0xc0000190 | The network logon failed. This may be because the validation authority can't be reached.\r\n
0xc0000191 | An attempt was made to acquire a mutant such that its maximum count would have been exceeded.\r\n
0xc0000192 | An attempt was made to logon, but the netlogon service was not started.\r\n
0xc0000193 | The user's account has expired.\r\n
0xc0000194 | {EXCEPTION}\r\nPossible deadlock condition.\r\n
0xc0000195 | The credentials supplied conflict with an existing set of credentials.\r\n
0xc0000196 | An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.\r\n
0xc0000197 | The log file has changed between reads.\r\n
0xc0000198 | The account used is an Interdomain Trust account. Use your global user account or local user account to access this server.\r\n
0xc0000199 | The account used is a Computer Account. Use your global user account or local user account to access this server.\r\n
0xc000019a | The account used is an Server Trust account. Use your global user account or local user account to access this server.\r\n
0xc000019b | The name or SID of the domain specified is inconsistent with the trust information for that domain.\r\n
0xc000019c | A volume has been accessed for which a file system driver is required that has not yet been loaded.\r\n
0xc0000202 | There is no user session key for the specified logon session.\r\n
0xc0000203 | The remote user session has been deleted.\r\n
0xc0000204 | Indicates the specified resource language ID cannot be found in the\r\nimage file.\r\n
0xc0000205 | Insufficient server resources exist to complete the request.\r\n
0xc0000206 | The size of the buffer is invalid for the specified operation.\r\n
0xc0000207 | The transport rejected the network address specified as invalid.\r\n
0xc0000208 | The transport rejected the network address specified due to an\r\ninvalid use of a wildcard.\r\n
0xc0000209 | The transport address could not be opened because all the available\r\naddresses are in use.\r\n
0xc000020a | The transport address could not be opened because it already exists.\r\n
0xc000020b | The transport address is now closed.\r\n
0xc000020c | The transport connection is now disconnected.\r\n
0xc000020d | The transport connection has been reset.\r\n
0xc000020e | The transport cannot dynamically acquire any more nodes.\r\n
0xc000020f | The transport aborted a pending transaction.\r\n
0xc0000210 | The transport timed out a request waiting for a response.\r\n
0xc0000211 | The transport did not receive a release for a pending response.\r\n
0xc0000212 | The transport did not find a transaction matching the specific\r\ntoken.\r\n
0xc0000213 | The transport had previously responded to a transaction request.\r\n
0xc0000214 | The transport does not recognized the transaction request identifier specified.\r\n
0xc0000215 | The transport does not recognize the transaction request type specified.\r\n
0xc0000216 | The transport can only process the specified request on the server side of a session.\r\n
0xc0000217 | The transport can only process the specified request on the client side of a session.\r\n
0xc0000218 | {Registry File Failure}\r\nThe registry cannot load the hive (file):\r\n%hs\r\nor its log or alternate.\r\nIt is corrupt, absent, or not writable.\r\n
0xc0000219 | {Unexpected Failure in DebugActiveProcess}\r\nAn unexpected failure occurred while processing a DebugActiveProcess API request. You may choose OK to terminate the process, or Cancel to ignore the error.\r\n
0xc000021a | {Fatal System Error}\r\nThe %hs system process terminated unexpectedly\r\nwith a status of 0x%08x (0x%08x 0x%08x).\r\nThe system has been shut down.\r\n
0xc000021b | {Data Not Accepted}\r\nThe TDI client could not handle the data received during an indication.\r\n
0xc000021c | {Unable to Retrieve Browser Server List}\r\nThe list of servers for this workgroup is not currently available.\r\n
0xc000021d | NTVDM encountered a hard error.\r\n
0xc000021e | {Cancel Timeout}\r\nThe driver %hs failed to complete a cancelled I/O request in the allotted time.\r\n
0xc000021f | {Reply Message Mismatch}\r\nAn attempt was made to reply to an LPC message, but the thread specified by the client ID in the message was not waiting on that message.\r\n
0xc0000220 | {Mapped View Alignment Incorrect}\r\nAn attempt was made to map a view of a file, but either the specified base address or the offset into the file were not aligned on the proper allocation granularity.\r\n
0xc0000221 | {Bad Image Checksum}\r\nThe image %hs is possibly corrupt. The header checksum does not match the computed checksum.\r\n
0xc0000222 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0xc0000223 | The parameter(s) passed to the server in the client/server shared memory\r\nwindow were invalid. Too much data may have been put in the shared memory window.\r\n
0xc0000224 | The user's password must be changed before logging on the first time.\r\n
0xc0000225 | The object was not found.\r\n
0xc0000226 | The stream is not a tiny stream.\r\n
0xc0000227 | A transaction recover failed.\r\n
0xc0000228 | The request must be handled by the stack overflow code.\r\n
0xc0000229 | A consistency check failed.\r\n
0xc000022a | The attempt to insert the ID in the index failed because the ID is already in the index.\r\n
0xc000022b | The attempt to set the object's ID failed because the object already has an ID.\r\n
0xc000022c | Internal OFS status codes indicating how an allocation operation is handled. Either it is retried after the containing onode is moved or the extent stream is converted to a large stream.\r\n
0xc000022d | The request needs to be retried.\r\n
0xc000022e | The attempt to find the object found an object matching by ID on the volume but it is out of the scope of the handle used for the operation.\r\n
0xc000022f | The bucket array must be grown. Retry transaction after doing so.\r\n
0xc0000230 | The property set specified does not exist on the object.\r\n
0xc0000231 | The user/kernel marshalling buffer has overflowed.\r\n
0xc0000232 | The supplied variant structure contains invalid data.\r\n
0xc0000233 | Could not find a domain controller for this domain.\r\n
0xc0000234 | The user account has been automatically locked because too many invalid logon attempts or password change attempts have been requested.\r\n
0xc0000235 | NtClose was called on a handle that was protected from close via NtSetInformationObject.\r\n
0xc0000236 | The transport connection attempt was refused by the remote system.\r\n
0xc0000237 | The transport connection was gracefully closed.\r\n
0xc0000238 | The transport endpoint already has an address associated with it.\r\n
0xc0000239 | An address has not yet been associated with the transport endpoint.\r\n
0xc000023a | An operation was attempted on a nonexistent transport connection.\r\n
0xc000023b | An invalid operation was attempted on an active transport connection.\r\n
0xc000023c | The remote network is not reachable by the transport.\r\n
0xc000023d | The remote system is not reachable by the transport.\r\n
0xc000023e | The remote system does not support the transport protocol.\r\n
0xc000023f | No service is operating at the destination port of the transport on the remote system.\r\n
0xc0000240 | The request was aborted.\r\n
0xc0000241 | The transport connection was aborted by the local system.\r\n
0xc0000242 | The specified buffer contains ill-formed data.\r\n
0xc0000243 | The requested operation cannot be performed on a file with a user mapped section open.\r\n
0xc0000244 | {Audit Failed}\r\nAn attempt to generate a security audit failed.\r\n
0xc0000245 | The timer resolution was not previously set by the current process.\r\n
0xc0000246 | A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.\r\n
0xc0000247 | Attempting to login during an unauthorized time of day for this account.\r\n
0xc0000248 | The account is not authorized to login from this station.\r\n
0xc0000249 | {UP/MP Image Mismatch}\r\nThe image %hs has been modified for use on a uniprocessor system, but you are running it on a multiprocessor machine.\r\nPlease reinstall the image file.\r\n
0xc0000250 | There is insufficient account information to log you on.\r\n
0xc0000251 | {Invalid DLL Entrypoint}\r\nThe dynamic link library %hs is not written correctly. The stack pointer has been left in an inconsistent state.\r\nThe entrypoint should be declared as WINAPI or STDCALL. Select YES to fail the DLL load. Select NO to continue\r\nexecution. Selecting NO may cause the application to operate incorrectly.\r\n
0xc0000252 | {Invalid Service Callback Entrypoint}\r\nThe %hs service is not written correctly. The stack pointer has been left in an inconsistent state.\r\nThe callback entrypoint should be declared as WINAPI or STDCALL. Selecting OK will cause the\r\nservice to continue operation. However, the service process may operate incorrectly.\r\n
0xc0000253 | The server received the messages but did not send a reply.\r\n
0xc0000254 | The system has detected an IP address conflict with another system on the network. The local interface has been disabled.\r\nMore details are available in the system event log.\r\nConsult your network administrator to resolve the conflict.\r\n
0xc0000255 | The system has detected an IP address conflict with another system on the network. Network operations on this system may be disrupted as a result.\r\nMore details are available in the system event log.\r\nConsult your network administrator immediately to resolve the conflict.\r\n
0xc0000256 | {Low On Registry Space}\r\nYour maximum registry size is too small. To ensure that Windows runs properly, increase your maximum registry size. For more information, see Help.\r\n
0xc0000257 | The contacted server does not support the indicated part of the DFS namespace.\r\n
0xc0000258 | A callback return system service cannot be executed when no callback is active.\r\n
0xc0000259 | The service being accessed is licensed for a particular number of connections.\r\nNo more connections can be made to the service at this time because there are already as many connections as the service can accept.\r\n
0xc000025a | The password provided is too short to meet the policy of your user account.\r\nPlease choose a longer password.\r\n
0xc000025b | The policy of your user account does not allow you to change passwords too frequently.\r\nThis is done to prevent users from changing back to a familiar, but potentially discovered, password.\r\nIf you feel your password has been compromised then please contact your administrator immediately to have a new one assigned.\r\n
0xc000025c | You have attempted to change your password to one that you have used in the past.\r\nThe policy of your user account does not allow this. Please select a password that you have not previously used.\r\n
0xc000025e | You have attempted to load a legacy device driver while its device instance had been disabled.\r\n
0xc000025f | The specified compression format is unsupported.\r\n
0xc0000260 | The specified hardware profile configuration is invalid.\r\n
0xc0000261 | The specified Plug and Play registry device path is invalid.\r\n
0xc0000262 | {Driver Entry Point Not Found}\r\nThe %hs device driver could not locate the ordinal %ld in driver %hs.\r\n
0xc0000263 | {Driver Entry Point Not Found}\r\nThe %hs device driver could not locate the entry point %hs in driver %hs.\r\n
0xc0000264 | {Application Error}\r\nThe application attempted to release a resource it did not own. Click on OK to terminate the application.\r\n
0xc0000265 | An attempt was made to create more links on a file than the file system supports.\r\n
0xc0000266 | The specified quota list is internally inconsistent with its descriptor.\r\n
0xc0000267 | The specified file has been relocated to offline storage.\r\n
0xc0000268 | {Windows Evaluation Notification}\r\nThe evaluation period for this installation of Windows has expired. This system will shutdown in 1 hour. To restore access to this installation of Windows, please upgrade this installation using a licensed distribution of this product.\r\n
0xc0000269 | {Illegal System DLL Relocation}\r\nThe system DLL %hs was relocated in memory. The application will not run properly.\r\nThe relocation occurred because the DLL %hs occupied an address range reserved for Windows system DLLs. The vendor supplying the DLL should be contacted for a new DLL.\r\n
0xc000026a | {License Violation}\r\nThe system has detected tampering with your registered product type. This is a violation of your software license. Tampering with product type is not permitted.\r\n
0xc000026b | {DLL Initialization Failed}\r\nThe application failed to initialize because the window station is shutting down.\r\n
0xc000026c | {Unable to Load Device Driver}\r\n%hs device driver could not be loaded.\r\nError Status was 0x%x\r\n
0xc000026d | DFS is unavailable on the contacted server.\r\n
0xc000026e | An operation was attempted to a volume after it was dismounted.\r\n
0xc000026f | An internal error occurred in the Win32 x86 emulation subsystem.\r\n
0xc0000270 | Win32 x86 emulation subsystem Floating-point stack check.\r\n
0xc0000271 | The validation process needs to continue on to the next step.\r\n
0xc0000272 | There was no match for the specified key in the index.\r\n
0xc0000273 | There are no more matches for the current index enumeration.\r\n
0xc0000275 | The NTFS file or directory is not a reparse point.\r\n
0xc0000276 | The Windows I/O reparse tag passed for the NTFS reparse point is invalid.\r\n
0xc0000277 | The Windows I/O reparse tag does not match the one present in the NTFS reparse point.\r\n
0xc0000278 | The user data passed for the NTFS reparse point is invalid.\r\n
0xc0000279 | The layered file system driver for this IO tag did not handle it when needed.\r\n
0xc0000280 | The NTFS symbolic link could not be resolved even though the initial file name is valid.\r\n
0xc0000281 | The NTFS directory is a reparse point.\r\n
0xc0000282 | The range could not be added to the range list because of a conflict.\r\n
0xc0000283 | The specified medium changer source element contains no media.\r\n
0xc0000284 | The specified medium changer destination element already contains media.\r\n
0xc0000285 | The specified medium changer element does not exist.\r\n
0xc0000286 | The specified element is contained within a magazine that is no longer present.\r\n
0xc0000287 | The device requires reinitialization due to hardware errors.\r\n
0xc000028a | The file encryption attempt failed.\r\n
0xc000028b | The file decryption attempt failed.\r\n
0xc000028c | The specified range could not be found in the range list.\r\n
0xc000028d | There is no encryption recovery policy configured for this system.\r\n
0xc000028e | The required encryption driver is not loaded for this system.\r\n
0xc000028f | The file was encrypted with a different encryption driver than is currently loaded.\r\n
0xc0000290 | There are no EFS keys defined for the user.\r\n
0xc0000291 | The specified file is not encrypted.\r\n
0xc0000292 | The specified file is not in the defined EFS export format.\r\n
0xc0000293 | The specified file is encrypted and the user does not have the ability to decrypt it.\r\n
0xc0000295 | The guid passed was not recognized as valid by a WMI data provider.\r\n
0xc0000296 | The instance name passed was not recognized as valid by a WMI data provider.\r\n
0xc0000297 | The data item id passed was not recognized as valid by a WMI data provider.\r\n
0xc0000298 | The WMI request could not be completed and should be retried.\r\n
0xc0000299 | The policy object is shared and can only be modified at the root\r\n
0xc000029a | The policy object does not exist when it should\r\n
0xc000029b | The requested policy information only lives in the Ds\r\n
0xc000029c | The volume must be upgraded to enable this feature\r\n
0xc000029d | The remote storage service is not operational at this time.\r\n
0xc000029e | The remote storage service encountered a media error.\r\n
0xc000029f | The tracking (workstation) service is not running.\r\n
0xc00002a0 | The server process is running under a SID different than that required by client.\r\n
0xc00002a1 | The specified directory service attribute or value does not exist.\r\n
0xc00002a2 | The attribute syntax specified to the directory service is invalid.\r\n
0xc00002a3 | The attribute type specified to the directory service is not defined.\r\n
0xc00002a4 | The specified directory service attribute or value already exists.\r\n
0xc00002a5 | The directory service is busy.\r\n
0xc00002a6 | The directory service is not available.\r\n
0xc00002a7 | The directory service was unable to allocate a relative identifier.\r\n
0xc00002a8 | The directory service has exhausted the pool of relative identifiers.\r\n
0xc00002a9 | The requested operation could not be performed because the directory service is not the master for that type of operation.\r\n
0xc00002aa | The directory service was unable to initialize the subsystem that allocates relative identifiers.\r\n
0xc00002ab | The requested operation did not satisfy one or more constraints associated with the class of the object.\r\n
0xc00002ac | The directory service can perform the requested operation only on a leaf object.\r\n
0xc00002ad | The directory service cannot perform the requested operation on the Relatively Defined Name (RDN) attribute of an object.\r\n
0xc00002ae | The directory service detected an attempt to modify the object class of an object.\r\n
0xc00002af | An error occurred while performing a cross domain move operation.\r\n
0xc00002b0 | Unable to Contact the Global Catalog Server.\r\n
0xc00002b1 | The requested operation requires a directory service, and none was available.\r\n
0xc00002b2 | The reparse attribute cannot be set as it is incompatible with an existing attribute.\r\n
0xc00002b3 | A group marked use for deny only  can not be enabled.\r\n
0xc00002b4 | {EXCEPTION}\r\nMultiple floating point faults.\r\n
0xc00002b5 | {EXCEPTION}\r\nMultiple floating point traps.\r\n
0xc00002b6 | The device has been removed.\r\n
0xc00002b7 | The volume change journal is being deleted.\r\n
0xc00002b8 | The volume change journal service is not active.\r\n
0xc00002b9 | The requested interface is not supported.\r\n
0xc00002c1 | A directory service resource limit has been exceeded.\r\n
0xc00002c2 | {System Standby Failed}\r\nThe driver %hs does not support standby mode. Updating this\r\ndriver may allow the system to go to standby mode.  \r\n
0xc00002c3 | Mutual Authentication failed. The server's password is out of date at the domain controller.\r\n
0xc00002c4 | The system file %1 has become corrupt and has been replaced.\r\n
0xc00002c5 | {EXCEPTION}\r\nAlignment Error\r\nA datatype misalignment error was detected in a load or store instruction.\r\n
0xc00002c6 | The WMI data item or data block is read only.\r\n
0xc00002c7 | The WMI data item or data block could not be changed.\r\n
0xc00002c8 | {Virtual Memory Minimum Too Low}\r\nYour system is low on virtual memory. Windows is increasing the size of your virtual memory paging file. \r\nDuring this process, memory requests for some applications may be denied. For more information, see Help.\r\n
0xc00002c9 | {EXCEPTION}\r\nRegister NaT consumption faults.\r\nA NaT value is consumed on a non speculative instruction.\r\n
0xc00002ca | The medium changer's transport element contains media, which is causing the operation to fail.\r\n
0xc00002cb | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.\r\n
0xc00002cc | This operation is supported only when you are connected to the server.\r\n
0xc00002cd | Only an administrator can modify the membership list of an administrative group.\r\n
0xc00002ce | A device was removed so enumeration must be restarted.\r\n
0xc00002cf | The journal entry has been deleted from the journal.\r\n
0xc00002d0 | Cannot change the primary group ID of a domain controller account.\r\n
0xc00002d1 | {Fatal System Error}\r\nThe system image %s is not properly signed.\r\nThe file has been replaced with the signed file.\r\nThe system has been shut down.\r\n
0xc00002d2 | Device will not start without a reboot.\r\n
0xc00002d3 | Current device power state cannot support this request.\r\n
0xc00002d4 | The specified group type is invalid.\r\n
0xc00002d5 | In mixed domain no nesting of global group if group is security enabled.\r\n
0xc00002d6 | In mixed domain, cannot nest local groups with other local groups, if the group is security enabled.\r\n
0xc00002d7 | A global group cannot have a local group as a member.\r\n
0xc00002d8 | A global group cannot have a universal group as a member.\r\n
0xc00002d9 | A universal group cannot have a local group as a member.\r\n
0xc00002da | A global group cannot have a cross domain member.\r\n
0xc00002db | A local group cannot have another cross domain local group as a member.\r\n
0xc00002dc | Can not change to security disabled group because of having primary members in this group.\r\n
0xc00002dd | The WMI operation is not supported by the data block or method.\r\n
0xc00002de | There is not enough power to complete the requested operation.\r\n
0xc00002df | Security Account Manager needs to get the boot password.\r\n
0xc00002e0 | Security Account Manager needs to get the boot key from floppy disk.\r\n
0xc00002e1 | Directory Service can not start.\r\n
0xc00002e2 | Directory Services could not start because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.\r\n
0xc00002e3 | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Safe Mode, check the event log for more detailed information.\r\n
0xc00002e4 | The requested operation can be performed only on a global catalog server.\r\n
0xc00002e5 | A local group can only be a member of other local groups in the same domain.\r\n
0xc00002e6 | Foreign security principals cannot be members of universal groups.\r\n
0xc00002e7 | Your computer could not be joined to the domain. You have exceeded the maximum number of computer accounts you are allowed to create in this domain. Contact your system administrator to have this limit reset or increased.\r\n
0xc00002e8 | STATUS_MULTIPLE_FAULT_VIOLATION\r\n
0xc0000300 | This operation is not supported on a Microsoft Small Business Server\r\n
0xc0009898 | WOW Assertion Error.\r\n
0xc0010001 | Debugger did not perform a state change.\r\n
0xc0010002 | Debugger has found the application is not idle.\r\n
0xc0020001 | The string binding is invalid.\r\n
0xc0020002 | The binding handle is not the correct type.\r\n
0xc0020003 | The binding handle is invalid.\r\n
0xc0020004 | The RPC protocol sequence is not supported.\r\n
0xc0020005 | The RPC protocol sequence is invalid.\r\n
0xc0020006 | The string UUID is invalid.\r\n
0xc0020007 | The endpoint format is invalid.\r\n
0xc0020008 | The network address is invalid.\r\n
0xc0020009 | No endpoint was found.\r\n
0xc002000a | The timeout value is invalid.\r\n
0xc002000b | The object UUID was not found.\r\n
0xc002000c | The object UUID has already been registered.\r\n
0xc002000d | The type UUID has already been registered.\r\n
0xc002000e | The RPC server is already listening.\r\n
0xc002000f | No protocol sequences have been registered.\r\n
0xc0020010 | The RPC server is not listening.\r\n
0xc0020011 | The manager type is unknown.\r\n
0xc0020012 | The interface is unknown.\r\n
0xc0020013 | There are no bindings.\r\n
0xc0020014 | There are no protocol sequences.\r\n
0xc0020015 | The endpoint cannot be created.\r\n
0xc0020016 | Not enough resources are available to complete this operation.\r\n
0xc0020017 | The RPC server is unavailable.\r\n
0xc0020018 | The RPC server is too busy to complete this operation.\r\n
0xc0020019 | The network options are invalid.\r\n
0xc002001a | There are no remote procedure calls active on this thread.\r\n
0xc002001b | The remote procedure call failed.\r\n
0xc002001c | The remote procedure call failed and did not execute.\r\n
0xc002001d | An RPC protocol error occurred.\r\n
0xc002001f | The transfer syntax is not supported by the RPC server.\r\n
0xc0020021 | The type UUID is not supported.\r\n
0xc0020022 | The tag is invalid.\r\n
0xc0020023 | The array bounds are invalid.\r\n
0xc0020024 | The binding does not contain an entry name.\r\n
0xc0020025 | The name syntax is invalid.\r\n
0xc0020026 | The name syntax is not supported.\r\n
0xc0020028 | No network address is available to use to construct a UUID.\r\n
0xc0020029 | The endpoint is a duplicate.\r\n
0xc002002a | The authentication type is unknown.\r\n
0xc002002b | The maximum number of calls is too small.\r\n
0xc002002c | The string is too long.\r\n
0xc002002d | The RPC protocol sequence was not found.\r\n
0xc002002e | The procedure number is out of range.\r\n
0xc002002f | The binding does not contain any authentication information.\r\n
0xc0020030 | The authentication service is unknown.\r\n
0xc0020031 | The authentication level is unknown.\r\n
0xc0020032 | The security context is invalid.\r\n
0xc0020033 | The authorization service is unknown.\r\n
0xc0020034 | The entry is invalid.\r\n
0xc0020035 | The operation cannot be performed.\r\n
0xc0020036 | There are no more endpoints available from the endpoint mapper.\r\n
0xc0020037 | No interfaces have been exported.\r\n
0xc0020038 | The entry name is incomplete.\r\n
0xc0020039 | The version option is invalid.\r\n
0xc002003a | There are no more members.\r\n
0xc002003b | There is nothing to unexport.\r\n
0xc002003c | The interface was not found.\r\n
0xc002003d | The entry already exists.\r\n
0xc002003e | The entry is not found.\r\n
0xc002003f | The name service is unavailable.\r\n
0xc0020040 | The network address family is invalid.\r\n
0xc0020041 | The requested operation is not supported.\r\n
0xc0020042 | No security context is available to allow impersonation.\r\n
0xc0020043 | An internal error occurred in RPC.\r\n
0xc0020044 | The RPC server attempted an integer divide by zero.\r\n
0xc0020045 | An addressing error occurred in the RPC server.\r\n
0xc0020046 | A floating point operation at the RPC server caused a divide by zero.\r\n
0xc0020047 | A floating point underflow occurred at the RPC server.\r\n
0xc0020048 | A floating point overflow occurred at the RPC server.\r\n
0xc0020049 | A remote procedure call is already in progress for this thread.\r\n
0xc002004a | There are no more bindings.\r\n
0xc002004b | The group member was not found.\r\n
0xc002004c | The endpoint mapper database entry could not be created.\r\n
0xc002004d | The object UUID is the nil UUID.\r\n
0xc002004f | No interfaces have been registered.\r\n
0xc0020050 | The remote procedure call was cancelled.\r\n
0xc0020051 | The binding handle does not contain all required information.\r\n
0xc0020052 | A communications failure occurred during a remote procedure call.\r\n
0xc0020053 | The requested authentication level is not supported.\r\n
0xc0020054 | No principal name registered.\r\n
0xc0020055 | The error specified is not a valid Windows RPC error code.\r\n
0xc0020057 | A security package specific error occurred.\r\n
0xc0020058 | Thread is not cancelled.\r\n
0xc0020062 | Invalid asynchronous remote procedure call handle.\r\n
0xc0020063 | Invalid asynchronous RPC call handle for this operation.\r\n
0xc0030001 | The list of RPC servers available for auto-handle binding has been exhausted.\r\n
0xc0030002 | The file designated by DCERPCCHARTRANS cannot be opened.\r\n
0xc0030003 | The file containing the character translation table has fewer than 512 bytes.\r\n
0xc0030004 | A null context handle is passed as an [in] parameter.\r\n
0xc0030005 | The context handle does not match any known context handles.\r\n
0xc0030006 | The context handle changed during a call.\r\n
0xc0030007 | The binding handles passed to a remote procedure call do not match.\r\n
0xc0030008 | The stub is unable to get the call handle.\r\n
0xc0030009 | A null reference pointer was passed to the stub.\r\n
0xc003000a | The enumeration value is out of range.\r\n
0xc003000b | The byte count is too small.\r\n
0xc003000c | The stub received bad data.\r\n
0xc0030059 | Invalid operation on the encoding/decoding handle.\r\n
0xc003005a | Incompatible version of the serializing package.\r\n
0xc003005b | Incompatible version of the RPC stub.\r\n
0xc003005c | The RPC pipe object is invalid or corrupted.\r\n
0xc003005d | An invalid operation was attempted on an RPC pipe object.\r\n
0xc003005e | Unsupported RPC pipe version.\r\n
0xc003005f | The RPC pipe object has already been closed.\r\n
0xc0030060 | The RPC call completed before all pipes were processed.\r\n
0xc0030061 | No more data is available from the RPC pipe.\r\n
0xc0040035 | A device is missing in the system BIOS MPS table. This device will not be used. \r\nPlease contact your system vendor for system BIOS update.\r\n
0xc0040036 | A translator failed to translate resources.\r\n
0xc0040037 | A IRQ translator failed to translate resources.\r\n
0xc00a0001 | Session name %1 is invalid.\r\n
0xc00a0002 | The protocol driver %1 is invalid.\r\n
0xc00a0003 | The protocol driver %1 was not found in the system path.\r\n
0xc00a0006 | A close operation is pending on the Terminal Connection.\r\n
0xc00a0007 | There are no free output buffers available.\r\n
0xc00a0008 | The MODEM.INF file was not found.\r\n
0xc00a0009 | The modem (%1) was not found in MODEM.INF.\r\n
0xc00a000a | The modem did not accept the command sent to it.\r\nVerify the configured modem name matches the attached modem.\r\n
0xc00a000b | The modem did not respond to the command sent to it.\r\nVerify the modem is properly cabled and powered on.\r\n
0xc00a000c | Carrier detect has failed or carrier has been dropped due to disconnect.\r\n
0xc00a000d | Dial tone not detected within required time.\r\nVerify phone cable is properly attached and functional.\r\n
0xc00a000e | Busy signal detected at remote site on callback.\r\n
0xc00a000f | Voice detected at remote site on callback.\r\n
0xc00a0010 | Transport driver error\r\n
0xc00a0012 | The client you are using is not licensed to use this system. Your logon request is denied.\r\n
0xc00a0013 | The system has reached its licensed logon limit.\r\nPlease try again later.\r\n
0xc00a0014 | The system license has expired. Your logon request is denied.\r\n
0xc00a0015 | The specified session cannot be found.\r\n
0xc00a0016 | The specified session name is already in use.\r\n
0xc00a0017 | The requested operation cannot be completed because the Terminal Connection is currently busy processing a connect, disconnect, reset, or delete operation.\r\n
0xc00a0018 | An attempt has been made to connect to a session whose video mode is not supported by the current client.\r\n
0xc00a0022 | The application attempted to enable DOS graphics mode.\r\nDOS graphics mode is not supported.\r\n
0xc00a0024 | The requested operation can be performed only on the system console.\r\nThis is most often the result of a driver or system DLL requiring direct console access.\r\n
0xc00a0026 | The client failed to respond to the server connect message.\r\n
0xc00a0027 | Disconnecting the console session is not supported.\r\n
0xc00a0028 | Reconnecting a disconnected session to the console is not supported.\r\n
0xc00a002a | The request to control another session remotely was denied.\r\n
0xc00a002b | A process has requested access to a session, but has not been granted those access rights.\r\n
0xc00a002e | The Terminal Connection driver %1 is invalid.\r\n
0xc00a002f | The Terminal Connection driver %1 was not found in the system path.\r\n
0xc00a0030 | The requested session cannot be controlled remotely.\r\nThis may be because the session is disconnected or does not currently have a user logged on.\r\nAlso, you cannot control a session remotely from the system console or control the system console remotely.\r\nAnd you cannot remote control your own current session.\r\n
0xc00a0031 | The requested session is not configured to allow remote control.\r\n
0xc00a0032 | The RDP protocol component %2 detected an error in the protocol stream and has disconnected the client.\r\n
0xc00a0033 | Your request to connect to this Terminal server has been rejected.\r\nYour Terminal Server Client license number has not been entered for this copy of the Terminal Client.\r\nPlease call your system administrator for help in entering a valid, unique license number for this Terminal Server Client.\r\nClick OK to continue.\r\n
0xc00a0034 | Your request to connect to this Terminal server has been rejected.\r\nYour Terminal Server Client license number is currently being used by another user.\r\nPlease call your system administrator to obtain a new copy of the Terminal Server Client with a valid, unique license number.\r\nClick OK to continue.\r\n
0xc0140001 | An attempt was made to run an invalid AML opcode\r\n
0xc0140002 | The AML Interpreter Stack has overflowed\r\n
0xc0140003 | An inconsistent state has occurred\r\n
0xc0140004 | An attempt was made to access an array outside of its bounds\r\n
0xc0140005 | A required argument was not specified\r\n
0xc0140006 | A fatal error has occurred\r\n
0xc0140007 | An invalid SuperName was specified\r\n
0xc0140008 | An argument with an incorrect type was specified\r\n
0xc0140009 | An object with an incorrect type was specified\r\n
0xc014000a | A target with an incorrect type was specified\r\n
0xc014000b | An incorrect number of arguments were specified\r\n
0xc014000c | An address failed to translate\r\n
0xc014000d | An incorrect event type was specified\r\n
0xc014000e | A handler for the target already exists\r\n
0xc014000f | Invalid data for the target was specified\r\n
0xc0140010 | An invalid region for the target was specified\r\n
0xc0140011 | An attempt was made to access a field outside of the defined range\r\n
0xc0140012 | The Global system lock could not be acquired\r\n
0xc0140013 | An attempt was made to reinitialize the ACPI subsystem\r\n
0xc0140014 | The ACPI subsystem has not been initialized\r\n
0xc0140015 | An incorrect mutex was specified\r\n
0xc0140016 | The mutex is not currently owned\r\n
0xc0140017 | An attempt was made to access the mutex by a process that was not the owner\r\n
0xc0140018 | An error occurred during an access to Region Space\r\n
0xc0140019 | An attempt was made to use an incorrect table\r\n
0xc0140020 | The registration of an ACPI event failed\r\n
0xc0140021 | An ACPI Power Object failed to transition state\r\n

### 5.1.2600.5512

Message identifier | Message string
--- | ---
0x00000000 | STATUS_WAIT_0\r\n
0x00000001 | STATUS_WAIT_1\r\n
0x00000002 | STATUS_WAIT_2\r\n
0x00000003 | STATUS_WAIT_3\r\n
0x0000003f | STATUS_WAIT_63\r\n
0x00000080 | STATUS_ABANDONED_WAIT_0\r\n
0x000000bf | STATUS_ABANDONED_WAIT_63\r\n
0x000000c0 | STATUS_USER_APC\r\n
0x00000100 | STATUS_KERNEL_APC\r\n
0x00000101 | STATUS_ALERTED\r\n
0x00000102 | STATUS_TIMEOUT\r\n
0x00000103 | The operation that was requested is pending completion.\r\n
0x00000104 | A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.\r\n
0x00000105 | Returned by enumeration APIs to indicate more information is available to successive calls.\r\n
0x00000106 | Indicates not all privileges referenced are assigned to the caller.\r\nThis allows, for example, all privileges to be disabled without having to know exactly which privileges are assigned.\r\n
0x00000107 | Some of the information to be translated has not been translated.\r\n
0x00000108 | An open/create operation completed while an oplock break is underway.\r\n
0x00000109 | A new volume has been mounted by a file system.\r\n
0x0000010a | This success level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.\r\nThe commit has now been completed.\r\n
0x0000010b | This indicates that a notify change request has been completed due to closing the handle which made the notify change request.\r\n
0x0000010c | This indicates that a notify change request is being completed and that the information is not being returned in the caller's buffer.\r\nThe caller now needs to enumerate the files to find the changes.\r\n
0x0000010d | {No Quotas}\r\nNo system quota limits are specifically set for this account.\r\n
0x0000010e | {Connect Failure on Primary Transport}\r\nAn attempt was made to connect to the remote server %hs on the primary transport, but the connection failed.\r\nThe computer WAS able to connect on a secondary transport.\r\n
0x00000110 | Page fault was a transition fault.\r\n
0x00000111 | Page fault was a demand zero fault.\r\n
0x00000112 | Page fault was a demand zero fault.\r\n
0x00000113 | Page fault was a demand zero fault.\r\n
0x00000114 | Page fault was satisfied by reading from a secondary storage device.\r\n
0x00000115 | Cached page was locked during operation.\r\n
0x00000116 | Crash dump exists in paging file.\r\n
0x00000117 | Specified buffer contains all zeros.\r\n
0x00000118 | A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.\r\n
0x00000119 | The device has succeeded a query-stop and its resource requirements have changed.\r\n
0x00000120 | The translator has translated these resources into the global space and no further translations should be performed.\r\n
0x00000121 | The directory service evaluated group memberships locally, as it was unable to contact a global catalog server.\r\n
0x00000122 | A process being terminated has no threads to terminate.\r\n
0x00000123 | The specified process is not part of a job.\r\n
0x00000124 | The specified process is part of a job.\r\n
0x00000367 | An operation is blocked waiting for an oplock.\r\n
0x00010001 | Debugger handled exception\r\n
0x00010002 | Debugger continued\r\n
0x40000000 | {Object Exists}\r\nAn attempt was made to create an object and the object name already existed.\r\n
0x40000001 | {Thread Suspended}\r\nA thread termination occurred while the thread was suspended. The thread was resumed, and termination proceeded.\r\n
0x40000002 | {Working Set Range Error}\r\nAn attempt was made to set the working set minimum or maximum to values which are outside of the allowable range.\r\n
0x40000003 | {Image Relocated}\r\nAn image file could not be mapped at the address specified in the image file. Local fixups must be performed on this image.\r\n
0x40000004 | This informational level status indicates that a specified registry sub-tree transaction state did not yet exist and had to be created.\r\n
0x40000005 | {Segment Load}\r\nA virtual DOS machine (VDM) is loading, unloading, or moving an MS-DOS or Win16 program segment image.\r\nAn exception is raised so a debugger can load, unload or track symbols and breakpoints within these 16-bit segments.\r\n
0x40000006 | {Local Session Key}\r\nA user session key was requested for a local RPC connection. The session key returned is a constant value and not unique to this connection.\r\n
0x40000007 | {Invalid Current Directory}\r\nThe process cannot switch to the startup current directory %hs.\r\nSelect OK to set current directory to %hs, or select CANCEL to exit.\r\n
0x40000008 | {Serial IOCTL Complete}\r\nA serial I/O operation was completed by another write to a serial port.\r\n(The IOCTL_SERIAL_XOFF_COUNTER reached zero.)\r\n
0x40000009 | {Registry Recovery}\r\nOne of the files containing the system's Registry data had to be recovered by use of a log or alternate copy.\r\nThe recovery was successful.\r\n
0x4000000a | {Redundant Read}\r\nTo satisfy a read request, the NT fault-tolerant file system successfully read the requested data from a redundant copy.\r\nThis was done because the file system encountered a failure on a member of the fault-tolerant volume, but was unable to reassign the failing area of the device.\r\n
0x4000000b | {Redundant Write}\r\nTo satisfy a write request, the NT fault-tolerant file system successfully wrote a redundant copy of the information.\r\nThis was done because the file system encountered a failure on a member of the fault-tolerant volume, but was not able to reassign the failing area of the device.\r\n
0x4000000c | {Serial IOCTL Timeout}\r\nA serial I/O operation completed because the time-out period expired.\r\n(The IOCTL_SERIAL_XOFF_COUNTER had not reached zero.)\r\n
0x4000000d | {Password Too Complex}\r\nThe Windows password is too complex to be converted to a LAN Manager password.\r\nThe LAN Manager password returned is a NULL string.\r\n
0x4000000e | {Machine Type Mismatch}\r\nThe image file %hs is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.\r\n
0x4000000f | {Partial Data Received}\r\nThe network transport returned partial data to its client. The remaining data will be sent later.\r\n
0x40000010 | {Expedited Data Received}\r\nThe network transport returned data to its client that was marked as expedited by the remote system.\r\n
0x40000011 | {Partial Expedited Data Received}\r\nThe network transport returned partial data to its client and this data was marked as expedited by the remote system. The remaining data will be sent later.\r\n
0x40000012 | {TDI Event Done}\r\nThe TDI indication has completed successfully.\r\n
0x40000013 | {TDI Event Pending}\r\nThe TDI indication has entered the pending state.\r\n
0x40000014 | Checking file system on %wZ\r\n
0x40000015 | {Fatal Application Exit}\r\n%hs\r\n
0x40000016 | The specified registry key is referenced by a predefined handle.\r\n
0x40000017 | {Page Unlocked}\r\nThe page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.\r\n
0x40000018 | %hs\r\n
0x40000019 | {Page Locked}\r\nOne of the pages to lock was already locked.\r\n
0x4000001a | Application popup: %1 : %2\r\n
0x4000001b | STATUS_ALREADY_WIN32\r\n
0x4000001c | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001d | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001e | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001f | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000020 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000021 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000022 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000023 | {Machine Type Mismatch}\r\nThe image file %hs is valid, but is for a machine type other than the current machine.\r\n
0x40000024 | A yield execution was performed and no thread was available to run.\r\n
0x40000025 | The resumable flag to a timer API was ignored.\r\n
0x40000026 | The arbiter has deferred arbitration of these resources to its parent\r\n
0x40000027 | The device "%hs" has detected a CardBus card in its slot, but the firmware on this system is not configured to allow the CardBus controller to be run in CardBus mode.\r\nThe operating system will currently accept only 16-bit (R2) pc-cards on this controller.\r\n
0x40000028 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000029 | The CPUs in this multiprocessor system are not all the same revision level.  To use all processors the operating system restricts itself to the features of the least capable processor in the system.  Should problems occur with this system, contact\r\nthe CPU manufacturer to see if this mix of processors is supported.\r\n
0x4000002a | The system was put into hibernation.\r\n
0x4000002b | The system was resumed from hibernation.\r\n
0x40000294 | The system has awoken\r\n
0x40000370 | The Directory Service is shuting down.\r\n
0x40010001 | Debugger will reply later.\r\n
0x40010002 | Debugger can not provide handle.\r\n
0x40010003 | Debugger terminated thread.\r\n
0x40010004 | Debugger terminated process.\r\n
0x40010005 | Debugger got control C.\r\n
0x40010006 | Debugger printerd exception on control C.\r\n
0x40010007 | Debugger recevice RIP exception.\r\n
0x40010008 | Debugger received control break.\r\n
0x40020056 | A UUID that is valid only on this computer has been allocated.\r\n
0x400200af | Some data remains to be sent in the request buffer.\r\n
0x400a0004 | The Client Drive Mapping Service Has Connected on Terminal Connection.\r\n
0x400a0005 | The Client Drive Mapping Service Has Disconnected on Terminal Connection.\r\n
0x4015000d | A kernel mode component is releasing a reference on an activation context.\r\n
0x80000001 | {EXCEPTION}\r\nGuard Page Exception\r\nA page of memory that marks the end of a data structure, such as a stack or an array, has been accessed.\r\n
0x80000002 | {EXCEPTION}\r\nAlignment Fault\r\nA datatype misalignment was detected in a load or store instruction.\r\n
0x80000003 | {EXCEPTION}\r\nBreakpoint\r\nA breakpoint has been reached.\r\n
0x80000004 | {EXCEPTION}\r\nSingle Step\r\nA single step or trace operation has just been completed.\r\n
0x80000005 | {Buffer Overflow}\r\nThe data was too large to fit into the specified buffer.\r\n
0x80000006 | {No More Files}\r\nNo more files were found which match the file specification.\r\n
0x80000007 | {Kernel Debugger Awakened}\r\nthe system debugger was awakened by an interrupt.\r\n
0x8000000a | {Handles Closed}\r\nHandles to objects have been automatically closed as a result of the requested operation.\r\n
0x8000000b | {Non-Inheritable ACL}\r\nAn access control list (ACL) contains no components that can be inherited.\r\n
0x8000000c | {GUID Substitution}\r\nDuring the translation of a global identifier (GUID) to a Windows security ID (SID), no administratively-defined GUID prefix was found.\r\nA substitute prefix was used, which will not compromise system security.\r\nHowever, this may provide a more restrictive access than intended.\r\n
0x8000000d | {Partial Copy}\r\nDue to protection conflicts not all the requested bytes could be copied.\r\n
0x8000000e | {Out of Paper}\r\nThe printer is out of paper.\r\n
0x8000000f | {Device Power Is Off}\r\nThe printer power has been turned off.\r\n
0x80000010 | {Device Offline}\r\nThe printer has been taken offline.\r\n
0x80000011 | {Device Busy}\r\nThe device is currently busy.\r\n
0x80000012 | {No More EAs}\r\nNo more extended attributes (EAs) were found for the file.\r\n
0x80000013 | {Illegal EA}\r\nThe specified extended attribute (EA) name contains at least one illegal character.\r\n
0x80000014 | {Inconsistent EA List}\r\nThe extended attribute (EA) list is inconsistent.\r\n
0x80000015 | {Invalid EA Flag}\r\nAn invalid extended attribute (EA) flag was set.\r\n
0x80000016 | {Verifying Disk}\r\nThe media has changed and a verify operation is in progress so no reads or writes may be performed to the device, except those used in the verify operation.\r\n
0x80000017 | {Too Much Information}\r\nThe specified access control list (ACL) contained more information than was expected.\r\n
0x80000018 | This warning level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.\r\nThe commit has NOT been completed, but has not been rolled back either (so it may still be committed if desired).\r\n
0x8000001a | {No More Entries}\r\nNo more entries are available from an enumeration operation.\r\n
0x8000001b | {Filemark Found}\r\nA filemark was detected.\r\n
0x8000001c | {Media Changed}\r\nThe media may have changed.\r\n
0x8000001d | {I/O Bus Reset}\r\nAn I/O bus reset was detected.\r\n
0x8000001e | {End of Media}\r\nThe end of the media was encountered.\r\n
0x8000001f | Beginning of tape or partition has been detected.\r\n
0x80000020 | {Media Changed}\r\nThe media may have changed.\r\n
0x80000021 | A tape access reached a setmark.\r\n
0x80000022 | During a tape access, the end of the data written is reached.\r\n
0x80000023 | The redirector is in use and cannot be unloaded.\r\n
0x80000024 | The server is in use and cannot be unloaded.\r\n
0x80000025 | The specified connection has already been disconnected.\r\n
0x80000026 | A long jump has been executed.\r\n
0x80000027 | A cleaner cartridge is present in the tape library.\r\n
0x80000028 | The Plug and Play query operation was not successful.\r\n
0x80000029 | A frame consolidation has been executed.\r\n
0x80000288 | The device has indicated that cleaning is necessary.\r\n
0x80000289 | The device has indicated that it's door is open. Further operations require it closed and secured.\r\n
0x80010001 | Debugger did not handle the exception.\r\n
0x80130001 | The cluster node is already up.\r\n
0x80130002 | The cluster node is already down.\r\n
0x80130003 | The cluster network is already online.\r\n
0x80130004 | The cluster network is already offline.\r\n
0x80130005 | The cluster node is already a member of the cluster.\r\n
0xc0000001 | {Operation Failed}\r\nThe requested operation was unsuccessful.\r\n
0xc0000002 | {Not Implemented}\r\nThe requested operation is not implemented.\r\n
0xc0000003 | {Invalid Parameter}\r\nThe specified information class is not a valid information class for the specified object.\r\n
0xc0000004 | The specified information record length does not match the length required for the specified information class.\r\n
0xc0000005 | The instruction at "0x%08lx" referenced memory at "0x%08lx". The memory could not be "%s".\r\n
0xc0000006 | The instruction at "0x%08lx" referenced memory at "0x%08lx". The required data was not placed into memory because of an I/O error status of "0x%08lx".\r\n
0xc0000007 | The pagefile quota for the process has been exhausted.\r\n
0xc0000008 | An invalid HANDLE was specified.\r\n
0xc0000009 | An invalid initial stack was specified in a call to NtCreateThread.\r\n
0xc000000a | An invalid initial start address was specified in a call to NtCreateThread.\r\n
0xc000000b | An invalid Client ID was specified.\r\n
0xc000000c | An attempt was made to cancel or set a timer that has an associated APC and the subject thread is not the thread that originally set the timer with an associated APC routine.\r\n
0xc000000d | An invalid parameter was passed to a service or function.\r\n
0xc000000e | A device which does not exist was specified.\r\n
0xc000000f | {File Not Found}\r\nThe file %hs does not exist.\r\n
0xc0000010 | The specified request is not a valid operation for the target device.\r\n
0xc0000011 | The end-of-file marker has been reached. There is no valid data in the file beyond this marker.\r\n
0xc0000012 | {Wrong Volume}\r\nThe wrong volume is in the drive.\r\nPlease insert volume %hs into drive %hs.\r\n
0xc0000013 | {No Disk}\r\nThere is no disk in the drive.\r\nPlease insert a disk into drive %hs.\r\n
0xc0000014 | {Unknown Disk Format}\r\nThe disk in drive %hs is not formatted properly.\r\nPlease check the disk, and reformat if necessary.\r\n
0xc0000015 | {Sector Not Found}\r\nThe specified sector does not exist.\r\n
0xc0000016 | {Still Busy}\r\nThe specified I/O request packet (IRP) cannot be disposed of because the I/O operation is not complete.\r\n
0xc0000017 | {Not Enough Quota}\r\nNot enough virtual memory or paging file quota is available to complete the specified operation.\r\n
0xc0000018 | {Conflicting Address Range}\r\nThe specified address range conflicts with the address space.\r\n
0xc0000019 | Address range to unmap is not a mapped view.\r\n
0xc000001a | Virtual memory cannot be freed.\r\n
0xc000001b | Specified section cannot be deleted.\r\n
0xc000001c | An invalid system service was specified in a system service call.\r\n
0xc000001d | {EXCEPTION}\r\nIllegal Instruction\r\nAn attempt was made to execute an illegal instruction.\r\n
0xc000001e | {Invalid Lock Sequence}\r\nAn attempt was made to execute an invalid lock sequence.\r\n
0xc000001f | {Invalid Mapping}\r\nAn attempt was made to create a view for a section which is bigger than the section.\r\n
0xc0000020 | {Bad File}\r\nThe attributes of the specified mapping file for a section of memory cannot be read.\r\n
0xc0000021 | {Already Committed}\r\nThe specified address range is already committed.\r\n
0xc0000022 | {Access Denied}\r\nA process has requested access to an object, but has not been granted those access rights.\r\n
0xc0000023 | {Buffer Too Small}\r\nThe buffer is too small to contain the entry. No information has been written to the buffer.\r\n
0xc0000024 | {Wrong Type}\r\nThere is a mismatch between the type of object required by the requested operation and the type of object that is specified in the request.\r\n
0xc0000025 | {EXCEPTION}\r\nCannot Continue\r\nWindows cannot continue from this exception.\r\n
0xc0000026 | An invalid exception disposition was returned by an exception handler.\r\n
0xc0000027 | Unwind exception code.\r\n
0xc0000028 | An invalid or unaligned stack was encountered during an unwind operation.\r\n
0xc0000029 | An invalid unwind target was encountered during an unwind operation.\r\n
0xc000002a | An attempt was made to unlock a page of memory which was not locked.\r\n
0xc000002b | Device parity error on I/O operation.\r\n
0xc000002c | An attempt was made to decommit uncommitted virtual memory.\r\n
0xc000002d | An attempt was made to change the attributes on memory that has not been committed.\r\n
0xc000002e | Invalid Object Attributes specified to NtCreatePort or invalid Port Attributes specified to NtConnectPort\r\n
0xc000002f | Length of message passed to NtRequestPort or NtRequestWaitReplyPort was longer than the maximum message allowed by the port.\r\n
0xc0000030 | An invalid combination of parameters was specified.\r\n
0xc0000031 | An attempt was made to lower a quota limit below the current usage.\r\n
0xc0000032 | {Corrupt Disk}\r\nThe file system structure on the disk is corrupt and unusable.\r\nPlease run the Chkdsk utility on the volume %hs.\r\n
0xc0000033 | Object Name invalid.\r\n
0xc0000034 | Object Name not found.\r\n
0xc0000035 | Object Name already exists.\r\n
0xc0000037 | Attempt to send a message to a disconnected communication port.\r\n
0xc0000038 | An attempt was made to attach to a device that was already attached to another device.\r\n
0xc0000039 | Object Path Component was not a directory object.\r\n
0xc000003a | {Path Not Found}\r\nThe path %hs does not exist.\r\n
0xc000003b | Object Path Component was not a directory object.\r\n
0xc000003c | {Data Overrun}\r\nA data overrun error occurred.\r\n
0xc000003d | {Data Late}\r\nA data late error occurred.\r\n
0xc000003e | {Data Error}\r\nAn error in reading or writing data occurred.\r\n
0xc000003f | {Bad CRC}\r\nA cyclic redundancy check (CRC) checksum error occurred.\r\n
0xc0000040 | {Section Too Large}\r\nThe specified section is too big to map the file.\r\n
0xc0000041 | The NtConnectPort request is refused.\r\n
0xc0000042 | The type of port handle is invalid for the operation requested.\r\n
0xc0000043 | A file cannot be opened because the share access flags are incompatible.\r\n
0xc0000044 | Insufficient quota exists to complete the operation\r\n
0xc0000045 | The specified page protection was not valid.\r\n
0xc0000046 | An attempt to release a mutant object was made by a thread that was not the owner of the mutant object.\r\n
0xc0000047 | An attempt was made to release a semaphore such that its maximum count would have been exceeded.\r\n
0xc0000048 | An attempt to set a processes DebugPort or ExceptionPort was made, but a port already exists in the process.\r\n
0xc0000049 | An attempt was made to query image information on a section which does not map an image.\r\n
0xc000004a | An attempt was made to suspend a thread whose suspend count was at its maximum.\r\n
0xc000004b | An attempt was made to suspend a thread that has begun termination.\r\n
0xc000004c | An attempt was made to set the working set limit to an invalid value (minimum greater than maximum, etc).\r\n
0xc000004d | A section was created to map a file which is not compatible to an already existing section which maps the same file.\r\n
0xc000004e | A view to a section specifies a protection which is incompatible with the initial view's protection.\r\n
0xc000004f | An operation involving EAs failed because the file system does not support EAs.\r\n
0xc0000050 | An EA operation failed because EA set is too large.\r\n
0xc0000051 | An EA operation failed because the name or EA index is invalid.\r\n
0xc0000052 | The file for which EAs were requested has no EAs.\r\n
0xc0000053 | The EA is corrupt and non-readable.\r\n
0xc0000054 | A requested read/write cannot be granted due to a conflicting file lock.\r\n
0xc0000055 | A requested file lock cannot be granted due to other existing locks.\r\n
0xc0000056 | A non close operation has been requested of a file object with a delete pending.\r\n
0xc0000057 | An attempt was made to set the control attribute on a file. This attribute is not supported in the target file system.\r\n
0xc0000058 | Indicates a revision number encountered or specified is not one known by the service. It may be a more recent revision than the service is aware of.\r\n
0xc0000059 | Indicates two revision levels are incompatible.\r\n
0xc000005a | Indicates a particular Security ID may not be assigned as the owner of an object.\r\n
0xc000005b | Indicates a particular Security ID may not be assigned as the primary group of an object.\r\n
0xc000005c | An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.\r\n
0xc000005d | A mandatory group may not be disabled.\r\n
0xc000005e | There are currently no logon servers available to service the logon request.\r\n
0xc000005f | A specified logon session does not exist. It may already have been terminated.\r\n
0xc0000060 | A specified privilege does not exist.\r\n
0xc0000061 | A required privilege is not held by the client.\r\n
0xc0000062 | The name provided is not a properly formed account name.\r\n
0xc0000063 | The specified user already exists.\r\n
0xc0000064 | The specified user does not exist.\r\n
0xc0000065 | The specified group already exists.\r\n
0xc0000066 | The specified group does not exist.\r\n
0xc0000067 | The specified user account is already in the specified group account.\r\nAlso used to indicate a group cannot be deleted because it contains a member.\r\n
0xc0000068 | The specified user account is not a member of the specified group account.\r\n
0xc0000069 | Indicates the requested operation would disable or delete the last remaining administration account.\r\nThis is not allowed to prevent creating a situation in which the system cannot be administrated.\r\n
0xc000006a | When trying to update a password, this return status indicates that the value provided as the current password is not correct.\r\n
0xc000006b | When trying to update a password, this return status indicates that the value provided for the new password contains values that are not allowed in passwords.\r\n
0xc000006c | When trying to update a password, this status indicates that some password update rule has been violated. For example, the password may not meet length criteria.\r\n
0xc000006d | The attempted logon is invalid. This is either due to a bad username or authentication information.\r\n
0xc000006e | Indicates a referenced user name and authentication information are valid, but some user account restriction has prevented successful authentication (such as time-of-day restrictions).\r\n
0xc000006f | The user account has time restrictions and may not be logged onto at this time.\r\n
0xc0000070 | The user account is restricted such that it may not be used to log on from the source workstation.\r\n
0xc0000071 | The user account's password has expired.\r\n
0xc0000072 | The referenced account is currently disabled and may not be logged on to.\r\n
0xc0000073 | None of the information to be translated has been translated.\r\n
0xc0000074 | The number of LUIDs requested may not be allocated with a single allocation.\r\n
0xc0000075 | Indicates there are no more LUIDs to allocate.\r\n
0xc0000076 | Indicates the sub-authority value is invalid for the particular use.\r\n
0xc0000077 | Indicates the ACL structure is not valid.\r\n
0xc0000078 | Indicates the SID structure is not valid.\r\n
0xc0000079 | Indicates the SECURITY_DESCRIPTOR structure is not valid.\r\n
0xc000007a | Indicates the specified procedure address cannot be found in the DLL.\r\n
0xc000007b | {Bad Image}\r\nThe application or DLL %hs is not a valid Windows image. Please check this against your installation diskette.\r\n
0xc000007c | An attempt was made to reference a token that doesn't exist.\r\nThis is typically done by referencing the token associated with a thread when the thread is not impersonating a client.\r\n
0xc000007d | Indicates that an attempt to build either an inherited ACL or ACE was not successful.\r\nThis can be caused by a number of things. One of the more probable causes is the replacement of a CreatorId with an SID that didn't fit into the ACE or ACL.\r\n
0xc000007e | The range specified in NtUnlockFile was not locked.\r\n
0xc000007f | An operation failed because the disk was full.\r\n
0xc0000080 | The GUID allocation server is [already] disabled at the moment.\r\n
0xc0000081 | The GUID allocation server is [already] enabled at the moment.\r\n
0xc0000082 | Too many GUIDs were requested from the allocation server at once.\r\n
0xc0000083 | The GUIDs could not be allocated because the Authority Agent was exhausted.\r\n
0xc0000084 | The value provided was an invalid value for an identifier authority.\r\n
0xc0000085 | There are no more authority agent values available for the given identifier authority value.\r\n
0xc0000086 | An invalid volume label has been specified.\r\n
0xc0000087 | A mapped section could not be extended.\r\n
0xc0000088 | Specified section to flush does not map a data file.\r\n
0xc0000089 | Indicates the specified image file did not contain a resource section.\r\n
0xc000008a | Indicates the specified resource type cannot be found in the image file.\r\n
0xc000008b | Indicates the specified resource name cannot be found in the image file.\r\n
0xc000008c | {EXCEPTION}\r\nArray bounds exceeded.\r\n
0xc000008d | {EXCEPTION}\r\nFloating-point denormal operand.\r\n
0xc000008e | {EXCEPTION}\r\nFloating-point division by zero.\r\n
0xc000008f | {EXCEPTION}\r\nFloating-point inexact result.\r\n
0xc0000090 | {EXCEPTION}\r\nFloating-point invalid operation.\r\n
0xc0000091 | {EXCEPTION}\r\nFloating-point overflow.\r\n
0xc0000092 | {EXCEPTION}\r\nFloating-point stack check.\r\n
0xc0000093 | {EXCEPTION}\r\nFloating-point underflow.\r\n
0xc0000094 | {EXCEPTION}\r\nInteger division by zero.\r\n
0xc0000095 | {EXCEPTION}\r\nInteger overflow.\r\n
0xc0000096 | {EXCEPTION}\r\nPrivileged instruction.\r\n
0xc0000097 | An attempt was made to install more paging files than the system supports.\r\n
0xc0000098 | The volume for a file has been externally altered such that the opened file is no longer valid.\r\n
0xc0000099 | When a block of memory is allotted for future updates, such as the memory allocated to hold discretionary access control and primary group information, successive updates may exceed the amount of memory originally allotted.\r\nSince quota may already have been charged to several processes which have handles to the object, it is not reasonable to alter the size of the allocated memory.\r\nInstead, a request that requires more memory than has been allotted must fail and the STATUS_ALLOTED_SPACE_EXCEEDED error returned.\r\n
0xc000009a | Insufficient system resources exist to complete the API.\r\n
0xc000009b | An attempt has been made to open a DFS exit path control file.\r\n
0xc000009c | STATUS_DEVICE_DATA_ERROR\r\n
0xc000009d | STATUS_DEVICE_NOT_CONNECTED\r\n
0xc000009e | STATUS_DEVICE_POWER_FAILURE\r\n
0xc000009f | Virtual memory cannot be freed as base address is not the base of the region and a region size of zero was specified.\r\n
0xc00000a0 | An attempt was made to free virtual memory which is not allocated.\r\n
0xc00000a1 | The working set is not big enough to allow the requested pages to be locked.\r\n
0xc00000a2 | {Write Protect Error}\r\nThe disk cannot be written to because it is write protected.\r\nPlease remove the write protection from the volume %hs in drive %hs.\r\n
0xc00000a3 | {Drive Not Ready}\r\nThe drive is not ready for use; its door may be open.\r\nPlease check drive %hs and make sure that a disk is inserted and that the drive door is closed.\r\n
0xc00000a4 | The specified attributes are invalid, or incompatible with the attributes for the group as a whole.\r\n
0xc00000a5 | A specified impersonation level is invalid.\r\nAlso used to indicate a required impersonation level was not provided.\r\n
0xc00000a6 | An attempt was made to open an Anonymous level token.\r\nAnonymous tokens may not be opened.\r\n
0xc00000a7 | The validation information class requested was invalid.\r\n
0xc00000a8 | The type of a token object is inappropriate for its attempted use.\r\n
0xc00000a9 | The type of a token object is inappropriate for its attempted use.\r\n
0xc00000aa | An attempt was made to execute an instruction at an unaligned address and the host system does not support unaligned instruction references.\r\n
0xc00000ab | The maximum named pipe instance count has been reached.\r\n
0xc00000ac | An instance of a named pipe cannot be found in the listening state.\r\n
0xc00000ad | The named pipe is not in the connected or closing state.\r\n
0xc00000ae | The specified pipe is set to complete operations and there are current I/O operations queued so it cannot be changed to queue operations.\r\n
0xc00000af | The specified handle is not open to the server end of the named pipe.\r\n
0xc00000b0 | The specified named pipe is in the disconnected state.\r\n
0xc00000b1 | The specified named pipe is in the closing state.\r\n
0xc00000b2 | The specified named pipe is in the connected state.\r\n
0xc00000b3 | The specified named pipe is in the listening state.\r\n
0xc00000b4 | The specified named pipe is not in message mode.\r\n
0xc00000b5 | {Device Timeout}\r\nThe specified I/O operation on %hs was not completed before the time-out period expired.\r\n
0xc00000b6 | The specified file has been closed by another process.\r\n
0xc00000b7 | Profiling not started.\r\n
0xc00000b8 | Profiling not stopped.\r\n
0xc00000b9 | The passed ACL did not contain the minimum required information.\r\n
0xc00000ba | The file that was specified as a target is a directory and the caller specified that it could be anything but a directory.\r\n
0xc00000bb | The request is not supported.\r\n
0xc00000bc | This remote computer is not listening.\r\n
0xc00000bd | A duplicate name exists on the network.\r\n
0xc00000be | The network path cannot be located.\r\n
0xc00000bf | The network is busy.\r\n
0xc00000c0 | This device does not exist.\r\n
0xc00000c1 | The network BIOS command limit has been reached.\r\n
0xc00000c2 | An I/O adapter hardware error has occurred.\r\n
0xc00000c3 | The network responded incorrectly.\r\n
0xc00000c4 | An unexpected network error occurred.\r\n
0xc00000c5 | The remote adapter is not compatible.\r\n
0xc00000c6 | The printer queue is full.\r\n
0xc00000c7 | Space to store the file waiting to be printed is not available on the server.\r\n
0xc00000c8 | The requested print file has been canceled.\r\n
0xc00000c9 | The network name was deleted.\r\n
0xc00000ca | Network access is denied.\r\n
0xc00000cb | {Incorrect Network Resource Type}\r\nThe specified device type (LPT, for example) conflicts with the actual device type on the remote resource.\r\n
0xc00000cc | {Network Name Not Found}\r\nThe specified share name cannot be found on the remote server.\r\n
0xc00000cd | The name limit for the local computer network adapter card was exceeded.\r\n
0xc00000ce | The network BIOS session limit was exceeded.\r\n
0xc00000cf | File sharing has been temporarily paused.\r\n
0xc00000d0 | No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept.\r\n
0xc00000d1 | Print or disk redirection is temporarily paused.\r\n
0xc00000d2 | A network data fault occurred.\r\n
0xc00000d3 | The number of active profiling objects is at the maximum and no more may be started.\r\n
0xc00000d4 | {Incorrect Volume}\r\nThe target file of a rename request is located on a different device than the source of the rename request.\r\n
0xc00000d5 | The file specified has been renamed and thus cannot be modified.\r\n
0xc00000d6 | {Network Request Timeout}\r\nThe session with a remote server has been disconnected because the time-out interval for a request has expired.\r\n
0xc00000d7 | Indicates an attempt was made to operate on the security of an object that does not have security associated with it.\r\n
0xc00000d8 | Used to indicate that an operation cannot continue without blocking for I/O.\r\n
0xc00000d9 | Used to indicate that a read operation was done on an empty pipe.\r\n
0xc00000da | Configuration information could not be read from the domain controller, either because the machine is unavailable, or access has been denied.\r\n
0xc00000db | Indicates that a thread attempted to terminate itself by default (called NtTerminateThread with NULL) and it was the last thread in the current process.\r\n
0xc00000dc | Indicates the Sam Server was in the wrong state to perform the desired operation.\r\n
0xc00000dd | Indicates the Domain was in the wrong state to perform the desired operation.\r\n
0xc00000de | This operation is only allowed for the Primary Domain Controller of the domain.\r\n
0xc00000df | The specified Domain did not exist.\r\n
0xc00000e0 | The specified Domain already exists.\r\n
0xc00000e1 | An attempt was made to exceed the limit on the number of domains per server for this release.\r\n
0xc00000e2 | Error status returned when oplock request is denied.\r\n
0xc00000e3 | Error status returned when an invalid oplock acknowledgment is received by a file system.\r\n
0xc00000e4 | This error indicates that the requested operation cannot be completed due to a catastrophic media failure or on-disk data structure corruption.\r\n
0xc00000e5 | An internal error occurred.\r\n
0xc00000e6 | Indicates generic access types were contained in an access mask which should already be mapped to non-generic access types.\r\n
0xc00000e7 | Indicates a security descriptor is not in the necessary format (absolute or self-relative).\r\n
0xc00000e8 | An access to a user buffer failed at an "expected" point in time.\r\nThis code is defined since the caller does not want to accept STATUS_ACCESS_VIOLATION in its filter.\r\n
0xc00000e9 | If an I/O error is returned which is not defined in the standard FsRtl filter, it is converted to the following error which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ea | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000eb | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ec | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ed | The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.\r\n
0xc00000ee | An attempt has been made to start a new session manager or LSA logon session with an ID that is already in use.\r\n
0xc00000ef | An invalid parameter was passed to a service or function as the first argument.\r\n
0xc00000f0 | An invalid parameter was passed to a service or function as the second argument.\r\n
0xc00000f1 | An invalid parameter was passed to a service or function as the third argument.\r\n
0xc00000f2 | An invalid parameter was passed to a service or function as the fourth argument.\r\n
0xc00000f3 | An invalid parameter was passed to a service or function as the fifth argument.\r\n
0xc00000f4 | An invalid parameter was passed to a service or function as the sixth argument.\r\n
0xc00000f5 | An invalid parameter was passed to a service or function as the seventh argument.\r\n
0xc00000f6 | An invalid parameter was passed to a service or function as the eighth argument.\r\n
0xc00000f7 | An invalid parameter was passed to a service or function as the ninth argument.\r\n
0xc00000f8 | An invalid parameter was passed to a service or function as the tenth argument.\r\n
0xc00000f9 | An invalid parameter was passed to a service or function as the eleventh argument.\r\n
0xc00000fa | An invalid parameter was passed to a service or function as the twelfth argument.\r\n
0xc00000fb | An attempt was made to access a network file, but the network software was not yet started.\r\n
0xc00000fc | An attempt was made to start the redirector, but the redirector has already been started.\r\n
0xc00000fd | A new guard page for the stack cannot be created.\r\n
0xc00000fe | A specified authentication package is unknown.\r\n
0xc00000ff | A malformed function table was encountered during an unwind operation.\r\n
0xc0000100 | Indicates the specified environment variable name was not found in the specified environment block.\r\n
0xc0000101 | Indicates that the directory trying to be deleted is not empty.\r\n
0xc0000102 | {Corrupt File}\r\nThe file or directory %hs is corrupt and unreadable.\r\nPlease run the Chkdsk utility.\r\n
0xc0000103 | A requested opened file is not a directory.\r\n
0xc0000104 | The logon session is not in a state that is consistent with the requested operation.\r\n
0xc0000105 | An internal LSA error has occurred. An authentication package has requested the creation of a Logon Session but the ID of an already existing Logon Session has been specified.\r\n
0xc0000106 | A specified name string is too long for its intended use.\r\n
0xc0000107 | The user attempted to force close the files on a redirected drive, but there were opened files on the drive, and the user did not specify a sufficient level of force.\r\n
0xc0000108 | The user attempted to force close the files on a redirected drive, but there were opened directories on the drive, and the user did not specify a sufficient level of force.\r\n
0xc0000109 | RtlFindMessage could not locate the requested message ID in the message table resource.\r\n
0xc000010a | An attempt was made to duplicate an object handle into or out of an exiting process.\r\n
0xc000010b | Indicates an invalid value has been provided for the LogonType requested.\r\n
0xc000010c | Indicates that an attempt was made to assign protection to a file system file or directory and one of the SIDs in the security descriptor could not be translated into a GUID that could be stored by the file system.\r\nThis causes the protection attempt to fail, which may cause a file creation attempt to fail.\r\n
0xc000010d | Indicates that an attempt has been made to impersonate via a named pipe that has not yet been read from.\r\n
0xc000010e | Indicates that the specified image is already loaded.\r\n
0xc000010f | STATUS_ABIOS_NOT_PRESENT\r\n
0xc0000110 | STATUS_ABIOS_LID_NOT_EXIST\r\n
0xc0000111 | STATUS_ABIOS_LID_ALREADY_OWNED\r\n
0xc0000112 | STATUS_ABIOS_NOT_LID_OWNER\r\n
0xc0000113 | STATUS_ABIOS_INVALID_COMMAND\r\n
0xc0000114 | STATUS_ABIOS_INVALID_LID\r\n
0xc0000115 | STATUS_ABIOS_SELECTOR_NOT_AVAILABLE\r\n
0xc0000116 | STATUS_ABIOS_INVALID_SELECTOR\r\n
0xc0000117 | Indicates that an attempt was made to change the size of the LDT for a process that has no LDT.\r\n
0xc0000118 | Indicates that an attempt was made to grow an LDT by setting its size, or that the size was not an even number of selectors.\r\n
0xc0000119 | Indicates that the starting value for the LDT information was not an integral multiple of the selector size.\r\n
0xc000011a | Indicates that the user supplied an invalid descriptor when trying to set up Ldt descriptors.\r\n
0xc000011b | The specified image file did not have the correct format. It appears to be NE format.\r\n
0xc000011c | Indicates that the transaction state of a registry sub-tree is incompatible with the requested operation.\r\nFor example, a request has been made to start a new transaction with one already in progress,\r\nor a request has been made to apply a transaction when one is not currently in progress.\r\n
0xc000011d | Indicates an error has occurred during a registry transaction commit.\r\nThe database has been left in an unknown, but probably inconsistent, state.\r\nThe state of the registry transaction is left as COMMITTING.\r\n
0xc000011e | An attempt was made to map a file of size zero with the maximum size specified as zero.\r\n
0xc000011f | Too many files are opened on a remote server.\r\nThis error should only be returned by the Windows redirector on a remote drive.\r\n
0xc0000120 | The I/O request was canceled.\r\n
0xc0000121 | An attempt has been made to remove a file or directory that cannot be deleted.\r\n
0xc0000122 | Indicates a name specified as a remote computer name is syntactically invalid.\r\n
0xc0000123 | An I/O request other than close was performed on a file after it has been deleted,\r\nwhich can only happen to a request which did not complete before the last handle was closed via NtClose.\r\n
0xc0000124 | Indicates an operation has been attempted on a built-in (special) SAM account which is incompatible with built-in accounts.\r\nFor example, built-in accounts cannot be deleted.\r\n
0xc0000125 | The operation requested may not be performed on the specified group because it is a built-in special group.\r\n
0xc0000126 | The operation requested may not be performed on the specified user because it is a built-in special user.\r\n
0xc0000127 | Indicates a member cannot be removed from a group because the group is currently the member's primary group.\r\n
0xc0000128 | An I/O request other than close and several other special case operations was attempted using a file object that had already been closed.\r\n
0xc0000129 | Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token may only be performed when a process has zero or one threads.\r\n
0xc000012a | An attempt was made to operate on a thread within a specific process, but the thread specified is not in the process specified.\r\n
0xc000012b | An attempt was made to establish a token for use as a primary token but the token is already in use. A token can only be the primary token of one process at a time.\r\n
0xc000012c | Page file quota was exceeded.\r\n
0xc000012d | {Out of Virtual Memory}\r\nYour system is low on virtual memory. To ensure that Windows runs properly, increase the size of your virtual memory paging file. For more information, see Help.\r\n
0xc000012e | The specified image file did not have the correct format, it appears to be LE format.\r\n
0xc000012f | The specified image file did not have the correct format, it did not have an initial MZ.\r\n
0xc0000130 | The specified image file did not have the correct format, it did not have a proper e_lfarlc in the MZ header.\r\n
0xc0000131 | The specified image file did not have the correct format, it appears to be a 16-bit Windows image.\r\n
0xc0000132 | The Netlogon service cannot start because another Netlogon service running in the domain conflicts with the specified role.\r\n
0xc0000133 | The time at the Primary Domain Controller is different than the time at the Backup Domain Controller or member server by too large an amount.\r\n
0xc0000134 | The SAM database on a Windows Server is significantly out of synchronization with the copy on the Domain Controller. A complete synchronization is required.\r\n
0xc0000135 | {Unable To Locate Component}\r\nThis application has failed to start because %hs was not found. Re-installing the application may fix this problem.\r\n
0xc0000136 | The NtCreateFile API failed. This error should never be returned to an application, it is a place holder for the Windows Lan Manager Redirector to use in its internal error mapping routines.\r\n
0xc0000137 | {Privilege Failed}\r\nThe I/O permissions for the process could not be changed.\r\n
0xc0000138 | {Ordinal Not Found}\r\nThe ordinal %ld could not be located in the dynamic link library %hs.\r\n
0xc0000139 | {Entry Point Not Found}\r\nThe procedure entry point %hs could not be located in the dynamic link library %hs.\r\n
0xc000013a | {Application Exit by CTRL+C}\r\nThe application terminated as a result of a CTRL+C.\r\n
0xc000013b | {Virtual Circuit Closed}\r\nThe network transport on your computer has closed a network connection. There may or may not be I/O requests outstanding.\r\n
0xc000013c | {Virtual Circuit Closed}\r\nThe network transport on a remote computer has closed a network connection. There may or may not be I/O requests outstanding.\r\n
0xc000013d | {Insufficient Resources on Remote Computer}\r\nThe remote computer has insufficient resources to complete the network request. For instance, there may not be enough memory available on the remote computer to carry out the request at this time.\r\n
0xc000013e | {Virtual Circuit Closed}\r\nAn existing connection (virtual circuit) has been broken at the remote computer. There is probably something wrong with the network software protocol or the network hardware on the remote computer.\r\n
0xc000013f | {Virtual Circuit Closed}\r\nThe network transport on your computer has closed a network connection because it had to wait too long for a response from the remote computer.\r\n
0xc0000140 | The connection handle given to the transport was invalid.\r\n
0xc0000141 | The address handle given to the transport was invalid.\r\n
0xc0000142 | {DLL Initialization Failed}\r\nInitialization of the dynamic link library %hs failed. The process is terminating abnormally.\r\n
0xc0000143 | {Missing System File}\r\nThe required system file %hs is bad or missing.\r\n
0xc0000144 | {Application Error}\r\nThe exception %s (0x%08lx) occurred in the application at location 0x%08lx.\r\n
0xc0000145 | {Application Error}\r\nThe application failed to initialize properly (0x%lx). Click on OK to terminate the application.\r\n
0xc0000146 | {Unable to Create Paging File}\r\nThe creation of the paging file %hs failed (%lx). The requested size was %ld.\r\n
0xc0000147 | {No Paging File Specified}\r\nNo paging file was specified in the system configuration.\r\n
0xc0000148 | {Incorrect System Call Level}\r\nAn invalid level was passed into the specified system call.\r\n
0xc0000149 | {Incorrect Password to LAN Manager Server}\r\nYou specified an incorrect password to a LAN Manager 2.x or MS-NET server.\r\n
0xc000014a | {EXCEPTION}\r\nA real-mode application issued a floating-point instruction and floating-point hardware is not present.\r\n
0xc000014b | The pipe operation has failed because the other end of the pipe has been closed.\r\n
0xc000014c | {The Registry Is Corrupt}\r\nThe structure of one of the files that contains Registry data is corrupt, or the image of the file in memory is corrupt, or the file could not be recovered because the alternate copy or log was absent or corrupt.\r\n
0xc000014d | An I/O operation initiated by the Registry failed unrecoverably.\r\nThe Registry could not read in, or write out, or flush, one of the files that contain the system's image of the Registry.\r\n
0xc000014e | An event pair synchronization operation was performed using the thread specific client/server event pair object, but no event pair object was associated with the thread.\r\n
0xc000014f | The volume does not contain a recognized file system.\r\nPlease make sure that all required file system drivers are loaded and that the volume is not corrupt.\r\n
0xc0000150 | No serial device was successfully initialized. The serial driver will unload.\r\n
0xc0000151 | The specified local group does not exist.\r\n
0xc0000152 | The specified account name is not a member of the local group.\r\n
0xc0000153 | The specified account name is already a member of the local group.\r\n
0xc0000154 | The specified local group already exists.\r\n
0xc0000155 | A requested type of logon (e.g., Interactive, Network, Service) is not granted by the target system's local security policy.\r\nPlease ask the system administrator to grant the necessary form of logon.\r\n
0xc0000156 | The maximum number of secrets that may be stored in a single system has been exceeded. The length and number of secrets is limited to satisfy United States State Department export restrictions.\r\n
0xc0000157 | The length of a secret exceeds the maximum length allowed. The length and number of secrets is limited to satisfy United States State Department export restrictions.\r\n
0xc0000158 | The Local Security Authority (LSA) database contains an internal inconsistency.\r\n
0xc0000159 | The requested operation cannot be performed in fullscreen mode.\r\n
0xc000015a | During a logon attempt, the user's security context accumulated too many security IDs. This is a very unusual situation.\r\nRemove the user from some global or local groups to reduce the number of security ids to incorporate into the security context.\r\n
0xc000015b | A user has requested a type of logon (e.g., interactive or network) that has not been granted. An administrator has control over who may logon interactively and through the network.\r\n
0xc000015c | The system has attempted to load or restore a file into the registry, and the specified file is not in the format of a registry file.\r\n
0xc000015d | An attempt was made to change a user password in the security account manager without providing the necessary Windows cross-encrypted password.\r\n
0xc000015e | A Windows Server has an incorrect configuration.\r\n
0xc000015f | An attempt was made to explicitly access the secondary copy of information via a device control to the Fault Tolerance driver and the secondary copy is not present in the system.\r\n
0xc0000160 | A configuration registry node representing a driver service entry was ill-formed and did not contain required value entries.\r\n
0xc0000161 | An illegal character was encountered. For a multi-byte character set this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE.\r\n
0xc0000162 | No mapping for the Unicode character exists in the target multi-byte code page.\r\n
0xc0000163 | The Unicode character is not defined in the Unicode character set installed on the system.\r\n
0xc0000164 | The paging file cannot be created on a floppy diskette.\r\n
0xc0000165 | {Floppy Disk Error}\r\nWhile accessing a floppy disk, an ID address mark was not found.\r\n
0xc0000166 | {Floppy Disk Error}\r\nWhile accessing a floppy disk, the track address from the sector ID field was found to be different than the track address maintained by the controller.\r\n
0xc0000167 | {Floppy Disk Error}\r\nThe floppy disk controller reported an error that is not recognized by the floppy disk driver.\r\n
0xc0000168 | {Floppy Disk Error}\r\nWhile accessing a floppy-disk, the controller returned inconsistent results via its registers.\r\n
0xc0000169 | {Hard Disk Error}\r\nWhile accessing the hard disk, a recalibrate operation failed, even after retries.\r\n
0xc000016a | {Hard Disk Error}\r\nWhile accessing the hard disk, a disk operation failed even after retries.\r\n
0xc000016b | {Hard Disk Error}\r\nWhile accessing the hard disk, a disk controller reset was needed, but even that failed.\r\n
0xc000016c | An attempt was made to open a device that was sharing an IRQ with other devices.\r\nAt least one other device that uses that IRQ was already opened.\r\nTwo concurrent opens of devices that share an IRQ and only work via interrupts is not supported for the particular bus type that the devices use.\r\n
0xc000016d | {FT Orphaning}\r\nA disk that is part of a fault-tolerant volume can no longer be accessed.\r\n
0xc000016e | The system bios failed to connect a system interrupt to the device or bus for\r\nwhich the device is connected.\r\n
0xc0000172 | Tape could not be partitioned.\r\n
0xc0000173 | When accessing a new tape of a multivolume partition, the current blocksize is incorrect.\r\n
0xc0000174 | Tape partition information could not be found when loading a tape.\r\n
0xc0000175 | Attempt to lock the eject media mechanism fails.\r\n
0xc0000176 | Unload media fails.\r\n
0xc0000177 | Physical end of tape was detected.\r\n
0xc0000178 | {No Media}\r\nThere is no media in the drive.\r\nPlease insert media into drive %hs.\r\n
0xc000017a | A member could not be added to or removed from the local group because the member does not exist.\r\n
0xc000017b | A new member could not be added to a local group because the member has the wrong account type.\r\n
0xc000017c | Illegal operation attempted on a registry key which has been marked for deletion.\r\n
0xc000017d | System could not allocate required space in a registry log.\r\n
0xc000017e | Too many Sids have been specified.\r\n
0xc000017f | An attempt was made to change a user password in the security account manager without providing the necessary LM cross-encrypted password.\r\n
0xc0000180 | An attempt was made to create a symbolic link in a registry key that already has subkeys or values.\r\n
0xc0000181 | An attempt was made to create a Stable subkey under a Volatile parent key.\r\n
0xc0000182 | The I/O device is configured incorrectly or the configuration parameters to the driver are incorrect.\r\n
0xc0000183 | An error was detected between two drivers or within an I/O driver.\r\n
0xc0000184 | The device is not in a valid state to perform this request.\r\n
0xc0000185 | The I/O device reported an I/O error.\r\n
0xc0000186 | A protocol error was detected between the driver and the device.\r\n
0xc0000187 | This operation is only allowed for the Primary Domain Controller of the domain.\r\n
0xc0000188 | Log file space is insufficient to support this operation.\r\n
0xc0000189 | A write operation was attempted to a volume after it was dismounted.\r\n
0xc000018a | The workstation does not have a trust secret for the primary domain in the local LSA database.\r\n
0xc000018b | The SAM database on the Windows Server does not have a computer account for this workstation trust relationship.\r\n
0xc000018c | The logon request failed because the trust relationship between the primary domain and the trusted domain failed.\r\n
0xc000018d | The logon request failed because the trust relationship between this workstation and the primary domain failed.\r\n
0xc000018e | The Eventlog log file is corrupt.\r\n
0xc000018f | No Eventlog log file could be opened. The Eventlog service did not start.\r\n
0xc0000190 | The network logon failed. This may be because the validation authority can't be reached.\r\n
0xc0000191 | An attempt was made to acquire a mutant such that its maximum count would have been exceeded.\r\n
0xc0000192 | An attempt was made to logon, but the netlogon service was not started.\r\n
0xc0000193 | The user's account has expired.\r\n
0xc0000194 | {EXCEPTION}\r\nPossible deadlock condition.\r\n
0xc0000195 | Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again..\r\n
0xc0000196 | An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.\r\n
0xc0000197 | The log file has changed between reads.\r\n
0xc0000198 | The account used is an Interdomain Trust account. Use your global user account or local user account to access this server.\r\n
0xc0000199 | The account used is a Computer Account. Use your global user account or local user account to access this server.\r\n
0xc000019a | The account used is an Server Trust account. Use your global user account or local user account to access this server.\r\n
0xc000019b | The name or SID of the domain specified is inconsistent with the trust information for that domain.\r\n
0xc000019c | A volume has been accessed for which a file system driver is required that has not yet been loaded.\r\n
0xc0000202 | There is no user session key for the specified logon session.\r\n
0xc0000203 | The remote user session has been deleted.\r\n
0xc0000204 | Indicates the specified resource language ID cannot be found in the\r\nimage file.\r\n
0xc0000205 | Insufficient server resources exist to complete the request.\r\n
0xc0000206 | The size of the buffer is invalid for the specified operation.\r\n
0xc0000207 | The transport rejected the network address specified as invalid.\r\n
0xc0000208 | The transport rejected the network address specified due to an invalid use of a wildcard.\r\n
0xc0000209 | The transport address could not be opened because all the available addresses are in use.\r\n
0xc000020a | The transport address could not be opened because it already exists.\r\n
0xc000020b | The transport address is now closed.\r\n
0xc000020c | The transport connection is now disconnected.\r\n
0xc000020d | The transport connection has been reset.\r\n
0xc000020e | The transport cannot dynamically acquire any more nodes.\r\n
0xc000020f | The transport aborted a pending transaction.\r\n
0xc0000210 | The transport timed out a request waiting for a response.\r\n
0xc0000211 | The transport did not receive a release for a pending response.\r\n
0xc0000212 | The transport did not find a transaction matching the specific\r\ntoken.\r\n
0xc0000213 | The transport had previously responded to a transaction request.\r\n
0xc0000214 | The transport does not recognized the transaction request identifier specified.\r\n
0xc0000215 | The transport does not recognize the transaction request type specified.\r\n
0xc0000216 | The transport can only process the specified request on the server side of a session.\r\n
0xc0000217 | The transport can only process the specified request on the client side of a session.\r\n
0xc0000218 | {Registry File Failure}\r\nThe registry cannot load the hive (file):\r\n%hs\r\nor its log or alternate.\r\nIt is corrupt, absent, or not writable.\r\n
0xc0000219 | {Unexpected Failure in DebugActiveProcess}\r\nAn unexpected failure occurred while processing a DebugActiveProcess API request. You may choose OK to terminate the process, or Cancel to ignore the error.\r\n
0xc000021a | {Fatal System Error}\r\nThe %hs system process terminated unexpectedly with a status of 0x%08x (0x%08x 0x%08x).\r\nThe system has been shut down.\r\n
0xc000021b | {Data Not Accepted}\r\nThe TDI client could not handle the data received during an indication.\r\n
0xc000021c | {Unable to Retrieve Browser Server List}\r\nThe list of servers for this workgroup is not currently available.\r\n
0xc000021d | NTVDM encountered a hard error.\r\n
0xc000021e | {Cancel Timeout}\r\nThe driver %hs failed to complete a cancelled I/O request in the allotted time.\r\n
0xc000021f | {Reply Message Mismatch}\r\nAn attempt was made to reply to an LPC message, but the thread specified by the client ID in the message was not waiting on that message.\r\n
0xc0000220 | {Mapped View Alignment Incorrect}\r\nAn attempt was made to map a view of a file, but either the specified base address or the offset into the file were not aligned on the proper allocation granularity.\r\n
0xc0000221 | {Bad Image Checksum}\r\nThe image %hs is possibly corrupt. The header checksum does not match the computed checksum.\r\n
0xc0000222 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0xc0000223 | The parameter(s) passed to the server in the client/server shared memory window were invalid. Too much data may have been put in the shared memory window.\r\n
0xc0000224 | The user's password must be changed before logging on the first time.\r\n
0xc0000225 | The object was not found.\r\n
0xc0000226 | The stream is not a tiny stream.\r\n
0xc0000227 | A transaction recover failed.\r\n
0xc0000228 | The request must be handled by the stack overflow code.\r\n
0xc0000229 | A consistency check failed.\r\n
0xc000022a | The attempt to insert the ID in the index failed because the ID is already in the index.\r\n
0xc000022b | The attempt to set the object's ID failed because the object already has an ID.\r\n
0xc000022c | Internal OFS status codes indicating how an allocation operation is handled. Either it is retried after the containing onode is moved or the extent stream is converted to a large stream.\r\n
0xc000022d | The request needs to be retried.\r\n
0xc000022e | The attempt to find the object found an object matching by ID on the volume but it is out of the scope of the handle used for the operation.\r\n
0xc000022f | The bucket array must be grown. Retry transaction after doing so.\r\n
0xc0000230 | The property set specified does not exist on the object.\r\n
0xc0000231 | The user/kernel marshalling buffer has overflowed.\r\n
0xc0000232 | The supplied variant structure contains invalid data.\r\n
0xc0000233 | Could not find a domain controller for this domain.\r\n
0xc0000234 | The user account has been automatically locked because too many invalid logon attempts or password change attempts have been requested.\r\n
0xc0000235 | NtClose was called on a handle that was protected from close via NtSetInformationObject.\r\n
0xc0000236 | The transport connection attempt was refused by the remote system.\r\n
0xc0000237 | The transport connection was gracefully closed.\r\n
0xc0000238 | The transport endpoint already has an address associated with it.\r\n
0xc0000239 | An address has not yet been associated with the transport endpoint.\r\n
0xc000023a | An operation was attempted on a nonexistent transport connection.\r\n
0xc000023b | An invalid operation was attempted on an active transport connection.\r\n
0xc000023c | The remote network is not reachable by the transport.\r\n
0xc000023d | The remote system is not reachable by the transport.\r\n
0xc000023e | The remote system does not support the transport protocol.\r\n
0xc000023f | No service is operating at the destination port of the transport on the remote system.\r\n
0xc0000240 | The request was aborted.\r\n
0xc0000241 | The transport connection was aborted by the local system.\r\n
0xc0000242 | The specified buffer contains ill-formed data.\r\n
0xc0000243 | The requested operation cannot be performed on a file with a user mapped section open.\r\n
0xc0000244 | {Audit Failed}\r\nAn attempt to generate a security audit failed.\r\n
0xc0000245 | The timer resolution was not previously set by the current process.\r\n
0xc0000246 | A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.\r\n
0xc0000247 | Attempting to login during an unauthorized time of day for this account.\r\n
0xc0000248 | The account is not authorized to login from this station.\r\n
0xc0000249 | {UP/MP Image Mismatch}\r\nThe image %hs has been modified for use on a uniprocessor system, but you are running it on a multiprocessor machine.\r\nPlease reinstall the image file.\r\n
0xc0000250 | There is insufficient account information to log you on.\r\n
0xc0000251 | {Invalid DLL Entrypoint}\r\nThe dynamic link library %hs is not written correctly. The stack pointer has been left in an inconsistent state.\r\nThe entrypoint should be declared as WINAPI or STDCALL. Select YES to fail the DLL load. Select NO to continue execution. Selecting NO may cause the application to operate incorrectly.\r\n
0xc0000252 | {Invalid Service Callback Entrypoint}\r\nThe %hs service is not written correctly. The stack pointer has been left in an inconsistent state.\r\nThe callback entrypoint should be declared as WINAPI or STDCALL. Selecting OK will cause the service to continue operation. However, the service process may operate incorrectly.\r\n
0xc0000253 | The server received the messages but did not send a reply.\r\n
0xc0000254 | There is an IP address conflict with another system on the network\r\n
0xc0000255 | There is an IP address conflict with another system on the network\r\n
0xc0000256 | {Low On Registry Space}\r\nThe system has reached the maximum size allowed for the system part of the registry.  Additional storage requests will be ignored.\r\n
0xc0000257 | The contacted server does not support the indicated part of the DFS namespace.\r\n
0xc0000258 | A callback return system service cannot be executed when no callback is active.\r\n
0xc0000259 | The service being accessed is licensed for a particular number of connections.\r\nNo more connections can be made to the service at this time because there are already as many connections as the service can accept.\r\n
0xc000025a | The password provided is too short to meet the policy of your user account.\r\nPlease choose a longer password.\r\n
0xc000025b | The policy of your user account does not allow you to change passwords too frequently.\r\nThis is done to prevent users from changing back to a familiar, but potentially discovered, password.\r\nIf you feel your password has been compromised then please contact your administrator immediately to have a new one assigned.\r\n
0xc000025c | You have attempted to change your password to one that you have used in the past.\r\nThe policy of your user account does not allow this. Please select a password that you have not previously used.\r\n
0xc000025e | You have attempted to load a legacy device driver while its device instance had been disabled.\r\n
0xc000025f | The specified compression format is unsupported.\r\n
0xc0000260 | The specified hardware profile configuration is invalid.\r\n
0xc0000261 | The specified Plug and Play registry device path is invalid.\r\n
0xc0000262 | {Driver Entry Point Not Found}\r\nThe %hs device driver could not locate the ordinal %ld in driver %hs.\r\n
0xc0000263 | {Driver Entry Point Not Found}\r\nThe %hs device driver could not locate the entry point %hs in driver %hs.\r\n
0xc0000264 | {Application Error}\r\nThe application attempted to release a resource it did not own. Click on OK to terminate the application.\r\n
0xc0000265 | An attempt was made to create more links on a file than the file system supports.\r\n
0xc0000266 | The specified quota list is internally inconsistent with its descriptor.\r\n
0xc0000267 | The specified file has been relocated to offline storage.\r\n
0xc0000268 | {Windows Evaluation Notification}\r\nThe evaluation period for this installation of Windows has expired. This system will shutdown in 1 hour. To restore access to this installation of Windows, please upgrade this installation using a licensed distribution of this product.\r\n
0xc0000269 | {Illegal System DLL Relocation}\r\nThe system DLL %hs was relocated in memory. The application will not run properly.\r\nThe relocation occurred because the DLL %hs occupied an address range reserved for Windows system DLLs. The vendor supplying the DLL should be contacted for a new DLL.\r\n
0xc000026a | {License Violation}\r\nThe system has detected tampering with your registered product type. This is a violation of your software license. Tampering with product type is not permitted.\r\n
0xc000026b | {DLL Initialization Failed}\r\nThe application failed to initialize because the window station is shutting down.\r\n
0xc000026c | {Unable to Load Device Driver}\r\n%hs device driver could not be loaded.\r\nError Status was 0x%x\r\n
0xc000026d | DFS is unavailable on the contacted server.\r\n
0xc000026e | An operation was attempted to a volume after it was dismounted.\r\n
0xc000026f | An internal error occurred in the Win32 x86 emulation subsystem.\r\n
0xc0000270 | Win32 x86 emulation subsystem Floating-point stack check.\r\n
0xc0000271 | The validation process needs to continue on to the next step.\r\n
0xc0000272 | There was no match for the specified key in the index.\r\n
0xc0000273 | There are no more matches for the current index enumeration.\r\n
0xc0000275 | The NTFS file or directory is not a reparse point.\r\n
0xc0000276 | The Windows I/O reparse tag passed for the NTFS reparse point is invalid.\r\n
0xc0000277 | The Windows I/O reparse tag does not match the one present in the NTFS reparse point.\r\n
0xc0000278 | The user data passed for the NTFS reparse point is invalid.\r\n
0xc0000279 | The layered file system driver for this IO tag did not handle it when needed.\r\n
0xc0000280 | The NTFS symbolic link could not be resolved even though the initial file name is valid.\r\n
0xc0000281 | The NTFS directory is a reparse point.\r\n
0xc0000282 | The range could not be added to the range list because of a conflict.\r\n
0xc0000283 | The specified medium changer source element contains no media.\r\n
0xc0000284 | The specified medium changer destination element already contains media.\r\n
0xc0000285 | The specified medium changer element does not exist.\r\n
0xc0000286 | The specified element is contained within a magazine that is no longer present.\r\n
0xc0000287 | The device requires reinitialization due to hardware errors.\r\n
0xc000028a | The file encryption attempt failed.\r\n
0xc000028b | The file decryption attempt failed.\r\n
0xc000028c | The specified range could not be found in the range list.\r\n
0xc000028d | There is no encryption recovery policy configured for this system.\r\n
0xc000028e | The required encryption driver is not loaded for this system.\r\n
0xc000028f | The file was encrypted with a different encryption driver than is currently loaded.\r\n
0xc0000290 | There are no EFS keys defined for the user.\r\n
0xc0000291 | The specified file is not encrypted.\r\n
0xc0000292 | The specified file is not in the defined EFS export format.\r\n
0xc0000293 | The specified file is encrypted and the user does not have the ability to decrypt it.\r\n
0xc0000295 | The guid passed was not recognized as valid by a WMI data provider.\r\n
0xc0000296 | The instance name passed was not recognized as valid by a WMI data provider.\r\n
0xc0000297 | The data item id passed was not recognized as valid by a WMI data provider.\r\n
0xc0000298 | The WMI request could not be completed and should be retried.\r\n
0xc0000299 | The policy object is shared and can only be modified at the root\r\n
0xc000029a | The policy object does not exist when it should\r\n
0xc000029b | The requested policy information only lives in the Ds\r\n
0xc000029c | The volume must be upgraded to enable this feature\r\n
0xc000029d | The remote storage service is not operational at this time.\r\n
0xc000029e | The remote storage service encountered a media error.\r\n
0xc000029f | The tracking (workstation) service is not running.\r\n
0xc00002a0 | The server process is running under a SID different than that required by client.\r\n
0xc00002a1 | The specified directory service attribute or value does not exist.\r\n
0xc00002a2 | The attribute syntax specified to the directory service is invalid.\r\n
0xc00002a3 | The attribute type specified to the directory service is not defined.\r\n
0xc00002a4 | The specified directory service attribute or value already exists.\r\n
0xc00002a5 | The directory service is busy.\r\n
0xc00002a6 | The directory service is not available.\r\n
0xc00002a7 | The directory service was unable to allocate a relative identifier.\r\n
0xc00002a8 | The directory service has exhausted the pool of relative identifiers.\r\n
0xc00002a9 | The requested operation could not be performed because the directory service is not the master for that type of operation.\r\n
0xc00002aa | The directory service was unable to initialize the subsystem that allocates relative identifiers.\r\n
0xc00002ab | The requested operation did not satisfy one or more constraints associated with the class of the object.\r\n
0xc00002ac | The directory service can perform the requested operation only on a leaf object.\r\n
0xc00002ad | The directory service cannot perform the requested operation on the Relatively Defined Name (RDN) attribute of an object.\r\n
0xc00002ae | The directory service detected an attempt to modify the object class of an object.\r\n
0xc00002af | An error occurred while performing a cross domain move operation.\r\n
0xc00002b0 | Unable to Contact the Global Catalog Server.\r\n
0xc00002b1 | The requested operation requires a directory service, and none was available.\r\n
0xc00002b2 | The reparse attribute cannot be set as it is incompatible with an existing attribute.\r\n
0xc00002b3 | A group marked use for deny only  can not be enabled.\r\n
0xc00002b4 | {EXCEPTION}\r\nMultiple floating point faults.\r\n
0xc00002b5 | {EXCEPTION}\r\nMultiple floating point traps.\r\n
0xc00002b6 | The device has been removed.\r\n
0xc00002b7 | The volume change journal is being deleted.\r\n
0xc00002b8 | The volume change journal is not active.\r\n
0xc00002b9 | The requested interface is not supported.\r\n
0xc00002c1 | A directory service resource limit has been exceeded.\r\n
0xc00002c2 | {System Standby Failed}\r\nThe driver %hs does not support standby mode. Updating this driver may allow the system to go to standby mode.\r\n
0xc00002c3 | Mutual Authentication failed. The server's password is out of date at the domain controller.\r\n
0xc00002c4 | The system file %1 has become corrupt and has been replaced.\r\n
0xc00002c5 | {EXCEPTION}\r\nAlignment Error\r\nA datatype misalignment error was detected in a load or store instruction.\r\n
0xc00002c6 | The WMI data item or data block is read only.\r\n
0xc00002c7 | The WMI data item or data block could not be changed.\r\n
0xc00002c8 | {Virtual Memory Minimum Too Low}\r\nYour system is low on virtual memory. Windows is increasing the size of your virtual memory paging file.\r\nDuring this process, memory requests for some applications may be denied. For more information, see Help.\r\n
0xc00002c9 | {EXCEPTION}\r\nRegister NaT consumption faults.\r\nA NaT value is consumed on a non speculative instruction.\r\n
0xc00002ca | The medium changer's transport element contains media, which is causing the operation to fail.\r\n
0xc00002cb | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.\r\n
0xc00002cc | This operation is supported only when you are connected to the server.\r\n
0xc00002cd | Only an administrator can modify the membership list of an administrative group.\r\n
0xc00002ce | A device was removed so enumeration must be restarted.\r\n
0xc00002cf | The journal entry has been deleted from the journal.\r\n
0xc00002d0 | Cannot change the primary group ID of a domain controller account.\r\n
0xc00002d1 | {Fatal System Error}\r\nThe system image %s is not properly signed.\r\nThe file has been replaced with the signed file.\r\nThe system has been shut down.\r\n
0xc00002d2 | Device will not start without a reboot.\r\n
0xc00002d3 | Current device power state cannot support this request.\r\n
0xc00002d4 | The specified group type is invalid.\r\n
0xc00002d5 | In mixed domain no nesting of global group if group is security enabled.\r\n
0xc00002d6 | In mixed domain, cannot nest local groups with other local groups, if the group is security enabled.\r\n
0xc00002d7 | A global group cannot have a local group as a member.\r\n
0xc00002d8 | A global group cannot have a universal group as a member.\r\n
0xc00002d9 | A universal group cannot have a local group as a member.\r\n
0xc00002da | A global group cannot have a cross domain member.\r\n
0xc00002db | A local group cannot have another cross domain local group as a member.\r\n
0xc00002dc | Can not change to security disabled group because of having primary members in this group.\r\n
0xc00002dd | The WMI operation is not supported by the data block or method.\r\n
0xc00002de | There is not enough power to complete the requested operation.\r\n
0xc00002df | Security Account Manager needs to get the boot password.\r\n
0xc00002e0 | Security Account Manager needs to get the boot key from floppy disk.\r\n
0xc00002e1 | Directory Service can not start.\r\n
0xc00002e2 | Directory Services could not start because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.\r\n
0xc00002e3 | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Safe Mode, check the event log for more detailed information.\r\n
0xc00002e4 | The requested operation can be performed only on a global catalog server.\r\n
0xc00002e5 | A local group can only be a member of other local groups in the same domain.\r\n
0xc00002e6 | Foreign security principals cannot be members of universal groups.\r\n
0xc00002e7 | Your computer could not be joined to the domain. You have exceeded the maximum number of computer accounts you are allowed to create in this domain. Contact your system administrator to have this limit reset or increased.\r\n
0xc00002e8 | STATUS_MULTIPLE_FAULT_VIOLATION\r\n
0xc00002e9 | This operation can not be performed on the current domain.\r\n
0xc00002ea | The directory or file cannot be created.\r\n
0xc00002eb | The system is in the process of shutting down.\r\n
0xc00002ec | Directory Services could not start because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown the system. You can use the recovery console to diagnose the system further.\r\n
0xc00002ed | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown the system. You can use the recovery console to diagnose the system further.\r\n
0xc00002ee | A security context was deleted before the context was completed.  This is considered a logon failure.\r\n
0xc00002ef | The client is trying to negotiate a context and the server requires user-to-user but didn't send a TGT reply.\r\n
0xc00002f0 | An object ID was not found in the file.\r\n
0xc00002f1 | Unable to accomplish the requested task because the local machine does not have any IP addresses.\r\n
0xc00002f2 | The supplied credential handle does not match the credential associated with the security context.\r\n
0xc00002f3 | The crypto system or checksum function is invalid because a required function is unavailable.\r\n
0xc00002f4 | The number of maximum ticket referrals has been exceeded.\r\n
0xc00002f5 | The local machine must be a Kerberos KDC (domain controller) and it is not.\r\n
0xc00002f6 | The other end of the security negotiation is requires strong crypto but it is not supported on the local machine.\r\n
0xc00002f7 | The KDC reply contained more than one principal name.\r\n
0xc00002f8 | Expected to find PA data for a hint of what etype to use, but it was not found.\r\n
0xc00002f9 | The client cert name does not matches the user name or the KDC name is incorrect.\r\n
0xc00002fa | Smartcard logon is required and was not used.\r\n
0xc00002fb | An invalid request was sent to the KDC.\r\n
0xc00002fc | The KDC was unable to generate a referral for the service requested.\r\n
0xc00002fd | The encryption type requested is not supported by the KDC.\r\n
0xc00002fe | A system shutdown is in progress.\r\n
0xc00002ff | The server machine is shutting down.\r\n
0xc0000300 | This operation is not supported on a Microsoft Small Business Server\r\n
0xc0000301 | The WMI GUID is no longer available\r\n
0xc0000302 | Collection or events for the WMI GUID is already disabled.\r\n
0xc0000303 | Collection or events for the WMI GUID is already enabled.\r\n
0xc0000304 | The Master File Table on the volume is too fragmented to complete this operation.\r\n
0xc0000305 | Copy protection failure.\r\n
0xc0000306 | Copy protection error - DVD CSS Authentication failed.\r\n
0xc0000307 | Copy protection error - The given sector does not contain a valid key.\r\n
0xc0000308 | Copy protection error - DVD session key not established.\r\n
0xc0000309 | Copy protection error - The read failed because the sector is encrypted.\r\n
0xc000030a | Copy protection error - The given DVD's region does not correspond to the\r\nregion setting of the drive.\r\n
0xc000030b | Copy protection error - The drive's region setting may be permanent.\r\n
0xc0000320 | The kerberos protocol encountered an error while validating the KDC certificate during smartcard Logon\r\n
0xc0000321 | The kerberos protocol encountered an error while attempting to utilize the smartcard subsystem.\r\n
0xc0000322 | The target server does not have acceptable kerberos credentials.\r\n
0xc0000350 | The transport determined that the remote system is down.\r\n
0xc0000351 | An unsupported preauthentication mechanism was presented to the kerberos package.\r\n
0xc0000352 | The encryption algorithm used on the source file needs a bigger key buffer than the one used on the destination file.\r\n
0xc0000353 | An attempt to remove a processes DebugPort was made, but a port was not already associated with the process.\r\n
0xc0000354 | An attempt to do an operation on a debug port failed because the port is in the process of being deleted.\r\n
0xc0000355 | This version of Windows is not compatible with the behavior version of directory forest, domain or domain controller.\r\n
0xc0000356 | The specified event is currently not being audited.\r\n
0xc0000357 | The machine account was created pre-NT4.  The account needs to be recreated.\r\n
0xc0000358 | A account group can not have a universal group as a member.\r\n
0xc0000359 | The specified image file did not have the correct format, it appears to be a 32-bit Windows image.\r\n
0xc000035a | The specified image file did not have the correct format, it appears to be a 64-bit Windows image.\r\n
0xc000035b | Client's supplied SSPI channel bindings were incorrect.\r\n
0xc000035c | The client's session has expired, so the client must reauthenticate to continue accessing the remote resources.\r\n
0xc000035d | AppHelp dialog canceled thus preventing the application from starting.\r\n
0xc000035e | The SID filtering operation removed all SIDs.\r\n
0xc000035f | The driver was not loaded because the system is booting into safe mode.\r\n
0xc0000361 | Access to %1 has been restricted by your Administrator by the default software restriction policy level.\r\n
0xc0000362 | Access to %1 has been restricted by your Administrator by location with policy rule %2 placed on path %3\r\n
0xc0000363 | Access to %1 has been restricted by your Administrator by software publisher policy.\r\n
0xc0000364 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0xc0000365 | The driver was not loaded because it failed it's initialization call.\r\n
0xc0000366 | The "%hs" encountered an error while applying power or reading the device configuration.\r\nThis may be caused by a failure of your hardware or by a poor connection.\r\n
0xc0000368 | The create operation failed because the name contained at least one mount point which resolves to a volume to which the specified device object is not attached.\r\n
0xc0000369 | The device object parameter is either not a valid device object or is not attached to the volume specified by the file name.\r\n
0xc000036a | A Machine Check Error has occured. Please check the system eventlog for additional information.\r\n
0xc000036b | Driver %2 has been blocked from loading.\r\n
0xc000036c | Driver %2 has been blocked from loading.\r\n
0xc000036d | There was error [%2] processing the driver database.\r\n
0xc000036e | System hive size has exceeded its limit.\r\n
0xc000036f | A dynamic link library (DLL) referenced a module that was neither a DLL nor the process's executable image.\r\n
0xc0000380 | An incorrect PIN was presented to the smart card\r\n
0xc0000381 | The smart card is blocked\r\n
0xc0000382 | No PIN was presented to the smart card\r\n
0xc0000383 | No smart card available\r\n
0xc0000384 | The requested key container does not exist on the smart card\r\n
0xc0000385 | The requested certificate does not exist on the smart card\r\n
0xc0000386 | The requested keyset does not exist\r\n
0xc0000387 | A communication error with the smart card has been detected.\r\n
0xc0000388 | The system detected a possible attempt to compromise security. Please ensure that you can contact the server that authenticated you.\r\n
0xc0000389 | The smartcard certificate used for authentication has been revoked.\r\nPlease contact your system administrator.  There may be additional information in the\r\nevent log.\r\n
0xc000038a | An untrusted certificate authority was detected While processing the\r\nsmartcard certificate used for authentication.  Please contact your system\r\nadministrator.\r\n
0xc000038b | The revocation status of the smartcard certificate used for\r\nauthentication could not be determined. Please contact your system administrator.\r\n
0xc000038c | The smartcard certificate used for authentication was not trusted.  Please\r\ncontact your system administrator.\r\n
0xc000038d | The smartcard certificate used for authentication has expired.  Please\r\ncontact your system administrator.\r\n
0xc000038e | The driver could not be loaded because a previous version of the driver is still in memory.\r\n
0xc0009898 | WOW Assertion Error.\r\n
0xc0010001 | Debugger did not perform a state change.\r\n
0xc0010002 | Debugger has found the application is not idle.\r\n
0xc0020001 | The string binding is invalid.\r\n
0xc0020002 | The binding handle is not the correct type.\r\n
0xc0020003 | The binding handle is invalid.\r\n
0xc0020004 | The RPC protocol sequence is not supported.\r\n
0xc0020005 | The RPC protocol sequence is invalid.\r\n
0xc0020006 | The string UUID is invalid.\r\n
0xc0020007 | The endpoint format is invalid.\r\n
0xc0020008 | The network address is invalid.\r\n
0xc0020009 | No endpoint was found.\r\n
0xc002000a | The timeout value is invalid.\r\n
0xc002000b | The object UUID was not found.\r\n
0xc002000c | The object UUID has already been registered.\r\n
0xc002000d | The type UUID has already been registered.\r\n
0xc002000e | The RPC server is already listening.\r\n
0xc002000f | No protocol sequences have been registered.\r\n
0xc0020010 | The RPC server is not listening.\r\n
0xc0020011 | The manager type is unknown.\r\n
0xc0020012 | The interface is unknown.\r\n
0xc0020013 | There are no bindings.\r\n
0xc0020014 | There are no protocol sequences.\r\n
0xc0020015 | The endpoint cannot be created.\r\n
0xc0020016 | Not enough resources are available to complete this operation.\r\n
0xc0020017 | The RPC server is unavailable.\r\n
0xc0020018 | The RPC server is too busy to complete this operation.\r\n
0xc0020019 | The network options are invalid.\r\n
0xc002001a | There are no remote procedure calls active on this thread.\r\n
0xc002001b | The remote procedure call failed.\r\n
0xc002001c | The remote procedure call failed and did not execute.\r\n
0xc002001d | An RPC protocol error occurred.\r\n
0xc002001f | The transfer syntax is not supported by the RPC server.\r\n
0xc0020021 | The type UUID is not supported.\r\n
0xc0020022 | The tag is invalid.\r\n
0xc0020023 | The array bounds are invalid.\r\n
0xc0020024 | The binding does not contain an entry name.\r\n
0xc0020025 | The name syntax is invalid.\r\n
0xc0020026 | The name syntax is not supported.\r\n
0xc0020028 | No network address is available to use to construct a UUID.\r\n
0xc0020029 | The endpoint is a duplicate.\r\n
0xc002002a | The authentication type is unknown.\r\n
0xc002002b | The maximum number of calls is too small.\r\n
0xc002002c | The string is too long.\r\n
0xc002002d | The RPC protocol sequence was not found.\r\n
0xc002002e | The procedure number is out of range.\r\n
0xc002002f | The binding does not contain any authentication information.\r\n
0xc0020030 | The authentication service is unknown.\r\n
0xc0020031 | The authentication level is unknown.\r\n
0xc0020032 | The security context is invalid.\r\n
0xc0020033 | The authorization service is unknown.\r\n
0xc0020034 | The entry is invalid.\r\n
0xc0020035 | The operation cannot be performed.\r\n
0xc0020036 | There are no more endpoints available from the endpoint mapper.\r\n
0xc0020037 | No interfaces have been exported.\r\n
0xc0020038 | The entry name is incomplete.\r\n
0xc0020039 | The version option is invalid.\r\n
0xc002003a | There are no more members.\r\n
0xc002003b | There is nothing to unexport.\r\n
0xc002003c | The interface was not found.\r\n
0xc002003d | The entry already exists.\r\n
0xc002003e | The entry is not found.\r\n
0xc002003f | The name service is unavailable.\r\n
0xc0020040 | The network address family is invalid.\r\n
0xc0020041 | The requested operation is not supported.\r\n
0xc0020042 | No security context is available to allow impersonation.\r\n
0xc0020043 | An internal error occurred in RPC.\r\n
0xc0020044 | The RPC server attempted an integer divide by zero.\r\n
0xc0020045 | An addressing error occurred in the RPC server.\r\n
0xc0020046 | A floating point operation at the RPC server caused a divide by zero.\r\n
0xc0020047 | A floating point underflow occurred at the RPC server.\r\n
0xc0020048 | A floating point overflow occurred at the RPC server.\r\n
0xc0020049 | A remote procedure call is already in progress for this thread.\r\n
0xc002004a | There are no more bindings.\r\n
0xc002004b | The group member was not found.\r\n
0xc002004c | The endpoint mapper database entry could not be created.\r\n
0xc002004d | The object UUID is the nil UUID.\r\n
0xc002004f | No interfaces have been registered.\r\n
0xc0020050 | The remote procedure call was cancelled.\r\n
0xc0020051 | The binding handle does not contain all required information.\r\n
0xc0020052 | A communications failure occurred during a remote procedure call.\r\n
0xc0020053 | The requested authentication level is not supported.\r\n
0xc0020054 | No principal name registered.\r\n
0xc0020055 | The error specified is not a valid Windows RPC error code.\r\n
0xc0020057 | A security package specific error occurred.\r\n
0xc0020058 | Thread is not cancelled.\r\n
0xc0020062 | Invalid asynchronous remote procedure call handle.\r\n
0xc0020063 | Invalid asynchronous RPC call handle for this operation.\r\n
0xc0030001 | The list of RPC servers available for auto-handle binding has been exhausted.\r\n
0xc0030002 | The file designated by DCERPCCHARTRANS cannot be opened.\r\n
0xc0030003 | The file containing the character translation table has fewer than 512 bytes.\r\n
0xc0030004 | A null context handle is passed as an [in] parameter.\r\n
0xc0030005 | The context handle does not match any known context handles.\r\n
0xc0030006 | The context handle changed during a call.\r\n
0xc0030007 | The binding handles passed to a remote procedure call do not match.\r\n
0xc0030008 | The stub is unable to get the call handle.\r\n
0xc0030009 | A null reference pointer was passed to the stub.\r\n
0xc003000a | The enumeration value is out of range.\r\n
0xc003000b | The byte count is too small.\r\n
0xc003000c | The stub received bad data.\r\n
0xc0030059 | Invalid operation on the encoding/decoding handle.\r\n
0xc003005a | Incompatible version of the serializing package.\r\n
0xc003005b | Incompatible version of the RPC stub.\r\n
0xc003005c | The RPC pipe object is invalid or corrupted.\r\n
0xc003005d | An invalid operation was attempted on an RPC pipe object.\r\n
0xc003005e | Unsupported RPC pipe version.\r\n
0xc003005f | The RPC pipe object has already been closed.\r\n
0xc0030060 | The RPC call completed before all pipes were processed.\r\n
0xc0030061 | No more data is available from the RPC pipe.\r\n
0xc0040035 | A device is missing in the system BIOS MPS table. This device will not be used.\r\nPlease contact your system vendor for system BIOS update.\r\n
0xc0040036 | A translator failed to translate resources.\r\n
0xc0040037 | A IRQ translator failed to translate resources.\r\n
0xc00a0001 | Session name %1 is invalid.\r\n
0xc00a0002 | The protocol driver %1 is invalid.\r\n
0xc00a0003 | The protocol driver %1 was not found in the system path.\r\n
0xc00a0006 | A close operation is pending on the Terminal Connection.\r\n
0xc00a0007 | There are no free output buffers available.\r\n
0xc00a0008 | The MODEM.INF file was not found.\r\n
0xc00a0009 | The modem (%1) was not found in MODEM.INF.\r\n
0xc00a000a | The modem did not accept the command sent to it.\r\nVerify the configured modem name matches the attached modem.\r\n
0xc00a000b | The modem did not respond to the command sent to it.\r\nVerify the modem is properly cabled and powered on.\r\n
0xc00a000c | Carrier detect has failed or carrier has been dropped due to disconnect.\r\n
0xc00a000d | Dial tone not detected within required time.\r\nVerify phone cable is properly attached and functional.\r\n
0xc00a000e | Busy signal detected at remote site on callback.\r\n
0xc00a000f | Voice detected at remote site on callback.\r\n
0xc00a0010 | Transport driver error\r\n
0xc00a0012 | The client you are using is not licensed to use this system. Your logon request is denied.\r\n
0xc00a0013 | The system has reached its licensed logon limit.\r\nPlease try again later.\r\n
0xc00a0014 | The system license has expired. Your logon request is denied.\r\n
0xc00a0015 | The specified session cannot be found.\r\n
0xc00a0016 | The specified session name is already in use.\r\n
0xc00a0017 | The requested operation cannot be completed because the Terminal Connection is currently busy processing a connect, disconnect, reset, or delete operation.\r\n
0xc00a0018 | An attempt has been made to connect to a session whose video mode is not supported by the current client.\r\n
0xc00a0022 | The application attempted to enable DOS graphics mode.\r\nDOS graphics mode is not supported.\r\n
0xc00a0024 | The requested operation can be performed only on the system console.\r\nThis is most often the result of a driver or system DLL requiring direct console access.\r\n
0xc00a0026 | The client failed to respond to the server connect message.\r\n
0xc00a0027 | Disconnecting the console session is not supported.\r\n
0xc00a0028 | Reconnecting a disconnected session to the console is not supported.\r\n
0xc00a002a | The request to control another session remotely was denied.\r\n
0xc00a002b | A process has requested access to a session, but has not been granted those access rights.\r\n
0xc00a002e | The Terminal Connection driver %1 is invalid.\r\n
0xc00a002f | The Terminal Connection driver %1 was not found in the system path.\r\n
0xc00a0030 | The requested session cannot be controlled remotely.\r\nYou cannot control your own session, a session that is trying to control your session,\r\na session that has no user logged on, nor control other sessions from the console.\r\n
0xc00a0031 | The requested session is not configured to allow remote control.\r\n
0xc00a0032 | The RDP protocol component %2 detected an error in the protocol stream and has disconnected the client.\r\n
0xc00a0033 | Your request to connect to this Terminal server has been rejected.\r\nYour Terminal Server Client license number has not been entered for this copy of the Terminal Client.\r\nPlease call your system administrator for help in entering a valid, unique license number for this Terminal Server Client.\r\nClick OK to continue.\r\n
0xc00a0034 | Your request to connect to this Terminal server has been rejected.\r\nYour Terminal Server Client license number is currently being used by another user.\r\nPlease call your system administrator to obtain a new copy of the Terminal Server Client with a valid, unique license number.\r\nClick OK to continue.\r\n
0xc00a0035 | The remote control of the console was terminated because the display mode was changed. Changing the display mode in a remote control session is not supported.\r\n
0xc00a0036 | Remote control could not be terminated because the specified session is not currently being remotely controlled.\r\n
0xc0130001 | The cluster node is not valid.\r\n
0xc0130002 | The cluster node already exists.\r\n
0xc0130003 | A node is in the process of joining the cluster.\r\n
0xc0130004 | The cluster node was not found.\r\n
0xc0130005 | The cluster local node information was not found.\r\n
0xc0130006 | The cluster network already exists.\r\n
0xc0130007 | The cluster network was not found.\r\n
0xc0130008 | The cluster network interface already exists.\r\n
0xc0130009 | The cluster network interface was not found.\r\n
0xc013000a | The cluster request is not valid for this object.\r\n
0xc013000b | The cluster network provider is not valid.\r\n
0xc013000c | The cluster node is down.\r\n
0xc013000d | The cluster node is not reachable.\r\n
0xc013000e | The cluster node is not a member of the cluster.\r\n
0xc013000f | A cluster join operation is not in progress.\r\n
0xc0130010 | The cluster network is not valid.\r\n
0xc0130011 | No network adapters are available.\r\n
0xc0130012 | The cluster node is up.\r\n
0xc0130013 | The cluster node is paused.\r\n
0xc0130014 | The cluster node is not paused.\r\n
0xc0130015 | No cluster security context is available.\r\n
0xc0130016 | The cluster network is not configured for internal cluster communication.\r\n
0xc0130017 | The cluster node has been poisoned.\r\n
0xc0140001 | An attempt was made to run an invalid AML opcode\r\n
0xc0140002 | The AML Interpreter Stack has overflowed\r\n
0xc0140003 | An inconsistent state has occurred\r\n
0xc0140004 | An attempt was made to access an array outside of its bounds\r\n
0xc0140005 | A required argument was not specified\r\n
0xc0140006 | A fatal error has occurred\r\n
0xc0140007 | An invalid SuperName was specified\r\n
0xc0140008 | An argument with an incorrect type was specified\r\n
0xc0140009 | An object with an incorrect type was specified\r\n
0xc014000a | A target with an incorrect type was specified\r\n
0xc014000b | An incorrect number of arguments were specified\r\n
0xc014000c | An address failed to translate\r\n
0xc014000d | An incorrect event type was specified\r\n
0xc014000e | A handler for the target already exists\r\n
0xc014000f | Invalid data for the target was specified\r\n
0xc0140010 | An invalid region for the target was specified\r\n
0xc0140011 | An attempt was made to access a field outside of the defined range\r\n
0xc0140012 | The Global system lock could not be acquired\r\n
0xc0140013 | An attempt was made to reinitialize the ACPI subsystem\r\n
0xc0140014 | The ACPI subsystem has not been initialized\r\n
0xc0140015 | An incorrect mutex was specified\r\n
0xc0140016 | The mutex is not currently owned\r\n
0xc0140017 | An attempt was made to access the mutex by a process that was not the owner\r\n
0xc0140018 | An error occurred during an access to Region Space\r\n
0xc0140019 | An attempt was made to use an incorrect table\r\n
0xc0140020 | The registration of an ACPI event failed\r\n
0xc0140021 | An ACPI Power Object failed to transition state\r\n
0xc0150001 | The requested section is not present in the activation context.\r\n
0xc0150002 | Windows was not able to process the application binding information.\r\nPlease refer to your System Event Log for further information.\r\n
0xc0150003 | The application binding data format is invalid.\r\n
0xc0150004 | The referenced assembly is not installed on your system.\r\n
0xc0150005 | The manifest file does not begin with the required tag and format information.\r\n
0xc0150006 | The manifest file contains one or more syntax errors.\r\n
0xc0150007 | The application attempted to activate a disabled activation context.\r\n
0xc0150008 | The requested lookup key was not found in any active activation context.\r\n
0xc0150009 | A component version required by the application conflicts with another component version already active.\r\n
0xc015000a | The type requested activation context section does not match the query API used.\r\n
0xc015000b | Lack of system resources has required isolated activation to be disabled for the current thread of execution.\r\n
0xc015000c | The referenced assembly could not be found.\r\n
0xc015000e | An attempt to set the process default activation context failed because the process default activation context was already set.\r\n
0xc015000f | The activation context being deactivated is not the most recently activated one.\r\n
0xc0150010 | The activation context being deactivated is not active for the current thread of execution.\r\n
0xc0150011 | The activation context being deactivated has already been deactivated.\r\n
0xc0150012 | The activation context of system default assembly could not be generated.\r\n
0xc0150013 | A component used by the isolation facility has requested to terminate the process.\r\n

### 5.2.3790.1830, 5.2.3790.3959

Message identifier | Message string
--- | ---
0x00000000 | STATUS_WAIT_0\r\n
0x00000001 | STATUS_WAIT_1\r\n
0x00000002 | STATUS_WAIT_2\r\n
0x00000003 | STATUS_WAIT_3\r\n
0x0000003f | STATUS_WAIT_63\r\n
0x00000080 | STATUS_ABANDONED_WAIT_0\r\n
0x000000bf | STATUS_ABANDONED_WAIT_63\r\n
0x000000c0 | STATUS_USER_APC\r\n
0x00000100 | STATUS_KERNEL_APC\r\n
0x00000101 | STATUS_ALERTED\r\n
0x00000102 | STATUS_TIMEOUT\r\n
0x00000103 | The operation that was requested is pending completion.\r\n
0x00000104 | A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.\r\n
0x00000105 | Returned by enumeration APIs to indicate more information is available to successive calls.\r\n
0x00000106 | Indicates not all privileges referenced are assigned to the caller.\r\nThis allows, for example, all privileges to be disabled without having to know exactly which privileges are assigned.\r\n
0x00000107 | Some of the information to be translated has not been translated.\r\n
0x00000108 | An open/create operation completed while an oplock break is underway.\r\n
0x00000109 | A new volume has been mounted by a file system.\r\n
0x0000010a | This success level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.\r\nThe commit has now been completed.\r\n
0x0000010b | This indicates that a notify change request has been completed due to closing the handle which made the notify change request.\r\n
0x0000010c | This indicates that a notify change request is being completed and that the information is not being returned in the caller's buffer.\r\nThe caller now needs to enumerate the files to find the changes.\r\n
0x0000010d | {No Quotas}\r\nNo system quota limits are specifically set for this account.\r\n
0x0000010e | {Connect Failure on Primary Transport}\r\nAn attempt was made to connect to the remote server %hs on the primary transport, but the connection failed.\r\nThe computer WAS able to connect on a secondary transport.\r\n
0x00000110 | Page fault was a transition fault.\r\n
0x00000111 | Page fault was a demand zero fault.\r\n
0x00000112 | Page fault was a demand zero fault.\r\n
0x00000113 | Page fault was a demand zero fault.\r\n
0x00000114 | Page fault was satisfied by reading from a secondary storage device.\r\n
0x00000115 | Cached page was locked during operation.\r\n
0x00000116 | Crash dump exists in paging file.\r\n
0x00000117 | Specified buffer contains all zeros.\r\n
0x00000118 | A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.\r\n
0x00000119 | The device has succeeded a query-stop and its resource requirements have changed.\r\n
0x00000120 | The translator has translated these resources into the global space and no further translations should be performed.\r\n
0x00000121 | The directory service evaluated group memberships locally, as it was unable to contact a global catalog server.\r\n
0x00000122 | A process being terminated has no threads to terminate.\r\n
0x00000123 | The specified process is not part of a job.\r\n
0x00000124 | The specified process is part of a job.\r\n
0x00000125 | {Volume Shadow Copy Service}\r\nThe system is now ready for hibernation.\r\n
0x00000126 | A file system or file system filter driver has successfully completed an FsFilter operation.\r\n
0x00000367 | An operation is blocked waiting for an oplock.\r\n
0x00010001 | Debugger handled exception\r\n
0x00010002 | Debugger continued\r\n
0x40000000 | {Object Exists}\r\nAn attempt was made to create an object and the object name already existed.\r\n
0x40000001 | {Thread Suspended}\r\nA thread termination occurred while the thread was suspended. The thread was resumed, and termination proceeded.\r\n
0x40000002 | {Working Set Range Error}\r\nAn attempt was made to set the working set minimum or maximum to values which are outside of the allowable range.\r\n
0x40000003 | {Image Relocated}\r\nAn image file could not be mapped at the address specified in the image file. Local fixups must be performed on this image.\r\n
0x40000004 | This informational level status indicates that a specified registry sub-tree transaction state did not yet exist and had to be created.\r\n
0x40000005 | {Segment Load}\r\nA virtual DOS machine (VDM) is loading, unloading, or moving an MS-DOS or Win16 program segment image.\r\nAn exception is raised so a debugger can load, unload or track symbols and breakpoints within these 16-bit segments.\r\n
0x40000006 | {Local Session Key}\r\nA user session key was requested for a local RPC connection. The session key returned is a constant value and not unique to this connection.\r\n
0x40000007 | {Invalid Current Directory}\r\nThe process cannot switch to the startup current directory %hs.\r\nSelect OK to set current directory to %hs, or select CANCEL to exit.\r\n
0x40000008 | {Serial IOCTL Complete}\r\nA serial I/O operation was completed by another write to a serial port.\r\n(The IOCTL_SERIAL_XOFF_COUNTER reached zero.)\r\n
0x40000009 | {Registry Recovery}\r\nOne of the files containing the system's Registry data had to be recovered by use of a log or alternate copy.\r\nThe recovery was successful.\r\n
0x4000000a | {Redundant Read}\r\nTo satisfy a read request, the NT fault-tolerant file system successfully read the requested data from a redundant copy.\r\nThis was done because the file system encountered a failure on a member of the fault-tolerant volume, but was unable to reassign the failing area of the device.\r\n
0x4000000b | {Redundant Write}\r\nTo satisfy a write request, the NT fault-tolerant file system successfully wrote a redundant copy of the information.\r\nThis was done because the file system encountered a failure on a member of the fault-tolerant volume, but was not able to reassign the failing area of the device.\r\n
0x4000000c | {Serial IOCTL Timeout}\r\nA serial I/O operation completed because the time-out period expired.\r\n(The IOCTL_SERIAL_XOFF_COUNTER had not reached zero.)\r\n
0x4000000d | {Password Too Complex}\r\nThe Windows password is too complex to be converted to a LAN Manager password.\r\nThe LAN Manager password returned is a NULL string.\r\n
0x4000000e | {Machine Type Mismatch}\r\nThe image file %hs is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.\r\n
0x4000000f | {Partial Data Received}\r\nThe network transport returned partial data to its client. The remaining data will be sent later.\r\n
0x40000010 | {Expedited Data Received}\r\nThe network transport returned data to its client that was marked as expedited by the remote system.\r\n
0x40000011 | {Partial Expedited Data Received}\r\nThe network transport returned partial data to its client and this data was marked as expedited by the remote system. The remaining data will be sent later.\r\n
0x40000012 | {TDI Event Done}\r\nThe TDI indication has completed successfully.\r\n
0x40000013 | {TDI Event Pending}\r\nThe TDI indication has entered the pending state.\r\n
0x40000014 | Checking file system on %wZ\r\n
0x40000015 | {Fatal Application Exit}\r\n%hs\r\n
0x40000016 | The specified registry key is referenced by a predefined handle.\r\n
0x40000017 | {Page Unlocked}\r\nThe page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.\r\n
0x40000018 | %hs\r\n
0x40000019 | {Page Locked}\r\nOne of the pages to lock was already locked.\r\n
0x4000001a | Application popup: %1 : %2\r\n
0x4000001b | STATUS_ALREADY_WIN32\r\n
0x4000001c | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001d | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001e | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001f | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000020 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000021 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000022 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000023 | {Machine Type Mismatch}\r\nThe image file %hs is valid, but is for a machine type other than the current machine.\r\n
0x40000024 | A yield execution was performed and no thread was available to run.\r\n
0x40000025 | The resumable flag to a timer API was ignored.\r\n
0x40000026 | The arbiter has deferred arbitration of these resources to its parent\r\n
0x40000027 | The device "%hs" has detected a CardBus card in its slot, but the firmware on this system is not configured to allow the CardBus controller to be run in CardBus mode.\r\nThe operating system will currently accept only 16-bit (R2) pc-cards on this controller.\r\n
0x40000028 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000029 | The CPUs in this multiprocessor system are not all the same revision level.  To use all processors the operating system restricts itself to the features of the least capable processor in the system.  Should problems occur with this system, contact\r\nthe CPU manufacturer to see if this mix of processors is supported.\r\n
0x4000002a | The system was put into hibernation.\r\n
0x4000002b | The system was resumed from hibernation.\r\n
0x4000002c | Windows has detected that the system firmware (BIOS) was updated [previous firmware date = %2, current firmware date %3].\r\n
0x4000002d | A device driver is leaking locked I/O pages causing system degradation.  The system has automatically enabled tracking code in order to try and catch the culprit.\r\n
0x40000294 | The system has awoken\r\n
0x40000370 | The Directory Service is shuting down.\r\n
0x40010001 | Debugger will reply later.\r\n
0x40010002 | Debugger can not provide handle.\r\n
0x40010003 | Debugger terminated thread.\r\n
0x40010004 | Debugger terminated process.\r\n
0x40010005 | Debugger got control C.\r\n
0x40010006 | Debugger printed exception on control C.\r\n
0x40010007 | Debugger received RIP exception.\r\n
0x40010008 | Debugger received control break.\r\n
0x40010009 | Debugger command communication exception.\r\n
0x40020056 | A UUID that is valid only on this computer has been allocated.\r\n
0x400200af | Some data remains to be sent in the request buffer.\r\n
0x400a0004 | The Client Drive Mapping Service Has Connected on Terminal Connection.\r\n
0x400a0005 | The Client Drive Mapping Service Has Disconnected on Terminal Connection.\r\n
0x4015000d | A kernel mode component is releasing a reference on an activation context.\r\n
0x80000001 | {EXCEPTION}\r\nGuard Page Exception\r\nA page of memory that marks the end of a data structure, such as a stack or an array, has been accessed.\r\n
0x80000002 | {EXCEPTION}\r\nAlignment Fault\r\nA datatype misalignment was detected in a load or store instruction.\r\n
0x80000003 | {EXCEPTION}\r\nBreakpoint\r\nA breakpoint has been reached.\r\n
0x80000004 | {EXCEPTION}\r\nSingle Step\r\nA single step or trace operation has just been completed.\r\n
0x80000005 | {Buffer Overflow}\r\nThe data was too large to fit into the specified buffer.\r\n
0x80000006 | {No More Files}\r\nNo more files were found which match the file specification.\r\n
0x80000007 | {Kernel Debugger Awakened}\r\nthe system debugger was awakened by an interrupt.\r\n
0x8000000a | {Handles Closed}\r\nHandles to objects have been automatically closed as a result of the requested operation.\r\n
0x8000000b | {Non-Inheritable ACL}\r\nAn access control list (ACL) contains no components that can be inherited.\r\n
0x8000000c | {GUID Substitution}\r\nDuring the translation of a global identifier (GUID) to a Windows security ID (SID), no administratively-defined GUID prefix was found.\r\nA substitute prefix was used, which will not compromise system security.\r\nHowever, this may provide a more restrictive access than intended.\r\n
0x8000000d | {Partial Copy}\r\nDue to protection conflicts not all the requested bytes could be copied.\r\n
0x8000000e | {Out of Paper}\r\nThe printer is out of paper.\r\n
0x8000000f | {Device Power Is Off}\r\nThe printer power has been turned off.\r\n
0x80000010 | {Device Offline}\r\nThe printer has been taken offline.\r\n
0x80000011 | {Device Busy}\r\nThe device is currently busy.\r\n
0x80000012 | {No More EAs}\r\nNo more extended attributes (EAs) were found for the file.\r\n
0x80000013 | {Illegal EA}\r\nThe specified extended attribute (EA) name contains at least one illegal character.\r\n
0x80000014 | {Inconsistent EA List}\r\nThe extended attribute (EA) list is inconsistent.\r\n
0x80000015 | {Invalid EA Flag}\r\nAn invalid extended attribute (EA) flag was set.\r\n
0x80000016 | {Verifying Disk}\r\nThe media has changed and a verify operation is in progress so no reads or writes may be performed to the device, except those used in the verify operation.\r\n
0x80000017 | {Too Much Information}\r\nThe specified access control list (ACL) contained more information than was expected.\r\n
0x80000018 | This warning level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.\r\nThe commit has NOT been completed, but has not been rolled back either (so it may still be committed if desired).\r\n
0x8000001a | {No More Entries}\r\nNo more entries are available from an enumeration operation.\r\n
0x8000001b | {Filemark Found}\r\nA filemark was detected.\r\n
0x8000001c | {Media Changed}\r\nThe media may have changed.\r\n
0x8000001d | {I/O Bus Reset}\r\nAn I/O bus reset was detected.\r\n
0x8000001e | {End of Media}\r\nThe end of the media was encountered.\r\n
0x8000001f | Beginning of tape or partition has been detected.\r\n
0x80000020 | {Media Changed}\r\nThe media may have changed.\r\n
0x80000021 | A tape access reached a setmark.\r\n
0x80000022 | During a tape access, the end of the data written is reached.\r\n
0x80000023 | The redirector is in use and cannot be unloaded.\r\n
0x80000024 | The server is in use and cannot be unloaded.\r\n
0x80000025 | The specified connection has already been disconnected.\r\n
0x80000026 | A long jump has been executed.\r\n
0x80000027 | A cleaner cartridge is present in the tape library.\r\n
0x80000028 | The Plug and Play query operation was not successful.\r\n
0x80000029 | A frame consolidation has been executed.\r\n
0x8000002a | {Registry Hive Recovered}\r\nRegistry hive (file):\r\n%hs\r\nwas corrupted and it has been recovered. Some data might have been lost.\r\n
0x8000002b | The application is attempting to run executable code from the module %hs.  This may be insecure.  An alternative, %hs, is available.  Should the application use the secure module %hs?\r\n
0x8000002c | The application is loading executable code from the module %hs.  This is secure, but may be incompatible with previous releases of the operating system.  An alternative, %hs, is available.  Should the application use the secure module %hs?\r\n
0x80000288 | The device has indicated that cleaning is necessary.\r\n
0x80000289 | The device has indicated that it's door is open. Further operations require it closed and secured.\r\n
0x80010001 | Debugger did not handle the exception.\r\n
0x80130001 | The cluster node is already up.\r\n
0x80130002 | The cluster node is already down.\r\n
0x80130003 | The cluster network is already online.\r\n
0x80130004 | The cluster network is already offline.\r\n
0x80130005 | The cluster node is already a member of the cluster.\r\n
0xc0000001 | {Operation Failed}\r\nThe requested operation was unsuccessful.\r\n
0xc0000002 | {Not Implemented}\r\nThe requested operation is not implemented.\r\n
0xc0000003 | {Invalid Parameter}\r\nThe specified information class is not a valid information class for the specified object.\r\n
0xc0000004 | The specified information record length does not match the length required for the specified information class.\r\n
0xc0000005 | The instruction at "0x%08lx" referenced memory at "0x%08lx". The memory could not be "%s".\r\n
0xc0000006 | The instruction at "0x%08lx" referenced memory at "0x%08lx". The required data was not placed into memory because of an I/O error status of "0x%08lx".\r\n
0xc0000007 | The pagefile quota for the process has been exhausted.\r\n
0xc0000008 | An invalid HANDLE was specified.\r\n
0xc0000009 | An invalid initial stack was specified in a call to NtCreateThread.\r\n
0xc000000a | An invalid initial start address was specified in a call to NtCreateThread.\r\n
0xc000000b | An invalid Client ID was specified.\r\n
0xc000000c | An attempt was made to cancel or set a timer that has an associated APC and the subject thread is not the thread that originally set the timer with an associated APC routine.\r\n
0xc000000d | An invalid parameter was passed to a service or function.\r\n
0xc000000e | A device which does not exist was specified.\r\n
0xc000000f | {File Not Found}\r\nThe file %hs does not exist.\r\n
0xc0000010 | The specified request is not a valid operation for the target device.\r\n
0xc0000011 | The end-of-file marker has been reached. There is no valid data in the file beyond this marker.\r\n
0xc0000012 | {Wrong Volume}\r\nThe wrong volume is in the drive.\r\nPlease insert volume %hs into drive %hs.\r\n
0xc0000013 | {No Disk}\r\nThere is no disk in the drive.\r\nPlease insert a disk into drive %hs.\r\n
0xc0000014 | {Unknown Disk Format}\r\nThe disk in drive %hs is not formatted properly.\r\nPlease check the disk, and reformat if necessary.\r\n
0xc0000015 | {Sector Not Found}\r\nThe specified sector does not exist.\r\n
0xc0000016 | {Still Busy}\r\nThe specified I/O request packet (IRP) cannot be disposed of because the I/O operation is not complete.\r\n
0xc0000017 | {Not Enough Quota}\r\nNot enough virtual memory or paging file quota is available to complete the specified operation.\r\n
0xc0000018 | {Conflicting Address Range}\r\nThe specified address range conflicts with the address space.\r\n
0xc0000019 | Address range to unmap is not a mapped view.\r\n
0xc000001a | Virtual memory cannot be freed.\r\n
0xc000001b | Specified section cannot be deleted.\r\n
0xc000001c | An invalid system service was specified in a system service call.\r\n
0xc000001d | {EXCEPTION}\r\nIllegal Instruction\r\nAn attempt was made to execute an illegal instruction.\r\n
0xc000001e | {Invalid Lock Sequence}\r\nAn attempt was made to execute an invalid lock sequence.\r\n
0xc000001f | {Invalid Mapping}\r\nAn attempt was made to create a view for a section which is bigger than the section.\r\n
0xc0000020 | {Bad File}\r\nThe attributes of the specified mapping file for a section of memory cannot be read.\r\n
0xc0000021 | {Already Committed}\r\nThe specified address range is already committed.\r\n
0xc0000022 | {Access Denied}\r\nA process has requested access to an object, but has not been granted those access rights.\r\n
0xc0000023 | {Buffer Too Small}\r\nThe buffer is too small to contain the entry. No information has been written to the buffer.\r\n
0xc0000024 | {Wrong Type}\r\nThere is a mismatch between the type of object required by the requested operation and the type of object that is specified in the request.\r\n
0xc0000025 | {EXCEPTION}\r\nCannot Continue\r\nWindows cannot continue from this exception.\r\n
0xc0000026 | An invalid exception disposition was returned by an exception handler.\r\n
0xc0000027 | Unwind exception code.\r\n
0xc0000028 | An invalid or unaligned stack was encountered during an unwind operation.\r\n
0xc0000029 | An invalid unwind target was encountered during an unwind operation.\r\n
0xc000002a | An attempt was made to unlock a page of memory which was not locked.\r\n
0xc000002b | Device parity error on I/O operation.\r\n
0xc000002c | An attempt was made to decommit uncommitted virtual memory.\r\n
0xc000002d | An attempt was made to change the attributes on memory that has not been committed.\r\n
0xc000002e | Invalid Object Attributes specified to NtCreatePort or invalid Port Attributes specified to NtConnectPort\r\n
0xc000002f | Length of message passed to NtRequestPort or NtRequestWaitReplyPort was longer than the maximum message allowed by the port.\r\n
0xc0000030 | An invalid combination of parameters was specified.\r\n
0xc0000031 | An attempt was made to lower a quota limit below the current usage.\r\n
0xc0000032 | {Corrupt Disk}\r\nThe file system structure on the disk is corrupt and unusable.\r\nPlease run the Chkdsk utility on the volume %hs.\r\n
0xc0000033 | Object Name invalid.\r\n
0xc0000034 | Object Name not found.\r\n
0xc0000035 | Object Name already exists.\r\n
0xc0000037 | Attempt to send a message to a disconnected communication port.\r\n
0xc0000038 | An attempt was made to attach to a device that was already attached to another device.\r\n
0xc0000039 | Object Path Component was not a directory object.\r\n
0xc000003a | {Path Not Found}\r\nThe path %hs does not exist.\r\n
0xc000003b | Object Path Component was not a directory object.\r\n
0xc000003c | {Data Overrun}\r\nA data overrun error occurred.\r\n
0xc000003d | {Data Late}\r\nA data late error occurred.\r\n
0xc000003e | {Data Error}\r\nAn error in reading or writing data occurred.\r\n
0xc000003f | {Bad CRC}\r\nA cyclic redundancy check (CRC) checksum error occurred.\r\n
0xc0000040 | {Section Too Large}\r\nThe specified section is too big to map the file.\r\n
0xc0000041 | The NtConnectPort request is refused.\r\n
0xc0000042 | The type of port handle is invalid for the operation requested.\r\n
0xc0000043 | A file cannot be opened because the share access flags are incompatible.\r\n
0xc0000044 | Insufficient quota exists to complete the operation\r\n
0xc0000045 | The specified page protection was not valid.\r\n
0xc0000046 | An attempt to release a mutant object was made by a thread that was not the owner of the mutant object.\r\n
0xc0000047 | An attempt was made to release a semaphore such that its maximum count would have been exceeded.\r\n
0xc0000048 | An attempt to set a processes DebugPort or ExceptionPort was made, but a port already exists in the process or\r\nan attempt to set a file's CompletionPort made, but a port was already set in the file.\r\n
0xc0000049 | An attempt was made to query image information on a section which does not map an image.\r\n
0xc000004a | An attempt was made to suspend a thread whose suspend count was at its maximum.\r\n
0xc000004b | An attempt was made to suspend a thread that has begun termination.\r\n
0xc000004c | An attempt was made to set the working set limit to an invalid value (minimum greater than maximum, etc).\r\n
0xc000004d | A section was created to map a file which is not compatible to an already existing section which maps the same file.\r\n
0xc000004e | A view to a section specifies a protection which is incompatible with the initial view's protection.\r\n
0xc000004f | An operation involving EAs failed because the file system does not support EAs.\r\n
0xc0000050 | An EA operation failed because EA set is too large.\r\n
0xc0000051 | An EA operation failed because the name or EA index is invalid.\r\n
0xc0000052 | The file for which EAs were requested has no EAs.\r\n
0xc0000053 | The EA is corrupt and non-readable.\r\n
0xc0000054 | A requested read/write cannot be granted due to a conflicting file lock.\r\n
0xc0000055 | A requested file lock cannot be granted due to other existing locks.\r\n
0xc0000056 | A non close operation has been requested of a file object with a delete pending.\r\n
0xc0000057 | An attempt was made to set the control attribute on a file. This attribute is not supported in the target file system.\r\n
0xc0000058 | Indicates a revision number encountered or specified is not one known by the service. It may be a more recent revision than the service is aware of.\r\n
0xc0000059 | Indicates two revision levels are incompatible.\r\n
0xc000005a | Indicates a particular Security ID may not be assigned as the owner of an object.\r\n
0xc000005b | Indicates a particular Security ID may not be assigned as the primary group of an object.\r\n
0xc000005c | An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.\r\n
0xc000005d | A mandatory group may not be disabled.\r\n
0xc000005e | There are currently no logon servers available to service the logon request.\r\n
0xc000005f | A specified logon session does not exist. It may already have been terminated.\r\n
0xc0000060 | A specified privilege does not exist.\r\n
0xc0000061 | A required privilege is not held by the client.\r\n
0xc0000062 | The name provided is not a properly formed account name.\r\n
0xc0000063 | The specified user already exists.\r\n
0xc0000064 | The specified user does not exist.\r\n
0xc0000065 | The specified group already exists.\r\n
0xc0000066 | The specified group does not exist.\r\n
0xc0000067 | The specified user account is already in the specified group account.\r\nAlso used to indicate a group cannot be deleted because it contains a member.\r\n
0xc0000068 | The specified user account is not a member of the specified group account.\r\n
0xc0000069 | Indicates the requested operation would disable or delete the last remaining administration account.\r\nThis is not allowed to prevent creating a situation in which the system cannot be administrated.\r\n
0xc000006a | When trying to update a password, this return status indicates that the value provided as the current password is not correct.\r\n
0xc000006b | When trying to update a password, this return status indicates that the value provided for the new password contains values that are not allowed in passwords.\r\n
0xc000006c | When trying to update a password, this status indicates that some password update rule has been violated. For example, the password may not meet length criteria.\r\n
0xc000006d | The attempted logon is invalid. This is either due to a bad username or authentication information.\r\n
0xc000006e | Indicates a referenced user name and authentication information are valid, but some user account restriction has prevented successful authentication (such as time-of-day restrictions).\r\n
0xc000006f | The user account has time restrictions and may not be logged onto at this time.\r\n
0xc0000070 | The user account is restricted such that it may not be used to log on from the source workstation.\r\n
0xc0000071 | The user account's password has expired.\r\n
0xc0000072 | The referenced account is currently disabled and may not be logged on to.\r\n
0xc0000073 | None of the information to be translated has been translated.\r\n
0xc0000074 | The number of LUIDs requested may not be allocated with a single allocation.\r\n
0xc0000075 | Indicates there are no more LUIDs to allocate.\r\n
0xc0000076 | Indicates the sub-authority value is invalid for the particular use.\r\n
0xc0000077 | Indicates the ACL structure is not valid.\r\n
0xc0000078 | Indicates the SID structure is not valid.\r\n
0xc0000079 | Indicates the SECURITY_DESCRIPTOR structure is not valid.\r\n
0xc000007a | Indicates the specified procedure address cannot be found in the DLL.\r\n
0xc000007b | {Bad Image}\r\nThe application or DLL %hs is not a valid Windows image. Please check this against your installation diskette.\r\n
0xc000007c | An attempt was made to reference a token that doesn't exist.\r\nThis is typically done by referencing the token associated with a thread when the thread is not impersonating a client.\r\n
0xc000007d | Indicates that an attempt to build either an inherited ACL or ACE was not successful.\r\nThis can be caused by a number of things. One of the more probable causes is the replacement of a CreatorId with an SID that didn't fit into the ACE or ACL.\r\n
0xc000007e | The range specified in NtUnlockFile was not locked.\r\n
0xc000007f | An operation failed because the disk was full.\r\n
0xc0000080 | The GUID allocation server is [already] disabled at the moment.\r\n
0xc0000081 | The GUID allocation server is [already] enabled at the moment.\r\n
0xc0000082 | Too many GUIDs were requested from the allocation server at once.\r\n
0xc0000083 | The GUIDs could not be allocated because the Authority Agent was exhausted.\r\n
0xc0000084 | The value provided was an invalid value for an identifier authority.\r\n
0xc0000085 | There are no more authority agent values available for the given identifier authority value.\r\n
0xc0000086 | An invalid volume label has been specified.\r\n
0xc0000087 | A mapped section could not be extended.\r\n
0xc0000088 | Specified section to flush does not map a data file.\r\n
0xc0000089 | Indicates the specified image file did not contain a resource section.\r\n
0xc000008a | Indicates the specified resource type cannot be found in the image file.\r\n
0xc000008b | Indicates the specified resource name cannot be found in the image file.\r\n
0xc000008c | {EXCEPTION}\r\nArray bounds exceeded.\r\n
0xc000008d | {EXCEPTION}\r\nFloating-point denormal operand.\r\n
0xc000008e | {EXCEPTION}\r\nFloating-point division by zero.\r\n
0xc000008f | {EXCEPTION}\r\nFloating-point inexact result.\r\n
0xc0000090 | {EXCEPTION}\r\nFloating-point invalid operation.\r\n
0xc0000091 | {EXCEPTION}\r\nFloating-point overflow.\r\n
0xc0000092 | {EXCEPTION}\r\nFloating-point stack check.\r\n
0xc0000093 | {EXCEPTION}\r\nFloating-point underflow.\r\n
0xc0000094 | {EXCEPTION}\r\nInteger division by zero.\r\n
0xc0000095 | {EXCEPTION}\r\nInteger overflow.\r\n
0xc0000096 | {EXCEPTION}\r\nPrivileged instruction.\r\n
0xc0000097 | An attempt was made to install more paging files than the system supports.\r\n
0xc0000098 | The volume for a file has been externally altered such that the opened file is no longer valid.\r\n
0xc0000099 | When a block of memory is allotted for future updates, such as the memory allocated to hold discretionary access control and primary group information, successive updates may exceed the amount of memory originally allotted.\r\nSince quota may already have been charged to several processes which have handles to the object, it is not reasonable to alter the size of the allocated memory.\r\nInstead, a request that requires more memory than has been allotted must fail and the STATUS_ALLOTED_SPACE_EXCEEDED error returned.\r\n
0xc000009a | Insufficient system resources exist to complete the API.\r\n
0xc000009b | An attempt has been made to open a DFS exit path control file.\r\n
0xc000009c | STATUS_DEVICE_DATA_ERROR\r\n
0xc000009d | STATUS_DEVICE_NOT_CONNECTED\r\n
0xc000009e | STATUS_DEVICE_POWER_FAILURE\r\n
0xc000009f | Virtual memory cannot be freed as base address is not the base of the region and a region size of zero was specified.\r\n
0xc00000a0 | An attempt was made to free virtual memory which is not allocated.\r\n
0xc00000a1 | The working set is not big enough to allow the requested pages to be locked.\r\n
0xc00000a2 | {Write Protect Error}\r\nThe disk cannot be written to because it is write protected.\r\nPlease remove the write protection from the volume %hs in drive %hs.\r\n
0xc00000a3 | {Drive Not Ready}\r\nThe drive is not ready for use; its door may be open.\r\nPlease check drive %hs and make sure that a disk is inserted and that the drive door is closed.\r\n
0xc00000a4 | The specified attributes are invalid, or incompatible with the attributes for the group as a whole.\r\n
0xc00000a5 | A specified impersonation level is invalid.\r\nAlso used to indicate a required impersonation level was not provided.\r\n
0xc00000a6 | An attempt was made to open an Anonymous level token.\r\nAnonymous tokens may not be opened.\r\n
0xc00000a7 | The validation information class requested was invalid.\r\n
0xc00000a8 | The type of a token object is inappropriate for its attempted use.\r\n
0xc00000a9 | The type of a token object is inappropriate for its attempted use.\r\n
0xc00000aa | An attempt was made to execute an instruction at an unaligned address and the host system does not support unaligned instruction references.\r\n
0xc00000ab | The maximum named pipe instance count has been reached.\r\n
0xc00000ac | An instance of a named pipe cannot be found in the listening state.\r\n
0xc00000ad | The named pipe is not in the connected or closing state.\r\n
0xc00000ae | The specified pipe is set to complete operations and there are current I/O operations queued so it cannot be changed to queue operations.\r\n
0xc00000af | The specified handle is not open to the server end of the named pipe.\r\n
0xc00000b0 | The specified named pipe is in the disconnected state.\r\n
0xc00000b1 | The specified named pipe is in the closing state.\r\n
0xc00000b2 | The specified named pipe is in the connected state.\r\n
0xc00000b3 | The specified named pipe is in the listening state.\r\n
0xc00000b4 | The specified named pipe is not in message mode.\r\n
0xc00000b5 | {Device Timeout}\r\nThe specified I/O operation on %hs was not completed before the time-out period expired.\r\n
0xc00000b6 | The specified file has been closed by another process.\r\n
0xc00000b7 | Profiling not started.\r\n
0xc00000b8 | Profiling not stopped.\r\n
0xc00000b9 | The passed ACL did not contain the minimum required information.\r\n
0xc00000ba | The file that was specified as a target is a directory and the caller specified that it could be anything but a directory.\r\n
0xc00000bb | The request is not supported.\r\n
0xc00000bc | This remote computer is not listening.\r\n
0xc00000bd | A duplicate name exists on the network.\r\n
0xc00000be | The network path cannot be located.\r\n
0xc00000bf | The network is busy.\r\n
0xc00000c0 | This device does not exist.\r\n
0xc00000c1 | The network BIOS command limit has been reached.\r\n
0xc00000c2 | An I/O adapter hardware error has occurred.\r\n
0xc00000c3 | The network responded incorrectly.\r\n
0xc00000c4 | An unexpected network error occurred.\r\n
0xc00000c5 | The remote adapter is not compatible.\r\n
0xc00000c6 | The printer queue is full.\r\n
0xc00000c7 | Space to store the file waiting to be printed is not available on the server.\r\n
0xc00000c8 | The requested print file has been canceled.\r\n
0xc00000c9 | The network name was deleted.\r\n
0xc00000ca | Network access is denied.\r\n
0xc00000cb | {Incorrect Network Resource Type}\r\nThe specified device type (LPT, for example) conflicts with the actual device type on the remote resource.\r\n
0xc00000cc | {Network Name Not Found}\r\nThe specified share name cannot be found on the remote server.\r\n
0xc00000cd | The name limit for the local computer network adapter card was exceeded.\r\n
0xc00000ce | The network BIOS session limit was exceeded.\r\n
0xc00000cf | File sharing has been temporarily paused.\r\n
0xc00000d0 | No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept.\r\n
0xc00000d1 | Print or disk redirection is temporarily paused.\r\n
0xc00000d2 | A network data fault occurred.\r\n
0xc00000d3 | The number of active profiling objects is at the maximum and no more may be started.\r\n
0xc00000d4 | {Incorrect Volume}\r\nThe target file of a rename request is located on a different device than the source of the rename request.\r\n
0xc00000d5 | The file specified has been renamed and thus cannot be modified.\r\n
0xc00000d6 | {Network Request Timeout}\r\nThe session with a remote server has been disconnected because the time-out interval for a request has expired.\r\n
0xc00000d7 | Indicates an attempt was made to operate on the security of an object that does not have security associated with it.\r\n
0xc00000d8 | Used to indicate that an operation cannot continue without blocking for I/O.\r\n
0xc00000d9 | Used to indicate that a read operation was done on an empty pipe.\r\n
0xc00000da | Configuration information could not be read from the domain controller, either because the machine is unavailable, or access has been denied.\r\n
0xc00000db | Indicates that a thread attempted to terminate itself by default (called NtTerminateThread with NULL) and it was the last thread in the current process.\r\n
0xc00000dc | Indicates the Sam Server was in the wrong state to perform the desired operation.\r\n
0xc00000dd | Indicates the Domain was in the wrong state to perform the desired operation.\r\n
0xc00000de | This operation is only allowed for the Primary Domain Controller of the domain.\r\n
0xc00000df | The specified Domain did not exist.\r\n
0xc00000e0 | The specified Domain already exists.\r\n
0xc00000e1 | An attempt was made to exceed the limit on the number of domains per server for this release.\r\n
0xc00000e2 | Error status returned when oplock request is denied.\r\n
0xc00000e3 | Error status returned when an invalid oplock acknowledgment is received by a file system.\r\n
0xc00000e4 | This error indicates that the requested operation cannot be completed due to a catastrophic media failure or on-disk data structure corruption.\r\n
0xc00000e5 | An internal error occurred.\r\n
0xc00000e6 | Indicates generic access types were contained in an access mask which should already be mapped to non-generic access types.\r\n
0xc00000e7 | Indicates a security descriptor is not in the necessary format (absolute or self-relative).\r\n
0xc00000e8 | An access to a user buffer failed at an "expected" point in time.\r\nThis code is defined since the caller does not want to accept STATUS_ACCESS_VIOLATION in its filter.\r\n
0xc00000e9 | If an I/O error is returned which is not defined in the standard FsRtl filter, it is converted to the following error which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ea | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000eb | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ec | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ed | The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.\r\n
0xc00000ee | An attempt has been made to start a new session manager or LSA logon session with an ID that is already in use.\r\n
0xc00000ef | An invalid parameter was passed to a service or function as the first argument.\r\n
0xc00000f0 | An invalid parameter was passed to a service or function as the second argument.\r\n
0xc00000f1 | An invalid parameter was passed to a service or function as the third argument.\r\n
0xc00000f2 | An invalid parameter was passed to a service or function as the fourth argument.\r\n
0xc00000f3 | An invalid parameter was passed to a service or function as the fifth argument.\r\n
0xc00000f4 | An invalid parameter was passed to a service or function as the sixth argument.\r\n
0xc00000f5 | An invalid parameter was passed to a service or function as the seventh argument.\r\n
0xc00000f6 | An invalid parameter was passed to a service or function as the eighth argument.\r\n
0xc00000f7 | An invalid parameter was passed to a service or function as the ninth argument.\r\n
0xc00000f8 | An invalid parameter was passed to a service or function as the tenth argument.\r\n
0xc00000f9 | An invalid parameter was passed to a service or function as the eleventh argument.\r\n
0xc00000fa | An invalid parameter was passed to a service or function as the twelfth argument.\r\n
0xc00000fb | An attempt was made to access a network file, but the network software was not yet started.\r\n
0xc00000fc | An attempt was made to start the redirector, but the redirector has already been started.\r\n
0xc00000fd | A new guard page for the stack cannot be created.\r\n
0xc00000fe | A specified authentication package is unknown.\r\n
0xc00000ff | A malformed function table was encountered during an unwind operation.\r\n
0xc0000100 | Indicates the specified environment variable name was not found in the specified environment block.\r\n
0xc0000101 | Indicates that the directory trying to be deleted is not empty.\r\n
0xc0000102 | {Corrupt File}\r\nThe file or directory %hs is corrupt and unreadable.\r\nPlease run the Chkdsk utility.\r\n
0xc0000103 | A requested opened file is not a directory.\r\n
0xc0000104 | The logon session is not in a state that is consistent with the requested operation.\r\n
0xc0000105 | An internal LSA error has occurred. An authentication package has requested the creation of a Logon Session but the ID of an already existing Logon Session has been specified.\r\n
0xc0000106 | A specified name string is too long for its intended use.\r\n
0xc0000107 | The user attempted to force close the files on a redirected drive, but there were opened files on the drive, and the user did not specify a sufficient level of force.\r\n
0xc0000108 | The user attempted to force close the files on a redirected drive, but there were opened directories on the drive, and the user did not specify a sufficient level of force.\r\n
0xc0000109 | RtlFindMessage could not locate the requested message ID in the message table resource.\r\n
0xc000010a | An attempt was made to duplicate an object handle into or out of an exiting process.\r\n
0xc000010b | Indicates an invalid value has been provided for the LogonType requested.\r\n
0xc000010c | Indicates that an attempt was made to assign protection to a file system file or directory and one of the SIDs in the security descriptor could not be translated into a GUID that could be stored by the file system.\r\nThis causes the protection attempt to fail, which may cause a file creation attempt to fail.\r\n
0xc000010d | Indicates that an attempt has been made to impersonate via a named pipe that has not yet been read from.\r\n
0xc000010e | Indicates that the specified image is already loaded.\r\n
0xc000010f | STATUS_ABIOS_NOT_PRESENT\r\n
0xc0000110 | STATUS_ABIOS_LID_NOT_EXIST\r\n
0xc0000111 | STATUS_ABIOS_LID_ALREADY_OWNED\r\n
0xc0000112 | STATUS_ABIOS_NOT_LID_OWNER\r\n
0xc0000113 | STATUS_ABIOS_INVALID_COMMAND\r\n
0xc0000114 | STATUS_ABIOS_INVALID_LID\r\n
0xc0000115 | STATUS_ABIOS_SELECTOR_NOT_AVAILABLE\r\n
0xc0000116 | STATUS_ABIOS_INVALID_SELECTOR\r\n
0xc0000117 | Indicates that an attempt was made to change the size of the LDT for a process that has no LDT.\r\n
0xc0000118 | Indicates that an attempt was made to grow an LDT by setting its size, or that the size was not an even number of selectors.\r\n
0xc0000119 | Indicates that the starting value for the LDT information was not an integral multiple of the selector size.\r\n
0xc000011a | Indicates that the user supplied an invalid descriptor when trying to set up Ldt descriptors.\r\n
0xc000011b | The specified image file did not have the correct format. It appears to be NE format.\r\n
0xc000011c | Indicates that the transaction state of a registry sub-tree is incompatible with the requested operation.\r\nFor example, a request has been made to start a new transaction with one already in progress,\r\nor a request has been made to apply a transaction when one is not currently in progress.\r\n
0xc000011d | Indicates an error has occurred during a registry transaction commit.\r\nThe database has been left in an unknown, but probably inconsistent, state.\r\nThe state of the registry transaction is left as COMMITTING.\r\n
0xc000011e | An attempt was made to map a file of size zero with the maximum size specified as zero.\r\n
0xc000011f | Too many files are opened on a remote server.\r\nThis error should only be returned by the Windows redirector on a remote drive.\r\n
0xc0000120 | The I/O request was canceled.\r\n
0xc0000121 | An attempt has been made to remove a file or directory that cannot be deleted.\r\n
0xc0000122 | Indicates a name specified as a remote computer name is syntactically invalid.\r\n
0xc0000123 | An I/O request other than close was performed on a file after it has been deleted,\r\nwhich can only happen to a request which did not complete before the last handle was closed via NtClose.\r\n
0xc0000124 | Indicates an operation has been attempted on a built-in (special) SAM account which is incompatible with built-in accounts.\r\nFor example, built-in accounts cannot be deleted.\r\n
0xc0000125 | The operation requested may not be performed on the specified group because it is a built-in special group.\r\n
0xc0000126 | The operation requested may not be performed on the specified user because it is a built-in special user.\r\n
0xc0000127 | Indicates a member cannot be removed from a group because the group is currently the member's primary group.\r\n
0xc0000128 | An I/O request other than close and several other special case operations was attempted using a file object that had already been closed.\r\n
0xc0000129 | Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token may only be performed when a process has zero or one threads.\r\n
0xc000012a | An attempt was made to operate on a thread within a specific process, but the thread specified is not in the process specified.\r\n
0xc000012b | An attempt was made to establish a token for use as a primary token but the token is already in use. A token can only be the primary token of one process at a time.\r\n
0xc000012c | Page file quota was exceeded.\r\n
0xc000012d | {Out of Virtual Memory}\r\nYour system is low on virtual memory. To ensure that Windows runs properly, increase the size of your virtual memory paging file. For more information, see Help.\r\n
0xc000012e | The specified image file did not have the correct format, it appears to be LE format.\r\n
0xc000012f | The specified image file did not have the correct format, it did not have an initial MZ.\r\n
0xc0000130 | The specified image file did not have the correct format, it did not have a proper e_lfarlc in the MZ header.\r\n
0xc0000131 | The specified image file did not have the correct format, it appears to be a 16-bit Windows image.\r\n
0xc0000132 | The Netlogon service cannot start because another Netlogon service running in the domain conflicts with the specified role.\r\n
0xc0000133 | The time at the Primary Domain Controller is different than the time at the Backup Domain Controller or member server by too large an amount.\r\n
0xc0000134 | The SAM database on a Windows Server is significantly out of synchronization with the copy on the Domain Controller. A complete synchronization is required.\r\n
0xc0000135 | {Unable To Locate Component}\r\nThis application has failed to start because %hs was not found. Re-installing the application may fix this problem.\r\n
0xc0000136 | The NtCreateFile API failed. This error should never be returned to an application, it is a place holder for the Windows Lan Manager Redirector to use in its internal error mapping routines.\r\n
0xc0000137 | {Privilege Failed}\r\nThe I/O permissions for the process could not be changed.\r\n
0xc0000138 | {Ordinal Not Found}\r\nThe ordinal %ld could not be located in the dynamic link library %hs.\r\n
0xc0000139 | {Entry Point Not Found}\r\nThe procedure entry point %hs could not be located in the dynamic link library %hs.\r\n
0xc000013a | {Application Exit by CTRL+C}\r\nThe application terminated as a result of a CTRL+C.\r\n
0xc000013b | {Virtual Circuit Closed}\r\nThe network transport on your computer has closed a network connection. There may or may not be I/O requests outstanding.\r\n
0xc000013c | {Virtual Circuit Closed}\r\nThe network transport on a remote computer has closed a network connection. There may or may not be I/O requests outstanding.\r\n
0xc000013d | {Insufficient Resources on Remote Computer}\r\nThe remote computer has insufficient resources to complete the network request. For instance, there may not be enough memory available on the remote computer to carry out the request at this time.\r\n
0xc000013e | {Virtual Circuit Closed}\r\nAn existing connection (virtual circuit) has been broken at the remote computer. There is probably something wrong with the network software protocol or the network hardware on the remote computer.\r\n
0xc000013f | {Virtual Circuit Closed}\r\nThe network transport on your computer has closed a network connection because it had to wait too long for a response from the remote computer.\r\n
0xc0000140 | The connection handle given to the transport was invalid.\r\n
0xc0000141 | The address handle given to the transport was invalid.\r\n
0xc0000142 | {DLL Initialization Failed}\r\nInitialization of the dynamic link library %hs failed. The process is terminating abnormally.\r\n
0xc0000143 | {Missing System File}\r\nThe required system file %hs is bad or missing.\r\n
0xc0000144 | {Application Error}\r\nThe exception %s (0x%08lx) occurred in the application at location 0x%08lx.\r\n
0xc0000145 | {Application Error}\r\nThe application failed to initialize properly (0x%lx). Click on OK to terminate the application.\r\n
0xc0000146 | {Unable to Create Paging File}\r\nThe creation of the paging file %hs failed (%lx). The requested size was %ld.\r\n
0xc0000147 | {No Paging File Specified}\r\nNo paging file was specified in the system configuration.\r\n
0xc0000148 | {Incorrect System Call Level}\r\nAn invalid level was passed into the specified system call.\r\n
0xc0000149 | {Incorrect Password to LAN Manager Server}\r\nYou specified an incorrect password to a LAN Manager 2.x or MS-NET server.\r\n
0xc000014a | {EXCEPTION}\r\nA real-mode application issued a floating-point instruction and floating-point hardware is not present.\r\n
0xc000014b | The pipe operation has failed because the other end of the pipe has been closed.\r\n
0xc000014c | {The Registry Is Corrupt}\r\nThe structure of one of the files that contains Registry data is corrupt, or the image of the file in memory is corrupt, or the file could not be recovered because the alternate copy or log was absent or corrupt.\r\n
0xc000014d | An I/O operation initiated by the Registry failed unrecoverably.\r\nThe Registry could not read in, or write out, or flush, one of the files that contain the system's image of the Registry.\r\n
0xc000014e | An event pair synchronization operation was performed using the thread specific client/server event pair object, but no event pair object was associated with the thread.\r\n
0xc000014f | The volume does not contain a recognized file system.\r\nPlease make sure that all required file system drivers are loaded and that the volume is not corrupt.\r\n
0xc0000150 | No serial device was successfully initialized. The serial driver will unload.\r\n
0xc0000151 | The specified local group does not exist.\r\n
0xc0000152 | The specified account name is not a member of the local group.\r\n
0xc0000153 | The specified account name is already a member of the local group.\r\n
0xc0000154 | The specified local group already exists.\r\n
0xc0000155 | A requested type of logon (e.g., Interactive, Network, Service) is not granted by the target system's local security policy.\r\nPlease ask the system administrator to grant the necessary form of logon.\r\n
0xc0000156 | The maximum number of secrets that may be stored in a single system has been exceeded. The length and number of secrets is limited to satisfy United States State Department export restrictions.\r\n
0xc0000157 | The length of a secret exceeds the maximum length allowed. The length and number of secrets is limited to satisfy United States State Department export restrictions.\r\n
0xc0000158 | The Local Security Authority (LSA) database contains an internal inconsistency.\r\n
0xc0000159 | The requested operation cannot be performed in fullscreen mode.\r\n
0xc000015a | During a logon attempt, the user's security context accumulated too many security IDs. This is a very unusual situation.\r\nRemove the user from some global or local groups to reduce the number of security ids to incorporate into the security context.\r\n
0xc000015b | A user has requested a type of logon (e.g., interactive or network) that has not been granted. An administrator has control over who may logon interactively and through the network.\r\n
0xc000015c | The system has attempted to load or restore a file into the registry, and the specified file is not in the format of a registry file.\r\n
0xc000015d | An attempt was made to change a user password in the security account manager without providing the necessary Windows cross-encrypted password.\r\n
0xc000015e | A Windows Server has an incorrect configuration.\r\n
0xc000015f | An attempt was made to explicitly access the secondary copy of information via a device control to the Fault Tolerance driver and the secondary copy is not present in the system.\r\n
0xc0000160 | A configuration registry node representing a driver service entry was ill-formed and did not contain required value entries.\r\n
0xc0000161 | An illegal character was encountered. For a multi-byte character set this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE.\r\n
0xc0000162 | No mapping for the Unicode character exists in the target multi-byte code page.\r\n
0xc0000163 | The Unicode character is not defined in the Unicode character set installed on the system.\r\n
0xc0000164 | The paging file cannot be created on a floppy diskette.\r\n
0xc0000165 | {Floppy Disk Error}\r\nWhile accessing a floppy disk, an ID address mark was not found.\r\n
0xc0000166 | {Floppy Disk Error}\r\nWhile accessing a floppy disk, the track address from the sector ID field was found to be different than the track address maintained by the controller.\r\n
0xc0000167 | {Floppy Disk Error}\r\nThe floppy disk controller reported an error that is not recognized by the floppy disk driver.\r\n
0xc0000168 | {Floppy Disk Error}\r\nWhile accessing a floppy-disk, the controller returned inconsistent results via its registers.\r\n
0xc0000169 | {Hard Disk Error}\r\nWhile accessing the hard disk, a recalibrate operation failed, even after retries.\r\n
0xc000016a | {Hard Disk Error}\r\nWhile accessing the hard disk, a disk operation failed even after retries.\r\n
0xc000016b | {Hard Disk Error}\r\nWhile accessing the hard disk, a disk controller reset was needed, but even that failed.\r\n
0xc000016c | An attempt was made to open a device that was sharing an IRQ with other devices.\r\nAt least one other device that uses that IRQ was already opened.\r\nTwo concurrent opens of devices that share an IRQ and only work via interrupts is not supported for the particular bus type that the devices use.\r\n
0xc000016d | {FT Orphaning}\r\nA disk that is part of a fault-tolerant volume can no longer be accessed.\r\n
0xc000016e | The system bios failed to connect a system interrupt to the device or bus for\r\nwhich the device is connected.\r\n
0xc0000172 | Tape could not be partitioned.\r\n
0xc0000173 | When accessing a new tape of a multivolume partition, the current blocksize is incorrect.\r\n
0xc0000174 | Tape partition information could not be found when loading a tape.\r\n
0xc0000175 | Attempt to lock the eject media mechanism fails.\r\n
0xc0000176 | Unload media fails.\r\n
0xc0000177 | Physical end of tape was detected.\r\n
0xc0000178 | {No Media}\r\nThere is no media in the drive.\r\nPlease insert media into drive %hs.\r\n
0xc000017a | A member could not be added to or removed from the local group because the member does not exist.\r\n
0xc000017b | A new member could not be added to a local group because the member has the wrong account type.\r\n
0xc000017c | Illegal operation attempted on a registry key which has been marked for deletion.\r\n
0xc000017d | System could not allocate required space in a registry log.\r\n
0xc000017e | Too many Sids have been specified.\r\n
0xc000017f | An attempt was made to change a user password in the security account manager without providing the necessary LM cross-encrypted password.\r\n
0xc0000180 | An attempt was made to create a symbolic link in a registry key that already has subkeys or values.\r\n
0xc0000181 | An attempt was made to create a Stable subkey under a Volatile parent key.\r\n
0xc0000182 | The I/O device is configured incorrectly or the configuration parameters to the driver are incorrect.\r\n
0xc0000183 | An error was detected between two drivers or within an I/O driver.\r\n
0xc0000184 | The device is not in a valid state to perform this request.\r\n
0xc0000185 | The I/O device reported an I/O error.\r\n
0xc0000186 | A protocol error was detected between the driver and the device.\r\n
0xc0000187 | This operation is only allowed for the Primary Domain Controller of the domain.\r\n
0xc0000188 | Log file space is insufficient to support this operation.\r\n
0xc0000189 | A write operation was attempted to a volume after it was dismounted.\r\n
0xc000018a | The workstation does not have a trust secret for the primary domain in the local LSA database.\r\n
0xc000018b | The SAM database on the Windows Server does not have a computer account for this workstation trust relationship.\r\n
0xc000018c | The logon request failed because the trust relationship between the primary domain and the trusted domain failed.\r\n
0xc000018d | The logon request failed because the trust relationship between this workstation and the primary domain failed.\r\n
0xc000018e | The Eventlog log file is corrupt.\r\n
0xc000018f | No Eventlog log file could be opened. The Eventlog service did not start.\r\n
0xc0000190 | The network logon failed. This may be because the validation authority can't be reached.\r\n
0xc0000191 | An attempt was made to acquire a mutant such that its maximum count would have been exceeded.\r\n
0xc0000192 | An attempt was made to logon, but the netlogon service was not started.\r\n
0xc0000193 | The user's account has expired.\r\n
0xc0000194 | {EXCEPTION}\r\nPossible deadlock condition.\r\n
0xc0000195 | Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.\r\n
0xc0000196 | An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.\r\n
0xc0000197 | The log file has changed between reads.\r\n
0xc0000198 | The account used is an Interdomain Trust account. Use your global user account or local user account to access this server.\r\n
0xc0000199 | The account used is a Computer Account. Use your global user account or local user account to access this server.\r\n
0xc000019a | The account used is an Server Trust account. Use your global user account or local user account to access this server.\r\n
0xc000019b | The name or SID of the domain specified is inconsistent with the trust information for that domain.\r\n
0xc000019c | A volume has been accessed for which a file system driver is required that has not yet been loaded.\r\n
0xc0000202 | There is no user session key for the specified logon session.\r\n
0xc0000203 | The remote user session has been deleted.\r\n
0xc0000204 | Indicates the specified resource language ID cannot be found in the\r\nimage file.\r\n
0xc0000205 | Insufficient server resources exist to complete the request.\r\n
0xc0000206 | The size of the buffer is invalid for the specified operation.\r\n
0xc0000207 | The transport rejected the network address specified as invalid.\r\n
0xc0000208 | The transport rejected the network address specified due to an invalid use of a wildcard.\r\n
0xc0000209 | The transport address could not be opened because all the available addresses are in use.\r\n
0xc000020a | The transport address could not be opened because it already exists.\r\n
0xc000020b | The transport address is now closed.\r\n
0xc000020c | The transport connection is now disconnected.\r\n
0xc000020d | The transport connection has been reset.\r\n
0xc000020e | The transport cannot dynamically acquire any more nodes.\r\n
0xc000020f | The transport aborted a pending transaction.\r\n
0xc0000210 | The transport timed out a request waiting for a response.\r\n
0xc0000211 | The transport did not receive a release for a pending response.\r\n
0xc0000212 | The transport did not find a transaction matching the specific\r\ntoken.\r\n
0xc0000213 | The transport had previously responded to a transaction request.\r\n
0xc0000214 | The transport does not recognized the transaction request identifier specified.\r\n
0xc0000215 | The transport does not recognize the transaction request type specified.\r\n
0xc0000216 | The transport can only process the specified request on the server side of a session.\r\n
0xc0000217 | The transport can only process the specified request on the client side of a session.\r\n
0xc0000218 | {Registry File Failure}\r\nThe registry cannot load the hive (file):\r\n%hs\r\nor its log or alternate.\r\nIt is corrupt, absent, or not writable.\r\n
0xc0000219 | {Unexpected Failure in DebugActiveProcess}\r\nAn unexpected failure occurred while processing a DebugActiveProcess API request. You may choose OK to terminate the process, or Cancel to ignore the error.\r\n
0xc000021a | {Fatal System Error}\r\nThe %hs system process terminated unexpectedly with a status of 0x%08x (0x%08x 0x%08x).\r\nThe system has been shut down.\r\n
0xc000021b | {Data Not Accepted}\r\nThe TDI client could not handle the data received during an indication.\r\n
0xc000021c | {Unable to Retrieve Browser Server List}\r\nThe list of servers for this workgroup is not currently available.\r\n
0xc000021d | NTVDM encountered a hard error.\r\n
0xc000021e | {Cancel Timeout}\r\nThe driver %hs failed to complete a cancelled I/O request in the allotted time.\r\n
0xc000021f | {Reply Message Mismatch}\r\nAn attempt was made to reply to an LPC message, but the thread specified by the client ID in the message was not waiting on that message.\r\n
0xc0000220 | {Mapped View Alignment Incorrect}\r\nAn attempt was made to map a view of a file, but either the specified base address or the offset into the file were not aligned on the proper allocation granularity.\r\n
0xc0000221 | {Bad Image Checksum}\r\nThe image %hs is possibly corrupt. The header checksum does not match the computed checksum.\r\n
0xc0000222 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0xc0000223 | The parameter(s) passed to the server in the client/server shared memory window were invalid. Too much data may have been put in the shared memory window.\r\n
0xc0000224 | The user's password must be changed before logging on the first time.\r\n
0xc0000225 | The object was not found.\r\n
0xc0000226 | The stream is not a tiny stream.\r\n
0xc0000227 | A transaction recover failed.\r\n
0xc0000228 | The request must be handled by the stack overflow code.\r\n
0xc0000229 | A consistency check failed.\r\n
0xc000022a | The attempt to insert the ID in the index failed because the ID is already in the index.\r\n
0xc000022b | The attempt to set the object's ID failed because the object already has an ID.\r\n
0xc000022c | Internal OFS status codes indicating how an allocation operation is handled. Either it is retried after the containing onode is moved or the extent stream is converted to a large stream.\r\n
0xc000022d | The request needs to be retried.\r\n
0xc000022e | The attempt to find the object found an object matching by ID on the volume but it is out of the scope of the handle used for the operation.\r\n
0xc000022f | The bucket array must be grown. Retry transaction after doing so.\r\n
0xc0000230 | The property set specified does not exist on the object.\r\n
0xc0000231 | The user/kernel marshalling buffer has overflowed.\r\n
0xc0000232 | The supplied variant structure contains invalid data.\r\n
0xc0000233 | Could not find a domain controller for this domain.\r\n
0xc0000234 | The user account has been automatically locked because too many invalid logon attempts or password change attempts have been requested.\r\n
0xc0000235 | NtClose was called on a handle that was protected from close via NtSetInformationObject.\r\n
0xc0000236 | The transport connection attempt was refused by the remote system.\r\n
0xc0000237 | The transport connection was gracefully closed.\r\n
0xc0000238 | The transport endpoint already has an address associated with it.\r\n
0xc0000239 | An address has not yet been associated with the transport endpoint.\r\n
0xc000023a | An operation was attempted on a nonexistent transport connection.\r\n
0xc000023b | An invalid operation was attempted on an active transport connection.\r\n
0xc000023c | The remote network is not reachable by the transport.\r\n
0xc000023d | The remote system is not reachable by the transport.\r\n
0xc000023e | The remote system does not support the transport protocol.\r\n
0xc000023f | No service is operating at the destination port of the transport on the remote system.\r\n
0xc0000240 | The request was aborted.\r\n
0xc0000241 | The transport connection was aborted by the local system.\r\n
0xc0000242 | The specified buffer contains ill-formed data.\r\n
0xc0000243 | The requested operation cannot be performed on a file with a user mapped section open.\r\n
0xc0000244 | {Audit Failed}\r\nAn attempt to generate a security audit failed.\r\n
0xc0000245 | The timer resolution was not previously set by the current process.\r\n
0xc0000246 | A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.\r\n
0xc0000247 | Attempting to login during an unauthorized time of day for this account.\r\n
0xc0000248 | The account is not authorized to login from this station.\r\n
0xc0000249 | {UP/MP Image Mismatch}\r\nThe image %hs has been modified for use on a uniprocessor system, but you are running it on a multiprocessor machine.\r\nPlease reinstall the image file.\r\n
0xc0000250 | There is insufficient account information to log you on.\r\n
0xc0000251 | {Invalid DLL Entrypoint}\r\nThe dynamic link library %hs is not written correctly. The stack pointer has been left in an inconsistent state.\r\nThe entrypoint should be declared as WINAPI or STDCALL. Select YES to fail the DLL load. Select NO to continue execution. Selecting NO may cause the application to operate incorrectly.\r\n
0xc0000252 | {Invalid Service Callback Entrypoint}\r\nThe %hs service is not written correctly. The stack pointer has been left in an inconsistent state.\r\nThe callback entrypoint should be declared as WINAPI or STDCALL. Selecting OK will cause the service to continue operation. However, the service process may operate incorrectly.\r\n
0xc0000253 | The server received the messages but did not send a reply.\r\n
0xc0000254 | There is an IP address conflict with another system on the network\r\n
0xc0000255 | There is an IP address conflict with another system on the network\r\n
0xc0000256 | {Low On Registry Space}\r\nThe system has reached the maximum size allowed for the system part of the registry.  Additional storage requests will be ignored.\r\n
0xc0000257 | The contacted server does not support the indicated part of the DFS namespace.\r\n
0xc0000258 | A callback return system service cannot be executed when no callback is active.\r\n
0xc0000259 | The service being accessed is licensed for a particular number of connections.\r\nNo more connections can be made to the service at this time because there are already as many connections as the service can accept.\r\n
0xc000025a | The password provided is too short to meet the policy of your user account.\r\nPlease choose a longer password.\r\n
0xc000025b | The policy of your user account does not allow you to change passwords too frequently.\r\nThis is done to prevent users from changing back to a familiar, but potentially discovered, password.\r\nIf you feel your password has been compromised then please contact your administrator immediately to have a new one assigned.\r\n
0xc000025c | You have attempted to change your password to one that you have used in the past.\r\nThe policy of your user account does not allow this. Please select a password that you have not previously used.\r\n
0xc000025e | You have attempted to load a legacy device driver while its device instance had been disabled.\r\n
0xc000025f | The specified compression format is unsupported.\r\n
0xc0000260 | The specified hardware profile configuration is invalid.\r\n
0xc0000261 | The specified Plug and Play registry device path is invalid.\r\n
0xc0000262 | {Driver Entry Point Not Found}\r\nThe %hs device driver could not locate the ordinal %ld in driver %hs.\r\n
0xc0000263 | {Driver Entry Point Not Found}\r\nThe %hs device driver could not locate the entry point %hs in driver %hs.\r\n
0xc0000264 | {Application Error}\r\nThe application attempted to release a resource it did not own. Click on OK to terminate the application.\r\n
0xc0000265 | An attempt was made to create more links on a file than the file system supports.\r\n
0xc0000266 | The specified quota list is internally inconsistent with its descriptor.\r\n
0xc0000267 | The specified file has been relocated to offline storage.\r\n
0xc0000268 | {Windows Evaluation Notification}\r\nThe evaluation period for this installation of Windows has expired. This system will shutdown in 1 hour. To restore access to this installation of Windows, please upgrade this installation using a licensed distribution of this product.\r\n
0xc0000269 | {Illegal System DLL Relocation}\r\nThe system DLL %hs was relocated in memory. The application will not run properly.\r\nThe relocation occurred because the DLL %hs occupied an address range reserved for Windows system DLLs. The vendor supplying the DLL should be contacted for a new DLL.\r\n
0xc000026a | {License Violation}\r\nThe system has detected tampering with your registered product type. This is a violation of your software license. Tampering with product type is not permitted.\r\n
0xc000026b | {DLL Initialization Failed}\r\nThe application failed to initialize because the window station is shutting down.\r\n
0xc000026c | {Unable to Load Device Driver}\r\n%hs device driver could not be loaded.\r\nError Status was 0x%x\r\n
0xc000026d | DFS is unavailable on the contacted server.\r\n
0xc000026e | An operation was attempted to a volume after it was dismounted.\r\n
0xc000026f | An internal error occurred in the Win32 x86 emulation subsystem.\r\n
0xc0000270 | Win32 x86 emulation subsystem Floating-point stack check.\r\n
0xc0000271 | The validation process needs to continue on to the next step.\r\n
0xc0000272 | There was no match for the specified key in the index.\r\n
0xc0000273 | There are no more matches for the current index enumeration.\r\n
0xc0000275 | The NTFS file or directory is not a reparse point.\r\n
0xc0000276 | The Windows I/O reparse tag passed for the NTFS reparse point is invalid.\r\n
0xc0000277 | The Windows I/O reparse tag does not match the one present in the NTFS reparse point.\r\n
0xc0000278 | The user data passed for the NTFS reparse point is invalid.\r\n
0xc0000279 | The layered file system driver for this IO tag did not handle it when needed.\r\n
0xc0000280 | The NTFS symbolic link could not be resolved even though the initial file name is valid.\r\n
0xc0000281 | The NTFS directory is a reparse point.\r\n
0xc0000282 | The range could not be added to the range list because of a conflict.\r\n
0xc0000283 | The specified medium changer source element contains no media.\r\n
0xc0000284 | The specified medium changer destination element already contains media.\r\n
0xc0000285 | The specified medium changer element does not exist.\r\n
0xc0000286 | The specified element is contained within a magazine that is no longer present.\r\n
0xc0000287 | The device requires reinitialization due to hardware errors.\r\n
0xc000028a | The file encryption attempt failed.\r\n
0xc000028b | The file decryption attempt failed.\r\n
0xc000028c | The specified range could not be found in the range list.\r\n
0xc000028d | There is no encryption recovery policy configured for this system.\r\n
0xc000028e | The required encryption driver is not loaded for this system.\r\n
0xc000028f | The file was encrypted with a different encryption driver than is currently loaded.\r\n
0xc0000290 | There are no EFS keys defined for the user.\r\n
0xc0000291 | The specified file is not encrypted.\r\n
0xc0000292 | The specified file is not in the defined EFS export format.\r\n
0xc0000293 | The specified file is encrypted and the user does not have the ability to decrypt it.\r\n
0xc0000295 | The guid passed was not recognized as valid by a WMI data provider.\r\n
0xc0000296 | The instance name passed was not recognized as valid by a WMI data provider.\r\n
0xc0000297 | The data item id passed was not recognized as valid by a WMI data provider.\r\n
0xc0000298 | The WMI request could not be completed and should be retried.\r\n
0xc0000299 | The policy object is shared and can only be modified at the root\r\n
0xc000029a | The policy object does not exist when it should\r\n
0xc000029b | The requested policy information only lives in the Ds\r\n
0xc000029c | The volume must be upgraded to enable this feature\r\n
0xc000029d | The remote storage service is not operational at this time.\r\n
0xc000029e | The remote storage service encountered a media error.\r\n
0xc000029f | The tracking (workstation) service is not running.\r\n
0xc00002a0 | The server process is running under a SID different than that required by client.\r\n
0xc00002a1 | The specified directory service attribute or value does not exist.\r\n
0xc00002a2 | The attribute syntax specified to the directory service is invalid.\r\n
0xc00002a3 | The attribute type specified to the directory service is not defined.\r\n
0xc00002a4 | The specified directory service attribute or value already exists.\r\n
0xc00002a5 | The directory service is busy.\r\n
0xc00002a6 | The directory service is not available.\r\n
0xc00002a7 | The directory service was unable to allocate a relative identifier.\r\n
0xc00002a8 | The directory service has exhausted the pool of relative identifiers.\r\n
0xc00002a9 | The requested operation could not be performed because the directory service is not the master for that type of operation.\r\n
0xc00002aa | The directory service was unable to initialize the subsystem that allocates relative identifiers.\r\n
0xc00002ab | The requested operation did not satisfy one or more constraints associated with the class of the object.\r\n
0xc00002ac | The directory service can perform the requested operation only on a leaf object.\r\n
0xc00002ad | The directory service cannot perform the requested operation on the Relatively Defined Name (RDN) attribute of an object.\r\n
0xc00002ae | The directory service detected an attempt to modify the object class of an object.\r\n
0xc00002af | An error occurred while performing a cross domain move operation.\r\n
0xc00002b0 | Unable to Contact the Global Catalog Server.\r\n
0xc00002b1 | The requested operation requires a directory service, and none was available.\r\n
0xc00002b2 | The reparse attribute cannot be set as it is incompatible with an existing attribute.\r\n
0xc00002b3 | A group marked use for deny only  can not be enabled.\r\n
0xc00002b4 | {EXCEPTION}\r\nMultiple floating point faults.\r\n
0xc00002b5 | {EXCEPTION}\r\nMultiple floating point traps.\r\n
0xc00002b6 | The device has been removed.\r\n
0xc00002b7 | The volume change journal is being deleted.\r\n
0xc00002b8 | The volume change journal is not active.\r\n
0xc00002b9 | The requested interface is not supported.\r\n
0xc00002c1 | A directory service resource limit has been exceeded.\r\n
0xc00002c2 | {System Standby Failed}\r\nThe driver %hs does not support standby mode. Updating this driver may allow the system to go to standby mode.\r\n
0xc00002c3 | Mutual Authentication failed. The server's password is out of date at the domain controller.\r\n
0xc00002c4 | The system file %1 has become corrupt and has been replaced.\r\n
0xc00002c5 | {EXCEPTION}\r\nAlignment Error\r\nA datatype misalignment error was detected in a load or store instruction.\r\n
0xc00002c6 | The WMI data item or data block is read only.\r\n
0xc00002c7 | The WMI data item or data block could not be changed.\r\n
0xc00002c8 | {Virtual Memory Minimum Too Low}\r\nYour system is low on virtual memory. Windows is increasing the size of your virtual memory paging file.\r\nDuring this process, memory requests for some applications may be denied. For more information, see Help.\r\n
0xc00002c9 | {EXCEPTION}\r\nRegister NaT consumption faults.\r\nA NaT value is consumed on a non speculative instruction.\r\n
0xc00002ca | The medium changer's transport element contains media, which is causing the operation to fail.\r\n
0xc00002cb | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.\r\n
0xc00002cc | This operation is supported only when you are connected to the server.\r\n
0xc00002cd | Only an administrator can modify the membership list of an administrative group.\r\n
0xc00002ce | A device was removed so enumeration must be restarted.\r\n
0xc00002cf | The journal entry has been deleted from the journal.\r\n
0xc00002d0 | Cannot change the primary group ID of a domain controller account.\r\n
0xc00002d1 | {Fatal System Error}\r\nThe system image %s is not properly signed.\r\nThe file has been replaced with the signed file.\r\nThe system has been shut down.\r\n
0xc00002d2 | Device will not start without a reboot.\r\n
0xc00002d3 | Current device power state cannot support this request.\r\n
0xc00002d4 | The specified group type is invalid.\r\n
0xc00002d5 | In mixed domain no nesting of global group if group is security enabled.\r\n
0xc00002d6 | In mixed domain, cannot nest local groups with other local groups, if the group is security enabled.\r\n
0xc00002d7 | A global group cannot have a local group as a member.\r\n
0xc00002d8 | A global group cannot have a universal group as a member.\r\n
0xc00002d9 | A universal group cannot have a local group as a member.\r\n
0xc00002da | A global group cannot have a cross domain member.\r\n
0xc00002db | A local group cannot have another cross domain local group as a member.\r\n
0xc00002dc | Can not change to security disabled group because of having primary members in this group.\r\n
0xc00002dd | The WMI operation is not supported by the data block or method.\r\n
0xc00002de | There is not enough power to complete the requested operation.\r\n
0xc00002df | Security Account Manager needs to get the boot password.\r\n
0xc00002e0 | Security Account Manager needs to get the boot key from floppy disk.\r\n
0xc00002e1 | Directory Service can not start.\r\n
0xc00002e2 | Directory Services could not start because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.\r\n
0xc00002e3 | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Safe Mode, check the event log for more detailed information.\r\n
0xc00002e4 | The requested operation can be performed only on a global catalog server.\r\n
0xc00002e5 | A local group can only be a member of other local groups in the same domain.\r\n
0xc00002e6 | Foreign security principals cannot be members of universal groups.\r\n
0xc00002e7 | Your computer could not be joined to the domain. You have exceeded the maximum number of computer accounts you are allowed to create in this domain. Contact your system administrator to have this limit reset or increased.\r\n
0xc00002e8 | STATUS_MULTIPLE_FAULT_VIOLATION\r\n
0xc00002e9 | This operation can not be performed on the current domain.\r\n
0xc00002ea | The directory or file cannot be created.\r\n
0xc00002eb | The system is in the process of shutting down.\r\n
0xc00002ec | Directory Services could not start because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown the system. You can use the recovery console to diagnose the system further.\r\n
0xc00002ed | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown the system. You can use the recovery console to diagnose the system further.\r\n
0xc00002ee | A security context was deleted before the context was completed.  This is considered a logon failure.\r\n
0xc00002ef | The client is trying to negotiate a context and the server requires user-to-user but didn't send a TGT reply.\r\n
0xc00002f0 | An object ID was not found in the file.\r\n
0xc00002f1 | Unable to accomplish the requested task because the local machine does not have any IP addresses.\r\n
0xc00002f2 | The supplied credential handle does not match the credential associated with the security context.\r\n
0xc00002f3 | The crypto system or checksum function is invalid because a required function is unavailable.\r\n
0xc00002f4 | The number of maximum ticket referrals has been exceeded.\r\n
0xc00002f5 | The local machine must be a Kerberos KDC (domain controller) and it is not.\r\n
0xc00002f6 | The other end of the security negotiation is requires strong crypto but it is not supported on the local machine.\r\n
0xc00002f7 | The KDC reply contained more than one principal name.\r\n
0xc00002f8 | Expected to find PA data for a hint of what etype to use, but it was not found.\r\n
0xc00002f9 | The client certificate does not contain a valid UPN, or does not match the client name \r\nin the logon request.  Please contact your administrator.\r\n
0xc00002fa | Smartcard logon is required and was not used.\r\n
0xc00002fb | An invalid request was sent to the KDC.\r\n
0xc00002fc | The KDC was unable to generate a referral for the service requested.\r\n
0xc00002fd | The encryption type requested is not supported by the KDC.\r\n
0xc00002fe | A system shutdown is in progress.\r\n
0xc00002ff | The server machine is shutting down.\r\n
0xc0000300 | This operation is not supported on a computer running Windows Server 2003 for Small Business Server\r\n
0xc0000301 | The WMI GUID is no longer available\r\n
0xc0000302 | Collection or events for the WMI GUID is already disabled.\r\n
0xc0000303 | Collection or events for the WMI GUID is already enabled.\r\n
0xc0000304 | The Master File Table on the volume is too fragmented to complete this operation.\r\n
0xc0000305 | Copy protection failure.\r\n
0xc0000306 | Copy protection error - DVD CSS Authentication failed.\r\n
0xc0000307 | Copy protection error - The given sector does not contain a valid key.\r\n
0xc0000308 | Copy protection error - DVD session key not established.\r\n
0xc0000309 | Copy protection error - The read failed because the sector is encrypted.\r\n
0xc000030a | Copy protection error - The given DVD's region does not correspond to the\r\nregion setting of the drive.\r\n
0xc000030b | Copy protection error - The drive's region setting may be permanent.\r\n
0xc0000320 | The kerberos protocol encountered an error while validating the KDC certificate during smartcard Logon.  There\r\nis more information in the system event log.\r\n
0xc0000321 | The kerberos protocol encountered an error while attempting to utilize the smartcard subsystem.\r\n
0xc0000322 | The target server does not have acceptable kerberos credentials.\r\n
0xc0000350 | The transport determined that the remote system is down.\r\n
0xc0000351 | An unsupported preauthentication mechanism was presented to the kerberos package.\r\n
0xc0000352 | The encryption algorithm used on the source file needs a bigger key buffer than the one used on the destination file.\r\n
0xc0000353 | An attempt to remove a processes DebugPort was made, but a port was not already associated with the process.\r\n
0xc0000354 | An attempt to do an operation on a debug port failed because the port is in the process of being deleted.\r\n
0xc0000355 | This version of Windows is not compatible with the behavior version of directory forest, domain or domain controller.\r\n
0xc0000356 | The specified event is currently not being audited.\r\n
0xc0000357 | The machine account was created pre-NT4.  The account needs to be recreated.\r\n
0xc0000358 | A account group can not have a universal group as a member.\r\n
0xc0000359 | The specified image file did not have the correct format, it appears to be a 32-bit Windows image.\r\n
0xc000035a | The specified image file did not have the correct format, it appears to be a 64-bit Windows image.\r\n
0xc000035b | Client's supplied SSPI channel bindings were incorrect.\r\n
0xc000035c | The client's session has expired, so the client must reauthenticate to continue accessing the remote resources.\r\n
0xc000035d | AppHelp dialog canceled thus preventing the application from starting.\r\n
0xc000035e | The SID filtering operation removed all SIDs.\r\n
0xc000035f | The driver was not loaded because the system is booting into safe mode.\r\n
0xc0000361 | Access to %1 has been restricted by your Administrator by the default software restriction policy level.\r\n
0xc0000362 | Access to %1 has been restricted by your Administrator by location with policy rule %2 placed on path %3\r\n
0xc0000363 | Access to %1 has been restricted by your Administrator by software publisher policy.\r\n
0xc0000364 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0xc0000365 | The driver was not loaded because it failed it's initialization call.\r\n
0xc0000366 | The "%hs" encountered an error while applying power or reading the device configuration.\r\nThis may be caused by a failure of your hardware or by a poor connection.\r\n
0xc0000368 | The create operation failed because the name contained at least one mount point which resolves to a volume to which the specified device object is not attached.\r\n
0xc0000369 | The device object parameter is either not a valid device object or is not attached to the volume specified by the file name.\r\n
0xc000036a | A Machine Check Error has occurred. Please check the system eventlog for additional information.\r\n
0xc000036b | Driver %2 has been blocked from loading.\r\n
0xc000036c | Driver %2 has been blocked from loading.\r\n
0xc000036d | There was error [%2] processing the driver database.\r\n
0xc000036e | System hive size has exceeded its limit.\r\n
0xc000036f | A dynamic link library (DLL) referenced a module that was neither a DLL nor the process's executable image.\r\n
0xc0000380 | An incorrect PIN was presented to the smart card\r\n
0xc0000381 | The smart card is blocked\r\n
0xc0000382 | No PIN was presented to the smart card\r\n
0xc0000383 | No smart card available\r\n
0xc0000384 | The requested key container does not exist on the smart card\r\n
0xc0000385 | The requested certificate does not exist on the smart card\r\n
0xc0000386 | The requested keyset does not exist\r\n
0xc0000387 | A communication error with the smart card has been detected.\r\n
0xc0000388 | The system detected a possible attempt to compromise security. Please ensure that you can contact the server that authenticated you.\r\n
0xc0000389 | The smartcard certificate used for authentication has been revoked.\r\nPlease contact your system administrator.  There may be additional information in the\r\nevent log.\r\n
0xc000038a | An untrusted certificate authority was detected While processing the\r\nsmartcard certificate used for authentication.  Please contact your system\r\nadministrator.\r\n
0xc000038b | The revocation status of the smartcard certificate used for\r\nauthentication could not be determined. Please contact your system administrator.\r\n
0xc000038c | The smartcard certificate used for authentication was not trusted.  Please\r\ncontact your system administrator.\r\n
0xc000038d | The smartcard certificate used for authentication has expired.  Please\r\ncontact your system administrator.\r\n
0xc000038e | The driver could not be loaded because a previous version of the driver is still in memory.\r\n
0xc000038f | The smartcard provider could not perform the action since the context was acquired as silent.\r\n
0xc0000401 | The current user's delegated trust creation quota has been exceeded.\r\n
0xc0000402 | The total delegated trust creation quota has been exceeded.\r\n
0xc0000403 | The current user's delegated trust deletion quota has been exceeded.\r\n
0xc0000404 | The requested name already exists as a unique identifier.\r\n
0xc0000405 | The requested object has a non-unique identifier and cannot be retrieved.\r\n
0xc0000406 | The group cannot be converted due to attribute restrictions on the requested group type.\r\n
0xc0000407 | {Volume Shadow Copy Service}\r\nPlease wait while the Volume Shadow Copy Service prepares volume %hs for hibernation.\r\n
0xc0000408 | Kerberos sub-protocol User2User is required.\r\n
0xc0000409 | The system detected an overrun of a stack-based buffer in this application.  This\r\noverrun could potentially allow a malicious user to gain control of this application.\r\n
0xc000040a | The Kerberos subsystem encountered an error.  A service for user protocol request was made \r\nagainst a domain controller which does not support service for user.\r\n
0xc000040b | An attempt was made by this server to make a Kerberos constrained delegation request for a target\r\noutside of the server's realm.  This is not supported, and indicates a misconfiguration on this\r\nserver's allowed to delegate to list.  Please contact your administrator.\r\n
0xc000040c | The revocation status of the domain controller certificate used for smartcard\r\nauthentication could not be determined.  There is additional information in the system event\r\nlog. Please contact your system administrator.\r\n
0xc000040d | An untrusted certificate authority was detected while processing the\r\ndomain controller certificate used for authentication.  There is additional information in\r\nthe system event log.  Please contact your system administrator.\r\n
0xc000040e | The domain controller certificate used for smartcard logon has expired.\r\nPlease contact your system administrator with the contents of your system event log.\r\n
0xc000040f | The domain controller certificate used for smartcard logon has been revoked.\r\nPlease contact your system administrator with the contents of your system event log.\r\n
0xc0000410 | Data present in one of the parameters is more than the function can operate on.\r\n
0xc0000411 | The system has failed to hibernate (The error code is %hs).  Hibernation will be disabled until the system is restarted.\r\n
0xc0000412 | An attempt to delay-load a .dll or get a function address in a delay-loaded .dll failed.\r\n
0xc0000413 | Logon Failure: The machine you are logging onto is protected by an authentication firewall.  The specified account is not allowed to authenticate to the machine.\r\n
0xc0000414 | %hs is a 16-bit application. You do not have permissions to execute 16-bit applications. Check your permissions with your system administrator.\r\n
0xc0000415 | {Display Driver Stopped Responding}\r\nThe %hs display driver has stopped working normally.  Save your work and reboot the system to restore full display functionality.\r\nThe next time you reboot the machine a dialog will be displayed giving you a chance to report this failure to Microsoft.\r\n
0xc0009898 | WOW Assertion Error.\r\n
0xc0010001 | Debugger did not perform a state change.\r\n
0xc0010002 | Debugger has found the application is not idle.\r\n
0xc0020001 | The string binding is invalid.\r\n
0xc0020002 | The binding handle is not the correct type.\r\n
0xc0020003 | The binding handle is invalid.\r\n
0xc0020004 | The RPC protocol sequence is not supported.\r\n
0xc0020005 | The RPC protocol sequence is invalid.\r\n
0xc0020006 | The string UUID is invalid.\r\n
0xc0020007 | The endpoint format is invalid.\r\n
0xc0020008 | The network address is invalid.\r\n
0xc0020009 | No endpoint was found.\r\n
0xc002000a | The timeout value is invalid.\r\n
0xc002000b | The object UUID was not found.\r\n
0xc002000c | The object UUID has already been registered.\r\n
0xc002000d | The type UUID has already been registered.\r\n
0xc002000e | The RPC server is already listening.\r\n
0xc002000f | No protocol sequences have been registered.\r\n
0xc0020010 | The RPC server is not listening.\r\n
0xc0020011 | The manager type is unknown.\r\n
0xc0020012 | The interface is unknown.\r\n
0xc0020013 | There are no bindings.\r\n
0xc0020014 | There are no protocol sequences.\r\n
0xc0020015 | The endpoint cannot be created.\r\n
0xc0020016 | Not enough resources are available to complete this operation.\r\n
0xc0020017 | The RPC server is unavailable.\r\n
0xc0020018 | The RPC server is too busy to complete this operation.\r\n
0xc0020019 | The network options are invalid.\r\n
0xc002001a | There are no remote procedure calls active on this thread.\r\n
0xc002001b | The remote procedure call failed.\r\n
0xc002001c | The remote procedure call failed and did not execute.\r\n
0xc002001d | An RPC protocol error occurred.\r\n
0xc002001f | The transfer syntax is not supported by the RPC server.\r\n
0xc0020021 | The type UUID is not supported.\r\n
0xc0020022 | The tag is invalid.\r\n
0xc0020023 | The array bounds are invalid.\r\n
0xc0020024 | The binding does not contain an entry name.\r\n
0xc0020025 | The name syntax is invalid.\r\n
0xc0020026 | The name syntax is not supported.\r\n
0xc0020028 | No network address is available to use to construct a UUID.\r\n
0xc0020029 | The endpoint is a duplicate.\r\n
0xc002002a | The authentication type is unknown.\r\n
0xc002002b | The maximum number of calls is too small.\r\n
0xc002002c | The string is too long.\r\n
0xc002002d | The RPC protocol sequence was not found.\r\n
0xc002002e | The procedure number is out of range.\r\n
0xc002002f | The binding does not contain any authentication information.\r\n
0xc0020030 | The authentication service is unknown.\r\n
0xc0020031 | The authentication level is unknown.\r\n
0xc0020032 | The security context is invalid.\r\n
0xc0020033 | The authorization service is unknown.\r\n
0xc0020034 | The entry is invalid.\r\n
0xc0020035 | The operation cannot be performed.\r\n
0xc0020036 | There are no more endpoints available from the endpoint mapper.\r\n
0xc0020037 | No interfaces have been exported.\r\n
0xc0020038 | The entry name is incomplete.\r\n
0xc0020039 | The version option is invalid.\r\n
0xc002003a | There are no more members.\r\n
0xc002003b | There is nothing to unexport.\r\n
0xc002003c | The interface was not found.\r\n
0xc002003d | The entry already exists.\r\n
0xc002003e | The entry is not found.\r\n
0xc002003f | The name service is unavailable.\r\n
0xc0020040 | The network address family is invalid.\r\n
0xc0020041 | The requested operation is not supported.\r\n
0xc0020042 | No security context is available to allow impersonation.\r\n
0xc0020043 | An internal error occurred in RPC.\r\n
0xc0020044 | The RPC server attempted an integer divide by zero.\r\n
0xc0020045 | An addressing error occurred in the RPC server.\r\n
0xc0020046 | A floating point operation at the RPC server caused a divide by zero.\r\n
0xc0020047 | A floating point underflow occurred at the RPC server.\r\n
0xc0020048 | A floating point overflow occurred at the RPC server.\r\n
0xc0020049 | A remote procedure call is already in progress for this thread.\r\n
0xc002004a | There are no more bindings.\r\n
0xc002004b | The group member was not found.\r\n
0xc002004c | The endpoint mapper database entry could not be created.\r\n
0xc002004d | The object UUID is the nil UUID.\r\n
0xc002004f | No interfaces have been registered.\r\n
0xc0020050 | The remote procedure call was cancelled.\r\n
0xc0020051 | The binding handle does not contain all required information.\r\n
0xc0020052 | A communications failure occurred during a remote procedure call.\r\n
0xc0020053 | The requested authentication level is not supported.\r\n
0xc0020054 | No principal name registered.\r\n
0xc0020055 | The error specified is not a valid Windows RPC error code.\r\n
0xc0020057 | A security package specific error occurred.\r\n
0xc0020058 | Thread is not cancelled.\r\n
0xc0020062 | Invalid asynchronous remote procedure call handle.\r\n
0xc0020063 | Invalid asynchronous RPC call handle for this operation.\r\n
0xc0030001 | The list of RPC servers available for auto-handle binding has been exhausted.\r\n
0xc0030002 | The file designated by DCERPCCHARTRANS cannot be opened.\r\n
0xc0030003 | The file containing the character translation table has fewer than 512 bytes.\r\n
0xc0030004 | A null context handle is passed as an [in] parameter.\r\n
0xc0030005 | The context handle does not match any known context handles.\r\n
0xc0030006 | The context handle changed during a call.\r\n
0xc0030007 | The binding handles passed to a remote procedure call do not match.\r\n
0xc0030008 | The stub is unable to get the call handle.\r\n
0xc0030009 | A null reference pointer was passed to the stub.\r\n
0xc003000a | The enumeration value is out of range.\r\n
0xc003000b | The byte count is too small.\r\n
0xc003000c | The stub received bad data.\r\n
0xc0030059 | Invalid operation on the encoding/decoding handle.\r\n
0xc003005a | Incompatible version of the serializing package.\r\n
0xc003005b | Incompatible version of the RPC stub.\r\n
0xc003005c | The RPC pipe object is invalid or corrupted.\r\n
0xc003005d | An invalid operation was attempted on an RPC pipe object.\r\n
0xc003005e | Unsupported RPC pipe version.\r\n
0xc003005f | The RPC pipe object has already been closed.\r\n
0xc0030060 | The RPC call completed before all pipes were processed.\r\n
0xc0030061 | No more data is available from the RPC pipe.\r\n
0xc0040035 | A device is missing in the system BIOS MPS table. This device will not be used.\r\nPlease contact your system vendor for system BIOS update.\r\n
0xc0040036 | A translator failed to translate resources.\r\n
0xc0040037 | A IRQ translator failed to translate resources.\r\n
0xc0040038 | Driver %2 returned invalid ID for a child device (%3).\r\n
0xc00a0001 | Session name %1 is invalid.\r\n
0xc00a0002 | The protocol driver %1 is invalid.\r\n
0xc00a0003 | The protocol driver %1 was not found in the system path.\r\n
0xc00a0006 | A close operation is pending on the Terminal Connection.\r\n
0xc00a0007 | There are no free output buffers available.\r\n
0xc00a0008 | The MODEM.INF file was not found.\r\n
0xc00a0009 | The modem (%1) was not found in MODEM.INF.\r\n
0xc00a000a | The modem did not accept the command sent to it.\r\nVerify the configured modem name matches the attached modem.\r\n
0xc00a000b | The modem did not respond to the command sent to it.\r\nVerify the modem is properly cabled and powered on.\r\n
0xc00a000c | Carrier detect has failed or carrier has been dropped due to disconnect.\r\n
0xc00a000d | Dial tone not detected within required time.\r\nVerify phone cable is properly attached and functional.\r\n
0xc00a000e | Busy signal detected at remote site on callback.\r\n
0xc00a000f | Voice detected at remote site on callback.\r\n
0xc00a0010 | Transport driver error\r\n
0xc00a0012 | The client you are using is not licensed to use this system. Your logon request is denied.\r\n
0xc00a0013 | The system has reached its licensed logon limit.\r\nPlease try again later.\r\n
0xc00a0014 | The system license has expired. Your logon request is denied.\r\n
0xc00a0015 | The specified session cannot be found.\r\n
0xc00a0016 | The specified session name is already in use.\r\n
0xc00a0017 | The requested operation cannot be completed because the Terminal Connection is currently busy processing a connect, disconnect, reset, or delete operation.\r\n
0xc00a0018 | An attempt has been made to connect to a session whose video mode is not supported by the current client.\r\n
0xc00a0022 | The application attempted to enable DOS graphics mode.\r\nDOS graphics mode is not supported.\r\n
0xc00a0024 | The requested operation can be performed only on the system console.\r\nThis is most often the result of a driver or system DLL requiring direct console access.\r\n
0xc00a0026 | The client failed to respond to the server connect message.\r\n
0xc00a0027 | Disconnecting the console session is not supported.\r\n
0xc00a0028 | Reconnecting a disconnected session to the console is not supported.\r\n
0xc00a002a | The request to control another session remotely was denied.\r\n
0xc00a002b | A process has requested access to a session, but has not been granted those access rights.\r\n
0xc00a002e | The Terminal Connection driver %1 is invalid.\r\n
0xc00a002f | The Terminal Connection driver %1 was not found in the system path.\r\n
0xc00a0030 | The requested session cannot be controlled remotely.\r\nYou cannot control your own session, a session that is trying to control your session,\r\na session that has no user logged on, nor control other sessions from the console.\r\n
0xc00a0031 | The requested session is not configured to allow remote control.\r\n
0xc00a0032 | The RDP protocol component %2 detected an error in the protocol stream and has disconnected the client.\r\n
0xc00a0033 | Your request to connect to this Terminal server has been rejected.\r\nYour Terminal Server Client license number has not been entered for this copy of the Terminal Client.\r\nPlease call your system administrator for help in entering a valid, unique license number for this Terminal Server Client.\r\nClick OK to continue.\r\n
0xc00a0034 | Your request to connect to this Terminal server has been rejected.\r\nYour Terminal Server Client license number is currently being used by another user.\r\nPlease call your system administrator to obtain a new copy of the Terminal Server Client with a valid, unique license number.\r\nClick OK to continue.\r\n
0xc00a0035 | The remote control of the console was terminated because the display mode was changed. Changing the display mode in a remote control session is not supported.\r\n
0xc00a0036 | Remote control could not be terminated because the specified session is not currently being remotely controlled.\r\n
0xc0130001 | The cluster node is not valid.\r\n
0xc0130002 | The cluster node already exists.\r\n
0xc0130003 | A node is in the process of joining the cluster.\r\n
0xc0130004 | The cluster node was not found.\r\n
0xc0130005 | The cluster local node information was not found.\r\n
0xc0130006 | The cluster network already exists.\r\n
0xc0130007 | The cluster network was not found.\r\n
0xc0130008 | The cluster network interface already exists.\r\n
0xc0130009 | The cluster network interface was not found.\r\n
0xc013000a | The cluster request is not valid for this object.\r\n
0xc013000b | The cluster network provider is not valid.\r\n
0xc013000c | The cluster node is down.\r\n
0xc013000d | The cluster node is not reachable.\r\n
0xc013000e | The cluster node is not a member of the cluster.\r\n
0xc013000f | A cluster join operation is not in progress.\r\n
0xc0130010 | The cluster network is not valid.\r\n
0xc0130011 | No network adapters are available.\r\n
0xc0130012 | The cluster node is up.\r\n
0xc0130013 | The cluster node is paused.\r\n
0xc0130014 | The cluster node is not paused.\r\n
0xc0130015 | No cluster security context is available.\r\n
0xc0130016 | The cluster network is not configured for internal cluster communication.\r\n
0xc0130017 | The cluster node has been poisoned.\r\n
0xc0140001 | An attempt was made to run an invalid AML opcode\r\n
0xc0140002 | The AML Interpreter Stack has overflowed\r\n
0xc0140003 | An inconsistent state has occurred\r\n
0xc0140004 | An attempt was made to access an array outside of its bounds\r\n
0xc0140005 | A required argument was not specified\r\n
0xc0140006 | A fatal error has occurred\r\n
0xc0140007 | An invalid SuperName was specified\r\n
0xc0140008 | An argument with an incorrect type was specified\r\n
0xc0140009 | An object with an incorrect type was specified\r\n
0xc014000a | A target with an incorrect type was specified\r\n
0xc014000b | An incorrect number of arguments were specified\r\n
0xc014000c | An address failed to translate\r\n
0xc014000d | An incorrect event type was specified\r\n
0xc014000e | A handler for the target already exists\r\n
0xc014000f | Invalid data for the target was specified\r\n
0xc0140010 | An invalid region for the target was specified\r\n
0xc0140011 | An attempt was made to access a field outside of the defined range\r\n
0xc0140012 | The Global system lock could not be acquired\r\n
0xc0140013 | An attempt was made to reinitialize the ACPI subsystem\r\n
0xc0140014 | The ACPI subsystem has not been initialized\r\n
0xc0140015 | An incorrect mutex was specified\r\n
0xc0140016 | The mutex is not currently owned\r\n
0xc0140017 | An attempt was made to access the mutex by a process that was not the owner\r\n
0xc0140018 | An error occurred during an access to Region Space\r\n
0xc0140019 | An attempt was made to use an incorrect table\r\n
0xc0140020 | The registration of an ACPI event failed\r\n
0xc0140021 | An ACPI Power Object failed to transition state\r\n
0xc0150001 | The requested section is not present in the activation context.\r\n
0xc0150002 | Windows was not able to process the application binding information.\r\nPlease refer to your System Event Log for further information.\r\n
0xc0150003 | The application binding data format is invalid.\r\n
0xc0150004 | The referenced assembly is not installed on your system.\r\n
0xc0150005 | The manifest file does not begin with the required tag and format information.\r\n
0xc0150006 | The manifest file contains one or more syntax errors.\r\n
0xc0150007 | The application attempted to activate a disabled activation context.\r\n
0xc0150008 | The requested lookup key was not found in any active activation context.\r\n
0xc0150009 | A component version required by the application conflicts with another component version already active.\r\n
0xc015000a | The type requested activation context section does not match the query API used.\r\n
0xc015000b | Lack of system resources has required isolated activation to be disabled for the current thread of execution.\r\n
0xc015000c | The referenced assembly could not be found.\r\n
0xc015000e | An attempt to set the process default activation context failed because the process default activation context was already set.\r\n
0xc015000f | The activation context being deactivated is not the most recently activated one.\r\n
0xc0150010 | The activation context being deactivated is not active for the current thread of execution.\r\n
0xc0150011 | The activation context being deactivated has already been deactivated.\r\n
0xc0150012 | The activation context of system default assembly could not be generated.\r\n
0xc0150013 | A component used by the isolation facility has requested to terminate the process.\r\n
0xc0150014 | The activation context activation stack for the running thread of execution is corrupt.\r\n
0xc0150015 | The application isolation metadata for this process or thread has become corrupt.\r\n

### 6.0.6000.16386

Message identifier | Message string
--- | ---
0x00000000 | STATUS_WAIT_0\r\n
0x00000001 | STATUS_WAIT_1\r\n
0x00000002 | STATUS_WAIT_2\r\n
0x00000003 | STATUS_WAIT_3\r\n
0x0000003f | STATUS_WAIT_63\r\n
0x00000080 | STATUS_ABANDONED_WAIT_0\r\n
0x000000bf | STATUS_ABANDONED_WAIT_63\r\n
0x000000c0 | STATUS_USER_APC\r\n
0x00000100 | STATUS_KERNEL_APC\r\n
0x00000101 | STATUS_ALERTED\r\n
0x00000102 | STATUS_TIMEOUT\r\n
0x00000103 | The operation that was requested is pending completion.\r\n
0x00000104 | A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.\r\n
0x00000105 | Returned by enumeration APIs to indicate more information is available to successive calls.\r\n
0x00000106 | Indicates not all privileges or groups referenced are assigned to the caller.\r\nThis allows, for example, all privileges to be disabled without having to know exactly which privileges are assigned.\r\n
0x00000107 | Some of the information to be translated has not been translated.\r\n
0x00000108 | An open/create operation completed while an oplock break is underway.\r\n
0x00000109 | A new volume has been mounted by a file system.\r\n
0x0000010a | This success level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.\r\nThe commit has now been completed.\r\n
0x0000010b | This indicates that a notify change request has been completed due to closing the handle which made the notify change request.\r\n
0x0000010c | This indicates that a notify change request is being completed and that the information is not being returned in the caller's buffer.\r\nThe caller now needs to enumerate the files to find the changes.\r\n
0x0000010d | {No Quotas}\r\nNo system quota limits are specifically set for this account.\r\n
0x0000010e | {Connect Failure on Primary Transport}\r\nAn attempt was made to connect to the remote server %hs on the primary transport, but the connection failed.\r\nThe computer WAS able to connect on a secondary transport.\r\n
0x00000110 | Page fault was a transition fault.\r\n
0x00000111 | Page fault was a demand zero fault.\r\n
0x00000112 | Page fault was a demand zero fault.\r\n
0x00000113 | Page fault was a demand zero fault.\r\n
0x00000114 | Page fault was satisfied by reading from a secondary storage device.\r\n
0x00000115 | Cached page was locked during operation.\r\n
0x00000116 | Crash dump exists in paging file.\r\n
0x00000117 | Specified buffer contains all zeros.\r\n
0x00000118 | A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.\r\n
0x00000119 | The device has succeeded a query-stop and its resource requirements have changed.\r\n
0x00000120 | The translator has translated these resources into the global space and no further translations should be performed.\r\n
0x00000121 | The directory service evaluated group memberships locally, as it was unable to contact a global catalog server.\r\n
0x00000122 | A process being terminated has no threads to terminate.\r\n
0x00000123 | The specified process is not part of a job.\r\n
0x00000124 | The specified process is part of a job.\r\n
0x00000125 | {Volume Shadow Copy Service}\r\nThe system is now ready for hibernation.\r\n
0x00000126 | A file system or file system filter driver has successfully completed an FsFilter operation.\r\n
0x00000127 | The specified interrupt vector was already connected.\r\n
0x00000128 | The specified interrupt vector is still connected.\r\n
0x00000129 | The current process is a cloned process.\r\n
0x0000012a | The file was locked and all users of the file can only read.\r\n
0x0000012b | The file was locked and at least one user of the file can write.\r\n
0x00000202 | The specified ResourceManager made no changes or updates to the resource under this transaction.\r\n
0x00000367 | An operation is blocked waiting for an oplock.\r\n
0x00010001 | Debugger handled exception\r\n
0x00010002 | Debugger continued\r\n
0x001c0001 | The IO was completed by a filter.\r\n
0x40000000 | {Object Exists}\r\nAn attempt was made to create an object and the object name already existed.\r\n
0x40000001 | {Thread Suspended}\r\nA thread termination occurred while the thread was suspended. The thread was resumed, and termination proceeded.\r\n
0x40000002 | {Working Set Range Error}\r\nAn attempt was made to set the working set minimum or maximum to values which are outside of the allowable range.\r\n
0x40000003 | {Image Relocated}\r\nAn image file could not be mapped at the address specified in the image file. Local fixups must be performed on this image.\r\n
0x40000004 | This informational level status indicates that a specified registry sub-tree transaction state did not yet exist and had to be created.\r\n
0x40000005 | {Segment Load}\r\nA virtual DOS machine (VDM) is loading, unloading, or moving an MS-DOS or Win16 program segment image.\r\nAn exception is raised so a debugger can load, unload or track symbols and breakpoints within these 16-bit segments.\r\n
0x40000006 | {Local Session Key}\r\nA user session key was requested for a local RPC connection. The session key returned is a constant value and not unique to this connection.\r\n
0x40000007 | {Invalid Current Directory}\r\nThe process cannot switch to the startup current directory %hs.\r\nSelect OK to set current directory to %hs, or select CANCEL to exit.\r\n
0x40000008 | {Serial IOCTL Complete}\r\nA serial I/O operation was completed by another write to a serial port.\r\n(The IOCTL_SERIAL_XOFF_COUNTER reached zero.)\r\n
0x40000009 | {Registry Recovery}\r\nOne of the files containing the system's Registry data had to be recovered by use of a log or alternate copy.\r\nThe recovery was successful.\r\n
0x4000000a | {Redundant Read}\r\nTo satisfy a read request, the NT fault-tolerant file system successfully read the requested data from a redundant copy.\r\nThis was done because the file system encountered a failure on a member of the fault-tolerant volume, but was unable to reassign the failing area of the device.\r\n
0x4000000b | {Redundant Write}\r\nTo satisfy a write request, the NT fault-tolerant file system successfully wrote a redundant copy of the information.\r\nThis was done because the file system encountered a failure on a member of the fault-tolerant volume, but was not able to reassign the failing area of the device.\r\n
0x4000000c | {Serial IOCTL Timeout}\r\nA serial I/O operation completed because the time-out period expired.\r\n(The IOCTL_SERIAL_XOFF_COUNTER had not reached zero.)\r\n
0x4000000d | {Password Too Complex}\r\nThe Windows password is too complex to be converted to a LAN Manager password.\r\nThe LAN Manager password returned is a NULL string.\r\n
0x4000000e | {Machine Type Mismatch}\r\nThe image file %hs is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.\r\n
0x4000000f | {Partial Data Received}\r\nThe network transport returned partial data to its client. The remaining data will be sent later.\r\n
0x40000010 | {Expedited Data Received}\r\nThe network transport returned data to its client that was marked as expedited by the remote system.\r\n
0x40000011 | {Partial Expedited Data Received}\r\nThe network transport returned partial data to its client and this data was marked as expedited by the remote system. The remaining data will be sent later.\r\n
0x40000012 | {TDI Event Done}\r\nThe TDI indication has completed successfully.\r\n
0x40000013 | {TDI Event Pending}\r\nThe TDI indication has entered the pending state.\r\n
0x40000014 | Checking file system on %wZ\r\n
0x40000015 | {Fatal Application Exit}\r\n%hs\r\n
0x40000016 | The specified registry key is referenced by a predefined handle.\r\n
0x40000017 | {Page Unlocked}\r\nThe page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.\r\n
0x40000018 | %hs\r\n
0x40000019 | {Page Locked}\r\nOne of the pages to lock was already locked.\r\n
0x4000001a | Application popup: %1 : %2\r\n
0x4000001b | STATUS_ALREADY_WIN32\r\n
0x4000001c | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001d | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001e | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001f | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000020 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000021 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000022 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000023 | {Machine Type Mismatch}\r\nThe image file %hs is valid, but is for a machine type other than the current machine.\r\n
0x40000024 | A yield execution was performed and no thread was available to run.\r\n
0x40000025 | The resumable flag to a timer API was ignored.\r\n
0x40000026 | The arbiter has deferred arbitration of these resources to its parent\r\n
0x40000027 | The device "%hs" has detected a CardBus card in its slot, but the firmware on this system is not configured to allow the CardBus controller to be run in CardBus mode.\r\nThe operating system will currently accept only 16-bit (R2) pc-cards on this controller.\r\n
0x40000028 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000029 | The CPUs in this multiprocessor system are not all the same revision level.  To use all processors the operating system restricts itself to the features of the least capable processor in the system.  Should problems occur with this system, contact\r\nthe CPU manufacturer to see if this mix of processors is supported.\r\n
0x4000002a | The system was put into hibernation.\r\n
0x4000002b | The system was resumed from hibernation.\r\n
0x4000002c | Windows has detected that the system firmware (BIOS) was updated [previous firmware date = %2, current firmware date %3].\r\n
0x4000002d | A device driver is leaking locked I/O pages causing system degradation.  The system has automatically enabled tracking code in order to try and catch the culprit.\r\n
0x4000002e | The ALPC message being canceled has already been retrieved from the queue on the other side.\r\n
0x4000002f | The system powerstate is transitioning from %2 to %3.\r\n
0x40000030 | The receive operation was successful. Check the ALPC completion list for the received message.\r\n
0x40000031 | The system powerstate is transitioning from %2 to %3 but could enter %4.\r\n
0x40000032 | Access to %1 is monitored by policy rule %2.\r\n
0x40000033 | A valid hibernation file has been invalidated and should be abandoned.\r\n
0x40000034 | Business rule scripts are disabled for the calling application.\r\n
0x40000294 | The system has awoken\r\n
0x40000370 | The Directory Service is shutting down.\r\n
0x40010001 | Debugger will reply later.\r\n
0x40010002 | Debugger cannot provide handle.\r\n
0x40010003 | Debugger terminated thread.\r\n
0x40010004 | Debugger terminated process.\r\n
0x40010005 | Debugger got control C.\r\n
0x40010006 | Debugger printed exception on control C.\r\n
0x40010007 | Debugger received RIP exception.\r\n
0x40010008 | Debugger received control break.\r\n
0x40010009 | Debugger command communication exception.\r\n
0x40020056 | A UUID that is valid only on this computer has been allocated.\r\n
0x400200af | Some data remains to be sent in the request buffer.\r\n
0x400a0004 | The Client Drive Mapping Service Has Connected on Terminal Connection.\r\n
0x400a0005 | The Client Drive Mapping Service Has Disconnected on Terminal Connection.\r\n
0x4015000d | A kernel mode component is releasing a reference on an activation context.\r\n
0x40190034 | The transactional resource manager is already consistent.  Recovery is not needed.\r\n
0x40190035 | The transactional resource manager has already been started.\r\n
0x401a000c | Log service encountered a log stream with no restart area.\r\n
0x401b00ec | {Display Driver Recovered From Failure}\r\nThe %hs display driver has detected and recovered from a failure. Some graphical operations may have failed. The next time you reboot the machine a dialog will be displayed giving you a chance to upload data about this failure to Microsoft.\r\n
0x401e000a | Specified buffer is not big enough to contain entire requested dataset. Partial data populated upto the size of the buffer.\r\nCaller needs to provide buffer of size as specified in the partially populated buffer's content (interface specific).\r\n
0x401e0307 | No mode is pinned on the specified VidPN source/target.\r\n
0x401e031e | Specified mode set does not specify preference for one of its modes.\r\n
0x401e034b | Specified data set (e.g. mode set, frequency range set, descriptor set, topology, etc.) is empty.\r\n
0x401e034c | Specified data set (e.g. mode set, frequency range set, descriptor set, topology, etc.) does not contain any more elements.\r\n
0x401e0351 | Specified content transformation is not pinned on the specified VidPN present path.\r\n
0x401e042f | Child device presence was not reliably detected.\r\n
0x401e0437 | Starting the leadlink adapter has been deferred temporarily.\r\n
0x401e0439 | The display adapter is being polled for children too frequently at the same polling level.\r\n
0x401e043a | Starting the adapter has been deferred temporarily.\r\n
0x40230001 | The request will be completed later by NDIS status indication.\r\n
0x80000001 | {EXCEPTION}\r\nGuard Page Exception\r\nA page of memory that marks the end of a data structure, such as a stack or an array, has been accessed.\r\n
0x80000002 | {EXCEPTION}\r\nAlignment Fault\r\nA datatype misalignment was detected in a load or store instruction.\r\n
0x80000003 | {EXCEPTION}\r\nBreakpoint\r\nA breakpoint has been reached.\r\n
0x80000004 | {EXCEPTION}\r\nSingle Step\r\nA single step or trace operation has just been completed.\r\n
0x80000005 | {Buffer Overflow}\r\nThe data was too large to fit into the specified buffer.\r\n
0x80000006 | {No More Files}\r\nNo more files were found which match the file specification.\r\n
0x80000007 | {Kernel Debugger Awakened}\r\nthe system debugger was awakened by an interrupt.\r\n
0x8000000a | {Handles Closed}\r\nHandles to objects have been automatically closed as a result of the requested operation.\r\n
0x8000000b | {Non-Inheritable ACL}\r\nAn access control list (ACL) contains no components that can be inherited.\r\n
0x8000000c | {GUID Substitution}\r\nDuring the translation of a global identifier (GUID) to a Windows security ID (SID), no administratively-defined GUID prefix was found.\r\nA substitute prefix was used, which will not compromise system security.\r\nHowever, this may provide a more restrictive access than intended.\r\n
0x8000000d | {Partial Copy}\r\nDue to protection conflicts not all the requested bytes could be copied.\r\n
0x8000000e | {Out of Paper}\r\nThe printer is out of paper.\r\n
0x8000000f | {Device Power Is Off}\r\nThe printer power has been turned off.\r\n
0x80000010 | {Device Offline}\r\nThe printer has been taken offline.\r\n
0x80000011 | {Device Busy}\r\nThe device is currently busy.\r\n
0x80000012 | {No More EAs}\r\nNo more extended attributes (EAs) were found for the file.\r\n
0x80000013 | {Illegal EA}\r\nThe specified extended attribute (EA) name contains at least one illegal character.\r\n
0x80000014 | {Inconsistent EA List}\r\nThe extended attribute (EA) list is inconsistent.\r\n
0x80000015 | {Invalid EA Flag}\r\nAn invalid extended attribute (EA) flag was set.\r\n
0x80000016 | {Verifying Disk}\r\nThe media has changed and a verify operation is in progress so no reads or writes may be performed to the device, except those used in the verify operation.\r\n
0x80000017 | {Too Much Information}\r\nThe specified access control list (ACL) contained more information than was expected.\r\n
0x80000018 | This warning level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.\r\nThe commit has NOT been completed, but has not been rolled back either (so it may still be committed if desired).\r\n
0x8000001a | {No More Entries}\r\nNo more entries are available from an enumeration operation.\r\n
0x8000001b | {Filemark Found}\r\nA filemark was detected.\r\n
0x8000001c | {Media Changed}\r\nThe media may have changed.\r\n
0x8000001d | {I/O Bus Reset}\r\nAn I/O bus reset was detected.\r\n
0x8000001e | {End of Media}\r\nThe end of the media was encountered.\r\n
0x8000001f | Beginning of tape or partition has been detected.\r\n
0x80000020 | {Media Changed}\r\nThe media may have changed.\r\n
0x80000021 | A tape access reached a setmark.\r\n
0x80000022 | During a tape access, the end of the data written is reached.\r\n
0x80000023 | The redirector is in use and cannot be unloaded.\r\n
0x80000024 | The server is in use and cannot be unloaded.\r\n
0x80000025 | The specified connection has already been disconnected.\r\n
0x80000026 | A long jump has been executed.\r\n
0x80000027 | A cleaner cartridge is present in the tape library.\r\n
0x80000028 | The Plug and Play query operation was not successful.\r\n
0x80000029 | A frame consolidation has been executed.\r\n
0x8000002a | {Registry Hive Recovered}\r\nRegistry hive (file):\r\n%hs\r\nwas corrupted and it has been recovered. Some data might have been lost.\r\n
0x8000002b | The application is attempting to run executable code from the module %hs.  This may be insecure.  An alternative, %hs, is available.  Should the application use the secure module %hs?\r\n
0x8000002c | The application is loading executable code from the module %hs.  This is secure, but may be incompatible with previous releases of the operating system.  An alternative, %hs, is available.  Should the application use the secure module %hs?\r\n
0x8000002d | The create operation stopped after reaching a symbolic link.\r\n
0x80000288 | The device has indicated that cleaning is necessary.\r\n
0x80000289 | The device has indicated that it's door is open. Further operations require it closed and secured.\r\n
0x80000803 | Windows discovered a corruption in the file %hs. This file has now been repaired.\r\nPlease check if any data in the file was lost because of the corruption.\r\n
0x80010001 | Debugger did not handle the exception.\r\n
0x80130001 | The cluster node is already up.\r\n
0x80130002 | The cluster node is already down.\r\n
0x80130003 | The cluster network is already online.\r\n
0x80130004 | The cluster network is already offline.\r\n
0x80130005 | The cluster node is already a member of the cluster.\r\n
0x80190009 | The log could not be set to the requested size.\r\n
0x80190029 | There is no transaction metadata on the file.\r\n
0x80190031 | The file can't be recovered because there is a handle still open on it.\r\n
0x80190041 | Transaction metadata is already present on this file and cannot be superseded.\r\n
0x80190042 | A transaction scope could not be entered because the scope handler has not been initialized.\r\n
0x801b00eb | {Display Driver Stopped Responding and recovered}\r\nThe %hs display driver has stopped working normally. The recovery had been performed.\r\n
0x801c0001 | {Buffer too small}\r\nThe buffer is too small to contain the entry. No information has been written to the buffer.\r\n
0x80210001 | Volume Metadata read or write is incomplete.\r\n
0xc0000001 | {Operation Failed}\r\nThe requested operation was unsuccessful.\r\n
0xc0000002 | {Not Implemented}\r\nThe requested operation is not implemented.\r\n
0xc0000003 | {Invalid Parameter}\r\nThe specified information class is not a valid information class for the specified object.\r\n
0xc0000004 | The specified information record length does not match the length required for the specified information class.\r\n
0xc0000005 | The instruction at 0x%08lx referenced memory at 0x%08lx. The memory could not be %s.\r\n
0xc0000006 | The instruction at 0x%08lx referenced memory at 0x%08lx. The required data was not placed into memory because of an I/O error status of 0x%08lx.\r\n
0xc0000007 | The pagefile quota for the process has been exhausted.\r\n
0xc0000008 | An invalid HANDLE was specified.\r\n
0xc0000009 | An invalid initial stack was specified in a call to NtCreateThread.\r\n
0xc000000a | An invalid initial start address was specified in a call to NtCreateThread.\r\n
0xc000000b | An invalid Client ID was specified.\r\n
0xc000000c | An attempt was made to cancel or set a timer that has an associated APC and the subject thread is not the thread that originally set the timer with an associated APC routine.\r\n
0xc000000d | An invalid parameter was passed to a service or function.\r\n
0xc000000e | A device which does not exist was specified.\r\n
0xc000000f | {File Not Found}\r\nThe file %hs does not exist.\r\n
0xc0000010 | The specified request is not a valid operation for the target device.\r\n
0xc0000011 | The end-of-file marker has been reached. There is no valid data in the file beyond this marker.\r\n
0xc0000012 | {Wrong Volume}\r\nThe wrong volume is in the drive.\r\nPlease insert volume %hs into drive %hs.\r\n
0xc0000013 | {No Disk}\r\nThere is no disk in the drive.\r\nPlease insert a disk into drive %hs.\r\n
0xc0000014 | {Unknown Disk Format}\r\nThe disk in drive %hs is not formatted properly.\r\nPlease check the disk, and reformat if necessary.\r\n
0xc0000015 | {Sector Not Found}\r\nThe specified sector does not exist.\r\n
0xc0000016 | {Still Busy}\r\nThe specified I/O request packet (IRP) cannot be disposed of because the I/O operation is not complete.\r\n
0xc0000017 | {Not Enough Quota}\r\nNot enough virtual memory or paging file quota is available to complete the specified operation.\r\n
0xc0000018 | {Conflicting Address Range}\r\nThe specified address range conflicts with the address space.\r\n
0xc0000019 | Address range to unmap is not a mapped view.\r\n
0xc000001a | Virtual memory cannot be freed.\r\n
0xc000001b | Specified section cannot be deleted.\r\n
0xc000001c | An invalid system service was specified in a system service call.\r\n
0xc000001d | {EXCEPTION}\r\nIllegal Instruction\r\nAn attempt was made to execute an illegal instruction.\r\n
0xc000001e | {Invalid Lock Sequence}\r\nAn attempt was made to execute an invalid lock sequence.\r\n
0xc000001f | {Invalid Mapping}\r\nAn attempt was made to create a view for a section which is bigger than the section.\r\n
0xc0000020 | {Bad File}\r\nThe attributes of the specified mapping file for a section of memory cannot be read.\r\n
0xc0000021 | {Already Committed}\r\nThe specified address range is already committed.\r\n
0xc0000022 | {Access Denied}\r\nA process has requested access to an object, but has not been granted those access rights.\r\n
0xc0000023 | {Buffer Too Small}\r\nThe buffer is too small to contain the entry. No information has been written to the buffer.\r\n
0xc0000024 | {Wrong Type}\r\nThere is a mismatch between the type of object required by the requested operation and the type of object that is specified in the request.\r\n
0xc0000025 | {EXCEPTION}\r\nCannot Continue\r\nWindows cannot continue from this exception.\r\n
0xc0000026 | An invalid exception disposition was returned by an exception handler.\r\n
0xc0000027 | Unwind exception code.\r\n
0xc0000028 | An invalid or unaligned stack was encountered during an unwind operation.\r\n
0xc0000029 | An invalid unwind target was encountered during an unwind operation.\r\n
0xc000002a | An attempt was made to unlock a page of memory which was not locked.\r\n
0xc000002b | Device parity error on I/O operation.\r\n
0xc000002c | An attempt was made to decommit uncommitted virtual memory.\r\n
0xc000002d | An attempt was made to change the attributes on memory that has not been committed.\r\n
0xc000002e | Invalid Object Attributes specified to NtCreatePort or invalid Port Attributes specified to NtConnectPort\r\n
0xc000002f | Length of message passed to NtRequestPort or NtRequestWaitReplyPort was longer than the maximum message allowed by the port.\r\n
0xc0000030 | An invalid combination of parameters was specified.\r\n
0xc0000031 | An attempt was made to lower a quota limit below the current usage.\r\n
0xc0000032 | {Corrupt Disk}\r\nThe file system structure on the disk is corrupt and unusable.\r\nPlease run the Chkdsk utility on the volume %hs.\r\n
0xc0000033 | Object Name invalid.\r\n
0xc0000034 | Object Name not found.\r\n
0xc0000035 | Object Name already exists.\r\n
0xc0000037 | Attempt to send a message to a disconnected communication port.\r\n
0xc0000038 | An attempt was made to attach to a device that was already attached to another device.\r\n
0xc0000039 | Object Path Component was not a directory object.\r\n
0xc000003a | {Path Not Found}\r\nThe path %hs does not exist.\r\n
0xc000003b | Object Path Component was not a directory object.\r\n
0xc000003c | {Data Overrun}\r\nA data overrun error occurred.\r\n
0xc000003d | {Data Late}\r\nA data late error occurred.\r\n
0xc000003e | {Data Error}\r\nAn error in reading or writing data occurred.\r\n
0xc000003f | {Bad CRC}\r\nA cyclic redundancy check (CRC) checksum error occurred.\r\n
0xc0000040 | {Section Too Large}\r\nThe specified section is too big to map the file.\r\n
0xc0000041 | The NtConnectPort request is refused.\r\n
0xc0000042 | The type of port handle is invalid for the operation requested.\r\n
0xc0000043 | A file cannot be opened because the share access flags are incompatible.\r\n
0xc0000044 | Insufficient quota exists to complete the operation\r\n
0xc0000045 | The specified page protection was not valid.\r\n
0xc0000046 | An attempt to release a mutant object was made by a thread that was not the owner of the mutant object.\r\n
0xc0000047 | An attempt was made to release a semaphore such that its maximum count would have been exceeded.\r\n
0xc0000048 | An attempt to set a processes DebugPort or ExceptionPort was made, but a port already exists in the process or\r\nan attempt to set a file's CompletionPort made, but a port was already set in the file or\r\nan attempt to set an alpc port's associated completion port was made, but it is already set.\r\n
0xc0000049 | An attempt was made to query image information on a section which does not map an image.\r\n
0xc000004a | An attempt was made to suspend a thread whose suspend count was at its maximum.\r\n
0xc000004b | An attempt was made to access a thread that has begun termination.\r\n
0xc000004c | An attempt was made to set the working set limit to an invalid value (minimum greater than maximum, etc).\r\n
0xc000004d | A section was created to map a file which is not compatible to an already existing section which maps the same file.\r\n
0xc000004e | A view to a section specifies a protection which is incompatible with the initial view's protection.\r\n
0xc000004f | An operation involving EAs failed because the file system does not support EAs.\r\n
0xc0000050 | An EA operation failed because EA set is too large.\r\n
0xc0000051 | An EA operation failed because the name or EA index is invalid.\r\n
0xc0000052 | The file for which EAs were requested has no EAs.\r\n
0xc0000053 | The EA is corrupt and non-readable.\r\n
0xc0000054 | A requested read/write cannot be granted due to a conflicting file lock.\r\n
0xc0000055 | A requested file lock cannot be granted due to other existing locks.\r\n
0xc0000056 | A non close operation has been requested of a file object with a delete pending.\r\n
0xc0000057 | An attempt was made to set the control attribute on a file. This attribute is not supported in the target file system.\r\n
0xc0000058 | Indicates a revision number encountered or specified is not one known by the service. It may be a more recent revision than the service is aware of.\r\n
0xc0000059 | Indicates two revision levels are incompatible.\r\n
0xc000005a | Indicates a particular Security ID may not be assigned as the owner of an object.\r\n
0xc000005b | Indicates a particular Security ID may not be assigned as the primary group of an object.\r\n
0xc000005c | An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.\r\n
0xc000005d | A mandatory group may not be disabled.\r\n
0xc000005e | There are currently no logon servers available to service the logon request.\r\n
0xc000005f | A specified logon session does not exist. It may already have been terminated.\r\n
0xc0000060 | A specified privilege does not exist.\r\n
0xc0000061 | A required privilege is not held by the client.\r\n
0xc0000062 | The name provided is not a properly formed account name.\r\n
0xc0000063 | The specified account already exists.\r\n
0xc0000064 | The specified account does not exist.\r\n
0xc0000065 | The specified group already exists.\r\n
0xc0000066 | The specified group does not exist.\r\n
0xc0000067 | The specified user account is already in the specified group account.\r\nAlso used to indicate a group cannot be deleted because it contains a member.\r\n
0xc0000068 | The specified user account is not a member of the specified group account.\r\n
0xc0000069 | Indicates the requested operation would disable or delete the last remaining administration account.\r\nThis is not allowed to prevent creating a situation in which the system cannot be administrated.\r\n
0xc000006a | When trying to update a password, this return status indicates that the value provided as the current password is not correct.\r\n
0xc000006b | When trying to update a password, this return status indicates that the value provided for the new password contains values that are not allowed in passwords.\r\n
0xc000006c | When trying to update a password, this status indicates that some password update rule has been violated. For example, the password may not meet length criteria.\r\n
0xc000006d | The attempted logon is invalid. This is either due to a bad username or authentication information.\r\n
0xc000006e | Indicates a referenced user name and authentication information are valid, but some user account restriction has prevented successful authentication (such as time-of-day restrictions).\r\n
0xc000006f | The user account has time restrictions and may not be logged onto at this time.\r\n
0xc0000070 | The user account is restricted such that it may not be used to log on from the source workstation.\r\n
0xc0000071 | The user account's password has expired.\r\n
0xc0000072 | The referenced account is currently disabled and may not be logged on to.\r\n
0xc0000073 | None of the information to be translated has been translated.\r\n
0xc0000074 | The number of LUIDs requested may not be allocated with a single allocation.\r\n
0xc0000075 | Indicates there are no more LUIDs to allocate.\r\n
0xc0000076 | Indicates the sub-authority value is invalid for the particular use.\r\n
0xc0000077 | Indicates the ACL structure is not valid.\r\n
0xc0000078 | Indicates the SID structure is not valid.\r\n
0xc0000079 | Indicates the SECURITY_DESCRIPTOR structure is not valid.\r\n
0xc000007a | Indicates the specified procedure address cannot be found in the DLL.\r\n
0xc000007b | {Bad Image}\r\n%hs is either not designed to run on Windows or it contains an error. Try installing the program again using the original installation media or contact your system administrator or the software vendor for support.\r\n
0xc000007c | An attempt was made to reference a token that doesn't exist.\r\nThis is typically done by referencing the token associated with a thread when the thread is not impersonating a client.\r\n
0xc000007d | Indicates that an attempt to build either an inherited ACL or ACE was not successful.\r\nThis can be caused by a number of things. One of the more probable causes is the replacement of a CreatorId with an SID that didn't fit into the ACE or ACL.\r\n
0xc000007e | The range specified in NtUnlockFile was not locked.\r\n
0xc000007f | An operation failed because the disk was full.\r\n
0xc0000080 | The GUID allocation server is [already] disabled at the moment.\r\n
0xc0000081 | The GUID allocation server is [already] enabled at the moment.\r\n
0xc0000082 | Too many GUIDs were requested from the allocation server at once.\r\n
0xc0000083 | The GUIDs could not be allocated because the Authority Agent was exhausted.\r\n
0xc0000084 | The value provided was an invalid value for an identifier authority.\r\n
0xc0000085 | There are no more authority agent values available for the given identifier authority value.\r\n
0xc0000086 | An invalid volume label has been specified.\r\n
0xc0000087 | A mapped section could not be extended.\r\n
0xc0000088 | Specified section to flush does not map a data file.\r\n
0xc0000089 | Indicates the specified image file did not contain a resource section.\r\n
0xc000008a | Indicates the specified resource type cannot be found in the image file.\r\n
0xc000008b | Indicates the specified resource name cannot be found in the image file.\r\n
0xc000008c | {EXCEPTION}\r\nArray bounds exceeded.\r\n
0xc000008d | {EXCEPTION}\r\nFloating-point denormal operand.\r\n
0xc000008e | {EXCEPTION}\r\nFloating-point division by zero.\r\n
0xc000008f | {EXCEPTION}\r\nFloating-point inexact result.\r\n
0xc0000090 | {EXCEPTION}\r\nFloating-point invalid operation.\r\n
0xc0000091 | {EXCEPTION}\r\nFloating-point overflow.\r\n
0xc0000092 | {EXCEPTION}\r\nFloating-point stack check.\r\n
0xc0000093 | {EXCEPTION}\r\nFloating-point underflow.\r\n
0xc0000094 | {EXCEPTION}\r\nInteger division by zero.\r\n
0xc0000095 | {EXCEPTION}\r\nInteger overflow.\r\n
0xc0000096 | {EXCEPTION}\r\nPrivileged instruction.\r\n
0xc0000097 | An attempt was made to install more paging files than the system supports.\r\n
0xc0000098 | The volume for a file has been externally altered such that the opened file is no longer valid.\r\n
0xc0000099 | When a block of memory is allotted for future updates, such as the memory allocated to hold discretionary access control and primary group information, successive updates may exceed the amount of memory originally allotted.\r\nSince quota may already have been charged to several processes which have handles to the object, it is not reasonable to alter the size of the allocated memory.\r\nInstead, a request that requires more memory than has been allotted must fail and the STATUS_ALLOTED_SPACE_EXCEEDED error returned.\r\n
0xc000009a | Insufficient system resources exist to complete the API.\r\n
0xc000009b | An attempt has been made to open a DFS exit path control file.\r\n
0xc000009c | STATUS_DEVICE_DATA_ERROR\r\n
0xc000009d | STATUS_DEVICE_NOT_CONNECTED\r\n
0xc000009e | STATUS_DEVICE_POWER_FAILURE\r\n
0xc000009f | Virtual memory cannot be freed as base address is not the base of the region and a region size of zero was specified.\r\n
0xc00000a0 | An attempt was made to free virtual memory which is not allocated.\r\n
0xc00000a1 | The working set is not big enough to allow the requested pages to be locked.\r\n
0xc00000a2 | {Write Protect Error}\r\nThe disk cannot be written to because it is write protected.\r\nPlease remove the write protection from the volume %hs in drive %hs.\r\n
0xc00000a3 | {Drive Not Ready}\r\nThe drive is not ready for use; its door may be open.\r\nPlease check drive %hs and make sure that a disk is inserted and that the drive door is closed.\r\n
0xc00000a4 | The specified attributes are invalid, or incompatible with the attributes for the group as a whole.\r\n
0xc00000a5 | A specified impersonation level is invalid.\r\nAlso used to indicate a required impersonation level was not provided.\r\n
0xc00000a6 | An attempt was made to open an Anonymous level token.\r\nAnonymous tokens may not be opened.\r\n
0xc00000a7 | The validation information class requested was invalid.\r\n
0xc00000a8 | The type of a token object is inappropriate for its attempted use.\r\n
0xc00000a9 | The type of a token object is inappropriate for its attempted use.\r\n
0xc00000aa | An attempt was made to execute an instruction at an unaligned address and the host system does not support unaligned instruction references.\r\n
0xc00000ab | The maximum named pipe instance count has been reached.\r\n
0xc00000ac | An instance of a named pipe cannot be found in the listening state.\r\n
0xc00000ad | The named pipe is not in the connected or closing state.\r\n
0xc00000ae | The specified pipe is set to complete operations and there are current I/O operations queued so it cannot be changed to queue operations.\r\n
0xc00000af | The specified handle is not open to the server end of the named pipe.\r\n
0xc00000b0 | The specified named pipe is in the disconnected state.\r\n
0xc00000b1 | The specified named pipe is in the closing state.\r\n
0xc00000b2 | The specified named pipe is in the connected state.\r\n
0xc00000b3 | The specified named pipe is in the listening state.\r\n
0xc00000b4 | The specified named pipe is not in message mode.\r\n
0xc00000b5 | {Device Timeout}\r\nThe specified I/O operation on %hs was not completed before the time-out period expired.\r\n
0xc00000b6 | The specified file has been closed by another process.\r\n
0xc00000b7 | Profiling not started.\r\n
0xc00000b8 | Profiling not stopped.\r\n
0xc00000b9 | The passed ACL did not contain the minimum required information.\r\n
0xc00000ba | The file that was specified as a target is a directory and the caller specified that it could be anything but a directory.\r\n
0xc00000bb | The request is not supported.\r\n
0xc00000bc | This remote computer is not listening.\r\n
0xc00000bd | A duplicate name exists on the network.\r\n
0xc00000be | The network path cannot be located.\r\n
0xc00000bf | The network is busy.\r\n
0xc00000c0 | This device does not exist.\r\n
0xc00000c1 | The network BIOS command limit has been reached.\r\n
0xc00000c2 | An I/O adapter hardware error has occurred.\r\n
0xc00000c3 | The network responded incorrectly.\r\n
0xc00000c4 | An unexpected network error occurred.\r\n
0xc00000c5 | The remote adapter is not compatible.\r\n
0xc00000c6 | The printer queue is full.\r\n
0xc00000c7 | Space to store the file waiting to be printed is not available on the server.\r\n
0xc00000c8 | The requested print file has been canceled.\r\n
0xc00000c9 | The network name was deleted.\r\n
0xc00000ca | Network access is denied.\r\n
0xc00000cb | {Incorrect Network Resource Type}\r\nThe specified device type (LPT, for example) conflicts with the actual device type on the remote resource.\r\n
0xc00000cc | {Network Name Not Found}\r\nThe specified share name cannot be found on the remote server.\r\n
0xc00000cd | The name limit for the local computer network adapter card was exceeded.\r\n
0xc00000ce | The network BIOS session limit was exceeded.\r\n
0xc00000cf | File sharing has been temporarily paused.\r\n
0xc00000d0 | No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept.\r\n
0xc00000d1 | Print or disk redirection is temporarily paused.\r\n
0xc00000d2 | A network data fault occurred.\r\n
0xc00000d3 | The number of active profiling objects is at the maximum and no more may be started.\r\n
0xc00000d4 | {Incorrect Volume}\r\nThe target file of a rename request is located on a different device than the source of the rename request.\r\n
0xc00000d5 | The file specified has been renamed and thus cannot be modified.\r\n
0xc00000d6 | {Network Request Timeout}\r\nThe session with a remote server has been disconnected because the time-out interval for a request has expired.\r\n
0xc00000d7 | Indicates an attempt was made to operate on the security of an object that does not have security associated with it.\r\n
0xc00000d8 | Used to indicate that an operation cannot continue without blocking for I/O.\r\n
0xc00000d9 | Used to indicate that a read operation was done on an empty pipe.\r\n
0xc00000da | Configuration information could not be read from the domain controller, either because the machine is unavailable, or access has been denied.\r\n
0xc00000db | Indicates that a thread attempted to terminate itself by default (called NtTerminateThread with NULL) and it was the last thread in the current process.\r\n
0xc00000dc | Indicates the Sam Server was in the wrong state to perform the desired operation.\r\n
0xc00000dd | Indicates the Domain was in the wrong state to perform the desired operation.\r\n
0xc00000de | This operation is only allowed for the Primary Domain Controller of the domain.\r\n
0xc00000df | The specified Domain did not exist.\r\n
0xc00000e0 | The specified Domain already exists.\r\n
0xc00000e1 | An attempt was made to exceed the limit on the number of domains per server for this release.\r\n
0xc00000e2 | Error status returned when oplock request is denied.\r\n
0xc00000e3 | Error status returned when an invalid oplock acknowledgment is received by a file system.\r\n
0xc00000e4 | This error indicates that the requested operation cannot be completed due to a catastrophic media failure or on-disk data structure corruption.\r\n
0xc00000e5 | An internal error occurred.\r\n
0xc00000e6 | Indicates generic access types were contained in an access mask which should already be mapped to non-generic access types.\r\n
0xc00000e7 | Indicates a security descriptor is not in the necessary format (absolute or self-relative).\r\n
0xc00000e8 | An access to a user buffer failed at an "expected" point in time.\r\nThis code is defined since the caller does not want to accept STATUS_ACCESS_VIOLATION in its filter.\r\n
0xc00000e9 | If an I/O error is returned which is not defined in the standard FsRtl filter, it is converted to the following error which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ea | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000eb | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ec | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter.\r\nIn this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ed | The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.\r\n
0xc00000ee | An attempt has been made to start a new session manager or LSA logon session with an ID that is already in use.\r\n
0xc00000ef | An invalid parameter was passed to a service or function as the first argument.\r\n
0xc00000f0 | An invalid parameter was passed to a service or function as the second argument.\r\n
0xc00000f1 | An invalid parameter was passed to a service or function as the third argument.\r\n
0xc00000f2 | An invalid parameter was passed to a service or function as the fourth argument.\r\n
0xc00000f3 | An invalid parameter was passed to a service or function as the fifth argument.\r\n
0xc00000f4 | An invalid parameter was passed to a service or function as the sixth argument.\r\n
0xc00000f5 | An invalid parameter was passed to a service or function as the seventh argument.\r\n
0xc00000f6 | An invalid parameter was passed to a service or function as the eighth argument.\r\n
0xc00000f7 | An invalid parameter was passed to a service or function as the ninth argument.\r\n
0xc00000f8 | An invalid parameter was passed to a service or function as the tenth argument.\r\n
0xc00000f9 | An invalid parameter was passed to a service or function as the eleventh argument.\r\n
0xc00000fa | An invalid parameter was passed to a service or function as the twelfth argument.\r\n
0xc00000fb | An attempt was made to access a network file, but the network software was not yet started.\r\n
0xc00000fc | An attempt was made to start the redirector, but the redirector has already been started.\r\n
0xc00000fd | A new guard page for the stack cannot be created.\r\n
0xc00000fe | A specified authentication package is unknown.\r\n
0xc00000ff | A malformed function table was encountered during an unwind operation.\r\n
0xc0000100 | Indicates the specified environment variable name was not found in the specified environment block.\r\n
0xc0000101 | Indicates that the directory trying to be deleted is not empty.\r\n
0xc0000102 | {Corrupt File}\r\nThe file or directory %hs is corrupt and unreadable.\r\nPlease run the Chkdsk utility.\r\n
0xc0000103 | A requested opened file is not a directory.\r\n
0xc0000104 | The logon session is not in a state that is consistent with the requested operation.\r\n
0xc0000105 | An internal LSA error has occurred. An authentication package has requested the creation of a Logon Session but the ID of an already existing Logon Session has been specified.\r\n
0xc0000106 | A specified name string is too long for its intended use.\r\n
0xc0000107 | The user attempted to force close the files on a redirected drive, but there were opened files on the drive, and the user did not specify a sufficient level of force.\r\n
0xc0000108 | The user attempted to force close the files on a redirected drive, but there were opened directories on the drive, and the user did not specify a sufficient level of force.\r\n
0xc0000109 | RtlFindMessage could not locate the requested message ID in the message table resource.\r\n
0xc000010a | An attempt was made to access an exiting process.\r\n
0xc000010b | Indicates an invalid value has been provided for the LogonType requested.\r\n
0xc000010c | Indicates that an attempt was made to assign protection to a file system file or directory and one of the SIDs in the security descriptor could not be translated into a GUID that could be stored by the file system.\r\nThis causes the protection attempt to fail, which may cause a file creation attempt to fail.\r\n
0xc000010d | Indicates that an attempt has been made to impersonate via a named pipe that has not yet been read from.\r\n
0xc000010e | Indicates that the specified image is already loaded.\r\n
0xc000010f | STATUS_ABIOS_NOT_PRESENT\r\n
0xc0000110 | STATUS_ABIOS_LID_NOT_EXIST\r\n
0xc0000111 | STATUS_ABIOS_LID_ALREADY_OWNED\r\n
0xc0000112 | STATUS_ABIOS_NOT_LID_OWNER\r\n
0xc0000113 | STATUS_ABIOS_INVALID_COMMAND\r\n
0xc0000114 | STATUS_ABIOS_INVALID_LID\r\n
0xc0000115 | STATUS_ABIOS_SELECTOR_NOT_AVAILABLE\r\n
0xc0000116 | STATUS_ABIOS_INVALID_SELECTOR\r\n
0xc0000117 | Indicates that an attempt was made to change the size of the LDT for a process that has no LDT.\r\n
0xc0000118 | Indicates that an attempt was made to grow an LDT by setting its size, or that the size was not an even number of selectors.\r\n
0xc0000119 | Indicates that the starting value for the LDT information was not an integral multiple of the selector size.\r\n
0xc000011a | Indicates that the user supplied an invalid descriptor when trying to set up Ldt descriptors.\r\n
0xc000011b | The specified image file did not have the correct format. It appears to be NE format.\r\n
0xc000011c | Indicates that the transaction state of a registry sub-tree is incompatible with the requested operation.\r\nFor example, a request has been made to start a new transaction with one already in progress,\r\nor a request has been made to apply a transaction when one is not currently in progress.\r\n
0xc000011d | Indicates an error has occurred during a registry transaction commit.\r\nThe database has been left in an unknown, but probably inconsistent, state.\r\nThe state of the registry transaction is left as COMMITTING.\r\n
0xc000011e | An attempt was made to map a file of size zero with the maximum size specified as zero.\r\n
0xc000011f | Too many files are opened on a remote server.\r\nThis error should only be returned by the Windows redirector on a remote drive.\r\n
0xc0000120 | The I/O request was canceled.\r\n
0xc0000121 | An attempt has been made to remove a file or directory that cannot be deleted.\r\n
0xc0000122 | Indicates a name specified as a remote computer name is syntactically invalid.\r\n
0xc0000123 | An I/O request other than close was performed on a file after it has been deleted,\r\nwhich can only happen to a request which did not complete before the last handle was closed via NtClose.\r\n
0xc0000124 | Indicates an operation has been attempted on a built-in (special) SAM account which is incompatible with built-in accounts.\r\nFor example, built-in accounts cannot be deleted.\r\n
0xc0000125 | The operation requested may not be performed on the specified group because it is a built-in special group.\r\n
0xc0000126 | The operation requested may not be performed on the specified user because it is a built-in special user.\r\n
0xc0000127 | Indicates a member cannot be removed from a group because the group is currently the member's primary group.\r\n
0xc0000128 | An I/O request other than close and several other special case operations was attempted using a file object that had already been closed.\r\n
0xc0000129 | Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token may only be performed when a process has zero or one threads.\r\n
0xc000012a | An attempt was made to operate on a thread within a specific process, but the thread specified is not in the process specified.\r\n
0xc000012b | An attempt was made to establish a token for use as a primary token but the token is already in use. A token can only be the primary token of one process at a time.\r\n
0xc000012c | Page file quota was exceeded.\r\n
0xc000012d | {Out of Virtual Memory}\r\nYour system is low on virtual memory. To ensure that Windows runs properly, increase the size of your virtual memory paging file. For more information, see Help.\r\n
0xc000012e | The specified image file did not have the correct format, it appears to be LE format.\r\n
0xc000012f | The specified image file did not have the correct format, it did not have an initial MZ.\r\n
0xc0000130 | The specified image file did not have the correct format, it did not have a proper e_lfarlc in the MZ header.\r\n
0xc0000131 | The specified image file did not have the correct format, it appears to be a 16-bit Windows image.\r\n
0xc0000132 | The Netlogon service cannot start because another Netlogon service running in the domain conflicts with the specified role.\r\n
0xc0000133 | The time at the Primary Domain Controller is different than the time at the Backup Domain Controller or member server by too large an amount.\r\n
0xc0000134 | The SAM database on a Windows Server is significantly out of synchronization with the copy on the Domain Controller. A complete synchronization is required.\r\n
0xc0000135 | {Unable To Locate Component}\r\nThis application has failed to start because %hs was not found. Re-installing the application may fix this problem.\r\n
0xc0000136 | The NtCreateFile API failed. This error should never be returned to an application, it is a place holder for the Windows Lan Manager Redirector to use in its internal error mapping routines.\r\n
0xc0000137 | {Privilege Failed}\r\nThe I/O permissions for the process could not be changed.\r\n
0xc0000138 | {Ordinal Not Found}\r\nThe ordinal %ld could not be located in the dynamic link library %hs.\r\n
0xc0000139 | {Entry Point Not Found}\r\nThe procedure entry point %hs could not be located in the dynamic link library %hs.\r\n
0xc000013a | {Application Exit by CTRL+C}\r\nThe application terminated as a result of a CTRL+C.\r\n
0xc000013b | {Virtual Circuit Closed}\r\nThe network transport on your computer has closed a network connection. There may or may not be I/O requests outstanding.\r\n
0xc000013c | {Virtual Circuit Closed}\r\nThe network transport on a remote computer has closed a network connection. There may or may not be I/O requests outstanding.\r\n
0xc000013d | {Insufficient Resources on Remote Computer}\r\nThe remote computer has insufficient resources to complete the network request. For instance, there may not be enough memory available on the remote computer to carry out the request at this time.\r\n
0xc000013e | {Virtual Circuit Closed}\r\nAn existing connection (virtual circuit) has been broken at the remote computer. There is probably something wrong with the network software protocol or the network hardware on the remote computer.\r\n
0xc000013f | {Virtual Circuit Closed}\r\nThe network transport on your computer has closed a network connection because it had to wait too long for a response from the remote computer.\r\n
0xc0000140 | The connection handle given to the transport was invalid.\r\n
0xc0000141 | The address handle given to the transport was invalid.\r\n
0xc0000142 | {DLL Initialization Failed}\r\nInitialization of the dynamic link library %hs failed. The process is terminating abnormally.\r\n
0xc0000143 | {Missing System File}\r\nThe required system file %hs is bad or missing.\r\n
0xc0000144 | {Application Error}\r\nThe exception %s (0x%08lx) occurred in the application at location 0x%08lx.\r\n
0xc0000145 | {Application Error}\r\nThe application failed to initialize properly (0x%lx). Click OK to terminate the application.\r\n
0xc0000146 | {Unable to Create Paging File}\r\nThe creation of the paging file %hs failed (%lx). The requested size was %ld.\r\n
0xc0000147 | {No Paging File Specified}\r\nNo paging file was specified in the system configuration.\r\n
0xc0000148 | {Incorrect System Call Level}\r\nAn invalid level was passed into the specified system call.\r\n
0xc0000149 | {Incorrect Password to LAN Manager Server}\r\nYou specified an incorrect password to a LAN Manager 2.x or MS-NET server.\r\n
0xc000014a | {EXCEPTION}\r\nA real-mode application issued a floating-point instruction and floating-point hardware is not present.\r\n
0xc000014b | The pipe operation has failed because the other end of the pipe has been closed.\r\n
0xc000014c | {The Registry Is Corrupt}\r\nThe structure of one of the files that contains Registry data is corrupt, or the image of the file in memory is corrupt, or the file could not be recovered because the alternate copy or log was absent or corrupt.\r\n
0xc000014d | An I/O operation initiated by the Registry failed unrecoverably.\r\nThe Registry could not read in, or write out, or flush, one of the files that contain the system's image of the Registry.\r\n
0xc000014e | An event pair synchronization operation was performed using the thread specific client/server event pair object, but no event pair object was associated with the thread.\r\n
0xc000014f | The volume does not contain a recognized file system.\r\nPlease make sure that all required file system drivers are loaded and that the volume is not corrupt.\r\n
0xc0000150 | No serial device was successfully initialized. The serial driver will unload.\r\n
0xc0000151 | The specified local group does not exist.\r\n
0xc0000152 | The specified account name is not a member of the group.\r\n
0xc0000153 | The specified account name is already a member of the group.\r\n
0xc0000154 | The specified local group already exists.\r\n
0xc0000155 | A requested type of logon (e.g., Interactive, Network, Service) is not granted by the target system's local security policy.\r\nPlease ask the system administrator to grant the necessary form of logon.\r\n
0xc0000156 | The maximum number of secrets that may be stored in a single system has been exceeded. The length and number of secrets is limited to satisfy United States State Department export restrictions.\r\n
0xc0000157 | The length of a secret exceeds the maximum length allowed. The length and number of secrets is limited to satisfy United States State Department export restrictions.\r\n
0xc0000158 | The Local Security Authority (LSA) database contains an internal inconsistency.\r\n
0xc0000159 | The requested operation cannot be performed in fullscreen mode.\r\n
0xc000015a | During a logon attempt, the user's security context accumulated too many security IDs. This is a very unusual situation.\r\nRemove the user from some global or local groups to reduce the number of security ids to incorporate into the security context.\r\n
0xc000015b | A user has requested a type of logon (e.g., interactive or network) that has not been granted. An administrator has control over who may logon interactively and through the network.\r\n
0xc000015c | The system has attempted to load or restore a file into the registry, and the specified file is not in the format of a registry file.\r\n
0xc000015d | An attempt was made to change a user password in the security account manager without providing the necessary Windows cross-encrypted password.\r\n
0xc000015e | A Windows Server has an incorrect configuration.\r\n
0xc000015f | An attempt was made to explicitly access the secondary copy of information via a device control to the Fault Tolerance driver and the secondary copy is not present in the system.\r\n
0xc0000160 | A configuration registry node representing a driver service entry was ill-formed and did not contain required value entries.\r\n
0xc0000161 | An illegal character was encountered. For a multi-byte character set this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE.\r\n
0xc0000162 | No mapping for the Unicode character exists in the target multi-byte code page.\r\n
0xc0000163 | The Unicode character is not defined in the Unicode character set installed on the system.\r\n
0xc0000164 | The paging file cannot be created on a floppy diskette.\r\n
0xc0000165 | {Floppy Disk Error}\r\nWhile accessing a floppy disk, an ID address mark was not found.\r\n
0xc0000166 | {Floppy Disk Error}\r\nWhile accessing a floppy disk, the track address from the sector ID field was found to be different than the track address maintained by the controller.\r\n
0xc0000167 | {Floppy Disk Error}\r\nThe floppy disk controller reported an error that is not recognized by the floppy disk driver.\r\n
0xc0000168 | {Floppy Disk Error}\r\nWhile accessing a floppy-disk, the controller returned inconsistent results via its registers.\r\n
0xc0000169 | {Hard Disk Error}\r\nWhile accessing the hard disk, a recalibrate operation failed, even after retries.\r\n
0xc000016a | {Hard Disk Error}\r\nWhile accessing the hard disk, a disk operation failed even after retries.\r\n
0xc000016b | {Hard Disk Error}\r\nWhile accessing the hard disk, a disk controller reset was needed, but even that failed.\r\n
0xc000016c | An attempt was made to open a device that was sharing an IRQ with other devices.\r\nAt least one other device that uses that IRQ was already opened.\r\nTwo concurrent opens of devices that share an IRQ and only work via interrupts is not supported for the particular bus type that the devices use.\r\n
0xc000016d | {FT Orphaning}\r\nA disk that is part of a fault-tolerant volume can no longer be accessed.\r\n
0xc000016e | The system bios failed to connect a system interrupt to the device or bus for\r\nwhich the device is connected.\r\n
0xc0000172 | Tape could not be partitioned.\r\n
0xc0000173 | When accessing a new tape of a multivolume partition, the current blocksize is incorrect.\r\n
0xc0000174 | Tape partition information could not be found when loading a tape.\r\n
0xc0000175 | Attempt to lock the eject media mechanism fails.\r\n
0xc0000176 | Unload media fails.\r\n
0xc0000177 | Physical end of tape was detected.\r\n
0xc0000178 | {No Media}\r\nThere is no media in the drive.\r\nPlease insert media into drive %hs.\r\n
0xc000017a | A member could not be added to or removed from the local group because the member does not exist.\r\n
0xc000017b | A new member could not be added to a local group because the member has the wrong account type.\r\n
0xc000017c | Illegal operation attempted on a registry key which has been marked for deletion.\r\n
0xc000017d | System could not allocate required space in a registry log.\r\n
0xc000017e | Too many Sids have been specified.\r\n
0xc000017f | An attempt was made to change a user password in the security account manager without providing the necessary LM cross-encrypted password.\r\n
0xc0000180 | An attempt was made to create a symbolic link in a registry key that already has subkeys or values.\r\n
0xc0000181 | An attempt was made to create a Stable subkey under a Volatile parent key.\r\n
0xc0000182 | The I/O device is configured incorrectly or the configuration parameters to the driver are incorrect.\r\n
0xc0000183 | An error was detected between two drivers or within an I/O driver.\r\n
0xc0000184 | The device is not in a valid state to perform this request.\r\n
0xc0000185 | The I/O device reported an I/O error.\r\n
0xc0000186 | A protocol error was detected between the driver and the device.\r\n
0xc0000187 | This operation is only allowed for the Primary Domain Controller of the domain.\r\n
0xc0000188 | Log file space is insufficient to support this operation.\r\n
0xc0000189 | A write operation was attempted to a volume after it was dismounted.\r\n
0xc000018a | The workstation does not have a trust secret for the primary domain in the local LSA database.\r\n
0xc000018b | The SAM database on the Windows Server does not have a computer account for this workstation trust relationship.\r\n
0xc000018c | The logon request failed because the trust relationship between the primary domain and the trusted domain failed.\r\n
0xc000018d | The logon request failed because the trust relationship between this workstation and the primary domain failed.\r\n
0xc000018e | The Eventlog log file is corrupt.\r\n
0xc000018f | No Eventlog log file could be opened. The Eventlog service did not start.\r\n
0xc0000190 | The network logon failed. This may be because the validation authority can't be reached.\r\n
0xc0000191 | An attempt was made to acquire a mutant such that its maximum count would have been exceeded.\r\n
0xc0000192 | An attempt was made to logon, but the netlogon service was not started.\r\n
0xc0000193 | The user's account has expired.\r\n
0xc0000194 | {EXCEPTION}\r\nPossible deadlock condition.\r\n
0xc0000195 | Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.\r\n
0xc0000196 | An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.\r\n
0xc0000197 | The log file has changed between reads.\r\n
0xc0000198 | The account used is an Interdomain Trust account. Use your global user account or local user account to access this server.\r\n
0xc0000199 | The account used is a Computer Account. Use your global user account or local user account to access this server.\r\n
0xc000019a | The account used is an Server Trust account. Use your global user account or local user account to access this server.\r\n
0xc000019b | The name or SID of the domain specified is inconsistent with the trust information for that domain.\r\n
0xc000019c | A volume has been accessed for which a file system driver is required that has not yet been loaded.\r\n
0xc000019d | Indicates that the specified image is already loaded as a DLL.\r\n
0xc0000201 | A remote open failed because the network open restrictions were not satisfied.\r\n
0xc0000202 | There is no user session key for the specified logon session.\r\n
0xc0000203 | The remote user session has been deleted.\r\n
0xc0000204 | Indicates the specified resource language ID cannot be found in the\r\nimage file.\r\n
0xc0000205 | Insufficient server resources exist to complete the request.\r\n
0xc0000206 | The size of the buffer is invalid for the specified operation.\r\n
0xc0000207 | The transport rejected the network address specified as invalid.\r\n
0xc0000208 | The transport rejected the network address specified due to an invalid use of a wildcard.\r\n
0xc0000209 | The transport address could not be opened because all the available addresses are in use.\r\n
0xc000020a | The transport address could not be opened because it already exists.\r\n
0xc000020b | The transport address is now closed.\r\n
0xc000020c | The transport connection is now disconnected.\r\n
0xc000020d | The transport connection has been reset.\r\n
0xc000020e | The transport cannot dynamically acquire any more nodes.\r\n
0xc000020f | The transport aborted a pending transaction.\r\n
0xc0000210 | The transport timed out a request waiting for a response.\r\n
0xc0000211 | The transport did not receive a release for a pending response.\r\n
0xc0000212 | The transport did not find a transaction matching the specific\r\ntoken.\r\n
0xc0000213 | The transport had previously responded to a transaction request.\r\n
0xc0000214 | The transport does not recognized the transaction request identifier specified.\r\n
0xc0000215 | The transport does not recognize the transaction request type specified.\r\n
0xc0000216 | The transport can only process the specified request on the server side of a session.\r\n
0xc0000217 | The transport can only process the specified request on the client side of a session.\r\n
0xc0000218 | {Registry File Failure}\r\nThe registry cannot load the hive (file):\r\n%hs\r\nor its log or alternate.\r\nIt is corrupt, absent, or not writable.\r\n
0xc0000219 | {Unexpected Failure in DebugActiveProcess}\r\nAn unexpected failure occurred while processing a DebugActiveProcess API request. You may choose OK to terminate the process, or Cancel to ignore the error.\r\n
0xc000021a | {Fatal System Error}\r\nThe %hs system process terminated unexpectedly with a status of 0x%08x (0x%08x 0x%08x).\r\nThe system has been shut down.\r\n
0xc000021b | {Data Not Accepted}\r\nThe TDI client could not handle the data received during an indication.\r\n
0xc000021c | {Unable to Retrieve Browser Server List}\r\nThe list of servers for this workgroup is not currently available.\r\n
0xc000021d | NTVDM encountered a hard error.\r\n
0xc000021e | {Cancel Timeout}\r\nThe driver %hs failed to complete a cancelled I/O request in the allotted time.\r\n
0xc000021f | {Reply Message Mismatch}\r\nAn attempt was made to reply to an LPC message, but the thread specified by the client ID in the message was not waiting on that message.\r\n
0xc0000220 | {Mapped View Alignment Incorrect}\r\nAn attempt was made to map a view of a file, but either the specified base address or the offset into the file were not aligned on the proper allocation granularity.\r\n
0xc0000221 | {Bad Image Checksum}\r\nThe image %hs is possibly corrupt. The header checksum does not match the computed checksum.\r\n
0xc0000222 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs. The data has been lost.\r\nThis error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0xc0000223 | The parameter(s) passed to the server in the client/server shared memory window were invalid. Too much data may have been put in the shared memory window.\r\n
0xc0000224 | The user's password must be changed before logging on the first time.\r\n
0xc0000225 | The object was not found.\r\n
0xc0000226 | The stream is not a tiny stream.\r\n
0xc0000227 | A transaction recover failed.\r\n
0xc0000228 | The request must be handled by the stack overflow code.\r\n
0xc0000229 | A consistency check failed.\r\n
0xc000022a | The attempt to insert the ID in the index failed because the ID is already in the index.\r\n
0xc000022b | The attempt to set the object's ID failed because the object already has an ID.\r\n
0xc000022c | Internal OFS status codes indicating how an allocation operation is handled. Either it is retried after the containing onode is moved or the extent stream is converted to a large stream.\r\n
0xc000022d | The request needs to be retried.\r\n
0xc000022e | The attempt to find the object found an object matching by ID on the volume but it is out of the scope of the handle used for the operation.\r\n
0xc000022f | The bucket array must be grown. Retry transaction after doing so.\r\n
0xc0000230 | The property set specified does not exist on the object.\r\n
0xc0000231 | The user/kernel marshalling buffer has overflowed.\r\n
0xc0000232 | The supplied variant structure contains invalid data.\r\n
0xc0000233 | Could not find a domain controller for this domain.\r\n
0xc0000234 | The user account has been automatically locked because too many invalid logon attempts or password change attempts have been requested.\r\n
0xc0000235 | NtClose was called on a handle that was protected from close via NtSetInformationObject.\r\n
0xc0000236 | The transport connection attempt was refused by the remote system.\r\n
0xc0000237 | The transport connection was gracefully closed.\r\n
0xc0000238 | The transport endpoint already has an address associated with it.\r\n
0xc0000239 | An address has not yet been associated with the transport endpoint.\r\n
0xc000023a | An operation was attempted on a nonexistent transport connection.\r\n
0xc000023b | An invalid operation was attempted on an active transport connection.\r\n
0xc000023c | The remote network is not reachable by the transport.\r\n
0xc000023d | The remote system is not reachable by the transport.\r\n
0xc000023e | The remote system does not support the transport protocol.\r\n
0xc000023f | No service is operating at the destination port of the transport on the remote system.\r\n
0xc0000240 | The request was aborted.\r\n
0xc0000241 | The transport connection was aborted by the local system.\r\n
0xc0000242 | The specified buffer contains ill-formed data.\r\n
0xc0000243 | The requested operation cannot be performed on a file with a user mapped section open.\r\n
0xc0000244 | {Audit Failed}\r\nAn attempt to generate a security audit failed.\r\n
0xc0000245 | The timer resolution was not previously set by the current process.\r\n
0xc0000246 | A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.\r\n
0xc0000247 | Attempting to login during an unauthorized time of day for this account.\r\n
0xc0000248 | The account is not authorized to login from this station.\r\n
0xc0000249 | {UP/MP Image Mismatch}\r\nThe image %hs has been modified for use on a uniprocessor system, but you are running it on a multiprocessor machine.\r\nPlease reinstall the image file.\r\n
0xc0000250 | There is insufficient account information to log you on.\r\n
0xc0000251 | {Invalid DLL Entrypoint}\r\nThe dynamic link library %hs is not written correctly. The stack pointer has been left in an inconsistent state.\r\nThe entrypoint should be declared as WINAPI or STDCALL. Select YES to fail the DLL load. Select NO to continue execution. Selecting NO may cause the application to operate incorrectly.\r\n
0xc0000252 | {Invalid Service Callback Entrypoint}\r\nThe %hs service is not written correctly. The stack pointer has been left in an inconsistent state.\r\nThe callback entrypoint should be declared as WINAPI or STDCALL. Selecting OK will cause the service to continue operation. However, the service process may operate incorrectly.\r\n
0xc0000253 | The server received the messages but did not send a reply.\r\n
0xc0000254 | There is an IP address conflict with another system on the network\r\n
0xc0000255 | There is an IP address conflict with another system on the network\r\n
0xc0000256 | {Low On Registry Space}\r\nThe system has reached the maximum size allowed for the system part of the registry.  Additional storage requests will be ignored.\r\n
0xc0000257 | The contacted server does not support the indicated part of the DFS namespace.\r\n
0xc0000258 | A callback return system service cannot be executed when no callback is active.\r\n
0xc0000259 | The service being accessed is licensed for a particular number of connections.\r\nNo more connections can be made to the service at this time because there are already as many connections as the service can accept.\r\n
0xc000025a | The password provided is too short to meet the policy of your user account.\r\nPlease choose a longer password.\r\n
0xc000025b | The policy of your user account does not allow you to change passwords too frequently.\r\nThis is done to prevent users from changing back to a familiar, but potentially discovered, password.\r\nIf you feel your password has been compromised then please contact your administrator immediately to have a new one assigned.\r\n
0xc000025c | You have attempted to change your password to one that you have used in the past.\r\nThe policy of your user account does not allow this. Please select a password that you have not previously used.\r\n
0xc000025e | You have attempted to load a legacy device driver while its device instance had been disabled.\r\n
0xc000025f | The specified compression format is unsupported.\r\n
0xc0000260 | The specified hardware profile configuration is invalid.\r\n
0xc0000261 | The specified Plug and Play registry device path is invalid.\r\n
0xc0000262 | {Driver Entry Point Not Found}\r\nThe %hs device driver could not locate the ordinal %ld in driver %hs.\r\n
0xc0000263 | {Driver Entry Point Not Found}\r\nThe %hs device driver could not locate the entry point %hs in driver %hs.\r\n
0xc0000264 | {Application Error}\r\nThe application attempted to release a resource it did not own. Click OK to terminate the application.\r\n
0xc0000265 | An attempt was made to create more links on a file than the file system supports.\r\n
0xc0000266 | The specified quota list is internally inconsistent with its descriptor.\r\n
0xc0000267 | The specified file has been relocated to offline storage.\r\n
0xc0000268 | {Windows Evaluation Notification}\r\nThe evaluation period for this installation of Windows has expired. This system will shutdown in 1 hour. To restore access to this installation of Windows, please upgrade this installation using a licensed distribution of this product.\r\n
0xc0000269 | {Illegal System DLL Relocation}\r\nThe system DLL %hs was relocated in memory. The application will not run properly.\r\nThe relocation occurred because the DLL %hs occupied an address range reserved for Windows system DLLs. The vendor supplying the DLL should be contacted for a new DLL.\r\n
0xc000026a | {License Violation}\r\nThe system has detected tampering with your registered product type. This is a violation of your software license. Tampering with product type is not permitted.\r\n
0xc000026b | {DLL Initialization Failed}\r\nThe application failed to initialize because the window station is shutting down.\r\n
0xc000026c | {Unable to Load Device Driver}\r\n%hs device driver could not be loaded.\r\nError Status was 0x%x\r\n
0xc000026d | DFS is unavailable on the contacted server.\r\n
0xc000026e | An operation was attempted to a volume after it was dismounted.\r\n
0xc000026f | An internal error occurred in the Win32 x86 emulation subsystem.\r\n
0xc0000270 | Win32 x86 emulation subsystem Floating-point stack check.\r\n
0xc0000271 | The validation process needs to continue on to the next step.\r\n
0xc0000272 | There was no match for the specified key in the index.\r\n
0xc0000273 | There are no more matches for the current index enumeration.\r\n
0xc0000275 | The NTFS file or directory is not a reparse point.\r\n
0xc0000276 | The Windows I/O reparse tag passed for the NTFS reparse point is invalid.\r\n
0xc0000277 | The Windows I/O reparse tag does not match the one present in the NTFS reparse point.\r\n
0xc0000278 | The user data passed for the NTFS reparse point is invalid.\r\n
0xc0000279 | The layered file system driver for this IO tag did not handle it when needed.\r\n
0xc0000280 | The NTFS symbolic link could not be resolved even though the initial file name is valid.\r\n
0xc0000281 | The NTFS directory is a reparse point.\r\n
0xc0000282 | The range could not be added to the range list because of a conflict.\r\n
0xc0000283 | The specified medium changer source element contains no media.\r\n
0xc0000284 | The specified medium changer destination element already contains media.\r\n
0xc0000285 | The specified medium changer element does not exist.\r\n
0xc0000286 | The specified element is contained within a magazine that is no longer present.\r\n
0xc0000287 | The device requires reinitialization due to hardware errors.\r\n
0xc000028a | The file encryption attempt failed.\r\n
0xc000028b | The file decryption attempt failed.\r\n
0xc000028c | The specified range could not be found in the range list.\r\n
0xc000028d | There is no encryption recovery policy configured for this system.\r\n
0xc000028e | The required encryption driver is not loaded for this system.\r\n
0xc000028f | The file was encrypted with a different encryption driver than is currently loaded.\r\n
0xc0000290 | There are no EFS keys defined for the user.\r\n
0xc0000291 | The specified file is not encrypted.\r\n
0xc0000292 | The specified file is not in the defined EFS export format.\r\n
0xc0000293 | The specified file is encrypted and the user does not have the ability to decrypt it.\r\n
0xc0000295 | The guid passed was not recognized as valid by a WMI data provider.\r\n
0xc0000296 | The instance name passed was not recognized as valid by a WMI data provider.\r\n
0xc0000297 | The data item id passed was not recognized as valid by a WMI data provider.\r\n
0xc0000298 | The WMI request could not be completed and should be retried.\r\n
0xc0000299 | The policy object is shared and can only be modified at the root\r\n
0xc000029a | The policy object does not exist when it should\r\n
0xc000029b | The requested policy information only lives in the Ds\r\n
0xc000029c | The volume must be upgraded to enable this feature\r\n
0xc000029d | The remote storage service is not operational at this time.\r\n
0xc000029e | The remote storage service encountered a media error.\r\n
0xc000029f | The tracking (workstation) service is not running.\r\n
0xc00002a0 | The server process is running under a SID different than that required by client.\r\n
0xc00002a1 | The specified directory service attribute or value does not exist.\r\n
0xc00002a2 | The attribute syntax specified to the directory service is invalid.\r\n
0xc00002a3 | The attribute type specified to the directory service is not defined.\r\n
0xc00002a4 | The specified directory service attribute or value already exists.\r\n
0xc00002a5 | The directory service is busy.\r\n
0xc00002a6 | The directory service is not available.\r\n
0xc00002a7 | The directory service was unable to allocate a relative identifier.\r\n
0xc00002a8 | The directory service has exhausted the pool of relative identifiers.\r\n
0xc00002a9 | The requested operation could not be performed because the directory service is not the master for that type of operation.\r\n
0xc00002aa | The directory service was unable to initialize the subsystem that allocates relative identifiers.\r\n
0xc00002ab | The requested operation did not satisfy one or more constraints associated with the class of the object.\r\n
0xc00002ac | The directory service can perform the requested operation only on a leaf object.\r\n
0xc00002ad | The directory service cannot perform the requested operation on the Relatively Defined Name (RDN) attribute of an object.\r\n
0xc00002ae | The directory service detected an attempt to modify the object class of an object.\r\n
0xc00002af | An error occurred while performing a cross domain move operation.\r\n
0xc00002b0 | Unable to Contact the Global Catalog Server.\r\n
0xc00002b1 | The requested operation requires a directory service, and none was available.\r\n
0xc00002b2 | The reparse attribute cannot be set as it is incompatible with an existing attribute.\r\n
0xc00002b3 | A group marked use for deny only cannot be enabled.\r\n
0xc00002b4 | {EXCEPTION}\r\nMultiple floating point faults.\r\n
0xc00002b5 | {EXCEPTION}\r\nMultiple floating point traps.\r\n
0xc00002b6 | The device has been removed.\r\n
0xc00002b7 | The volume change journal is being deleted.\r\n
0xc00002b8 | The volume change journal is not active.\r\n
0xc00002b9 | The requested interface is not supported.\r\n
0xc00002c1 | A directory service resource limit has been exceeded.\r\n
0xc00002c2 | {System Standby Failed}\r\nThe driver %hs does not support standby mode. Updating this driver may allow the system to go to standby mode.\r\n
0xc00002c3 | Mutual Authentication failed. The server's password is out of date at the domain controller.\r\n
0xc00002c4 | The system file %1 has become corrupt and has been replaced.\r\n
0xc00002c5 | {EXCEPTION}\r\nAlignment Error\r\nA datatype misalignment error was detected in a load or store instruction.\r\n
0xc00002c6 | The WMI data item or data block is read only.\r\n
0xc00002c7 | The WMI data item or data block could not be changed.\r\n
0xc00002c8 | {Virtual Memory Minimum Too Low}\r\nYour system is low on virtual memory. Windows is increasing the size of your virtual memory paging file.\r\nDuring this process, memory requests for some applications may be denied. For more information, see Help.\r\n
0xc00002c9 | {EXCEPTION}\r\nRegister NaT consumption faults.\r\nA NaT value is consumed on a non speculative instruction.\r\n
0xc00002ca | The medium changer's transport element contains media, which is causing the operation to fail.\r\n
0xc00002cb | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.\r\n
0xc00002cc | This operation is supported only when you are connected to the server.\r\n
0xc00002cd | Only an administrator can modify the membership list of an administrative group.\r\n
0xc00002ce | A device was removed so enumeration must be restarted.\r\n
0xc00002cf | The journal entry has been deleted from the journal.\r\n
0xc00002d0 | Cannot change the primary group ID of a domain controller account.\r\n
0xc00002d1 | {Fatal System Error}\r\nThe system image %s is not properly signed.\r\nThe file has been replaced with the signed file.\r\nThe system has been shut down.\r\n
0xc00002d2 | Device will not start without a reboot.\r\n
0xc00002d3 | Current device power state cannot support this request.\r\n
0xc00002d4 | The specified group type is invalid.\r\n
0xc00002d5 | In mixed domain no nesting of global group if group is security enabled.\r\n
0xc00002d6 | In mixed domain, cannot nest local groups with other local groups, if the group is security enabled.\r\n
0xc00002d7 | A global group cannot have a local group as a member.\r\n
0xc00002d8 | A global group cannot have a universal group as a member.\r\n
0xc00002d9 | A universal group cannot have a local group as a member.\r\n
0xc00002da | A global group cannot have a cross domain member.\r\n
0xc00002db | A local group cannot have another cross domain local group as a member.\r\n
0xc00002dc | Cannot change to security disabled group because of having primary members in this group.\r\n
0xc00002dd | The WMI operation is not supported by the data block or method.\r\n
0xc00002de | There is not enough power to complete the requested operation.\r\n
0xc00002df | Security Account Manager needs to get the boot password.\r\n
0xc00002e0 | Security Account Manager needs to get the boot key from floppy disk.\r\n
0xc00002e1 | Directory Service cannot start.\r\n
0xc00002e2 | Directory Services could not start because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.\r\n
0xc00002e3 | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Safe Mode, check the event log for more detailed information.\r\n
0xc00002e4 | The requested operation can be performed only on a global catalog server.\r\n
0xc00002e5 | A local group can only be a member of other local groups in the same domain.\r\n
0xc00002e6 | Foreign security principals cannot be members of universal groups.\r\n
0xc00002e7 | Your computer could not be joined to the domain. You have exceeded the maximum number of computer accounts you are allowed to create in this domain. Contact your system administrator to have this limit reset or increased.\r\n
0xc00002e8 | STATUS_MULTIPLE_FAULT_VIOLATION\r\n
0xc00002e9 | This operation cannot be performed on the current domain.\r\n
0xc00002ea | The directory or file cannot be created.\r\n
0xc00002eb | The system is in the process of shutting down.\r\n
0xc00002ec | Directory Services could not start because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown the system. You can use the recovery console to diagnose the system further.\r\n
0xc00002ed | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown the system. You can use the recovery console to diagnose the system further.\r\n
0xc00002ee | A security context was deleted before the context was completed.  This is considered a logon failure.\r\n
0xc00002ef | The client is trying to negotiate a context and the server requires user-to-user but didn't send a TGT reply.\r\n
0xc00002f0 | An object ID was not found in the file.\r\n
0xc00002f1 | Unable to accomplish the requested task because the local machine does not have any IP addresses.\r\n
0xc00002f2 | The supplied credential handle does not match the credential associated with the security context.\r\n
0xc00002f3 | The crypto system or checksum function is invalid because a required function is unavailable.\r\n
0xc00002f4 | The number of maximum ticket referrals has been exceeded.\r\n
0xc00002f5 | The local machine must be a Kerberos KDC (domain controller) and it is not.\r\n
0xc00002f6 | The other end of the security negotiation is requires strong crypto but it is not supported on the local machine.\r\n
0xc00002f7 | The KDC reply contained more than one principal name.\r\n
0xc00002f8 | Expected to find PA data for a hint of what etype to use, but it was not found.\r\n
0xc00002f9 | The client certificate does not contain a valid UPN, or does not match the client name\r\nin the logon request.  Please contact your administrator.\r\n
0xc00002fa | Smartcard logon is required and was not used.\r\n
0xc00002fb | An invalid request was sent to the KDC.\r\n
0xc00002fc | The KDC was unable to generate a referral for the service requested.\r\n
0xc00002fd | The encryption type requested is not supported by the KDC.\r\n
0xc00002fe | A system shutdown is in progress.\r\n
0xc00002ff | The server machine is shutting down.\r\n
0xc0000300 | This operation is not supported on a computer running Windows Server 2003 for Small Business Server\r\n
0xc0000301 | The WMI GUID is no longer available\r\n
0xc0000302 | Collection or events for the WMI GUID is already disabled.\r\n
0xc0000303 | Collection or events for the WMI GUID is already enabled.\r\n
0xc0000304 | The Master File Table on the volume is too fragmented to complete this operation.\r\n
0xc0000305 | Copy protection failure.\r\n
0xc0000306 | Copy protection error - DVD CSS Authentication failed.\r\n
0xc0000307 | Copy protection error - The given sector does not contain a valid key.\r\n
0xc0000308 | Copy protection error - DVD session key not established.\r\n
0xc0000309 | Copy protection error - The read failed because the sector is encrypted.\r\n
0xc000030a | Copy protection error - The given DVD's region does not correspond to the\r\nregion setting of the drive.\r\n
0xc000030b | Copy protection error - The drive's region setting may be permanent.\r\n
0xc0000320 | The kerberos protocol encountered an error while validating the KDC certificate during smartcard Logon.  There\r\nis more information in the system event log.\r\n
0xc0000321 | The kerberos protocol encountered an error while attempting to utilize the smartcard subsystem.\r\n
0xc0000322 | The target server does not have acceptable kerberos credentials.\r\n
0xc0000350 | The transport determined that the remote system is down.\r\n
0xc0000351 | An unsupported preauthentication mechanism was presented to the kerberos package.\r\n
0xc0000352 | The encryption algorithm used on the source file needs a bigger key buffer than the one used on the destination file.\r\n
0xc0000353 | An attempt to remove a processes DebugPort was made, but a port was not already associated with the process.\r\n
0xc0000354 | An attempt to do an operation on a debug port failed because the port is in the process of being deleted.\r\n
0xc0000355 | This version of Windows is not compatible with the behavior version of directory forest, domain or domain controller.\r\n
0xc0000356 | The specified event is currently not being audited.\r\n
0xc0000357 | The machine account was created pre-NT4.  The account needs to be recreated.\r\n
0xc0000358 | A account group cannot have a universal group as a member.\r\n
0xc0000359 | The specified image file did not have the correct format, it appears to be a 32-bit Windows image.\r\n
0xc000035a | The specified image file did not have the correct format, it appears to be a 64-bit Windows image.\r\n
0xc000035b | Client's supplied SSPI channel bindings were incorrect.\r\n
0xc000035c | The client's session has expired, so the client must reauthenticate to continue accessing the remote resources.\r\n
0xc000035d | AppHelp dialog canceled thus preventing the application from starting.\r\n
0xc000035e | The SID filtering operation removed all SIDs.\r\n
0xc000035f | The driver was not loaded because the system is booting into safe mode.\r\n
0xc0000361 | Access to %1 has been restricted by your Administrator by the default software restriction policy level.\r\n
0xc0000362 | Access to %1 has been restricted by your Administrator by location with policy rule %2 placed on path %3\r\n
0xc0000363 | Access to %1 has been restricted by your Administrator by software publisher policy.\r\n
0xc0000364 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0xc0000365 | The driver was not loaded because it failed it's initialization call.\r\n
0xc0000366 | The "%hs" encountered an error while applying power or reading the device configuration.\r\nThis may be caused by a failure of your hardware or by a poor connection.\r\n
0xc0000368 | The create operation failed because the name contained at least one mount point which resolves to a volume to which the specified device object is not attached.\r\n
0xc0000369 | The device object parameter is either not a valid device object or is not attached to the volume specified by the file name.\r\n
0xc000036a | A Machine Check Error has occurred. Please check the system eventlog for additional information.\r\n
0xc000036b | Driver %2 has been blocked from loading.\r\n
0xc000036c | Driver %2 has been blocked from loading.\r\n
0xc000036d | There was error [%2] processing the driver database.\r\n
0xc000036e | System hive size has exceeded its limit.\r\n
0xc000036f | A dynamic link library (DLL) referenced a module that was neither a DLL nor the process's executable image.\r\n
0xc0000371 | The local account store does not contain secret material for the specified account.\r\n
0xc0000372 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0xc0000373 | The system was not able to allocate enough memory to perform a stack switch.\r\n
0xc0000374 | A heap has been corrupted.\r\n
0xc0000380 | An incorrect PIN was presented to the smart card\r\n
0xc0000381 | The smart card is blocked\r\n
0xc0000382 | No PIN was presented to the smart card\r\n
0xc0000383 | No smart card available\r\n
0xc0000384 | The requested key container does not exist on the smart card\r\n
0xc0000385 | The requested certificate does not exist on the smart card\r\n
0xc0000386 | The requested keyset does not exist\r\n
0xc0000387 | A communication error with the smart card has been detected.\r\n
0xc0000388 | The system detected a possible attempt to compromise security. Please ensure that you can contact the server that authenticated you.\r\n
0xc0000389 | The smartcard certificate used for authentication has been revoked.\r\nPlease contact your system administrator.  There may be additional information in the\r\nevent log.\r\n
0xc000038a | An untrusted certificate authority was detected While processing the\r\nsmartcard certificate used for authentication.  Please contact your system\r\nadministrator.\r\n
0xc000038b | The revocation status of the smartcard certificate used for\r\nauthentication could not be determined. Please contact your system administrator.\r\n
0xc000038c | The smartcard certificate used for authentication was not trusted.  Please\r\ncontact your system administrator.\r\n
0xc000038d | The smartcard certificate used for authentication has expired.  Please\r\ncontact your system administrator.\r\n
0xc000038e | The driver could not be loaded because a previous version of the driver is still in memory.\r\n
0xc000038f | The smartcard provider could not perform the action since the context was acquired as silent.\r\n
0xc0000401 | The current user's delegated trust creation quota has been exceeded.\r\n
0xc0000402 | The total delegated trust creation quota has been exceeded.\r\n
0xc0000403 | The current user's delegated trust deletion quota has been exceeded.\r\n
0xc0000404 | The requested name already exists as a unique identifier.\r\n
0xc0000405 | The requested object has a non-unique identifier and cannot be retrieved.\r\n
0xc0000406 | The group cannot be converted due to attribute restrictions on the requested group type.\r\n
0xc0000407 | {Volume Shadow Copy Service}\r\nPlease wait while the Volume Shadow Copy Service prepares volume %hs for hibernation.\r\n
0xc0000408 | Kerberos sub-protocol User2User is required.\r\n
0xc0000409 | The system detected an overrun of a stack-based buffer in this application.  This\r\noverrun could potentially allow a malicious user to gain control of this application.\r\n
0xc000040a | The Kerberos subsystem encountered an error.  A service for user protocol request was made\r\nagainst a domain controller which does not support service for user.\r\n
0xc000040b | An attempt was made by this server to make a Kerberos constrained delegation request for a target\r\noutside of the server's realm.  This is not supported, and indicates a misconfiguration on this\r\nserver's allowed to delegate to list.  Please contact your administrator.\r\n
0xc000040c | The revocation status of the domain controller certificate used for smartcard\r\nauthentication could not be determined.  There is additional information in the system event\r\nlog. Please contact your system administrator.\r\n
0xc000040d | An untrusted certificate authority was detected while processing the\r\ndomain controller certificate used for authentication.  There is additional information in\r\nthe system event log.  Please contact your system administrator.\r\n
0xc000040e | The domain controller certificate used for smartcard logon has expired.\r\nPlease contact your system administrator with the contents of your system event log.\r\n
0xc000040f | The domain controller certificate used for smartcard logon has been revoked.\r\nPlease contact your system administrator with the contents of your system event log.\r\n
0xc0000410 | Data present in one of the parameters is more than the function can operate on.\r\n
0xc0000411 | The system has failed to hibernate (The error code is %hs).  Hibernation will be disabled until the system is restarted.\r\n
0xc0000412 | An attempt to delay-load a .dll or get a function address in a delay-loaded .dll failed.\r\n
0xc0000413 | Logon Failure: The machine you are logging onto is protected by an authentication firewall.  The specified account is not allowed to authenticate to the machine.\r\n
0xc0000414 | %hs is a 16-bit application. You do not have permissions to execute 16-bit applications. Check your permissions with your system administrator.\r\n
0xc0000415 | {Display Driver Stopped Responding}\r\nThe %hs display driver has stopped working normally.  Save your work and reboot the system to restore full display functionality.\r\nThe next time you reboot the machine a dialog will be displayed giving you a chance to report this failure to Microsoft.\r\n
0xc0000416 | The Desktop heap encountered an error while allocating session memory.  There is more information in the system event log.\r\n
0xc0000417 | An invalid parameter was passed to a C runtime function.\r\n
0xc0000418 | The authentication failed since NTLM was blocked.\r\n
0xc0000421 | Application verifier has found an error in the current process.\r\n
0xc0000424 | %2 has been blocked from loading due to incompatibility with this system. Please contact your software\r\nvendor for a compatible version of the driver.\r\n
0xc0000425 | Illegal operation attempted on a registry key which has already been unloaded.\r\n
0xc0000426 | Compression is disabled for this volume.\r\n
0xc0000427 | The requested operation could not be completed due to a file system limitation\r\n
0xc0000428 | Windows cannot verify the digital signature for this file. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source.\r\n
0xc0000429 | The implementation is not capable of performing the request.\r\n
0xc000042a | The requested operation is out of order with respect to other operations.\r\n
0xc000042b | An operation attempted to exceed an implementation-defined limit.\r\n
0xc000042c | The requested operation requires elevation.\r\n
0xc0000432 | The operation was attempted beyond the valid data length of the file.\r\n
0xc0000433 | The attempted write operation encountered a write already in progress for some portion of the range.\r\n
0xc0000434 | The page fault mappings changed in the middle of processing a fault so the operation must be retried.\r\n
0xc0000435 | The attempt to purge this file from memory failed to purge some or all the data from memory.\r\n
0xc0000440 | The requested credential requires confirmation.\r\n
0xc0000441 | The remote server sent an invalid response for a file being opened with Client Side Encryption.\r\n
0xc0000442 | Client Side Encryption is not supported by the remote server even though it claims to support it.\r\n
0xc0000443 | File is encrypted and should be opened in Client Side Encryption mode.\r\n
0xc0000444 | A new encrypted file is being created and a $EFS needs to be provided.\r\n
0xc0000445 | The SMB client requested a CSE FSCTL on a non-CSE file.\r\n
0xc0000446 | Indicates a particular Security ID may not be assigned as the label of an object.\r\n
0xc0000450 | The process hosting the driver for this device has terminated.\r\n
0xc0000451 | The requested system device cannot be identified due to multiple indistinguishable devices potentially matching the identification criteria.\r\n
0xc0000452 | The requested system device cannot be found.\r\n
0xc0000453 | This boot application must be restarted.\r\n
0xc0000500 | The specified task name is invalid.\r\n
0xc0000501 | The specified task index is invalid.\r\n
0xc0000502 | The specified thread is already joining a task.\r\n
0xc0000503 | A callback has requested to bypass native code.\r\n
0xc0000700 | The ALPC port is closed.\r\n
0xc0000701 | The ALPC message requested is no longer available.\r\n
0xc0000702 | The ALPC message supplied is invalid.\r\n
0xc0000703 | The ALPC message has been canceled.\r\n
0xc0000704 | Invalid recursive dispatch attempt.\r\n
0xc0000705 | No receive buffer has been supplied in a synchrounus request.\r\n
0xc0000706 | The connection port is used in an invalid context.\r\n
0xc0000707 | The ALPC port does not accept new request messages.\r\n
0xc0000708 | The resource requested is already in use.\r\n
0xc0000709 | The hardware has reported an uncorrectable memory error.\r\n
0xc000070a | Status 0x%08x was returned, waiting on handle 0x%x for wait 0x%p, in waiter 0x%p.\r\n
0xc000070b | After a callback to 0x%p(0x%p), a completion call to SetEvent(0x%p) failed with status 0x%08x.\r\n
0xc000070c | After a callback to 0x%p(0x%p), a completion call to ReleaseSemaphore(0x%p, %d) failed with status 0x%08x.\r\n
0xc000070d | After a callback to 0x%p(0x%p), a completion call to ReleaseMutex(%p) failed with status 0x%08x.\r\n
0xc000070e | After a callback to 0x%p(0x%p), an completion call to FreeLibrary(%p) failed with status 0x%08x.\r\n
0xc000070f | The threadpool 0x%p was released while a thread was posting a callback to 0x%p(0x%p) to it.\r\n
0xc0000710 | A threadpool worker thread is impersonating a client, after a callback to 0x%p(0x%p).\r\nThis is unexpected, indicating that the callback is missing a call to revert the impersonation.\r\n
0xc0000711 | A threadpool worker thread is impersonating a client, after executing an APC.\r\nThis is unexpected, indicating that the APC is missing a call to revert the impersonation.\r\n
0xc0000712 | Either the target process, or the target thread's containing process, is a protected process.\r\n
0xc0000713 | A Thread is getting dispatched with MCA EXCEPTION because of MCA.\r\n
0xc0000714 | The client certificate account mapping is not unique.\r\n
0xc0000715 | The symbolic link cannot be followed because its type is disabled.\r\n
0xc0000716 | Indicates that the specified string is not valid for IDN normalization.\r\n
0xc0000717 | No mapping for the Unicode character exists in the target multi-byte code page.\r\n
0xc0000718 | The provided callback is already registered.\r\n
0xc0000719 | The provided context did not match the target.\r\n
0xc000071a | The specified port already has a completion list.\r\n
0xc000071b | A threadpool worker thread enter a callback at thread base priority 0x%x and exited at priority 0x%x.\r\nThis is unexpected, indicating that the callback missed restoring the priority.\r\n
0xc000071c | An invalid thread, handle %p, is specified for this operation.  Possibly, a threadpool worker thread was specified.\r\n
0xc000071d | A threadpool worker thread enter a callback, which left transaction state.\r\nThis is unexpected, indicating that the callback missed clearing the transaction.\r\n
0xc000071e | A threadpool worker thread enter a callback, which left the loader lock held.\r\nThis is unexpected, indicating that the callback missed releasing the lock.\r\n
0xc000071f | A threadpool worker thread enter a callback, which left with preferred languages set.\r\nThis is unexpected, indicating that the callback missed clearing them.\r\n
0xc0000720 | A threadpool worker thread enter a callback, which left with background priorities set.\r\nThis is unexpected, indicating that the callback missed restoring the original priorities.\r\n
0xc0000721 | A threadpool worker thread enter a callback at thread affinity %p and exited at affinity %p.\r\nThis is unexpected, indicating that the callback missed restoring the priority.\r\n
0xc0000800 | The attempted operation required self healing to be enabled.\r\n
0xc0000801 | The Directory Service cannot perform the requested operation because a domain rename operation is in progress.\r\n
0xc0000802 | The requested file operation failed because the storage quota was exceeded.\r\nTo free up disk space, move files to a different location or delete unnecessary files. For more information, contact your system administrator.\r\n
0xc0000804 | The requested file operation failed because the storage policy blocks that type of file. For more information, contact your system administrator.\r\n
0xc0000805 | The operation could not be completed due to bad clusters on disk.\r\n
0xc0000806 | The operation could not be completed because the volume is dirty.  Please run chkdsk and try again.\r\n
0xc0000901 | This file is checked out or locked for editing by another user.\r\n
0xc0000902 | The file must be checked out before saving changes.\r\n
0xc0000903 | The file type being saved or retrieved has been blocked.\r\n
0xc0000904 | The file size exceeds the limit allowed and cannot be saved.\r\n
0xc0000905 | Access Denied.  Before opening files in this location, you must first browse to the web site and select the option to login automatically.\r\n
0xc0000906 | Operation did not complete successfully because the file contains a virus.\r\n
0xc0000907 | This file contains a virus and cannot be opened. Due to the nature of this virus, the file has been removed from this location.\r\n
0xc0000908 | The resources required for this device conflict with the MCFG table.\r\n
0xc0009898 | WOW Assertion Error.\r\n
0xc000a000 | The cryptographic signature is invalid.\r\n
0xc000a001 | The cryptographic provider does not support HMAC.\r\n
0xc000a010 | The IPSEC queue overflowed.\r\n
0xc000a011 | The neighbor discovery queue overflowed.\r\n
0xc000a012 | An ICMP hop limit exceeded error was received.\r\n
0xc000a013 | The protocol is not installed on the local machine.\r\n
0xc000a080 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0xc000a081 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0xc000a082 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0xc000a083 | Windows was unable to parse the requested XML data.\r\n
0xc000a084 | An error was encountered while processing an XML digital signature.\r\n
0xc000a085 | Indicates that the caller made the connection request in the wrong routing compartment.\r\n
0xc000a086 | Indicates that there was an AuthIP failure when attempting to connect to the remote host.\r\n
0xc0010001 | Debugger did not perform a state change.\r\n
0xc0010002 | Debugger has found the application is not idle.\r\n
0xc0020001 | The string binding is invalid.\r\n
0xc0020002 | The binding handle is not the correct type.\r\n
0xc0020003 | The binding handle is invalid.\r\n
0xc0020004 | The RPC protocol sequence is not supported.\r\n
0xc0020005 | The RPC protocol sequence is invalid.\r\n
0xc0020006 | The string UUID is invalid.\r\n
0xc0020007 | The endpoint format is invalid.\r\n
0xc0020008 | The network address is invalid.\r\n
0xc0020009 | No endpoint was found.\r\n
0xc002000a | The timeout value is invalid.\r\n
0xc002000b | The object UUID was not found.\r\n
0xc002000c | The object UUID has already been registered.\r\n
0xc002000d | The type UUID has already been registered.\r\n
0xc002000e | The RPC server is already listening.\r\n
0xc002000f | No protocol sequences have been registered.\r\n
0xc0020010 | The RPC server is not listening.\r\n
0xc0020011 | The manager type is unknown.\r\n
0xc0020012 | The interface is unknown.\r\n
0xc0020013 | There are no bindings.\r\n
0xc0020014 | There are no protocol sequences.\r\n
0xc0020015 | The endpoint cannot be created.\r\n
0xc0020016 | Not enough resources are available to complete this operation.\r\n
0xc0020017 | The RPC server is unavailable.\r\n
0xc0020018 | The RPC server is too busy to complete this operation.\r\n
0xc0020019 | The network options are invalid.\r\n
0xc002001a | There are no remote procedure calls active on this thread.\r\n
0xc002001b | The remote procedure call failed.\r\n
0xc002001c | The remote procedure call failed and did not execute.\r\n
0xc002001d | An RPC protocol error occurred.\r\n
0xc002001f | The transfer syntax is not supported by the RPC server.\r\n
0xc0020021 | The type UUID is not supported.\r\n
0xc0020022 | The tag is invalid.\r\n
0xc0020023 | The array bounds are invalid.\r\n
0xc0020024 | The binding does not contain an entry name.\r\n
0xc0020025 | The name syntax is invalid.\r\n
0xc0020026 | The name syntax is not supported.\r\n
0xc0020028 | No network address is available to use to construct a UUID.\r\n
0xc0020029 | The endpoint is a duplicate.\r\n
0xc002002a | The authentication type is unknown.\r\n
0xc002002b | The maximum number of calls is too small.\r\n
0xc002002c | The string is too long.\r\n
0xc002002d | The RPC protocol sequence was not found.\r\n
0xc002002e | The procedure number is out of range.\r\n
0xc002002f | The binding does not contain any authentication information.\r\n
0xc0020030 | The authentication service is unknown.\r\n
0xc0020031 | The authentication level is unknown.\r\n
0xc0020032 | The security context is invalid.\r\n
0xc0020033 | The authorization service is unknown.\r\n
0xc0020034 | The entry is invalid.\r\n
0xc0020035 | The operation cannot be performed.\r\n
0xc0020036 | There are no more endpoints available from the endpoint mapper.\r\n
0xc0020037 | No interfaces have been exported.\r\n
0xc0020038 | The entry name is incomplete.\r\n
0xc0020039 | The version option is invalid.\r\n
0xc002003a | There are no more members.\r\n
0xc002003b | There is nothing to unexport.\r\n
0xc002003c | The interface was not found.\r\n
0xc002003d | The entry already exists.\r\n
0xc002003e | The entry is not found.\r\n
0xc002003f | The name service is unavailable.\r\n
0xc0020040 | The network address family is invalid.\r\n
0xc0020041 | The requested operation is not supported.\r\n
0xc0020042 | No security context is available to allow impersonation.\r\n
0xc0020043 | An internal error occurred in RPC.\r\n
0xc0020044 | The RPC server attempted an integer divide by zero.\r\n
0xc0020045 | An addressing error occurred in the RPC server.\r\n
0xc0020046 | A floating point operation at the RPC server caused a divide by zero.\r\n
0xc0020047 | A floating point underflow occurred at the RPC server.\r\n
0xc0020048 | A floating point overflow occurred at the RPC server.\r\n
0xc0020049 | A remote procedure call is already in progress for this thread.\r\n
0xc002004a | There are no more bindings.\r\n
0xc002004b | The group member was not found.\r\n
0xc002004c | The endpoint mapper database entry could not be created.\r\n
0xc002004d | The object UUID is the nil UUID.\r\n
0xc002004f | No interfaces have been registered.\r\n
0xc0020050 | The remote procedure call was cancelled.\r\n
0xc0020051 | The binding handle does not contain all required information.\r\n
0xc0020052 | A communications failure occurred during a remote procedure call.\r\n
0xc0020053 | The requested authentication level is not supported.\r\n
0xc0020054 | No principal name registered.\r\n
0xc0020055 | The error specified is not a valid Windows RPC error code.\r\n
0xc0020057 | A security package specific error occurred.\r\n
0xc0020058 | Thread is not cancelled.\r\n
0xc0020062 | Invalid asynchronous remote procedure call handle.\r\n
0xc0020063 | Invalid asynchronous RPC call handle for this operation.\r\n
0xc0020064 | Access to the HTTP proxy is denied.\r\n
0xc0030001 | The list of RPC servers available for auto-handle binding has been exhausted.\r\n
0xc0030002 | The file designated by DCERPCCHARTRANS cannot be opened.\r\n
0xc0030003 | The file containing the character translation table has fewer than 512 bytes.\r\n
0xc0030004 | A null context handle is passed as an [in] parameter.\r\n
0xc0030005 | The context handle does not match any known context handles.\r\n
0xc0030006 | The context handle changed during a call.\r\n
0xc0030007 | The binding handles passed to a remote procedure call do not match.\r\n
0xc0030008 | The stub is unable to get the call handle.\r\n
0xc0030009 | A null reference pointer was passed to the stub.\r\n
0xc003000a | The enumeration value is out of range.\r\n
0xc003000b | The byte count is too small.\r\n
0xc003000c | The stub received bad data.\r\n
0xc0030059 | Invalid operation on the encoding/decoding handle.\r\n
0xc003005a | Incompatible version of the serializing package.\r\n
0xc003005b | Incompatible version of the RPC stub.\r\n
0xc003005c | The RPC pipe object is invalid or corrupted.\r\n
0xc003005d | An invalid operation was attempted on an RPC pipe object.\r\n
0xc003005e | Unsupported RPC pipe version.\r\n
0xc003005f | The RPC pipe object has already been closed.\r\n
0xc0030060 | The RPC call completed before all pipes were processed.\r\n
0xc0030061 | No more data is available from the RPC pipe.\r\n
0xc0040035 | A device is missing in the system BIOS MPS table. This device will not be used.\r\nPlease contact your system vendor for system BIOS update.\r\n
0xc0040036 | A translator failed to translate resources.\r\n
0xc0040037 | A IRQ translator failed to translate resources.\r\n
0xc0040038 | Driver %2 returned invalid ID for a child device (%3).\r\n
0xc0040039 | Reissue the given operation as a cached IO operation\r\n
0xc00a0001 | Session name %1 is invalid.\r\n
0xc00a0002 | The protocol driver %1 is invalid.\r\n
0xc00a0003 | The protocol driver %1 was not found in the system path.\r\n
0xc00a0006 | A close operation is pending on the Terminal Connection.\r\n
0xc00a0007 | There are no free output buffers available.\r\n
0xc00a0008 | The MODEM.INF file was not found.\r\n
0xc00a0009 | The modem (%1) was not found in MODEM.INF.\r\n
0xc00a000a | The modem did not accept the command sent to it.\r\nVerify the configured modem name matches the attached modem.\r\n
0xc00a000b | The modem did not respond to the command sent to it.\r\nVerify the modem is properly cabled and powered on.\r\n
0xc00a000c | Carrier detect has failed or carrier has been dropped due to disconnect.\r\n
0xc00a000d | Dial tone not detected within required time.\r\nVerify phone cable is properly attached and functional.\r\n
0xc00a000e | Busy signal detected at remote site on callback.\r\n
0xc00a000f | Voice detected at remote site on callback.\r\n
0xc00a0010 | Transport driver error\r\n
0xc00a0012 | The client you are using is not licensed to use this system. Your logon request is denied.\r\n
0xc00a0013 | The system has reached its licensed logon limit.\r\nPlease try again later.\r\n
0xc00a0014 | The system license has expired. Your logon request is denied.\r\n
0xc00a0015 | The specified session cannot be found.\r\n
0xc00a0016 | The specified session name is already in use.\r\n
0xc00a0017 | The requested operation cannot be completed because the Terminal Connection is currently busy processing a connect, disconnect, reset, or delete operation.\r\n
0xc00a0018 | An attempt has been made to connect to a session whose video mode is not supported by the current client.\r\n
0xc00a0022 | The application attempted to enable DOS graphics mode.\r\nDOS graphics mode is not supported.\r\n
0xc00a0024 | The requested operation can be performed only on the system console.\r\nThis is most often the result of a driver or system DLL requiring direct console access.\r\n
0xc00a0026 | The client failed to respond to the server connect message.\r\n
0xc00a0027 | Disconnecting the console session is not supported.\r\n
0xc00a0028 | Reconnecting a disconnected session to the console is not supported.\r\n
0xc00a002a | The request to control another session remotely was denied.\r\n
0xc00a002b | A process has requested access to a session, but has not been granted those access rights.\r\n
0xc00a002e | The Terminal Connection driver %1 is invalid.\r\n
0xc00a002f | The Terminal Connection driver %1 was not found in the system path.\r\n
0xc00a0030 | The requested session cannot be controlled remotely.\r\nYou cannot control your own session, a session that is trying to control your session,\r\na session that has no user logged on, nor control other sessions from the console.\r\n
0xc00a0031 | The requested session is not configured to allow remote control.\r\n
0xc00a0032 | The RDP protocol component %2 detected an error in the protocol stream and has disconnected the client.\r\n
0xc00a0033 | Your request to connect to this Terminal server has been rejected.\r\nYour Terminal Server Client license number has not been entered for this copy of the Terminal Client.\r\nPlease call your system administrator for help in entering a valid, unique license number for this Terminal Server Client.\r\nClick OK to continue.\r\n
0xc00a0034 | Your request to connect to this Terminal server has been rejected.\r\nYour Terminal Server Client license number is currently being used by another user.\r\nPlease call your system administrator to obtain a new copy of the Terminal Server Client with a valid, unique license number.\r\nClick OK to continue.\r\n
0xc00a0035 | The remote control of the console was terminated because the display mode was changed. Changing the display mode in a remote control session is not supported.\r\n
0xc00a0036 | Remote control could not be terminated because the specified session is not currently being remotely controlled.\r\n
0xc00a0037 | Your interactive logon privilege has been disabled.\r\nPlease contact your system administrator.\r\n
0xc00a0038 | The Terminal Server security layer detected an error in the protocol stream and has disconnected the client.\r\n
0xc00a0039 | The target session is incompatible with the current session.\r\n
0xc00b0001 | The resource loader failed to find MUI file.\r\n
0xc00b0002 | The resource loader failed to load MUI file because the file fail to pass validation.\r\n
0xc00b0003 | The RC Manifest is corrupted with garbage data or unsupported version or missing required item.\r\n
0xc00b0004 | The RC Manifest has invalid culture name.\r\n
0xc00b0005 | The RC Manifest has invalid ultimatefallback name.\r\n
0xc00b0006 | The resource loader cache doesn't have loaded MUI entry.\r\n
0xc00b0007 | User stopped resource enumeration.\r\n
0xc0130001 | The cluster node is not valid.\r\n
0xc0130002 | The cluster node already exists.\r\n
0xc0130003 | A node is in the process of joining the cluster.\r\n
0xc0130004 | The cluster node was not found.\r\n
0xc0130005 | The cluster local node information was not found.\r\n
0xc0130006 | The cluster network already exists.\r\n
0xc0130007 | The cluster network was not found.\r\n
0xc0130008 | The cluster network interface already exists.\r\n
0xc0130009 | The cluster network interface was not found.\r\n
0xc013000a | The cluster request is not valid for this object.\r\n
0xc013000b | The cluster network provider is not valid.\r\n
0xc013000c | The cluster node is down.\r\n
0xc013000d | The cluster node is not reachable.\r\n
0xc013000e | The cluster node is not a member of the cluster.\r\n
0xc013000f | A cluster join operation is not in progress.\r\n
0xc0130010 | The cluster network is not valid.\r\n
0xc0130011 | No network adapters are available.\r\n
0xc0130012 | The cluster node is up.\r\n
0xc0130013 | The cluster node is paused.\r\n
0xc0130014 | The cluster node is not paused.\r\n
0xc0130015 | No cluster security context is available.\r\n
0xc0130016 | The cluster network is not configured for internal cluster communication.\r\n
0xc0130017 | The cluster node has been poisoned.\r\n
0xc0140001 | An attempt was made to run an invalid AML opcode\r\n
0xc0140002 | The AML Interpreter Stack has overflowed\r\n
0xc0140003 | An inconsistent state has occurred\r\n
0xc0140004 | An attempt was made to access an array outside of its bounds\r\n
0xc0140005 | A required argument was not specified\r\n
0xc0140006 | A fatal error has occurred\r\n
0xc0140007 | An invalid SuperName was specified\r\n
0xc0140008 | An argument with an incorrect type was specified\r\n
0xc0140009 | An object with an incorrect type was specified\r\n
0xc014000a | A target with an incorrect type was specified\r\n
0xc014000b | An incorrect number of arguments were specified\r\n
0xc014000c | An address failed to translate\r\n
0xc014000d | An incorrect event type was specified\r\n
0xc014000e | A handler for the target already exists\r\n
0xc014000f | Invalid data for the target was specified\r\n
0xc0140010 | An invalid region for the target was specified\r\n
0xc0140011 | An attempt was made to access a field outside of the defined range\r\n
0xc0140012 | The Global system lock could not be acquired\r\n
0xc0140013 | An attempt was made to reinitialize the ACPI subsystem\r\n
0xc0140014 | The ACPI subsystem has not been initialized\r\n
0xc0140015 | An incorrect mutex was specified\r\n
0xc0140016 | The mutex is not currently owned\r\n
0xc0140017 | An attempt was made to access the mutex by a process that was not the owner\r\n
0xc0140018 | An error occurred during an access to Region Space\r\n
0xc0140019 | An attempt was made to use an incorrect table\r\n
0xc0140020 | The registration of an ACPI event failed\r\n
0xc0140021 | An ACPI Power Object failed to transition state\r\n
0xc0150001 | The requested section is not present in the activation context.\r\n
0xc0150002 | Windows was not able to process the application binding information.\r\nPlease refer to your System Event Log for further information.\r\n
0xc0150003 | The application binding data format is invalid.\r\n
0xc0150004 | The referenced assembly is not installed on your system.\r\n
0xc0150005 | The manifest file does not begin with the required tag and format information.\r\n
0xc0150006 | The manifest file contains one or more syntax errors.\r\n
0xc0150007 | The application attempted to activate a disabled activation context.\r\n
0xc0150008 | The requested lookup key was not found in any active activation context.\r\n
0xc0150009 | A component version required by the application conflicts with another component version already active.\r\n
0xc015000a | The type requested activation context section does not match the query API used.\r\n
0xc015000b | Lack of system resources has required isolated activation to be disabled for the current thread of execution.\r\n
0xc015000c | The referenced assembly could not be found.\r\n
0xc015000e | An attempt to set the process default activation context failed because the process default activation context was already set.\r\n
0xc015000f | The activation context being deactivated is not the most recently activated one.\r\n
0xc0150010 | The activation context being deactivated is not active for the current thread of execution.\r\n
0xc0150011 | The activation context being deactivated has already been deactivated.\r\n
0xc0150012 | The activation context of system default assembly could not be generated.\r\n
0xc0150013 | A component used by the isolation facility has requested to terminate the process.\r\n
0xc0150014 | The activation context activation stack for the running thread of execution is corrupt.\r\n
0xc0150015 | The application isolation metadata for this process or thread has become corrupt.\r\n
0xc0150016 | The value of an attribute in an identity is not within the legal range.\r\n
0xc0150017 | The name of an attribute in an identity is not within the legal range.\r\n
0xc0150018 | An identity contains two definitions for the same attribute.\r\n
0xc0150019 | The identity string is malformed.  This may be due to a trailing comma, more than two unnamed attributes, missing attribute name or missing attribute value.\r\n
0xc015001a | The component store has been corrupted.\r\n
0xc015001b | A component's file does not match the verification information present in the component manifest.\r\n
0xc015001c | The identities of the manifests are identical but their contents are different.\r\n
0xc015001d | The component identities are different.\r\n
0xc015001e | The assembly is not a deployment.\r\n
0xc015001f | The file is not a part of the assembly.\r\n
0xc0150020 | An advanced installer failed during setup or servicing.\r\n
0xc0150021 | The character encoding in the XML declaration did not match the encoding used in the document.\r\n
0xc0150022 | The size of the manifest exceeds the maximum allowed.\r\n
0xc0150023 | The setting is not registered.\r\n
0xc0150024 | One or more required members of the transaction are not present.\r\n
0xc0150025 | The SMI primitive installer failed during setup or servicing.\r\n
0xc0150026 | A generic command executable returned a result that indicates failure.\r\n
0xc0150027 | A component is missing file verification information in its manifest.\r\n
0xc0190001 | The function attempted to use a name that is reserved for use by another transaction.\r\n
0xc0190002 | The transaction handle associated with this operation is not valid.\r\n
0xc0190003 | The requested operation was made in the context of a transaction that is no longer active.\r\n
0xc0190004 | The Transaction Manager was unable to be successfully initialized.  Transacted operations are not supported.\r\n
0xc0190005 | Transaction support within the specified file system resource manager is not started or was shutdown due to an error.\r\n
0xc0190006 | The metadata of the RM has been corrupted.  The RM will not function.\r\n
0xc0190007 | The resource manager has attempted to prepare a transaction that it has not successfully joined.\r\n
0xc0190008 | The specified directory does not contain a file system resource manager.\r\n
0xc019000a | The remote server or share does not support transacted file operations.\r\n
0xc019000b | The requested log size for the file system resource manager is invalid.\r\n
0xc019000c | The remote server sent mismatching version number or Fid for a file opened with transactions.\r\n
0xc019000f | The RM tried to register a protocol that already exists.\r\n
0xc0190010 | The attempt to propagate the Transaction failed.\r\n
0xc0190011 | The requested propagation protocol was not registered as a CRM.\r\n
0xc0190012 | The Transaction object already has a superior enlistment, and the caller attempted an operation that would have created a new superior.  Only a single superior enlistment is allowed.\r\n
0xc0190013 | The requested operation is not valid on the Transaction object in its current state.\r\n
0xc0190014 | The caller has called a response API, but the response is not expected because the TM did not issue the corresponding request to the caller.\r\n
0xc0190015 | It is too late to perform the requested operation, since the Transaction has already been aborted.\r\n
0xc0190016 | It is too late to perform the requested operation, since the Transaction has already been committed.\r\n
0xc0190017 | The buffer passed in to NtPushTransaction or NtPullTransaction is not in a valid format.\r\n
0xc0190018 | The current transaction context associated with the thread is not a valid handle to a transaction object.\r\n
0xc0190019 | An attempt to create space in the transactional resource manager's log failed.  The failure status has been recorded in the event log.\r\n
0xc0190021 | The object (file, stream, link) corresponding to the handle has been deleted by a transaction savepoint rollback.\r\n
0xc0190022 | The specified file miniversion was not found for this transacted file open.\r\n
0xc0190023 | The specified file miniversion was found but has been invalidated. Most likely cause is a transaction savepoint rollback.\r\n
0xc0190024 | A miniversion may only be opened in the context of the transaction that created it.\r\n
0xc0190025 | It is not possible to open a miniversion with modify access.\r\n
0xc0190026 | It is not possible to create any more miniversions for this stream.\r\n
0xc0190028 | The handle has been invalidated by a transaction. The most likely cause is the presence of memory mapping on a file or an open handle when the transaction ended or rolled back to savepoint.\r\n
0xc0190030 | The log data is corrupt.\r\n
0xc0190032 | The transaction outcome is unavailable because the resource manager responsible for it has disconnected.\r\n
0xc0190033 | The request was rejected because the enlistment in question is not a superior enlistment.\r\n
0xc0190036 | The file cannot be opened transactionally, because its identity depends on the outcome of an unresolved transaction.\r\n
0xc0190037 | The operation cannot be performed because another transaction is depending on the fact that this property will not change.\r\n
0xc0190038 | The operation would involve a single file with two transactional resource managers and is therefore not allowed.\r\n
0xc0190039 | The $Txf directory must be empty for this operation to succeed.\r\n
0xc019003a | The operation would leave a transactional resource manager in an inconsistent state and is therefore not allowed.\r\n
0xc019003b | The operation could not be completed because the transaction manager does not have a log.\r\n
0xc019003c | A rollback could not be scheduled because a previously scheduled rollback has already executed or been queued for execution.\r\n
0xc019003d | The transactional metadata attribute on the file or directory %hs is corrupt and unreadable.\r\n
0xc019003e | The encryption operation could not be completed because a transaction is active.\r\n
0xc019003f | This object is not allowed to be opened in a transaction.\r\n
0xc0190040 | Memory mapping (creating a mapped section) a remote file under a transaction is not supported.\r\n
0xc0190043 | Promotion was required in order to allow the resource manager to enlist, but the transaction was set to disallow it.\r\n
0xc0190044 | This file is open for modification in an unresolved transaction and may be opened for execute only by a transacted reader.\r\n
0xc0190045 | The request to thaw frozen transactions was ignored because transactions had not previously been frozen.\r\n
0xc0190046 | Transactions cannot be frozen because a freeze is already in progress.\r\n
0xc0190047 | The target volume is not a snapshot volume.  This operation is only valid on a volume mounted as a snapshot.\r\n
0xc0190048 | The savepoint operation failed because files are open on the transaction.  This is not permitted.\r\n
0xc0190049 | The sparse operation could not be completed because a transaction is active on the file.\r\n
0xc019004a | The call to create a TransactionManager object failed because the Tm Identity stored in the logfile does not match the Tm Identity that was passed in as an argument.\r\n
0xc019004b | I/O was attempted on a section object that has been floated as a result of a transaction ending.  There is no valid data.\r\n
0xc019004c | The transactional resource manager cannot currently accept transacted work due to a transient condition such as low resources.\r\n
0xc019004d | The transactional resource manager had too many tranactions outstanding that could not be aborted.  The transactional resource manger has been shut down.\r\n
0xc019004e | The specified Transaction was unable to be opened, because it was not found.\r\n
0xc019004f | The specified ResourceManager was unable to be opened, because it was not found.\r\n
0xc0190050 | The specified Enlistment was unable to be opened, because it was not found.\r\n
0xc0190051 | The specified TransactionManager was unable to be opened, because it was not found.\r\n
0xc0190052 | The specified ResourceManager was unable to create an enlistment, because its associated TransactionManager is not online.\r\n
0xc0190053 | The specified TransactionManager was unable to create the objects contained in its logfile in the Ob namespace.  Therefore, the TransactionManager was unable to recover.\r\n
0xc0190054 | The call to create a superior Enlistment on this Transaction object could not be completed, because the Transaction object specified for the enlistment is a subordinate branch of the Transaction.  Only the root of the Transactoin can be enlisted on as a superior.\r\n
0xc0190055 | Because the associated transaction manager or resource manager has been closed, the handle is no longer valid.\r\n
0xc0190056 | The compression operation could not be completed because a transaction is active on the file.\r\n
0xc0190057 | The specified operation could not be performed on this Superior enlistment, because the enlistment was not created with the corresponding completion response in the NotificationMask.\r\n
0xc0190058 | The specified operation could not be performed, because the record that would be logged was too long.  This can occur because of two conditions:  either there are too many Enlistments on this Transaction, or the combined RecoveryInformation being logged on behalf of those Enlistments is too long.\r\n
0xc0190059 | The link tracking operation could not be completed because a transaction is active.\r\n
0xc019005a | This operation cannot be performed in a transaction.\r\n
0xc019005b | The kernel transaction manager had to abort or forget the transaction because it blocked forward progress.\r\n
0xc01a0001 | Log service found an invalid log sector.\r\n
0xc01a0002 | Log service encountered a log sector with invalid block parity.\r\n
0xc01a0003 | Log service encountered a remapped log sector.\r\n
0xc01a0004 | Log service encountered a partial or incomplete log block.\r\n
0xc01a0005 | Log service encountered an attempt access data outside the active log range.\r\n
0xc01a0006 | Log service user log marshalling buffers are exhausted.\r\n
0xc01a0007 | Log service encountered an attempt read from a marshalling area with an invalid read context.\r\n
0xc01a0008 | Log service encountered an invalid log restart area.\r\n
0xc01a0009 | Log service encountered an invalid log block version.\r\n
0xc01a000a | Log service encountered an invalid log block.\r\n
0xc01a000b | Log service encountered an attempt to read the log with an invalid read mode.\r\n
0xc01a000d | Log service encountered a corrupted metadata file.\r\n
0xc01a000e | Log service encountered a metadata file that could not be created by the log file system.\r\n
0xc01a000f | Log service encountered a metadata file with inconsistent data.\r\n
0xc01a0010 | Log service encountered an attempt to erroneously allocate or dispose reservation space.\r\n
0xc01a0011 | Log service cannot delete log file or file system container.\r\n
0xc01a0012 | Log service has reached the maximum allowable containers allocated to a log file.\r\n
0xc01a0013 | Log service has attempted to read or write backwards past the start of the log.\r\n
0xc01a0014 | Log policy could not be installed because a policy of the same type is already present.\r\n
0xc01a0015 | Log policy in question was not installed at the time of the request.\r\n
0xc01a0016 | The installed set of policies on the log is invalid.\r\n
0xc01a0017 | A policy on the log in question prevented the operation from completing.\r\n
0xc01a0018 | Log space cannot be reclaimed because the log is pinned by the archive tail.\r\n
0xc01a0019 | Log record is not a record in the log file.\r\n
0xc01a001a | Number of reserved log records or the adjustment of the number of reserved log records is invalid.\r\n
0xc01a001b | Reserved log space or the adjustment of the log space is invalid.\r\n
0xc01a001c | A new or existing archive tail or base of the active log is invalid.\r\n
0xc01a001d | Log space is exhausted.\r\n
0xc01a001e | Log is multiplexed, no direct writes to the physical log is allowed.\r\n
0xc01a001f | The operation failed because the log is a dedicated log.\r\n
0xc01a0020 | The operation requires an archive context.\r\n
0xc01a0021 | Log archival is in progress.\r\n
0xc01a0022 | The operation requires a non-ephemeral log, but the log is ephemeral.\r\n
0xc01a0023 | The log must have at least two containers before it can be read from or written to.\r\n
0xc01a0024 | A log client has already registered on the stream.\r\n
0xc01a0025 | A log client has not been registered on the stream.\r\n
0xc01a0026 | A request has already been made to handle the log full condition.\r\n
0xc01a0027 | Log service enountered an error when attempting to read from a log container.\r\n
0xc01a0028 | Log service enountered an error when attempting to write to a log container.\r\n
0xc01a0029 | Log service enountered an error when attempting open a log container.\r\n
0xc01a002a | Log service enountered an invalid container state when attempting a requested action.\r\n
0xc01a002b | Log service is not in the correct state to perform a requested action.\r\n
0xc01a002c | Log space cannot be reclaimed because the log is pinned.\r\n
0xc01a002d | Log metadata flush failed.\r\n
0xc01a002e | Security on the log and its containers is inconsistent.\r\n
0xc01a002f | Records were appended to the log or reservation changes were made, but the log could not be flushed.\r\n
0xc01a0030 | The log is pinned due to reservation consuming most of the log space.  Free some reserved records to make space available.\r\n
0xc01b00ea | {Display Driver Stopped Responding}\r\nThe %hs display driver has stopped working normally. Save your work and reboot the system to restore full display functionality. The next time you reboot the machine a dialog will be displayed giving you a chance to upload data about this failure to Microsoft.\r\n
0xc01c0001 | A handler was not defined by the filter for this operation.\r\n
0xc01c0002 | A context is already defined for this object.\r\n
0xc01c0003 | Asynchronous requests are not valid for this operation.\r\n
0xc01c0004 | Internal error code used by the filter manager to determine if a fastio operation\r\nshould be forced down the IRP path.  Mini-filters should never return this value.\r\n
0xc01c0005 | An invalid name request was made.  The name requested cannot be retrieved at this time.\r\n
0xc01c0006 | Posting this operation to a worker thread for further processing is not safe\r\nat this time because it could lead to a system deadlock.\r\n
0xc01c0007 | The Filter Manager was not initialized when a filter tried to register.  Make\r\nsure that the Filter Manager is getting loaded as a driver.\r\n
0xc01c0008 | The filter is not ready for attachment to volumes because it has not finished\r\ninitializing (FltStartFiltering has not been called).\r\n
0xc01c0009 | The filter must cleanup any operation specific context at this time because\r\nit is being removed from the system before the operation is completed by\r\nthe lower drivers.\r\n
0xc01c000a | The Filter Manager had an internal error from which it cannot recover,\r\ntherefore the operation has been failed.  This is usually the result\r\nof a filter returning an invalid value from a pre-operation callback.\r\n
0xc01c000b | The object specified for this action is in the process of being\r\ndeleted, therefore the action requested cannot be completed at\r\nthis time.\r\n
0xc01c000c | Non-paged pool must be used for this type of context.\r\n
0xc01c000d | A duplicate handler definition has been provided for an operation.\r\n
0xc01c000e | The callback data queue has been disabled.\r\n
0xc01c000f | Do not attach the filter to the volume at this time.\r\n
0xc01c0010 | Do not detach the filter from the volume at this time.\r\n
0xc01c0011 | An instance already exists at this altitude on the volume specified.\r\n
0xc01c0012 | An instance already exists with this name on the volume specified.\r\n
0xc01c0013 | The system could not find the filter specified.\r\n
0xc01c0014 | The system could not find the volume specified.\r\n
0xc01c0015 | The system could not find the instance specified.\r\n
0xc01c0016 | No registered context allocation definition was found for the given request.\r\n
0xc01c0017 | An invalid parameter was specified during context registration.\r\n
0xc01c0018 | The name requested was not found in Filter Manager's name cache and could not be retrieved from the file system.\r\n
0xc01c0019 | The requested device object does not exist for the given volume.\r\n
0xc01c001a | The specified volume is already mounted.\r\n
0xc01c001b | The specified Transaction Context is already enlisted in a transaction\r\n
0xc01c001c | The specifiec context is already attached to another object\r\n
0xc01c0020 | No waiter is present for the filter's reply to this message.\r\n
0xc01d0001 | Monitor descriptor could not be obtained.\r\n
0xc01d0002 | Format of the obtained monitor descriptor is not supported by this release.\r\n
0xc01d0003 | Checksum of the obtained monitor descriptor is invalid.\r\n
0xc01d0004 | Monitor descriptor contains an invalid standard timing block.\r\n
0xc01d0005 | WMI data block registration failed for one of the MSMonitorClass WMI subclasses.\r\n
0xc01d0006 | Provided monitor descriptor block is either corrupted or does not contain monitor's detailed serial number.\r\n
0xc01d0007 | Provided monitor descriptor block is either corrupted or does not contain monitor's user friendly name.\r\n
0xc01d0008 | There is no monitor descriptor data at the specified (offset, size) region.\r\n
0xc01d0009 | Monitor descriptor contains an invalid detailed timing block.\r\n
0xc01e0000 | Exclusive mode ownership is needed to create unmanaged primary allocation.\r\n
0xc01e0001 | The driver needs more DMA buffer space in order to complete the requested operation.\r\n
0xc01e0002 | Specified display adapter handle is invalid.\r\n
0xc01e0003 | Specified display adapter and all of its state has been reset.\r\n
0xc01e0004 | The driver stack doesn't match the expected driver model.\r\n
0xc01e0005 | Present happened but ended up into the changed desktop mode\r\n
0xc01e0006 | Nothing to present due to desktop occlusion\r\n
0xc01e0007 | Not able to present due to denial of desktop access\r\n
0xc01e0008 | Not able to present with color convertion\r\n
0xc01e0009 | The kernel driver detected a version mismatch between it and the user mode driver.\r\n
0xc01e0100 | Not enough video memory available to complete the operation.\r\n
0xc01e0101 | Couldn't probe and lock the underlying memory of an allocation.\r\n
0xc01e0102 | The allocation is currently busy.\r\n
0xc01e0103 | An object being referenced has already reached the maximum reference count and can't be referenced any further.\r\n
0xc01e0104 | A problem couldn't be solved due to some currently existing condition. The problem should be tried again later.\r\n
0xc01e0105 | A problem couldn't be solved due to some currently existing condition. The problem should be tried again immediately.\r\n
0xc01e0106 | The allocation is invalid.\r\n
0xc01e0107 | No more unswizzling aperture are currently available.\r\n
0xc01e0108 | The current allocation can't be unswizzled by an aperture.\r\n
0xc01e0109 | The request failed because a pinned allocation can't be evicted.\r\n
0xc01e0110 | The allocation can't be used from it's current segment location for the specified operation.\r\n
0xc01e0111 | A locked allocation can't be used in the current command buffer.\r\n
0xc01e0112 | The allocation being referenced has been closed permanently.\r\n
0xc01e0113 | An invalid allocation instance is being referenced.\r\n
0xc01e0114 | An invalid allocation handle is being referenced.\r\n
0xc01e0115 | The allocation being referenced doesn't belong to the current device.\r\n
0xc01e0116 | The specified allocation lost its content.\r\n
0xc01e0200 | GPU exception is detected on the given device. The device is not able to be scheduled.\r\n
0xc01e0300 | Specified VidPN topology is invalid.\r\n
0xc01e0301 | Specified VidPN topology is valid but is not supported by this model of the display adapter.\r\n
0xc01e0302 | Specified VidPN topology is valid but is not supported by the display adapter at this time, due to current allocation of its resources.\r\n
0xc01e0303 | Specified VidPN handle is invalid.\r\n
0xc01e0304 | Specified video present source is invalid.\r\n
0xc01e0305 | Specified video present target is invalid.\r\n
0xc01e0306 | Specified VidPN modality is not supported (e.g. at least two of the pinned modes are not cofunctional).\r\n
0xc01e0308 | Specified VidPN source mode set is invalid.\r\n
0xc01e0309 | Specified VidPN target mode set is invalid.\r\n
0xc01e030a | Specified video signal frequency is invalid.\r\n
0xc01e030b | Specified video signal active region is invalid.\r\n
0xc01e030c | Specified video signal total region is invalid.\r\n
0xc01e0310 | Specified video present source mode is invalid.\r\n
0xc01e0311 | Specified video present target mode is invalid.\r\n
0xc01e0312 | Pinned mode must remain in the set on VidPN's cofunctional modality enumeration.\r\n
0xc01e0313 | Specified video present path is already in VidPN's topology.\r\n
0xc01e0314 | Specified mode is already in the mode set.\r\n
0xc01e0315 | Specified video present source set is invalid.\r\n
0xc01e0316 | Specified video present target set is invalid.\r\n
0xc01e0317 | Specified video present source is already in the video present source set.\r\n
0xc01e0318 | Specified video present target is already in the video present target set.\r\n
0xc01e0319 | Specified VidPN present path is invalid.\r\n
0xc01e031a | Miniport has no recommendation for augmentation of the specified VidPN's topology.\r\n
0xc01e031b | Specified monitor frequency range set is invalid.\r\n
0xc01e031c | Specified monitor frequency range is invalid.\r\n
0xc01e031d | Specified frequency range is not in the specified monitor frequency range set.\r\n
0xc01e031f | Specified frequency range is already in the specified monitor frequency range set.\r\n
0xc01e0320 | Specified mode set is stale. Please reacquire the new mode set.\r\n
0xc01e0321 | Specified monitor source mode set is invalid.\r\n
0xc01e0322 | Specified monitor source mode is invalid.\r\n
0xc01e0323 | Miniport does not have any recommendation regarding the request to provide a functional VidPN given the current display adapter configuration.\r\n
0xc01e0324 | ID of the specified mode is already used by another mode in the set.\r\n
0xc01e0325 | System failed to determine a mode that is supported by both the display adapter and the monitor connected to it.\r\n
0xc01e0326 | Number of video present targets must be greater than or equal to the number of video present sources.\r\n
0xc01e0327 | Specified present path is not in VidPN's topology.\r\n
0xc01e0328 | Display adapter must have at least one video present source.\r\n
0xc01e0329 | Display adapter must have at least one video present target.\r\n
0xc01e032a | Specified monitor descriptor set is invalid.\r\n
0xc01e032b | Specified monitor descriptor is invalid.\r\n
0xc01e032c | Specified descriptor is not in the specified monitor descriptor set.\r\n
0xc01e032d | Specified descriptor is already in the specified monitor descriptor set.\r\n
0xc01e032e | ID of the specified monitor descriptor is already used by another descriptor in the set.\r\n
0xc01e032f | Specified video present target subset type is invalid.\r\n
0xc01e0330 | Two or more of the specified resources are not related to each other, as defined by the interface semantics.\r\n
0xc01e0331 | ID of the specified video present source is already used by another source in the set.\r\n
0xc01e0332 | ID of the specified video present target is already used by another target in the set.\r\n
0xc01e0333 | Specified VidPN source cannot be used because there is no available VidPN target to connect it to.\r\n
0xc01e0334 | Newly arrived monitor could not be associated with a display adapter.\r\n
0xc01e0335 | Display adapter in question does not have an associated VidPN manager.\r\n
0xc01e0336 | VidPN manager of the display adapter in question does not have an active VidPN.\r\n
0xc01e0337 | Specified VidPN topology is stale. Please reacquire the new topology.\r\n
0xc01e0338 | There is no monitor connected on the specified video present target.\r\n
0xc01e0339 | Specified source is not part of the specified VidPN's topology.\r\n
0xc01e033a | Specified primary surface size is invalid.\r\n
0xc01e033b | Specified visible region size is invalid.\r\n
0xc01e033c | Specified stride is invalid.\r\n
0xc01e033d | Specified pixel format is invalid.\r\n
0xc01e033e | Specified color basis is invalid.\r\n
0xc01e033f | Specified pixel value access mode is invalid.\r\n
0xc01e0340 | Specified target is not part of the specified VidPN's topology.\r\n
0xc01e0341 | Failed to acquire display mode management interface.\r\n
0xc01e0342 | Specified VidPN source is already owned by a DMM client and cannot be used until that client releases it.\r\n
0xc01e0343 | Specified VidPN is active and cannot be accessed.\r\n
0xc01e0344 | Specified VidPN present path importance ordinal is invalid.\r\n
0xc01e0345 | Specified VidPN present path content geometry transformation is invalid.\r\n
0xc01e0346 | Specified content geometry transformation is not supported on the respective VidPN present path.\r\n
0xc01e0347 | Specified gamma ramp is invalid.\r\n
0xc01e0348 | Specified gamma ramp is not supported on the respective VidPN present path.\r\n
0xc01e0349 | Multi-sampling is not supported on the respective VidPN present path.\r\n
0xc01e034a | Specified mode is not in the specified mode set.\r\n
0xc01e034d | Specified VidPN topology recommendation reason is invalid.\r\n
0xc01e034e | Specified VidPN present path content type is invalid.\r\n
0xc01e034f | Specified VidPN present path copy protection type is invalid.\r\n
0xc01e0350 | No more than one unassigned mode set can exist at any given time for a given VidPN source/target.\r\n
0xc01e0352 | Specified scanline ordering type is invalid.\r\n
0xc01e0353 | Topology changes are not allowed for the specified VidPN.\r\n
0xc01e0354 | All available importance ordinals are already used in specified topology.\r\n
0xc01e0355 | Specified primary surface has a different private format attribute than the current primary surface\r\n
0xc01e0356 | Specified mode pruning algorithm is invalid\r\n
0xc01e0357 | Specified monitor capability origin is invalid.\r\n
0xc01e0358 | Specified monitor frequency range constraint is invalid.\r\n
0xc01e0359 | Maximum supported number of present paths has been reached.\r\n
0xc01e035a | Miniport requested that augmentation be cancelled for the specified source of the specified VidPN's topology.\r\n
0xc01e035b | Specified client type was not recognized.\r\n
0xc01e035c | Client VidPN is not set on this adapter (e.g. no user mode initiated mode changes took place on this adapter yet).\r\n
0xc01e0400 | Specified display adapter child device already has an external device connected to it.\r\n
0xc01e0401 | Specified display adapter child device does not support descriptor exposure.\r\n
0xc01e0430 | The display adapter is not linked to any other adapters.\r\n
0xc01e0431 | Lead adapter in a linked configuration was not enumerated yet.\r\n
0xc01e0432 | Some chain adapters in a linked configuration were not enumerated yet.\r\n
0xc01e0433 | The chain of linked adapters is not ready to start because of an unknown failure.\r\n
0xc01e0434 | An attempt was made to start a lead link display adapter when the chain links were not started yet.\r\n
0xc01e0435 | An attempt was made to power up a lead link display adapter when the chain links were powered down.\r\n
0xc01e0436 | The adapter link was found to be in an inconsistent state. Not all adapters are in an expected PNP/Power state.\r\n
0xc01e0438 | The driver trying to start is not the same as the driver for the POSTed display adapter.\r\n
0xc01e043b | An operation is being attempted that requires the display adapter to be in a quiescent state.\r\n
0xc01e0500 | The driver does not support OPM.\r\n
0xc01e0501 | The driver does not support COPP.\r\n
0xc01e0502 | The driver does not support UAB.\r\n
0xc01e0503 | The specified encrypted parameters are invalid.\r\n
0xc01e0505 | The GDI display device passed to this function does not have any active protected outputs.\r\n
0xc01e050b | An internal error caused an operation to fail.\r\n
0xc01e050c | The function failed because the caller passed in an invalid OPM user mode handle.\r\n
0xc01e050e | A certificate could not be returned because the certificate buffer passed to the function was too small.\r\n
0xc01e050f | The DxgkDdiOpmCreateProtectedOutput function could not create a protected output because the Video Present Target is in spanning mode.\r\n
0xc01e0510 | The DxgkDdiOpmCreateProtectedOutput function could not create a protected output because the Video Present Target is in theater mode.\r\n
0xc01e0511 | The function failed because the display adapter's Hardware Functionality Scan failed to validate the graphics hardware.  \r\n
0xc01e0512 | The HDCP System Renewability Message passed to this function did not comply with section 5 of the HDCP 1.1 specification.\r\n
0xc01e0513 | The protected output cannot enable the High-bandwidth Digital Content Protection (HDCP) System because it does not support HDCP.\r\n
0xc01e0514 | The protected output cannot enable Analogue Copy Protection (ACP) because it does not support ACP.\r\n
0xc01e0515 | The protected output cannot enable the Content Generation Management System Analogue (CGMS-A) protection technology because it does not support CGMS-A.\r\n
0xc01e0516 | The DxgkDdiOPMGetInformation function cannot return the version of the SRM being used because the application never successfully passed an SRM to the protected output.  \r\n
0xc01e0517 | The DxgkDdiOPMConfigureProtectedOutput function cannot enable the specified output protection technology because the output's screen resolution is too high.  \r\n
0xc01e0518 | The DxgkDdiOPMConfigureProtectedOutput function cannot enable HDCP because the display adapter's HDCP hardware is already being used by other physical outputs.\r\n
0xc01e051a | The operating system asynchronously destroyed this OPM protected output because the operating system's state changed.  This error typically occurs because the monitor PDO associated with this protected output was removed, the monitor PDO associated with this protected output was stopped, or the protected output's session became a non-console session.\r\n
0xc01e051c | Either the DxgkDdiOPMGetCOPPCompatibleInformation, DxgkDdiOPMGetInformation, or DxgkDdiOPMConfigureProtectedOutput function failed.  This error is only returned if a protected output has OPM semantics.  DxgkDdiOPMGetCOPPCompatibleInformation always returns this error if a protected output has OPM semantics.  DxgkDdiOPMGetInformation returns this error code if the caller requested COPP specific information.  DxgkDdiOPMConfigureProtectedOutput returns this error when the caller tries to use a COPP specific command.  \r\n
0xc01e051d | The DxgkDdiOPMGetInformation and DxgkDdiOPMGetCOPPCompatibleInformation functions return this error code if the passed in sequence number is not the expected sequence number or the passed in OMAC value is invalid.\r\n
0xc01e051e | The function failed because an unexpected error occurred inside of a display driver.\r\n
0xc01e051f | Either the DxgkDdiOPMGetCOPPCompatibleInformation, DxgkDdiOPMGetInformation, or DxgkDdiOPMConfigureProtectedOutput function failed.  This error is only returned if a protected output has COPP semantics.  DxgkDdiOPMGetCOPPCompatibleInformation returns this error code if the caller requested OPM specific information.  DxgkDdiOPMGetInformation always returns this error if a protected output has COPP semantics.  DxgkDdiOPMConfigureProtectedOutput returns this error when the caller tries to use an OPM specific command.  \r\n
0xc01e0520 | The DxgkDdiOPMGetCOPPCompatibleInformation and DxgkDdiOPMConfigureProtectedOutput functions return this error if the display driver does not support the DXGKMDT_OPM_GET_ACP_AND_CGMSA_SIGNALING and DXGKMDT_OPM_SET_ACP_AND_CGMSA_SIGNALING GUIDs.\r\n
0xc01e0521 | The DxgkDdiOPMConfigureProtectedOutput function returns this error code if the passed in sequence number is not the expected sequence number or the passed in OMAC value is invalid.\r\n
0xc01e0580 | The monitor connected to the specified video output does not have an I2C bus.\r\n
0xc01e0581 | No device on the I2C bus has the specified address.\r\n
0xc01e0582 | An error occurred while transmitting data to the device on the I2C bus.\r\n
0xc01e0583 | An error occurred while receiving data from the device on the I2C bus.\r\n
0xc01e0584 | The monitor does not support the specified VCP code.\r\n
0xc01e0585 | The data received from the monitor is invalid.\r\n
0xc01e0586 | The function failed because a monitor returned an invalid Timing Status byte when the operating system used the DDC/CI Get Timing Report & Timing Message command to get a timing report from a monitor.\r\n
0xc01e0587 | A monitor returned a DDC/CI capabilities string which did not comply with the ACCESS.bus 3.0, DDC/CI 1.1, or MCCS 2 Revision 1 specification.\r\n
0xc01e0588 | An internal error caused an operation to fail.\r\n
0xc01e0589 | An operation failed because a DDC/CI message had an invalid value in its command field.\r\n
0xc01e058a | An error occurred because the field length of a DDC/CI message contained an invalid value.  \r\n
0xc01e058b | An error occurred because the checksum field in a DDC/CI message did not match the message's computed checksum value.  This error implies that the data was corrupted while it was being transmitted from a monitor to a computer.\r\n
0xc01e058c | This function failed because an invalid monitor handle was passed to it.\r\n
0xc01e058d | The operating system asynchronously destroyed the monitor which corresponds to this handle because the operating system's state changed.  This error typically occurs because the monitor PDO associated with this handle was removed, the monitor PDO associated with this handle was stopped, or a display mode change occurred.  A display mode change occurs when windows sends a WM_DISPLAYCHANGE windows message to applications.\r\n
0xc01e05e0 | This function can only be used if a program is running in the local console session.  It cannot be used if a program is running on a remote desktop session or on a terminal server session.\r\n
0xc01e05e1 | This function cannot find an actual GDI display device which corresponds to the specified GDI display device name.\r\n
0xc01e05e2 | The function failed because the specified GDI display device was not attached to the Windows desktop.\r\n
0xc01e05e3 | This function does not support GDI mirroring display devices because GDI mirroring display devices do not have any physical monitors associated with them.\r\n
0xc01e05e4 | The function failed because an invalid pointer parameter was passed to it.  A pointer parameter is invalid if it is NULL, it points to an invalid address, it points to a kernel mode address or it is not correctly aligned.\r\n
0xc01e05e5 | This function failed because the GDI device passed to it did not have any monitors associated with it.\r\n
0xc01e05e6 | An array passed to the function cannot hold all of the data that the function must copy into the array.\r\n
0xc01e05e7 | An internal error caused an operation to fail.\r\n
0xc01e05e8 | The function failed because the current session is changing its type.  This function cannot be called when the current session is changing its type.  There are currently three types of sessions: console, disconnected and remote (RDP or ICA).\r\n
0xc0210000 | This volume is locked by BitLocker Drive Encryption.\r\n
0xc0210001 | The volume is not encrypted, no key is available.\r\n
0xc0210002 | The control block for the encrypted volume is not valid.\r\n
0xc0210003 | The volume cannot be encrypted because it does not have enough free space.\r\n
0xc0210004 | The volume cannot be encrypted because the file system is not supported.\r\n
0xc0210005 | The file system is corrupt. Run CHKDSK.\r\n
0xc0210006 | The file system does not extend to the end of the volume.\r\n
0xc0210007 | This operation cannot be performed while a file system is mounted on the volume.\r\n
0xc0210008 | BitLocker Drive Encryption is not included with this version of Windows.\r\n
0xc0210009 | Requested action not allowed in the current volume state.\r\n
0xc021000a | Data supplied is malformed.\r\n
0xc021000b | The volume is not bound to the system.\r\n
0xc021000c | That volume is not a data volume.\r\n
0xc021000d | A read operation failed while converting the volume.\r\n
0xc021000e | A write operation failed while converting the volume.\r\n
0xc021000f | The control block for the encrypted volume was updated by another thread. Try again.\r\n
0xc0210010 | The encryption algorithm does not support the sector size of that volume.\r\n
0xc0210011 | BitLocker recovery authentication failed.\r\n
0xc0210012 | That volume is not the OS volume.\r\n
0xc0210013 | The BitLocker startup key or recovery password could not be read from external media.\r\n
0xc0210014 | The BitLocker startup key or recovery password file is corrupt or invalid.\r\n
0xc0210015 | The BitLocker encryption key could not be obtained from the startup key or recovery password.\r\n
0xc0210016 | The Trusted Platform Module (TPM) is disabled.\r\n
0xc0210017 | The authorization data for the Storage Root Key (SRK) of the Trusted Platform Module (TPM) is not zero.\r\n
0xc0210018 | The system boot information changed or the Trusted Platform Module (TPM) locked out access to BitLocker encryption keys until the computer is restarted.\r\n
0xc0210019 | The BitLocker encryption key could not be obtained from the Trusted Platform Module (TPM).\r\n
0xc021001a | The BitLocker encryption key could not be obtained from the Trusted Platform Module (TPM) and PIN.\r\n
0xc021001b | A boot application hash does not match the hash computed when BitLocker was turned on.\r\n
0xc021001c | The Boot Configuration Data (BCD) settings are not supported or have changed since BitLocker was enabled.\r\n
0xc021001d | Boot debugging is enabled.  Run bcdedit to turn it off.\r\n
0xc021001e | The BitLocker encryption key could not be obtained.\r\n
0xc021001f | The metadata disk region pointer is incorrect.\r\n
0xc0210020 | The backup copy of the metadata is out of date.\r\n
0xc0210021 | No action was taken as a system reboot is required.\r\n
0xc0210022 | No action was taken as BitLocker Drive Encryption is in RAW access mode.\r\n
0xc0210023 | BitLocker Drive Encryption cannot enter raw access mode for this volume.\r\n
0xc0220001 | The callout does not exist.\r\n
0xc0220002 | The filter condition does not exist.\r\n
0xc0220003 | The filter does not exist.\r\n
0xc0220004 | The layer does not exist.\r\n
0xc0220005 | The provider does not exist.\r\n
0xc0220006 | The provider context does not exist.\r\n
0xc0220007 | The sublayer does not exist.\r\n
0xc0220008 | The object does not exist.\r\n
0xc0220009 | An object with that GUID or LUID already exists.\r\n
0xc022000a | The object is referenced by other objects so cannot be deleted.\r\n
0xc022000b | The call is not allowed from within a dynamic session.\r\n
0xc022000c | The call was made from the wrong session so cannot be completed.\r\n
0xc022000d | The call must be made from within an explicit transaction.\r\n
0xc022000e | The call is not allowed from within an explicit transaction.\r\n
0xc022000f | The explicit transaction has been forcibly cancelled.\r\n
0xc0220010 | The session has been cancelled.\r\n
0xc0220011 | The call is not allowed from within a read-only transaction.\r\n
0xc0220012 | The call timed out while waiting to acquire the transaction lock.\r\n
0xc0220013 | Collection of network diagnostic events is disabled.\r\n
0xc0220014 | The operation is not supported by the specified layer.\r\n
0xc0220015 | The call is allowed for kernel-mode callers only.\r\n
0xc0220016 | The call tried to associate two objects with incompatible lifetimes.\r\n
0xc0220017 | The object is built in so cannot be deleted.\r\n
0xc0220018 | The maximum number of callouts has been reached.\r\n
0xc0220019 | A notification could not be delivered because a message queue is at its maximum capacity.\r\n
0xc022001a | The traffic parameters do not match those for the security association context.\r\n
0xc022001b | The call is not allowed for the current security association state.\r\n
0xc022001c | A required pointer is null.\r\n
0xc022001d | An enumerator is not valid.\r\n
0xc022001e | The flags field contains an invalid value.\r\n
0xc022001f | A network mask is not valid.\r\n
0xc0220020 | An FWP_RANGE is not valid.\r\n
0xc0220021 | The time interval is not valid.\r\n
0xc0220022 | An array that must contain at least one element is zero length.\r\n
0xc0220023 | The displayData.name field cannot be null.\r\n
0xc0220024 | The action type is not one of the allowed action types for a filter.\r\n
0xc0220025 | The filter weight is not valid.\r\n
0xc0220026 | A filter condition contains a match type that is not compatible with the operands.\r\n
0xc0220027 | An FWP_VALUE or FWPM_CONDITION_VALUE is of the wrong type.\r\n
0xc0220028 | An integer value is outside the allowed range.\r\n
0xc0220029 | A reserved field is non-zero.\r\n
0xc022002a | A filter cannot contain multiple conditions operating on a single field.\r\n
0xc022002b | A policy cannot contain the same keying module more than once.\r\n
0xc022002c | The action type is not compatible with the layer.\r\n
0xc022002d | The action type is not compatible with the sublayer.\r\n
0xc022002e | The raw context or the provider context is not compatible with the layer.\r\n
0xc022002f | The raw context or the provider context is not compatible with the callout.\r\n
0xc0220030 | The authentication method is not compatible with the policy type.\r\n
0xc0220031 | The Diffie-Hellman group is not compatible with the policy type.\r\n
0xc0220032 | An IKE policy cannot contain an Extended Mode policy.\r\n
0xc0220033 | The enumeration template or subscription will never match any objects.\r\n
0xc0220034 | The provider context is of the wrong type.\r\n
0xc0220035 | The parameter is incorrect.\r\n
0xc0220036 | The maximum number of sublayers has been reached.\r\n
0xc0220037 | The notification function for a callout returned an error.\r\n
0xc0220038 | The IPsec authentication transform is not valid.\r\n
0xc0220039 | The IPsec cipher transform is not valid.\r\n
0xc0220100 | The TCP/IP stack is not ready.\r\n
0xc0220101 | The injection handle is being closed by another thread.\r\n
0xc0220102 | The injection handle is stale.\r\n
0xc0220103 | The classify cannot be pended.\r\n
0xc0230002 | The binding to the network interface is being closed.\r\n
0xc0230004 | An invalid version was specified.\r\n
0xc0230005 | An invalid characteristics table was used.\r\n
0xc0230006 | Failed to find the network interface or network interface is not ready.\r\n
0xc0230007 | Failed to open the network interface.\r\n
0xc0230008 | Network interface has encountered an internal unrecoverable failure.\r\n
0xc0230009 | The multicast list on the network interface is full.\r\n
0xc023000a | An attempt was made to add a duplicate multicast address to the list.\r\n
0xc023000b | At attempt was made to remove a multicast address that was never added.\r\n
0xc023000c | Netowork interface aborted the request.\r\n
0xc023000d | Network interface can not process the request because it is being reset.\r\n
0xc023000f | An attempt was made to send an invalid packet on a network interface.\r\n
0xc0230010 | The specified request is not a valid operation for the target device.\r\n
0xc0230011 | Network interface is not ready to complete this operation.\r\n
0xc0230014 | The length of the buffer submitted for this operation is not valid.\r\n
0xc0230015 | The data used for this operation is not valid.\r\n
0xc0230016 | The length of buffer submitted for this operation is too small.\r\n
0xc0230017 | Network interface does not support this OID (Object Identifier)\r\n
0xc0230018 | The network interface has been removed.\r\n
0xc0230019 | Network interface does not support this media type.\r\n
0xc023001a | An attempt was made to remove a token ring group address that is in use by other components.\r\n
0xc023001b | An attempt was made to map a file that can not be found.\r\n
0xc023001c | An error occured while NDIS tried to map the file.\r\n
0xc023001d | An attempt was made to map a file that is alreay mapped.\r\n
0xc023001e | An attempt to allocate a hardware resource failed because the resource is used by another component.\r\n
0xc023001f | The I/O operation failed because network media is disconnected or wireless access point is out of range.\r\n
0xc0230022 | The network address used in the request is invalid.\r\n
0xc023002a | The offload operation on the network interface has been paused.\r\n
0xc023002b | Network interface was not found.\r\n
0xc023002c | The revision number specified in the structure is not supported.\r\n
0xc023002d | The specified port does not exist on this network interface.\r\n
0xc023002e | The current state of the specified port on this network interface does not support the requested operation.\r\n
0xc023002f | The miniport adapter is in lower power state.\r\n
0xc02300bb | Netword interface does not support this request.\r\n
0xc0232000 | The wireless local area network interface is in auto configuration mode and doesn't support the requested parameter change operation.\r\n
0xc0232001 | The wireless local area network interface is busy and can not perform the requested operation.\r\n
0xc0232002 | The wireless local area network interface is power down and doesn't support the requested operation.\r\n
0xc0360001 | The SPI in the packet does not match a valid IPsec SA.\r\n
0xc0360002 | Packet was received on an IPsec SA whose lifetime has expired.\r\n
0xc0360003 | Packet was received on an IPsec SA that doesn't match the packet characteristics.\r\n
0xc0360004 | Packet sequence number replay check failed.\r\n
0xc0360005 | IPsec header and/or trailer in the packet is invalid.\r\n
0xc0360006 | IPsec integrity check failed.\r\n
0xc0360007 | IPsec dropped a clear text packet.\r\n

### 6.1.7600.16385, 6.1.7601.17725

Message identifier | Message string
--- | ---
0x00000000 | STATUS_WAIT_0\r\n
0x00000001 | STATUS_WAIT_1\r\n
0x00000002 | STATUS_WAIT_2\r\n
0x00000003 | STATUS_WAIT_3\r\n
0x0000003f | STATUS_WAIT_63\r\n
0x00000080 | STATUS_ABANDONED_WAIT_0\r\n
0x000000bf | STATUS_ABANDONED_WAIT_63\r\n
0x000000c0 | STATUS_USER_APC\r\n
0x00000100 | STATUS_KERNEL_APC\r\n
0x00000101 | STATUS_ALERTED\r\n
0x00000102 | STATUS_TIMEOUT\r\n
0x00000103 | The operation that was requested is pending completion.\r\n
0x00000104 | A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.\r\n
0x00000105 | Returned by enumeration APIs to indicate more information is available to successive calls.\r\n
0x00000106 | Indicates not all privileges or groups referenced are assigned to the caller.\r\nThis allows, for example, all privileges to be disabled without having to know exactly which privileges are assigned.\r\n
0x00000107 | Some of the information to be translated has not been translated.\r\n
0x00000108 | An open/create operation completed while an oplock break is underway.\r\n
0x00000109 | A new volume has been mounted by a file system.\r\n
0x0000010a | This success level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted. The commit has now been completed.\r\n
0x0000010b | This indicates that a notify change request has been completed due to closing the handle which made the notify change request.\r\n
0x0000010c | This indicates that a notify change request is being completed and that the information is not being returned in the caller's buffer.\r\nThe caller now needs to enumerate the files to find the changes.\r\n
0x0000010d | {No Quotas}\r\nNo system quota limits are specifically set for this account.\r\n
0x0000010e | {Connect Failure on Primary Transport}\r\nAn attempt was made to connect to the remote server %hs on the primary transport, but the connection failed.\r\nThe computer WAS able to connect on a secondary transport.\r\n
0x00000110 | Page fault was a transition fault.\r\n
0x00000111 | Page fault was a demand zero fault.\r\n
0x00000112 | Page fault was a demand zero fault.\r\n
0x00000113 | Page fault was a demand zero fault.\r\n
0x00000114 | Page fault was satisfied by reading from a secondary storage device.\r\n
0x00000115 | Cached page was locked during operation.\r\n
0x00000116 | Crash dump exists in paging file.\r\n
0x00000117 | Specified buffer contains all zeros.\r\n
0x00000118 | A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.\r\n
0x00000119 | The device has succeeded a query-stop and its resource requirements have changed.\r\n
0x00000120 | The translator has translated these resources into the global space and no further translations should be performed.\r\n
0x00000121 | The directory service evaluated group memberships locally, as it was unable to contact a global catalog server.\r\n
0x00000122 | A process being terminated has no threads to terminate.\r\n
0x00000123 | The specified process is not part of a job.\r\n
0x00000124 | The specified process is part of a job.\r\n
0x00000125 | {Volume Shadow Copy Service}\r\nThe system is now ready for hibernation.\r\n
0x00000126 | A file system or file system filter driver has successfully completed an FsFilter operation.\r\n
0x00000127 | The specified interrupt vector was already connected.\r\n
0x00000128 | The specified interrupt vector is still connected.\r\n
0x00000129 | The current process is a cloned process.\r\n
0x0000012a | The file was locked and all users of the file can only read.\r\n
0x0000012b | The file was locked and at least one user of the file can write.\r\n
0x00000202 | The specified ResourceManager made no changes or updates to the resource under this transaction.\r\n
0x00000210 | The specified ring buffer was empty before the packet was successfully inserted.\r\n
0x00000211 | The specified ring buffer was full before the packet was successfully removed.\r\n
0x00000212 | The specified ring buffer has dropped below its quota of outstanding transactions.\r\n
0x00000213 | The specified ring buffer has, with the removal of the current packet, now become empty.\r\n
0x00000214 | The specified ring buffer was either previously empty or previously full which implies that the caller should signal the opposite endpoint.\r\n
0x00000215 | The oplock that was associated with this handle is now associated with a different handle.\r\n
0x00000216 | The handle with which this oplock was associated has been closed.  The oplock is now broken.\r\n
0x00000367 | An operation is blocked waiting for an oplock.\r\n
0x00010001 | Debugger handled exception\r\n
0x00010002 | Debugger continued\r\n
0x001c0001 | The IO was completed by a filter.\r\n
0x003c0001 | An attribute was successfully built.\r\n
0x40000000 | {Object Exists}\r\nAn attempt was made to create an object and the object name already existed.\r\n
0x40000001 | {Thread Suspended}\r\nA thread termination occurred while the thread was suspended. The thread was resumed, and termination proceeded.\r\n
0x40000002 | {Working Set Range Error}\r\nAn attempt was made to set the working set minimum or maximum to values which are outside of the allowable range.\r\n
0x40000003 | {Image Relocated}\r\nAn image file could not be mapped at the address specified in the image file. Local fixups must be performed on this image.\r\n
0x40000004 | This informational level status indicates that a specified registry sub-tree transaction state did not yet exist and had to be created.\r\n
0x40000005 | {Segment Load}\r\nA virtual DOS machine (VDM) is loading, unloading, or moving an MS-DOS or Win16 program segment image.\r\nAn exception is raised so a debugger can load, unload or track symbols and breakpoints within these 16-bit segments.\r\n
0x40000006 | {Local Session Key}\r\nA user session key was requested for a local RPC connection. The session key returned is a constant value and not unique to this connection.\r\n
0x40000007 | {Invalid Current Directory}\r\nThe process cannot switch to the startup current directory %hs.\r\nSelect OK to set current directory to %hs, or select CANCEL to exit.\r\n
0x40000008 | {Serial IOCTL Complete}\r\nA serial I/O operation was completed by another write to a serial port.\r\n(The IOCTL_SERIAL_XOFF_COUNTER reached zero.)\r\n
0x40000009 | {Registry Recovery}\r\nOne of the files containing the system's Registry data had to be recovered by use of a log or alternate copy. The recovery was successful.\r\n
0x4000000a | {Redundant Read}\r\nTo satisfy a read request, the NT fault-tolerant file system successfully read the requested data from a redundant copy.\r\nThis was done because the file system encountered a failure on a member of the fault-tolerant volume, but was unable to reassign the failing area of the device.\r\n
0x4000000b | {Redundant Write}\r\nTo satisfy a write request, the NT fault-tolerant file system successfully wrote a redundant copy of the information.\r\nThis was done because the file system encountered a failure on a member of the fault-tolerant volume, but was not able to reassign the failing area of the device.\r\n
0x4000000c | {Serial IOCTL Timeout}\r\nA serial I/O operation completed because the time-out period expired. (The IOCTL_SERIAL_XOFF_COUNTER had not reached zero.)\r\n
0x4000000d | {Password Too Complex}\r\nThe Windows password is too complex to be converted to a LAN Manager password. The LAN Manager password returned is a NULL string.\r\n
0x4000000e | {Machine Type Mismatch}\r\nThe image file %hs is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.\r\n
0x4000000f | {Partial Data Received}\r\nThe network transport returned partial data to its client. The remaining data will be sent later.\r\n
0x40000010 | {Expedited Data Received}\r\nThe network transport returned data to its client that was marked as expedited by the remote system.\r\n
0x40000011 | {Partial Expedited Data Received}\r\nThe network transport returned partial data to its client and this data was marked as expedited by the remote system. The remaining data will be sent later.\r\n
0x40000012 | {TDI Event Done}\r\nThe TDI indication has completed successfully.\r\n
0x40000013 | {TDI Event Pending}\r\nThe TDI indication has entered the pending state.\r\n
0x40000014 | Checking file system on %wZ\r\n
0x40000015 | {Fatal Application Exit}\r\n%hs\r\n
0x40000016 | The specified registry key is referenced by a predefined handle.\r\n
0x40000017 | {Page Unlocked}\r\nThe page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.\r\n
0x40000018 | %hs\r\n
0x40000019 | {Page Locked}\r\nOne of the pages to lock was already locked.\r\n
0x4000001a | Application popup: %1 : %2\r\n
0x4000001b | STATUS_ALREADY_WIN32\r\n
0x4000001c | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001d | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001e | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x4000001f | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000020 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000021 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000022 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000023 | {Machine Type Mismatch}\r\nThe image file %hs is valid, but is for a machine type other than the current machine.\r\n
0x40000024 | A yield execution was performed and no thread was available to run.\r\n
0x40000025 | The resumable flag to a timer API was ignored.\r\n
0x40000026 | The arbiter has deferred arbitration of these resources to its parent\r\n
0x40000027 | The device "%hs" has detected a CardBus card in its slot, but the firmware on this system is not configured to allow the CardBus controller to be run in CardBus mode.\r\nThe operating system will currently accept only 16-bit (R2) pc-cards on this controller.\r\n
0x40000028 | Exception status code used by Win32 x86 emulation subsystem.\r\n
0x40000029 | The CPUs in this multiprocessor system are not all the same revision level. To use all processors the operating system restricts itself to the features of the least capable processor in the system. Should problems occur with this system, contact the CPU manufacturer to see if this mix of processors is supported.\r\n
0x4000002a | The system was put into hibernation.\r\n
0x4000002b | The system was resumed from hibernation.\r\n
0x4000002c | Windows has detected that the system firmware (BIOS) was updated [previous firmware date = %2, current firmware date %3].\r\n
0x4000002d | A device driver is leaking locked I/O pages causing system degradation. The system has automatically enabled tracking code in order to try and catch the culprit.\r\n
0x4000002e | The ALPC message being canceled has already been retrieved from the queue on the other side.\r\n
0x4000002f | The system power state is transitioning from %2 to %3.\r\n
0x40000030 | The receive operation was successful. Check the ALPC completion list for the received message.\r\n
0x40000031 | The system power state is transitioning from %2 to %3 but could enter %4.\r\n
0x40000032 | Access to %1 is monitored by policy rule %2.\r\n
0x40000033 | A valid hibernation file has been invalidated and should be abandoned.\r\n
0x40000034 | Business rule scripts are disabled for the calling application.\r\n
0x40000294 | The system has awoken\r\n
0x40000370 | The Directory Service is shutting down.\r\n
0x40010001 | Debugger will reply later.\r\n
0x40010002 | Debugger cannot provide handle.\r\n
0x40010003 | Debugger terminated thread.\r\n
0x40010004 | Debugger terminated process.\r\n
0x40010005 | Debugger got control C.\r\n
0x40010006 | Debugger printed exception on control C.\r\n
0x40010007 | Debugger received RIP exception.\r\n
0x40010008 | Debugger received control break.\r\n
0x40010009 | Debugger command communication exception.\r\n
0x40020056 | A UUID that is valid only on this computer has been allocated.\r\n
0x400200af | Some data remains to be sent in the request buffer.\r\n
0x400a0004 | The Client Drive Mapping Service Has Connected on Terminal Connection.\r\n
0x400a0005 | The Client Drive Mapping Service Has Disconnected on Terminal Connection.\r\n
0x4015000d | A kernel mode component is releasing a reference on an activation context.\r\n
0x40190001 | The attempt to commit the Transaction completed, but it is possible that some portion of the transaction tree did not commit successfully due to heuristics.  Therefore it is possible that some data modified in the transaction may not have committed, resulting in transactional inconsistency.  If possible, check the consistency of the associated data.\r\n
0x40190034 | The transactional resource manager is already consistent. Recovery is not needed.\r\n
0x40190035 | The transactional resource manager has already been started.\r\n
0x401a000c | Log service encountered a log stream with no restart area.\r\n
0x401b00ec | {Display Driver Recovered From Failure}\r\nThe %hs display driver has detected and recovered from a failure. Some graphical operations may have failed. The next time you reboot the machine a dialog will be displayed giving you a chance to upload data about this failure to Microsoft.\r\n
0x401e000a | Specified buffer is not big enough to contain entire requested dataset. Partial data populated upto the size of the buffer. Caller needs to provide buffer of size as specified in the partially populated buffer's content (interface specific).\r\n
0x401e0307 | No mode is pinned on the specified VidPN source/target.\r\n
0x401e031e | Specified mode set does not specify preference for one of its modes.\r\n
0x401e034b | Specified data set (e.g. mode set, frequency range set, descriptor set, topology, etc.) is empty.\r\n
0x401e034c | Specified data set (e.g. mode set, frequency range set, descriptor set, topology, etc.) does not contain any more elements.\r\n
0x401e0351 | Specified content transformation is not pinned on the specified VidPN present path.\r\n
0x401e042f | Child device presence was not reliably detected.\r\n
0x401e0437 | Starting the leadlink adapter has been deferred temporarily.\r\n
0x401e0439 | The display adapter is being polled for children too frequently at the same polling level.\r\n
0x401e043a | Starting the adapter has been deferred temporarily.\r\n
0x40230001 | The request will be completed later by NDIS status indication.\r\n
0x80000001 | {EXCEPTION}\r\nGuard Page Exception\r\nA page of memory that marks the end of a data structure, such as a stack or an array, has been accessed.\r\n
0x80000002 | {EXCEPTION}\r\nAlignment Fault\r\nA datatype misalignment was detected in a load or store instruction.\r\n
0x80000003 | {EXCEPTION}\r\nBreakpoint\r\nA breakpoint has been reached.\r\n
0x80000004 | {EXCEPTION}\r\nSingle Step\r\nA single step or trace operation has just been completed.\r\n
0x80000005 | {Buffer Overflow}\r\nThe data was too large to fit into the specified buffer.\r\n
0x80000006 | {No More Files}\r\nNo more files were found which match the file specification.\r\n
0x80000007 | {Kernel Debugger Awakened}\r\nthe system debugger was awakened by an interrupt.\r\n
0x8000000a | {Handles Closed}\r\nHandles to objects have been automatically closed as a result of the requested operation.\r\n
0x8000000b | {Non-Inheritable ACL}\r\nAn access control list (ACL) contains no components that can be inherited.\r\n
0x8000000c | {GUID Substitution}\r\nDuring the translation of a global identifier (GUID) to a Windows security ID (SID), no administratively-defined GUID prefix was found. A substitute prefix was used, which will not compromise system security. However, this may provide a more restrictive access than intended.\r\n
0x8000000d | {Partial Copy}\r\nDue to protection conflicts not all the requested bytes could be copied.\r\n
0x8000000e | {Out of Paper}\r\nThe printer is out of paper.\r\n
0x8000000f | {Device Power Is Off}\r\nThe printer power has been turned off.\r\n
0x80000010 | {Device Offline}\r\nThe printer has been taken offline.\r\n
0x80000011 | {Device Busy}\r\nThe device is currently busy.\r\n
0x80000012 | {No More EAs}\r\nNo more extended attributes (EAs) were found for the file.\r\n
0x80000013 | {Illegal EA}\r\nThe specified extended attribute (EA) name contains at least one illegal character.\r\n
0x80000014 | {Inconsistent EA List}\r\nThe extended attribute (EA) list is inconsistent.\r\n
0x80000015 | {Invalid EA Flag}\r\nAn invalid extended attribute (EA) flag was set.\r\n
0x80000016 | {Verifying Disk}\r\nThe media has changed and a verify operation is in progress so no reads or writes may be performed to the device, except those used in the verify operation.\r\n
0x80000017 | {Too Much Information}\r\nThe specified access control list (ACL) contained more information than was expected.\r\n
0x80000018 | This warning level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted.\r\nThe commit has NOT been completed, but has not been rolled back either (so it may still be committed if desired).\r\n
0x8000001a | {No More Entries}\r\nNo more entries are available from an enumeration operation.\r\n
0x8000001b | {Filemark Found}\r\nA filemark was detected.\r\n
0x8000001c | {Media Changed}\r\nThe media may have changed.\r\n
0x8000001d | {I/O Bus Reset}\r\nAn I/O bus reset was detected.\r\n
0x8000001e | {End of Media}\r\nThe end of the media was encountered.\r\n
0x8000001f | Beginning of tape or partition has been detected.\r\n
0x80000020 | {Media Changed}\r\nThe media may have changed.\r\n
0x80000021 | A tape access reached a setmark.\r\n
0x80000022 | During a tape access, the end of the data written is reached.\r\n
0x80000023 | The redirector is in use and cannot be unloaded.\r\n
0x80000024 | The server is in use and cannot be unloaded.\r\n
0x80000025 | The specified connection has already been disconnected.\r\n
0x80000026 | A long jump has been executed.\r\n
0x80000027 | A cleaner cartridge is present in the tape library.\r\n
0x80000028 | The Plug and Play query operation was not successful.\r\n
0x80000029 | A frame consolidation has been executed.\r\n
0x8000002a | {Registry Hive Recovered}\r\nRegistry hive (file):\r\n%hs\r\nwas corrupted and it has been recovered. Some data might have been lost.\r\n
0x8000002b | The application is attempting to run executable code from the module %hs. This may be insecure. An alternative, %hs, is available. Should the application use the secure module %hs?\r\n
0x8000002c | The application is loading executable code from the module %hs. This is secure, but may be incompatible with previous releases of the operating system. An alternative, %hs, is available. Should the application use the secure module %hs?\r\n
0x8000002d | The create operation stopped after reaching a symbolic link.\r\n
0x8000002e | An oplock of the requested level cannot be granted.  An oplock of a lower level may be available.\r\n
0x8000002f | {No ACE Condition}\r\nThe specified access control entry (ACE) does not contain a condition.\r\n
0x80000288 | The device has indicated that cleaning is necessary.\r\n
0x80000289 | The device has indicated that it's door is open. Further operations require it closed and secured.\r\n
0x80000803 | Windows discovered a corruption in the file "%hs".\r\nThis file has now been repaired.\r\nPlease check if any data in the file was lost because of the corruption.\r\n
0x80010001 | Debugger did not handle the exception.\r\n
0x80130001 | The cluster node is already up.\r\n
0x80130002 | The cluster node is already down.\r\n
0x80130003 | The cluster network is already online.\r\n
0x80130004 | The cluster network is already offline.\r\n
0x80130005 | The cluster node is already a member of the cluster.\r\n
0x80190009 | The log could not be set to the requested size.\r\n
0x80190029 | There is no transaction metadata on the file.\r\n
0x80190031 | The file can't be recovered because there is a handle still open on it.\r\n
0x80190041 | Transaction metadata is already present on this file and cannot be superseded.\r\n
0x80190042 | A transaction scope could not be entered because the scope handler has not been initialized.\r\n
0x801b00eb | {Display Driver Stopped Responding and recovered}\r\nThe %hs display driver has stopped working normally. The recovery had been performed.\r\n
0x801c0001 | {Buffer too small}\r\nThe buffer is too small to contain the entry. No information has been written to the buffer.\r\n
0x80210001 | Volume Metadata read or write is incomplete.\r\n
0x80210002 | BitLocker encryption keys were ignored because the volume was in a transient state.\r\n
0x80370001 | A virtual machine is running with its memory allocated across multiple NUMA nodes. This does not indicate a problem unless the performance of your virtual machine is unusually slow. If you are experiencing performance problems, you may need to modify the NUMA configuration. For detailed information, see http://go.microsoft.com/fwlink/?LinkId=92362.\r\n
0x80380001 | The regeneration operation was not able to copy all data from the active plexes due to bad sectors.\r\n
0x80380002 | One or more disks were not fully migrated to the target pack. They may or may not require reimport after fixing the hardware problems.\r\n
0x80390001 | Some BCD entries were not imported correctly from the BCD store.\r\n
0x80390003 | Some BCD entries were not synchronized correctly with the firmware.\r\n
0x803a0001 | The virtualization storage subsystem has generated an error.\r\n
0xc0000001 | {Operation Failed}\r\nThe requested operation was unsuccessful.\r\n
0xc0000002 | {Not Implemented}\r\nThe requested operation is not implemented.\r\n
0xc0000003 | {Invalid Parameter}\r\nThe specified information class is not a valid information class for the specified object.\r\n
0xc0000004 | The specified information record length does not match the length required for the specified information class.\r\n
0xc0000005 | The instruction at 0x%08lx referenced memory at 0x%08lx. The memory could not be %s.\r\n
0xc0000006 | The instruction at 0x%p referenced memory at 0x%p. The required data was not placed into memory because of an I/O error status of 0x%x.\r\n
0xc0000007 | The pagefile quota for the process has been exhausted.\r\n
0xc0000008 | An invalid HANDLE was specified.\r\n
0xc0000009 | An invalid initial stack was specified in a call to NtCreateThread.\r\n
0xc000000a | An invalid initial start address was specified in a call to NtCreateThread.\r\n
0xc000000b | An invalid Client ID was specified.\r\n
0xc000000c | An attempt was made to cancel or set a timer that has an associated APC and the subject thread is not the thread that originally set the timer with an associated APC routine.\r\n
0xc000000d | An invalid parameter was passed to a service or function.\r\n
0xc000000e | A device which does not exist was specified.\r\n
0xc000000f | {File Not Found}\r\nThe file %hs does not exist.\r\n
0xc0000010 | The specified request is not a valid operation for the target device.\r\n
0xc0000011 | The end-of-file marker has been reached. There is no valid data in the file beyond this marker.\r\n
0xc0000012 | {Wrong Volume}\r\nThe wrong volume is in the drive.\r\nPlease insert volume %hs into drive %hs.\r\n
0xc0000013 | {No Disk}\r\nThere is no disk in the drive.\r\nPlease insert a disk into drive %hs.\r\n
0xc0000014 | {Unknown Disk Format}\r\nThe disk in drive %hs is not formatted properly.\r\nPlease check the disk, and reformat if necessary.\r\n
0xc0000015 | {Sector Not Found}\r\nThe specified sector does not exist.\r\n
0xc0000016 | {Still Busy}\r\nThe specified I/O request packet (IRP) cannot be disposed of because the I/O operation is not complete.\r\n
0xc0000017 | {Not Enough Quota}\r\nNot enough virtual memory or paging file quota is available to complete the specified operation.\r\n
0xc0000018 | {Conflicting Address Range}\r\nThe specified address range conflicts with the address space.\r\n
0xc0000019 | Address range to unmap is not a mapped view.\r\n
0xc000001a | Virtual memory cannot be freed.\r\n
0xc000001b | Specified section cannot be deleted.\r\n
0xc000001c | An invalid system service was specified in a system service call.\r\n
0xc000001d | {EXCEPTION}\r\nIllegal Instruction\r\nAn attempt was made to execute an illegal instruction.\r\n
0xc000001e | {Invalid Lock Sequence}\r\nAn attempt was made to execute an invalid lock sequence.\r\n
0xc000001f | {Invalid Mapping}\r\nAn attempt was made to create a view for a section which is bigger than the section.\r\n
0xc0000020 | {Bad File}\r\nThe attributes of the specified mapping file for a section of memory cannot be read.\r\n
0xc0000021 | {Already Committed}\r\nThe specified address range is already committed.\r\n
0xc0000022 | {Access Denied}\r\nA process has requested access to an object, but has not been granted those access rights.\r\n
0xc0000023 | {Buffer Too Small}\r\nThe buffer is too small to contain the entry. No information has been written to the buffer.\r\n
0xc0000024 | {Wrong Type}\r\nThere is a mismatch between the type of object required by the requested operation and the type of object that is specified in the request.\r\n
0xc0000025 | {EXCEPTION}\r\nCannot Continue\r\nWindows cannot continue from this exception.\r\n
0xc0000026 | An invalid exception disposition was returned by an exception handler.\r\n
0xc0000027 | Unwind exception code.\r\n
0xc0000028 | An invalid or unaligned stack was encountered during an unwind operation.\r\n
0xc0000029 | An invalid unwind target was encountered during an unwind operation.\r\n
0xc000002a | An attempt was made to unlock a page of memory which was not locked.\r\n
0xc000002b | Device parity error on I/O operation.\r\n
0xc000002c | An attempt was made to decommit uncommitted virtual memory.\r\n
0xc000002d | An attempt was made to change the attributes on memory that has not been committed.\r\n
0xc000002e | Invalid Object Attributes specified to NtCreatePort or invalid Port Attributes specified to NtConnectPort\r\n
0xc000002f | Length of message passed to NtRequestPort or NtRequestWaitReplyPort was longer than the maximum message allowed by the port.\r\n
0xc0000030 | An invalid combination of parameters was specified.\r\n
0xc0000031 | An attempt was made to lower a quota limit below the current usage.\r\n
0xc0000032 | {Corrupt Disk}\r\nThe file system structure on the disk is corrupt and unusable.\r\nPlease run the Chkdsk utility on the volume %hs.\r\n
0xc0000033 | Object Name invalid.\r\n
0xc0000034 | Object Name not found.\r\n
0xc0000035 | Object Name already exists.\r\n
0xc0000037 | Attempt to send a message to a disconnected communication port.\r\n
0xc0000038 | An attempt was made to attach to a device that was already attached to another device.\r\n
0xc0000039 | Object Path Component was not a directory object.\r\n
0xc000003a | {Path Not Found}\r\nThe path %hs does not exist.\r\n
0xc000003b | Object Path Component was not a directory object.\r\n
0xc000003c | {Data Overrun}\r\nA data overrun error occurred.\r\n
0xc000003d | {Data Late}\r\nA data late error occurred.\r\n
0xc000003e | {Data Error}\r\nAn error in reading or writing data occurred.\r\n
0xc000003f | {Bad CRC}\r\nA cyclic redundancy check (CRC) checksum error occurred.\r\n
0xc0000040 | {Section Too Large}\r\nThe specified section is too big to map the file.\r\n
0xc0000041 | The NtConnectPort request is refused.\r\n
0xc0000042 | The type of port handle is invalid for the operation requested.\r\n
0xc0000043 | A file cannot be opened because the share access flags are incompatible.\r\n
0xc0000044 | Insufficient quota exists to complete the operation\r\n
0xc0000045 | The specified page protection was not valid.\r\n
0xc0000046 | An attempt to release a mutant object was made by a thread that was not the owner of the mutant object.\r\n
0xc0000047 | An attempt was made to release a semaphore such that its maximum count would have been exceeded.\r\n
0xc0000048 | An attempt to set a process's DebugPort or ExceptionPort was made, but a port already exists in the process or an attempt to set a file's CompletionPort made, but a port was already set in the file or an attempt to set an ALPC port's associated completion port was made, but it is already set.\r\n
0xc0000049 | An attempt was made to query image information on a section which does not map an image.\r\n
0xc000004a | An attempt was made to suspend a thread whose suspend count was at its maximum.\r\n
0xc000004b | An attempt was made to access a thread that has begun termination.\r\n
0xc000004c | An attempt was made to set the working set limit to an invalid value (minimum greater than maximum, etc).\r\n
0xc000004d | A section was created to map a file which is not compatible to an already existing section which maps the same file.\r\n
0xc000004e | A view to a section specifies a protection which is incompatible with the initial view's protection.\r\n
0xc000004f | An operation involving EAs failed because the file system does not support EAs.\r\n
0xc0000050 | An EA operation failed because EA set is too large.\r\n
0xc0000051 | An EA operation failed because the name or EA index is invalid.\r\n
0xc0000052 | The file for which EAs were requested has no EAs.\r\n
0xc0000053 | The EA is corrupt and non-readable.\r\n
0xc0000054 | A requested read/write cannot be granted due to a conflicting file lock.\r\n
0xc0000055 | A requested file lock cannot be granted due to other existing locks.\r\n
0xc0000056 | A non close operation has been requested of a file object with a delete pending.\r\n
0xc0000057 | An attempt was made to set the control attribute on a file. This attribute is not supported in the target file system.\r\n
0xc0000058 | Indicates a revision number encountered or specified is not one known by the service. It may be a more recent revision than the service is aware of.\r\n
0xc0000059 | Indicates two revision levels are incompatible.\r\n
0xc000005a | Indicates a particular Security ID may not be assigned as the owner of an object.\r\n
0xc000005b | Indicates a particular Security ID may not be assigned as the primary group of an object.\r\n
0xc000005c | An attempt has been made to operate on an impersonation token by a thread that is not currently impersonating a client.\r\n
0xc000005d | A mandatory group may not be disabled.\r\n
0xc000005e | There are currently no logon servers available to service the logon request.\r\n
0xc000005f | A specified logon session does not exist. It may already have been terminated.\r\n
0xc0000060 | A specified privilege does not exist.\r\n
0xc0000061 | A required privilege is not held by the client.\r\n
0xc0000062 | The name provided is not a properly formed account name.\r\n
0xc0000063 | The specified account already exists.\r\n
0xc0000064 | The specified account does not exist.\r\n
0xc0000065 | The specified group already exists.\r\n
0xc0000066 | The specified group does not exist.\r\n
0xc0000067 | The specified user account is already in the specified group account. Also used to indicate a group cannot be deleted because it contains a member.\r\n
0xc0000068 | The specified user account is not a member of the specified group account.\r\n
0xc0000069 | Indicates the requested operation would disable or delete the last remaining administration account.\r\nThis is not allowed to prevent creating a situation in which the system cannot be administrated.\r\n
0xc000006a | When trying to update a password, this return status indicates that the value provided as the current password is not correct.\r\n
0xc000006b | When trying to update a password, this return status indicates that the value provided for the new password contains values that are not allowed in passwords.\r\n
0xc000006c | When trying to update a password, this status indicates that some password update rule has been violated. For example, the password may not meet length criteria.\r\n
0xc000006d | The attempted logon is invalid. This is either due to a bad username or authentication information.\r\n
0xc000006e | Indicates a referenced user name and authentication information are valid, but some user account restriction has prevented successful authentication (such as time-of-day restrictions).\r\n
0xc000006f | The user account has time restrictions and may not be logged onto at this time.\r\n
0xc0000070 | The user account is restricted such that it may not be used to log on from the source workstation.\r\n
0xc0000071 | The user account's password has expired.\r\n
0xc0000072 | The referenced account is currently disabled and may not be logged on to.\r\n
0xc0000073 | None of the information to be translated has been translated.\r\n
0xc0000074 | The number of LUIDs requested may not be allocated with a single allocation.\r\n
0xc0000075 | Indicates there are no more LUIDs to allocate.\r\n
0xc0000076 | Indicates the sub-authority value is invalid for the particular use.\r\n
0xc0000077 | Indicates the ACL structure is not valid.\r\n
0xc0000078 | Indicates the SID structure is not valid.\r\n
0xc0000079 | Indicates the SECURITY_DESCRIPTOR structure is not valid.\r\n
0xc000007a | Indicates the specified procedure address cannot be found in the DLL.\r\n
0xc000007b | {Bad Image}\r\n%hs is either not designed to run on Windows or it contains an error. Try installing the program again using the original installation media or contact your system administrator or the software vendor for support.\r\n
0xc000007c | An attempt was made to reference a token that doesn't exist.\r\nThis is typically done by referencing the token associated with a thread when the thread is not impersonating a client.\r\n
0xc000007d | Indicates that an attempt to build either an inherited ACL or ACE was not successful.\r\nThis can be caused by a number of things. One of the more probable causes is the replacement of a CreatorId with an SID that didn't fit into the ACE or ACL.\r\n
0xc000007e | The range specified in NtUnlockFile was not locked.\r\n
0xc000007f | An operation failed because the disk was full.\r\n
0xc0000080 | The GUID allocation server is [already] disabled at the moment.\r\n
0xc0000081 | The GUID allocation server is [already] enabled at the moment.\r\n
0xc0000082 | Too many GUIDs were requested from the allocation server at once.\r\n
0xc0000083 | The GUIDs could not be allocated because the Authority Agent was exhausted.\r\n
0xc0000084 | The value provided was an invalid value for an identifier authority.\r\n
0xc0000085 | There are no more authority agent values available for the given identifier authority value.\r\n
0xc0000086 | An invalid volume label has been specified.\r\n
0xc0000087 | A mapped section could not be extended.\r\n
0xc0000088 | Specified section to flush does not map a data file.\r\n
0xc0000089 | Indicates the specified image file did not contain a resource section.\r\n
0xc000008a | Indicates the specified resource type cannot be found in the image file.\r\n
0xc000008b | Indicates the specified resource name cannot be found in the image file.\r\n
0xc000008c | {EXCEPTION}\r\nArray bounds exceeded.\r\n
0xc000008d | {EXCEPTION}\r\nFloating-point denormal operand.\r\n
0xc000008e | {EXCEPTION}\r\nFloating-point division by zero.\r\n
0xc000008f | {EXCEPTION}\r\nFloating-point inexact result.\r\n
0xc0000090 | {EXCEPTION}\r\nFloating-point invalid operation.\r\n
0xc0000091 | {EXCEPTION}\r\nFloating-point overflow.\r\n
0xc0000092 | {EXCEPTION}\r\nFloating-point stack check.\r\n
0xc0000093 | {EXCEPTION}\r\nFloating-point underflow.\r\n
0xc0000094 | {EXCEPTION}\r\nInteger division by zero.\r\n
0xc0000095 | {EXCEPTION}\r\nInteger overflow.\r\n
0xc0000096 | {EXCEPTION}\r\nPrivileged instruction.\r\n
0xc0000097 | An attempt was made to install more paging files than the system supports.\r\n
0xc0000098 | The volume for a file has been externally altered such that the opened file is no longer valid.\r\n
0xc0000099 | When a block of memory is allotted for future updates, such as the memory allocated to hold discretionary access control and primary group information, successive updates may exceed the amount of memory originally allotted.\r\nSince quota may already have been charged to several processes which have handles to the object, it is not reasonable to alter the size of the allocated memory.\r\nInstead, a request that requires more memory than has been allotted must fail and the STATUS_ALLOTED_SPACE_EXCEEDED error returned.\r\n
0xc000009a | Insufficient system resources exist to complete the API.\r\n
0xc000009b | An attempt has been made to open a DFS exit path control file.\r\n
0xc000009c | STATUS_DEVICE_DATA_ERROR\r\n
0xc000009d | STATUS_DEVICE_NOT_CONNECTED\r\n
0xc000009e | STATUS_DEVICE_POWER_FAILURE\r\n
0xc000009f | Virtual memory cannot be freed as base address is not the base of the region and a region size of zero was specified.\r\n
0xc00000a0 | An attempt was made to free virtual memory which is not allocated.\r\n
0xc00000a1 | The working set is not big enough to allow the requested pages to be locked.\r\n
0xc00000a2 | {Write Protect Error}\r\nThe disk cannot be written to because it is write protected. Please remove the write protection from the volume %hs in drive %hs.\r\n
0xc00000a3 | {Drive Not Ready}\r\nThe drive is not ready for use; its door may be open. Please check drive %hs and make sure that a disk is inserted and that the drive door is closed.\r\n
0xc00000a4 | The specified attributes are invalid, or incompatible with the attributes for the group as a whole.\r\n
0xc00000a5 | A specified impersonation level is invalid.\r\nAlso used to indicate a required impersonation level was not provided.\r\n
0xc00000a6 | An attempt was made to open an Anonymous level token.\r\nAnonymous tokens may not be opened.\r\n
0xc00000a7 | The validation information class requested was invalid.\r\n
0xc00000a8 | The type of a token object is inappropriate for its attempted use.\r\n
0xc00000a9 | The type of a token object is inappropriate for its attempted use.\r\n
0xc00000aa | An attempt was made to execute an instruction at an unaligned address and the host system does not support unaligned instruction references.\r\n
0xc00000ab | The maximum named pipe instance count has been reached.\r\n
0xc00000ac | An instance of a named pipe cannot be found in the listening state.\r\n
0xc00000ad | The named pipe is not in the connected or closing state.\r\n
0xc00000ae | The specified pipe is set to complete operations and there are current I/O operations queued so it cannot be changed to queue operations.\r\n
0xc00000af | The specified handle is not open to the server end of the named pipe.\r\n
0xc00000b0 | The specified named pipe is in the disconnected state.\r\n
0xc00000b1 | The specified named pipe is in the closing state.\r\n
0xc00000b2 | The specified named pipe is in the connected state.\r\n
0xc00000b3 | The specified named pipe is in the listening state.\r\n
0xc00000b4 | The specified named pipe is not in message mode.\r\n
0xc00000b5 | {Device Timeout}\r\nThe specified I/O operation on %hs was not completed before the time-out period expired.\r\n
0xc00000b6 | The specified file has been closed by another process.\r\n
0xc00000b7 | Profiling not started.\r\n
0xc00000b8 | Profiling not stopped.\r\n
0xc00000b9 | The passed ACL did not contain the minimum required information.\r\n
0xc00000ba | The file that was specified as a target is a directory and the caller specified that it could be anything but a directory.\r\n
0xc00000bb | The request is not supported.\r\n
0xc00000bc | This remote computer is not listening.\r\n
0xc00000bd | A duplicate name exists on the network.\r\n
0xc00000be | The network path cannot be located.\r\n
0xc00000bf | The network is busy.\r\n
0xc00000c0 | This device does not exist.\r\n
0xc00000c1 | The network BIOS command limit has been reached.\r\n
0xc00000c2 | An I/O adapter hardware error has occurred.\r\n
0xc00000c3 | The network responded incorrectly.\r\n
0xc00000c4 | An unexpected network error occurred.\r\n
0xc00000c5 | The remote adapter is not compatible.\r\n
0xc00000c6 | The printer queue is full.\r\n
0xc00000c7 | Space to store the file waiting to be printed is not available on the server.\r\n
0xc00000c8 | The requested print file has been canceled.\r\n
0xc00000c9 | The network name was deleted.\r\n
0xc00000ca | Network access is denied.\r\n
0xc00000cb | {Incorrect Network Resource Type}\r\nThe specified device type (LPT, for example) conflicts with the actual device type on the remote resource.\r\n
0xc00000cc | {Network Name Not Found}\r\nThe specified share name cannot be found on the remote server.\r\n
0xc00000cd | The name limit for the local computer network adapter card was exceeded.\r\n
0xc00000ce | The network BIOS session limit was exceeded.\r\n
0xc00000cf | File sharing has been temporarily paused.\r\n
0xc00000d0 | No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept.\r\n
0xc00000d1 | Print or disk redirection is temporarily paused.\r\n
0xc00000d2 | A network data fault occurred.\r\n
0xc00000d3 | The number of active profiling objects is at the maximum and no more may be started.\r\n
0xc00000d4 | {Incorrect Volume}\r\nThe target file of a rename request is located on a different device than the source of the rename request.\r\n
0xc00000d5 | The file specified has been renamed and thus cannot be modified.\r\n
0xc00000d6 | {Network Request Timeout}\r\nThe session with a remote server has been disconnected because the time-out interval for a request has expired.\r\n
0xc00000d7 | Indicates an attempt was made to operate on the security of an object that does not have security associated with it.\r\n
0xc00000d8 | Used to indicate that an operation cannot continue without blocking for I/O.\r\n
0xc00000d9 | Used to indicate that a read operation was done on an empty pipe.\r\n
0xc00000da | Configuration information could not be read from the domain controller, either because the machine is unavailable, or access has been denied.\r\n
0xc00000db | Indicates that a thread attempted to terminate itself by default (called NtTerminateThread with NULL) and it was the last thread in the current process.\r\n
0xc00000dc | Indicates the Sam Server was in the wrong state to perform the desired operation.\r\n
0xc00000dd | Indicates the Domain was in the wrong state to perform the desired operation.\r\n
0xc00000de | This operation is only allowed for the Primary Domain Controller of the domain.\r\n
0xc00000df | The specified Domain did not exist.\r\n
0xc00000e0 | The specified Domain already exists.\r\n
0xc00000e1 | An attempt was made to exceed the limit on the number of domains per server for this release.\r\n
0xc00000e2 | Error status returned when oplock request is denied.\r\n
0xc00000e3 | Error status returned when an invalid oplock acknowledgment is received by a file system.\r\n
0xc00000e4 | This error indicates that the requested operation cannot be completed due to a catastrophic media failure or on-disk data structure corruption.\r\n
0xc00000e5 | An internal error occurred.\r\n
0xc00000e6 | Indicates generic access types were contained in an access mask which should already be mapped to non-generic access types.\r\n
0xc00000e7 | Indicates a security descriptor is not in the necessary format (absolute or self-relative).\r\n
0xc00000e8 | An access to a user buffer failed at an "expected" point in time. This code is defined since the caller does not want to accept STATUS_ACCESS_VIOLATION in its filter.\r\n
0xc00000e9 | If an I/O error is returned which is not defined in the standard FsRtl filter, it is converted to the following error which is guaranteed to be in the filter. In this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ea | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter. In this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000eb | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter. In this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ec | If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter. In this case information is lost, however, the filter correctly handles the exception.\r\n
0xc00000ed | The requested action is restricted for use by logon processes only. The calling process has not registered as a logon process.\r\n
0xc00000ee | An attempt has been made to start a new session manager or LSA logon session with an ID that is already in use.\r\n
0xc00000ef | An invalid parameter was passed to a service or function as the first argument.\r\n
0xc00000f0 | An invalid parameter was passed to a service or function as the second argument.\r\n
0xc00000f1 | An invalid parameter was passed to a service or function as the third argument.\r\n
0xc00000f2 | An invalid parameter was passed to a service or function as the fourth argument.\r\n
0xc00000f3 | An invalid parameter was passed to a service or function as the fifth argument.\r\n
0xc00000f4 | An invalid parameter was passed to a service or function as the sixth argument.\r\n
0xc00000f5 | An invalid parameter was passed to a service or function as the seventh argument.\r\n
0xc00000f6 | An invalid parameter was passed to a service or function as the eighth argument.\r\n
0xc00000f7 | An invalid parameter was passed to a service or function as the ninth argument.\r\n
0xc00000f8 | An invalid parameter was passed to a service or function as the tenth argument.\r\n
0xc00000f9 | An invalid parameter was passed to a service or function as the eleventh argument.\r\n
0xc00000fa | An invalid parameter was passed to a service or function as the twelfth argument.\r\n
0xc00000fb | An attempt was made to access a network file, but the network software was not yet started.\r\n
0xc00000fc | An attempt was made to start the redirector, but the redirector has already been started.\r\n
0xc00000fd | A new guard page for the stack cannot be created.\r\n
0xc00000fe | A specified authentication package is unknown.\r\n
0xc00000ff | A malformed function table was encountered during an unwind operation.\r\n
0xc0000100 | Indicates the specified environment variable name was not found in the specified environment block.\r\n
0xc0000101 | Indicates that the directory trying to be deleted is not empty.\r\n
0xc0000102 | {Corrupt File}\r\nThe file or directory %hs is corrupt and unreadable.\r\nPlease run the Chkdsk utility.\r\n
0xc0000103 | A requested opened file is not a directory.\r\n
0xc0000104 | The logon session is not in a state that is consistent with the requested operation.\r\n
0xc0000105 | An internal LSA error has occurred. An authentication package has requested the creation of a Logon Session but the ID of an already existing Logon Session has been specified.\r\n
0xc0000106 | A specified name string is too long for its intended use.\r\n
0xc0000107 | The user attempted to force close the files on a redirected drive, but there were opened files on the drive, and the user did not specify a sufficient level of force.\r\n
0xc0000108 | The user attempted to force close the files on a redirected drive, but there were opened directories on the drive, and the user did not specify a sufficient level of force.\r\n
0xc0000109 | RtlFindMessage could not locate the requested message ID in the message table resource.\r\n
0xc000010a | An attempt was made to access an exiting process.\r\n
0xc000010b | Indicates an invalid value has been provided for the LogonType requested.\r\n
0xc000010c | Indicates that an attempt was made to assign protection to a file system file or directory and one of the SIDs in the security descriptor could not be translated into a GUID that could be stored by the file system.\r\nThis causes the protection attempt to fail, which may cause a file creation attempt to fail.\r\n
0xc000010d | Indicates that an attempt has been made to impersonate via a named pipe that has not yet been read from.\r\n
0xc000010e | Indicates that the specified image is already loaded.\r\n
0xc000010f | STATUS_ABIOS_NOT_PRESENT\r\n
0xc0000110 | STATUS_ABIOS_LID_NOT_EXIST\r\n
0xc0000111 | STATUS_ABIOS_LID_ALREADY_OWNED\r\n
0xc0000112 | STATUS_ABIOS_NOT_LID_OWNER\r\n
0xc0000113 | STATUS_ABIOS_INVALID_COMMAND\r\n
0xc0000114 | STATUS_ABIOS_INVALID_LID\r\n
0xc0000115 | STATUS_ABIOS_SELECTOR_NOT_AVAILABLE\r\n
0xc0000116 | STATUS_ABIOS_INVALID_SELECTOR\r\n
0xc0000117 | Indicates that an attempt was made to change the size of the LDT for a process that has no LDT.\r\n
0xc0000118 | Indicates that an attempt was made to grow an LDT by setting its size, or that the size was not an even number of selectors.\r\n
0xc0000119 | Indicates that the starting value for the LDT information was not an integral multiple of the selector size.\r\n
0xc000011a | Indicates that the user supplied an invalid descriptor when trying to set up Ldt descriptors.\r\n
0xc000011b | The specified image file did not have the correct format. It appears to be NE format.\r\n
0xc000011c | Indicates that the transaction state of a registry sub-tree is incompatible with the requested operation. For example, a request has been made to start a new transaction with one already in progress, or a request has been made to apply a transaction when one is not currently in progress.\r\n
0xc000011d | Indicates an error has occurred during a registry transaction commit. The database has been left in an unknown, but probably inconsistent, state. The state of the registry transaction is left as COMMITTING.\r\n
0xc000011e | An attempt was made to map a file of size zero with the maximum size specified as zero.\r\n
0xc000011f | Too many files are opened on a remote server.\r\nThis error should only be returned by the Windows redirector on a remote drive.\r\n
0xc0000120 | The I/O request was canceled.\r\n
0xc0000121 | An attempt has been made to remove a file or directory that cannot be deleted.\r\n
0xc0000122 | Indicates a name specified as a remote computer name is syntactically invalid.\r\n
0xc0000123 | An I/O request other than close was performed on a file after it has been deleted, which can only happen to a request which did not complete before the last handle was closed via NtClose.\r\n
0xc0000124 | Indicates an operation has been attempted on a built-in (special) SAM account which is incompatible with built-in accounts. For example, built-in accounts cannot be deleted.\r\n
0xc0000125 | The operation requested may not be performed on the specified group because it is a built-in special group.\r\n
0xc0000126 | The operation requested may not be performed on the specified user because it is a built-in special user.\r\n
0xc0000127 | Indicates a member cannot be removed from a group because the group is currently the member's primary group.\r\n
0xc0000128 | An I/O request other than close and several other special case operations was attempted using a file object that had already been closed.\r\n
0xc0000129 | Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token may only be performed when a process has zero or one threads.\r\n
0xc000012a | An attempt was made to operate on a thread within a specific process, but the thread specified is not in the process specified.\r\n
0xc000012b | An attempt was made to establish a token for use as a primary token but the token is already in use. A token can only be the primary token of one process at a time.\r\n
0xc000012c | Page file quota was exceeded.\r\n
0xc000012d | {Out of Virtual Memory}\r\nYour system is low on virtual memory. To ensure that Windows runs properly, increase the size of your virtual memory paging file. For more information, see Help.\r\n
0xc000012e | The specified image file did not have the correct format, it appears to be LE format.\r\n
0xc000012f | The specified image file did not have the correct format, it did not have an initial MZ.\r\n
0xc0000130 | The specified image file did not have the correct format, it did not have a proper e_lfarlc in the MZ header.\r\n
0xc0000131 | The specified image file did not have the correct format, it appears to be a 16-bit Windows image.\r\n
0xc0000132 | The Netlogon service cannot start because another Netlogon service running in the domain conflicts with the specified role.\r\n
0xc0000133 | The time at the Primary Domain Controller is different than the time at the Backup Domain Controller or member server by too large an amount.\r\n
0xc0000134 | The SAM database on a Windows Server is significantly out of synchronization with the copy on the Domain Controller. A complete synchronization is required.\r\n
0xc0000135 | The program can't start because %hs is missing from your computer. Try reinstalling the program to fix this problem.\r\n
0xc0000136 | The NtCreateFile API failed. This error should never be returned to an application, it is a place holder for the Windows Lan Manager Redirector to use in its internal error mapping routines.\r\n
0xc0000137 | {Privilege Failed}\r\nThe I/O permissions for the process could not be changed.\r\n
0xc0000138 | {Ordinal Not Found}\r\nThe ordinal %ld could not be located in the dynamic link library %hs.\r\n
0xc0000139 | {Entry Point Not Found}\r\nThe procedure entry point %hs could not be located in the dynamic link library %hs.\r\n
0xc000013a | {Application Exit by CTRL+C}\r\nThe application terminated as a result of a CTRL+C.\r\n
0xc000013b | {Virtual Circuit Closed}\r\nThe network transport on your computer has closed a network connection. There may or may not be I/O requests outstanding.\r\n
0xc000013c | {Virtual Circuit Closed}\r\nThe network transport on a remote computer has closed a network connection. There may or may not be I/O requests outstanding.\r\n
0xc000013d | {Insufficient Resources on Remote Computer}\r\nThe remote computer has insufficient resources to complete the network request. For instance, there may not be enough memory available on the remote computer to carry out the request at this time.\r\n
0xc000013e | {Virtual Circuit Closed}\r\nAn existing connection (virtual circuit) has been broken at the remote computer. There is probably something wrong with the network software protocol or the network hardware on the remote computer.\r\n
0xc000013f | {Virtual Circuit Closed}\r\nThe network transport on your computer has closed a network connection because it had to wait too long for a response from the remote computer.\r\n
0xc0000140 | The connection handle given to the transport was invalid.\r\n
0xc0000141 | The address handle given to the transport was invalid.\r\n
0xc0000142 | {DLL Initialization Failed}\r\nInitialization of the dynamic link library %hs failed. The process is terminating abnormally.\r\n
0xc0000143 | {Missing System File}\r\nThe required system file %hs is bad or missing.\r\n
0xc0000144 | {Application Error}\r\nThe exception %s (0x%08lx) occurred in the application at location 0x%08lx.\r\n
0xc0000145 | {Application Error}\r\nThe application was unable to start correctly (0x%lx). Click OK to close the application.\r\n
0xc0000146 | {Unable to Create Paging File}\r\nThe creation of the paging file %hs failed (%lx). The requested size was %ld.\r\n
0xc0000147 | {No Paging File Specified}\r\nNo paging file was specified in the system configuration.\r\n
0xc0000148 | {Incorrect System Call Level}\r\nAn invalid level was passed into the specified system call.\r\n
0xc0000149 | {Incorrect Password to LAN Manager Server}\r\nYou specified an incorrect password to a LAN Manager 2.x or MS-NET server.\r\n
0xc000014a | {EXCEPTION}\r\nA real-mode application issued a floating-point instruction and floating-point hardware is not present.\r\n
0xc000014b | The pipe operation has failed because the other end of the pipe has been closed.\r\n
0xc000014c | {The Registry Is Corrupt}\r\nThe structure of one of the files that contains Registry data is corrupt, or the image of the file in memory is corrupt, or the file could not be recovered because the alternate copy or log was absent or corrupt.\r\n
0xc000014d | An I/O operation initiated by the Registry failed unrecoverably. The Registry could not read in, or write out, or flush, one of the files that contain the system's image of the Registry.\r\n
0xc000014e | An event pair synchronization operation was performed using the thread specific client/server event pair object, but no event pair object was associated with the thread.\r\n
0xc000014f | The volume does not contain a recognized file system. Please make sure that all required file system drivers are loaded and that the volume is not corrupt.\r\n
0xc0000150 | No serial device was successfully initialized. The serial driver will unload.\r\n
0xc0000151 | The specified local group does not exist.\r\n
0xc0000152 | The specified account name is not a member of the group.\r\n
0xc0000153 | The specified account name is already a member of the group.\r\n
0xc0000154 | The specified local group already exists.\r\n
0xc0000155 | A requested type of logon (e.g., Interactive, Network, Service) is not granted by the target system's local security policy.\r\nPlease ask the system administrator to grant the necessary form of logon.\r\n
0xc0000156 | The maximum number of secrets that may be stored in a single system has been exceeded. The length and number of secrets is limited to satisfy United States State Department export restrictions.\r\n
0xc0000157 | The length of a secret exceeds the maximum length allowed. The length and number of secrets is limited to satisfy United States State Department export restrictions.\r\n
0xc0000158 | The Local Security Authority (LSA) database contains an internal inconsistency.\r\n
0xc0000159 | The requested operation cannot be performed in fullscreen mode.\r\n
0xc000015a | During a logon attempt, the user's security context accumulated too many security IDs. This is a very unusual situation. Remove the user from some global or local groups to reduce the number of security ids to incorporate into the security context.\r\n
0xc000015b | A user has requested a type of logon (e.g., interactive or network) that has not been granted. An administrator has control over who may logon interactively and through the network.\r\n
0xc000015c | The system has attempted to load or restore a file into the registry, and the specified file is not in the format of a registry file.\r\n
0xc000015d | An attempt was made to change a user password in the security account manager without providing the necessary Windows cross-encrypted password.\r\n
0xc000015e | A Windows Server has an incorrect configuration.\r\n
0xc000015f | An attempt was made to explicitly access the secondary copy of information via a device control to the Fault Tolerance driver and the secondary copy is not present in the system.\r\n
0xc0000160 | A configuration registry node representing a driver service entry was ill-formed and did not contain required value entries.\r\n
0xc0000161 | An illegal character was encountered. For a multi-byte character set this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE.\r\n
0xc0000162 | No mapping for the Unicode character exists in the target multi-byte code page.\r\n
0xc0000163 | The Unicode character is not defined in the Unicode character set installed on the system.\r\n
0xc0000164 | The paging file cannot be created on a floppy diskette.\r\n
0xc0000165 | {Floppy Disk Error}\r\nWhile accessing a floppy disk, an ID address mark was not found.\r\n
0xc0000166 | {Floppy Disk Error}\r\nWhile accessing a floppy disk, the track address from the sector ID field was found to be different than the track address maintained by the controller.\r\n
0xc0000167 | {Floppy Disk Error}\r\nThe floppy disk controller reported an error that is not recognized by the floppy disk driver.\r\n
0xc0000168 | {Floppy Disk Error}\r\nWhile accessing a floppy-disk, the controller returned inconsistent results via its registers.\r\n
0xc0000169 | {Hard Disk Error}\r\nWhile accessing the hard disk, a recalibrate operation failed, even after retries.\r\n
0xc000016a | {Hard Disk Error}\r\nWhile accessing the hard disk, a disk operation failed even after retries.\r\n
0xc000016b | {Hard Disk Error}\r\nWhile accessing the hard disk, a disk controller reset was needed, but even that failed.\r\n
0xc000016c | An attempt was made to open a device that was sharing an IRQ with other devices.\r\nAt least one other device that uses that IRQ was already opened.\r\nTwo concurrent opens of devices that share an IRQ and only work via interrupts is not supported for the particular bus type that the devices use.\r\n
0xc000016d | {FT Orphaning}\r\nA disk that is part of a fault-tolerant volume can no longer be accessed.\r\n
0xc000016e | The system bios failed to connect a system interrupt to the device or bus for which the device is connected.\r\n
0xc0000172 | Tape could not be partitioned.\r\n
0xc0000173 | When accessing a new tape of a multivolume partition, the current blocksize is incorrect.\r\n
0xc0000174 | Tape partition information could not be found when loading a tape.\r\n
0xc0000175 | Attempt to lock the eject media mechanism fails.\r\n
0xc0000176 | Unload media fails.\r\n
0xc0000177 | Physical end of tape was detected.\r\n
0xc0000178 | {No Media}\r\nThere is no media in the drive. Please insert media into drive %hs.\r\n
0xc000017a | A member could not be added to or removed from the local group because the member does not exist.\r\n
0xc000017b | A new member could not be added to a local group because the member has the wrong account type.\r\n
0xc000017c | Illegal operation attempted on a registry key which has been marked for deletion.\r\n
0xc000017d | System could not allocate required space in a registry log.\r\n
0xc000017e | Too many Sids have been specified.\r\n
0xc000017f | An attempt was made to change a user password in the security account manager without providing the necessary LM cross-encrypted password.\r\n
0xc0000180 | An attempt was made to create a symbolic link in a registry key that already has subkeys or values.\r\n
0xc0000181 | An attempt was made to create a Stable subkey under a Volatile parent key.\r\n
0xc0000182 | The I/O device is configured incorrectly or the configuration parameters to the driver are incorrect.\r\n
0xc0000183 | An error was detected between two drivers or within an I/O driver.\r\n
0xc0000184 | The device is not in a valid state to perform this request.\r\n
0xc0000185 | The I/O device reported an I/O error.\r\n
0xc0000186 | A protocol error was detected between the driver and the device.\r\n
0xc0000187 | This operation is only allowed for the Primary Domain Controller of the domain.\r\n
0xc0000188 | Log file space is insufficient to support this operation.\r\n
0xc0000189 | A write operation was attempted to a volume after it was dismounted.\r\n
0xc000018a | The workstation does not have a trust secret for the primary domain in the local LSA database.\r\n
0xc000018b | The SAM database on the Windows Server does not have a computer account for this workstation trust relationship.\r\n
0xc000018c | The logon request failed because the trust relationship between the primary domain and the trusted domain failed.\r\n
0xc000018d | The logon request failed because the trust relationship between this workstation and the primary domain failed.\r\n
0xc000018e | The Eventlog log file is corrupt.\r\n
0xc000018f | No Eventlog log file could be opened. The Eventlog service did not start.\r\n
0xc0000190 | The network logon failed. This may be because the validation authority can't be reached.\r\n
0xc0000191 | An attempt was made to acquire a mutant such that its maximum count would have been exceeded.\r\n
0xc0000192 | An attempt was made to logon, but the netlogon service was not started.\r\n
0xc0000193 | The user's account has expired.\r\n
0xc0000194 | {EXCEPTION}\r\nPossible deadlock condition.\r\n
0xc0000195 | Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.\r\n
0xc0000196 | An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.\r\n
0xc0000197 | The log file has changed between reads.\r\n
0xc0000198 | The account used is an Interdomain Trust account. Use your global user account or local user account to access this server.\r\n
0xc0000199 | The account used is a Computer Account. Use your global user account or local user account to access this server.\r\n
0xc000019a | The account used is an Server Trust account. Use your global user account or local user account to access this server.\r\n
0xc000019b | The name or SID of the domain specified is inconsistent with the trust information for that domain.\r\n
0xc000019c | A volume has been accessed for which a file system driver is required that has not yet been loaded.\r\n
0xc000019d | Indicates that the specified image is already loaded as a DLL.\r\n
0xc000019e | Short name settings may not be changed on this volume due to the global registry setting.\r\n
0xc000019f | Short names are not enabled on this volume.\r\n
0xc00001a0 | The security stream for the given volume is in an inconsistent state.\r\nPlease run CHKDSK on the volume.\r\n
0xc00001a1 | A requested file lock operation cannot be processed due to an invalid byte range.\r\n
0xc00001a2 | {Invalid ACE Condition}\r\nThe specified access control entry (ACE) contains an invalid condition.\r\n
0xc00001a3 | The subsystem needed to support the image type is not present.\r\n
0xc00001a4 | {Invalid ACE Condition}\r\nThe specified file already has a notification GUID associated with it.\r\n
0xc0000201 | A remote open failed because the network open restrictions were not satisfied.\r\n
0xc0000202 | There is no user session key for the specified logon session.\r\n
0xc0000203 | The remote user session has been deleted.\r\n
0xc0000204 | Indicates the specified resource language ID cannot be found in the\r\nimage file.\r\n
0xc0000205 | Insufficient server resources exist to complete the request.\r\n
0xc0000206 | The size of the buffer is invalid for the specified operation.\r\n
0xc0000207 | The transport rejected the network address specified as invalid.\r\n
0xc0000208 | The transport rejected the network address specified due to an invalid use of a wildcard.\r\n
0xc0000209 | The transport address could not be opened because all the available addresses are in use.\r\n
0xc000020a | The transport address could not be opened because it already exists.\r\n
0xc000020b | The transport address is now closed.\r\n
0xc000020c | The transport connection is now disconnected.\r\n
0xc000020d | The transport connection has been reset.\r\n
0xc000020e | The transport cannot dynamically acquire any more nodes.\r\n
0xc000020f | The transport aborted a pending transaction.\r\n
0xc0000210 | The transport timed out a request waiting for a response.\r\n
0xc0000211 | The transport did not receive a release for a pending response.\r\n
0xc0000212 | The transport did not find a transaction matching the specific token.\r\n
0xc0000213 | The transport had previously responded to a transaction request.\r\n
0xc0000214 | The transport does not recognized the transaction request identifier specified.\r\n
0xc0000215 | The transport does not recognize the transaction request type specified.\r\n
0xc0000216 | The transport can only process the specified request on the server side of a session.\r\n
0xc0000217 | The transport can only process the specified request on the client side of a session.\r\n
0xc0000218 | {Registry File Failure}\r\nThe registry cannot load the hive (file):\r\n%hs\r\nor its log or alternate.\r\nIt is corrupt, absent, or not writable.\r\n
0xc0000219 | {Unexpected Failure in DebugActiveProcess}\r\nAn unexpected failure occurred while processing a DebugActiveProcess API request. You may choose OK to terminate the process, or Cancel to ignore the error.\r\n
0xc000021a | {Fatal System Error}\r\nThe %hs system process terminated unexpectedly with a status of 0x%08x (0x%08x 0x%08x).\r\nThe system has been shut down.\r\n
0xc000021b | {Data Not Accepted}\r\nThe TDI client could not handle the data received during an indication.\r\n
0xc000021c | {Unable to Retrieve Browser Server List}\r\nThe list of servers for this workgroup is not currently available.\r\n
0xc000021d | NTVDM encountered a hard error.\r\n
0xc000021e | {Cancel Timeout}\r\nThe driver %hs failed to complete a cancelled I/O request in the allotted time.\r\n
0xc000021f | {Reply Message Mismatch}\r\nAn attempt was made to reply to an LPC message, but the thread specified by the client ID in the message was not waiting on that message.\r\n
0xc0000220 | {Mapped View Alignment Incorrect}\r\nAn attempt was made to map a view of a file, but either the specified base address or the offset into the file were not aligned on the proper allocation granularity.\r\n
0xc0000221 | {Bad Image Checksum}\r\nThe image %hs is possibly corrupt. The header checksum does not match the computed checksum.\r\n
0xc0000222 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs. The data has been lost. This error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.\r\n
0xc0000223 | The parameter(s) passed to the server in the client/server shared memory window were invalid. Too much data may have been put in the shared memory window.\r\n
0xc0000224 | The user's password must be changed before logging on the first time.\r\n
0xc0000225 | The object was not found.\r\n
0xc0000226 | The stream is not a tiny stream.\r\n
0xc0000227 | A transaction recover failed.\r\n
0xc0000228 | The request must be handled by the stack overflow code.\r\n
0xc0000229 | A consistency check failed.\r\n
0xc000022a | The attempt to insert the ID in the index failed because the ID is already in the index.\r\n
0xc000022b | The attempt to set the object's ID failed because the object already has an ID.\r\n
0xc000022c | Internal OFS status codes indicating how an allocation operation is handled. Either it is retried after the containing onode is moved or the extent stream is converted to a large stream.\r\n
0xc000022d | The request needs to be retried.\r\n
0xc000022e | The attempt to find the object found an object matching by ID on the volume but it is out of the scope of the handle used for the operation.\r\n
0xc000022f | The bucket array must be grown. Retry transaction after doing so.\r\n
0xc0000230 | The property set specified does not exist on the object.\r\n
0xc0000231 | The user/kernel marshalling buffer has overflowed.\r\n
0xc0000232 | The supplied variant structure contains invalid data.\r\n
0xc0000233 | Could not find a domain controller for this domain.\r\n
0xc0000234 | The user account has been automatically locked because too many invalid logon attempts or password change attempts have been requested.\r\n
0xc0000235 | NtClose was called on a handle that was protected from close via NtSetInformationObject.\r\n
0xc0000236 | The transport connection attempt was refused by the remote system.\r\n
0xc0000237 | The transport connection was gracefully closed.\r\n
0xc0000238 | The transport endpoint already has an address associated with it.\r\n
0xc0000239 | An address has not yet been associated with the transport endpoint.\r\n
0xc000023a | An operation was attempted on a nonexistent transport connection.\r\n
0xc000023b | An invalid operation was attempted on an active transport connection.\r\n
0xc000023c | The remote network is not reachable by the transport.\r\n
0xc000023d | The remote system is not reachable by the transport.\r\n
0xc000023e | The remote system does not support the transport protocol.\r\n
0xc000023f | No service is operating at the destination port of the transport on the remote system.\r\n
0xc0000240 | The request was aborted.\r\n
0xc0000241 | The transport connection was aborted by the local system.\r\n
0xc0000242 | The specified buffer contains ill-formed data.\r\n
0xc0000243 | The requested operation cannot be performed on a file with a user mapped section open.\r\n
0xc0000244 | {Audit Failed}\r\nAn attempt to generate a security audit failed.\r\n
0xc0000245 | The timer resolution was not previously set by the current process.\r\n
0xc0000246 | A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.\r\n
0xc0000247 | Attempting to login during an unauthorized time of day for this account.\r\n
0xc0000248 | The account is not authorized to login from this station.\r\n
0xc0000249 | {UP/MP Image Mismatch}\r\nThe image %hs has been modified for use on a uniprocessor system, but you are running it on a multiprocessor machine.\r\nPlease reinstall the image file.\r\n
0xc0000250 | There is insufficient account information to log you on.\r\n
0xc0000251 | {Invalid DLL Entrypoint}\r\nThe dynamic link library %hs is not written correctly. The stack pointer has been left in an inconsistent state. The entrypoint should be declared as WINAPI or STDCALL. Select YES to fail the DLL load. Select NO to continue execution. Selecting NO may cause the application to operate incorrectly.\r\n
0xc0000252 | {Invalid Service Callback Entrypoint}\r\nThe %hs service is not written correctly. The stack pointer has been left in an inconsistent state. The callback entrypoint should be declared as WINAPI or STDCALL. Selecting OK will cause the service to continue operation. However, the service process may operate incorrectly.\r\n
0xc0000253 | The server received the messages but did not send a reply.\r\n
0xc0000254 | There is an IP address conflict with another system on the network\r\n
0xc0000255 | There is an IP address conflict with another system on the network\r\n
0xc0000256 | {Low On Registry Space}\r\nThe system has reached the maximum size allowed for the system part of the registry. Additional storage requests will be ignored.\r\n
0xc0000257 | The contacted server does not support the indicated part of the DFS namespace.\r\n
0xc0000258 | A callback return system service cannot be executed when no callback is active.\r\n
0xc0000259 | The service being accessed is licensed for a particular number of connections. No more connections can be made to the service at this time because there are already as many connections as the service can accept.\r\n
0xc000025a | The password provided is too short to meet the policy of your user account. Please choose a longer password.\r\n
0xc000025b | The policy of your user account does not allow you to change passwords too frequently. This is done to prevent users from changing back to a familiar, but potentially discovered, password. If you feel your password has been compromised then please contact your administrator immediately to have a new one assigned.\r\n
0xc000025c | You have attempted to change your password to one that you have used in the past. The policy of your user account does not allow this. Please select a password that you have not previously used.\r\n
0xc000025e | You have attempted to load a legacy device driver while its device instance had been disabled.\r\n
0xc000025f | The specified compression format is unsupported.\r\n
0xc0000260 | The specified hardware profile configuration is invalid.\r\n
0xc0000261 | The specified Plug and Play registry device path is invalid.\r\n
0xc0000262 | {Driver Entry Point Not Found}\r\nThe %hs device driver could not locate the ordinal %ld in driver %hs.\r\n
0xc0000263 | {Driver Entry Point Not Found}\r\nThe %hs device driver could not locate the entry point %hs in driver %hs.\r\n
0xc0000264 | {Application Error}\r\nThe application attempted to release a resource it did not own. Click OK to terminate the application.\r\n
0xc0000265 | An attempt was made to create more links on a file than the file system supports.\r\n
0xc0000266 | The specified quota list is internally inconsistent with its descriptor.\r\n
0xc0000267 | The specified file has been relocated to offline storage.\r\n
0xc0000268 | {Windows Evaluation Notification}\r\nThe evaluation period for this installation of Windows has expired. This system will shutdown in 1 hour. To restore access to this installation of Windows, please upgrade this installation using a licensed distribution of this product.\r\n
0xc0000269 | {Illegal System DLL Relocation}\r\nThe system DLL %hs was relocated in memory. The application will not run properly. The relocation occurred because the DLL %hs occupied an address range reserved for Windows system DLLs. The vendor supplying the DLL should be contacted for a new DLL.\r\n
0xc000026a | {License Violation}\r\nThe system has detected tampering with your registered product type. This is a violation of your software license. Tampering with product type is not permitted.\r\n
0xc000026b | {DLL Initialization Failed}\r\nThe application failed to initialize because the window station is shutting down.\r\n
0xc000026c | {Unable to Load Device Driver}\r\n%hs device driver could not be loaded.\r\nError Status was 0x%x\r\n
0xc000026d | DFS is unavailable on the contacted server.\r\n
0xc000026e | An operation was attempted to a volume after it was dismounted.\r\n
0xc000026f | An internal error occurred in the Win32 x86 emulation subsystem.\r\n
0xc0000270 | Win32 x86 emulation subsystem Floating-point stack check.\r\n
0xc0000271 | The validation process needs to continue on to the next step.\r\n
0xc0000272 | There was no match for the specified key in the index.\r\n
0xc0000273 | There are no more matches for the current index enumeration.\r\n
0xc0000275 | The NTFS file or directory is not a reparse point.\r\n
0xc0000276 | The Windows I/O reparse tag passed for the NTFS reparse point is invalid.\r\n
0xc0000277 | The Windows I/O reparse tag does not match the one present in the NTFS reparse point.\r\n
0xc0000278 | The user data passed for the NTFS reparse point is invalid.\r\n
0xc0000279 | The layered file system driver for this IO tag did not handle it when needed.\r\n
0xc0000280 | The NTFS symbolic link could not be resolved even though the initial file name is valid.\r\n
0xc0000281 | The NTFS directory is a reparse point.\r\n
0xc0000282 | The range could not be added to the range list because of a conflict.\r\n
0xc0000283 | The specified medium changer source element contains no media.\r\n
0xc0000284 | The specified medium changer destination element already contains media.\r\n
0xc0000285 | The specified medium changer element does not exist.\r\n
0xc0000286 | The specified element is contained within a magazine that is no longer present.\r\n
0xc0000287 | The device requires reinitialization due to hardware errors.\r\n
0xc000028a | The file encryption attempt failed.\r\n
0xc000028b | The file decryption attempt failed.\r\n
0xc000028c | The specified range could not be found in the range list.\r\n
0xc000028d | There is no encryption recovery policy configured for this system.\r\n
0xc000028e | The required encryption driver is not loaded for this system.\r\n
0xc000028f | The file was encrypted with a different encryption driver than is currently loaded.\r\n
0xc0000290 | There are no EFS keys defined for the user.\r\n
0xc0000291 | The specified file is not encrypted.\r\n
0xc0000292 | The specified file is not in the defined EFS export format.\r\n
0xc0000293 | The specified file is encrypted and the user does not have the ability to decrypt it.\r\n
0xc0000295 | The guid passed was not recognized as valid by a WMI data provider.\r\n
0xc0000296 | The instance name passed was not recognized as valid by a WMI data provider.\r\n
0xc0000297 | The data item id passed was not recognized as valid by a WMI data provider.\r\n
0xc0000298 | The WMI request could not be completed and should be retried.\r\n
0xc0000299 | The policy object is shared and can only be modified at the root\r\n
0xc000029a | The policy object does not exist when it should\r\n
0xc000029b | The requested policy information only lives in the Ds\r\n
0xc000029c | The volume must be upgraded to enable this feature\r\n
0xc000029d | The remote storage service is not operational at this time.\r\n
0xc000029e | The remote storage service encountered a media error.\r\n
0xc000029f | The tracking (workstation) service is not running.\r\n
0xc00002a0 | The server process is running under a SID different than that required by client.\r\n
0xc00002a1 | The specified directory service attribute or value does not exist.\r\n
0xc00002a2 | The attribute syntax specified to the directory service is invalid.\r\n
0xc00002a3 | The attribute type specified to the directory service is not defined.\r\n
0xc00002a4 | The specified directory service attribute or value already exists.\r\n
0xc00002a5 | The directory service is busy.\r\n
0xc00002a6 | The directory service is not available.\r\n
0xc00002a7 | The directory service was unable to allocate a relative identifier.\r\n
0xc00002a8 | The directory service has exhausted the pool of relative identifiers.\r\n
0xc00002a9 | The requested operation could not be performed because the directory service is not the master for that type of operation.\r\n
0xc00002aa | The directory service was unable to initialize the subsystem that allocates relative identifiers.\r\n
0xc00002ab | The requested operation did not satisfy one or more constraints associated with the class of the object.\r\n
0xc00002ac | The directory service can perform the requested operation only on a leaf object.\r\n
0xc00002ad | The directory service cannot perform the requested operation on the Relatively Defined Name (RDN) attribute of an object.\r\n
0xc00002ae | The directory service detected an attempt to modify the object class of an object.\r\n
0xc00002af | An error occurred while performing a cross domain move operation.\r\n
0xc00002b0 | Unable to Contact the Global Catalog Server.\r\n
0xc00002b1 | The requested operation requires a directory service, and none was available.\r\n
0xc00002b2 | The reparse attribute cannot be set as it is incompatible with an existing attribute.\r\n
0xc00002b3 | A group marked use for deny only cannot be enabled.\r\n
0xc00002b4 | {EXCEPTION}\r\nMultiple floating point faults.\r\n
0xc00002b5 | {EXCEPTION}\r\nMultiple floating point traps.\r\n
0xc00002b6 | The device has been removed.\r\n
0xc00002b7 | The volume change journal is being deleted.\r\n
0xc00002b8 | The volume change journal is not active.\r\n
0xc00002b9 | The requested interface is not supported.\r\n
0xc00002c1 | A directory service resource limit has been exceeded.\r\n
0xc00002c2 | {System Standby Failed}\r\nThe driver %hs does not support standby mode. Updating this driver may allow the system to go to standby mode.\r\n
0xc00002c3 | Mutual Authentication failed. The server's password is out of date at the domain controller.\r\n
0xc00002c4 | The system file %1 has become corrupt and has been replaced.\r\n
0xc00002c5 | {EXCEPTION}\r\nAlignment Error\r\nA datatype misalignment error was detected in a load or store instruction.\r\n
0xc00002c6 | The WMI data item or data block is read only.\r\n
0xc00002c7 | The WMI data item or data block could not be changed.\r\n
0xc00002c8 | {Virtual Memory Minimum Too Low}\r\nYour system is low on virtual memory. Windows is increasing the size of your virtual memory paging file. During this process, memory requests for some applications may be denied. For more information, see Help.\r\n
0xc00002c9 | {EXCEPTION}\r\nRegister NaT consumption faults.\r\nA NaT value is consumed on a non speculative instruction.\r\n
0xc00002ca | The medium changer's transport element contains media, which is causing the operation to fail.\r\n
0xc00002cb | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.\r\n
0xc00002cc | This operation is supported only when you are connected to the server.\r\n
0xc00002cd | Only an administrator can modify the membership list of an administrative group.\r\n
0xc00002ce | A device was removed so enumeration must be restarted.\r\n
0xc00002cf | The journal entry has been deleted from the journal.\r\n
0xc00002d0 | Cannot change the primary group ID of a domain controller account.\r\n
0xc00002d1 | {Fatal System Error}\r\nThe system image %s is not properly signed. The file has been replaced with the signed file. The system has been shut down.\r\n
0xc00002d2 | Device will not start without a reboot.\r\n
0xc00002d3 | Current device power state cannot support this request.\r\n
0xc00002d4 | The specified group type is invalid.\r\n
0xc00002d5 | In mixed domain no nesting of global group if group is security enabled.\r\n
0xc00002d6 | In mixed domain, cannot nest local groups with other local groups, if the group is security enabled.\r\n
0xc00002d7 | A global group cannot have a local group as a member.\r\n
0xc00002d8 | A global group cannot have a universal group as a member.\r\n
0xc00002d9 | A universal group cannot have a local group as a member.\r\n
0xc00002da | A global group cannot have a cross domain member.\r\n
0xc00002db | A local group cannot have another cross domain local group as a member.\r\n
0xc00002dc | Cannot change to security disabled group because of having primary members in this group.\r\n
0xc00002dd | The WMI operation is not supported by the data block or method.\r\n
0xc00002de | There is not enough power to complete the requested operation.\r\n
0xc00002df | Security Account Manager needs to get the boot password.\r\n
0xc00002e0 | Security Account Manager needs to get the boot key from floppy disk.\r\n
0xc00002e1 | Directory Service cannot start.\r\n
0xc00002e2 | Directory Services could not start because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.\r\n
0xc00002e3 | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown this system and reboot into Safe Mode, check the event log for more detailed information.\r\n
0xc00002e4 | The requested operation can be performed only on a global catalog server.\r\n
0xc00002e5 | A local group can only be a member of other local groups in the same domain.\r\n
0xc00002e6 | Foreign security principals cannot be members of universal groups.\r\n
0xc00002e7 | Your computer could not be joined to the domain. You have exceeded the maximum number of computer accounts you are allowed to create in this domain. Contact your system administrator to have this limit reset or increased.\r\n
0xc00002e8 | STATUS_MULTIPLE_FAULT_VIOLATION\r\n
0xc00002e9 | This operation cannot be performed on the current domain.\r\n
0xc00002ea | The directory or file cannot be created.\r\n
0xc00002eb | The system is in the process of shutting down.\r\n
0xc00002ec | Directory Services could not start because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown the system. You can use the recovery console to diagnose the system further.\r\n
0xc00002ed | Security Accounts Manager initialization failed because of the following error:\r\n%hs\r\nError Status: 0x%x.\r\nPlease click OK to shutdown the system. You can use the recovery console to diagnose the system further.\r\n
0xc00002ee | A security context was deleted before the context was completed. This is considered a logon failure.\r\n
0xc00002ef | The client is trying to negotiate a context and the server requires user-to-user but didn't send a TGT reply.\r\n
0xc00002f0 | An object ID was not found in the file.\r\n
0xc00002f1 | Unable to accomplish the requested task because the local machine does not have any IP addresses.\r\n
0xc00002f2 | The supplied credential handle does not match the credential associated with the security context.\r\n
0xc00002f3 | The crypto system or checksum function is invalid because a required function is unavailable.\r\n
0xc00002f4 | The number of maximum ticket referrals has been exceeded.\r\n
0xc00002f5 | The local machine must be a Kerberos KDC (domain controller) and it is not.\r\n
0xc00002f6 | The other end of the security negotiation is requires strong crypto but it is not supported on the local machine.\r\n
0xc00002f7 | The KDC reply contained more than one principal name.\r\n
0xc00002f8 | Expected to find PA data for a hint of what etype to use, but it was not found.\r\n
0xc00002f9 | The client certificate does not contain a valid UPN, or does not match the client name in the logon request. Please contact your administrator.\r\n
0xc00002fa | Smartcard logon is required and was not used.\r\n
0xc00002fb | An invalid request was sent to the KDC.\r\n
0xc00002fc | The KDC was unable to generate a referral for the service requested.\r\n
0xc00002fd | The encryption type requested is not supported by the KDC.\r\n
0xc00002fe | A system shutdown is in progress.\r\n
0xc00002ff | The server machine is shutting down.\r\n
0xc0000300 | This operation is not supported on a computer running Windows Server 2003 for Small Business Server\r\n
0xc0000301 | The WMI GUID is no longer available\r\n
0xc0000302 | Collection or events for the WMI GUID is already disabled.\r\n
0xc0000303 | Collection or events for the WMI GUID is already enabled.\r\n
0xc0000304 | The Master File Table on the volume is too fragmented to complete this operation.\r\n
0xc0000305 | Copy protection failure.\r\n
0xc0000306 | Copy protection error - DVD CSS Authentication failed.\r\n
0xc0000307 | Copy protection error - The given sector does not contain a valid key.\r\n
0xc0000308 | Copy protection error - DVD session key not established.\r\n
0xc0000309 | Copy protection error - The read failed because the sector is encrypted.\r\n
0xc000030a | Copy protection error - The given DVD's region does not correspond to the\r\nregion setting of the drive.\r\n
0xc000030b | Copy protection error - The drive's region setting may be permanent.\r\n
0xc0000320 | The Kerberos protocol encountered an error while validating the KDC certificate during smartcard Logon. There is more information in the system event log.\r\n
0xc0000321 | The Kerberos protocol encountered an error while attempting to utilize the smartcard subsystem.\r\n
0xc0000322 | The target server does not have acceptable Kerberos credentials.\r\n
0xc0000350 | The transport determined that the remote system is down.\r\n
0xc0000351 | An unsupported preauthentication mechanism was presented to the Kerberos package.\r\n
0xc0000352 | The encryption algorithm used on the source file needs a bigger key buffer than the one used on the destination file.\r\n
0xc0000353 | An attempt to remove a process's DebugPort was made, but a port was not already associated with the process.\r\n
0xc0000354 | Debugger Inactive: Windows may have been started without kernel debugging enabled.\r\n
0xc0000355 | This version of Windows is not compatible with the behavior version of directory forest, domain or domain controller.\r\n
0xc0000356 | The specified event is currently not being audited.\r\n
0xc0000357 | The machine account was created pre-NT4. The account needs to be recreated.\r\n
0xc0000358 | A account group cannot have a universal group as a member.\r\n
0xc0000359 | The specified image file did not have the correct format, it appears to be a 32-bit Windows image.\r\n
0xc000035a | The specified image file did not have the correct format, it appears to be a 64-bit Windows image.\r\n
0xc000035b | Client's supplied SSPI channel bindings were incorrect.\r\n
0xc000035c | The client's session has expired, so the client must reauthenticate to continue accessing the remote resources.\r\n
0xc000035d | AppHelp dialog canceled thus preventing the application from starting.\r\n
0xc000035e | The SID filtering operation removed all SIDs.\r\n
0xc000035f | The driver was not loaded because the system is booting into safe mode.\r\n
0xc0000361 | Access to %1 has been restricted by your Administrator by the default software restriction policy level.\r\n
0xc0000362 | Access to %1 has been restricted by your Administrator by location with policy rule %2 placed on path %3\r\n
0xc0000363 | Access to %1 has been restricted by your Administrator by software publisher policy.\r\n
0xc0000364 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0xc0000365 | The driver was not loaded because it failed it's initialization call.\r\n
0xc0000366 | The "%hs" encountered an error while applying power or reading the device configuration. This may be caused by a failure of your hardware or by a poor connection.\r\n
0xc0000368 | The create operation failed because the name contained at least one mount point which resolves to a volume to which the specified device object is not attached.\r\n
0xc0000369 | The device object parameter is either not a valid device object or is not attached to the volume specified by the file name.\r\n
0xc000036a | A Machine Check Error has occurred. Please check the system eventlog for additional information.\r\n
0xc000036b | Driver %2 has been blocked from loading.\r\n
0xc000036c | Driver %2 has been blocked from loading.\r\n
0xc000036d | There was error [%2] processing the driver database.\r\n
0xc000036e | System hive size has exceeded its limit.\r\n
0xc000036f | A dynamic link library (DLL) referenced a module that was neither a DLL nor the process's executable image.\r\n
0xc0000371 | The local account store does not contain secret material for the specified account.\r\n
0xc0000372 | Access to %1 has been restricted by your Administrator by policy rule %2.\r\n
0xc0000373 | The system was not able to allocate enough memory to perform a stack switch.\r\n
0xc0000374 | A heap has been corrupted.\r\n
0xc0000380 | An incorrect PIN was presented to the smart card\r\n
0xc0000381 | The smart card is blocked\r\n
0xc0000382 | No PIN was presented to the smart card\r\n
0xc0000383 | No smart card available\r\n
0xc0000384 | The requested key container does not exist on the smart card\r\n
0xc0000385 | The requested certificate does not exist on the smart card\r\n
0xc0000386 | The requested keyset does not exist\r\n
0xc0000387 | A communication error with the smart card has been detected.\r\n
0xc0000388 | The system detected a possible attempt to compromise security. Please ensure that you can contact the server that authenticated you.\r\n
0xc0000389 | The smartcard certificate used for authentication has been revoked. Please contact your system administrator. There may be additional information in the event log.\r\n
0xc000038a | An untrusted certificate authority was detected While processing the smartcard certificate used for authentication. Please contact your system administrator.\r\n
0xc000038b | The revocation status of the smartcard certificate used for authentication could not be determined. Please contact your system administrator.\r\n
0xc000038c | The smartcard certificate used for authentication was not trusted. Please contact your system administrator.\r\n
0xc000038d | The smartcard certificate used for authentication has expired. Please\r\ncontact your system administrator.\r\n
0xc000038e | The driver could not be loaded because a previous version of the driver is still in memory.\r\n
0xc000038f | The smartcard provider could not perform the action since the context was acquired as silent.\r\n
0xc0000401 | The current user's delegated trust creation quota has been exceeded.\r\n
0xc0000402 | The total delegated trust creation quota has been exceeded.\r\n
0xc0000403 | The current user's delegated trust deletion quota has been exceeded.\r\n
0xc0000404 | The requested name already exists as a unique identifier.\r\n
0xc0000405 | The requested object has a non-unique identifier and cannot be retrieved.\r\n
0xc0000406 | The group cannot be converted due to attribute restrictions on the requested group type.\r\n
0xc0000407 | {Volume Shadow Copy Service}\r\nPlease wait while the Volume Shadow Copy Service prepares volume %hs for hibernation.\r\n
0xc0000408 | Kerberos sub-protocol User2User is required.\r\n
0xc0000409 | The system detected an overrun of a stack-based buffer in this application. This overrun could potentially allow a malicious user to gain control of this application.\r\n
0xc000040a | The Kerberos subsystem encountered an error. A service for user protocol request was made against a domain controller which does not support service for user.\r\n
0xc000040b | An attempt was made by this server to make a Kerberos constrained delegation request for a target outside of the server's realm. This is not supported, and indicates a misconfiguration on this server's allowed to delegate to list. Please contact your administrator.\r\n
0xc000040c | The revocation status of the domain controller certificate used for smartcard authentication could not be determined. There is additional information in the system event log. Please contact your system administrator.\r\n
0xc000040d | An untrusted certificate authority was detected while processing the domain controller certificate used for authentication. There is additional information in the system event log. Please contact your system administrator.\r\n
0xc000040e | The domain controller certificate used for smartcard logon has expired. Please contact your system administrator with the contents of your system event log.\r\n
0xc000040f | The domain controller certificate used for smartcard logon has been revoked. Please contact your system administrator with the contents of your system event log.\r\n
0xc0000410 | Data present in one of the parameters is more than the function can operate on.\r\n
0xc0000411 | The system has failed to hibernate (The error code is %hs). Hibernation will be disabled until the system is restarted.\r\n
0xc0000412 | An attempt to delay-load a .dll or get a function address in a delay-loaded .dll failed.\r\n
0xc0000413 | Logon Failure: The machine you are logging onto is protected by an authentication firewall. The specified account is not allowed to authenticate to the machine.\r\n
0xc0000414 | %hs is a 16-bit application. You do not have permissions to execute 16-bit applications. Check your permissions with your system administrator.\r\n
0xc0000415 | {Display Driver Stopped Responding}\r\nThe %hs display driver has stopped working normally. Save your work and reboot the system to restore full display functionality. The next time you reboot the machine a dialog will be displayed giving you a chance to report this failure to Microsoft.\r\n
0xc0000416 | The Desktop heap encountered an error while allocating session memory. There is more information in the system event log.\r\n
0xc0000417 | An invalid parameter was passed to a C runtime function.\r\n
0xc0000418 | The authentication failed since NTLM was blocked.\r\n
0xc0000419 | The source object's SID already exists in destination forest.\r\n
0xc000041a | The domain name of the trusted domain already exists in the forest.\r\n
0xc000041b | The flat name of the trusted domain already exists in the forest.\r\n
0xc000041c | The User Principal Name (UPN) is invalid.\r\n
0xc000041d | An unhandled exception was encountered during a user callback.\r\n
0xc0000420 | An assertion failure has occurred.\r\n
0xc0000421 | Application verifier has found an error in the current process.\r\n
0xc0000423 | An exception has occurred in a user mode callback and the kernel callback frame should be removed.\r\n
0xc0000424 | %2 has been blocked from loading due to incompatibility with this system. Please contact your software vendor for a compatible version of the driver.\r\n
0xc0000425 | Illegal operation attempted on a registry key which has already been unloaded.\r\n
0xc0000426 | Compression is disabled for this volume.\r\n
0xc0000427 | The requested operation could not be completed due to a file system limitation\r\n
0xc0000428 | Windows cannot verify the digital signature for this file. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source.\r\n
0xc0000429 | The implementation is not capable of performing the request.\r\n
0xc000042a | The requested operation is out of order with respect to other operations.\r\n
0xc000042b | An operation attempted to exceed an implementation-defined limit.\r\n
0xc000042c | The requested operation requires elevation.\r\n
0xc000042d | The required security context does not exist.\r\n
0xc000042f | The PKU2U protocol encountered an error while attempting to utilize the associated certificates.\r\n
0xc0000432 | The operation was attempted beyond the valid data length of the file.\r\n
0xc0000433 | The attempted write operation encountered a write already in progress for some portion of the range.\r\n
0xc0000434 | The page fault mappings changed in the middle of processing a fault so the operation must be retried.\r\n
0xc0000435 | The attempt to purge this file from memory failed to purge some or all the data from memory.\r\n
0xc0000440 | The requested credential requires confirmation.\r\n
0xc0000441 | The remote server sent an invalid response for a file being opened with Client Side Encryption.\r\n
0xc0000442 | Client Side Encryption is not supported by the remote server even though it claims to support it.\r\n
0xc0000443 | File is encrypted and should be opened in Client Side Encryption mode.\r\n
0xc0000444 | A new encrypted file is being created and a $EFS needs to be provided.\r\n
0xc0000445 | The SMB client requested a CSE FSCTL on a non-CSE file.\r\n
0xc0000446 | Indicates a particular Security ID may not be assigned as the label of an object.\r\n
0xc0000450 | The process hosting the driver for this device has terminated.\r\n
0xc0000451 | The requested system device cannot be identified due to multiple indistinguishable devices potentially matching the identification criteria.\r\n
0xc0000452 | The requested system device cannot be found.\r\n
0xc0000453 | This boot application must be restarted.\r\n
0xc0000454 | Insufficient NVRAM resources exist to complete the API.  A reboot might be required.\r\n
0xc0000500 | The specified task name is invalid.\r\n
0xc0000501 | The specified task index is invalid.\r\n
0xc0000502 | The specified thread is already joining a task.\r\n
0xc0000503 | A callback has requested to bypass native code.\r\n
0xc0000602 | {Fail Fast Exception}\r\nA fail fast exception occurred. Exception handlers will not be invoked and the process will be terminated immediately.\r\n
0xc0000603 | Windows cannot verify the digital signature for this file. The signing certificate for this file has been revoked.\r\n
0xc0000700 | The ALPC port is closed.\r\n
0xc0000701 | The ALPC message requested is no longer available.\r\n
0xc0000702 | The ALPC message supplied is invalid.\r\n
0xc0000703 | The ALPC message has been canceled.\r\n
0xc0000704 | Invalid recursive dispatch attempt.\r\n
0xc0000705 | No receive buffer has been supplied in a synchrounus request.\r\n
0xc0000706 | The connection port is used in an invalid context.\r\n
0xc0000707 | The ALPC port does not accept new request messages.\r\n
0xc0000708 | The resource requested is already in use.\r\n
0xc0000709 | The hardware has reported an uncorrectable memory error.\r\n
0xc000070a | Status 0x%08x was returned, waiting on handle 0x%x for wait 0x%p, in waiter 0x%p.\r\n
0xc000070b | After a callback to 0x%p(0x%p), a completion call to SetEvent(0x%p) failed with status 0x%08x.\r\n
0xc000070c | After a callback to 0x%p(0x%p), a completion call to ReleaseSemaphore(0x%p, %d) failed with status 0x%08x.\r\n
0xc000070d | After a callback to 0x%p(0x%p), a completion call to ReleaseMutex(%p) failed with status 0x%08x.\r\n
0xc000070e | After a callback to 0x%p(0x%p), an completion call to FreeLibrary(%p) failed with status 0x%08x.\r\n
0xc000070f | The threadpool 0x%p was released while a thread was posting a callback to 0x%p(0x%p) to it.\r\n
0xc0000710 | A threadpool worker thread is impersonating a client, after a callback to 0x%p(0x%p).\r\nThis is unexpected, indicating that the callback is missing a call to revert the impersonation.\r\n
0xc0000711 | A threadpool worker thread is impersonating a client, after executing an APC.\r\nThis is unexpected, indicating that the APC is missing a call to revert the impersonation.\r\n
0xc0000712 | Either the target process, or the target thread's containing process, is a protected process.\r\n
0xc0000713 | A Thread is getting dispatched with MCA EXCEPTION because of MCA.\r\n
0xc0000714 | The client certificate account mapping is not unique.\r\n
0xc0000715 | The symbolic link cannot be followed because its type is disabled.\r\n
0xc0000716 | Indicates that the specified string is not valid for IDN normalization.\r\n
0xc0000717 | No mapping for the Unicode character exists in the target multi-byte code page.\r\n
0xc0000718 | The provided callback is already registered.\r\n
0xc0000719 | The provided context did not match the target.\r\n
0xc000071a | The specified port already has a completion list.\r\n
0xc000071b | A threadpool worker thread enter a callback at thread base priority 0x%x and exited at priority 0x%x.\r\nThis is unexpected, indicating that the callback missed restoring the priority.\r\n
0xc000071c | An invalid thread, handle %p, is specified for this operation. Possibly, a threadpool worker thread was specified.\r\n
0xc000071d | A threadpool worker thread enter a callback, which left transaction state.\r\nThis is unexpected, indicating that the callback missed clearing the transaction.\r\n
0xc000071e | A threadpool worker thread enter a callback, which left the loader lock held.\r\nThis is unexpected, indicating that the callback missed releasing the lock.\r\n
0xc000071f | A threadpool worker thread enter a callback, which left with preferred languages set.\r\nThis is unexpected, indicating that the callback missed clearing them.\r\n
0xc0000720 | A threadpool worker thread enter a callback, which left with background priorities set.\r\nThis is unexpected, indicating that the callback missed restoring the original priorities.\r\n
0xc0000721 | A threadpool worker thread enter a callback at thread affinity %p and exited at affinity %p.\r\nThis is unexpected, indicating that the callback missed restoring the priority.\r\n
0xc0000800 | The attempted operation required self healing to be enabled.\r\n
0xc0000801 | The Directory Service cannot perform the requested operation because a domain rename operation is in progress.\r\n
0xc0000802 | The requested file operation failed because the storage quota was exceeded.\r\nTo free up disk space, move files to a different location or delete unnecessary files. For more information, contact your system administrator.\r\n
0xc0000804 | The requested file operation failed because the storage policy blocks that type of file. For more information, contact your system administrator.\r\n
0xc0000805 | The operation could not be completed due to bad clusters on disk.\r\n
0xc0000806 | The operation could not be completed because the volume is dirty. Please run chkdsk and try again.\r\n
0xc0000901 | This file is checked out or locked for editing by another user.\r\n
0xc0000902 | The file must be checked out before saving changes.\r\n
0xc0000903 | The file type being saved or retrieved has been blocked.\r\n
0xc0000904 | The file size exceeds the limit allowed and cannot be saved.\r\n
0xc0000905 | Access Denied. Before opening files in this location, you must first browse to the web site and select the option to login automatically.\r\n
0xc0000906 | Operation did not complete successfully because the file contains a virus.\r\n
0xc0000907 | This file contains a virus and cannot be opened. Due to the nature of this virus, the file has been removed from this location.\r\n
0xc0000908 | The resources required for this device conflict with the MCFG table.\r\n
0xc0000909 | The operation did not complete successfully because it would cause an oplock to be broken. The caller has requested that existing oplocks not be broken.\r\n
0xc0009898 | WOW Assertion Error.\r\n
0xc000a000 | The cryptographic signature is invalid.\r\n
0xc000a001 | The cryptographic provider does not support HMAC.\r\n
0xc000a002 | The computed authentication tag did not match the input authentication tag.\r\n
0xc000a010 | The IPSEC queue overflowed.\r\n
0xc000a011 | The neighbor discovery queue overflowed.\r\n
0xc000a012 | An ICMP hop limit exceeded error was received.\r\n
0xc000a013 | The protocol is not installed on the local machine.\r\n
0xc000a014 | An operation or data has been rejected while on the network fast path.\r\n
0xc000a080 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs; the data has been lost.\r\nThis error may be caused by network connectivity issues. Please try to save this file elsewhere.\r\n
0xc000a081 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs; the data has been lost.\r\nThis error was returned by the server on which the file exists. Please try to save this file elsewhere.\r\n
0xc000a082 | {Delayed Write Failed}\r\nWindows was unable to save all the data for the file %hs; the data has been lost.\r\nThis error may be caused if the device has been removed or the media is write-protected.\r\n
0xc000a083 | Windows was unable to parse the requested XML data.\r\n
0xc000a084 | An error was encountered while processing an XML digital signature.\r\n
0xc000a085 | Indicates that the caller made the connection request in the wrong routing compartment.\r\n
0xc000a086 | Indicates that there was an AuthIP failure when attempting to connect to the remote host.\r\n
0xc000a087 | OID mapped groups cannot have members.\r\n
0xc000a088 | The specified OID cannot be found.\r\n
0xc000a100 | Hash generation for the specified version and hash type is not enabled on server.\r\n
0xc000a101 | The hash requests is not present or not up to date with the current file contents.\r\n
0xc0010001 | Debugger did not perform a state change.\r\n
0xc0010002 | Debugger has found the application is not idle.\r\n
0xc0020001 | The string binding is invalid.\r\n
0xc0020002 | The binding handle is not the correct type.\r\n
0xc0020003 | The binding handle is invalid.\r\n
0xc0020004 | The RPC protocol sequence is not supported.\r\n
0xc0020005 | The RPC protocol sequence is invalid.\r\n
0xc0020006 | The string UUID is invalid.\r\n
0xc0020007 | The endpoint format is invalid.\r\n
0xc0020008 | The network address is invalid.\r\n
0xc0020009 | No endpoint was found.\r\n
0xc002000a | The timeout value is invalid.\r\n
0xc002000b | The object UUID was not found.\r\n
0xc002000c | The object UUID has already been registered.\r\n
0xc002000d | The type UUID has already been registered.\r\n
0xc002000e | The RPC server is already listening.\r\n
0xc002000f | No protocol sequences have been registered.\r\n
0xc0020010 | The RPC server is not listening.\r\n
0xc0020011 | The manager type is unknown.\r\n
0xc0020012 | The interface is unknown.\r\n
0xc0020013 | There are no bindings.\r\n
0xc0020014 | There are no protocol sequences.\r\n
0xc0020015 | The endpoint cannot be created.\r\n
0xc0020016 | Not enough resources are available to complete this operation.\r\n
0xc0020017 | The RPC server is unavailable.\r\n
0xc0020018 | The RPC server is too busy to complete this operation.\r\n
0xc0020019 | The network options are invalid.\r\n
0xc002001a | There are no remote procedure calls active on this thread.\r\n
0xc002001b | The remote procedure call failed.\r\n
0xc002001c | The remote procedure call failed and did not execute.\r\n
0xc002001d | An RPC protocol error occurred.\r\n
0xc002001f | The transfer syntax is not supported by the RPC server.\r\n
0xc0020021 | The type UUID is not supported.\r\n
0xc0020022 | The tag is invalid.\r\n
0xc0020023 | The array bounds are invalid.\r\n
0xc0020024 | The binding does not contain an entry name.\r\n
0xc0020025 | The name syntax is invalid.\r\n
0xc0020026 | The name syntax is not supported.\r\n
0xc0020028 | No network address is available to use to construct a UUID.\r\n
0xc0020029 | The endpoint is a duplicate.\r\n
0xc002002a | The authentication type is unknown.\r\n
0xc002002b | The maximum number of calls is too small.\r\n
0xc002002c | The string is too long.\r\n
0xc002002d | The RPC protocol sequence was not found.\r\n
0xc002002e | The procedure number is out of range.\r\n
0xc002002f | The binding does not contain any authentication information.\r\n
0xc0020030 | The authentication service is unknown.\r\n
0xc0020031 | The authentication level is unknown.\r\n
0xc0020032 | The security context is invalid.\r\n
0xc0020033 | The authorization service is unknown.\r\n
0xc0020034 | The entry is invalid.\r\n
0xc0020035 | The operation cannot be performed.\r\n
0xc0020036 | There are no more endpoints available from the endpoint mapper.\r\n
0xc0020037 | No interfaces have been exported.\r\n
0xc0020038 | The entry name is incomplete.\r\n
0xc0020039 | The version option is invalid.\r\n
0xc002003a | There are no more members.\r\n
0xc002003b | There is nothing to unexport.\r\n
0xc002003c | The interface was not found.\r\n
0xc002003d | The entry already exists.\r\n
0xc002003e | The entry is not found.\r\n
0xc002003f | The name service is unavailable.\r\n
0xc0020040 | The network address family is invalid.\r\n
0xc0020041 | The requested operation is not supported.\r\n
0xc0020042 | No security context is available to allow impersonation.\r\n
0xc0020043 | An internal error occurred in RPC.\r\n
0xc0020044 | The RPC server attempted an integer divide by zero.\r\n
0xc0020045 | An addressing error occurred in the RPC server.\r\n
0xc0020046 | A floating point operation at the RPC server caused a divide by zero.\r\n
0xc0020047 | A floating point underflow occurred at the RPC server.\r\n
0xc0020048 | A floating point overflow occurred at the RPC server.\r\n
0xc0020049 | A remote procedure call is already in progress for this thread.\r\n
0xc002004a | There are no more bindings.\r\n
0xc002004b | The group member was not found.\r\n
0xc002004c | The endpoint mapper database entry could not be created.\r\n
0xc002004d | The object UUID is the nil UUID.\r\n
0xc002004f | No interfaces have been registered.\r\n
0xc0020050 | The remote procedure call was cancelled.\r\n
0xc0020051 | The binding handle does not contain all required information.\r\n
0xc0020052 | A communications failure occurred during a remote procedure call.\r\n
0xc0020053 | The requested authentication level is not supported.\r\n
0xc0020054 | No principal name registered.\r\n
0xc0020055 | The error specified is not a valid Windows RPC error code.\r\n
0xc0020057 | A security package specific error occurred.\r\n
0xc0020058 | Thread is not cancelled.\r\n
0xc0020062 | Invalid asynchronous remote procedure call handle.\r\n
0xc0020063 | Invalid asynchronous RPC call handle for this operation.\r\n
0xc0020064 | Access to the HTTP proxy is denied.\r\n
0xc0020065 | HTTP proxy server rejected the connection because the cookie authentication failed.\r\n
0xc0030001 | The list of RPC servers available for auto-handle binding has been exhausted.\r\n
0xc0030002 | The file designated by DCERPCCHARTRANS cannot be opened.\r\n
0xc0030003 | The file containing the character translation table has fewer than 512 bytes.\r\n
0xc0030004 | A null context handle is passed as an [in] parameter.\r\n
0xc0030005 | The context handle does not match any known context handles.\r\n
0xc0030006 | The context handle changed during a call.\r\n
0xc0030007 | The binding handles passed to a remote procedure call do not match.\r\n
0xc0030008 | The stub is unable to get the call handle.\r\n
0xc0030009 | A null reference pointer was passed to the stub.\r\n
0xc003000a | The enumeration value is out of range.\r\n
0xc003000b | The byte count is too small.\r\n
0xc003000c | The stub received bad data.\r\n
0xc0030059 | Invalid operation on the encoding/decoding handle.\r\n
0xc003005a | Incompatible version of the serializing package.\r\n
0xc003005b | Incompatible version of the RPC stub.\r\n
0xc003005c | The RPC pipe object is invalid or corrupted.\r\n
0xc003005d | An invalid operation was attempted on an RPC pipe object.\r\n
0xc003005e | Unsupported RPC pipe version.\r\n
0xc003005f | The RPC pipe object has already been closed.\r\n
0xc0030060 | The RPC call completed before all pipes were processed.\r\n
0xc0030061 | No more data is available from the RPC pipe.\r\n
0xc0040035 | A device is missing in the system BIOS MPS table. This device will not be used.\r\nPlease contact your system vendor for system BIOS update.\r\n
0xc0040036 | A translator failed to translate resources.\r\n
0xc0040037 | A IRQ translator failed to translate resources.\r\n
0xc0040038 | Driver %2 returned invalid ID for a child device (%3).\r\n
0xc0040039 | Reissue the given operation as a cached IO operation\r\n
0xc00a0001 | Session name %1 is invalid.\r\n
0xc00a0002 | The protocol driver %1 is invalid.\r\n
0xc00a0003 | The protocol driver %1 was not found in the system path.\r\n
0xc00a0006 | A close operation is pending on the Terminal Connection.\r\n
0xc00a0007 | There are no free output buffers available.\r\n
0xc00a0008 | The MODEM.INF file was not found.\r\n
0xc00a0009 | The modem (%1) was not found in MODEM.INF.\r\n
0xc00a000a | The modem did not accept the command sent to it.\r\nVerify the configured modem name matches the attached modem.\r\n
0xc00a000b | The modem did not respond to the command sent to it.\r\nVerify the modem is properly cabled and powered on.\r\n
0xc00a000c | Carrier detect has failed or carrier has been dropped due to disconnect.\r\n
0xc00a000d | Dial tone not detected within required time.\r\nVerify phone cable is properly attached and functional.\r\n
0xc00a000e | Busy signal detected at remote site on callback.\r\n
0xc00a000f | Voice detected at remote site on callback.\r\n
0xc00a0010 | Transport driver error\r\n
0xc00a0012 | The client you are using is not licensed to use this system. Your logon request is denied.\r\n
0xc00a0013 | The system has reached its licensed logon limit.\r\nPlease try again later.\r\n
0xc00a0014 | The system license has expired. Your logon request is denied.\r\n
0xc00a0015 | The specified session cannot be found.\r\n
0xc00a0016 | The specified session name is already in use.\r\n
0xc00a0017 | The task you are trying to do can't be completed because Remote Desktop Services is currently busy. Please try again in a few minutes. Other users should still be able to log on.\r\n
0xc00a0018 | An attempt has been made to connect to a session whose video mode is not supported by the current client.\r\n
0xc00a0022 | The application attempted to enable DOS graphics mode.\r\nDOS graphics mode is not supported.\r\n
0xc00a0024 | The requested operation can be performed only on the system console.\r\nThis is most often the result of a driver or system DLL requiring direct console access.\r\n
0xc00a0026 | The client failed to respond to the server connect message.\r\n
0xc00a0027 | Disconnecting the console session is not supported.\r\n
0xc00a0028 | Reconnecting a disconnected session to the console is not supported.\r\n
0xc00a002a | The request to control another session remotely was denied.\r\n
0xc00a002b | A process has requested access to a session, but has not been granted those access rights.\r\n
0xc00a002e | The Terminal Connection driver %1 is invalid.\r\n
0xc00a002f | The Terminal Connection driver %1 was not found in the system path.\r\n
0xc00a0030 | The requested session cannot be controlled remotely.\r\nYou cannot control your own session, a session that is trying to control your session,\r\na session that has no user logged on, nor control other sessions from the console.\r\n
0xc00a0031 | The requested session is not configured to allow remote control.\r\n
0xc00a0032 | The RDP protocol component %2 detected an error in the protocol stream and has disconnected the client.\r\n
0xc00a0033 | Your request to connect to this Terminal server has been rejected.\r\nYour Terminal Server Client license number has not been entered for this copy of the Terminal Client.\r\nPlease call your system administrator for help in entering a valid, unique license number for this Terminal Server Client.\r\nClick OK to continue.\r\n
0xc00a0034 | Your request to connect to this Terminal server has been rejected.\r\nYour Terminal Server Client license number is currently being used by another user.\r\nPlease call your system administrator to obtain a new copy of the Terminal Server Client with a valid, unique license number.\r\nClick OK to continue.\r\n
0xc00a0035 | The remote control of the console was terminated because the display mode was changed. Changing the display mode in a remote control session is not supported.\r\n
0xc00a0036 | Remote control could not be terminated because the specified session is not currently being remotely controlled.\r\n
0xc00a0037 | Your interactive logon privilege has been disabled.\r\nPlease contact your system administrator.\r\n
0xc00a0038 | The Terminal Server security layer detected an error in the protocol stream and has disconnected the client.\r\nClient IP: %2.\r\n
0xc00a0039 | The target session is incompatible with the current session.\r\n
0xc00a003a | Windows can't connect to your session because a problem occurred in the Windows video subsystem. Try connecting again later, or contact the server administrator for assistance.\r\n
0xc00b0001 | The resource loader failed to find MUI file.\r\n
0xc00b0002 | The resource loader failed to load MUI file because the file fail to pass validation.\r\n
0xc00b0003 | The RC Manifest is corrupted with garbage data or unsupported version or missing required item.\r\n
0xc00b0004 | The RC Manifest has invalid culture name.\r\n
0xc00b0005 | The RC Manifest has invalid ultimatefallback name.\r\n
0xc00b0006 | The resource loader cache doesn't have loaded MUI entry.\r\n
0xc00b0007 | User stopped resource enumeration.\r\n
0xc0130001 | The cluster node is not valid.\r\n
0xc0130002 | The cluster node already exists.\r\n
0xc0130003 | A node is in the process of joining the cluster.\r\n
0xc0130004 | The cluster node was not found.\r\n
0xc0130005 | The cluster local node information was not found.\r\n
0xc0130006 | The cluster network already exists.\r\n
0xc0130007 | The cluster network was not found.\r\n
0xc0130008 | The cluster network interface already exists.\r\n
0xc0130009 | The cluster network interface was not found.\r\n
0xc013000a | The cluster request is not valid for this object.\r\n
0xc013000b | The cluster network provider is not valid.\r\n
0xc013000c | The cluster node is down.\r\n
0xc013000d | The cluster node is not reachable.\r\n
0xc013000e | The cluster node is not a member of the cluster.\r\n
0xc013000f | A cluster join operation is not in progress.\r\n
0xc0130010 | The cluster network is not valid.\r\n
0xc0130011 | No network adapters are available.\r\n
0xc0130012 | The cluster node is up.\r\n
0xc0130013 | The cluster node is paused.\r\n
0xc0130014 | The cluster node is not paused.\r\n
0xc0130015 | No cluster security context is available.\r\n
0xc0130016 | The cluster network is not configured for internal cluster communication.\r\n
0xc0130017 | The cluster node has been poisoned.\r\n
0xc0130018 | The path does not belong to a cluster shared volume.\r\n
0xc0130019 | The cluster shared volume is not locally mounted.\r\n
0xc0140001 | An attempt was made to run an invalid AML opcode\r\n
0xc0140002 | The AML Interpreter Stack has overflowed\r\n
0xc0140003 | An inconsistent state has occurred\r\n
0xc0140004 | An attempt was made to access an array outside of its bounds\r\n
0xc0140005 | A required argument was not specified\r\n
0xc0140006 | A fatal error has occurred\r\n
0xc0140007 | An invalid SuperName was specified\r\n
0xc0140008 | An argument with an incorrect type was specified\r\n
0xc0140009 | An object with an incorrect type was specified\r\n
0xc014000a | A target with an incorrect type was specified\r\n
0xc014000b | An incorrect number of arguments were specified\r\n
0xc014000c | An address failed to translate\r\n
0xc014000d | An incorrect event type was specified\r\n
0xc014000e | A handler for the target already exists\r\n
0xc014000f | Invalid data for the target was specified\r\n
0xc0140010 | An invalid region for the target was specified\r\n
0xc0140011 | An attempt was made to access a field outside of the defined range\r\n
0xc0140012 | The Global system lock could not be acquired\r\n
0xc0140013 | An attempt was made to reinitialize the ACPI subsystem\r\n
0xc0140014 | The ACPI subsystem has not been initialized\r\n
0xc0140015 | An incorrect mutex was specified\r\n
0xc0140016 | The mutex is not currently owned\r\n
0xc0140017 | An attempt was made to access the mutex by a process that was not the owner\r\n
0xc0140018 | An error occurred during an access to Region Space\r\n
0xc0140019 | An attempt was made to use an incorrect table\r\n
0xc0140020 | The registration of an ACPI event failed\r\n
0xc0140021 | An ACPI Power Object failed to transition state\r\n
0xc0150001 | The requested section is not present in the activation context.\r\n
0xc0150002 | Windows was not able to process the application binding information.\r\nPlease refer to your System Event Log for further information.\r\n
0xc0150003 | The application binding data format is invalid.\r\n
0xc0150004 | The referenced assembly is not installed on your system.\r\n
0xc0150005 | The manifest file does not begin with the required tag and format information.\r\n
0xc0150006 | The manifest file contains one or more syntax errors.\r\n
0xc0150007 | The application attempted to activate a disabled activation context.\r\n
0xc0150008 | The requested lookup key was not found in any active activation context.\r\n
0xc0150009 | A component version required by the application conflicts with another component version already active.\r\n
0xc015000a | The type requested activation context section does not match the query API used.\r\n
0xc015000b | Lack of system resources has required isolated activation to be disabled for the current thread of execution.\r\n
0xc015000c | The referenced assembly could not be found.\r\n
0xc015000e | An attempt to set the process default activation context failed because the process default activation context was already set.\r\n
0xc015000f | The activation context being deactivated is not the most recently activated one.\r\n
0xc0150010 | The activation context being deactivated is not active for the current thread of execution.\r\n
0xc0150011 | The activation context being deactivated has already been deactivated.\r\n
0xc0150012 | The activation context of system default assembly could not be generated.\r\n
0xc0150013 | A component used by the isolation facility has requested to terminate the process.\r\n
0xc0150014 | The activation context activation stack for the running thread of execution is corrupt.\r\n
0xc0150015 | The application isolation metadata for this process or thread has become corrupt.\r\n
0xc0150016 | The value of an attribute in an identity is not within the legal range.\r\n
0xc0150017 | The name of an attribute in an identity is not within the legal range.\r\n
0xc0150018 | An identity contains two definitions for the same attribute.\r\n
0xc0150019 | The identity string is malformed. This may be due to a trailing comma, more than two unnamed attributes, missing attribute name or missing attribute value.\r\n
0xc015001a | The component store has been corrupted.\r\n
0xc015001b | A component's file does not match the verification information present in the component manifest.\r\n
0xc015001c | The identities of the manifests are identical but their contents are different.\r\n
0xc015001d | The component identities are different.\r\n
0xc015001e | The assembly is not a deployment.\r\n
0xc015001f | The file is not a part of the assembly.\r\n
0xc0150020 | An advanced installer failed during setup or servicing.\r\n
0xc0150021 | The character encoding in the XML declaration did not match the encoding used in the document.\r\n
0xc0150022 | The size of the manifest exceeds the maximum allowed.\r\n
0xc0150023 | The setting is not registered.\r\n
0xc0150024 | One or more required members of the transaction are not present.\r\n
0xc0150025 | The SMI primitive installer failed during setup or servicing.\r\n
0xc0150026 | A generic command executable returned a result that indicates failure.\r\n
0xc0150027 | A component is missing file verification information in its manifest.\r\n
0xc0190001 | The function attempted to use a name that is reserved for use by another transaction.\r\n
0xc0190002 | The transaction handle associated with this operation is not valid.\r\n
0xc0190003 | The requested operation was made in the context of a transaction that is no longer active.\r\n
0xc0190004 | The Transaction Manager was unable to be successfully initialized. Transacted operations are not supported.\r\n
0xc0190005 | Transaction support within the specified resource manager is not started or was shut down due to an error.\r\n
0xc0190006 | The metadata of the RM has been corrupted. The RM will not function.\r\n
0xc0190007 | The resource manager has attempted to prepare a transaction that it has not successfully joined.\r\n
0xc0190008 | The specified directory does not contain a file system resource manager.\r\n
0xc019000a | The remote server or share does not support transacted file operations.\r\n
0xc019000b | The requested log size for the file system resource manager is invalid.\r\n
0xc019000c | The remote server sent mismatching version number or Fid for a file opened with transactions.\r\n
0xc019000f | The RM tried to register a protocol that already exists.\r\n
0xc0190010 | The attempt to propagate the Transaction failed.\r\n
0xc0190011 | The requested propagation protocol was not registered as a CRM.\r\n
0xc0190012 | The Transaction object already has a superior enlistment, and the caller attempted an operation that would have created a new superior. Only a single superior enlistment is allowed.\r\n
0xc0190013 | The requested operation is not valid on the Transaction object in its current state.\r\n
0xc0190014 | The caller has called a response API, but the response is not expected because the TM did not issue the corresponding request to the caller.\r\n
0xc0190015 | It is too late to perform the requested operation, since the Transaction has already been aborted.\r\n
0xc0190016 | It is too late to perform the requested operation, since the Transaction has already been committed.\r\n
0xc0190017 | The buffer passed in to NtPushTransaction or NtPullTransaction is not in a valid format.\r\n
0xc0190018 | The current transaction context associated with the thread is not a valid handle to a transaction object.\r\n
0xc0190019 | An attempt to create space in the transactional resource manager's log failed. The failure status has been recorded in the event log.\r\n
0xc0190021 | The object (file, stream, link) corresponding to the handle has been deleted by a transaction savepoint rollback.\r\n
0xc0190022 | The specified file miniversion was not found for this transacted file open.\r\n
0xc0190023 | The specified file miniversion was found but has been invalidated. Most likely cause is a transaction savepoint rollback.\r\n
0xc0190024 | A miniversion may only be opened in the context of the transaction that created it.\r\n
0xc0190025 | It is not possible to open a miniversion with modify access.\r\n
0xc0190026 | It is not possible to create any more miniversions for this stream.\r\n
0xc0190028 | The handle has been invalidated by a transaction. The most likely cause is the presence of memory mapping on a file or an open handle when the transaction ended or rolled back to savepoint.\r\n
0xc0190030 | The log data is corrupt.\r\n
0xc0190032 | The transaction outcome is unavailable because the resource manager responsible for it has disconnected.\r\n
0xc0190033 | The request was rejected because the enlistment in question is not a superior enlistment.\r\n
0xc0190036 | The file cannot be opened transactionally, because its identity depends on the outcome of an unresolved transaction.\r\n
0xc0190037 | The operation cannot be performed because another transaction is depending on the fact that this property will not change.\r\n
0xc0190038 | The operation would involve a single file with two transactional resource managers and is therefore not allowed.\r\n
0xc0190039 | The $Txf directory must be empty for this operation to succeed.\r\n
0xc019003a | The operation would leave a transactional resource manager in an inconsistent state and is therefore not allowed.\r\n
0xc019003b | The operation could not be completed because the transaction manager does not have a log.\r\n
0xc019003c | A rollback could not be scheduled because a previously scheduled rollback has already executed or been queued for execution.\r\n
0xc019003d | The transactional metadata attribute on the file or directory %hs is corrupt and unreadable.\r\n
0xc019003e | The encryption operation could not be completed because a transaction is active.\r\n
0xc019003f | This object is not allowed to be opened in a transaction.\r\n
0xc0190040 | Memory mapping (creating a mapped section) a remote file under a transaction is not supported.\r\n
0xc0190043 | Promotion was required in order to allow the resource manager to enlist, but the transaction was set to disallow it.\r\n
0xc0190044 | This file is open for modification in an unresolved transaction and may be opened for execute only by a transacted reader.\r\n
0xc0190045 | The request to thaw frozen transactions was ignored because transactions had not previously been frozen.\r\n
0xc0190046 | Transactions cannot be frozen because a freeze is already in progress.\r\n
0xc0190047 | The target volume is not a snapshot volume. This operation is only valid on a volume mounted as a snapshot.\r\n
0xc0190048 | The savepoint operation failed because files are open on the transaction. This is not permitted.\r\n
0xc0190049 | The sparse operation could not be completed because a transaction is active on the file.\r\n
0xc019004a | The call to create a TransactionManager object failed because the Tm Identity stored in the logfile does not match the Tm Identity that was passed in as an argument.\r\n
0xc019004b | I/O was attempted on a section object that has been floated as a result of a transaction ending. There is no valid data.\r\n
0xc019004c | The transactional resource manager cannot currently accept transacted work due to a transient condition such as low resources.\r\n
0xc019004d | The transactional resource manager had too many tranactions outstanding that could not be aborted. The transactional resource manger has been shut down.\r\n
0xc019004e | The specified Transaction was unable to be opened, because it was not found.\r\n
0xc019004f | The specified ResourceManager was unable to be opened, because it was not found.\r\n
0xc0190050 | The specified Enlistment was unable to be opened, because it was not found.\r\n
0xc0190051 | The specified TransactionManager was unable to be opened, because it was not found.\r\n
0xc0190052 | The object specified could not be created or opened, because its associated TransactionManager is not online.  The TransactionManager must be brought fully Online by calling RecoverTransactionManager to recover to the end of its LogFile before objects in its Transaction or ResourceManager namespaces can be opened.  In addition, errors in writing records to its LogFile can cause a TransactionManager to go offline.\r\n
0xc0190053 | The specified TransactionManager was unable to create the objects contained in its logfile in the Ob namespace. Therefore, the TransactionManager was unable to recover.\r\n
0xc0190054 | The call to create a superior Enlistment on this Transaction object could not be completed, because the Transaction object specified for the enlistment is a subordinate branch of the Transaction. Only the root of the Transaction can be enlisted on as a superior.\r\n
0xc0190055 | Because the associated transaction manager or resource manager has been closed, the handle is no longer valid.\r\n
0xc0190056 | The compression operation could not be completed because a transaction is active on the file.\r\n
0xc0190057 | The specified operation could not be performed on this Superior enlistment, because the enlistment was not created with the corresponding completion response in the NotificationMask.\r\n
0xc0190058 | The specified operation could not be performed, because the record that would be logged was too long. This can occur because of two conditions:  either there are too many Enlistments on this Transaction, or the combined RecoveryInformation being logged on behalf of those Enlistments is too long.\r\n
0xc0190059 | The link tracking operation could not be completed because a transaction is active.\r\n
0xc019005a | This operation cannot be performed in a transaction.\r\n
0xc019005b | The kernel transaction manager had to abort or forget the transaction because it blocked forward progress.\r\n
0xc019005c | The TransactionManager identity that was supplied did not match the one recorded in the TransactionManager's log file.\r\n
0xc019005d | This snapshot operation cannot continue because a transactional resource manager cannot be frozen in its current state.  Please try again.\r\n
0xc019005e | The transaction cannot be enlisted on with the specified EnlistmentMask, because the transaction has already completed the PrePrepare phase.  In order to ensure correctness, the ResourceManager must switch to a write-through mode and cease caching data within this transaction.  Enlisting for only subsequent transaction phases may still succeed.\r\n
0xc019005f | The transaction does not have a superior enlistment.\r\n
0xc0190060 | The handle is no longer properly associated with its transaction.  It may have been opened in a transactional resource manager that was subsequently forced to restart.  Please close the handle and open a new one.\r\n
0xc0190061 | The specified operation could not be performed because the resource manager is not enlisted in the transaction.\r\n
0xc01a0001 | Log service found an invalid log sector.\r\n
0xc01a0002 | Log service encountered a log sector with invalid block parity.\r\n
0xc01a0003 | Log service encountered a remapped log sector.\r\n
0xc01a0004 | Log service encountered a partial or incomplete log block.\r\n
0xc01a0005 | Log service encountered an attempt access data outside the active log range.\r\n
0xc01a0006 | Log service user log marshalling buffers are exhausted.\r\n
0xc01a0007 | Log service encountered an attempt read from a marshalling area with an invalid read context.\r\n
0xc01a0008 | Log service encountered an invalid log restart area.\r\n
0xc01a0009 | Log service encountered an invalid log block version.\r\n
0xc01a000a | Log service encountered an invalid log block.\r\n
0xc01a000b | Log service encountered an attempt to read the log with an invalid read mode.\r\n
0xc01a000d | Log service encountered a corrupted metadata file.\r\n
0xc01a000e | Log service encountered a metadata file that could not be created by the log file system.\r\n
0xc01a000f | Log service encountered a metadata file with inconsistent data.\r\n
0xc01a0010 | Log service encountered an attempt to erroneously allocate or dispose reservation space.\r\n
0xc01a0011 | Log service cannot delete log file or file system container.\r\n
0xc01a0012 | Log service has reached the maximum allowable containers allocated to a log file.\r\n
0xc01a0013 | Log service has attempted to read or write backwards past the start of the log.\r\n
0xc01a0014 | Log policy could not be installed because a policy of the same type is already present.\r\n
0xc01a0015 | Log policy in question was not installed at the time of the request.\r\n
0xc01a0016 | The installed set of policies on the log is invalid.\r\n
0xc01a0017 | A policy on the log in question prevented the operation from completing.\r\n
0xc01a0018 | Log space cannot be reclaimed because the log is pinned by the archive tail.\r\n
0xc01a0019 | Log record is not a record in the log file.\r\n
0xc01a001a | Number of reserved log records or the adjustment of the number of reserved log records is invalid.\r\n
0xc01a001b | Reserved log space or the adjustment of the log space is invalid.\r\n
0xc01a001c | A new or existing archive tail or base of the active log is invalid.\r\n
0xc01a001d | Log space is exhausted.\r\n
0xc01a001e | Log is multiplexed, no direct writes to the physical log is allowed.\r\n
0xc01a001f | The operation failed because the log is a dedicated log.\r\n
0xc01a0020 | The operation requires an archive context.\r\n
0xc01a0021 | Log archival is in progress.\r\n
0xc01a0022 | The operation requires a non-ephemeral log, but the log is ephemeral.\r\n
0xc01a0023 | The log must have at least two containers before it can be read from or written to.\r\n
0xc01a0024 | A log client has already registered on the stream.\r\n
0xc01a0025 | A log client has not been registered on the stream.\r\n
0xc01a0026 | A request has already been made to handle the log full condition.\r\n
0xc01a0027 | Log service encountered an error when attempting to read from a log container.\r\n
0xc01a0028 | Log service encountered an error when attempting to write to a log container.\r\n
0xc01a0029 | Log service encountered an error when attempting open a log container.\r\n
0xc01a002a | Log service encountered an invalid container state when attempting a requested action.\r\n
0xc01a002b | Log service is not in the correct state to perform a requested action.\r\n
0xc01a002c | Log space cannot be reclaimed because the log is pinned.\r\n
0xc01a002d | Log metadata flush failed.\r\n
0xc01a002e | Security on the log and its containers is inconsistent.\r\n
0xc01a002f | Records were appended to the log or reservation changes were made, but the log could not be flushed.\r\n
0xc01a0030 | The log is pinned due to reservation consuming most of the log space. Free some reserved records to make space available.\r\n
0xc01b00ea | {Display Driver Stopped Responding}\r\nThe %hs display driver has stopped working normally. Save your work and reboot the system to restore full display functionality. The next time you reboot the machine a dialog will be displayed giving you a chance to upload data about this failure to Microsoft.\r\n
0xc01c0001 | A handler was not defined by the filter for this operation.\r\n
0xc01c0002 | A context is already defined for this object.\r\n
0xc01c0003 | Asynchronous requests are not valid for this operation.\r\n
0xc01c0004 | Internal error code used by the filter manager to determine if a fastio operation should be forced down the IRP path. Mini-filters should never return this value.\r\n
0xc01c0005 | An invalid name request was made. The name requested cannot be retrieved at this time.\r\n
0xc01c0006 | Posting this operation to a worker thread for further processing is not safe at this time because it could lead to a system deadlock.\r\n
0xc01c0007 | The Filter Manager was not initialized when a filter tried to register. Make sure that the Filter Manager is getting loaded as a driver.\r\n
0xc01c0008 | The filter is not ready for attachment to volumes because it has not finished initializing (FltStartFiltering has not been called).\r\n
0xc01c0009 | The filter must cleanup any operation specific context at this time because it is being removed from the system before the operation is completed by the lower drivers.\r\n
0xc01c000a | The Filter Manager had an internal error from which it cannot recover, therefore the operation has been failed. This is usually the result of a filter returning an invalid value from a pre-operation callback.\r\n
0xc01c000b | The object specified for this action is in the process of being deleted, therefore the action requested cannot be completed at this time.\r\n
0xc01c000c | Non-paged pool must be used for this type of context.\r\n
0xc01c000d | A duplicate handler definition has been provided for an operation.\r\n
0xc01c000e | The callback data queue has been disabled.\r\n
0xc01c000f | Do not attach the filter to the volume at this time.\r\n
0xc01c0010 | Do not detach the filter from the volume at this time.\r\n
0xc01c0011 | An instance already exists at this altitude on the volume specified.\r\n
0xc01c0012 | An instance already exists with this name on the volume specified.\r\n
0xc01c0013 | The system could not find the filter specified.\r\n
0xc01c0014 | The system could not find the volume specified.\r\n
0xc01c0015 | The system could not find the instance specified.\r\n
0xc01c0016 | No registered context allocation definition was found for the given request.\r\n
0xc01c0017 | An invalid parameter was specified during context registration.\r\n
0xc01c0018 | The name requested was not found in Filter Manager's name cache and could not be retrieved from the file system.\r\n
0xc01c0019 | The requested device object does not exist for the given volume.\r\n
0xc01c001a | The specified volume is already mounted.\r\n
0xc01c001b | The specified Transaction Context is already enlisted in a transaction\r\n
0xc01c001c | The specifiec context is already attached to another object\r\n
0xc01c0020 | No waiter is present for the filter's reply to this message.\r\n
0xc01d0001 | Monitor descriptor could not be obtained.\r\n
0xc01d0002 | Format of the obtained monitor descriptor is not supported by this release.\r\n
0xc01d0003 | Checksum of the obtained monitor descriptor is invalid.\r\n
0xc01d0004 | Monitor descriptor contains an invalid standard timing block.\r\n
0xc01d0005 | WMI data block registration failed for one of the MSMonitorClass WMI subclasses.\r\n
0xc01d0006 | Provided monitor descriptor block is either corrupted or does not contain monitor's detailed serial number.\r\n
0xc01d0007 | Provided monitor descriptor block is either corrupted or does not contain monitor's user friendly name.\r\n
0xc01d0008 | There is no monitor descriptor data at the specified (offset, size) region.\r\n
0xc01d0009 | Monitor descriptor contains an invalid detailed timing block.\r\n
0xc01d000a | Monitor descriptor contains invalid manufacture date.\r\n
0xc01e0000 | Exclusive mode ownership is needed to create unmanaged primary allocation.\r\n
0xc01e0001 | The driver needs more DMA buffer space in order to complete the requested operation.\r\n
0xc01e0002 | Specified display adapter handle is invalid.\r\n
0xc01e0003 | Specified display adapter and all of its state has been reset.\r\n
0xc01e0004 | The driver stack doesn't match the expected driver model.\r\n
0xc01e0005 | Present happened but ended up into the changed desktop mode\r\n
0xc01e0006 | Nothing to present due to desktop occlusion\r\n
0xc01e0007 | Not able to present due to denial of desktop access\r\n
0xc01e0008 | Not able to present with color convertion\r\n
0xc01e0009 | The kernel driver detected a version mismatch between it and the user mode driver.\r\n
0xc01e000b | Present redirection is disabled (desktop windowing management subsystem is off).\r\n
0xc01e000c | Previous exclusive VidPn source owner has released its ownership\r\n
0xc01e0100 | Not enough video memory available to complete the operation.\r\n
0xc01e0101 | Couldn't probe and lock the underlying memory of an allocation.\r\n
0xc01e0102 | The allocation is currently busy.\r\n
0xc01e0103 | An object being referenced has already reached the maximum reference count and can't be referenced any further.\r\n
0xc01e0104 | A problem couldn't be solved due to some currently existing condition. The problem should be tried again later.\r\n
0xc01e0105 | A problem couldn't be solved due to some currently existing condition. The problem should be tried again immediately.\r\n
0xc01e0106 | The allocation is invalid.\r\n
0xc01e0107 | No more unswizzling aperture are currently available.\r\n
0xc01e0108 | The current allocation can't be unswizzled by an aperture.\r\n
0xc01e0109 | The request failed because a pinned allocation can't be evicted.\r\n
0xc01e0110 | The allocation can't be used from it's current segment location for the specified operation.\r\n
0xc01e0111 | A locked allocation can't be used in the current command buffer.\r\n
0xc01e0112 | The allocation being referenced has been closed permanently.\r\n
0xc01e0113 | An invalid allocation instance is being referenced.\r\n
0xc01e0114 | An invalid allocation handle is being referenced.\r\n
0xc01e0115 | The allocation being referenced doesn't belong to the current device.\r\n
0xc01e0116 | The specified allocation lost its content.\r\n
0xc01e0200 | GPU exception is detected on the given device. The device is not able to be scheduled.\r\n
0xc01e0300 | Specified VidPN topology is invalid.\r\n
0xc01e0301 | Specified VidPN topology is valid but is not supported by this model of the display adapter.\r\n
0xc01e0302 | Specified VidPN topology is valid but is not supported by the display adapter at this time, due to current allocation of its resources.\r\n
0xc01e0303 | Specified VidPN handle is invalid.\r\n
0xc01e0304 | Specified video present source is invalid.\r\n
0xc01e0305 | Specified video present target is invalid.\r\n
0xc01e0306 | Specified VidPN modality is not supported (e.g. at least two of the pinned modes are not cofunctional).\r\n
0xc01e0308 | Specified VidPN source mode set is invalid.\r\n
0xc01e0309 | Specified VidPN target mode set is invalid.\r\n
0xc01e030a | Specified video signal frequency is invalid.\r\n
0xc01e030b | Specified video signal active region is invalid.\r\n
0xc01e030c | Specified video signal total region is invalid.\r\n
0xc01e0310 | Specified video present source mode is invalid.\r\n
0xc01e0311 | Specified video present target mode is invalid.\r\n
0xc01e0312 | Pinned mode must remain in the set on VidPN's cofunctional modality enumeration.\r\n
0xc01e0313 | Specified video present path is already in VidPN's topology.\r\n
0xc01e0314 | Specified mode is already in the mode set.\r\n
0xc01e0315 | Specified video present source set is invalid.\r\n
0xc01e0316 | Specified video present target set is invalid.\r\n
0xc01e0317 | Specified video present source is already in the video present source set.\r\n
0xc01e0318 | Specified video present target is already in the video present target set.\r\n
0xc01e0319 | Specified VidPN present path is invalid.\r\n
0xc01e031a | Miniport has no recommendation for augmentation of the specified VidPN's topology.\r\n
0xc01e031b | Specified monitor frequency range set is invalid.\r\n
0xc01e031c | Specified monitor frequency range is invalid.\r\n
0xc01e031d | Specified frequency range is not in the specified monitor frequency range set.\r\n
0xc01e031f | Specified frequency range is already in the specified monitor frequency range set.\r\n
0xc01e0320 | Specified mode set is stale. Please reacquire the new mode set.\r\n
0xc01e0321 | Specified monitor source mode set is invalid.\r\n
0xc01e0322 | Specified monitor source mode is invalid.\r\n
0xc01e0323 | Miniport does not have any recommendation regarding the request to provide a functional VidPN given the current display adapter configuration.\r\n
0xc01e0324 | ID of the specified mode is already used by another mode in the set.\r\n
0xc01e0325 | System failed to determine a mode that is supported by both the display adapter and the monitor connected to it.\r\n
0xc01e0326 | Number of video present targets must be greater than or equal to the number of video present sources.\r\n
0xc01e0327 | Specified present path is not in VidPN's topology.\r\n
0xc01e0328 | Display adapter must have at least one video present source.\r\n
0xc01e0329 | Display adapter must have at least one video present target.\r\n
0xc01e032a | Specified monitor descriptor set is invalid.\r\n
0xc01e032b | Specified monitor descriptor is invalid.\r\n
0xc01e032c | Specified descriptor is not in the specified monitor descriptor set.\r\n
0xc01e032d | Specified descriptor is already in the specified monitor descriptor set.\r\n
0xc01e032e | ID of the specified monitor descriptor is already used by another descriptor in the set.\r\n
0xc01e032f | Specified video present target subset type is invalid.\r\n
0xc01e0330 | Two or more of the specified resources are not related to each other, as defined by the interface semantics.\r\n
0xc01e0331 | ID of the specified video present source is already used by another source in the set.\r\n
0xc01e0332 | ID of the specified video present target is already used by another target in the set.\r\n
0xc01e0333 | Specified VidPN source cannot be used because there is no available VidPN target to connect it to.\r\n
0xc01e0334 | Newly arrived monitor could not be associated with a display adapter.\r\n
0xc01e0335 | Display adapter in question does not have an associated VidPN manager.\r\n
0xc01e0336 | VidPN manager of the display adapter in question does not have an active VidPN.\r\n
0xc01e0337 | Specified VidPN topology is stale. Please reacquire the new topology.\r\n
0xc01e0338 | There is no monitor connected on the specified video present target.\r\n
0xc01e0339 | Specified source is not part of the specified VidPN's topology.\r\n
0xc01e033a | Specified primary surface size is invalid.\r\n
0xc01e033b | Specified visible region size is invalid.\r\n
0xc01e033c | Specified stride is invalid.\r\n
0xc01e033d | Specified pixel format is invalid.\r\n
0xc01e033e | Specified color basis is invalid.\r\n
0xc01e033f | Specified pixel value access mode is invalid.\r\n
0xc01e0340 | Specified target is not part of the specified VidPN's topology.\r\n
0xc01e0341 | Failed to acquire display mode management interface.\r\n
0xc01e0342 | Specified VidPN source is already owned by a DMM client and cannot be used until that client releases it.\r\n
0xc01e0343 | Specified VidPN is active and cannot be accessed.\r\n
0xc01e0344 | Specified VidPN present path importance ordinal is invalid.\r\n
0xc01e0345 | Specified VidPN present path content geometry transformation is invalid.\r\n
0xc01e0346 | Specified content geometry transformation is not supported on the respective VidPN present path.\r\n
0xc01e0347 | Specified gamma ramp is invalid.\r\n
0xc01e0348 | Specified gamma ramp is not supported on the respective VidPN present path.\r\n
0xc01e0349 | Multi-sampling is not supported on the respective VidPN present path.\r\n
0xc01e034a | Specified mode is not in the specified mode set.\r\n
0xc01e034d | Specified VidPN topology recommendation reason is invalid.\r\n
0xc01e034e | Specified VidPN present path content type is invalid.\r\n
0xc01e034f | Specified VidPN present path copy protection type is invalid.\r\n
0xc01e0350 | No more than one unassigned mode set can exist at any given time for a given VidPN source/target.\r\n
0xc01e0352 | Specified scanline ordering type is invalid.\r\n
0xc01e0353 | Topology changes are not allowed for the specified VidPN.\r\n
0xc01e0354 | All available importance ordinals are already used in specified topology.\r\n
0xc01e0355 | Specified primary surface has a different private format attribute than the current primary surface\r\n
0xc01e0356 | Specified mode pruning algorithm is invalid\r\n
0xc01e0357 | Specified monitor capability origin is invalid.\r\n
0xc01e0358 | Specified monitor frequency range constraint is invalid.\r\n
0xc01e0359 | Maximum supported number of present paths has been reached.\r\n
0xc01e035a | Miniport requested that augmentation be cancelled for the specified source of the specified VidPN's topology.\r\n
0xc01e035b | Specified client type was not recognized.\r\n
0xc01e035c | Client VidPN is not set on this adapter (e.g. no user mode initiated mode changes took place on this adapter yet).\r\n
0xc01e0400 | Specified display adapter child device already has an external device connected to it.\r\n
0xc01e0401 | Specified display adapter child device does not support descriptor exposure.\r\n
0xc01e0430 | The display adapter is not linked to any other adapters.\r\n
0xc01e0431 | Lead adapter in a linked configuration was not enumerated yet.\r\n
0xc01e0432 | Some chain adapters in a linked configuration were not enumerated yet.\r\n
0xc01e0433 | The chain of linked adapters is not ready to start because of an unknown failure.\r\n
0xc01e0434 | An attempt was made to start a lead link display adapter when the chain links were not started yet.\r\n
0xc01e0435 | An attempt was made to power up a lead link display adapter when the chain links were powered down.\r\n
0xc01e0436 | The adapter link was found to be in an inconsistent state. Not all adapters are in an expected PNP/Power state.\r\n
0xc01e0438 | The driver trying to start is not the same as the driver for the POSTed display adapter.\r\n
0xc01e043b | An operation is being attempted that requires the display adapter to be in a quiescent state.\r\n
0xc01e0500 | The driver does not support OPM.\r\n
0xc01e0501 | The driver does not support COPP.\r\n
0xc01e0502 | The driver does not support UAB.\r\n
0xc01e0503 | The specified encrypted parameters are invalid.\r\n
0xc01e0505 | The GDI display device passed to this function does not have any active protected outputs.\r\n
0xc01e050b | An internal error caused an operation to fail.\r\n
0xc01e050c | The function failed because the caller passed in an invalid OPM user mode handle.\r\n
0xc01e050e | A certificate could not be returned because the certificate buffer passed to the function was too small.\r\n
0xc01e050f | The DxgkDdiOpmCreateProtectedOutput function could not create a protected output because the Video Present Target is in spanning mode.\r\n
0xc01e0510 | The DxgkDdiOpmCreateProtectedOutput function could not create a protected output because the Video Present Target is in theater mode.\r\n
0xc01e0511 | The function failed because the display adapter's Hardware Functionality Scan failed to validate the graphics hardware.\r\n
0xc01e0512 | The HDCP System Renewability Message passed to this function did not comply with section 5 of the HDCP 1.1 specification.\r\n
0xc01e0513 | The protected output cannot enable the High-bandwidth Digital Content Protection (HDCP) System because it does not support HDCP.\r\n
0xc01e0514 | The protected output cannot enable Analogue Copy Protection (ACP) because it does not support ACP.\r\n
0xc01e0515 | The protected output cannot enable the Content Generation Management System Analogue (CGMS-A) protection technology because it does not support CGMS-A.\r\n
0xc01e0516 | The DxgkDdiOPMGetInformation function cannot return the version of the SRM being used because the application never successfully passed an SRM to the protected output.\r\n
0xc01e0517 | The DxgkDdiOPMConfigureProtectedOutput function cannot enable the specified output protection technology because the output's screen resolution is too high.\r\n
0xc01e0518 | The DxgkDdiOPMConfigureProtectedOutput function cannot enable HDCP because the display adapter's HDCP hardware is already being used by other physical outputs.\r\n
0xc01e051a | The operating system asynchronously destroyed this OPM protected output because the operating system's state changed. This error typically occurs because the monitor PDO associated with this protected output was removed, the monitor PDO associated with this protected output was stopped, or the protected output's session became a non-console session.\r\n
0xc01e051c | Either the DxgkDdiOPMGetCOPPCompatibleInformation, DxgkDdiOPMGetInformation, or DxgkDdiOPMConfigureProtectedOutput function failed. This error is returned when the caller tries to use a COPP specific command while the protected output has OPM semantics only.\r\n
0xc01e051d | The DxgkDdiOPMGetInformation and DxgkDdiOPMGetCOPPCompatibleInformation functions return this error code if the passed in sequence number is not the expected sequence number or the passed in OMAC value is invalid.\r\n
0xc01e051e | The function failed because an unexpected error occurred inside of a display driver.\r\n
0xc01e051f | Either the DxgkDdiOPMGetCOPPCompatibleInformation, DxgkDdiOPMGetInformation, or DxgkDdiOPMConfigureProtectedOutput function failed. This error is returned when the caller tries to use an OPM specific command while the protected output has COPP semantics only.\r\n
0xc01e0520 | The DxgkDdiOPMGetCOPPCompatibleInformation and DxgkDdiOPMConfigureProtectedOutput functions return this error if the display driver does not support the DXGKMDT_OPM_GET_ACP_AND_CGMSA_SIGNALING and DXGKMDT_OPM_SET_ACP_AND_CGMSA_SIGNALING GUIDs.\r\n
0xc01e0521 | The DxgkDdiOPMConfigureProtectedOutput function returns this error code if the passed in sequence number is not the expected sequence number or the passed in OMAC value is invalid.\r\n
0xc01e0580 | The monitor connected to the specified video output does not have an I2C bus.\r\n
0xc01e0581 | No device on the I2C bus has the specified address.\r\n
0xc01e0582 | An error occurred while transmitting data to the device on the I2C bus.\r\n
0xc01e0583 | An error occurred while receiving data from the device on the I2C bus.\r\n
0xc01e0584 | The monitor does not support the specified VCP code.\r\n
0xc01e0585 | The data received from the monitor is invalid.\r\n
0xc01e0586 | The function failed because a monitor returned an invalid Timing Status byte when the operating system used the DDC/CI Get Timing Report & Timing Message command to get a timing report from a monitor.\r\n
0xc01e0587 | A monitor returned a DDC/CI capabilities string which did not comply with the ACCESS.bus 3.0, DDC/CI 1.1, or MCCS 2 Revision 1 specification.\r\n
0xc01e0588 | An internal error caused an operation to fail.\r\n
0xc01e0589 | An operation failed because a DDC/CI message had an invalid value in its command field.\r\n
0xc01e058a | An error occurred because the field length of a DDC/CI message contained an invalid value.\r\n
0xc01e058b | An error occurred because the checksum field in a DDC/CI message did not match the message's computed checksum value. This error implies that the data was corrupted while it was being transmitted from a monitor to a computer.\r\n
0xc01e058c | This function failed because an invalid monitor handle was passed to it.\r\n
0xc01e058d | The operating system asynchronously destroyed the monitor which corresponds to this handle because the operating system's state changed. This error typically occurs because the monitor PDO associated with this handle was removed, the monitor PDO associated with this handle was stopped, or a display mode change occurred. A display mode change occurs when windows sends a WM_DISPLAYCHANGE windows message to applications.\r\n
0xc01e05e0 | This function can only be used if a program is running in the local console session. It cannot be used if a program is running on a remote desktop session or on a terminal server session.\r\n
0xc01e05e1 | This function cannot find an actual GDI display device which corresponds to the specified GDI display device name.\r\n
0xc01e05e2 | The function failed because the specified GDI display device was not attached to the Windows desktop.\r\n
0xc01e05e3 | This function does not support GDI mirroring display devices because GDI mirroring display devices do not have any physical monitors associated with them.\r\n
0xc01e05e4 | The function failed because an invalid pointer parameter was passed to it. A pointer parameter is invalid if it is NULL, it points to an invalid address, it points to a kernel mode address or it is not correctly aligned.\r\n
0xc01e05e5 | This function failed because the GDI device passed to it did not have any monitors associated with it.\r\n
0xc01e05e6 | An array passed to the function cannot hold all of the data that the function must copy into the array.\r\n
0xc01e05e7 | An internal error caused an operation to fail.\r\n
0xc01e05e8 | The function failed because the current session is changing its type. This function cannot be called when the current session is changing its type. There are currently three types of sessions: console, disconnected and remote.\r\n
0xc0210000 | This volume is locked by BitLocker Drive Encryption.\r\n
0xc0210001 | The volume is not encrypted, no key is available.\r\n
0xc0210002 | The control block for the encrypted volume is not valid.\r\n
0xc0210003 | The volume cannot be encrypted because it does not have enough free space.\r\n
0xc0210004 | The volume cannot be encrypted because the file system is not supported.\r\n
0xc0210005 | The file system size is larger than the partition size in the partition table.\r\n
0xc0210006 | The file system does not extend to the end of the volume.\r\n
0xc0210007 | This operation cannot be performed while a file system is mounted on the volume.\r\n
0xc0210008 | BitLocker Drive Encryption is not included with this version of Windows.\r\n
0xc0210009 | Requested action not allowed in the current volume state.\r\n
0xc021000a | Data supplied is malformed.\r\n
0xc021000b | The volume is not bound to the system.\r\n
0xc021000c | That volume is not a data volume.\r\n
0xc021000d | A read operation failed while converting the volume.\r\n
0xc021000e | A write operation failed while converting the volume.\r\n
0xc021000f | The control block for the encrypted volume was updated by another thread. Try again.\r\n
0xc0210010 | The encryption algorithm does not support the sector size of that volume.\r\n
0xc0210011 | BitLocker recovery authentication failed.\r\n
0xc0210012 | That volume is not the OS volume.\r\n
0xc0210013 | The BitLocker startup key or recovery password could not be read from external media.\r\n
0xc0210014 | The BitLocker startup key or recovery password file is corrupt or invalid.\r\n
0xc0210015 | The BitLocker encryption key could not be obtained from the startup key or recovery password.\r\n
0xc0210016 | The Trusted Platform Module (TPM) is disabled.\r\n
0xc0210017 | The authorization data for the Storage Root Key (SRK) of the Trusted Platform Module (TPM) is not zero.\r\n
0xc0210018 | The system boot information changed or the Trusted Platform Module (TPM) locked out access to BitLocker encryption keys until the computer is restarted.\r\n
0xc0210019 | The BitLocker encryption key could not be obtained from the Trusted Platform Module (TPM).\r\n
0xc021001a | The BitLocker encryption key could not be obtained from the Trusted Platform Module (TPM) and PIN.\r\n
0xc021001b | A boot application hash does not match the hash computed when BitLocker was turned on.\r\n
0xc021001c | The Boot Configuration Data (BCD) settings are not supported or have changed since BitLocker was enabled.\r\n
0xc021001d | Boot debugging is enabled. Run bcdedit to turn it off.\r\n
0xc021001e | The BitLocker encryption key could not be obtained.\r\n
0xc021001f | The metadata disk region pointer is incorrect.\r\n
0xc0210020 | The backup copy of the metadata is out of date.\r\n
0xc0210021 | No action was taken as a system reboot is required.\r\n
0xc0210022 | No action was taken as BitLocker Drive Encryption is in RAW access mode.\r\n
0xc0210023 | BitLocker Drive Encryption cannot enter raw access mode for this volume.\r\n
0xc0210024 | The auto-unlock master key was not available from the operating system volume. Retry the operation using the BitLocker WMI interface.\r\n
0xc0210025 | The system firmware failed to enable clearing of system memory on reboot.\r\n
0xc0210026 | This feature of BitLocker Drive Encryption is not included with this version of Windows.\r\n
0xc0210027 | Group policy does not permit turning off BitLocker Drive Encryption on roaming data volumes.\r\n
0xc0210028 | Bitlocker Drive Encryption failed to recover from aborted conversion. This could be due to either all conversion logs being corrupted or the media being write-protected.\r\n
0xc0210029 | The requested virtualization size is too big.\r\n
0xc021002a | The management information stored on the drive contained an unknown type. If you are using an old version of Windows, try accessing the drive from the latest version.\r\n
0xc0210030 | The drive is too small to be protected using BitLocker Drive Encryption.\r\n
0xc0210031 | The BitLocker encryption key could not be obtained from the Trusted Platform Module (TPM) and enhanced PIN. Try using a PIN containing only numerals.\r\n
0xc0220001 | The callout does not exist.\r\n
0xc0220002 | The filter condition does not exist.\r\n
0xc0220003 | The filter does not exist.\r\n
0xc0220004 | The layer does not exist.\r\n
0xc0220005 | The provider does not exist.\r\n
0xc0220006 | The provider context does not exist.\r\n
0xc0220007 | The sublayer does not exist.\r\n
0xc0220008 | The object does not exist.\r\n
0xc0220009 | An object with that GUID or LUID already exists.\r\n
0xc022000a | The object is referenced by other objects so cannot be deleted.\r\n
0xc022000b | The call is not allowed from within a dynamic session.\r\n
0xc022000c | The call was made from the wrong session so cannot be completed.\r\n
0xc022000d | The call must be made from within an explicit transaction.\r\n
0xc022000e | The call is not allowed from within an explicit transaction.\r\n
0xc022000f | The explicit transaction has been forcibly cancelled.\r\n
0xc0220010 | The session has been cancelled.\r\n
0xc0220011 | The call is not allowed from within a read-only transaction.\r\n
0xc0220012 | The call timed out while waiting to acquire the transaction lock.\r\n
0xc0220013 | Collection of network diagnostic events is disabled.\r\n
0xc0220014 | The operation is not supported by the specified layer.\r\n
0xc0220015 | The call is allowed for kernel-mode callers only.\r\n
0xc0220016 | The call tried to associate two objects with incompatible lifetimes.\r\n
0xc0220017 | The object is built in so cannot be deleted.\r\n
0xc0220018 | The maximum number of callouts has been reached.\r\n
0xc0220019 | A notification could not be delivered because a message queue is at its maximum capacity.\r\n
0xc022001a | The traffic parameters do not match those for the security association context.\r\n
0xc022001b | The call is not allowed for the current security association state.\r\n
0xc022001c | A required pointer is null.\r\n
0xc022001d | An enumerator is not valid.\r\n
0xc022001e | The flags field contains an invalid value.\r\n
0xc022001f | A network mask is not valid.\r\n
0xc0220020 | An FWP_RANGE is not valid.\r\n
0xc0220021 | The time interval is not valid.\r\n
0xc0220022 | An array that must contain at least one element is zero length.\r\n
0xc0220023 | The displayData.name field cannot be null.\r\n
0xc0220024 | The action type is not one of the allowed action types for a filter.\r\n
0xc0220025 | The filter weight is not valid.\r\n
0xc0220026 | A filter condition contains a match type that is not compatible with the operands.\r\n
0xc0220027 | An FWP_VALUE or FWPM_CONDITION_VALUE is of the wrong type.\r\n
0xc0220028 | An integer value is outside the allowed range.\r\n
0xc0220029 | A reserved field is non-zero.\r\n
0xc022002a | A filter cannot contain multiple conditions operating on a single field.\r\n
0xc022002b | A policy cannot contain the same keying module more than once.\r\n
0xc022002c | The action type is not compatible with the layer.\r\n
0xc022002d | The action type is not compatible with the sublayer.\r\n
0xc022002e | The raw context or the provider context is not compatible with the layer.\r\n
0xc022002f | The raw context or the provider context is not compatible with the callout.\r\n
0xc0220030 | The authentication method is not compatible with the policy type.\r\n
0xc0220031 | The Diffie-Hellman group is not compatible with the policy type.\r\n
0xc0220032 | An IKE policy cannot contain an Extended Mode policy.\r\n
0xc0220033 | The enumeration template or subscription will never match any objects.\r\n
0xc0220034 | The provider context is of the wrong type.\r\n
0xc0220035 | The parameter is incorrect.\r\n
0xc0220036 | The maximum number of sublayers has been reached.\r\n
0xc0220037 | The notification function for a callout returned an error.\r\n
0xc0220038 | The IPsec authentication transform is not valid.\r\n
0xc0220039 | The IPsec cipher transform is not valid.\r\n
0xc022003a | The IPsec cipher transform is not compatible with the policy.\r\n
0xc022003b | The combination of IPsec transform types is not valid.\r\n
0xc022003c | A policy cannot contain the same auth method more than once.\r\n
0xc0220100 | The TCP/IP stack is not ready.\r\n
0xc0220101 | The injection handle is being closed by another thread.\r\n
0xc0220102 | The injection handle is stale.\r\n
0xc0220103 | The classify cannot be pended.\r\n
0xc0220104 | The packet should be dropped, no ICMP should be sent.\r\n
0xc0230002 | The binding to the network interface is being closed.\r\n
0xc0230004 | An invalid version was specified.\r\n
0xc0230005 | An invalid characteristics table was used.\r\n
0xc0230006 | Failed to find the network interface or network interface is not ready.\r\n
0xc0230007 | Failed to open the network interface.\r\n
0xc0230008 | Network interface has encountered an internal unrecoverable failure.\r\n
0xc0230009 | The multicast list on the network interface is full.\r\n
0xc023000a | An attempt was made to add a duplicate multicast address to the list.\r\n
0xc023000b | At attempt was made to remove a multicast address that was never added.\r\n
0xc023000c | Netowork interface aborted the request.\r\n
0xc023000d | Network interface can not process the request because it is being reset.\r\n
0xc023000f | An attempt was made to send an invalid packet on a network interface.\r\n
0xc0230010 | The specified request is not a valid operation for the target device.\r\n
0xc0230011 | Network interface is not ready to complete this operation.\r\n
0xc0230014 | The length of the buffer submitted for this operation is not valid.\r\n
0xc0230015 | The data used for this operation is not valid.\r\n
0xc0230016 | The length of buffer submitted for this operation is too small.\r\n
0xc0230017 | Network interface does not support this OID (Object Identifier)\r\n
0xc0230018 | The network interface has been removed.\r\n
0xc0230019 | Network interface does not support this media type.\r\n
0xc023001a | An attempt was made to remove a token ring group address that is in use by other components.\r\n
0xc023001b | An attempt was made to map a file that can not be found.\r\n
0xc023001c | An error occured while NDIS tried to map the file.\r\n
0xc023001d | An attempt was made to map a file that is alreay mapped.\r\n
0xc023001e | An attempt to allocate a hardware resource failed because the resource is used by another component.\r\n
0xc023001f | The I/O operation failed because network media is disconnected or wireless access point is out of range.\r\n
0xc0230022 | The network address used in the request is invalid.\r\n
0xc023002a | The offload operation on the network interface has been paused.\r\n
0xc023002b | Network interface was not found.\r\n
0xc023002c | The revision number specified in the structure is not supported.\r\n
0xc023002d | The specified port does not exist on this network interface.\r\n
0xc023002e | The current state of the specified port on this network interface does not support the requested operation.\r\n
0xc023002f | The miniport adapter is in lower power state.\r\n
0xc02300bb | Netword interface does not support this request.\r\n
0xc023100f | The TCP connection is not offloadable because of a local policy setting.\r\n
0xc0231012 | The TCP connection is not offloadable by the Chimney offload target.\r\n
0xc0231013 | The IP Path object is not in an offloadable state.\r\n
0xc0232000 | The wireless local area network interface is in auto configuration mode and doesn't support the requested parameter change operation.\r\n
0xc0232001 | The wireless local area network interface is busy and can not perform the requested operation.\r\n
0xc0232002 | The wireless local area network interface is power down and doesn't support the requested operation.\r\n
0xc0232003 | The list of wake on LAN patterns is full.\r\n
0xc0232004 | The list of low power protocol offloads is full.\r\n
0xc0350002 | The hypervisor does not support the operation because the specified hypercall code is not supported.\r\n
0xc0350003 | The hypervisor does not support the operation because the encoding for the hypercall input register is not supported.\r\n
0xc0350004 | The hypervisor could not perform the operation beacuse a parameter has an invalid alignment.\r\n
0xc0350005 | The hypervisor could not perform the operation beacuse an invalid parameter was specified.\r\n
0xc0350006 | Access to the specified object was denied.\r\n
0xc0350007 | The hypervisor could not perform the operation because the partition is entering or in an invalid state.\r\n
0xc0350008 | The operation is not allowed in the current state.\r\n
0xc0350009 | The hypervisor does not recognize the specified partition property.\r\n
0xc035000a | The specified value of a partition property is out of range or violates an invariant.\r\n
0xc035000b | There is not enough memory in the hypervisor pool to complete the operation.\r\n
0xc035000c | The maximum partition depth has been exceeded for the partition hierarchy.\r\n
0xc035000d | A partition with the specified partition Id does not exist.\r\n
0xc035000e | The hypervisor could not perform the operation because the specified VP index is invalid.\r\n
0xc0350011 | The hypervisor could not perform the operation because the specified port identifier is invalid.\r\n
0xc0350012 | The hypervisor could not perform the operation because the specified connection identifier is invalid.\r\n
0xc0350013 | Not enough buffers were supplied to send a message.\r\n
0xc0350014 | The previous virtual interrupt has not been acknowledged.\r\n
0xc0350016 | The previous virtual interrupt has already been acknowledged.\r\n
0xc0350017 | The indicated partition is not in a valid state for saving or restoring.\r\n
0xc0350018 | The hypervisor could not complete the operation because a required feature of the synthetic interrupt controller (SynIC) was disabled.\r\n
0xc0350019 | The hypervisor could not perform the operation because the object or value was either already in use or being used for a purpose that would not permit completing the operation.\r\n
0xc035001a | The proximity domain information is invalid.\r\n
0xc035001b | An attempt to retrieve debugging data failed because none was available.\r\n
0xc035001c | The physical connection being used for debuggging has not recorded any receive activity since the last operation.\r\n
0xc035001d | There are not enough resources to complete the operation.\r\n
0xc035001e | A hypervisor feature is not available to the user.\r\n
0xc0351000 | No hypervisor is present on this system.\r\n
0xc0360001 | The SPI in the packet does not match a valid IPsec SA.\r\n
0xc0360002 | Packet was received on an IPsec SA whose lifetime has expired.\r\n
0xc0360003 | Packet was received on an IPsec SA that does not match the packet characteristics.\r\n
0xc0360004 | Packet sequence number replay check failed.\r\n
0xc0360005 | IPsec header and/or trailer in the packet is invalid.\r\n
0xc0360006 | IPsec integrity check failed.\r\n
0xc0360007 | IPsec dropped a clear text packet.\r\n
0xc0360008 | IPsec dropped an incoming ESP packet in authenticated firewall mode. This drop is benign.\r\n
0xc0360009 | IPsec dropped a packet due to DoS throttling.\r\n
0xc0368000 | IPsec DoS Protection matched an explicit block rule.\r\n
0xc0368001 | IPsec DoS Protection received an IPsec specific multicast packet which is not allowed.\r\n
0xc0368002 | IPsec DoS Protection received an incorrectly formatted packet.\r\n
0xc0368003 | IPsec DoS Protection failed to look up state.\r\n
0xc0368004 | IPsec DoS Protection failed to create state because the maximum number of entries allowed by policy has been reached.\r\n
0xc0368005 | IPsec DoS Protection received an IPsec negotiation packet for a keying module which is not allowed by policy.\r\n
0xc0368006 | IPsec DoS Protection failed to create a per internal IP rate limit queue because the maximum number of queues allowed by policy has been reached.\r\n
0xc0370001 | The handler for the virtualization infrastructure driver is already registered. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370002 | The number of registered handlers for the virtualization infrastructure driver exceeded the maximum. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370003 | The message queue for the virtualization infrastructure driver is full and cannot accept new messages. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370004 | No handler exists to handle the message for the virtualization infrastructure driver. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370005 | The name of the partition or message queue for the virtualization infrastructure driver is invalid. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370006 | The partition name of the virtualization infrastructure driver exceeds the maximum.\r\n
0xc0370007 | The message queue name of the virtualization infrastructure driver exceeds the maximum.\r\n
0xc0370008 | Cannot create the partition for the virtualization infrastructure driver because another partition with the same name already exists.\r\n
0xc0370009 | The virtualization infrastructure driver has encountered an error. The requested partition does not exist. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc037000a | The virtualization infrastructure driver has encountered an error. Could not find the requested partition. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc037000b | A message queue with the same name already exists for the virtualization infrastructure driver.\r\n
0xc037000c | The memory block page for the virtualization infrastructure driver cannot be mapped because the page map limit has been reached. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc037000d | The memory block for the virtualization infrastructure driver is still being used and cannot be destroyed.\r\n
0xc037000e | Cannot unlock the page array for the guest operating system memory address because it does not match a previous lock request. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc037000f | The non-uniform memory access (NUMA) node settings do not match the system NUMA topology. In order to start the virtual machine, you will need to modify the NUMA configuration. For detailed information, see http://go.microsoft.com/fwlink/?LinkId=92362.\r\n
0xc0370010 | The non-uniform memory access (NUMA) node index does not match a valid index in the system NUMA topology.\r\n
0xc0370011 | The memory block for the virtualization infrastructure driver is already associated with a message queue.\r\n
0xc0370012 | The handle is not a valid memory block handle for the virtualization infrastructure driver.\r\n
0xc0370013 | The request exceeded the memory block page limit for the virtualization infrastructure driver. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370014 | The handle is not a valid message queue handle for the virtualization infrastructure driver.\r\n
0xc0370015 | The handle is not a valid page range handle for the virtualization infrastructure driver.\r\n
0xc0370016 | Cannot install client notifications because no message queue for the virtualization infrastructure driver is associated with the memory block.\r\n
0xc0370017 | The request to lock or map a memory block page failed because the virtualization infrastructure driver memory block limit has been reached. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370018 | The handle is not a valid parent partition mapping handle for the virtualization infrastructure driver.\r\n
0xc0370019 | Notifications cannot be created on the memory block because it is use.\r\n
0xc037001a | The message queue for the virtualization infrastructure driver has been closed. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc037001b | Cannot add a virtual processor to the partition because the maximum has been reached.\r\n
0xc037001c | Cannot stop the virtual processor immediately because of a pending intercept.\r\n
0xc037001d | Invalid state for the virtual processor. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc037001e | The maximum number of kernel mode clients for the virtualization infrastructure driver has been reached. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc037001f | This kernel mode interface for the virtualization infrastructure driver has already been initialized. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370020 | Cannot set or reset the memory block property more than once for the virtualization infrastructure driver. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370021 | The memory mapped I/O for this page range no longer exists. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370022 | The lock or unlock request uses an invalid guest operating system memory address. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370023 | Cannot destroy or reuse the reserve page set for the virtualization infrastructure driver because it is in use. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370024 | The reserve page set for the virtualization infrastructure driver is too small to use in the lock request. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370025 | Cannot lock or map the memory block page for the virtualization infrastructure driver because it has already been locked using a reserve page set page. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370026 | Cannot create the memory block for the virtualization infrastructure driver because the requested number of pages exceeded the limit. Restarting the virtual machine may fix the problem. If the problem persists, try restarting the physical computer.\r\n
0xc0370027 | Cannot restore this virtual machine because the saved state data cannot be read. Delete the saved state data and then try to start the virtual machine.\r\n
0xc0370028 | Cannot restore this virtual machine because an item read from the saved state data is not recognized. Delete the saved state data and then try to start the virtual machine.\r\n
0xc0370029 | Cannot restore this virtual machine to the saved state because of hypervisor incompatibility. Delete the saved state data and then try to start the virtual machine.\r\n
0xc0380001 | The configuration database is full.\r\n
0xc0380002 | The configuration data on the disk is corrupted.\r\n
0xc0380003 | The configuration on the disk is not insync with the in-memory configuration.\r\n
0xc0380004 | A majority of disks failed to be updated with the new configuration.\r\n
0xc0380005 | The disk contains non-simple volumes.\r\n
0xc0380006 | The same disk was specified more than once in the migration list.\r\n
0xc0380007 | The disk is already dynamic.\r\n
0xc0380008 | The specified disk id is invalid. There are no disks with the specified disk id.\r\n
0xc0380009 | The specified disk is an invalid disk. Operation cannot complete on an invalid disk.\r\n
0xc038000a | The specified disk(s) cannot be removed since it is the last remaining voter.\r\n
0xc038000b | The specified disk has an invalid disk layout.\r\n
0xc038000c | The disk layout contains non-basic partitions which appear after basic paritions. This is an invalid disk layout.\r\n
0xc038000d | The disk layout contains partitions which are not cylinder aligned.\r\n
0xc038000e | The disk layout contains partitions which are samller than the minimum size.\r\n
0xc038000f | The disk layout contains primary partitions in between logical drives. This is an invalid disk layout.\r\n
0xc0380010 | The disk layout contains more than the maximum number of supported partitions.\r\n
0xc0380011 | The specified disk is missing. The operation cannot complete on a missing disk.\r\n
0xc0380012 | The specified disk is not empty.\r\n
0xc0380013 | There is not enough usable space for this operation.\r\n
0xc0380014 | The force revectoring of bad sectors failed.\r\n
0xc0380015 | The specified disk has an invalid sector size.\r\n
0xc0380016 | The specified disk set contains volumes which exist on disks outside of the set.\r\n
0xc0380017 | A disk in the volume layout provides extents to more than one member of a plex.\r\n
0xc0380018 | A disk in the volume layout provides extents to more than one plex.\r\n
0xc0380019 | Dynamic disks are not supported on this system.\r\n
0xc038001a | The specified extent is already used by other volumes.\r\n
0xc038001b | The specified volume is retained and can only be extended into a contiguous extent. The specified extent to grow the volume is not contiguous with the specified volume.\r\n
0xc038001c | The specified volume extent is not within the public region of the disk.\r\n
0xc038001d | The specifed volume extent is not sector aligned.\r\n
0xc038001e | The specified parition overlaps an EBR (the first track of an extended partition on a MBR disks).\r\n
0xc038001f | The specified extent lengths cannot be used to construct a volume with specified length.\r\n
0xc0380020 | The system does not support fault tolerant volumes.\r\n
0xc0380021 | The specified interleave length is invalid.\r\n
0xc0380022 | There is already a maximum number of registered users.\r\n
0xc0380023 | The specified member is already in-sync with the other active members. It does not need to be regenerated.\r\n
0xc0380024 | The same member index was specified more than once.\r\n
0xc0380025 | The specified member index is greater or equal than the number of members in the volume plex.\r\n
0xc0380026 | The specified member is missing. It cannot be regenerated.\r\n
0xc0380027 | The specified member is not detached. Cannot replace a member which is not detached.\r\n
0xc0380028 | The specified member is already regenerating.\r\n
0xc0380029 | All disks belonging to the pack failed.\r\n
0xc038002a | There are currently no registered users for notifications. The task number is irrelevant unless there are registered users.\r\n
0xc038002b | The specified notification user does not exist. Failed to unregister user for notifications.\r\n
0xc038002c | The notifications have been reset. Notifications for the current user are invalid. Unregister and re-register for notifications.\r\n
0xc038002d | The specified number of members is invalid.\r\n
0xc038002e | The specified number of plexes is invalid.\r\n
0xc038002f | The specified source and target packs are identical.\r\n
0xc0380030 | The specified pack id is invalid. There are no packs with the specified pack id.\r\n
0xc0380031 | The specified pack is the invalid pack. The operation cannot complete with the invalid pack.\r\n
0xc0380032 | The specified pack name is invalid.\r\n
0xc0380033 | The specified pack is offline.\r\n
0xc0380034 | The specified pack already has a quorum of healthy disks.\r\n
0xc0380035 | The pack does not have a quorum of healthy disks.\r\n
0xc0380036 | The specified disk has an unsupported partition style. Only MBR and GPT partition styles are supported.\r\n
0xc0380037 | Failed to update the disk's partition layout.\r\n
0xc0380038 | The specified plex is already in-sync with the other active plexes. It does not need to be regenerated.\r\n
0xc0380039 | The same plex index was specified more than once.\r\n
0xc038003a | The specified plex index is greater or equal than the number of plexes in the volume.\r\n
0xc038003b | The specified plex is the last active plex in the volume. The plex cannot be removed or else the volume will go offline.\r\n
0xc038003c | The specified plex is missing.\r\n
0xc038003d | The specified plex is currently regenerating.\r\n
0xc038003e | The specified plex type is invalid.\r\n
0xc038003f | The operation is only supported on RAID-5 plexes.\r\n
0xc0380040 | The operation is only supported on simple plexes.\r\n
0xc0380041 | The Size fields in the VM_VOLUME_LAYOUT input structure are incorrectly set.\r\n
0xc0380042 | There is already a pending request for notifications. Wait for the existing request to return before requesting for more notifications.\r\n
0xc0380043 | There is currently a transaction in process.\r\n
0xc0380044 | An unexpected layout change occurred outside of the volume manager.\r\n
0xc0380045 | The specified volume contains a missing disk.\r\n
0xc0380046 | The specified volume id is invalid. There are no volumes with the specified volume id.\r\n
0xc0380047 | The specified volume length is invalid.\r\n
0xc0380048 | The specified size for the volume is not a multiple of the sector size.\r\n
0xc0380049 | The operation is only supported on mirrored volumes.\r\n
0xc038004a | The specified volume does not have a retain partition.\r\n
0xc038004b | The specified volume is offline.\r\n
0xc038004c | The specified volume already has a retain partition.\r\n
0xc038004d | The specified number of extents is invalid.\r\n
0xc038004e | All disks participating to the volume must have the same sector size.\r\n
0xc038004f | The boot disk experienced failures.\r\n
0xc0380050 | The configuration of the pack is offline.\r\n
0xc0380051 | The configuration of the pack is online.\r\n
0xc0380052 | The specified pack is not the primary pack.\r\n
0xc0380053 | All disks failed to be updated with the new content of the log.\r\n
0xc0380054 | The specified number of disks in a plex is invalid.\r\n
0xc0380055 | The specified number of disks in a plex member is invalid.\r\n
0xc0380056 | The operation is not supported on mirrored volumes.\r\n
0xc0380057 | The operation is only supported on simple and spanned plexes.\r\n
0xc0380058 | The pack has no valid log copies.\r\n
0xc0380059 | A primary pack is already present.\r\n
0xc038005a | The specified number of disks is invalid.\r\n
0xc038005b | The system does not support mirrored volumes.\r\n
0xc038005c | The system does not support RAID-5 volumes.\r\n
0xc0390002 | Entries enumerated have exceeded the allowed threshold.\r\n
0xc03a0001 | The virtual hard disk is corrupted. The virtual hard disk drive footer is missing.\r\n
0xc03a0002 | The virtual hard disk is corrupted. The virtual hard disk drive footer checksum does not match the on-disk checksum.\r\n
0xc03a0003 | The virtual hard disk is corrupted. The virtual hard disk drive footer in the virtual hard disk is corrupted.\r\n
0xc03a0004 | The system does not recognize the file format of this virtual hard disk.\r\n
0xc03a0005 | The version does not support this version of the file format.\r\n
0xc03a0006 | The virtual hard disk is corrupted. The sparse header checksum does not match the on-disk checksum.\r\n
0xc03a0007 | The system does not support this version of the virtual hard disk.This version of the sparse header is not supported.\r\n
0xc03a0008 | The virtual hard disk is corrupted. The sparse header in the virtual hard disk is corrupt.\r\n
0xc03a0009 | Failed to write to the virtual hard disk failed because the system failed to allocate a new block in the virtual hard disk.\r\n
0xc03a000a | The virtual hard disk is corrupted. The block allocation table in the virtual hard disk is corrupt.\r\n
0xc03a000b | The system does not support this version of the virtual hard disk. The block size is invalid.\r\n
0xc03a000c | The virtual hard disk is corrupted. The block bitmap does not match with the block data present in the virtual hard disk.\r\n
0xc03a000d | The chain of virtual hard disks is broken. The system cannot locate the parent virtual hard disk for the differencing disk.\r\n
0xc03a000e | The chain of virtual hard disks is corrupted. There is a mismatch in the identifiers of the parent virtual hard disk and differencing disk.\r\n
0xc03a000f | The chain of virtual hard disks is corrupted. The time stamp of the parent virtual hard disk does not match the time stamp of the differencing disk.\r\n
0xc03a0010 | Failed to read the metadata of the virtual hard disk.\r\n
0xc03a0011 | Failed to write to the metadata of the virtual hard disk.\r\n
0xc03a0012 | The size of the virtual hard disk is not valid.\r\n
0xc03a0013 | The file size of this virtual hard disk is not valid.\r\n
0xc03a0014 | A virtual disk support provider for the specified file was not found.\r\n
0xc03a0015 | The specified disk is not a virtual disk.\r\n
0xc03a0016 | The chain of virtual hard disks is inaccessible. The process has not been granted access rights to the parent virtual hard disk for the differencing disk.\r\n
0xc03a0017 | The chain of virtual hard disks is corrupted. There is a mismatch in the virtual sizes of the parent virtual hard disk and differencing disk.\r\n
0xc03a0018 | The chain of virtual hard disks is corrupted. A differencing disk is indicated in its own parent chain.\r\n
0xc03a0019 | The chain of virtual hard disks is inaccessible. There was an error opening a virtual hard disk further up the chain.\r\n
0xc03a001a | The requested operation could not be completed due to a virtual disk system limitation.  Virtual disks are only supported on NTFS volumes and must be both uncompressed and unencrypted.\r\n
0xc03a001b | The requested operation cannot be performed on a virtual disk of this type.\r\n
0xc03a001c | The requested operation cannot be performed on the virtual disk in its current state.\r\n
0xc03a001d | The sector size of the physical disk on which the virtual disk resides is not supported.\r\n
0xc03c0001 | The Derived Indexed Store is not present (or currently loaded) on this system.\r\n
0xc03c0002 | The Attribute was not found in the store for a given object.\r\n
0xc03c0003 | This is not a recognized built-in attribute.\r\n
0xc03c0004 | Partial data was successfully returned, some attributes need to be calculated from elsewhere.\r\n
