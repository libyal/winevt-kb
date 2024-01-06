## locationframework.dll

Path: %SystemRoot%\System32\locationframework.dll

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x00000001 | Geolocation positioning is enabled.\r\n
0x00000002 | Geolocation positioning has been disabled by the user.\r\n
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000003 | Selfhost\r\n
0x10000004 | WiFiTracing\r\n
0x10000005 | Init\r\n
0x10000006 | Position\r\n
0x10000007 | FixSession\r\n
0x10000008 | CompositePe\r\n
0x10000009 | Gnss\r\n
0x1000000a | CellPe\r\n
0x1000000b | WifiPe\r\n
0x1000000c | ClientApi\r\n
0x1000000d | Orion\r\n
0x1000000e | Supl\r\n
0x1000000f | Crowdsource\r\n
0x10000010 | ManagedApi\r\n
0x10000011 | GeofenceTracing\r\n
0x10000012 | GeofenceStore\r\n
0x1000001c | WebproxyTracing\r\n
0x1000001e | CellPeAdvanceTracing\r\n
0x1000001f | SpeedEstimatorTracing\r\n
0x10000020 | VenuePE\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | LocationServiceProvider\r\n
0x90000002 | Debug\r\n
0xb000000d | WER Report: ExInfo[0]=%1, ExInfo[1]=%2, Result=%3\r\n
0xb000000e | Init[%1, %2]: %3 [%4]\r\n
0xb000000f | hr=%1, file=%2, line=%3\r\n
0xb0000010 | hr=%1, custommessage=%2, function=%3 callingcode=%4 filename=%5 line=%6\r\n
0xb0000011 | context=%1, component=%2, istakeref=%3\r\n
0xb0000064 | LS_REQUEST_LATLON: %1 %2, dwHint=%3 error=%4 \r\n
0xb0000065 | LS_REPORT_LATLON: error=%8, lat=%1, lon=%2, altitude=%3, hAccuracy=%4, vAccuracy=%5, heading=%6, velocity=%7\r\n
0xb00000c8 | GnssError hr=%1, eventType=%2, numBytesTransferred=%3, eventSize=%4\r\n
0xb00000c9 | Gnss[id=%1, Adapter] START %2: param=%3\r\n
0xb00000ca | Gnss[id=%1, Adapter] STOP\r\n
0xb00000cb | Gnss[id=%1, Driver] START %2: param=%3\r\n
0xb00000cc | Gnss[id=%1, Driver] STOP\r\n
0xb00000cd | Gnss[id=%1] POS: %3, Intermediate=%4, lat=%5, lon=%6, alt=%7, speed=%8, head=%9, hAccuracy=%10, vAccuracy=%11, speedAcc=%12, HDOP=%13, PDOP=%14, Status=%2\r\n
0xb00000ce | Gnss[id=%1, Driver] MOD %2: param=%3\r\n
0xb00000cf | Gnss[id=%1, Driver] Ioctl=%2, hr=%3, Duration=%4\r\n
0xb00000d0 | Gnss[id=%1] SAT: %2\r\n
0xb00000d1 | Gnss[id=%1, Driver] FixEventError hr=%2, numBytesTransferred=%3, fixlevelofdetails=%4, expectedMinBytes=%5, expectedMinSatelliteBytes=%6\r\n
0xb00000d2 | Session[%1,%2] START %3, IsClient=%9, Acquire[attached=%10, owner=%11], Age=%7, %4, AccuracyValue=%5, VenueMandatory=%8, Param=%6\r\n
0xb00000d3 | Session[%1,%2] STOP: hr=%3\r\n
0xb00000d4 | Session[%1,%2] POS: %5, Status=%3, SourcePe=%4, Intermediate=%6, lat=%7, lon=%8, HAcc=%9, Speed=%10, Floor=%11, Venue=%12\r\n
0xb00000d5 | Session[%1,%2] CallerName=%6, CallerProductId=%3, Sid=%4, PackageId=%5\r\n
0xb00000dc | Orion ServerTime: hr=%1, Report hr=%2, time=%3\r\n
0xb00000dd | Orion Agnss: hr=%1, Report hr=%2, BlobSize=%3\r\n
0xb00000de | Orion Inference: Winhttp hr=%1, Orion=%2, lat=%3, lon=%4, Accuracy=%5\r\n
0xb00000e6 | SUPL config: hslp=%1 (src=%2), hslp_from_imsi=%3\r\n
0xb00000e7 | V2UPL config: MPC=%1, PDE=%2, AppType=%3\r\n
0xb00000e8 | Set SUPL version: %1.%2\r\n
0xb00000e9 | Cert config: Action=%1, Name=%2, Size=%3\r\n
0xb00000ea | Driver cmd=%1, value=%2\r\n
0xb00000eb | Agnss Inject: type=%1, status=%2, dataSize=%3\r\n
0xb00000ec | NI Request: id=%1, type=%2, NotType=%3, Plane=%4\r\n
0xb00000ed | NI Response: id=%1, response=%2\r\n
0xb00000ee | Driver: ForceOperationMode=%1\r\n
0xb00000ef | Agnss Request: type=%1 %2\r\n
0xb00000f0 | SUPL Reconfig: Trigger=%1, CurrentRegStatus=%2\r\n
0xb00000f1 | Agnss Clear: type=%1\r\n
0xb00000f2 | Agnss Position Inject: status=%1, lat=%2, lon=%3, alt=%4, speed=%5, head=%6, hAccuracy=%7\r\n
0xb00000f3 | Agnss Time Inject: status=%1, Time=%2, Uncertainty=%3\r\n
0xb00000f4 | Agnss Blob Inject: status=%1, Version=%2, Format=%3, Size=%4\r\n
0xb00000f5 | GnssAdapt GFAdd Id=[%1:%2], hwId=%3 hr=%4\r\n
0xb00000f6 | GnssAdapt GFRemove: hwId=%1, hr=%2\r\n
0xb00000f7 | GnssAdapt GFResetTracking: hr=%1\r\n
0xb00000f8 | GnssAdapt GFEvent: id=%1, triggerState=%2\r\n
0xb00000f9 | GnssAdapt GFTrackingStatus: state=%1\r\n
0xb00000fa | SC GSM MCC=%1, MNC=%2, CID=%3, LAC=%4\r\n
0xb00000fb | SC UMTS MCC=%1, MNC=%2, CID=%3, LAC=%4\r\n
0xb00000fc | SC CDMA BaseLat=%1, BaseLong=%2, BSID=%3, NID=%4, SID=%5\r\n
0xb00000fd | SC LTE MCC=%1, MNC=%2, CID=%3\r\n
0xb00000fe | Neighbors: %1\r\n
0xb00000ff | SC TDSCDMA MCC=%1, MNC=%2, LAC=%3, CID=%4\r\n
0xb0000100 | [Cell Adapter]Cell Location update noficiation: Parms = %1, Exe= %2, UiccApp = %3, LAC=%4, TAC = %5, CID=%6\r\n
0xb0000101 | [Cell Adapter]Cell Location update notification Error state, hr =%1\r\n
0xb0000102 | Neighbors Used: %1\r\n
0xb0000103 | IsMulticellUsed=%1\r\n
0xb0000104 | Mac Address=%1, Signal Strength=%2\r\n
0xb0000105 | Wifi Change: Name=%1, State=%2\r\n
0xb0000106 | Wifi MACs:%1\r\n
0xb0000109 | GnssAdapt GnssError Error=%1, Recoverable=%2, Description=%3\r\n
0xb000010a | GnssAdapt DeviceAvailable = %1, SymbolicLink=%2, DeviceInUse=%3, hr= %4\r\n
0xb000010b | GnssPnPManager Device Arrival SymbolicLink= %1, IsExternal=%2\r\n
0xb000010c | GnssPnPManager Device Removal SymbolicLink= %1, IsExternal=%2\r\n
0xb000010d | GnssPnPManager Retrying for SymbolicLink= %1\r\n
0xb000010e | Server Cache IsHit=%1, PE=%2\r\n
0xb000010f | Tile Cache IsHit=%1, PE=%2\r\n
0xb0000110 | %1 Scan: Result=%2\r\n
0xb0000111 | [VenuePE] Id=[%1], Positions:[%2]\r\n
0xb0000112 | [VenuePE] IsInsideVenue=%1, Pos[Lat=%2,Lon=%3,Acc=%4,Source=%5]\r\n
0xb0000118 | [CS]InitializeDcpProfile: DcpProfile=%1, hr=%2\r\n
0xb0000119 | [CS]SubmitData: SizeInBytes=%1, DcpProfile=%2, hr=%3\r\n
0xb000011a | [CS]DataReceived: SourcePE=%1, IsReadyForData=%2, IsValidData=%3, hr=%4\r\n
0xb000011b | [CS]RawDataProcessing begins: DataListSize =%1, IsCollectionActive=%2\r\n
0xb000011c | [CS]State: Level=%1, CollectionType=%2, IsBufferFull=%3 IsBatterySavings=%4 IsUserPresenceOn=%5\r\n
0xb0000122 | Acquire[Id=%2, Cpe] SelectedPes: PrimaryPe=%1\r\n
0xb0000123 | Acquire[Id=%4, Cpe] StartPrimitivePes with Role=%1, Remaining time=%2, hr=%3\r\n
0xb0000124 | Acquire[Id=%4, Cpe] AttemptFallback with best available position Status=%1, Sourcepe=%2, AccuracyValue=%3\r\n
0xb0000126 | Acquire[Id=%14, Cpe] DT: Wait: Dist(m)=%1, IsSpeedUnknown=%12, SpeedUsed(m/s)=%2, IsMDUsed=%3, MDPrecision(m)=%4, Speed_Wait(s)=%5, MD_Wait(s)=%6, MinWait_Budget(s)=%7, SelectedWait(s)=%8, TimeBoundApplied=%13 {Cumulative Runningtime(s)=%9, Acqtime(s)=%10, Requests=%11}\r\n
0xb0000127 | [Cpe] New SpeedEstimate Speed(m/s)=%1, Bearing=%2, Positions=%3\r\n
0xb0000128 | [Cpe] SpeedEstimate Input: Timestamp=%1, Latitude=%2, Longitude=%3, Accuracy=%4\r\n
0xb000012a | Acquire[Id=%5, Cpe] Unreliable position {acc=%1, sourcepe=%2} detected on validation with position{acc=%3, sourcepe=%4} \r\n
0xb000012b | [Cpe] TotalPeCount=%1, AvailPes=[%2,%3,%4,%5,%6,%7]\r\n
0xb000012c | [%1] [%2], URL=%4, TrackingId=%6\r\n
0xb000012d | [%1] [%2]: Coordinate=[%3, %4], Acc=%7, Floor=%8, VenueId=%9, ServerStatus=[%5], WinHttpStatus=[%6], ProtocolStatus=[%11], OrionSource=[%12]\r\n
0xb000012f | [%1] [%2]: ServerStatus=[%3], WinHttpStatus=[%4], ProtocolStatus=[%6]\r\n
0xb0000130 | [%1] [%2]: ServerStatus=[%3], WinHttpStatus=[%4], ProtocolStatus=[%6]\r\n
0xb0000132 | [%1] [%2] Canceled By [%3], Status=[%4]\r\n
0xb0000133 | [%1]: Request=[%2], WinhttpHandle=[%3], WinHttpEvent=[%4], Status=[%5]\r\n
0xb0000134 | [%1]: Request=[%2], WinhttpHandle=[%3], WinHttpAPI=[%4], Status=[%5]\r\n
0xb0000135 | Request=[%2]\r\n
0xb0000136 | Response=[%2]\r\n
0xb0000191 | [Cpe] MD: Start MD, hr=%1, hrwifi=%2, hrcell=%3, wifi{ConnState=%4, ThrottlingOn=%5, Elapsedtime(s)=%6}, cell{ThrottlingOn=%7, Elapsedtime(s)=%8}\r\n
0xb0000192 | [Cpe] MD: Stop MD, hr =%1 \r\n
0xb0000193 | [Cpe] MD: Notify potential movement, hr =%1 \r\n
0xb0000194 | [Cpe] MD: Notify state changed, hr =%1 \r\n
0xb0000195 | [Cpe] MD: Get movementPrecision hr=%1, wifi{ConnState=%2, ThrottlingOn=%3, Elapsedtime=%4}, cell{ThrottlingOn=%5, Elapsedtime=%6}\r\n
0xb0000196 | Acquire[Id=%3, Cpe] StartTracking on Pe=%1, IsPrimaryNativeTracking=%2\r\n
0xb0000197 | [Cpe] SessionType=%1, IsSupportsNativePT=%2, IsSupportsNativeDT=%3, IsSupportsRequest=%4\r\n
0xb00001f4 | GeolocationStartOperation[%1] SessionType=%2, Age(ms)=%3, Accuracy(m)=%4, RequestParameter=%5\r\n
0xb00001f5 | GeolocationStartOperation[%1] Status=%2\r\n
0xb00001f6 | GeolocationEventHandler[%1] PositionStatus=%2, Latitude=%3, Longitude=%4, HAccuracy=%5, Status=%6\r\n
0xb00001f7 | GeolocationStopTrackingOperation[%1] Status=%2\r\n
0xb00001f8 | GeolocationPromptAppState State=%1\r\n
0xb000020d | GFClient Add Geofence at Index = %1, Lat=%2, Lon=%3, Radius =%4, Starttime=%5, Duration=%6, Dwelltime=%7, SingleUse=%8\r\n
0xb000020e | GFClient Remove Geofence at Index = %1, Lat=%2, Lon=%3, Radius =%4, Starttime=%5, Duration=%6, Dwelltime=%7, SingleUse=%8\r\n
0xb000020f | GFClient Clear all Geofences\r\n
0xb0000210 | GFClient Register for %1 changes \r\n
0xb0000211 | GFClient Unregister for %1 changes\r\n
0xb0000212 | GFClient Read Geofence reports\r\n
0xb0000213 | GFClient Event signalled on client for %1\r\n
0xb0000214 | GFClient Create location trigger \r\n
0xb0000215 | GFClient Delete location trigger \r\n
0xb0000216 | GFClient  Geofence: Id=[%1:%2] Lat=%3, Lon=%4, Radius=%5, Starttime=%6, Duration=%7, Dwelltime=%8, SingleUse=%9 \r\n
0xb0000226 | GeofenceOperation[%1] Status=%2\r\n
0xb0000227 | GFAppBoundary GeofenceOperation[%1] ClientId=%2, EventId=%3, Status=%4\r\n
0xb0000228 | GFAppBoundary %3 %2 %1Event: PID=%4, AppId=%5, EventId=%6, Status=%7\r\n
0xb0000229 | GFAppBoundary  AddGeofence: CallerName=%11, Id=[%1:%2] Lat=%3, Lon=%4, Radius=%5, Starttime=%6, Duration=%7, Dwelltime=%8, SingleUse=%9, hr=%10\r\n
0xb000022a | GFAppBoundary  RemoveGeofence: CallerName=%4, Id=[%1:%2], hr = %3\r\n
0xb000022b | GFAppBoundary  RemoveAllGeofences: CallerName=%3, AppId=%1, hr = %2\r\n
0xb000022c | GFAppBoundary  ListAllGeofences: AppId=%1, GeofencesCount=%2, hr=%3\r\n
0xb000022d | GFAppBoundary  ReadGeofenceReports: AppId=%1, GeofenceReportsCount=%2, hr=%3\r\n
0xb000022e | GFClient  GeofenceReport: GfId=%1, Trigger=%2, RemovalReason=%3, Status=%4, Lat=%5, Lon=%6, HAcc=%7\r\n
0xb000022f | GFAppBoundary  ForegroundEventFired ForegroundEventType=%1\r\n
0xb0000230 | GFAppBoundary  BackgroundEventSignalled ClientId=%1, EventId=%2, hr=%3\r\n
0xb0000258 | GCW: Instance=[%1], Type=[%2], Source=[%3], Taskhost=[%4], CurrentState=[%5], Timeout=[%6]\r\n
0xb0000259 | GCW: Instance=[%1], GeoStatus=[%2], GeoPermission=[%3]\r\n
0xb00002bc | TRK_RG Trigger: Id=[%1:%2], Trigger=%3, Lat=%4, Lon=%5\r\n
0xb00002bd | TRK_RG GF State: Tracker=%1, Id=[%2:%3], State=%4, Lat=%5, Lon=%6\r\n
0xb00002be | TRK_RG BeginRegionLoad\r\n
0xb00002bf | TRK_RG EndRegionLoad: Lat=%1, Lon=%2, Radius=%3, Geofences=%4\r\n
0xb00002c0 | TRK_RG Start tracking for: AppId=[%1]\r\n
0xb00002c1 | TRK_RG Stop tracking for: AppId=[%1]\r\n
0xb00002c2 | TRK_%1 Start Tracking: Id=[%2:%3], Lat=%4, Lon=%5, Radius=%6, Dwelltime=%7ms, Start=%8, Duration=%9ms, Singleuse=%10\r\n
0xb00002c3 | TRK_%1 Stop Tracking: Id=[%2:%3]\r\n
0xb00002c4 | TRK_SW Active=%1, Distance=%2, Accuracy=%3\r\n
0xb00002c5 | TRK_RG Not Tracking: Id=[%1:%2], Lat=%3, Lon=%4, Radius=%5, Dwelltime=%6ms, Start=%7, Duration=%8ms, Singleuse=%9\r\n
0xb00002c6 | TRK_RG Tracker State: Tracker=%1, NewState=%2\r\n
0xb00002c7 | TRK_%1 Enable=%2\r\n
0xb00002c8 | TRK_RG Add to Trackers: Id=[%1:%2], Lat=%3, Lon=%4, Radius=%5, Dwelltime=%6ms, Start=%7, Duration=%8ms, Singleuse=%9 {TrackedGeofencesCount=%10}\r\n
0xb00002c9 | TRK_RG Remove from Trackers: Id=[%1:%2] {TrackedGeofencesCount=%3}\r\n
0xb0000320 | Location KPI : [%1]:  , TTFF = %2msec, Accuracy = %3m\r\n
0xb0000384 | GFStore Add: Id=[%1:%2], hr=%3 \r\n
0xb0000385 | GFStore Remove: Id=[%1:%2], hr=%3 \r\n
0xb0000386 | GFStore Update: Id=[%1:%2], TriggerState= %3, hr=%4 \r\n
0xb0000387 | GFStore Get Id=[%1:%2], hr=%3 \r\n
0xb0000388 | GFStore DeleteAll: AppId=%1, hr=%2 \r\n
0xb0000389 | GFStore GetAllGeofence: AppId=%1, Count=%2 hr=%3 \r\n
0xb000038a | GFStore GetClosestGeofence: Lat=%1, Lon=%2, AppCount=%3, GFCount=%4 TransGFCount= %5, hr=%6 \r\n
0xb000038b | GFStore DeleteApp: AppId=%1, hr=%2 \r\n
0xb000038c | GFStore Internal: Messsage=%1, hr=%2 \r\n
0xb000038d | GFStore GetAppID: AppContext= %1 AppId=%2, hr=%3 \r\n
0xb00003e8 | Location Geofence Power Scenario: [%1]:  , Start\r\n
0xb00003e9 | Location Geofence Power Scenario: [%1]:  , Stop\r\n
0xb000044c | Permission denied for client = %1. Unconditional = %2, Policy = %3, LegacyPolicy = %4, Master = %5, User = %6, UserLegacyPolicy = %7, App = %8, is app container = %9. UserSid = %10, Package = %11\r\n
0xb000044d | Permission denied because client was not found, client = %1. User = %2, Package = %3\r\n
0xb00004b0 | Disabling geofencing because we are entering into Disconnected standby\r\n
0xb00004b1 | Re-enabling geofencing because we are exiting Disconnected standby\r\n
0xb00004e2 | WiFiAcquire: Id[0x%1], InferenceResult[%2], PositionSource[%3], PositionStatus[%4]\r\n
0xb00004e3 | SUPL Reconfig: Trigger=%1, CurrentRegStatus=%2\r\n
0xd0000001 | OK\r\n
0xd0000002 | Not resolvable\r\n
0xd0000003 | Invalid parameter\r\n
0xd0000004 | Server Error\r\n
0xd0000005 | Invalid Server Response\r\n
0xd0000006 | Other failure\r\n
0xd0000007 | WinHttp: No CM Connection\r\n
0xd0000008 | WinHttp: Not Redirected\r\n
0xd0000009 | Connectivity Error\r\n
0xd000000a | ProviderHelper\r\n
0xd000000b | Session\r\n
0xd000000c | LocationInformation\r\n
0xd000000d | ServiceProxy\r\n
0xd000000e | Cpe\r\n
0xd000000f | CpeAcquireSingleShot\r\n
0xd0000010 | CpeAcquirePeriodicTracking\r\n
0xd0000011 | CpeAcquireDistanceTracking\r\n
0xd0000012 | WifiPe\r\n
0xd0000013 | WifiPeAdapter\r\n
0xd0000014 | WifiPeAcquireSingleShot\r\n
0xd0000015 | CellPe\r\n
0xd0000016 | CellPeAdapter\r\n
0xd0000017 | CellPeAcquireSingleShot\r\n
0xd0000018 | GnssPe\r\n
0xd0000019 | GnssPeAcquireSingleShot\r\n
0xd000001a | GnssPeAcquirePeriodicTracking\r\n
0xd000001b | GnssPeAcquireDistanceTracking\r\n
0xd000001c | GnssAdapter\r\n
0xd000001d | Crowdsource\r\n
0xd000001e | Invalid\r\n
0xd000001f | SingleShot\r\n
0xd0000020 | Distance\r\n
0xd0000021 | Periodic\r\n
0xd0000022 | Geofence\r\n
0xd0000023 | Passive\r\n
0xd0000024 | AccuracySpecific\r\n
0xd0000025 | AccuracyAny\r\n
0xd0000026 | AccuracyHighest\r\n
0xd0000027 | Unknown\r\n
0xd0000028 | Cpe\r\n
0xd0000029 | Gnss\r\n
0xd000002a | Wifi\r\n
0xd000002b | Cell\r\n
0xd000002c | Venue\r\n
0xd000002d | IpAddr\r\n
0xd000002e | User\r\n
0xd000002f | Legacy\r\n
0xd0000030 | SingleShot\r\n
0xd0000031 | Distance\r\n
0xd0000032 | Periodic\r\n
0xd0000033 | LKG\r\n
0xd0000034 | AccuracyHigh\r\n
0xd0000035 | AccuracyPowerOptimized\r\n
0xd0000036 | GenerateLast\r\n
0xd0000037 | GenerateFirst\r\n
0xd0000038 | GenerateBest\r\n
0xd0000039 | Inject\r\n
0xd000003a | Delete\r\n
0xd000003b | Purge\r\n
0xd000003c | Time\r\n
0xd000003d | Position\r\n
0xd000003e | Blob\r\n
0xd000003f | XTRA1\r\n
0xd0000040 | XTRA2\r\n
0xd0000041 | LTO\r\n
0xd0000042 | XTRA3\r\n
0xd0000043 | SingleShot\r\n
0xd0000044 | AreaTrigger\r\n
0xd0000045 | NoNotifyNoVerify\r\n
0xd0000046 | NotifyOnly\r\n
0xd0000047 | NotifyVerifyDefaultAllow\r\n
0xd0000048 | NotifyVerifyDefaultNotAllow\r\n
0xd0000049 | PrivacyOverride\r\n
0xd000004a | SUPL\r\n
0xd000004b | CP\r\n
0xd000004c | V2UPL\r\n
0xd000004d | Accept\r\n
0xd000004e | Deny\r\n
0xd000004f | Timeout\r\n
0xd0000050 | Unknown\r\n
0xd0000051 | CAN_Removed\r\n
0xd0000052 | Csp_Update\r\n
0xd0000053 | Cellular_Update\r\n
0xd0000054 | None\r\n
0xd0000055 | Home\r\n
0xd0000056 | Deregistered\r\n
0xd0000057 | Searching\r\n
0xd0000058 | Denied\r\n
0xd0000059 | Roaming\r\n
0xd000005a | Partner\r\n
0xd000005b | Unknown\r\n
0xd000005c | CSP\r\n
0xd000005d | UICC\r\n
0xd000005e | IMSI\r\n
0xd000005f | Unknown\r\n
0xd0000060 | Unregistered\r\n
0xd0000061 | Home\r\n
0xd0000062 | Attempting\r\n
0xd0000063 | Denied\r\n
0xd0000064 | Roaming\r\n
0xd0000065 | Domestic roaming\r\n
0xd0000066 | SetLocationServiceEnabled\r\n
0xd0000067 | SetLocationNIRequestAllowed\r\n
0xd0000068 | ForceSatelliteSystem\r\n
0xd0000069 | ForceOperationMode\r\n
0xd000006a | SetEngineKeepWarmPeriod\r\n
0xd000006b | SetEngineWarm\r\n
0xd000006c | SetEngineCold\r\n
0xd000006d | SetEngineHot\r\n
0xd000006e | ResetEngine\r\n
0xd000006f | ClearAgnssData\r\n
0xd0000070 | SetDefaultFixResponseTime\r\n
0xd0000071 | SetSuplVersion\r\n
0xd0000072 | SetNMEALogging\r\n
0xd0000073 | SetUplServerAccessInterval\r\n
0xd0000074 | SetNiTimeoutInterval\r\n
0xd0000075 | ResetGeofencesTracking\r\n
0xd0000076 | Any\r\n
0xd0000077 | MSA\r\n
0xd0000078 | MSB\r\n
0xd0000079 | MSS\r\n
0xd000007a | CellId\r\n
0xd000007b | AFLT\r\n
0xd000007c | OTDOA\r\n
0xd000007d | SEND_PLATFORM_CAPABILITY\r\n
0xd000007e | GET_DEVICE_CAPABILITY\r\n
0xd000007f | SEND_DRIVERCOMMAND\r\n
0xd0000080 | START_FIXSESSION\r\n
0xd0000081 | MODIFY_FIXSESSION\r\n
0xd0000082 | STOP_FIXSESSION\r\n
0xd0000083 | GET_FIXDATA\r\n
0xd0000084 | INJECT_AGNSS\r\n
0xd0000085 | LISTEN_AGNSS\r\n
0xd0000086 | LISTEN_ERROR\r\n
0xd0000087 | LISTEN_FAILOVER\r\n
0xd0000088 | LISTEN_CUSTOM\r\n
0xd0000089 | LISTEN_NI\r\n
0xd000008a | SET_SUPL_HSLP\r\n
0xd000008b | CONFIG_SUPL_CERT\r\n
0xd000008c | RESPOND_NI\r\n
0xd000008d | EXECUTE_CWTEST\r\n
0xd000008e | EXECUTE_SELFTEST\r\n
0xd000008f | GET_CHIPSETINFO\r\n
0xd0000090 | LISTEN_NMEA\r\n
0xd0000091 | SET_V2UPL_CONFIG\r\n
0xd0000092 | TimeBound\r\n
0xd0000093 | BestEffort\r\n
0xd0000094 | Low\r\n
0xd0000095 | Medium\r\n
0xd0000096 | High\r\n
0xd0000097 | None\r\n
0xd0000098 | Cell\r\n
0xd0000099 | WiFi\r\n
0xd000009a | All\r\n
0xd000009b | CellInference\r\n
0xd000009c | WiFiInference\r\n
0xd000009d | AgnssData\r\n
0xd000009e | ServerTimeData\r\n
0xd000009f | WebproxyTileRequest\r\n
0xd00000a0 | CrowdsourceData\r\n
0xd00000a1 | VenueTileRequest\r\n
0xd00000a2 | VenueModelRequest\r\n
0xd00000a3 | WebproxyCaller\r\n
0xd00000a4 | WebproxyInternal\r\n
0xd00000a5 | WebproxyWinHttp\r\n
0xd00000a6 | WinHttpResponseHeaderAvail\r\n
0xd00000a7 | WinHttpResponseReadComplete\r\n
0xd00000a8 | WinHttpResponseWriteComplete\r\n
0xd00000a9 | WinHttpRequestError\r\n
0xd00000aa | WinHttpRequestSendComplete\r\n
0xd00000ab | WinHttpOpenRequest\r\n
0xd00000ac | WinHttpSendRequest\r\n
0xd00000ad | WinHttpWriteData\r\n
0xd00000ae | WinHttpReceiveResponse\r\n
0xd00000af | WinHttpReadData\r\n
0xd00000b0 | WinHttpPayloadConversionFailed\r\n
0xd00000b1 | Start\r\n
0xd00000b2 | Stop\r\n
0xd00000b3 | StopByDisposed\r\n
0xd00000b4 | TryStart\r\n
0xd00000b5 | Execution\r\n
0xd00000b6 | PostStatusToApp\r\n
0xd00000b7 | PostPositionToApp\r\n
0xd00000b8 | Application\r\n
0xd00000b9 | Taskhost\r\n
0xd00000ba | LocationService\r\n
0xd00000bb | InternalGCW\r\n
0xd00000bc | None\r\n
0xd00000bd | Paused\r\n
0xd00000be | ResumedTombstone\r\n
0xd00000bf | ResumedFAS\r\n
0xd00000c0 | Starting\r\n
0xd00000c1 | Started\r\n
0xd00000c2 | Stopping\r\n
0xd00000c3 | Stopped\r\n
0xd00000c4 | Executing\r\n
0xd00000c5 | Disabled\r\n
0xd00000c6 | Ready\r\n
0xd00000c7 | Initializing\r\n
0xd00000c8 | NoData\r\n
0xd00000c9 | Unknown\r\n
0xd00000ca | Granted\r\n
0xd00000cb | Denied\r\n
0xd00000cc | Primary\r\n
0xd00000cd | Fallback\r\n
0xd00000ce | Unknown\r\n
0xd00000cf | Inside\r\n
0xd00000d0 | Outside\r\n
0xd00000d1 | Unknown\r\n
0xd00000d2 | Enter\r\n
0xd00000d3 | Exit\r\n
0xd00000d4 | Removed\r\n
0xd00000d5 | ??\r\n
0xd00000d6 | SW\r\n
0xd00000d7 | HW\r\n
0xd00000d8 | Unknown\r\n
0xd00000d9 | Tracking\r\n
0xd00000da | NotTracking\r\n
0xd00000db | Geofence\r\n
0xd00000dc | GeofenceMonitor\r\n
0xd00000dd | Background\r\n
0xd00000de | Foreground\r\n
0xd00000df | Win32Event\r\n
0xd00000e0 | WnfEvent\r\n
0xd00000e1 | Unregister\r\n
0xd00000e2 | Register\r\n
0xd00000e3 | Used\r\n
0xd00000e4 | Expired\r\n
0xd00000e5 | NotTracking\r\n
0xd00000e6 | Tracking\r\n
0xd00000e7 | WiFiDisconnected\r\n
0xd00000e8 | WiFiConnected\r\n
0xd00000e9 | Unset\r\n
0xd00000ea | Enabled\r\n
0xd00000eb | Disabled\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1

Message identifier | Message string
--- | ---
0x00000001 | Geolocation positioning is enabled.\r\n
0x00000002 | Geolocation positioning has been disabled by the user.\r\n
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000003 | Selfhost\r\n
0x10000004 | WiFiTracing\r\n
0x10000005 | Init\r\n
0x10000006 | Position\r\n
0x10000007 | FixSession\r\n
0x10000008 | CompositePe\r\n
0x10000009 | Gnss\r\n
0x1000000a | CellPe\r\n
0x1000000b | WifiPe\r\n
0x1000000c | ClientApi\r\n
0x1000000d | Orion\r\n
0x1000000e | Supl\r\n
0x1000000f | Crowdsource\r\n
0x10000010 | ManagedApi\r\n
0x10000011 | GeofenceTracing\r\n
0x10000012 | GeofenceStore\r\n
0x1000001c | WebproxyTracing\r\n
0x1000001e | CellPeAdvanceTracing\r\n
0x1000001f | SpeedEstimatorTracing\r\n
0x10000020 | VenuePE\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | LocationServiceProvider\r\n
0x90000002 | Debug\r\n
0xb000000d | WER Report: ExInfo[0]=%1, ExInfo[1]=%2, Result=%3\r\n
0xb000000e | Init[%1, %2]: %3 [%4]\r\n
0xb000000f | hr=%1, file=%2, line=%3\r\n
0xb0000010 | hr=%1, custommessage=%2, function=%3 callingcode=%4 filename=%5 line=%6\r\n
0xb0000011 | context=%1, component=%2, istakeref=%3\r\n
0xb0000064 | LS_REQUEST_LATLON: %1 %2, dwHint=%3 error=%4 \r\n
0xb0000065 | LS_REPORT_LATLON: error=%8, lat=%1, lon=%2, altitude=%3, hAccuracy=%4, vAccuracy=%5, heading=%6, velocity=%7\r\n
0xb00000c8 | GnssError hr=%1, eventType=%2, numBytesTransferred=%3, eventSize=%4\r\n
0xb00000c9 | Gnss[id=%1, Adapter] START %2: param=%3\r\n
0xb00000ca | Gnss[id=%1, Adapter] STOP\r\n
0xb00000cb | Gnss[id=%1, Driver] START %2: param=%3\r\n
0xb00000cc | Gnss[id=%1, Driver] STOP\r\n
0xb00000cd | Gnss[id=%1] POS: %3, Intermediate=%4, lat=%5, lon=%6, alt=%7, speed=%8, head=%9, hAccuracy=%10, vAccuracy=%11, speedAcc=%12, HDOP=%13, PDOP=%14, Status=%2\r\n
0xb00000ce | Gnss[id=%1, Driver] MOD %2: param=%3\r\n
0xb00000cf | Gnss[id=%1, Driver] Ioctl=%2, hr=%3, Duration=%4\r\n
0xb00000d0 | Gnss[id=%1] SAT: %2\r\n
0xb00000d1 | Gnss[id=%1, Driver] FixEventError hr=%2, numBytesTransferred=%3, fixlevelofdetails=%4, expectedMinBytes=%5, expectedMinSatelliteBytes=%6\r\n
0xb00000d2 | Session[%1,%2] START %3, IsClient=%9, Acquire[attached=%10, owner=%11], Age=%7, %4, AccuracyValue=%5, VenueMandatory=%8, Param=%6\r\n
0xb00000d3 | Session[%1,%2] STOP: hr=%3\r\n
0xb00000d4 | Session[%1,%2] POS: %5, Status=%3, SourcePe=%4, Intermediate=%6, lat=%7, lon=%8, HAcc=%9, Speed=%10, Floor=%11, Venue=%12\r\n
0xb00000d5 | Session[%1,%2] CallerName=%6, CallerProductId=%3, Sid=%4, PackageId=%5\r\n
0xb00000dc | Orion ServerTime: hr=%1, Report hr=%2, time=%3\r\n
0xb00000dd | Orion Agnss: hr=%1, Report hr=%2, BlobSize=%3\r\n
0xb00000de | Orion Inference: Winhttp hr=%1, Orion=%2, lat=%3, lon=%4, Accuracy=%5\r\n
0xb00000e6 | SUPL config: hslp=%1 (src=%2), hslp_from_imsi=%3\r\n
0xb00000e7 | V2UPL config: MPC=%1, PDE=%2, AppType=%3\r\n
0xb00000e8 | Set SUPL version: %1.%2\r\n
0xb00000e9 | Cert config: Action=%1, Name=%2, Size=%3\r\n
0xb00000ea | Driver cmd=%1, value=%2\r\n
0xb00000eb | Agnss Inject: type=%1, status=%2, dataSize=%3\r\n
0xb00000ec | NI Request: id=%1, type=%2, NotType=%3, Plane=%4\r\n
0xb00000ed | NI Response: id=%1, response=%2\r\n
0xb00000ee | Driver: ForceOperationMode=%1\r\n
0xb00000ef | Agnss Request: type=%1 %2\r\n
0xb00000f0 | SUPL Reconfig: Trigger=%1, CurrentRegStatus=%2\r\n
0xb00000f1 | Agnss Clear: type=%1\r\n
0xb00000f2 | Agnss Position Inject: status=%1, lat=%2, lon=%3, alt=%4, speed=%5, head=%6, hAccuracy=%7\r\n
0xb00000f3 | Agnss Time Inject: status=%1, Time=%2, Uncertainty=%3\r\n
0xb00000f4 | Agnss Blob Inject: status=%1, Version=%2, Format=%3, Size=%4\r\n
0xb00000f5 | GnssAdapt GFAdd Id=[%1:%2], hwId=%3 hr=%4\r\n
0xb00000f6 | GnssAdapt GFRemove: hwId=%1, hr=%2\r\n
0xb00000f7 | GnssAdapt GFResetTracking: hr=%1\r\n
0xb00000f8 | GnssAdapt GFEvent: id=%1, triggerState=%2\r\n
0xb00000f9 | GnssAdapt GFTrackingStatus: state=%1\r\n
0xb00000fa | SC GSM MCC=%1, MNC=%2, CID=%3, LAC=%4\r\n
0xb00000fb | SC UMTS MCC=%1, MNC=%2, CID=%3, LAC=%4\r\n
0xb00000fc | SC CDMA BaseLat=%1, BaseLong=%2, BSID=%3, NID=%4, SID=%5\r\n
0xb00000fd | SC LTE MCC=%1, MNC=%2, CID=%3\r\n
0xb00000fe | Neighbors: %1\r\n
0xb00000ff | SC TDSCDMA MCC=%1, MNC=%2, LAC=%3, CID=%4\r\n
0xb0000100 | [Cell Adapter]Cell Location update noficiation: Parms = %1, Exe= %2, UiccApp = %3, LAC=%4, TAC = %5, CID=%6\r\n
0xb0000101 | [Cell Adapter]Cell Location update notification Error state, hr =%1\r\n
0xb0000102 | Neighbors Used: %1\r\n
0xb0000103 | IsMulticellUsed=%1\r\n
0xb0000104 | Mac Address=%1, Signal Strength=%2\r\n
0xb0000105 | Wifi Change: Name=%1, State=%2\r\n
0xb0000106 | Wifi MACs:%1\r\n
0xb0000109 | GnssAdapt GnssError Error=%1, Recoverable=%2, Description=%3\r\n
0xb000010a | GnssAdapt DeviceAvailable = %1, SymbolicLink=%2, DeviceInUse=%3, hr= %4\r\n
0xb000010b | GnssPnPManager Device Arrival SymbolicLink= %1, IsExternal=%2\r\n
0xb000010c | GnssPnPManager Device Removal SymbolicLink= %1, IsExternal=%2\r\n
0xb000010d | GnssPnPManager Retrying for SymbolicLink= %1\r\n
0xb000010e | Server Cache IsHit=%1, PE=%2\r\n
0xb000010f | Tile Cache IsHit=%1, PE=%2\r\n
0xb0000110 | %1 Scan: Result=%2\r\n
0xb0000111 | [VenuePE] Id=[%1], Positions:[%2]\r\n
0xb0000112 | [VenuePE] IsInsideVenue=%1, Pos[Lat=%2,Lon=%3,Acc=%4,Source=%5]\r\n
0xb0000118 | [CS]InitializeDcpProfile: DcpProfile=%1, hr=%2\r\n
0xb0000119 | [CS]SubmitData: SizeInBytes=%1, DcpProfile=%2, hr=%3\r\n
0xb000011a | [CS]DataReceived: SourcePE=%1, IsReadyForData=%2, IsValidData=%3, hr=%4\r\n
0xb000011b | [CS]RawDataProcessing begins: DataListSize =%1, IsCollectionActive=%2\r\n
0xb000011c | [CS]State: Level=%1, CollectionType=%2, IsBufferFull=%3 IsBatterySavings=%4 IsUserPresenceOn=%5\r\n
0xb0000122 | Acquire[Id=%2, Cpe] SelectedPes: PrimaryPe=%1\r\n
0xb0000123 | Acquire[Id=%4, Cpe] StartPrimitivePes with Role=%1, Remaining time=%2, hr=%3\r\n
0xb0000124 | Acquire[Id=%4, Cpe] AttemptFallback with best available position Status=%1, Sourcepe=%2, AccuracyValue=%3\r\n
0xb0000126 | Acquire[Id=%14, Cpe] DT: Wait: Dist(m)=%1, IsSpeedUnknown=%12, SpeedUsed(m/s)=%2, IsMDUsed=%3, MDPrecision(m)=%4, Speed_Wait(s)=%5, MD_Wait(s)=%6, MinWait_Budget(s)=%7, SelectedWait(s)=%8, TimeBoundApplied=%13 {Cumulative Runningtime(s)=%9, Acqtime(s)=%10, Requests=%11}\r\n
0xb0000127 | [Cpe] New SpeedEstimate Speed(m/s)=%1, Bearing=%2, Positions=%3\r\n
0xb0000128 | [Cpe] SpeedEstimate Input: Timestamp=%1, Latitude=%2, Longitude=%3, Accuracy=%4\r\n
0xb000012a | Acquire[Id=%5, Cpe] Unreliable position {acc=%1, sourcepe=%2} detected on validation with position{acc=%3, sourcepe=%4} \r\n
0xb000012b | [Cpe] TotalPeCount=%1, AvailPes=[%2,%3,%4,%5,%6,%7]\r\n
0xb000012c | [%1] [%2], URL=%4, TrackingId=%6\r\n
0xb000012d | [%1] [%2]: Coordinate=[%3, %4], Acc=%7, Floor=%8, VenueId=%9, ServerStatus=[%5], WinHttpStatus=[%6], ProtocolStatus=[%11], OrionSource=[%12]\r\n
0xb000012f | [%1] [%2]: ServerStatus=[%3], WinHttpStatus=[%4], ProtocolStatus=[%6]\r\n
0xb0000130 | [%1] [%2]: ServerStatus=[%3], WinHttpStatus=[%4], ProtocolStatus=[%6]\r\n
0xb0000132 | [%1] [%2] Canceled By [%3], Status=[%4]\r\n
0xb0000133 | [%1]: Request=[%2], WinhttpHandle=[%3], WinHttpEvent=[%4], Status=[%5]\r\n
0xb0000134 | [%1]: Request=[%2], WinhttpHandle=[%3], WinHttpAPI=[%4], Status=[%5]\r\n
0xb0000135 | Request=[%2]\r\n
0xb0000136 | Response=[%2]\r\n
0xb0000191 | [Cpe] MD: Start MD, hr=%1, hrwifi=%2, hrcell=%3, wifi{ConnState=%4, ThrottlingOn=%5, Elapsedtime(s)=%6}, cell{ThrottlingOn=%7, Elapsedtime(s)=%8} ActivityDetection{ThrottlingOn=%9, Elapsedtime(s)=%10}\r\n
0xb0000192 | [Cpe] MD: Stop MD, hr =%1 \r\n
0xb0000193 | [Cpe] MD: Notify potential movement, hr =%1 \r\n
0xb0000194 | [Cpe] MD: Notify state changed, hr =%1 \r\n
0xb0000195 | [Cpe] MD: Get movementPrecision hr=%1, wifi{ConnState=%2, ThrottlingOn=%3, Elapsedtime=%4}, cell{ThrottlingOn=%5, Elapsedtime=%6} AD={ThrottlingOn=%7, Elapsedtime=%8}\r\n
0xb0000196 | Acquire[Id=%3, Cpe] StartTracking on Pe=%1, IsPrimaryNativeTracking=%2\r\n
0xb0000197 | [Cpe] SessionType=%1, IsSupportsNativePT=%2, IsSupportsNativeDT=%3, IsSupportsRequest=%4\r\n
0xb00001f4 | GeolocationStartOperation[%1] SessionType=%2, Age(ms)=%3, Accuracy(m)=%4, RequestParameter=%5\r\n
0xb00001f5 | GeolocationStartOperation[%1] Status=%2\r\n
0xb00001f6 | GeolocationEventHandler[%1] PositionStatus=%2, Latitude=%3, Longitude=%4, HAccuracy=%5, Status=%6\r\n
0xb00001f7 | GeolocationStopTrackingOperation[%1] Status=%2\r\n
0xb00001f8 | GeolocationPromptAppState State=%1\r\n
0xb000020d | GFClient Add Geofence at Index = %1, Lat=%2, Lon=%3, Radius =%4, Starttime=%5, Duration=%6, Dwelltime=%7, SingleUse=%8\r\n
0xb000020e | GFClient Remove Geofence at Index = %1, Lat=%2, Lon=%3, Radius =%4, Starttime=%5, Duration=%6, Dwelltime=%7, SingleUse=%8\r\n
0xb000020f | GFClient Clear all Geofences\r\n
0xb0000210 | GFClient Register for %1 changes \r\n
0xb0000211 | GFClient Unregister for %1 changes\r\n
0xb0000212 | GFClient Read Geofence reports\r\n
0xb0000213 | GFClient Event signalled on client for %1\r\n
0xb0000214 | GFClient Create location trigger \r\n
0xb0000215 | GFClient Delete location trigger \r\n
0xb0000216 | GFClient  Geofence: Id=[%1:%2] Lat=%3, Lon=%4, Radius=%5, Starttime=%6, Duration=%7, Dwelltime=%8, SingleUse=%9 \r\n
0xb0000226 | GeofenceOperation[%1] Status=%2\r\n
0xb0000227 | GFAppBoundary GeofenceOperation[%1] ClientId=%2, EventId=%3, Status=%4\r\n
0xb0000228 | GFAppBoundary %3 %2 %1Event: PID=%4, AppId=%5, EventId=%6, Status=%7\r\n
0xb0000229 | GFAppBoundary  AddGeofence: CallerName=%11, Id=[%1:%2] Lat=%3, Lon=%4, Radius=%5, Starttime=%6, Duration=%7, Dwelltime=%8, SingleUse=%9, hr=%10\r\n
0xb000022a | GFAppBoundary  RemoveGeofence: CallerName=%4, Id=[%1:%2], hr = %3\r\n
0xb000022b | GFAppBoundary  RemoveAllGeofences: CallerName=%3, AppId=%1, hr = %2\r\n
0xb000022c | GFAppBoundary  ListAllGeofences: AppId=%1, GeofencesCount=%2, hr=%3\r\n
0xb000022d | GFAppBoundary  ReadGeofenceReports: AppId=%1, GeofenceReportsCount=%2, hr=%3\r\n
0xb000022e | GFClient  GeofenceReport: GfId=%1, Trigger=%2, RemovalReason=%3, Status=%4, Lat=%5, Lon=%6, HAcc=%7\r\n
0xb000022f | GFAppBoundary  ForegroundEventFired ForegroundEventType=%1\r\n
0xb0000230 | GFAppBoundary  BackgroundEventSignalled ClientId=%1, EventId=%2, hr=%3\r\n
0xb0000258 | GCW: Instance=[%1], Type=[%2], Source=[%3], Taskhost=[%4], CurrentState=[%5], Timeout=[%6]\r\n
0xb0000259 | GCW: Instance=[%1], GeoStatus=[%2], GeoPermission=[%3]\r\n
0xb00002bc | TRK_RG Trigger: Id=[%1:%2], Trigger=%3, Lat=%4, Lon=%5\r\n
0xb00002bd | TRK_RG GF State: Tracker=%1, Id=[%2:%3], State=%4, Lat=%5, Lon=%6\r\n
0xb00002be | TRK_RG BeginRegionLoad\r\n
0xb00002bf | TRK_RG EndRegionLoad: Lat=%1, Lon=%2, Radius=%3, Geofences=%4\r\n
0xb00002c0 | TRK_RG Start tracking for: AppId=[%1]\r\n
0xb00002c1 | TRK_RG Stop tracking for: AppId=[%1]\r\n
0xb00002c2 | TRK_%1 Start Tracking: Id=[%2:%3], Lat=%4, Lon=%5, Radius=%6, Dwelltime=%7ms, Start=%8, Duration=%9ms, Singleuse=%10\r\n
0xb00002c3 | TRK_%1 Stop Tracking: Id=[%2:%3]\r\n
0xb00002c4 | TRK_SW Active=%1, Distance=%2, Accuracy=%3\r\n
0xb00002c5 | TRK_RG Not Tracking: Id=[%1:%2], Lat=%3, Lon=%4, Radius=%5, Dwelltime=%6ms, Start=%7, Duration=%8ms, Singleuse=%9\r\n
0xb00002c6 | TRK_RG Tracker State: Tracker=%1, NewState=%2\r\n
0xb00002c7 | TRK_%1 Enable=%2\r\n
0xb00002c8 | TRK_RG Add to Trackers: Id=[%1:%2], Lat=%3, Lon=%4, Radius=%5, Dwelltime=%6ms, Start=%7, Duration=%8ms, Singleuse=%9 {TrackedGeofencesCount=%10,InternalTrackedGeofencesCount=%11}\r\n
0xb00002c9 | TRK_RG Remove from Trackers: Id=[%1:%2] {TrackedGeofencesCount=%3,InternalTrackedGeofencesCount=%4}\r\n
0xb0000320 | Location KPI : [%1]:  , TTFF = %2msec, Accuracy = %3m\r\n
0xb0000384 | GFStore Add: Id=[%1:%2], hr=%3 \r\n
0xb0000385 | GFStore Remove: Id=[%1:%2], hr=%3 \r\n
0xb0000386 | GFStore Update: Id=[%1:%2], TriggerState= %3, hr=%4 \r\n
0xb0000387 | GFStore Get Id=[%1:%2], hr=%3 \r\n
0xb0000388 | GFStore DeleteAll: AppId=%1, hr=%2 \r\n
0xb0000389 | GFStore GetAllGeofence: AppId=%1, Count=%2 hr=%3 \r\n
0xb000038a | GFStore GetClosestGeofence: Lat=%1, Lon=%2, AppCount=%3, GFCount=%4 TransGFCount= %5, hr=%6 \r\n
0xb000038b | GFStore DeleteApp: AppId=%1, hr=%2 \r\n
0xb000038c | GFStore Internal: Messsage=%1, hr=%2 \r\n
0xb000038d | GFStore GetAppID: AppContext= %1 AppId=%2, hr=%3 \r\n
0xb00003e8 | Location Geofence Power Scenario: [%1]:  , Start\r\n
0xb00003e9 | Location Geofence Power Scenario: [%1]:  , Stop\r\n
0xb000044c | Permission denied for client = %1. Unconditional = %2, Policy = %3, LegacyPolicy = %4, Master = %5, User = %6, UserLegacyPolicy = %7, App = %8, is app container = %9. UserSid = %10, Package = %11\r\n
0xb000044d | Permission denied because client was not found, client = %1. User = %2, Package = %3\r\n
0xb00004b0 | Disabling geofencing because we are entering into Disconnected standby\r\n
0xb00004b1 | Re-enabling geofencing because we are exiting Disconnected standby\r\n
0xb00004e2 | WiFiAcquire: Id[0x%1], InferenceResult[%2], PositionSource[%3], PositionStatus[%4]\r\n
0xb00004e3 | SUPL Reconfig: Trigger=%1, CurrentRegStatus=%2\r\n
0xd0000001 | OK\r\n
0xd0000002 | Not resolvable\r\n
0xd0000003 | Invalid parameter\r\n
0xd0000004 | Server Error\r\n
0xd0000005 | Invalid Server Response\r\n
0xd0000006 | Other failure\r\n
0xd0000007 | WinHttp: No CM Connection\r\n
0xd0000008 | WinHttp: Not Redirected\r\n
0xd0000009 | Connectivity Error\r\n
0xd000000a | ProviderHelper\r\n
0xd000000b | Session\r\n
0xd000000c | LocationInformation\r\n
0xd000000d | ServiceProxy\r\n
0xd000000e | Cpe\r\n
0xd000000f | CpeAcquireSingleShot\r\n
0xd0000010 | CpeAcquirePeriodicTracking\r\n
0xd0000011 | CpeAcquireDistanceTracking\r\n
0xd0000012 | WifiPe\r\n
0xd0000013 | WifiPeAdapter\r\n
0xd0000014 | WifiPeAcquireSingleShot\r\n
0xd0000015 | CellPe\r\n
0xd0000016 | CellPeAdapter\r\n
0xd0000017 | CellPeAcquireSingleShot\r\n
0xd0000018 | GnssPe\r\n
0xd0000019 | GnssPeAcquireSingleShot\r\n
0xd000001a | GnssPeAcquirePeriodicTracking\r\n
0xd000001b | GnssPeAcquireDistanceTracking\r\n
0xd000001c | GnssAdapter\r\n
0xd000001d | Crowdsource\r\n
0xd000001e | Invalid\r\n
0xd000001f | SingleShot\r\n
0xd0000020 | Distance\r\n
0xd0000021 | Periodic\r\n
0xd0000022 | Geofence\r\n
0xd0000023 | Passive\r\n
0xd0000024 | AccuracySpecific\r\n
0xd0000025 | AccuracyAny\r\n
0xd0000026 | AccuracyHighest\r\n
0xd0000027 | Unknown\r\n
0xd0000028 | Cpe\r\n
0xd0000029 | Gnss\r\n
0xd000002a | Wifi\r\n
0xd000002b | Cell\r\n
0xd000002c | Venue\r\n
0xd000002d | IpAddr\r\n
0xd000002e | User\r\n
0xd000002f | Legacy\r\n
0xd0000030 | SingleShot\r\n
0xd0000031 | Distance\r\n
0xd0000032 | Periodic\r\n
0xd0000033 | LKG\r\n
0xd0000034 | AccuracyHigh\r\n
0xd0000035 | AccuracyPowerOptimized\r\n
0xd0000036 | GenerateLast\r\n
0xd0000037 | GenerateFirst\r\n
0xd0000038 | GenerateBest\r\n
0xd0000039 | Inject\r\n
0xd000003a | Delete\r\n
0xd000003b | Purge\r\n
0xd000003c | Time\r\n
0xd000003d | Position\r\n
0xd000003e | Blob\r\n
0xd000003f | XTRA1\r\n
0xd0000040 | XTRA2\r\n
0xd0000041 | LTO\r\n
0xd0000042 | XTRA3\r\n
0xd0000043 | SingleShot\r\n
0xd0000044 | AreaTrigger\r\n
0xd0000045 | NoNotifyNoVerify\r\n
0xd0000046 | NotifyOnly\r\n
0xd0000047 | NotifyVerifyDefaultAllow\r\n
0xd0000048 | NotifyVerifyDefaultNotAllow\r\n
0xd0000049 | PrivacyOverride\r\n
0xd000004a | SUPL\r\n
0xd000004b | CP\r\n
0xd000004c | V2UPL\r\n
0xd000004d | Accept\r\n
0xd000004e | Deny\r\n
0xd000004f | Timeout\r\n
0xd0000050 | Unknown\r\n
0xd0000051 | CAN_Removed\r\n
0xd0000052 | Csp_Update\r\n
0xd0000053 | Cellular_Update\r\n
0xd0000054 | None\r\n
0xd0000055 | Deregistered\r\n
0xd0000056 | Searching\r\n
0xd0000057 | Home\r\n
0xd0000058 | Roaming\r\n
0xd0000059 | Partner\r\n
0xd000005a | Denied\r\n
0xd000005b | Unknown\r\n
0xd000005c | CSP\r\n
0xd000005d | UICC\r\n
0xd000005e | IMSI\r\n
0xd000005f | Unknown\r\n
0xd0000060 | Unregistered\r\n
0xd0000061 | Home\r\n
0xd0000062 | Attempting\r\n
0xd0000063 | Denied\r\n
0xd0000064 | Roaming\r\n
0xd0000065 | Domestic roaming\r\n
0xd0000066 | SetLocationServiceEnabled\r\n
0xd0000067 | SetLocationNIRequestAllowed\r\n
0xd0000068 | ForceSatelliteSystem\r\n
0xd0000069 | ForceOperationMode\r\n
0xd000006a | SetEngineKeepWarmPeriod\r\n
0xd000006b | SetEngineWarm\r\n
0xd000006c | SetEngineCold\r\n
0xd000006d | SetEngineHot\r\n
0xd000006e | ResetEngine\r\n
0xd000006f | ClearAgnssData\r\n
0xd0000070 | SetDefaultFixResponseTime\r\n
0xd0000071 | SetSuplVersion\r\n
0xd0000072 | SetNMEALogging\r\n
0xd0000073 | SetUplServerAccessInterval\r\n
0xd0000074 | SetNiTimeoutInterval\r\n
0xd0000075 | ResetGeofencesTracking\r\n
0xd0000076 | Any\r\n
0xd0000077 | MSA\r\n
0xd0000078 | MSB\r\n
0xd0000079 | MSS\r\n
0xd000007a | CellId\r\n
0xd000007b | AFLT\r\n
0xd000007c | OTDOA\r\n
0xd000007d | SEND_PLATFORM_CAPABILITY\r\n
0xd000007e | GET_DEVICE_CAPABILITY\r\n
0xd000007f | SEND_DRIVERCOMMAND\r\n
0xd0000080 | START_FIXSESSION\r\n
0xd0000081 | MODIFY_FIXSESSION\r\n
0xd0000082 | STOP_FIXSESSION\r\n
0xd0000083 | GET_FIXDATA\r\n
0xd0000084 | INJECT_AGNSS\r\n
0xd0000085 | LISTEN_AGNSS\r\n
0xd0000086 | LISTEN_ERROR\r\n
0xd0000087 | LISTEN_FAILOVER\r\n
0xd0000088 | LISTEN_CUSTOM\r\n
0xd0000089 | LISTEN_NI\r\n
0xd000008a | SET_SUPL_HSLP\r\n
0xd000008b | CONFIG_SUPL_CERT\r\n
0xd000008c | RESPOND_NI\r\n
0xd000008d | EXECUTE_CWTEST\r\n
0xd000008e | EXECUTE_SELFTEST\r\n
0xd000008f | GET_CHIPSETINFO\r\n
0xd0000090 | LISTEN_NMEA\r\n
0xd0000091 | SET_V2UPL_CONFIG\r\n
0xd0000092 | TimeBound\r\n
0xd0000093 | BestEffort\r\n
0xd0000094 | Low\r\n
0xd0000095 | Medium\r\n
0xd0000096 | High\r\n
0xd0000097 | None\r\n
0xd0000098 | Cell\r\n
0xd0000099 | WiFi\r\n
0xd000009a | All\r\n
0xd000009b | CellInference\r\n
0xd000009c | WiFiInference\r\n
0xd000009d | AgnssData\r\n
0xd000009e | ServerTimeData\r\n
0xd000009f | WebproxyTileRequest\r\n
0xd00000a0 | CrowdsourceData\r\n
0xd00000a1 | VenueTileRequest\r\n
0xd00000a2 | VenueModelRequest\r\n
0xd00000a3 | WebproxyCaller\r\n
0xd00000a4 | WebproxyInternal\r\n
0xd00000a5 | WebproxyWinHttp\r\n
0xd00000a6 | WinHttpResponseHeaderAvail\r\n
0xd00000a7 | WinHttpResponseReadComplete\r\n
0xd00000a8 | WinHttpResponseWriteComplete\r\n
0xd00000a9 | WinHttpRequestError\r\n
0xd00000aa | WinHttpRequestSendComplete\r\n
0xd00000ab | WinHttpOpenRequest\r\n
0xd00000ac | WinHttpSendRequest\r\n
0xd00000ad | WinHttpWriteData\r\n
0xd00000ae | WinHttpReceiveResponse\r\n
0xd00000af | WinHttpReadData\r\n
0xd00000b0 | WinHttpPayloadConversionFailed\r\n
0xd00000b1 | Start\r\n
0xd00000b2 | Stop\r\n
0xd00000b3 | StopByDisposed\r\n
0xd00000b4 | TryStart\r\n
0xd00000b5 | Execution\r\n
0xd00000b6 | PostStatusToApp\r\n
0xd00000b7 | PostPositionToApp\r\n
0xd00000b8 | Application\r\n
0xd00000b9 | Taskhost\r\n
0xd00000ba | LocationService\r\n
0xd00000bb | InternalGCW\r\n
0xd00000bc | None\r\n
0xd00000bd | Paused\r\n
0xd00000be | ResumedTombstone\r\n
0xd00000bf | ResumedFAS\r\n
0xd00000c0 | Starting\r\n
0xd00000c1 | Started\r\n
0xd00000c2 | Stopping\r\n
0xd00000c3 | Stopped\r\n
0xd00000c4 | Executing\r\n
0xd00000c5 | Disabled\r\n
0xd00000c6 | Ready\r\n
0xd00000c7 | Initializing\r\n
0xd00000c8 | NoData\r\n
0xd00000c9 | Unknown\r\n
0xd00000ca | Granted\r\n
0xd00000cb | Denied\r\n
0xd00000cc | Primary\r\n
0xd00000cd | Fallback\r\n
0xd00000ce | Unknown\r\n
0xd00000cf | Inside\r\n
0xd00000d0 | Outside\r\n
0xd00000d1 | Unknown\r\n
0xd00000d2 | Enter\r\n
0xd00000d3 | Exit\r\n
0xd00000d4 | Removed\r\n
0xd00000d5 | ??\r\n
0xd00000d6 | SW\r\n
0xd00000d7 | HW\r\n
0xd00000d8 | Unknown\r\n
0xd00000d9 | Tracking\r\n
0xd00000da | NotTracking\r\n
0xd00000db | Geofence\r\n
0xd00000dc | GeofenceMonitor\r\n
0xd00000dd | Background\r\n
0xd00000de | Foreground\r\n
0xd00000df | Win32Event\r\n
0xd00000e0 | WnfEvent\r\n
0xd00000e1 | Unregister\r\n
0xd00000e2 | Register\r\n
0xd00000e3 | Used\r\n
0xd00000e4 | Expired\r\n
0xd00000e5 | NotTracking\r\n
0xd00000e6 | Tracking\r\n
0xd00000e7 | WiFiDisconnected\r\n
0xd00000e8 | WiFiConnected\r\n
0xd00000e9 | Unset\r\n
0xd00000ea | Enabled\r\n
0xd00000eb | Disabled\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x00000001 | Geolocation positioning is enabled.\r\n
0x00000002 | Geolocation positioning has been disabled by the user.\r\n
0x10000001 | Error\r\n
0x10000002 | Performance\r\n
0x10000003 | Selfhost\r\n
0x10000004 | WiFiTracing\r\n
0x10000005 | Init\r\n
0x10000006 | Position\r\n
0x10000007 | FixSession\r\n
0x10000008 | CompositePe\r\n
0x10000009 | Gnss\r\n
0x1000000a | CellPe\r\n
0x1000000b | WifiPe\r\n
0x1000000c | ClientApi\r\n
0x1000000d | Orion\r\n
0x1000000e | Supl\r\n
0x1000000f | Crowdsource\r\n
0x10000010 | ManagedApi\r\n
0x10000011 | GeofenceTracing\r\n
0x10000012 | GeofenceStore\r\n
0x1000001c | WebproxyTracing\r\n
0x1000001e | CellPeAdvanceTracing\r\n
0x1000001f | SpeedEstimatorTracing\r\n
0x10000020 | VenuePE\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x90000001 | LocationServiceProvider\r\n
0x90000002 | Debug\r\n
0xb000000d | WER Report: ExInfo[0]=%1, ExInfo[1]=%2, Result=%3\r\n
0xb000000e | Init[%1, %2]: %3 [%4]\r\n
0xb000000f | hr=%1, file=%2, line=%3\r\n
0xb0000010 | hr=%1, custommessage=%2, function=%3 callingcode=%4 filename=%5 line=%6\r\n
0xb0000011 | context=%1, component=%2, istakeref=%3\r\n
0xb0000064 | LS_REQUEST_LATLON: %1 %2, dwHint=%3 error=%4 \r\n
0xb0000065 | LS_REPORT_LATLON: error=%8, lat=%1, lon=%2, altitude=%3, hAccuracy=%4, vAccuracy=%5, heading=%6, velocity=%7\r\n
0xb00000c8 | GnssError hr=%1, eventType=%2, numBytesTransferred=%3, eventSize=%4\r\n
0xb00000c9 | Gnss[id=%1, Adapter] START %2: param=%3\r\n
0xb00000ca | Gnss[id=%1, Adapter] STOP\r\n
0xb00000cb | Gnss[id=%1, Driver] START %2: param=%3\r\n
0xb00000cc | Gnss[id=%1, Driver] STOP\r\n
0xb00000cd | Gnss[id=%1] POS: %3, Intermediate=%4, lat=%5, lon=%6, alt=%7, speed=%8, head=%9, hAccuracy=%10, vAccuracy=%11, speedAcc=%12, HDOP=%13, PDOP=%14, Status=%2\r\n
0xb00000ce | Gnss[id=%1, Driver] MOD %2: param=%3\r\n
0xb00000cf | Gnss[id=%1, Driver] Ioctl=%2, hr=%3, Duration=%4\r\n
0xb00000d0 | Gnss[id=%1] SAT: %2\r\n
0xb00000d1 | Gnss[id=%1, Driver] FixEventError hr=%2, numBytesTransferred=%3, fixlevelofdetails=%4, expectedMinBytes=%5, expectedMinSatelliteBytes=%6\r\n
0xb00000d2 | Session[%1,%2] START %3, IsClient=%9, Acquire[attached=%10, owner=%11], Age=%7, %4, AccuracyValue=%5, VenueMandatory=%8, Param=%6\r\n
0xb00000d3 | Session[%1,%2] STOP: hr=%3\r\n
0xb00000d4 | Session[%1,%2] POS: %5, Status=%3, SourcePe=%4, Intermediate=%6, lat=%7, lon=%8, HAcc=%9, Speed=%10, Floor=%11, Venue=%12\r\n
0xb00000d5 | Session[%1,%2] CallerName=%6, CallerProductId=%3, Sid=%4, PackageId=%5\r\n
0xb00000dc | Orion ServerTime: hr=%1, Report hr=%2, time=%3\r\n
0xb00000dd | Orion Agnss: hr=%1, Report hr=%2, BlobSize=%3\r\n
0xb00000de | Orion Inference: Winhttp hr=%1, Orion=%2, lat=%3, lon=%4, Accuracy=%5\r\n
0xb00000e6 | SUPL config: hslp=%1 (src=%2), hslp_from_imsi=%3\r\n
0xb00000e7 | V2UPL config: MPC=%1, PDE=%2, AppType=%3\r\n
0xb00000e8 | Set SUPL version: %1.%2\r\n
0xb00000e9 | Cert config: Action=%1, Name=%2, Size=%3\r\n
0xb00000ea | Driver cmd=%1, value=%2\r\n
0xb00000eb | Agnss Inject: type=%1, status=%2, dataSize=%3\r\n
0xb00000ec | NI Request: id=%1, type=%2, NotType=%3, Plane=%4\r\n
0xb00000ed | NI Response: id=%1, response=%2\r\n
0xb00000ee | Driver: ForceOperationMode=%1\r\n
0xb00000ef | Agnss Request: type=%1 %2\r\n
0xb00000f0 | SUPL Reconfig: Trigger=%1, CurrentRegStatus=%2\r\n
0xb00000f1 | Agnss Clear: type=%1\r\n
0xb00000f2 | Agnss Position Inject: status=%1, lat=%2, lon=%3, alt=%4, speed=%5, head=%6, hAccuracy=%7\r\n
0xb00000f3 | Agnss Time Inject: status=%1, Time=%2, Uncertainty=%3\r\n
0xb00000f4 | Agnss Blob Inject: status=%1, Version=%2, Format=%3, Size=%4\r\n
0xb00000f5 | GnssAdapt GFAdd Id=[%1:%2], hwId=%3 hr=%4\r\n
0xb00000f6 | GnssAdapt GFRemove: hwId=%1, hr=%2\r\n
0xb00000f7 | GnssAdapt GFResetTracking: hr=%1\r\n
0xb00000f8 | GnssAdapt GFEvent: id=%1, triggerState=%2\r\n
0xb00000f9 | GnssAdapt GFTrackingStatus: state=%1\r\n
0xb00000fa | SC GSM MCC=%1, MNC=%2, CID=%3, LAC=%4\r\n
0xb00000fb | SC UMTS MCC=%1, MNC=%2, CID=%3, LAC=%4\r\n
0xb00000fc | SC CDMA BaseLat=%1, BaseLong=%2, BSID=%3, NID=%4, SID=%5\r\n
0xb00000fd | SC LTE MCC=%1, MNC=%2, CID=%3\r\n
0xb00000fe | Neighbors: %1\r\n
0xb00000ff | SC TDSCDMA MCC=%1, MNC=%2, LAC=%3, CID=%4\r\n
0xb0000100 | [Cell Adapter]Cell Location update noficiation: Parms = %1, Exe= %2, UiccApp = %3, LAC=%4, TAC = %5, CID=%6\r\n
0xb0000101 | [Cell Adapter]Cell Location update notification Error state, hr =%1\r\n
0xb0000102 | Neighbors Used: %1\r\n
0xb0000103 | IsMulticellUsed=%1\r\n
0xb0000104 | Mac Address=%1, Signal Strength=%2\r\n
0xb0000105 | Wifi Change: Name=%1, State=%2\r\n
0xb0000106 | Wifi MACs:%1\r\n
0xb0000109 | GnssAdapt GnssError Error=%1, Recoverable=%2, Description=%3\r\n
0xb000010a | GnssAdapt DeviceAvailable = %1, SymbolicLink=%2, DeviceInUse=%3, hr= %4\r\n
0xb000010b | GnssPnPManager Device Arrival SymbolicLink= %1, IsExternal=%2\r\n
0xb000010c | GnssPnPManager Device Removal SymbolicLink= %1, IsExternal=%2\r\n
0xb000010d | GnssPnPManager Retrying for SymbolicLink= %1\r\n
0xb000010e | Server Cache IsHit=%1, PE=%2\r\n
0xb000010f | Tile Cache IsHit=%1, PE=%2\r\n
0xb0000110 | %1 Scan: Result=%2\r\n
0xb0000111 | [VenuePE] Id=[%1], Positions:[%2]\r\n
0xb0000112 | [VenuePE] IsInsideVenue=%1, Pos[Lat=%2,Lon=%3,Acc=%4,Source=%5]\r\n
0xb0000118 | [CS]InitializeDcpProfile: DcpProfile=%1, hr=%2\r\n
0xb0000119 | [CS]SubmitData: SizeInBytes=%1, DcpProfile=%2, hr=%3\r\n
0xb000011a | [CS]DataReceived: SourcePE=%1, IsReadyForData=%2, IsValidData=%3, hr=%4\r\n
0xb000011b | [CS]RawDataProcessing begins: DataListSize =%1, IsCollectionActive=%2\r\n
0xb000011c | [CS]State: Level=%1, CollectionType=%2, IsBufferFull=%3 IsBatterySavings=%4 IsUserPresenceOn=%5\r\n
0xb0000122 | Acquire[Id=%2, Cpe] SelectedPes: PrimaryPe=%1\r\n
0xb0000123 | Acquire[Id=%4, Cpe] StartPrimitivePes with Role=%1, Remaining time=%2, hr=%3\r\n
0xb0000124 | Acquire[Id=%4, Cpe] AttemptFallback with best available position Status=%1, Sourcepe=%2, AccuracyValue=%3\r\n
0xb0000126 | Acquire[Id=%14, Cpe] DT: Wait: Dist(m)=%1, IsSpeedUnknown=%12, SpeedUsed(m/s)=%2, IsMDUsed=%3, MDPrecision(m)=%4, Speed_Wait(s)=%5, MD_Wait(s)=%6, MinWait_Budget(s)=%7, SelectedWait(s)=%8, TimeBoundApplied=%13 {Cumulative Runningtime(s)=%9, Acqtime(s)=%10, Requests=%11}\r\n
0xb0000127 | [Cpe] New SpeedEstimate Speed(m/s)=%1, Bearing=%2, Positions=%3\r\n
0xb0000128 | [Cpe] SpeedEstimate Input: Timestamp=%1, Latitude=%2, Longitude=%3, Accuracy=%4\r\n
0xb000012a | Acquire[Id=%5, Cpe] Unreliable position {acc=%1, sourcepe=%2} detected on validation with position{acc=%3, sourcepe=%4} \r\n
0xb000012b | [Cpe] TotalPeCount=%1, AvailPes=[%2,%3,%4,%5,%6,%7]\r\n
0xb000012c | [%1] [%2], URL=%4, TrackingId=%6\r\n
0xb000012d | [%1] [%2]: Coordinate=[%3, %4], Acc=%7, Floor=%8, VenueId=%9, ServerStatus=[%5], WinHttpStatus=[%6], ProtocolStatus=[%11], OrionSource=[%12]\r\n
0xb000012f | [%1] [%2]: ServerStatus=[%3], WinHttpStatus=[%4], ProtocolStatus=[%6]\r\n
0xb0000130 | [%1] [%2]: ServerStatus=[%3], WinHttpStatus=[%4], ProtocolStatus=[%6]\r\n
0xb0000132 | [%1] [%2] Canceled By [%3], Status=[%4]\r\n
0xb0000133 | [%1]: Request=[%2], WinhttpHandle=[%3], WinHttpEvent=[%4], Status=[%5]\r\n
0xb0000134 | [%1]: Request=[%2], WinhttpHandle=[%3], WinHttpAPI=[%4], Status=[%5]\r\n
0xb0000135 | Request=[%2]\r\n
0xb0000136 | Response=[%2]\r\n
0xb0000137 | Set SUPL version: %1.%2.%3\r\n
0xb0000191 | [Cpe] MD: Start MD, hr=%1, hrwifi=%2, hrcell=%3, wifi{ConnState=%4, ThrottlingOn=%5, Elapsedtime(s)=%6}, cell{ThrottlingOn=%7, Elapsedtime(s)=%8} ActivityDetection{ThrottlingOn=%9, Elapsedtime(s)=%10}\r\n
0xb0000192 | [Cpe] MD: Stop MD, hr =%1 \r\n
0xb0000193 | [Cpe] MD: Notify potential movement, hr =%1 \r\n
0xb0000194 | [Cpe] MD: Notify state changed, hr =%1 \r\n
0xb0000195 | [Cpe] MD: Get movementPrecision hr=%1, wifi{ConnState=%2, ThrottlingOn=%3, Elapsedtime=%4}, cell{ThrottlingOn=%5, Elapsedtime=%6} AD={ThrottlingOn=%7, Elapsedtime=%8}\r\n
0xb0000196 | Acquire[Id=%3, Cpe] StartTracking on Pe=%1, IsPrimaryNativeTracking=%2\r\n
0xb0000197 | [Cpe] SessionType=%1, IsSupportsNativePT=%2, IsSupportsNativeDT=%3, IsSupportsRequest=%4\r\n
0xb00001f4 | GeolocationStartOperation[%1] SessionType=%2, Age(ms)=%3, Accuracy(m)=%4, RequestParameter=%5\r\n
0xb00001f5 | GeolocationStartOperation[%1] Status=%2\r\n
0xb00001f6 | GeolocationEventHandler[%1] PositionStatus=%2, Latitude=%3, Longitude=%4, HAccuracy=%5, Status=%6\r\n
0xb00001f7 | GeolocationStopTrackingOperation[%1] Status=%2\r\n
0xb00001f8 | GeolocationPromptAppState State=%1\r\n
0xb000020d | GFClient Add Geofence at Index = %1, Lat=%2, Lon=%3, Radius =%4, Starttime=%5, Duration=%6, Dwelltime=%7, SingleUse=%8\r\n
0xb000020e | GFClient Remove Geofence at Index = %1, Lat=%2, Lon=%3, Radius =%4, Starttime=%5, Duration=%6, Dwelltime=%7, SingleUse=%8\r\n
0xb000020f | GFClient Clear all Geofences\r\n
0xb0000210 | GFClient Register for %1 changes \r\n
0xb0000211 | GFClient Unregister for %1 changes\r\n
0xb0000212 | GFClient Read Geofence reports\r\n
0xb0000213 | GFClient Event signalled on client for %1\r\n
0xb0000214 | GFClient Create location trigger \r\n
0xb0000215 | GFClient Delete location trigger \r\n
0xb0000216 | GFClient  Geofence: Id=[%1:%2] Lat=%3, Lon=%4, Radius=%5, Starttime=%6, Duration=%7, Dwelltime=%8, SingleUse=%9 \r\n
0xb0000226 | GeofenceOperation[%1] Status=%2\r\n
0xb0000227 | GFAppBoundary GeofenceOperation[%1] ClientId=%2, EventId=%3, Status=%4\r\n
0xb0000228 | GFAppBoundary %3 %2 %1Event: PID=%4, AppId=%5, EventId=%6, Status=%7\r\n
0xb0000229 | GFAppBoundary  AddGeofence: CallerName=%11, Id=[%1:%2] Lat=%3, Lon=%4, Radius=%5, Starttime=%6, Duration=%7, Dwelltime=%8, SingleUse=%9, hr=%10\r\n
0xb000022a | GFAppBoundary  RemoveGeofence: CallerName=%4, Id=[%1:%2], hr = %3\r\n
0xb000022b | GFAppBoundary  RemoveAllGeofences: CallerName=%3, AppId=%1, hr = %2\r\n
0xb000022c | GFAppBoundary  ListAllGeofences: AppId=%1, GeofencesCount=%2, hr=%3\r\n
0xb000022d | GFAppBoundary  ReadGeofenceReports: AppId=%1, GeofenceReportsCount=%2, hr=%3\r\n
0xb000022e | GFClient  GeofenceReport: GfId=%1, Trigger=%2, RemovalReason=%3, Status=%4, Lat=%5, Lon=%6, HAcc=%7\r\n
0xb000022f | GFAppBoundary  ForegroundEventFired ForegroundEventType=%1\r\n
0xb0000230 | GFAppBoundary  BackgroundEventSignalled ClientId=%1, EventId=%2, hr=%3\r\n
0xb0000258 | GCW: Instance=[%1], Type=[%2], Source=[%3], Taskhost=[%4], CurrentState=[%5], Timeout=[%6]\r\n
0xb0000259 | GCW: Instance=[%1], GeoStatus=[%2], GeoPermission=[%3]\r\n
0xb00002bc | TRK_RG Trigger: Id=[%1:%2], Trigger=%3, Lat=%4, Lon=%5\r\n
0xb00002bd | TRK_RG GF State: Tracker=%1, Id=[%2:%3], State=%4, Lat=%5, Lon=%6\r\n
0xb00002be | TRK_RG BeginRegionLoad\r\n
0xb00002bf | TRK_RG EndRegionLoad: Lat=%1, Lon=%2, Radius=%3, Geofences=%4\r\n
0xb00002c0 | TRK_RG Start tracking for: AppId=[%1]\r\n
0xb00002c1 | TRK_RG Stop tracking for: AppId=[%1]\r\n
0xb00002c2 | TRK_%1 Start Tracking: Id=[%2:%3], Lat=%4, Lon=%5, Radius=%6, Dwelltime=%7ms, Start=%8, Duration=%9ms, Singleuse=%10\r\n
0xb00002c3 | TRK_%1 Stop Tracking: Id=[%2:%3]\r\n
0xb00002c4 | TRK_SW Active=%1, Distance=%2, Accuracy=%3\r\n
0xb00002c5 | TRK_RG Not Tracking: Id=[%1:%2], Lat=%3, Lon=%4, Radius=%5, Dwelltime=%6ms, Start=%7, Duration=%8ms, Singleuse=%9\r\n
0xb00002c6 | TRK_RG Tracker State: Tracker=%1, NewState=%2\r\n
0xb00002c7 | TRK_%1 Enable=%2\r\n
0xb00002c8 | TRK_RG Add to Trackers: Id=[%1:%2], Lat=%3, Lon=%4, Radius=%5, Dwelltime=%6ms, Start=%7, Duration=%8ms, Singleuse=%9 {TrackedGeofencesCount=%10,InternalTrackedGeofencesCount=%11}\r\n
0xb00002c9 | TRK_RG Remove from Trackers: Id=[%1:%2] {TrackedGeofencesCount=%3,InternalTrackedGeofencesCount=%4}\r\n
0xb0000320 | Location KPI : [%1]:  , TTFF = %2msec, Accuracy = %3m\r\n
0xb0000384 | GFStore Add: Id=[%1:%2], hr=%3 \r\n
0xb0000385 | GFStore Remove: Id=[%1:%2], hr=%3 \r\n
0xb0000386 | GFStore Update: Id=[%1:%2], TriggerState= %3, hr=%4 \r\n
0xb0000387 | GFStore Get Id=[%1:%2], hr=%3 \r\n
0xb0000388 | GFStore DeleteAll: AppId=%1, hr=%2 \r\n
0xb0000389 | GFStore GetAllGeofence: AppId=%1, Count=%2 hr=%3 \r\n
0xb000038a | GFStore GetClosestGeofence: Lat=%1, Lon=%2, AppCount=%3, GFCount=%4 TransGFCount= %5, hr=%6 \r\n
0xb000038b | GFStore DeleteApp: AppId=%1, hr=%2 \r\n
0xb000038c | GFStore Internal: Messsage=%1, hr=%2 \r\n
0xb000038d | GFStore GetAppID: AppContext= %1 AppId=%2, hr=%3 \r\n
0xb00003e8 | Location Geofence Power Scenario: [%1]:  , Start\r\n
0xb00003e9 | Location Geofence Power Scenario: [%1]:  , Stop\r\n
0xb000044c | Permission denied for client = %1. Unconditional = %2, Policy = %3, LegacyPolicy = %4, Master = %5, User = %6, UserLegacyPolicy = %7, App = %8, is app container = %9. UserSid = %10, Package = %11\r\n
0xb000044d | Permission denied because client was not found, client = %1. User = %2, Package = %3\r\n
0xb00004b0 | Disabling geofencing because we are entering into Disconnected standby\r\n
0xb00004b1 | Re-enabling geofencing because we are exiting Disconnected standby\r\n
0xb00004e2 | WiFiAcquire: Id[0x%1], InferenceResult[%2], PositionSource[%3], PositionStatus[%4]\r\n
0xb00004e3 | SUPL Reconfig: Trigger=%1, CurrentRegStatus=%2\r\n
0xd0000001 | OK\r\n
0xd0000002 | Not resolvable\r\n
0xd0000003 | Invalid parameter\r\n
0xd0000004 | Server Error\r\n
0xd0000005 | Invalid Server Response\r\n
0xd0000006 | Other failure\r\n
0xd0000007 | WinHttp: No CM Connection\r\n
0xd0000008 | WinHttp: Not Redirected\r\n
0xd0000009 | Connectivity Error\r\n
0xd000000a | ProviderHelper\r\n
0xd000000b | Session\r\n
0xd000000c | LocationInformation\r\n
0xd000000d | ServiceProxy\r\n
0xd000000e | Cpe\r\n
0xd000000f | CpeAcquireSingleShot\r\n
0xd0000010 | CpeAcquirePeriodicTracking\r\n
0xd0000011 | CpeAcquireDistanceTracking\r\n
0xd0000012 | WifiPe\r\n
0xd0000013 | WifiPeAdapter\r\n
0xd0000014 | WifiPeAcquireSingleShot\r\n
0xd0000015 | CellPe\r\n
0xd0000016 | CellPeAdapter\r\n
0xd0000017 | CellPeAcquireSingleShot\r\n
0xd0000018 | GnssPe\r\n
0xd0000019 | GnssPeAcquireSingleShot\r\n
0xd000001a | GnssPeAcquirePeriodicTracking\r\n
0xd000001b | GnssPeAcquireDistanceTracking\r\n
0xd000001c | GnssAdapter\r\n
0xd000001d | Crowdsource\r\n
0xd000001e | Invalid\r\n
0xd000001f | SingleShot\r\n
0xd0000020 | Distance\r\n
0xd0000021 | Periodic\r\n
0xd0000022 | Geofence\r\n
0xd0000023 | Passive\r\n
0xd0000024 | AccuracySpecific\r\n
0xd0000025 | AccuracyAny\r\n
0xd0000026 | AccuracyHighest\r\n
0xd0000027 | Unknown\r\n
0xd0000028 | Cpe\r\n
0xd0000029 | Gnss\r\n
0xd000002a | Wifi\r\n
0xd000002b | Cell\r\n
0xd000002c | Venue\r\n
0xd000002d | IpAddr\r\n
0xd000002e | User\r\n
0xd000002f | Legacy\r\n
0xd0000030 | SingleShot\r\n
0xd0000031 | Distance\r\n
0xd0000032 | Periodic\r\n
0xd0000033 | LKG\r\n
0xd0000034 | AccuracyHigh\r\n
0xd0000035 | AccuracyPowerOptimized\r\n
0xd0000036 | GenerateLast\r\n
0xd0000037 | GenerateFirst\r\n
0xd0000038 | GenerateBest\r\n
0xd0000039 | Inject\r\n
0xd000003a | Delete\r\n
0xd000003b | Purge\r\n
0xd000003c | Time\r\n
0xd000003d | Position\r\n
0xd000003e | Blob\r\n
0xd000003f | XTRA1\r\n
0xd0000040 | XTRA2\r\n
0xd0000041 | LTO\r\n
0xd0000042 | XTRA3\r\n
0xd0000043 | SingleShot\r\n
0xd0000044 | AreaTrigger\r\n
0xd0000045 | NoNotifyNoVerify\r\n
0xd0000046 | NotifyOnly\r\n
0xd0000047 | NotifyVerifyDefaultAllow\r\n
0xd0000048 | NotifyVerifyDefaultNotAllow\r\n
0xd0000049 | PrivacyOverride\r\n
0xd000004a | SUPL\r\n
0xd000004b | CP\r\n
0xd000004c | V2UPL\r\n
0xd000004d | Accept\r\n
0xd000004e | Deny\r\n
0xd000004f | Timeout\r\n
0xd0000050 | Unknown\r\n
0xd0000051 | CAN_Removed\r\n
0xd0000052 | Csp_Update\r\n
0xd0000053 | Cellular_Update\r\n
0xd0000054 | None\r\n
0xd0000055 | Deregistered\r\n
0xd0000056 | Searching\r\n
0xd0000057 | Home\r\n
0xd0000058 | Roaming\r\n
0xd0000059 | Partner\r\n
0xd000005a | Denied\r\n
0xd000005b | Unknown\r\n
0xd000005c | CSP\r\n
0xd000005d | UICC\r\n
0xd000005e | IMSI\r\n
0xd000005f | Unknown\r\n
0xd0000060 | Unregistered\r\n
0xd0000061 | Home\r\n
0xd0000062 | Attempting\r\n
0xd0000063 | Denied\r\n
0xd0000064 | Roaming\r\n
0xd0000065 | Domestic roaming\r\n
0xd0000066 | SetLocationServiceEnabled\r\n
0xd0000067 | SetLocationNIRequestAllowed\r\n
0xd0000068 | ForceSatelliteSystem\r\n
0xd0000069 | ForceOperationMode\r\n
0xd000006a | SetEngineKeepWarmPeriod\r\n
0xd000006b | SetEngineWarm\r\n
0xd000006c | SetEngineCold\r\n
0xd000006d | SetEngineHot\r\n
0xd000006e | ResetEngine\r\n
0xd000006f | ClearAgnssData\r\n
0xd0000070 | SetDefaultFixResponseTime\r\n
0xd0000071 | SetSuplVersion\r\n
0xd0000072 | SetNMEALogging\r\n
0xd0000073 | SetUplServerAccessInterval\r\n
0xd0000074 | SetNiTimeoutInterval\r\n
0xd0000075 | ResetGeofencesTracking\r\n
0xd0000076 | SetSuplVersion2\r\n
0xd0000077 | Any\r\n
0xd0000078 | MSA\r\n
0xd0000079 | MSB\r\n
0xd000007a | MSS\r\n
0xd000007b | CellId\r\n
0xd000007c | AFLT\r\n
0xd000007d | OTDOA\r\n
0xd000007e | SEND_PLATFORM_CAPABILITY\r\n
0xd000007f | GET_DEVICE_CAPABILITY\r\n
0xd0000080 | SEND_DRIVERCOMMAND\r\n
0xd0000081 | START_FIXSESSION\r\n
0xd0000082 | MODIFY_FIXSESSION\r\n
0xd0000083 | STOP_FIXSESSION\r\n
0xd0000084 | GET_FIXDATA\r\n
0xd0000085 | INJECT_AGNSS\r\n
0xd0000086 | LISTEN_AGNSS\r\n
0xd0000087 | LISTEN_ERROR\r\n
0xd0000088 | LISTEN_FAILOVER\r\n
0xd0000089 | LISTEN_CUSTOM\r\n
0xd000008a | LISTEN_NI\r\n
0xd000008b | SET_SUPL_HSLP\r\n
0xd000008c | CONFIG_SUPL_CERT\r\n
0xd000008d | RESPOND_NI\r\n
0xd000008e | EXECUTE_CWTEST\r\n
0xd000008f | EXECUTE_SELFTEST\r\n
0xd0000090 | GET_CHIPSETINFO\r\n
0xd0000091 | LISTEN_NMEA\r\n
0xd0000092 | SET_V2UPL_CONFIG\r\n
0xd0000093 | TimeBound\r\n
0xd0000094 | BestEffort\r\n
0xd0000095 | Low\r\n
0xd0000096 | Medium\r\n
0xd0000097 | High\r\n
0xd0000098 | None\r\n
0xd0000099 | Cell\r\n
0xd000009a | WiFi\r\n
0xd000009b | All\r\n
0xd000009c | CellInference\r\n
0xd000009d | WiFiInference\r\n
0xd000009e | AgnssData\r\n
0xd000009f | ServerTimeData\r\n
0xd00000a0 | WebproxyTileRequest\r\n
0xd00000a1 | CrowdsourceData\r\n
0xd00000a2 | VenueTileRequest\r\n
0xd00000a3 | VenueModelRequest\r\n
0xd00000a4 | WebproxyCaller\r\n
0xd00000a5 | WebproxyInternal\r\n
0xd00000a6 | WebproxyWinHttp\r\n
0xd00000a7 | WinHttpResponseHeaderAvail\r\n
0xd00000a8 | WinHttpResponseReadComplete\r\n
0xd00000a9 | WinHttpResponseWriteComplete\r\n
0xd00000aa | WinHttpRequestError\r\n
0xd00000ab | WinHttpRequestSendComplete\r\n
0xd00000ac | WinHttpOpenRequest\r\n
0xd00000ad | WinHttpSendRequest\r\n
0xd00000ae | WinHttpWriteData\r\n
0xd00000af | WinHttpReceiveResponse\r\n
0xd00000b0 | WinHttpReadData\r\n
0xd00000b1 | WinHttpPayloadConversionFailed\r\n
0xd00000b2 | Start\r\n
0xd00000b3 | Stop\r\n
0xd00000b4 | StopByDisposed\r\n
0xd00000b5 | TryStart\r\n
0xd00000b6 | Execution\r\n
0xd00000b7 | PostStatusToApp\r\n
0xd00000b8 | PostPositionToApp\r\n
0xd00000b9 | Application\r\n
0xd00000ba | Taskhost\r\n
0xd00000bb | LocationService\r\n
0xd00000bc | InternalGCW\r\n
0xd00000bd | None\r\n
0xd00000be | Paused\r\n
0xd00000bf | ResumedTombstone\r\n
0xd00000c0 | ResumedFAS\r\n
0xd00000c1 | Starting\r\n
0xd00000c2 | Started\r\n
0xd00000c3 | Stopping\r\n
0xd00000c4 | Stopped\r\n
0xd00000c5 | Executing\r\n
0xd00000c6 | Disabled\r\n
0xd00000c7 | Ready\r\n
0xd00000c8 | Initializing\r\n
0xd00000c9 | NoData\r\n
0xd00000ca | Unknown\r\n
0xd00000cb | Granted\r\n
0xd00000cc | Denied\r\n
0xd00000cd | Primary\r\n
0xd00000ce | Fallback\r\n
0xd00000cf | Unknown\r\n
0xd00000d0 | Inside\r\n
0xd00000d1 | Outside\r\n
0xd00000d2 | Unknown\r\n
0xd00000d3 | Enter\r\n
0xd00000d4 | Exit\r\n
0xd00000d5 | Removed\r\n
0xd00000d6 | ??\r\n
0xd00000d7 | SW\r\n
0xd00000d8 | HW\r\n
0xd00000d9 | Unknown\r\n
0xd00000da | Tracking\r\n
0xd00000db | NotTracking\r\n
0xd00000dc | Geofence\r\n
0xd00000dd | GeofenceMonitor\r\n
0xd00000de | Background\r\n
0xd00000df | Foreground\r\n
0xd00000e0 | Win32Event\r\n
0xd00000e1 | WnfEvent\r\n
0xd00000e2 | Unregister\r\n
0xd00000e3 | Register\r\n
0xd00000e4 | Used\r\n
0xd00000e5 | Expired\r\n
0xd00000e6 | NotTracking\r\n
0xd00000e7 | Tracking\r\n
0xd00000e8 | WiFiDisconnected\r\n
0xd00000e9 | WiFiConnected\r\n
0xd00000ea | Unset\r\n
0xd00000eb | Enabled\r\n
0xd00000ec | Disabled\r\n
