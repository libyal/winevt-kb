## sensorsutilsv2.dll

Path: %SystemRoot%\system32\SensorsUtilsV2.dll

### 10.0.17763.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0xd0000001 | Start\r\n
0xd0000002 | Stop\r\n
0xd0000003 | GetSupportedDatafields\r\n
0xd0000004 | GetProperties\r\n
0xd0000005 | GetDatafieldProperties\r\n
0xd0000006 | GetDataInterval\r\n
0xd0000007 | SetDataInterval\r\n
0xd0000008 | GetDataThresholds\r\n
0xd0000009 | SetDataThresholds\r\n
0xd000000a | UpdateDeclination\r\n
0xd000000b | StartHistory\r\n
0xd000000c | StopHistory\r\n
0xd000000d | ClearHistory\r\n
0xd000000e | GetHistory\r\n
0xd000000f | SetReportLatency\r\n
0xd0000010 | GetDataDeliveryMode\r\n
0xd0000011 | GetReportLatency\r\n
0xd0000012 | GetBatchedSamples\r\n
0xd0000013 | GetDefaultDataThresholds\r\n

### 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x51000002 | Error\r\n
0x51000003 | Warning\r\n
0x51000004 | Information\r\n
0xb10003e9 | [SensorsCx] Sensor Class extension failed to initalize file context policy for DeviceInit (%1). 'UmdfFsContextUsePolicy' is not set to 'CannotUseFsContexts'\r\n
0xb10003ea | [SensorsCx] Device (%1) does not implement all required sensor DDI callbacks\r\n
0xb10003eb | [SensorsCx] Device (%1) Supports state change notification=(%2)\r\n
0xb10003ec | [SensorsCx] Device (%1) is power policy owner=(%2)\r\n
0xb10003ed | [SensorsCx] Sensor (%2) exposed by Device (%1) supports SensorType=(%3) with PersistentUniqueID=(%4)\r\n
0xb10003ee | [SensorsCx] Custom Sensor (%2) exposed by Device (%1) with SubType=(%2) and PersistentUniqueID=(%3)\r\n
0xb10003ef | [SensorsCx] Sensor (%2) with PersistentUniqueID=(%3) exposed by Device=(%1) missing vendor defined sub type\r\n
0xb10003f0 | [SensorsCx] Published device interface of Class=(%3) with ReferenceString=(%4) for Sensor (%2) exposed by Device (%1)\r\n
0xb10003f1 | [SensorsCx] Sensor Category missing in Sensor (%1)\r\n
0xb10003f2 | [SensorsCx] Found Enumeration Property({%3}-%4) in Sensor (%2) exposed by Device (%1)\r\n
0xb10003f3 | [SensorsCx] Default Report Interval (%3) in Sensor (%2) exposed by Device (%1) is <= 1ms\r\n
0xb10003f4 | [SensorsCx] Minimum Report Interval (%3) in Sensor (%2) exposed by Device (%1) is 0\r\n
0xb10003f5 | [SensorsCx] MaxDataSize (%3) in Sensor (%2) exposed by Device (%1) is <= sizeof(SENSOR_COLLECTION_LIST)\r\n
0xb10003f6 | [SensorsCx] PKEY_Sensor_MaximumDataFieldSize_Bytes value=(%3) in Sensor (%2) exposed by Device (%1) is incorrect. Please  use CollectionsListGetMarshalledSize() instead of SENSOR_COLLECTION_LIST_SIZE() to compute the value for that property.\r\n
0xb10003f7 | [SensorsCx] Batch Size (%3) in Sensor (%2) exposed by Device (%1) is more than the maximum amount\r\n
0xb10003f8 | [SensorsCx] PKEY_SensorData_SupportedActivityStates not exposed by activity sensor\r\n
0xb10003f9 | [SensorsCx] PKEY_Sensor_Power_Milliwatts not exposed by activity sensor\r\n
0xb10003fa | [SensorsCx] PKEY_SensorData_SupportedStepTypes not exposed by pedometer\r\n
0xb10003fb | [SensorsCx] Get Data Interval DDI call failed with NTSTATUS=(%4) [Device=(%1) Sensor=(%2) pIntervalMs=(%3)]\r\n
0xb10003fc | [SensorsCx] Set Data Interval DDI call failed with NTSTATUS=(%4) [Device=(%1) Sensor=(%2) IntervalMs=(%3)]\r\n
0xb10003fd | [SensorsCx] Get Data Thresholds DDI call failed with NTSTATUS=(%5) [Device=(%1) Sensor=(%2) pThresholds=(%3) pSize=(%4)]\r\n
0xb10003fe | [SensorsCx] Set Data Thresholds DDI call failed with NTSTATUS=(%4) [Device=(%1) Sensor=(%2) pThresholds=(%3)]\r\n
0xb10003ff | [SensorsCx] Get Properties DDI call failed with NTSTATUS=(%5) [Device=(%1) Sensor=(%2) pProperties=(%3) pSize=(%4)]\r\n
0xb1000400 | [SensorsCx] Get Supported Datafields DDI call failed with NTSTATUS=(%5) [Device=(%1) Sensor=(%2) pDatafields=(%3) pSize=(%4)]\r\n
0xb1000401 | [SensorsCx] Get Datafield Properties DDI call failed with NTSTATUS=(%6) [Device=(%1) Sensor=(%2) pDatafield=(%3) pProperties=(%4) pSize=(%5)]\r\n
0xb1000402 | [SensorsCx] Start Sensor DDI call failed with NTSTATUS=(%3) [Device=(%1) Sensor=(%2)]\r\n
0xb1000403 | [SensorsCx] Stop Sensor DDI call failed with NTSTATUS=(%3) [Device=(%1) Sensor=(%2)]\r\n
0xb1000404 | [SensorsCx] Start Sensor History DDI call failed with NTSTATUS=(%3) [Device=(%1) Sensor=(%2)]\r\n
0xb1000405 | [SensorsCx] Stop Sensor History DDI call failed with NTSTATUS=(%3) [Device=(%1) Sensor=(%2)]\r\n
0xb1000406 | [SensorsCx] Start Sensor History DDI call failed with NTSTATUS=(%5) [Device=(%1) Sensor=(%2) pHistoryCollection=(%3) Size=(%4)]\r\n
0xb1000407 | [SensorsCx] Start Sensor History DDI call failed with NTSTATUS=(%4) [Device=(%1) Sensor=(%2) pSize=(%3)]\r\n
0xb1000408 | [SensorsCx] Clear Sensor History DDI call failed with NTSTATUS=(%3) [Device=(%1) Sensor=(%2)]\r\n
0xb1000409 | [SensorsCx] Start Set Report Latency DDI call failed with NTSTATUS=(%4) [Device=(%1) Sensor=(%2) ReportLatencyMs=(%3)]\r\n
0xb100040a | [SensorsCx] Enable Wake DDI call failed with NTSTATUS=(%3) [Device=(%1) Sensor=(%2)]\r\n
0xb100040b | [SensorsCx] Disable Wake DDI call failed with NTSTATUS=(%3) [Device=(%1) Sensor=(%2)]\r\n
0xb100040c | [SensorsCx] Sensor Rundown: Device=(%1) Sensor=(%2) Type=(%3) Category=(%4) SubType=(%5) UniqueId=(%6) Name=(%7) Model=(%8) Manufacturer=(%9)\r\n
0xb100044c | [SensorsCx] Sensor Subscriber Rundown: UniqueId=(%1) ProcessId=(%2) ReportIntervalMs=(%3) ReportLatency=(%4) IsStreaming=(%5)\r\n
0xb100044d | [Sensors] Found Interface=(%1)\r\n
0xb100044e | [Sensors] Picked Interface=(%1) as the default interface\r\n
0xb100044f | [Sensors] Interface=(%1) marked as primary\r\n
0xb1000450 | [Sensors] Interface=(%1) marked as integrated\r\n
0xb1000451 | [Sensors] Interface=(%1) has power usage set to (%2)\r\n
0xb1000452 | [Sensors] Interface=(%1) marked as supporting history\r\n
0xb1000453 | [Sensors] Interface=(%1) marked as Auto-brightness preferred\r\n
0xb1000454 | [Sensors] Interface=(%1) marked as color capable\r\n
0xb10004b0 | [SensorsHid] Found Sensor=(%2) WdfDevice=(%1)\r\n
0xb10004b1 | [SensorsHid] Skipping unsupported Sensor=(%2) WdfDevice=(%1)\r\n
0xb10004b2 | [SensorsHid] Incorrect Report ID found in capabilities and reports of Sensor=(%2) don't match. Report ID found on capabilities is (%3). Report ID found on report is (%4). WdfDevice=(%1)\r\n
0xb10004b3 | [SensorsHid] Sensor=(%2) with ReportId=(%3) supports history. WdfDevice=(%1)\r\n
0xb10004b4 | [SensorsHid] Feature Usage=(%4) reported by Sensor=(%2) with ReportId=(%3) must be a selector usage. WdfDevice=(%1)\r\n
0xb10004b5 | [SensorsHid] Datafield {%5-%6} was added for input Usage=(%4) reported by Sensor=(%2) with ReportId=(%3) must be a selector usage. WdfDevice=(%1)\r\n
0xb10004b6 | [SensorsHid] Property {%5-%6} was added for input Usage=(%4) reported by Sensor=(%2) with ReportId=(%3) must be a selector usage. WdfDevice=(%1)\r\n
0xb10004b7 | [SensorsHid] Threshold {%5-%6} was added for input Usage=(%4) reported by Sensor=(%2) with ReportId=(%3) must be a selector usage. WdfDevice=(%1)\r\n
0xb10004b8 | [SensorsHid] Timestamp usage reported by Sensor=(%2) with ReportId=(%3) is ignored since it does not have right capabilities. (Expected Report Size=%4) (Actual Report Size=%5) (Expected Report Count=%6) (Actual Report Count=%7) (Expected Exponent=%8) (Actual Exponent=%9). WdfDevice=(%1)\r\n
0xb10004b9 | [SensorsHid] Report Interval is supported by Sensor=(%2) with ReportId=(%3). WdfDevice=(%1)\r\n
0xb10004ba | [SensorsHid] Report Interval is missing in Sensor=(%2) with ReportId=(%3). WdfDevice=(%1)\r\n
0xb10004bb | [SensorsHid] Reporting State is supported by Sensor=(%2) with ReportId=(%3). WdfDevice=(%1)\r\n
0xb10004bc | [SensorsHid] Reporting State is missing in Sensor=(%2) with ReportId=(%3). WdfDevice=(%1)\r\n
0xb10004bd | [SensorsHid] Power State is supported by Sensor=(%2) with ReportId=(%3). WdfDevice=(%1)\r\n
0xb10004be | [SensorsHid] Power State is missing in Sensor=(%2) with ReportId=(%3). WdfDevice=(%1)\r\n
0xb10004bf | [SensorsHid] Report Latency is supported by Sensor=(%2) with ReportId=(%3). WdfDevice=(%1)\r\n
0xb10004c0 | [SensorsHid] Report Latency is marked as not supported by Sensor=(%2) with ReportId=(%3) since timestamp is missing. WdfDevice=(%1)\r\n
0xb10004c1 | [SensorsHid] Sensor State is supported by Sensor=(%2) with ReportId=(%3). WdfDevice=(%1)\r\n
0xb10004c2 | [SensorsHid] Wake is supported by Sensor=(%2) with ReportId=(%3). WdfDevice=(%1)\r\n
0xb10004c3 | [SensorsHid] IsWakeReportingStateSupported=(%4) and IsWakePowerStateSupported=(%5). Wake is not supported by Sensor=(%2) with ReportId=(%3). WdfDevice=(%1)\r\n
0xb10004c4 | [SensorsHid] Incorrect Report ID found in report (%2). WdfDevice=(%1)\r\n
0xb10004c5 | [SensorsHid] Failed to get input report from Sensor=(%2) with ReportId=(%3) NTSTATUS=(%4). WdfDevice=(%1)\r\n
0xb10004c6 | [SensorsHid] Failed to get feature report from Sensor=(%2) with ReportId=(%3) NTSTATUS=(%4). WdfDevice=(%1)\r\n
0xb10004c7 | [SensorsHid] Failed to set feature report from Sensor=(%2) with ReportId=(%3) NTSTATUS=(%4). WdfDevice=(%1)\r\n
0xb10004c8 | [SensorsHid] Sensor=(%2) with ReportId=(%3) is color capable. WdfDevice=(%1)\r\n
0xb1000514 | [SensorsHid] Using Accelerometer=(%1) to create Software SDO\r\n
0xb1000515 | [SensorsHid] Using Hardware Offloaded SDO=(%1) to create hardware SDO\r\n
0xb1000516 | [SensorsHid] Removing SDO based on sensor=(%1)\r\n
0xd0000001 | Start\r\n
0xd0000002 | Stop\r\n
0xd0000003 | GetSupportedDatafields\r\n
0xd0000004 | GetProperties\r\n
0xd0000005 | GetDatafieldProperties\r\n
0xd0000006 | GetDataInterval\r\n
0xd0000007 | SetDataInterval\r\n
0xd0000008 | GetDataThresholds\r\n
0xd0000009 | SetDataThresholds\r\n
0xd000000a | UpdateDeclination\r\n
0xd000000b | StartHistory\r\n
0xd000000c | StopHistory\r\n
0xd000000d | ClearHistory\r\n
0xd000000e | GetHistory\r\n
0xd000000f | SetReportLatency\r\n
0xd0000010 | GetDataDeliveryMode\r\n
0xd0000011 | GetReportLatency\r\n
0xd0000012 | GetBatchedSamples\r\n
0xd0000013 | GetDefaultDataThresholds\r\n
