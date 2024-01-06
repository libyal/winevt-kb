## comsvcs.dll

Path: %SystemRoot%\System32\COMSVCS.DLL

### 2000.2.3504.0

Message identifier | Message string
--- | ---
0x00000001 | SVC%0\r\n
0x00000002 | Executive%0\r\n
0x00000003 | Catalog%0\r\n
0x00000004 | SPM%0\r\n
0x00000005 | QC Recorder%0\r\n
0x00000006 | QC ListenerHelper%0\r\n
0x00000007 | QC Player%0\r\n
0x00000008 | QC Listener%0\r\n
0x00000009 | CRM%0\r\n
0x0000000a | Security%0\r\n
0x0000000b | Activation%0\r\n
0x0000000c | BYOT%0\r\n
0x0000000d | QC Queue Admin%0\r\n
0x0000000e | Queue Moniker%0\r\n
0x0000000f | MTS 2.0 Migration%0\r\n
0x00000010 | External%0\r\n
0x00000011 | Events%0\r\n
0x00000012 | QC Marshal%0\r\n
0x00000013 | QC MSMQ Runtime%0\r\n
0x00000014 | New Moniker%0\r\n
0x00000015 | <>%0\r\n
0x40001006 | The mtstocom launching routine has started.%1%0\r\n
0x40001007 | The mtstocom launching routine has completed.%1%0\r\n
0x40001008 | The MTSTOCOM migration utility is attempting to retry populating the packages collection because it failed it's first attempt.%1%0\r\n
0x40021003 | A new CRM log file was created. This CRM log file is not secure because the application Identity is Interactive User or the file system is not NTFS. %1%0\r\n
0x40021004 | A new CRM log file was created. This CRM log file is secure. %1%0\r\n
0x40021005 | A new CRM log file was created for the System Application.%0\r\n
0x80001001 | An error occurred in your COM+ component.  %1%0\r\n
0x80001002 | A method call to an object in a COM+ application was rejected because the caller is not properly authorized to make this call. The COM+ application is configured to use Application and Component level access checks, and enforcement of these checks is currently enabled. The remainder of this message provides information about the component method that the caller attempted to invoke and the identity of the caller.%1%0\r\n
0x80001003 | A method call to an object in a COM+ application was rejected because the caller is not properly authorized to make this call. The COM+ application is configured to use Application and Component level access checks, and enforcement of these checks is currently enabled. Information about the component method that the caller attempted to invoke and about the identity of the caller could not be obtained, probably due to low memory conditions on this computer.%0\r\n
0x80001014 | Failures reported during migration of MTS packages and program settings to COM+ applications and program settings. See the mtstocom.log file in the windows directory for more information.%1%0\r\n
0x80021008 | The CRM log file was originally created on a computer with a different name. It has been updated with the name of the current computer. If this warning appears when the computer name has been changed then no further action is required. %1%0\r\n
0x80021009 | The CRM log file was originally created with a different application ID. It has been updated with the current application ID. If this warning appears when the CRM log file has been renamed then no further action is required. %1%0\r\n
0x8002100a | A log information record was not found in the existing CRM log file. It has been added. If this warning appears when the CRM log file is being initially created then no further action is required. %1%0\r\n
0x8002100b | An unexpected method call was received. It has been safely ignored. Method Name: %1%0\r\n
0x8002100c | An empty CRM log file was detected. It has been re-initialized. If this warning appears when the CRM log file is being initially created then no further action is required. %1%0\r\n
0x8002100d | An incompletely initialized CRM log file was detected. It has been re-initialized. If this warning appears when the CRM log file is being initially created then no further action is required. %1%0\r\n
0x8002100e | The application attempted to use the CRM but the CRM is not enabled for this application. You can correct this problem using the Component Services administrative tool. Display the Properties for your application. Select the Advanced tab and check Enable Compensating Resource Managers. The CRM can only be enabled for server applications. %1%0\r\n
0x80021010 | Some transactions could not be completed because they are in-doubt. The CRM will attempt to complete them on its next recovery. %1%0\r\n
0x80021011 | The system has called the CRM Compensator custom component and that component has failed and generated an exception. This indicates a problem with the CRM Compensator component. Notify the developer of the CRM Compensator component that this failure has occurred. The system will continue because the IgnoreCompensatorErrors registry flag is set, but correct compensation might not have occurred. %1%0\r\n
0x80021012 | The system has called the CRM Compensator custom component and that component has returned an error. This indicates a problem with the CRM Compensator component. Notify the developer of the CRM Compensator component that this failure has occurred. The system will continue because the IgnoreCompensatorErrors registry flag is set, but correct compensation might not have occurred. %1%0\r\n
0x80021013 | The CRM log file for this application is located on a disk which is short of space. This may cause failures of this application. Please increase the space available on this disk. The CRM log file name is shown below.%1%0\r\n
0x80021015 | CRM Worker custom components require a transaction. You can correct this problem using the Component Services administrative tool. Display the Properties for your CRM Worker component. Select the Transactions tab. Select the Transaction support Required option button.%1%0\r\n
0x80021016 | Event class failed Query Interface. Please check the event log for any other errors from the EventSystem.%1%0\r\n
0x80021017 | Failed to create event class. Please check the event log for any other errors from the EventSystem.%1%0\r\n
0x80021018 | Event failed. Please check the event log for any other errors from the EventSystem.%1%0\r\n
0x80021019 | A previous instance of this server application has been terminated.%1%0\r\n
0x8002106c | COM+ Services was unable to lookup the local Administrator account and obtain its security identifier (SID). COM+ will continue to operate normally, but any calls between local and remote COM+ components will incur additional overhead. The error returned by LookupAccountName is shown below.%1%0\r\n
0x8002108b | A COM+ service (such as Queued Components or Compensating Resource Manager) failed an ApplicationFree event.  This is not a normal occurrence, but it is considered a non-critical error. The service GUID and HRESULT are: %1%0\r\n
0x8002108c | A COM+ service (such as Queued Components or Compensating Resource Manager) failed an ApplicationShutdown event.  This is not a normal occurrence, but it is considered a non-critical error. The service GUID and HRESULT are: %1%0\r\n
0x8002108e | COM+ has determined that your machine is running very low on available memory.  In order to ensure proper system behavior, the activation of the component has been refused.  If this problem continues, either install more memory or increase the size of your paging file.  Memory statistics are: %1%0\r\n
0x8002108f | COM+ failed an activation because the creation of a context property returned E_OUTOFMEMORY %1%0\r\n
0x80021092 | The shutdown process of COM+ surrogate failed because of an unknown ApplId. This is an unexpected error, but is ignored because the application is in the process of shutting down.%1%0\r\n
0x80021502 | An external error has been reported to COM+ services.%1%0\r\n
0x80021503 | The server process has lost its connection with MS DTC. This is expected if MS DTC has stopped, or if MS DTC failover has occurred on a cluster.%1%0\r\n
0xc0001068 | The current registration database is corrupt. COM+ catalog has reverted to a previous version of the database. %0\r\n
0xc0001083 | Error creating security descriptor. %0\r\n
0xc0001084 | Failed to initialize registration database server. %0\r\n
0xc0001085 | Failed to initialize registration database API. %0\r\n
0xc0001087 | COM Replication: An unexpected error occurred.  The function which failed is listed below. %1%0\r\n
0xc0021001 | The run-time environment has detected an inconsistency in its internal state. Please contact Microsoft Product Support Services to report this error.  %1%0\r\n
0xc0021002 | The run-time environment has detected the absence of a critical resource and has caused the process that hosted it to terminate.  %1%0\r\n
0xc0021003 | The run-time environment was unable to initialize for transactions required to support transactional components. Make sure that MS DTC is running.%1%0\r\n
0xc0021009 | Could not obtain a proxy/stub class factory for given interface. Proxy/stub is not registered correctly.  %1%0\r\n
0xc002100a | Failed to create a stub object for given interface.  %1%0\r\n
0xc0021024 | Replication: Invalid machine name supplied for %1.%0\r\n
0xc002104f | The clsid of the proxy stub dll for the interface is not available, or failed to load the proxy stub dll, or failed to create a proxy.%0\r\n
0xc0021051 | COM+ Queued Components: An unexpected error occurred. The failing function is listed below. The data section may have additional information.%1%0\r\n
0xc0021053 | COM+ QC failed to obtain necessary information from the catalog.%1%0\r\n
0xc0021057 | The listener has timed out waiting for the MSMQ service to start.  Therefore the process was terminated.%0\t\r\n
0xc0021062 | The system has called a custom component and that component has failed and generated an exception. This indicates a problem with the custom component. Notify the developer of this component that a failure has occurred and provide them with the information below. %1%2%0\r\n
0xc0021064 | An error occurred while checking to see if a queued message was sent by a trusted partner. The process may have insufficient privileges to call GetEffectiveRightsFromAcl. The HRESULT from this call is %1%0\r\n
0xc0021065 | The server was unable to determine if a queued message was sent by a trusted partner due to a lack of available memory. The sender is assumed to be untrusted. %1%0\r\n
0xc0021066 | The server was unable to determine if a queued message was sent by a trusted partner due to an unexpected failure in a Win32 API call. The sender is assumed to be untrusted. The failed API and corresponding error code are shown below. %1%0\r\n
0xc0021067 | The COM+ Services DLL (comsvcs.dll) was unable to load because allocation of thread local storage failed. %1%0\r\n
0xc002106a | COM+ Services was unable to load a required string resource. The string resource identifier was not found. This results from an error in the localization process for this product and should be reported to Microsoft customer support. The binary data for this event contains the resource identifier that failed to load. %1%0\r\n
0xc002106b | COM+ Services was unable to load a required string resource. The buffer supplied for the string was not large enough. This results from an error in the localization process for this product and should be reported to Microsoft customer support. The binary data for this event contains the resource identifier that failed to load.%1%0\r\n
0xc002106d | COM+ Services was unable to initialize due to a failure in the system API shown below. This is often caused by a shortage of system resources on the local machine.%1%0\r\n
0xc002106e | The system has called the CRM Compensator custom component and that component has failed and generated an exception. This indicates a problem with the CRM Compensator component. Notify the developer of the CRM Compensator component that this failure has occurred. %1%0\r\n
0xc002106f | The application cannot access the CRM log file because it is being used by another process. Most likely this is because another server process is running for the same application. Please check that no other server processes are running for this application and try again. If the condition persists, please contact Microsoft Product Support Services. %1%0\r\n
0xc0021070 | COM+ Services was unable to authorize the incoming call due to an unexpected failure. The incoming call was denied and a "permission denied" error was returned to the caller. The unexpected error code is shown below.%1%0\r\n
0xc0021071 | COM+ Services was unable to determine the caller's identity because of an unexpected error. This may be caused by a shortage of system resources on the local machine. The caller will be treated as anonymous which may result in access failures or other errors. The name of the failed API and the error code that it returned are shown below.%1%0\r\n
0xc0021072 | COM+ Services was unable to process a component's call to IsCallerInRole due to an unexpected failure. The unexpected error code (shown below) was returned to the caller.%1%0\r\n
0xc0021073 | The system has called the CRM Compensator custom component and that component has returned an error. This indicates a problem with the CRM Compensator component. Notify the developer of the CRM Compensator component that this failure has occurred. %1%0\r\n
0xc0021074 | The system failed to create the CRM Compensator custom component. %1%0\r\n
0xc0021075 | The system failed to create the CRM Compensator because the system is out of memory. %1%0\r\n
0xc0021076 | The QC Player detected an invalid QC message. The message will be moved to the deadqueue.%1%0\r\n
0xc0021077 | COM+ QC was unable to open or set thread token due to an unexpected failure in the system API shown below. (Make sure that there are no ACLs set on the thread.) %1%0\r\n
0xc0021078 | An unexpected error was returned by the MSMQ API function indicated. The following error message was retrieved from MSMQ.%1%0 \r\n
0xc002107a | The server was unable to determine if a queued message was sent by a trusted partner due to an unexpected failure in a COM+ catalog component. The sender is assumed to be untrusted. The failed catalog API and corresponding error code are shown below.%1%0\r\n
0xc002107b | An unexpected error was returned by the MSMQ API function indicated. An error occurred while retrieving the error message from MSMQ. MSMQ API function return values are defined in MSMQ header file MQ.H.%1%0 \r\n
0xc0021080 | The Synchronization property is required for the Transaction property. Activation failed for object: %1%0\r\n
0xc0021081 | The Synchronization property is required for the JIT property. Activation failed for object: %1%0\r\n
0xc0021082 | The following component is configured for Construction, and either the IObjectConstruct::Construct() method failed, or the component does not support IObjectConstruct. Activation failed for object: %1%0\r\n
0xc0021086 | COM+ Internal Error. Please contact Microsoft Product Support Services to report this error. Assertion Failure: %1%0\r\n
0xc0021089 | COM Queued Components: Output arguments are not supported by queued methods. Check the data section for IID and method ID.%1%0\r\n
0xc002108a | A COM+ service (such as Queued Components or Compensating Resource Manager) failed an ApplicationLaunch event.  If this problem continues, try disabling CRM and/or QC on your application. If you are using QC, make sure that MSMQ is installed. The service GUID and HRESULT are: %1%0\r\n
0xc002108d | A COM+ service (such as Queued Components or Compensating Resource Manager) failed to start. The service GUID and HRESULT are: %1%0\r\n
0xc0021090 | A request for a callback on a MTA thread failed. The only time this should happen is your machine is in a completely unstable state and you should reboot, or there is a bug in COM+.  If the problem is reproducible, please report this error to Microsoft. %1%0\r\n
0xc0021091 | The initialization of the COM+ surrogate failed -- the CApplication object failed to initialize.%1%0\r\n
0xc0021093 | The Byot Gateway failed to import the transaction using Tip. Make sure that the installed DTC supports the TIP protocol. %1%0\r\n
0xc0021094 | The Byot Gateway failed to create the component.%1%0\r\n
0xc0021095 | The Byot Gateway could not set transactional property in new object context.%1%0\r\n
0xc0021096 | The Byot Gateway could not delegate the activation. The component being created may be incorrectly configured. %1%0\r\n
0xc0021097 | The Byot Gateway component is incorrectly configured. %1%0\r\n
0xc0021098 | The IObjectControl::Activate() method failed.  The CLSID of the object is: %1%0\r\n
0xc0021099 | QC has detected an invalid Marshaled object. The message will be moved to the deadqueue.%1%0\r\n
0xc002109a | An unsupported object reference was used during a method call to a QC component.  The object reference should either be a QC recorder or support IPersistStream.%1%0\r\n
0xc002109b | The CRM has lost its connection with MS DTC. This is expected if MS DTC has stopped, or if MS DTC failover has occurred on a cluster.%1%0\r\n
0xc00210a0 | Unable to delete queue because it has messages.  Purge messages and try again.%1%0\r\n
0xc00210a1 | Queued Application has an obsolete catalog entry. Uncheck and check the Application's Queue property.%1%0\r\n
0xc00210a2 | Queued Application has an invalid catalog entry (Queue BLOB).%1%0\r\n
0xc00210a3 | MSMQ is unavailable.  QC requires MSMQ to be installed.  If no queued calls are made then simply turn off the listener and use DCOM calls.%1%0\r\n
0xc00210a4 | GetProcAddress on one of the MSMQ functions failed.  Please make sure that MSMQ is installed correctly.%1%0\r\n
0xc00210a5 | Unknown event id. Please check the event log for any other errors from the EventSystem.%1%0\r\n
0xc00210a6 | Unable to instantiate Exception Class.%1%0\r\n
0xc00210a7 | COM+ requires that ODBC version 2.0 or greater be installed on your machine.  The version of ODBC that ships with Windows 2000 is sufficient.  Please reinstall ODBC from your distribution media.%1%0\r\n
0xc00210a8 | COM+ was unable to set up the ODBC shared environment, which means that automatic transaction enlistment will not work.%1%0\r\n
0xc00210a9 | A CRM checkpoint has failed. Most likely this application is not configured correctly for use on the cluster. See the COM+ Compensating Resource Manager (CRM) documentation for details on how to fix this problem.%1%0\r\n
0xc00210aa | The threading model of the component specified in the registry is inconsistent with the registration database. The faulty component is: %1%0\r\n
0xc00210ab | CRM recovery has failed because MS DTC thinks that the previous instance of this application is still connected. This is a temporary condition which can occur if the system is too busy. Please attempt the CRM recovery again by restarting this application.%1%0\r\n
0xc00210ac | The CRM Compensator custom component has timed out out waiting for the CRM Worker custom component to complete. See the COM+ Compensating Resource Manager (CRM) documentation for further explanation of this error.%1%0\r\n
0xc00210ad | CRM recovery has failed because the device is not ready. This is a temporary condition which can occur during cluster failover. Please attempt the CRM recovery again by restarting this application.%1%0\r\n
0xc0021500 | This is the first external error message in this file. It is a marker only, never issued.%1%0\r\n
0xc0021501 | An external error has been reported to COM+ services.%1%0\r\n
0xc0021504 | COM+ could not create a new thread due to a low memory situation.%1%0\r\n
0xc0021505 | This is the last external error message in this file. It is a marker only, never issued.%1%0\r\n
