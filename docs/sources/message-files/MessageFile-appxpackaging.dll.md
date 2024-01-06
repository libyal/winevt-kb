## appxpackaging.dll

Path: %SystemRoot%\System32\AppxPackaging.dll

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4.\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2.\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "windows.backgroundTasks" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo attribute if the LockScreen element is specified.\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The OSMaxVersionTested value must not be less than the OSMinVersion value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value if absolute URI, must only specify the "https" scheme.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "windows.backgroundTasks" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for OSMinVersion specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct OSMinVersion specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: ResourcePackage must not specify multiple Resource elements.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 6.3.9600.16481

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The OSMaxVersionTested value must not be less than the OSMinVersion value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value if absolute URI, must only specify the "https" scheme.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "windows.backgroundTasks" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for OSMinVersion specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct OSMinVersion specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: ResourcePackage must not specify multiple Resource elements.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb00000b4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify the "%5" attribute.\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute or relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The max version tested value must not be less than the min version value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "https" scheme if it's an absolute URI.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for OSMinVersion specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct OSMinVersion specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: Only one type of resource qualifier can be specified for a resource package.  Attribute %4 must be the same as attribute %5 on element %6.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000a5 | error %1: An encrypted app package (ID = %2) in the bundle could not be signed.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb00000b4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify the "%5" attribute.\r\n
0xb00000b5 | The reader was created successfully without manifest validation.\r\n
0xb00000b6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The StartPage attribute must be a valid URI.\r\n
0xb00000b7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Executable attribute for the windows.backgroundTask extension must be "wwahost.exe" when StartPage is specified.\r\n
0xb00000b8 | error %1: The chaining mode string for encryption algorithm cannot be empty.\r\n
0xb00000b9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The WindowsRuntimeAccess attribute must not be specified if the Type attribute value is "exclude".\r\n
0xb00000ba | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http", "https" or "ms-appx-web" scheme if it's an absolute URI.\r\n
0xb00000bb | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http" or "https" scheme if it's an absolute URI and the Type attribute value is "exclude".\r\n
0xb00000bc | error %1: App manifest validation error: Line %2, Column %3, Reason: The Url specified is a duplicate of the base Url specified for the windows.webAccountProvider extension\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xb000018f | The bundle reader was created successfully without manifest validation.\r\n
0xb0000190 | Checking Eappx SIP support for file\r\n
0xb0000191 | Check for Eappx SIP support completed\r\n
0xb0000192 | Returning signature or signature size from encrypted app package\r\n
0xb0000193 | Signature or signature size returned from encrypted app package\r\n
0xb0000194 | Adding signature to encrypted app package\r\n
0xb0000195 | Signature added to encrypted app package\r\n
0xb0000196 | Removing signature from encrypted app package\r\n
0xb0000197 | Signature removed from encrypted app package\r\n
0xb0000198 | Creating or sizing encrypted app indirect data\r\n
0xb0000199 | Encrypted app indirect data created or sized\r\n
0xb000019a | Verifying encrypted app indirect data\r\n
0xb000019b | Encrypted app indirect data verified\r\n
0xb000019c | Checking EappxBundle SIP support for file\r\n
0xb000019d | Check for EappxBundle SIP support completed\r\n
0xb000019e | Returning signature or signature size from encrypted app bundle\r\n
0xb000019f | Signature or signature size returned from encrypted app bundle\r\n
0xb00001a0 | Adding signature to encrypted app bundle\r\n
0xb00001a1 | Signature added to encrypted app bundle\r\n
0xb00001a2 | Removing signature from encrypted app bundle\r\n
0xb00001a3 | Signature removed from encrypted app bundle\r\n
0xb00001a4 | Creating or sizing encrypted bundle indirect data\r\n
0xb00001a5 | Encrypted bundle indirect data created or sized\r\n
0xb00001a6 | Verifying encrypted bundle indirect data\r\n
0xb00001a7 | Encrypted bundle indirect data verified\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute or relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The max version tested value must not be less than the min version value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "https" scheme if it's an absolute URI.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for OSMinVersion specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct OSMinVersion specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: Only one type of resource qualifier can be specified for a resource package.  Attribute %4 must be the same as attribute %5 on element %6.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000a5 | error %1: An encrypted app package (ID = %2) in the bundle could not be signed.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb00000b4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify the "%5" attribute.\r\n
0xb00000b5 | The reader was created successfully without manifest validation.\r\n
0xb00000b6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The StartPage attribute must be a valid URI.\r\n
0xb00000b7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Executable attribute for the windows.backgroundTask extension must be "wwahost.exe" when StartPage is specified.\r\n
0xb00000b8 | error %1: The chaining mode string for encryption algorithm cannot be empty.\r\n
0xb00000b9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The WindowsRuntimeAccess attribute must not be specified if the Type attribute value is "exclude".\r\n
0xb00000ba | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http", "https" or "ms-appx-web" scheme if it's an absolute URI.\r\n
0xb00000bb | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http" or "https" scheme if it's an absolute URI and the Type attribute value is "exclude".\r\n
0xb00000bc | error %1: App manifest validation error: Line %2, Column %3, Reason: The Url specified is a duplicate of the base Url specified for the windows.webAccountProvider extension\r\n
0xb00000bd | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP manifests.\r\n
0xb00000be | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP desktop applications whose minVersion >= 10.0.14257.0.\r\n
0xb00000bf | error %1: App manifest validation error: Line %2, Column %3, Reason: The element specified requires "%4" capability.\r\n
0xb00000c0 | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency can't be specified when the %4 element is specified.\r\n
0xb00000c1 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't target version %5 of device family "%4".  You must specify a higher MinVersion.\r\n
0xb00000c3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The use of startuptask extension requires the containing Application use the Windows.FullTrustApplication entry point.\r\n
0xb00000c4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c5 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in prototype element if in a full trust application.\r\n
0xb00000c6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in verb element if in a full trust application.\r\n
0xb00000c8 | error %1: App manifest validation error: Line %2, Column %3, Reason: AppExecutionAlias can only be used by Centennial Applications.\r\n
0xb00000c9 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" extension.\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xb000018f | The bundle reader was created successfully without manifest validation.\r\n
0xb0000190 | Checking Eappx SIP support for file\r\n
0xb0000191 | Check for Eappx SIP support completed\r\n
0xb0000192 | Returning signature or signature size from encrypted app package\r\n
0xb0000193 | Signature or signature size returned from encrypted app package\r\n
0xb0000194 | Adding signature to encrypted app package\r\n
0xb0000195 | Signature added to encrypted app package\r\n
0xb0000196 | Removing signature from encrypted app package\r\n
0xb0000197 | Signature removed from encrypted app package\r\n
0xb0000198 | Creating or sizing encrypted app indirect data\r\n
0xb0000199 | Encrypted app indirect data created or sized\r\n
0xb000019a | Verifying encrypted app indirect data\r\n
0xb000019b | Encrypted app indirect data verified\r\n
0xb000019c | Checking EappxBundle SIP support for file\r\n
0xb000019d | Check for EappxBundle SIP support completed\r\n
0xb000019e | Returning signature or signature size from encrypted app bundle\r\n
0xb000019f | Signature or signature size returned from encrypted app bundle\r\n
0xb00001a0 | Adding signature to encrypted app bundle\r\n
0xb00001a1 | Signature added to encrypted app bundle\r\n
0xb00001a2 | Removing signature from encrypted app bundle\r\n
0xb00001a3 | Signature removed from encrypted app bundle\r\n
0xb00001a4 | Creating or sizing encrypted bundle indirect data\r\n
0xb00001a5 | Encrypted bundle indirect data created or sized\r\n
0xb00001a6 | Verifying encrypted bundle indirect data\r\n
0xb00001a7 | Encrypted bundle indirect data verified\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 10.0.15063.0

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x3037000b | Parse CGM\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x70000037 | Content Group Map\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute or relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The max version tested value must not be less than the min version value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "https" scheme if it's an absolute URI.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for MaxVersionTested specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct MaxVersionTested specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: Only one type of resource qualifier can be specified for a resource package.  Attribute %4 must be the same as attribute %5 on element %6.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000a5 | error %1: An encrypted app package (ID = %2) in the bundle could not be signed.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb00000b4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify the "%5" attribute.\r\n
0xb00000b5 | The reader was created successfully without manifest validation.\r\n
0xb00000b6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The StartPage attribute must be a valid URI.\r\n
0xb00000b7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Executable attribute for the windows.backgroundTask extension must be "wwahost.exe" when StartPage is specified.\r\n
0xb00000b8 | error %1: The chaining mode string for encryption algorithm cannot be empty.\r\n
0xb00000b9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The WindowsRuntimeAccess attribute must not be specified if the Type attribute value is "exclude".\r\n
0xb00000ba | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http", "https" or "ms-appx-web" scheme if it's an absolute URI.\r\n
0xb00000bb | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http" or "https" scheme if it's an absolute URI and the Type attribute value is "exclude".\r\n
0xb00000bc | error %1: App manifest validation error: Line %2, Column %3, Reason: The Url specified is a duplicate of the base Url specified for the windows.webAccountProvider extension\r\n
0xb00000bd | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP manifests.\r\n
0xb00000be | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP desktop applications whose minVersion >= 10.0.14257.0.\r\n
0xb00000bf | error %1: App manifest validation error: Line %2, Column %3, Reason: The element specified requires "%4" capability.\r\n
0xb00000c0 | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency can't be specified when the %4 element is specified.\r\n
0xb00000c1 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't target version %5 of device family "%4".  You must specify a higher MinVersion.\r\n
0xb00000c3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The use of startuptask extension requires the containing Application use the Windows.FullTrustApplication entry point.\r\n
0xb00000c4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c5 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in prototype element if in a full trust application.\r\n
0xb00000c6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in verb element if in a full trust application.\r\n
0xb00000c8 | error %1: App manifest validation error: Line %2, Column %3, Reason: AppExecutionAlias can only be used by Centennial Applications.\r\n
0xb00000c9 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" extension.\r\n
0xb00000ca | error %1: App manifest validation error: Line %2, Column %3, Reason: The Prog Id refrenced by the Class element must have for its CLSID the Class element id value.\r\n
0xb00000cb | error %1: App manifest validation error: Line %2, Column %3, Reason: The VersionIndependentProgId refrenced by the Class element must eventualy resolve in a Prog Id with CLSID matching the Class element id value.\r\n
0xb00000cc | error %1: App manifest validation error: Line %2, Column %3, Reason: Prog Id element can not have its own Id for CurrentVersion.\r\n
0xb00000cd | error %1: App manifest validation error: Line %2, Column %3, Reason: AutoConvertTo attribute of Class can not refer to its own id.\r\n
0xb00000ce | error %1: App manifest validation error: Line %2, Column %3, Reason: If InsertableObject is present then ProgId attribute must also be.\r\n
0xb00000cf | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormats element can not have both DefaultFormatName and DefaultStandardFormat attributes.\r\n
0xb00000d0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The TypeLib element must have either a Win32Path or a Win64Path child element.\r\n
0xb00000d1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormat element can not have both FormatName and StandardFormat attributes.\r\n
0xb00000d2 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Conversion element must have a Readable or ReadWritable child.\r\n
0xb00000d3 | error %1: App manifest validation error: Line %2, Column %3, Reason: If useUniversalMarshaler is true the following attributes should not also exist: ProxyStubClsid, AsynchronousInterface, SynchronousInterface\r\n
0xb00000d4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Interface child element typeLib's ID does not match a typeLib ID which also contains the child element's version number.\r\n
0xb00000d5 | error %1: App manifest validation error: Line %2, Column %3, Reason: Both AsynchronousInterface and SynchronousInterface can't exist in the same Interface element.\r\n
0xb00000d6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The AsynchronousInterface value should match the ID of an Interface with a SynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The SynchronousInterface value should match the ID of an Interface with a AsynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d8 | App manifest validation warning: Declared namespace %1 is inapplicable, it will be ignored during manifest processing.\r\n
0xb00000d9 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName attribute must be specified if ShellNewDisplayName attribute is specified.\r\n
0xb00000da | error %1: App manifest validation error: Line %2, Column %3, Reason: DdeExecCommand attribute must be specified if DdeExecApplication, DdeExecTopic or DdeExecIfExec attribute is specified.\r\n
0xb00000db | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dc | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dd | error %1: App manifest validation error: Line %2, Column %3, Reason: SystemSurrogate attribute and CustomSurrogateExecutable attribute are mutual exclusive.\r\n
0xb00000de | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency with name "%4" and publisher "%5" can't be specified multiple times.\r\n
0xb00000df | error %1: App manifest validation error: Line %2, Column %3, Reason: One and only one of AumId and ShortcutPath attribute should be declared.\r\n
0xb00000e0 | error %1: App manifest validation error: Line %2, Column %3, Reason: Either AppServiceName attribute or ActivatableClassId, Path attributes should be declared.\r\n
0xb00000e1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComServer SurrogateServer referenced by DesktopPropertyHandler must not declare SystemSurrogate or CustomSurrogateExecutable attribute.\r\n
0xb00000e2 | error %1: App manifest validation error: Line %2, Column %3, Reason: PortMin and PortMax attributes should either be both present or not. The value of PortMin attributes should be less than or equal to the value of PortMax attributes.\r\n
0xb00000e3 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support AppService multiple instances, the extension EntryPoint attribute must be declared, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support BackgroundTasks multiple instances, the extension Executable attribute, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e5 | error %1: App content group map validation error: Line %2, Column %3, Reason: %4\r\n
0xb00000e6 | error %1: App manifest validation error: Line %2, Column %3, Reason: SearchFilterHandler extension must declare Path and ProcessorArchitecture on builds later than 10.0.15001.0.\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xb000018f | The bundle reader was created successfully without manifest validation.\r\n
0xb0000190 | Checking Eappx SIP support for file\r\n
0xb0000191 | Check for Eappx SIP support completed\r\n
0xb0000192 | Returning signature or signature size from encrypted app package\r\n
0xb0000193 | Signature or signature size returned from encrypted app package\r\n
0xb0000194 | Adding signature to encrypted app package\r\n
0xb0000195 | Signature added to encrypted app package\r\n
0xb0000196 | Removing signature from encrypted app package\r\n
0xb0000197 | Signature removed from encrypted app package\r\n
0xb0000198 | Creating or sizing encrypted app indirect data\r\n
0xb0000199 | Encrypted app indirect data created or sized\r\n
0xb000019a | Verifying encrypted app indirect data\r\n
0xb000019b | Encrypted app indirect data verified\r\n
0xb000019c | Checking EappxBundle SIP support for file\r\n
0xb000019d | Check for EappxBundle SIP support completed\r\n
0xb000019e | Returning signature or signature size from encrypted app bundle\r\n
0xb000019f | Signature or signature size returned from encrypted app bundle\r\n
0xb00001a0 | Adding signature to encrypted app bundle\r\n
0xb00001a1 | Signature added to encrypted app bundle\r\n
0xb00001a2 | Removing signature from encrypted app bundle\r\n
0xb00001a3 | Signature removed from encrypted app bundle\r\n
0xb00001a4 | Creating or sizing encrypted bundle indirect data\r\n
0xb00001a5 | Encrypted bundle indirect data created or sized\r\n
0xb00001a6 | Verifying encrypted bundle indirect data\r\n
0xb00001a7 | Encrypted bundle indirect data verified\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x3037000b | Parse CGM\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x70000037 | Content Group Map\r\n
0x7000003b | AppInstaller\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute or relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The max version tested value must not be less than the min version value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "https" scheme if it's an absolute URI.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for MaxVersionTested specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct MaxVersionTested specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: Only one type of resource qualifier can be specified for a resource package.  Attribute %4 must be the same as attribute %5 on element %6.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000a5 | error %1: An encrypted app package (ID = %2) in the bundle could not be signed.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb00000b4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify the "%5" attribute.\r\n
0xb00000b5 | The reader was created successfully without manifest validation.\r\n
0xb00000b6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The StartPage attribute must be a valid URI.\r\n
0xb00000b7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Executable attribute for the windows.backgroundTask extension must be "wwahost.exe" when StartPage is specified.\r\n
0xb00000b8 | error %1: The chaining mode string for encryption algorithm cannot be empty.\r\n
0xb00000b9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The WindowsRuntimeAccess attribute must not be specified if the Type attribute value is "exclude".\r\n
0xb00000ba | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http", "https" or "ms-appx-web" scheme if it's an absolute URI.\r\n
0xb00000bb | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http" or "https" scheme if it's an absolute URI and the Type attribute value is "exclude".\r\n
0xb00000bc | error %1: App manifest validation error: Line %2, Column %3, Reason: The Url specified is a duplicate of the base Url specified for the windows.webAccountProvider extension\r\n
0xb00000bd | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP manifests.\r\n
0xb00000be | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP desktop applications whose minVersion >= 10.0.14257.0.\r\n
0xb00000bf | error %1: App manifest validation error: Line %2, Column %3, Reason: The element specified requires "%4" capability.\r\n
0xb00000c0 | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency can't be specified when the %4 element is specified.\r\n
0xb00000c1 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't target version %5 of device family "%4".  You must specify a higher MinVersion.\r\n
0xb00000c3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The use of startuptask extension requires the containing Application use the Windows.FullTrustApplication entry point.\r\n
0xb00000c4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c5 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in prototype element if in a full trust application.\r\n
0xb00000c6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in verb element if in a full trust application.\r\n
0xb00000c8 | error %1: App manifest validation error: Line %2, Column %3, Reason: AppExecutionAlias can only be used by Centennial Applications.\r\n
0xb00000c9 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" extension.\r\n
0xb00000ca | error %1: App manifest validation error: Line %2, Column %3, Reason: The Prog Id refrenced by the Class element must have for its CLSID the Class element id value.\r\n
0xb00000cb | error %1: App manifest validation error: Line %2, Column %3, Reason: The VersionIndependentProgId refrenced by the Class element must eventualy resolve in a Prog Id with CLSID matching the Class element id value.\r\n
0xb00000cc | error %1: App manifest validation error: Line %2, Column %3, Reason: Prog Id element can not have its own Id for CurrentVersion.\r\n
0xb00000cd | error %1: App manifest validation error: Line %2, Column %3, Reason: AutoConvertTo attribute of Class can not refer to its own id.\r\n
0xb00000ce | error %1: App manifest validation error: Line %2, Column %3, Reason: If InsertableObject is present then ProgId attribute must also be.\r\n
0xb00000cf | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormats element can not have both DefaultFormatName and DefaultStandardFormat attributes.\r\n
0xb00000d0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The TypeLib element must have either a Win32Path or a Win64Path child element.\r\n
0xb00000d1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormat element can not have both FormatName and StandardFormat attributes.\r\n
0xb00000d2 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Conversion element must have a Readable or ReadWritable child.\r\n
0xb00000d3 | error %1: App manifest validation error: Line %2, Column %3, Reason: If useUniversalMarshaler is true the following attributes should not also exist: ProxyStubClsid, AsynchronousInterface, SynchronousInterface\r\n
0xb00000d4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Interface child element typeLib's ID does not match a typeLib ID which also contains the child element's version number.\r\n
0xb00000d5 | error %1: App manifest validation error: Line %2, Column %3, Reason: Both AsynchronousInterface and SynchronousInterface can't exist in the same Interface element.\r\n
0xb00000d6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The AsynchronousInterface value should match the ID of an Interface with a SynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The SynchronousInterface value should match the ID of an Interface with a AsynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d8 | App manifest validation warning: Declared namespace %1 is inapplicable, it will be ignored during manifest processing.\r\n
0xb00000d9 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName attribute must be specified if ShellNewDisplayName attribute is specified.\r\n
0xb00000da | error %1: App manifest validation error: Line %2, Column %3, Reason: DdeExecCommand attribute must be specified if DdeExecApplication, DdeExecTopic or DdeExecIfExec attribute is specified.\r\n
0xb00000db | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dc | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dd | error %1: App manifest validation error: Line %2, Column %3, Reason: SystemSurrogate attribute and CustomSurrogateExecutable attribute are mutual exclusive.\r\n
0xb00000de | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency with name "%4" and publisher "%5" can't be specified multiple times.\r\n
0xb00000df | error %1: App manifest validation error: Line %2, Column %3, Reason: One and only one of AumId and ShortcutPath attribute should be declared.\r\n
0xb00000e0 | error %1: App manifest validation error: Line %2, Column %3, Reason: Either AppServiceName attribute or ActivatableClassId, Path attributes should be declared.\r\n
0xb00000e1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComServer SurrogateServer referenced by DesktopPropertyHandler must not declare SystemSurrogate or CustomSurrogateExecutable attribute.\r\n
0xb00000e2 | error %1: App manifest validation error: Line %2, Column %3, Reason: PortMin and PortMax attributes should either be both present or not. The value of PortMin attributes should be less than or equal to the value of PortMax attributes.\r\n
0xb00000e3 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support AppService multiple instances, the extension EntryPoint attribute must be declared, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support BackgroundTasks multiple instances, the extension Executable attribute, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e5 | error %1: App content group map validation error: Line %2, Column %3, Reason: %4\r\n
0xb00000e6 | error %1: App manifest validation error: Line %2, Column %3, Reason: SearchFilterHandler extension must declare Path and ProcessorArchitecture on builds later than 10.0.15001.0.\r\n
0xb00000e7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComInterface ProxyStub element must have either Path attribute or ProxyStubDll child element. Path attribute is required if the TargetDeviceFamily is targeting MinVersion 15063 or earlier.\r\n
0xb00000e8 | App manifest validation warning: Line %1, Column %2, Reason: The "%3" element is ignored during manifest processing because it's missing required child elements at xpath "%4".\r\n
0xb00000e9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" extension should be declared under %5 extensions.\r\n
0xb00000ea | error %1: App manifest validation error: Line %2, Column %3, Reason: The ExeServer Conversion Format cannot declare both FormatName and StandardFormat.\r\n
0xb00000eb | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its architecture is unknown.\r\n
0xb00000ec | error %1: App manifest validation error: Line %2, Column %3, Reason: The package extension OutOfProcessServer must declare IdentityType as activateAsPackage if RunFullTrust attribute value is true.\r\n
0xb00000ed | error %1: The XML in the .appinstaller file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000ee | error %1: The namespace "%2" of the root AppInstaller element in the .appinstaller file is not recognized.\r\n
0xb00000ef | error %1: The XML in the .appinstaller file doesn't contain a valid root AppInstaller element.\r\n
0xb00000f0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Content element cannot declare both Parameters attribute and DropTargetHandler attribute.\r\n
0xb00000f1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The binary file value "%4" must use lower case extension (exe or dll) on builds earlier than 10.0.16255.0.\r\n
0xb00000f2 | error %1: App manifest validation error: Line %2, Column %3, Reason: If it is not an audio background task, it is not allowed to have EntryPoint="%4" without ActivatableClassId in windows.activatableClass.inProcessServer.\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed. Files Written = %1, Total Size = %2\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xb000018f | The bundle reader was created successfully without manifest validation.\r\n
0xb0000190 | Checking Eappx SIP support for file\r\n
0xb0000191 | Check for Eappx SIP support completed\r\n
0xb0000192 | Returning signature or signature size from encrypted app package\r\n
0xb0000193 | Signature or signature size returned from encrypted app package\r\n
0xb0000194 | Adding signature to encrypted app package\r\n
0xb0000195 | Signature added to encrypted app package\r\n
0xb0000196 | Removing signature from encrypted app package\r\n
0xb0000197 | Signature removed from encrypted app package\r\n
0xb0000198 | Creating or sizing encrypted app indirect data\r\n
0xb0000199 | Encrypted app indirect data created or sized\r\n
0xb000019a | Verifying encrypted app indirect data\r\n
0xb000019b | Encrypted app indirect data verified\r\n
0xb000019c | Checking EappxBundle SIP support for file\r\n
0xb000019d | Check for EappxBundle SIP support completed\r\n
0xb000019e | Returning signature or signature size from encrypted app bundle\r\n
0xb000019f | Signature or signature size returned from encrypted app bundle\r\n
0xb00001a0 | Adding signature to encrypted app bundle\r\n
0xb00001a1 | Signature added to encrypted app bundle\r\n
0xb00001a2 | Removing signature from encrypted app bundle\r\n
0xb00001a3 | Signature removed from encrypted app bundle\r\n
0xb00001a4 | Creating or sizing encrypted bundle indirect data\r\n
0xb00001a5 | Encrypted bundle indirect data created or sized\r\n
0xb00001a6 | Verifying encrypted bundle indirect data\r\n
0xb00001a7 | Encrypted bundle indirect data verified\r\n
0xb00001a8 | Adding payload files, file count = %1\r\n
0xb00001a9 | Payload files added\r\n
0xb00001aa | Processing payload file, file name = %1, content type = %2, compression = %3\r\n
0xb00001ab | Payload file processed\r\n
0xb00001ac | Adding reference package\r\n
0xb00001ad | Reference package added\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x3037000b | Parse CGM\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x70000037 | Content Group Map\r\n
0x7000003b | AppInstaller\r\n
0x7000003c | PackagingLayout\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute or relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The max version tested value must not be less than the min version value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "https" scheme if it's an absolute URI.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for MaxVersionTested specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct MaxVersionTested specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: Only one type of resource qualifier can be specified for a resource package.  Attribute %4 must be the same as attribute %5 on element %6.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000a5 | error %1: An encrypted app package (ID = %2) in the bundle could not be signed.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb00000b4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify the "%5" attribute.\r\n
0xb00000b5 | The reader was created successfully without manifest validation.\r\n
0xb00000b6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The StartPage attribute must be a valid URI.\r\n
0xb00000b7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Executable attribute for the windows.backgroundTask extension must be "wwahost.exe" when StartPage is specified.\r\n
0xb00000b8 | error %1: The chaining mode string for encryption algorithm cannot be empty.\r\n
0xb00000b9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The WindowsRuntimeAccess attribute must not be specified if the Type attribute value is "exclude".\r\n
0xb00000ba | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http", "https" or "ms-appx-web" scheme if it's an absolute URI.\r\n
0xb00000bb | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http" or "https" scheme if it's an absolute URI and the Type attribute value is "exclude".\r\n
0xb00000bc | error %1: App manifest validation error: Line %2, Column %3, Reason: The Url specified is a duplicate of the base Url specified for the windows.webAccountProvider extension\r\n
0xb00000bd | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP manifests.\r\n
0xb00000be | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP desktop applications whose minVersion >= 10.0.14257.0.\r\n
0xb00000bf | error %1: App manifest validation error: Line %2, Column %3, Reason: The element specified requires "%4" capability.\r\n
0xb00000c0 | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency can't be specified when the %4 element is specified.\r\n
0xb00000c1 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't target version %5 of device family "%4".  You must specify a higher MinVersion.\r\n
0xb00000c3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The use of startuptask extension requires the containing Application use the Windows.FullTrustApplication entry point.\r\n
0xb00000c4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c5 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in prototype element if in a full trust application.\r\n
0xb00000c6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in verb element if in a full trust application.\r\n
0xb00000c8 | error %1: App manifest validation error: Line %2, Column %3, Reason: AppExecutionAlias can only be used by Centennial Applications.\r\n
0xb00000c9 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" extension.\r\n
0xb00000ca | error %1: App manifest validation error: Line %2, Column %3, Reason: The Prog Id refrenced by the Class element must have for its CLSID the Class element id value.\r\n
0xb00000cb | error %1: App manifest validation error: Line %2, Column %3, Reason: The VersionIndependentProgId refrenced by the Class element must eventualy resolve in a Prog Id with CLSID matching the Class element id value.\r\n
0xb00000cc | error %1: App manifest validation error: Line %2, Column %3, Reason: Prog Id element can not have its own Id for CurrentVersion.\r\n
0xb00000cd | error %1: App manifest validation error: Line %2, Column %3, Reason: AutoConvertTo attribute of Class can not refer to its own id.\r\n
0xb00000ce | error %1: App manifest validation error: Line %2, Column %3, Reason: If InsertableObject is present then ProgId attribute must also be.\r\n
0xb00000cf | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormats element can not have both DefaultFormatName and DefaultStandardFormat attributes.\r\n
0xb00000d0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The TypeLib element must have either a Win32Path or a Win64Path child element.\r\n
0xb00000d1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormat element can not have both FormatName and StandardFormat attributes.\r\n
0xb00000d2 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Conversion element must have a Readable or ReadWritable child.\r\n
0xb00000d3 | error %1: App manifest validation error: Line %2, Column %3, Reason: If useUniversalMarshaler is true the following attributes should not also exist: ProxyStubClsid, AsynchronousInterface, SynchronousInterface\r\n
0xb00000d4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Interface child element typeLib's ID does not match a typeLib ID which also contains the child element's version number.\r\n
0xb00000d5 | error %1: App manifest validation error: Line %2, Column %3, Reason: Both AsynchronousInterface and SynchronousInterface can't exist in the same Interface element.\r\n
0xb00000d6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The AsynchronousInterface value should match the ID of an Interface with a SynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The SynchronousInterface value should match the ID of an Interface with a AsynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d8 | App manifest validation warning: Declared namespace %1 is inapplicable, it will be ignored during manifest processing.\r\n
0xb00000d9 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName attribute must be specified if ShellNewDisplayName attribute is specified.\r\n
0xb00000da | error %1: App manifest validation error: Line %2, Column %3, Reason: DdeExecCommand attribute must be specified if DdeExecApplication, DdeExecTopic or DdeExecIfExec attribute is specified.\r\n
0xb00000db | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dc | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dd | error %1: App manifest validation error: Line %2, Column %3, Reason: SystemSurrogate attribute and CustomSurrogateExecutable attribute are mutual exclusive.\r\n
0xb00000de | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency with name "%4" and publisher "%5" can't be specified multiple times.\r\n
0xb00000df | error %1: App manifest validation error: Line %2, Column %3, Reason: One and only one of AumId and ShortcutPath attribute should be declared.\r\n
0xb00000e0 | error %1: App manifest validation error: Line %2, Column %3, Reason: Either AppServiceName attribute or ActivatableClassId, Path attributes should be declared.\r\n
0xb00000e1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComServer SurrogateServer referenced by DesktopPropertyHandler must not declare SystemSurrogate or CustomSurrogateExecutable attribute.\r\n
0xb00000e2 | error %1: App manifest validation error: Line %2, Column %3, Reason: PortMin and PortMax attributes should either be both present or not. The value of PortMin attributes should be less than or equal to the value of PortMax attributes.\r\n
0xb00000e3 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support AppService multiple instances, the extension EntryPoint attribute must be declared, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support BackgroundTasks multiple instances, the extension Executable attribute, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e5 | error %1: App content group map validation error: Line %2, Column %3, Reason: %4\r\n
0xb00000e6 | error %1: App manifest validation error: Line %2, Column %3, Reason: SearchFilterHandler extension must declare Path and ProcessorArchitecture on builds later than 10.0.15001.0.\r\n
0xb00000e7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComInterface ProxyStub element must have either Path attribute or ProxyStubDll child element. Path attribute is required if the TargetDeviceFamily is targeting MinVersion 15063 or earlier.\r\n
0xb00000e8 | App manifest validation warning: Line %1, Column %2, Reason: The "%3" element is ignored during manifest processing because it's missing required child elements at xpath "%4".\r\n
0xb00000e9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" extension should be declared under %5 extensions.\r\n
0xb00000ea | error %1: App manifest validation error: Line %2, Column %3, Reason: The ExeServer Conversion Format cannot declare both FormatName and StandardFormat.\r\n
0xb00000eb | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its architecture is unknown.\r\n
0xb00000ec | error %1: App manifest validation error: Line %2, Column %3, Reason: The package extension OutOfProcessServer must declare IdentityType as activateAsPackage if RunFullTrust attribute value is true.\r\n
0xb00000ed | error %1: The XML in the .appinstaller file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000ee | error %1: The namespace "%2" of the root AppInstaller element in the .appinstaller file is not recognized.\r\n
0xb00000ef | error %1: The XML in the .appinstaller file doesn't contain a valid root AppInstaller element.\r\n
0xb00000f0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Content element cannot declare both Parameters attribute and DropTargetHandler attribute.\r\n
0xb00000f1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The binary file value "%4" must use lower case extension (exe or dll) on builds earlier than 10.0.16255.0.\r\n
0xb00000f2 | error %1: App manifest validation error: Line %2, Column %3, Reason: If it is not an audio background task, it is not allowed to have EntryPoint="%4" without ActivatableClassId in windows.activatableClass.inProcessServer.\r\n
0xb00000f3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The %4 element cannot declare the attribute Subsystem with value console without declaring  the attribute SupportsMultipleInstances with value true in element %5.\r\n
0xb00000f4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support Application multiple instances, the ResourceGroup attribute must not be declared.\r\n
0xb00000f5 | error %1: App manifest validation error: Line %2, Column %3, Reason: A <Resource> element is required for packages targeting OS version 10.0.16299.0 or earlier.\r\n
0xb00000f6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The <AllowExecution> property cannot be set to false for packages targeting OS version 10.0.16299.0 or earlier.\r\n
0xb00000f7 | error %1: The XML in the packaging layout file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000f8 | error %1: The namespace "%2" of the root <PackagingLayout> element in the packaging layout file is not recognized.\r\n
0xb00000f9 | error %1: The XML in the packaging layout file doesn't contain a valid root <PackagingLayout> element.\r\n
0xb00000fa | error %1: App manifest validation error: Line %2, Column %3, Reason: The extension windows.barcodeScannerPreviewProvider must be declared with the extension windows.barcodeScannerProvider with the attribute supportsVideoPreview with value "true" in element BarcodeScannerProvider.\r\n
0xb00000fb | error %1: App manifest validation error: Line %2, Column %3, Reason: The element ClassicAppCompatKey must have "Name" or "Name and Value"  or "Name, ValueName, Value and ValueType", any other combination is not valid.\r\n
0xb00000fc | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute Name in element ClassicAppCompatKey cannot be defined under "\\Software\\Microsoft", except under "\\Software\\Microsoft\Office".\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed. Files Written = %1, Total Size = %2\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xb000018f | The bundle reader was created successfully without manifest validation.\r\n
0xb0000190 | Checking Eappx SIP support for file\r\n
0xb0000191 | Check for Eappx SIP support completed\r\n
0xb0000192 | Returning signature or signature size from encrypted app package\r\n
0xb0000193 | Signature or signature size returned from encrypted app package\r\n
0xb0000194 | Adding signature to encrypted app package\r\n
0xb0000195 | Signature added to encrypted app package\r\n
0xb0000196 | Removing signature from encrypted app package\r\n
0xb0000197 | Signature removed from encrypted app package\r\n
0xb0000198 | Creating or sizing encrypted app indirect data\r\n
0xb0000199 | Encrypted app indirect data created or sized\r\n
0xb000019a | Verifying encrypted app indirect data\r\n
0xb000019b | Encrypted app indirect data verified\r\n
0xb000019c | Checking EappxBundle SIP support for file\r\n
0xb000019d | Check for EappxBundle SIP support completed\r\n
0xb000019e | Returning signature or signature size from encrypted app bundle\r\n
0xb000019f | Signature or signature size returned from encrypted app bundle\r\n
0xb00001a0 | Adding signature to encrypted app bundle\r\n
0xb00001a1 | Signature added to encrypted app bundle\r\n
0xb00001a2 | Removing signature from encrypted app bundle\r\n
0xb00001a3 | Signature removed from encrypted app bundle\r\n
0xb00001a4 | Creating or sizing encrypted bundle indirect data\r\n
0xb00001a5 | Encrypted bundle indirect data created or sized\r\n
0xb00001a6 | Verifying encrypted bundle indirect data\r\n
0xb00001a7 | Encrypted bundle indirect data verified\r\n
0xb00001a8 | Adding payload files, file count = %1\r\n
0xb00001a9 | Payload files added\r\n
0xb00001aa | Processing payload file, file name = %1, content type = %2, compression = %3\r\n
0xb00001ab | Payload file processed\r\n
0xb00001ac | Adding reference package\r\n
0xb00001ad | Reference package added\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 10.0.17763.1

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x3037000b | Parse CGM\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x70000037 | Content Group Map\r\n
0x7000003b | AppInstaller\r\n
0x7000003c | PackagingLayout\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute or relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The max version tested value must not be less than the min version value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "https" scheme if it's an absolute URI.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for MaxVersionTested specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct MaxVersionTested specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: Only one type of resource qualifier can be specified for a resource package.  Attribute %4 must be the same as attribute %5 on element %6.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000a5 | error %1: An encrypted app package (ID = %2) in the bundle could not be signed.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb00000b4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify the "%5" attribute.\r\n
0xb00000b5 | The reader was created successfully without manifest validation.\r\n
0xb00000b6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The StartPage attribute must be a valid URI.\r\n
0xb00000b7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Executable attribute for the windows.backgroundTask extension must be "wwahost.exe" when StartPage is specified.\r\n
0xb00000b8 | error %1: The chaining mode string for encryption algorithm cannot be empty.\r\n
0xb00000b9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The WindowsRuntimeAccess attribute must not be specified if the Type attribute value is "exclude".\r\n
0xb00000ba | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http", "https" or "ms-appx-web" scheme if it's an absolute URI.\r\n
0xb00000bb | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http" or "https" scheme if it's an absolute URI and the Type attribute value is "exclude".\r\n
0xb00000bc | error %1: App manifest validation error: Line %2, Column %3, Reason: The Url specified is a duplicate of the base Url specified for the windows.webAccountProvider extension\r\n
0xb00000bd | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP manifests.\r\n
0xb00000be | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP desktop applications whose minVersion >= 10.0.14257.0.\r\n
0xb00000bf | error %1: App manifest validation error: Line %2, Column %3, Reason: The element specified requires "%4" capability.\r\n
0xb00000c0 | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency can't be specified when the %4 element is specified.\r\n
0xb00000c1 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't target version %5 of device family "%4".  You must specify a higher MinVersion.\r\n
0xb00000c3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The use of startuptask extension requires the containing Application use the Windows.FullTrustApplication entry point.\r\n
0xb00000c4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c5 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in prototype element if in a full trust application.\r\n
0xb00000c6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in verb element if in a full trust application.\r\n
0xb00000c8 | error %1: App manifest validation error: Line %2, Column %3, Reason: AppExecutionAlias can only be used by Centennial Applications.\r\n
0xb00000c9 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" extension.\r\n
0xb00000ca | error %1: App manifest validation error: Line %2, Column %3, Reason: The Prog Id refrenced by the Class element must have for its CLSID the Class element id value.\r\n
0xb00000cb | error %1: App manifest validation error: Line %2, Column %3, Reason: The VersionIndependentProgId refrenced by the Class element must eventualy resolve in a Prog Id with CLSID matching the Class element id value.\r\n
0xb00000cc | error %1: App manifest validation error: Line %2, Column %3, Reason: Prog Id element can not have its own Id for CurrentVersion.\r\n
0xb00000cd | error %1: App manifest validation error: Line %2, Column %3, Reason: AutoConvertTo attribute of Class can not refer to its own id.\r\n
0xb00000ce | error %1: App manifest validation error: Line %2, Column %3, Reason: If InsertableObject is present then ProgId attribute must also be.\r\n
0xb00000cf | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormats element can not have both DefaultFormatName and DefaultStandardFormat attributes.\r\n
0xb00000d0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The TypeLib element must have either a Win32Path or a Win64Path child element.\r\n
0xb00000d1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormat element can not have both FormatName and StandardFormat attributes.\r\n
0xb00000d2 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Conversion element must have a Readable or ReadWritable child.\r\n
0xb00000d3 | error %1: App manifest validation error: Line %2, Column %3, Reason: If useUniversalMarshaler is true the following attributes should not also exist: ProxyStubClsid, AsynchronousInterface, SynchronousInterface\r\n
0xb00000d4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Interface child element typeLib's ID does not match a typeLib ID which also contains the child element's version number.\r\n
0xb00000d5 | error %1: App manifest validation error: Line %2, Column %3, Reason: Both AsynchronousInterface and SynchronousInterface can't exist in the same Interface element.\r\n
0xb00000d6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The AsynchronousInterface value should match the ID of an Interface with a SynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The SynchronousInterface value should match the ID of an Interface with a AsynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d8 | App manifest validation warning: Declared namespace %1 is inapplicable, it will be ignored during manifest processing.\r\n
0xb00000d9 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName attribute must be specified if ShellNewDisplayName attribute is specified.\r\n
0xb00000da | error %1: App manifest validation error: Line %2, Column %3, Reason: DdeExecCommand attribute must be specified if DdeExecApplication, DdeExecTopic or DdeExecIfExec attribute is specified.\r\n
0xb00000db | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dc | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dd | error %1: App manifest validation error: Line %2, Column %3, Reason: SystemSurrogate attribute and CustomSurrogateExecutable attribute are mutual exclusive.\r\n
0xb00000de | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency with name "%4" and publisher "%5" can't be specified multiple times.\r\n
0xb00000df | error %1: App manifest validation error: Line %2, Column %3, Reason: One and only one of AumId and ShortcutPath attribute should be declared.\r\n
0xb00000e0 | error %1: App manifest validation error: Line %2, Column %3, Reason: Either AppServiceName attribute or ActivatableClassId, Path attributes should be declared.\r\n
0xb00000e1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComServer SurrogateServer referenced by DesktopPropertyHandler must not declare SystemSurrogate or CustomSurrogateExecutable attribute.\r\n
0xb00000e2 | error %1: App manifest validation error: Line %2, Column %3, Reason: PortMin and PortMax attributes should either be both present or not. The value of PortMin attributes should be less than or equal to the value of PortMax attributes.\r\n
0xb00000e3 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support AppService multiple instances, the extension EntryPoint attribute must be declared, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support BackgroundTasks multiple instances, the extension Executable attribute, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e5 | error %1: App content group map validation error: Line %2, Column %3, Reason: %4\r\n
0xb00000e6 | error %1: App manifest validation error: Line %2, Column %3, Reason: SearchFilterHandler extension must declare Path and ProcessorArchitecture on builds later than 10.0.15001.0.\r\n
0xb00000e7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComInterface ProxyStub element must have either Path attribute or ProxyStubDll child element. Path attribute is required if the TargetDeviceFamily is targeting MinVersion 15063 or earlier.\r\n
0xb00000e8 | App manifest validation warning: Line %1, Column %2, Reason: The "%3" element is ignored during manifest processing because it's missing required child elements at xpath "%4".\r\n
0xb00000e9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" extension should be declared under %5 extensions.\r\n
0xb00000ea | error %1: App manifest validation error: Line %2, Column %3, Reason: The ExeServer Conversion Format cannot declare both FormatName and StandardFormat.\r\n
0xb00000eb | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its architecture is unknown.\r\n
0xb00000ec | error %1: App manifest validation error: Line %2, Column %3, Reason: The package extension OutOfProcessServer must declare IdentityType as activateAsPackage if RunFullTrust attribute value is true.\r\n
0xb00000ed | error %1: The XML in the .appinstaller file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000ee | error %1: The namespace "%2" of the root AppInstaller element in the .appinstaller file is not recognized.\r\n
0xb00000ef | error %1: The XML in the .appinstaller file doesn't contain a valid root AppInstaller element.\r\n
0xb00000f0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Content element cannot declare both Parameters attribute and DropTargetHandler attribute.\r\n
0xb00000f1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The binary file value "%4" must use lower case extension (exe or dll) on builds earlier than 10.0.16255.0.\r\n
0xb00000f2 | error %1: App manifest validation error: Line %2, Column %3, Reason: If it is not an audio background task, it is not allowed to have EntryPoint="%4" without ActivatableClassId in windows.activatableClass.inProcessServer.\r\n
0xb00000f3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The %4 element cannot declare the attribute Subsystem with value console without declaring  the attribute SupportsMultipleInstances with value true in element %5.\r\n
0xb00000f4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support Application multiple instances, the ResourceGroup attribute must not be declared.\r\n
0xb00000f5 | error %1: App manifest validation error: Line %2, Column %3, Reason: A <Resource> element is required for packages targeting OS version 10.0.16299.0 or earlier.\r\n
0xb00000f6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The <AllowExecution> property cannot be set to false for packages targeting OS version 10.0.16299.0 or earlier.\r\n
0xb00000f7 | error %1: The XML in the packaging layout file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000f8 | error %1: The namespace "%2" of the root <PackagingLayout> element in the packaging layout file is not recognized.\r\n
0xb00000f9 | error %1: The XML in the packaging layout file doesn't contain a valid root <PackagingLayout> element.\r\n
0xb00000fa | error %1: App manifest validation error: Line %2, Column %3, Reason: The extension windows.barcodeScannerPreviewProvider must be declared with the extension windows.barcodeScannerProvider with the attribute supportsVideoPreview with value "true" in element BarcodeScannerProvider.\r\n
0xb00000fb | error %1: App manifest validation error: Line %2, Column %3, Reason: The element ClassicAppCompatKey must have "Name" or "Name and Value"  or "Name, ValueName, Value and ValueType", any other combination is not valid.\r\n
0xb00000fc | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute Name in element ClassicAppCompatKey cannot be defined under "\\Software\\Microsoft", except under "\\Software\\Microsoft\Office".\r\n
0xb00000fd | error %1: App manifest validation error: Line %2, Column %3, Reason: The combination of atributes "AssemblyName, AssemblyVersion, PublicKey and MachineType" in element PrimaryInteropAssemblies must be unique.\r\n
0xb00000fe | error %1: App manifest validation error: Line %2, Column %3, Reason: Extension "windows.service" must declared with "Executable" and "EntryPoint".\r\n
0xb00000ff | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Partial Trust or Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb0000100 | error %1: App manifest validation error: Line %2, Column %3, Reason: "Default" attribute should be specified as true for only one "Verb" in a set of "SupportedVerbs".\r\n
0xb0000101 | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared with Partial Trust EntryPoint.\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed. Files Written = %1, Total Size = %2\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xb000018f | The bundle reader was created successfully without manifest validation.\r\n
0xb0000190 | Checking Eappx SIP support for file\r\n
0xb0000191 | Check for Eappx SIP support completed\r\n
0xb0000192 | Returning signature or signature size from encrypted app package\r\n
0xb0000193 | Signature or signature size returned from encrypted app package\r\n
0xb0000194 | Adding signature to encrypted app package\r\n
0xb0000195 | Signature added to encrypted app package\r\n
0xb0000196 | Removing signature from encrypted app package\r\n
0xb0000197 | Signature removed from encrypted app package\r\n
0xb0000198 | Creating or sizing encrypted app indirect data\r\n
0xb0000199 | Encrypted app indirect data created or sized\r\n
0xb000019a | Verifying encrypted app indirect data\r\n
0xb000019b | Encrypted app indirect data verified\r\n
0xb000019c | Checking EappxBundle SIP support for file\r\n
0xb000019d | Check for EappxBundle SIP support completed\r\n
0xb000019e | Returning signature or signature size from encrypted app bundle\r\n
0xb000019f | Signature or signature size returned from encrypted app bundle\r\n
0xb00001a0 | Adding signature to encrypted app bundle\r\n
0xb00001a1 | Signature added to encrypted app bundle\r\n
0xb00001a2 | Removing signature from encrypted app bundle\r\n
0xb00001a3 | Signature removed from encrypted app bundle\r\n
0xb00001a4 | Creating or sizing encrypted bundle indirect data\r\n
0xb00001a5 | Encrypted bundle indirect data created or sized\r\n
0xb00001a6 | Verifying encrypted bundle indirect data\r\n
0xb00001a7 | Encrypted bundle indirect data verified\r\n
0xb00001a8 | Adding payload files, file count = %1\r\n
0xb00001a9 | Payload files added\r\n
0xb00001aa | Processing payload file, file name = %1, content type = %2, compression = %3\r\n
0xb00001ab | Payload file processed\r\n
0xb00001ac | Adding reference package\r\n
0xb00001ad | Reference package added\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 10.0.18362.1

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x3037000b | Parse CGM\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x70000037 | Content Group Map\r\n
0x7000003b | AppInstaller\r\n
0x7000003c | PackagingLayout\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute or relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The max version tested value must not be less than the min version value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "https" scheme if it's an absolute URI.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for MaxVersionTested specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct MaxVersionTested specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: Only one type of resource qualifier can be specified for a resource package.  Attribute %4 must be the same as attribute %5 on element %6.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000a5 | error %1: An encrypted app package (ID = %2) in the bundle could not be signed.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb00000b4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify the "%5" attribute.\r\n
0xb00000b5 | The reader was created successfully without manifest validation.\r\n
0xb00000b6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The StartPage attribute must be a valid URI.\r\n
0xb00000b7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Executable attribute for the windows.backgroundTask extension must be "wwahost.exe" when StartPage is specified.\r\n
0xb00000b8 | error %1: The chaining mode string for encryption algorithm cannot be empty.\r\n
0xb00000b9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The WindowsRuntimeAccess attribute must not be specified if the Type attribute value is "exclude".\r\n
0xb00000ba | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http", "https" or "ms-appx-web" scheme if it's an absolute URI.\r\n
0xb00000bb | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http" or "https" scheme if it's an absolute URI and the Type attribute value is "exclude".\r\n
0xb00000bc | error %1: App manifest validation error: Line %2, Column %3, Reason: The Url specified is a duplicate of the base Url specified for the windows.webAccountProvider extension\r\n
0xb00000bd | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP manifests.\r\n
0xb00000be | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP desktop applications whose minVersion >= 10.0.14257.0.\r\n
0xb00000bf | error %1: App manifest validation error: Line %2, Column %3, Reason: The element specified requires "%4" capability.\r\n
0xb00000c0 | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency can't be specified when the %4 element is specified.\r\n
0xb00000c1 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't target version %5 of device family "%4".  You must specify a higher MinVersion.\r\n
0xb00000c3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The use of startuptask extension requires the containing Application use the Windows.FullTrustApplication entry point.\r\n
0xb00000c4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c5 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in prototype element if in a full trust application.\r\n
0xb00000c6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in verb element if in a full trust application.\r\n
0xb00000c8 | error %1: App manifest validation error: Line %2, Column %3, Reason: AppExecutionAlias can only be used by Centennial Applications.\r\n
0xb00000c9 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" extension.\r\n
0xb00000ca | error %1: App manifest validation error: Line %2, Column %3, Reason: The Prog Id refrenced by the Class element must have for its CLSID the Class element id value.\r\n
0xb00000cb | error %1: App manifest validation error: Line %2, Column %3, Reason: The VersionIndependentProgId refrenced by the Class element must eventualy resolve in a Prog Id with CLSID matching the Class element id value.\r\n
0xb00000cc | error %1: App manifest validation error: Line %2, Column %3, Reason: Prog Id element can not have its own Id for CurrentVersion.\r\n
0xb00000cd | error %1: App manifest validation error: Line %2, Column %3, Reason: AutoConvertTo attribute of Class can not refer to its own id.\r\n
0xb00000ce | error %1: App manifest validation error: Line %2, Column %3, Reason: If InsertableObject is present then ProgId attribute must also be.\r\n
0xb00000cf | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormats element can not have both DefaultFormatName and DefaultStandardFormat attributes.\r\n
0xb00000d0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The TypeLib element must have either a Win32Path or a Win64Path child element.\r\n
0xb00000d1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormat element can not have both FormatName and StandardFormat attributes.\r\n
0xb00000d2 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Conversion element must have a Readable or ReadWritable child.\r\n
0xb00000d3 | error %1: App manifest validation error: Line %2, Column %3, Reason: If useUniversalMarshaler is true the following attributes should not also exist: ProxyStubClsid, AsynchronousInterface, SynchronousInterface\r\n
0xb00000d4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Interface child element typeLib's ID does not match a typeLib ID which also contains the child element's version number.\r\n
0xb00000d5 | error %1: App manifest validation error: Line %2, Column %3, Reason: Both AsynchronousInterface and SynchronousInterface can't exist in the same Interface element.\r\n
0xb00000d6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The AsynchronousInterface value should match the ID of an Interface with a SynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The SynchronousInterface value should match the ID of an Interface with a AsynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d8 | App manifest validation warning: Declared namespace %1 is inapplicable, it will be ignored during manifest processing.\r\n
0xb00000d9 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName attribute must be specified if ShellNewDisplayName attribute is specified.\r\n
0xb00000da | error %1: App manifest validation error: Line %2, Column %3, Reason: DdeExecCommand attribute must be specified if DdeExecApplication, DdeExecTopic or DdeExecIfExec attribute is specified.\r\n
0xb00000db | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dc | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dd | error %1: App manifest validation error: Line %2, Column %3, Reason: SystemSurrogate attribute and CustomSurrogateExecutable attribute are mutual exclusive.\r\n
0xb00000de | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency with name "%4" and publisher "%5" can't be specified multiple times.\r\n
0xb00000df | error %1: App manifest validation error: Line %2, Column %3, Reason: One and only one of AumId and ShortcutPath attribute should be declared.\r\n
0xb00000e0 | error %1: App manifest validation error: Line %2, Column %3, Reason: Either AppServiceName attribute or ActivatableClassId, Path attributes should be declared.\r\n
0xb00000e1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComServer SurrogateServer referenced by DesktopPropertyHandler must not declare SystemSurrogate or CustomSurrogateExecutable attribute.\r\n
0xb00000e2 | error %1: App manifest validation error: Line %2, Column %3, Reason: PortMin and PortMax attributes should either be both present or not. The value of PortMin attributes should be less than or equal to the value of PortMax attributes.\r\n
0xb00000e3 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support AppService multiple instances, the extension EntryPoint attribute must be declared, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support BackgroundTasks multiple instances, the extension Executable attribute, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e5 | error %1: App content group map validation error: Line %2, Column %3, Reason: %4\r\n
0xb00000e6 | error %1: App manifest validation error: Line %2, Column %3, Reason: SearchFilterHandler extension must declare Path and ProcessorArchitecture on builds later than 10.0.15001.0.\r\n
0xb00000e7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComInterface ProxyStub element must have either Path attribute or ProxyStubDll child element. Path attribute is required if the TargetDeviceFamily is targeting MinVersion 15063 or earlier.\r\n
0xb00000e8 | App manifest validation warning: Line %1, Column %2, Reason: The "%3" element is ignored during manifest processing because it's missing required child elements at xpath "%4".\r\n
0xb00000e9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" extension should be declared under %5 extensions.\r\n
0xb00000ea | error %1: App manifest validation error: Line %2, Column %3, Reason: The ExeServer Conversion Format cannot declare both FormatName and StandardFormat.\r\n
0xb00000eb | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its architecture is unknown.\r\n
0xb00000ec | error %1: App manifest validation error: Line %2, Column %3, Reason: The package extension OutOfProcessServer must declare IdentityType as activateAsPackage if RunFullTrust attribute value is true.\r\n
0xb00000ed | error %1: The XML in the .appinstaller file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000ee | error %1: The namespace "%2" of the root AppInstaller element in the .appinstaller file is not recognized.\r\n
0xb00000ef | error %1: The XML in the .appinstaller file doesn't contain a valid root AppInstaller element.\r\n
0xb00000f0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Content element cannot declare both Parameters attribute and DropTargetHandler attribute.\r\n
0xb00000f1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The binary file value "%4" must use lower case extension (exe or dll) on builds earlier than 10.0.16255.0.\r\n
0xb00000f2 | error %1: App manifest validation error: Line %2, Column %3, Reason: If it is not an audio background task, it is not allowed to have EntryPoint="%4" without ActivatableClassId in windows.activatableClass.inProcessServer.\r\n
0xb00000f3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The %4 element cannot declare the attribute Subsystem with value console without declaring  the attribute SupportsMultipleInstances with value true in element %5.\r\n
0xb00000f4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support Application multiple instances, the ResourceGroup attribute must not be declared.\r\n
0xb00000f5 | error %1: App manifest validation error: Line %2, Column %3, Reason: A <Resource> element is required for packages targeting OS version 10.0.16299.0 or earlier.\r\n
0xb00000f6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The <AllowExecution> property cannot be set to false for packages targeting OS version 10.0.16299.0 or earlier.\r\n
0xb00000f7 | error %1: The XML in the packaging layout file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000f8 | error %1: The namespace "%2" of the root <PackagingLayout> element in the packaging layout file is not recognized.\r\n
0xb00000f9 | error %1: The XML in the packaging layout file doesn't contain a valid root <PackagingLayout> element.\r\n
0xb00000fa | error %1: App manifest validation error: Line %2, Column %3, Reason: The extension windows.barcodeScannerPreviewProvider must be declared with the extension windows.barcodeScannerProvider with the attribute supportsVideoPreview with value "true" in element BarcodeScannerProvider.\r\n
0xb00000fb | error %1: App manifest validation error: Line %2, Column %3, Reason: The element ClassicAppCompatKey must have "Name" or "Name and Value"  or "Name, ValueName, Value and ValueType", any other combination is not valid.\r\n
0xb00000fc | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute Name in element ClassicAppCompatKey cannot be defined under "\\Software\\Microsoft", except under "\\Software\\Microsoft\Office".\r\n
0xb00000fd | error %1: App manifest validation error: Line %2, Column %3, Reason: The combination of atributes "AssemblyName, AssemblyVersion, PublicKey and MachineType" in element PrimaryInteropAssemblies must be unique.\r\n
0xb00000fe | error %1: App manifest validation error: Line %2, Column %3, Reason: Extension "windows.service" must declared with "Executable" and "EntryPoint".\r\n
0xb00000ff | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Partial Trust or Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb0000100 | error %1: App manifest validation error: Line %2, Column %3, Reason: "Default" attribute should be specified as true for only one "Verb" in a set of "SupportedVerbs".\r\n
0xb0000101 | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared with Partial Trust EntryPoint.\r\n
0xb0000102 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ProgId value "%4" must have a length equal to or less than 39 on builds earlier than 10.0.18256.0.\r\n
0xb0000103 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" property.\r\n
0xb0000104 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which targets the same device family.  Bundles can't contain multiple neutral app packages with the same target device family value.\r\n
0xb0000105 | error %1: The bundle contains at least two conflicting app packages. Bundles that contain packages targeting 10.0.17763.0 or lower can't contain more than one neutral application package.\r\n
0xb0000106 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package without MainPackageDependency can't use the "ModificationPackage" property.\r\n
0xb0000107 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute "%4" is required if the TargetDeviceFamily is targeting MinVersion "%5" or earlier.\r\n
0xb0000108 | error %1: App manifest validation error: Line %2, Column %3, Reason: "Default" and "Extended" attributes can't be "True" at the same time.\r\n
0xb0000109 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute "%4" value "%5" must have a length equal to or less than "%6" on builds earlier than "%7".\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed. Files Written = %1, Total Size = %2\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xb000018f | The bundle reader was created successfully without manifest validation.\r\n
0xb0000190 | Checking Eappx SIP support for file\r\n
0xb0000191 | Check for Eappx SIP support completed\r\n
0xb0000192 | Returning signature or signature size from encrypted app package\r\n
0xb0000193 | Signature or signature size returned from encrypted app package\r\n
0xb0000194 | Adding signature to encrypted app package\r\n
0xb0000195 | Signature added to encrypted app package\r\n
0xb0000196 | Removing signature from encrypted app package\r\n
0xb0000197 | Signature removed from encrypted app package\r\n
0xb0000198 | Creating or sizing encrypted app indirect data\r\n
0xb0000199 | Encrypted app indirect data created or sized\r\n
0xb000019a | Verifying encrypted app indirect data\r\n
0xb000019b | Encrypted app indirect data verified\r\n
0xb000019c | Checking EappxBundle SIP support for file\r\n
0xb000019d | Check for EappxBundle SIP support completed\r\n
0xb000019e | Returning signature or signature size from encrypted app bundle\r\n
0xb000019f | Signature or signature size returned from encrypted app bundle\r\n
0xb00001a0 | Adding signature to encrypted app bundle\r\n
0xb00001a1 | Signature added to encrypted app bundle\r\n
0xb00001a2 | Removing signature from encrypted app bundle\r\n
0xb00001a3 | Signature removed from encrypted app bundle\r\n
0xb00001a4 | Creating or sizing encrypted bundle indirect data\r\n
0xb00001a5 | Encrypted bundle indirect data created or sized\r\n
0xb00001a6 | Verifying encrypted bundle indirect data\r\n
0xb00001a7 | Encrypted bundle indirect data verified\r\n
0xb00001a8 | Adding payload files, file count = %1\r\n
0xb00001a9 | Payload files added\r\n
0xb00001aa | Processing payload file, file name = %1, content type = %2, compression = %3\r\n
0xb00001ab | Payload file processed\r\n
0xb00001ac | Adding reference package\r\n
0xb00001ad | Reference package added\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 10.0.19041.1

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x3037000b | Parse CGM\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x70000037 | Content Group Map\r\n
0x7000003b | AppInstaller\r\n
0x7000003c | PackagingLayout\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute or relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The max version tested value must not be less than the min version value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "https" scheme if it's an absolute URI.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for MaxVersionTested specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct MaxVersionTested specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: Only one type of resource qualifier can be specified for a resource package.  Attribute %4 must be the same as attribute %5 on element %6.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000a5 | error %1: An encrypted app package (ID = %2) in the bundle could not be signed.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package targeting a known processor architecture.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb00000b4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify the "%5" attribute.\r\n
0xb00000b5 | The reader was created successfully without manifest validation.\r\n
0xb00000b6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The StartPage attribute must be a valid URI.\r\n
0xb00000b7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Executable attribute for the windows.backgroundTask extension must be "wwahost.exe" when StartPage is specified.\r\n
0xb00000b8 | error %1: The chaining mode string for encryption algorithm cannot be empty.\r\n
0xb00000b9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The WindowsRuntimeAccess attribute must not be specified if the Type attribute value is "exclude".\r\n
0xb00000ba | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http", "https" or "ms-appx-web" scheme if it's an absolute URI.\r\n
0xb00000bb | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http" or "https" scheme if it's an absolute URI and the Type attribute value is "exclude".\r\n
0xb00000bc | error %1: App manifest validation error: Line %2, Column %3, Reason: The Url specified is a duplicate of the base Url specified for the windows.webAccountProvider extension\r\n
0xb00000bd | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP manifests.\r\n
0xb00000be | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP desktop applications whose minVersion >= 10.0.14257.0.\r\n
0xb00000bf | error %1: App manifest validation error: Line %2, Column %3, Reason: The element specified requires "%4" capability.\r\n
0xb00000c0 | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency can't be specified when the %4 element is specified.\r\n
0xb00000c1 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't target version %5 of device family "%4".  You must specify a higher MinVersion.\r\n
0xb00000c3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The use of startuptask extension requires the containing Application use the Windows.FullTrustApplication entry point.\r\n
0xb00000c4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c5 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in prototype element if in a full trust application.\r\n
0xb00000c6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in verb element if in a full trust application.\r\n
0xb00000c8 | error %1: App manifest validation error: Line %2, Column %3, Reason: AppExecutionAlias can only be used by Centennial Applications.\r\n
0xb00000c9 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" extension.\r\n
0xb00000ca | error %1: App manifest validation error: Line %2, Column %3, Reason: The Prog Id refrenced by the Class element must have for its CLSID the Class element id value.\r\n
0xb00000cb | error %1: App manifest validation error: Line %2, Column %3, Reason: The VersionIndependentProgId refrenced by the Class element must eventualy resolve in a Prog Id with CLSID matching the Class element id value.\r\n
0xb00000cc | error %1: App manifest validation error: Line %2, Column %3, Reason: Prog Id element can not have its own Id for CurrentVersion.\r\n
0xb00000cd | error %1: App manifest validation error: Line %2, Column %3, Reason: AutoConvertTo attribute of Class can not refer to its own id.\r\n
0xb00000ce | error %1: App manifest validation error: Line %2, Column %3, Reason: If InsertableObject is present then ProgId attribute must also be.\r\n
0xb00000cf | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormats element can not have both DefaultFormatName and DefaultStandardFormat attributes.\r\n
0xb00000d0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The TypeLib element must have either a Win32Path or a Win64Path child element.\r\n
0xb00000d1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormat element can not have both FormatName and StandardFormat attributes.\r\n
0xb00000d2 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Conversion element must have a Readable or ReadWritable child.\r\n
0xb00000d3 | error %1: App manifest validation error: Line %2, Column %3, Reason: If useUniversalMarshaler is true the following attributes should not also exist: ProxyStubClsid, AsynchronousInterface, SynchronousInterface\r\n
0xb00000d4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Interface child element typeLib's ID does not match a typeLib ID which also contains the child element's version number.\r\n
0xb00000d5 | error %1: App manifest validation error: Line %2, Column %3, Reason: Both AsynchronousInterface and SynchronousInterface can't exist in the same Interface element.\r\n
0xb00000d6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The AsynchronousInterface value should match the ID of an Interface with a SynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The SynchronousInterface value should match the ID of an Interface with a AsynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d8 | App manifest validation warning: Declared namespace %1 is inapplicable, it will be ignored during manifest processing.\r\n
0xb00000d9 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName attribute must be specified if ShellNewDisplayName attribute is specified.\r\n
0xb00000da | error %1: App manifest validation error: Line %2, Column %3, Reason: DdeExecCommand attribute must be specified if DdeExecApplication, DdeExecTopic or DdeExecIfExec attribute is specified.\r\n
0xb00000db | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dc | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dd | error %1: App manifest validation error: Line %2, Column %3, Reason: SystemSurrogate attribute and CustomSurrogateExecutable attribute are mutual exclusive.\r\n
0xb00000de | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency with name "%4" and publisher "%5" can't be specified multiple times.\r\n
0xb00000df | error %1: App manifest validation error: Line %2, Column %3, Reason: One and only one of AumId and ShortcutPath attribute should be declared.\r\n
0xb00000e0 | error %1: App manifest validation error: Line %2, Column %3, Reason: Either AppServiceName attribute or ActivatableClassId, Path attributes should be declared.\r\n
0xb00000e1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComServer SurrogateServer referenced by DesktopPropertyHandler must not declare SystemSurrogate or CustomSurrogateExecutable attribute.\r\n
0xb00000e2 | error %1: App manifest validation error: Line %2, Column %3, Reason: PortMin and PortMax attributes should either be both present or not. The value of PortMin attributes should be less than or equal to the value of PortMax attributes.\r\n
0xb00000e3 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support AppService multiple instances, the extension EntryPoint attribute must be declared, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support BackgroundTasks multiple instances, the extension Executable attribute, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e5 | error %1: App content group map validation error: Line %2, Column %3, Reason: %4\r\n
0xb00000e6 | error %1: App manifest validation error: Line %2, Column %3, Reason: SearchFilterHandler extension must declare Path and ProcessorArchitecture on builds later than 10.0.15001.0.\r\n
0xb00000e7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComInterface ProxyStub element must have either Path attribute or ProxyStubDll child element. Path attribute is required if the TargetDeviceFamily is targeting MinVersion 15063 or earlier.\r\n
0xb00000e8 | App manifest validation warning: Line %1, Column %2, Reason: The "%3" element is ignored during manifest processing because it's missing required child elements at xpath "%4".\r\n
0xb00000e9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" extension should be declared under %5 extensions.\r\n
0xb00000ea | error %1: App manifest validation error: Line %2, Column %3, Reason: The ExeServer Conversion Format cannot declare both FormatName and StandardFormat.\r\n
0xb00000eb | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its architecture is unknown.\r\n
0xb00000ec | error %1: App manifest validation error: Line %2, Column %3, Reason: The package extension OutOfProcessServer must declare IdentityType as activateAsPackage if RunFullTrust attribute value is true.\r\n
0xb00000ed | error %1: The XML in the .appinstaller file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000ee | error %1: The namespace "%2" of the root AppInstaller element in the .appinstaller file is not recognized.\r\n
0xb00000ef | error %1: The XML in the .appinstaller file doesn't contain a valid root AppInstaller element.\r\n
0xb00000f0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Content element cannot declare both Parameters attribute and DropTargetHandler attribute.\r\n
0xb00000f1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The binary file value "%4" must use lower case extension (exe or dll) on builds earlier than 10.0.16255.0.\r\n
0xb00000f2 | error %1: App manifest validation error: Line %2, Column %3, Reason: If it is not an audio background task, it is not allowed to have EntryPoint="%4" without ActivatableClassId in windows.activatableClass.inProcessServer.\r\n
0xb00000f3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The %4 element cannot declare the attribute Subsystem with value console without declaring  the attribute SupportsMultipleInstances with value true in element %5.\r\n
0xb00000f4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support Application multiple instances, the ResourceGroup attribute must not be declared.\r\n
0xb00000f5 | error %1: App manifest validation error: Line %2, Column %3, Reason: A <Resource> element is required for packages targeting OS version 10.0.16299.0 or earlier.\r\n
0xb00000f6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The <AllowExecution> property cannot be set to false for packages targeting OS version 10.0.16299.0 or earlier.\r\n
0xb00000f7 | error %1: The XML in the packaging layout file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000f8 | error %1: The namespace "%2" of the root <PackagingLayout> element in the packaging layout file is not recognized.\r\n
0xb00000f9 | error %1: The XML in the packaging layout file doesn't contain a valid root <PackagingLayout> element.\r\n
0xb00000fa | error %1: App manifest validation error: Line %2, Column %3, Reason: The extension windows.barcodeScannerPreviewProvider must be declared with the extension windows.barcodeScannerProvider with the attribute supportsVideoPreview with value "true" in element BarcodeScannerProvider.\r\n
0xb00000fb | error %1: App manifest validation error: Line %2, Column %3, Reason: The element ClassicAppCompatKey must have "Name" or "Name and Value"  or "Name, ValueName, Value and ValueType", any other combination is not valid.\r\n
0xb00000fc | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute Name in element ClassicAppCompatKey cannot be defined under "\\Software\\Microsoft", except under "\\Software\\Microsoft\Office".\r\n
0xb00000fd | error %1: App manifest validation error: Line %2, Column %3, Reason: The combination of atributes "AssemblyName, AssemblyVersion, PublicKey and MachineType" in element PrimaryInteropAssemblies must be unique.\r\n
0xb00000fe | error %1: App manifest validation error: Line %2, Column %3, Reason: Extension "windows.service" must declared with "Executable" and "EntryPoint".\r\n
0xb00000ff | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Partial Trust or Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb0000100 | error %1: App manifest validation error: Line %2, Column %3, Reason: "Default" attribute should be specified as true for only one "Verb" in a set of "SupportedVerbs".\r\n
0xb0000101 | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared with Partial Trust EntryPoint.\r\n
0xb0000102 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ProgId value "%4" must have a length equal to or less than 39 on builds earlier than 10.0.18256.0.\r\n
0xb0000103 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" property.\r\n
0xb0000104 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which targets the same device family.  Bundles can't contain multiple neutral app packages with the same target device family value.\r\n
0xb0000105 | error %1: The bundle contains at least two conflicting app packages. Bundles that contain packages targeting 10.0.17763.0 or lower can't contain more than one neutral application package.\r\n
0xb0000106 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package without MainPackageDependency can't use the "ModificationPackage" property.\r\n
0xb0000107 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute "%4" is required if the TargetDeviceFamily is targeting MinVersion "%5" or earlier.\r\n
0xb0000108 | error %1: App manifest validation error: Line %2, Column %3, Reason: "Default" and "Extended" attributes can't be "True" at the same time.\r\n
0xb0000109 | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" value "%5" must have a length equal to or less than "%6" on builds earlier than "%7".\r\n
0xb000010a | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be "%5" if the attribute %6 on the %7 element is specified.\r\n
0xb000010b | error %1: App manifest validation error: Line %2, Column %3, Reason: The extension windows.activatableClass.outOfProcessServer must declare TrustLevel equals "mediumIL" and RuntimeBehavior equals "packagedClassicApp" when the attribute RunFullTrust under OutProcessServer Element is equal to "true" on builds later than "%4".\r\n
0xb000010c | error %1: App manifest validation error: Line %2, Column %3, Reason: The EntryPoint value "%4" must declare attribute "%5" with value "%6".\r\n
0xb000010d | error %1: App manifest validation error: Line %2, Column %3, Reason: RuntimeBehavior value "win32App" must declare TrustLevel with value "mediumIL"\r\n
0xb000010e | error %1: App manifest validation error: Line %2, Column %3, Reason: Application with RuntimeBehavior value "win32App" must not declare EntryPoint\r\n
0xb000010f | error %1: App manifest validation error: Line %2, Column %3, Reason: Extension windows.hostRuntime must not declare HostId.\r\n
0xb0000110 | error %1: App manifest validation error: Line %2, Column %3, Reason: "%4" with HostId specified can only declare "%5" attribute.\r\n
0xb0000111 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName and ShellNewCommandParameters attributes can't be declared at the same time.\r\n
0xb0000112 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName or ShellNewCommandParameters attributes must be specified if ShellNewDisplayName attribute is specified.\r\n
0xb0000113 | error %1: App manifest validation error: Line %2, Column %3, Reason: %4 can only be used by Centennial Applications.\r\n
0xb0000114 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewDisplayName must be declared with ShellNewFile on builds earlier than 10.0.18901.0.\r\n
0xb0000115 | error %1: App manifest validation error: Line %2, Column %3, Reason: It is not allowed to have ServiceName equals "%4" without a matching attribute "Name" on "Service" element under extension "windows.service".\r\n
0xb0000116 | error %1: App manifest validation error: Line %2, Column %3, Reason: Attribute "%4" is inconsistent in different namespaces under element "%5".\r\n
0xb0000117 | App manifest validation warning: Declared namespace %1 is a preview namespace.\r\n
0xb0000118 | error %1: App manifest validation error: Line %2, Column %3, Reason: SupportedFileTypes must declare at least one FileType from uap namespace on builds earlier than 10.0.18941.0.\r\n
0xb0000119 | error %1: App manifest validation error: Line %2, Column %3, Reason: FileType with value "*" must not declare attributes.\r\n
0xb000011a | error %1: App manifest validation error: Line %2, Column %3, Reason: SupportedFileTypes must declare at least one FileType element.\r\n
0xb000011b | error %1: Stubs in the bundle must contain at least one app package targeting a known processor architecture.\r\n
0xb000011c | error %1: Line %2, Column %3, Reason: The bundle with name "%4" and publisher "%5" cannot appear multiple times.\r\n
0xb000011d | error %1: App manifest validation error: Line %2, Column %3, Reason: Application with RuntimeBehavior value "PackagedClassicApp" must not declare EntryPoint other than "Windows.FullTrustApplication" or "Windows.PartialTrustApplication"\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed. Files Written = %1, Total Size = %2\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xb000018f | The bundle reader was created successfully without manifest validation.\r\n
0xb0000190 | Checking Eappx SIP support for file\r\n
0xb0000191 | Check for Eappx SIP support completed\r\n
0xb0000192 | Returning signature or signature size from encrypted app package\r\n
0xb0000193 | Signature or signature size returned from encrypted app package\r\n
0xb0000194 | Adding signature to encrypted app package\r\n
0xb0000195 | Signature added to encrypted app package\r\n
0xb0000196 | Removing signature from encrypted app package\r\n
0xb0000197 | Signature removed from encrypted app package\r\n
0xb0000198 | Creating or sizing encrypted app indirect data\r\n
0xb0000199 | Encrypted app indirect data created or sized\r\n
0xb000019a | Verifying encrypted app indirect data\r\n
0xb000019b | Encrypted app indirect data verified\r\n
0xb000019c | Checking EappxBundle SIP support for file\r\n
0xb000019d | Check for EappxBundle SIP support completed\r\n
0xb000019e | Returning signature or signature size from encrypted app bundle\r\n
0xb000019f | Signature or signature size returned from encrypted app bundle\r\n
0xb00001a0 | Adding signature to encrypted app bundle\r\n
0xb00001a1 | Signature added to encrypted app bundle\r\n
0xb00001a2 | Removing signature from encrypted app bundle\r\n
0xb00001a3 | Signature removed from encrypted app bundle\r\n
0xb00001a4 | Creating or sizing encrypted bundle indirect data\r\n
0xb00001a5 | Encrypted bundle indirect data created or sized\r\n
0xb00001a6 | Verifying encrypted bundle indirect data\r\n
0xb00001a7 | Encrypted bundle indirect data verified\r\n
0xb00001a8 | Adding payload files, file count = %1\r\n
0xb00001a9 | Payload files added\r\n
0xb00001aa | Processing payload file, file name = %1, content type = %2, compression = %3\r\n
0xb00001ab | Payload file processed\r\n
0xb00001ac | Adding reference package\r\n
0xb00001ad | Reference package added\r\n
0xb00001ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same package full name.\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n

### 10.0.22000.184

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x3004000b | Parse Manifest\r\n
0x3007000b | Signing\r\n
0x3007000c | Verifying\r\n
0x3037000b | Parse CGM\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x70000001 | Package writer\r\n
0x70000002 | Package reader\r\n
0x70000003 | Package streaming reader\r\n
0x70000004 | Manifest\r\n
0x70000005 | Blockmap\r\n
0x70000006 | Packaging API internal\r\n
0x70000007 | Digital Signature\r\n
0x7000001b | Bundle writer\r\n
0x70000027 | Bundle reader\r\n
0x70000028 | Bundle streaming reader\r\n
0x70000029 | Bundle manifest\r\n
0x70000037 | Content Group Map\r\n
0x7000003b | AppInstaller\r\n
0x7000003c | PackagingLayout\r\n
0x7000003d | Publisher bridging\r\n
0x90000001 | Microsoft-Windows-AppxPackagingOM\r\n
0x90000002 | Microsoft-Windows-AppxPackaging/Operational\r\n
0x90000003 | Microsoft-Windows-AppxPackaging/Performance\r\n
0x90000004 | Microsoft-Windows-AppxPackaging/Debug\r\n
0xb0000064 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Reason: %4\r\n
0xb0000065 | error %1: App manifest validation error: The document root element %2 must be defined in the %3 namespace.\r\n
0xb0000066 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the domain name segment if the Type attribute value is "include".\r\n
0xb0000067 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not use wildcards in the host name segment if a domain name is not present and the Type attribute value is "include".\r\n
0xb0000068 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must not specify values "*" or "*.*" if the Type attribute value is "exclude".\r\n
0xb0000069 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute URI as per the CreateUri API.\r\n
0xb000006a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must be a valid absolute or relative URI as per the CreateUri API.\r\n
0xb000006b | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application element must specify the Executable or StartPage attribute.\r\n
0xb000006e | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the Wide310x150Logo attribute if the Square310x310Logo attribute is specified.\r\n
0xb000006f | error %1: App manifest validation error: Line %2, Column %3, Reason: The logo %4 must be specified if the %5 value is set to "%6".\r\n
0xb0000070 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element must specify the Executable attribute with the EntryPoint attribute for a web application.\r\n
0xb0000071 | error %1: App manifest validation error: Line %2, Column %3, Reason: The UriTemplate field must specify an absolute URI with the scheme HTTP or HTTPS.\r\n
0xb0000072 | error %1: App manifest validation error: Line %2, Column %3, Reason: The max version tested value must not be less than the min version value.\r\n
0xb0000073 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "https" scheme if it's an absolute URI.\r\n
0xb0000074 | error %1: App manifest validation error: Line %2, Column %3, Reason: The manifest must specify at least one Resource element with a Language attribute.\r\n
0xb0000075 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Language attribute value "%4" must comply with BCP 47 specification.\r\n
0xb0000076 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify a child element.\r\n
0xb0000077 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify a child element.\r\n
0xb0000078 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the matching child element.\r\n
0xb0000079 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "%4" must only be declared once.\r\n
0xb000007a | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with Category attribute value "windows.shareTarget" must specify either a SupportedFileTypes child element or at least one DataFormat child element.\r\n
0xb000007b | error %1: App manifest validation error: The app manifest XML must be valid: Line %2, Column %3, Reason: %4\r\n
0xb000007c | error %1: App manifest validation error: Line %2, Column %3, Reason: The Identity/@Name attribute value "%4" must not contain a reserved name.\r\n
0xb000007e | error %1: App manifest validation error: Line %2, Column %3, Reason: The Application/@Id attribute value "%4" must not contain the reserved name "%5".\r\n
0xb000007f | error %1: App manifest validation error: Line %2, Column %3, Reason: The field "%4" with value "%5" must only be declared once. A duplicate exists on Line %6, Column %7.\r\n
0xb0000080 | error %1: App manifest validation error: The app manifest schema must be valid: Reason: %2\r\n
0xb0000081 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Publisher attribute value "%4" must be valid as per publisher naming rules.\r\n
0xb0000082 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must specify the EntryPoint or StartPage attribute.\r\n
0xb0000083 | error %1: App manifest validation error: Line %2, Column %3, Reason: The DefaultTile element must specify the WideLogo or Wide310x150Logo attribute if the LockScreen Notification attribute is specified as "badgeAndTileText".\r\n
0xb0000084 | error %1: App manifest validation error: The app manifest XML encoding must be UTF-8 or UTF-16.\r\n
0xb0000085 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000086 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must not be specified if the attribute %5 on the %6 element is specified.\r\n
0xb0000087 | error %1: App manifest validation error: The app manifest must be valid as per schema: Line %2, Column %3, Note: The schema for MaxVersionTested specified does not recognize XML fields with namespace "%4". Please ensure that you have the correct MaxVersionTested specified. Reason: %5\r\n
0xb000008b | error %1: App manifest validation error: Line %2, Column %3, Reason: The field %4 must not be specified if the ResourcePackage element value "true" is specified.\r\n
0xb000008c | error %1: App manifest validation error: Line %2, Column %3, Reason: Only one type of resource qualifier can be specified for a resource package.  Attribute %4 must be the same as attribute %5 on element %6.\r\n
0xb000008d | error %1: App manifest validation error: Line %2, Column %3, Reason: The Framework and ResourcePackage element values must not be specified to "true" at the same time.\r\n
0xb000008e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify at least one attribute.\r\n
0xb000008f | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element must specify the Executable attribute with the EntryPoint attribute if neither the Application nor the Extension element specify an Executable.\r\n
0xb0000090 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ServiceId element must specify the Executable attribute with the EntryPoint attribute if the Application, the Extension or the LaunchAction element do not specify an Executable.\r\n
0xb0000091 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must not specify ServiceId elements if the Verb attribute is specified as "map".\r\n
0xb0000092 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must specify at least one ServiceId element if any Verb attribute other than "map" is specified.\r\n
0xb0000093 | error %1: App manifest validation error: Line %2, Column %3, Reason: The LaunchAction element under ContactLaunchActions must only specify the ServiceId value as "telephone" if the Verb attribute is specified as "call" or "message".\r\n
0xb0000096 | error %1: The app manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb0000097 | error %1: The signature hash method specified (%3) must match the hash method used in the app package block map (%2).\r\n
0xb0000098 | error %1: The app package contents must validate against its block map.\r\n
0xb0000099 | error %1: The signature in the app package or bundle must be trusted.\r\n
0xb000009a | error %1: The root certificate of the signature in the app package or bundle must be trusted.\r\n
0xb000009b | error %1: The root certificate and all intermediate certificates of the signature in the app package or bundle must be trusted.\r\n
0xb000009c | error %1: The app package must be digitally signed for signature validation.\r\n
0xb000009d | The app package signature was validated for core content of the app package published by %1. Payload won't be validated until the files are read.\r\n
0xb000009e | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must not be specified if the Framework element value "true" is specified.\r\n
0xb000009f | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must specify a host name segment if the Type attribute value is "include".\r\n
0xb00000a0 | error %1: The app bundle manifest publisher name (%3) must match the subject name of the signing certificate (%2).\r\n
0xb00000a1 | error %1: The signature hash method specified (%3) must match the hash method used in the app bundle block map (%2).\r\n
0xb00000a2 | error %1: An app package (%2) in the bundle could not be signed.\r\n
0xb00000a3 | error %1: The app bundle must be digitally signed for signature validation.\r\n
0xb00000a4 | The app bundle signature was validated for core content of the app bundle published by %1. App packages won't be validated until they are read.\r\n
0xb00000a5 | error %1: An encrypted app package (ID = %2) in the bundle could not be signed.\r\n
0xb00000aa | The streaming reader was created successfully for app package %1.\r\n
0xb00000ab | The reader was created successfully for app package %1.\r\n
0xb00000ac | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it's a framework package.\r\n
0xb00000ad | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which applies to the same processor architecture.  Bundles can't contain multiple app packages for the same processor architecture, or an architecture-neutral app package with any architecture-specific app package.\r\n
0xb00000ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which has the same resource ID.  Bundles can't contain multiple resource packages with the same resource ID.\r\n
0xb00000af | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it uses a different hash algorithm than other packages in the bundle. The expected hash algorithm is %4.\r\n
0xb00000b0 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected package name is %4.\r\n
0xb00000b1 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because it has a different package family name than other packages in the bundle. The expected publisher is %4.\r\n
0xb00000b2 | error %1: The bundle must contain at least one app package targeting a known processor architecture.\r\n
0xb00000b3 | error %1: The bundle can't contain more than 10000 packages.\r\n
0xb00000b4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Extension element with the Category attribute value "%4" must not specify the "%5" attribute.\r\n
0xb00000b5 | The reader was created successfully without manifest validation.\r\n
0xb00000b6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The StartPage attribute must be a valid URI.\r\n
0xb00000b7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Executable attribute for the windows.backgroundTask extension must be "wwahost.exe" when StartPage is specified.\r\n
0xb00000b8 | error %1: The chaining mode string for encryption algorithm cannot be empty.\r\n
0xb00000b9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The WindowsRuntimeAccess attribute must not be specified if the Type attribute value is "exclude".\r\n
0xb00000ba | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http", "https" or "ms-appx-web" scheme if it's an absolute URI.\r\n
0xb00000bb | error %1: App manifest validation error: Line %2, Column %3, Reason: The Match attribute value must only specify the "http" or "https" scheme if it's an absolute URI and the Type attribute value is "exclude".\r\n
0xb00000bc | error %1: App manifest validation error: Line %2, Column %3, Reason: The Url specified is a duplicate of the base Url specified for the windows.webAccountProvider extension\r\n
0xb00000bd | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP manifests.\r\n
0xb00000be | error %1: App manifest validation error: Line %2, Column %3, Reason: Windows.FullTrustApplication entry points are only valid for UWP desktop applications whose minVersion >= 10.0.14257.0.\r\n
0xb00000bf | error %1: App manifest validation error: Line %2, Column %3, Reason: The element specified requires "%4" capability.\r\n
0xb00000c0 | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency can't be specified when the %4 element is specified.\r\n
0xb00000c1 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't target version %5 of device family "%4".  You must specify a higher MinVersion.\r\n
0xb00000c3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The use of startuptask extension requires the containing Application use the Windows.FullTrustApplication entry point.\r\n
0xb00000c4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c5 | error %1: App manifest validation error: Line %2, Column %3, Reason: The parameter attribute can only be used in prototype element if in a full trust application.\r\n
0xb00000c6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in filetype association element if in a full trust application.\r\n
0xb00000c7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The MultiSelectModel attribute can only be used in verb element if in a full trust application.\r\n
0xb00000c8 | error %1: App manifest validation error: Line %2, Column %3, Reason: AppExecutionAlias can only be used by Centennial Applications.\r\n
0xb00000c9 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" extension.\r\n
0xb00000ca | error %1: App manifest validation error: Line %2, Column %3, Reason: The Prog Id refrenced by the Class element must have for its CLSID the Class element id value.\r\n
0xb00000cb | error %1: App manifest validation error: Line %2, Column %3, Reason: The VersionIndependentProgId refrenced by the Class element must eventualy resolve in a Prog Id with CLSID matching the Class element id value.\r\n
0xb00000cc | error %1: App manifest validation error: Line %2, Column %3, Reason: Prog Id element can not have its own Id for CurrentVersion.\r\n
0xb00000cd | error %1: App manifest validation error: Line %2, Column %3, Reason: AutoConvertTo attribute of Class can not refer to its own id.\r\n
0xb00000ce | error %1: App manifest validation error: Line %2, Column %3, Reason: If InsertableObject is present then ProgId attribute must also be.\r\n
0xb00000cf | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormats element can not have both DefaultFormatName and DefaultStandardFormat attributes.\r\n
0xb00000d0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The TypeLib element must have either a Win32Path or a Win64Path child element.\r\n
0xb00000d1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The dataFormat element can not have both FormatName and StandardFormat attributes.\r\n
0xb00000d2 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Conversion element must have a Readable or ReadWritable child.\r\n
0xb00000d3 | error %1: App manifest validation error: Line %2, Column %3, Reason: If useUniversalMarshaler is true the following attributes should not also exist: ProxyStubClsid, AsynchronousInterface, SynchronousInterface\r\n
0xb00000d4 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Interface child element typeLib's ID does not match a typeLib ID which also contains the child element's version number.\r\n
0xb00000d5 | error %1: App manifest validation error: Line %2, Column %3, Reason: Both AsynchronousInterface and SynchronousInterface can't exist in the same Interface element.\r\n
0xb00000d6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The AsynchronousInterface value should match the ID of an Interface with a SynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The SynchronousInterface value should match the ID of an Interface with a AsynchronousInterface which matches the current Interface's ID. Also the two Interface's ProxyStubClsid should match.\r\n
0xb00000d8 | App manifest validation warning: Declared namespace %1 is inapplicable, it will be ignored during manifest processing.\r\n
0xb00000d9 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName attribute must be specified if ShellNewDisplayName attribute is specified.\r\n
0xb00000da | error %1: App manifest validation error: Line %2, Column %3, Reason: DdeExecCommand attribute must be specified if DdeExecApplication, DdeExecTopic or DdeExecIfExec attribute is specified.\r\n
0xb00000db | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dc | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared outside of Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb00000dd | error %1: App manifest validation error: Line %2, Column %3, Reason: SystemSurrogate attribute and CustomSurrogateExecutable attribute are mutual exclusive.\r\n
0xb00000de | error %1: App manifest validation error: Line %2, Column %3, Reason: MainPackageDependency with name "%4" and publisher "%5" can't be specified multiple times.\r\n
0xb00000df | error %1: App manifest validation error: Line %2, Column %3, Reason: One and only one of AumId and ShortcutPath attribute should be declared.\r\n
0xb00000e0 | error %1: App manifest validation error: Line %2, Column %3, Reason: Either AppServiceName attribute or ActivatableClassId, Path attributes should be declared.\r\n
0xb00000e1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComServer SurrogateServer referenced by DesktopPropertyHandler must not declare SystemSurrogate or CustomSurrogateExecutable attribute.\r\n
0xb00000e2 | error %1: App manifest validation error: Line %2, Column %3, Reason: PortMin and PortMax attributes should either be both present or not. The value of PortMin attributes should be less than or equal to the value of PortMax attributes.\r\n
0xb00000e3 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support AppService multiple instances, the extension EntryPoint attribute must be declared, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support BackgroundTasks multiple instances, the extension Executable attribute, ResourceGroup attribute and ServerName attribute must not be declared.\r\n
0xb00000e5 | error %1: App content group map validation error: Line %2, Column %3, Reason: %4\r\n
0xb00000e6 | error %1: App manifest validation error: Line %2, Column %3, Reason: SearchFilterHandler extension must declare Path and ProcessorArchitecture on builds later than 10.0.15001.0.\r\n
0xb00000e7 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ComInterface ProxyStub element must have either Path attribute or ProxyStubDll child element. Path attribute is required if the TargetDeviceFamily is targeting MinVersion 15063 or earlier.\r\n
0xb00000e8 | App manifest validation warning: Line %1, Column %2, Reason: The "%3" element is ignored during manifest processing because it's missing required child elements at xpath "%4".\r\n
0xb00000e9 | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" extension should be declared under %5 extensions.\r\n
0xb00000ea | error %1: App manifest validation error: Line %2, Column %3, Reason: The ExeServer Conversion Format cannot declare both FormatName and StandardFormat.\r\n
0xb00000eb | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its architecture is unknown.\r\n
0xb00000ec | error %1: App manifest validation error: Line %2, Column %3, Reason: The package extension OutOfProcessServer must declare IdentityType as activateAsPackage if RunFullTrust attribute value is true.\r\n
0xb00000ed | error %1: The XML in the .appinstaller file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000ee | error %1: The namespace "%2" of the root AppInstaller element in the .appinstaller file is not recognized.\r\n
0xb00000ef | error %1: The XML in the .appinstaller file doesn't contain a valid root AppInstaller element.\r\n
0xb00000f0 | error %1: App manifest validation error: Line %2, Column %3, Reason: The Content element cannot declare both Parameters attribute and DropTargetHandler attribute.\r\n
0xb00000f1 | error %1: App manifest validation error: Line %2, Column %3, Reason: The binary file value "%4" must use lower case extension (exe or dll) on builds earlier than 10.0.16255.0.\r\n
0xb00000f2 | error %1: App manifest validation error: Line %2, Column %3, Reason: If it is not an audio background task, it is not allowed to have EntryPoint="%4" without ActivatableClassId in windows.activatableClass.inProcessServer.\r\n
0xb00000f3 | error %1: App manifest validation error: Line %2, Column %3, Reason: The %4 element cannot declare the attribute Subsystem with value console without declaring  the attribute SupportsMultipleInstances with value true in element %5.\r\n
0xb00000f4 | error %1: App manifest validation error: Line %2, Column %3, Reason: To support Application multiple instances, the ResourceGroup attribute must not be declared.\r\n
0xb00000f5 | error %1: App manifest validation error: Line %2, Column %3, Reason: A <Resource> element is required for packages targeting OS version 10.0.16299.0 or earlier.\r\n
0xb00000f6 | error %1: App manifest validation error: Line %2, Column %3, Reason: The <AllowExecution> property cannot be set to false for packages targeting OS version 10.0.16299.0 or earlier.\r\n
0xb00000f7 | error %1: The XML in the packaging layout file is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00000f8 | error %1: The namespace "%2" of the root <PackagingLayout> element in the packaging layout file is not recognized.\r\n
0xb00000f9 | error %1: The XML in the packaging layout file doesn't contain a valid root <PackagingLayout> element.\r\n
0xb00000fa | error %1: App manifest validation error: Line %2, Column %3, Reason: The extension windows.barcodeScannerPreviewProvider must be declared with the extension windows.barcodeScannerProvider with the attribute supportsVideoPreview with value "true" in element BarcodeScannerProvider.\r\n
0xb00000fb | error %1: App manifest validation error: Line %2, Column %3, Reason: The element ClassicAppCompatKey must have "Name" or "Name and Value"  or "Name, ValueName, Value and ValueType", any other combination is not valid.\r\n
0xb00000fc | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute Name in element ClassicAppCompatKey cannot be defined under "\\Software\\Microsoft", except under "\\Software\\Microsoft\Office".\r\n
0xb00000fd | error %1: App manifest validation error: Line %2, Column %3, Reason: The combination of atributes "AssemblyName, AssemblyVersion, PublicKey and MachineType" in element PrimaryInteropAssemblies must be unique.\r\n
0xb00000fe | error %1: App manifest validation error: Line %2, Column %3, Reason: Extension "windows.service" must declared with "Executable" and "EntryPoint".\r\n
0xb00000ff | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" can't be declared outside of Partial Trust or Full Trust EntryPoint(either inherited from Application or declared in the Extension).\r\n
0xb0000100 | error %1: App manifest validation error: Line %2, Column %3, Reason: "Default" attribute should be specified as true for only one "Verb" in a set of "SupportedVerbs".\r\n
0xb0000101 | error %1: App manifest validation error: Line %2, Column %3, Reason: The "%4" Extension can't be declared with Partial Trust EntryPoint.\r\n
0xb0000102 | error %1: App manifest validation error: Line %2, Column %3, Reason: The ProgId value "%4" must have a length equal to or less than 39 on builds earlier than 10.0.18256.0.\r\n
0xb0000103 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package containing MainPackageDependency can't use the "%4" property.\r\n
0xb0000104 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle also contains the package with file name "%4" and package full name "%5" which targets the same device family.  Bundles can't contain multiple neutral app packages with the same target device family value.\r\n
0xb0000105 | error %1: The bundle contains at least two conflicting app packages. Bundles that contain packages targeting 10.0.17763.0 or lower can't contain more than one neutral application package.\r\n
0xb0000106 | error %1: App manifest validation error: Line %2, Column %3, Reason: A package without MainPackageDependency can't use the "ModificationPackage" property.\r\n
0xb0000107 | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute "%4" is required if the TargetDeviceFamily is targeting MinVersion "%5" or earlier.\r\n
0xb0000108 | error %1: App manifest validation error: Line %2, Column %3, Reason: "Default" and "Extended" attributes can't be "True" at the same time.\r\n
0xb0000109 | error %1: App manifest validation error: Line %2, Column %3, Reason: The element or attribute "%4" value "%5" must have a length equal to or less than "%6" on builds earlier than "%7".\r\n
0xb000010a | error %1: App manifest validation error: Line %2, Column %3, Reason: The attribute %4 must be "%5" if the attribute %6 on the %7 element is specified.\r\n
0xb000010b | error %1: App manifest validation error: Line %2, Column %3, Reason: The extension windows.activatableClass.outOfProcessServer must declare TrustLevel equals "mediumIL" and RuntimeBehavior equals "packagedClassicApp" when the attribute RunFullTrust under OutProcessServer Element is equal to "true" on builds later than "%4".\r\n
0xb000010c | error %1: App manifest validation error: Line %2, Column %3, Reason: The EntryPoint value "%4" must declare attribute "%5" with value "%6".\r\n
0xb000010d | error %1: App manifest validation error: Line %2, Column %3, Reason: RuntimeBehavior value "win32App" must declare TrustLevel with value "mediumIL"\r\n
0xb000010e | error %1: App manifest validation error: Line %2, Column %3, Reason: Application with RuntimeBehavior value "win32App" must not declare EntryPoint\r\n
0xb000010f | error %1: App manifest validation error: Line %2, Column %3, Reason: Extension windows.hostRuntime must not declare HostId.\r\n
0xb0000110 | error %1: App manifest validation error: Line %2, Column %3, Reason: "%4" with HostId specified can only declare "%5" attribute.\r\n
0xb0000111 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName and ShellNewCommandParameters attributes can't be declared at the same time.\r\n
0xb0000112 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewFileName or ShellNewCommandParameters attributes must be specified if ShellNewDisplayName attribute is specified.\r\n
0xb0000113 | error %1: App manifest validation error: Line %2, Column %3, Reason: %4 can only be used by Centennial Applications.\r\n
0xb0000114 | error %1: App manifest validation error: Line %2, Column %3, Reason: ShellNewDisplayName must be declared with ShellNewFile on builds earlier than 10.0.18901.0.\r\n
0xb0000115 | error %1: App manifest validation error: Line %2, Column %3, Reason: It is not allowed to have ServiceName equals "%4" without a matching attribute "Name" on "Service" element under extension "windows.service".\r\n
0xb0000116 | error %1: App manifest validation error: Line %2, Column %3, Reason: Attribute "%4" is inconsistent in different namespaces under element "%5".\r\n
0xb0000117 | App manifest validation warning: Declared namespace %1 is a preview namespace.\r\n
0xb0000118 | error %1: App manifest validation error: Line %2, Column %3, Reason: SupportedFileTypes must declare at least one FileType from uap namespace on builds earlier than 10.0.18941.0.\r\n
0xb0000119 | error %1: App manifest validation error: Line %2, Column %3, Reason: FileType with value "*" must not declare attributes.\r\n
0xb000011a | error %1: App manifest validation error: Line %2, Column %3, Reason: SupportedFileTypes must declare at least one FileType element.\r\n
0xb000011b | error %1: Stubs in the bundle must contain at least one app package targeting a known processor architecture.\r\n
0xb000011c | error %1: Line %2, Column %3, Reason: The bundle with name "%4" and publisher "%5" cannot appear multiple times.\r\n
0xb000011d | error %1: App manifest validation error: Line %2, Column %3, Reason: Application with RuntimeBehavior value "PackagedClassicApp" must not declare EntryPoint other than "Windows.FullTrustApplication" or "Windows.PartialTrustApplication"\r\n
0xb000011e | error %1: App manifest validation error: Line %2, Column %3, Reason: Extension "windows.comServer" must be declared on application level.\r\n
0xb000011f | error %1: App manifest validation error: Line %2, Column %3, Reason: Package extension "windows.comServer" must not declared the elements "ExeServer", "SurrogateServer", or "ServiceServer".\r\n
0xb0000120 | error %1: App manifest validation error: Line %2, Column %3, Reason: Element "%4" must not specify fullpath on "CurrentDirectoryPath" when "HostId" is not present.\r\n
0xb0000121 | error %1: App manifest validation error: Line %2, Column %3, Reason: Element "%4" must have at least one child element.\r\n
0xb0000122 | error %1: App manifest validation error: Line %2, Column %3, Reason: Subsystem is inconsistent between Extension and AppService %4:Subsystem.\r\n
0xb0000123 | error %1: App manifest validation error: Line %2, Column %3, Reason: The element %4 must specify only one attribute.\r\n
0xb0000124 | error %1: App manifest validation error: Line %2, Column %3, Reason: The package contains an XML prefix that is not defined.\r\n
0xb0000125 | error %1: App manifest validation error: Line %2, Column %3, Reason: Extension "%4" must declare SupportsMultipleInstances equals true.\r\n
0xb0000126 | error %1: App manifest validation error: Line %2, Column %3, Reason: Extension "windows.comServer" must be "%4" or newer on package level.\r\n
0xb0000127 | error %1: App manifest validation error: Line %2, Column %3, Reason: Attribute "IdentityType" with value "activateAsPackage" on element "outOfProcessServer" can't be used in Framework Package.\r\n
0xb0000128 | error %1: App manifest validation error: Line %2, Column %3, Reason: Extension "%4" requires "Scope" equals "%5".\r\n
0xb000012a | error %1: App manifest validation error: Line %2, Column %3, Reason: Dependencies can't declare element "%4" more than %5.\r\n
0xb000012b | error %1: App manifest validation error: Line %2, Column %3, Reason: If the attribute "Id" is delacred with value "%4" on element "TypeLib" in the extension "windows.comServer", the extension "windows.comInterface" must declare an attribute "Id" with value equals "%4" on element "TypeLib"\r\n
0xb000012c | Creating IAppxPackageWriter, force Zip32 format = %1, hash method = %2\r\n
0xb000012d | IAppxPackageWriter closed. Files Written = %1, Total Size = %2\r\n
0xb000012e | Adding payload file, file name = %1, content type = %2, compression = %3\r\n
0xb000012f | Payload file added\r\n
0xb0000130 | Adding footprint files and closing IAppxPackageWriter\r\n
0xb0000131 | IAppxPackageWriter closed\r\n
0xb0000132 | Creating IAppxPackageReader\r\n
0xb0000133 | IAppxPackageReader created\r\n
0xb0000134 | Caching and validating block hash of payload file, file name = %1, size = %2, compression = %3\r\n
0xb0000135 | Payload file cached and validated\r\n
0xb0000136 | Creating IAppxPackageStreamingReader, options = %1\r\n
0xb0000137 | IAppxPackageStreamingReader created\r\n
0xb0000138 | Executing %1 range requests in IAppxRequestHandler, priority = %2\r\n
0xb0000139 | Range requests completed\r\n
0xb000013a | Creating app manifest reader\r\n
0xb000013b | App manifest reader created\r\n
0xb000013c | Creating blockmap reader\r\n
0xb000013d | Blockmap reader created\r\n
0xb000013e | Decompressing block, compressed size = %1\r\n
0xb000013f | Block decompressed, uncompressed size = %1\r\n
0xb0000140 | Downloading package metadata\r\n
0xb0000141 | Package metadata downloaded\r\n
0xb000015e | Checking SIP support for file\r\n
0xb000015f | Check for SIP support completed\r\n
0xb0000160 | Returning signature or signature size from app package\r\n
0xb0000161 | Signature or signature size returned from app package\r\n
0xb0000162 | Adding signature to app package\r\n
0xb0000163 | Signature added to app package\r\n
0xb0000164 | Removing signature from app package\r\n
0xb0000165 | Signature removed from app package\r\n
0xb0000166 | Creating or sizing indirect data\r\n
0xb0000167 | Indirect data created or sized\r\n
0xb0000168 | Verifying indirect data\r\n
0xb0000169 | Indirect data verified\r\n
0xb000016a | Looking up friendly names for capability with SID %1\r\n
0xb000016b | Looking up friendly names for capability with SID %1 finished with result %2\r\n
0xb000016c | Verifying the file stream against the block map file hash\r\n
0xb000016d | Block map file hash verified against the file stream\r\n
0xb000016e | Creating IAppxBundleWriter\r\n
0xb000016f | IAppxBundleWriter closed\r\n
0xb0000170 | Adding payload package\r\n
0xb0000171 | Payload package added\r\n
0xb0000172 | Adding footprint files and closing IAppxBundleWriter\r\n
0xb0000173 | Footprint files added and IAppxBundleWriter closed\r\n
0xb0000174 | Checking AppxBundle SIP support for file\r\n
0xb0000175 | Check for AppxBundle SIP support completed\r\n
0xb0000176 | Returning signature or signature size from app bundle\r\n
0xb0000177 | Signature or signature size returned from app bundle\r\n
0xb0000178 | Adding signature to app bundle\r\n
0xb0000179 | Signature added to app bundle\r\n
0xb000017a | Removing signature from app bundle\r\n
0xb000017b | Signature removed from app bundle\r\n
0xb000017c | Creating or sizing bundle indirect data\r\n
0xb000017d | Bundle indirect data created or sized\r\n
0xb000017e | Verifying bundle indirect data\r\n
0xb000017f | Bundle indirect data verified\r\n
0xb0000180 | Creating IAppxBundleReader\r\n
0xb0000181 | IAppxBundleReader created\r\n
0xb0000184 | Creating bundle manifest reader\r\n
0xb0000185 | Bundle manifest reader created\r\n
0xb0000186 | The bundle reader was created successfully for bundle %1.\r\n
0xb0000187 | The bundle streaming reader was created successfully for bundle %1.\r\n
0xb0000188 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same file name.\r\n
0xb0000189 | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its package type doesn't match the value found in the bundle manifest.\r\n
0xb000018a | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its identity doesn't match the value found in the bundle manifest. The expected package full name is %4.\r\n
0xb000018b | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its resources don't match the values found in the bundle manifest.\r\n
0xb000018c | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest declares a value for %4 which isn't supported in bundles.  The minimum supported value is %5.\r\n
0xb000018d | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because its manifest doesn't declare any Application elements.\r\n
0xb000018e | error %1: All app package manifests in a bundle must declare the same values under the XPath %10.  The values under this XPath declared in the manifest for the package with file name "%2" and package full name "%3" at line %4, column %5 don't match those declared in the manifest for the package with file name "%6" and package full name "%7" at line %8, column %9.\r\n
0xb000018f | The bundle reader was created successfully without manifest validation.\r\n
0xb0000190 | Checking Eappx SIP support for file\r\n
0xb0000191 | Check for Eappx SIP support completed\r\n
0xb0000192 | Returning signature or signature size from encrypted app package\r\n
0xb0000193 | Signature or signature size returned from encrypted app package\r\n
0xb0000194 | Adding signature to encrypted app package\r\n
0xb0000195 | Signature added to encrypted app package\r\n
0xb0000196 | Removing signature from encrypted app package\r\n
0xb0000197 | Signature removed from encrypted app package\r\n
0xb0000198 | Creating or sizing encrypted app indirect data\r\n
0xb0000199 | Encrypted app indirect data created or sized\r\n
0xb000019a | Verifying encrypted app indirect data\r\n
0xb000019b | Encrypted app indirect data verified\r\n
0xb000019c | Checking EappxBundle SIP support for file\r\n
0xb000019d | Check for EappxBundle SIP support completed\r\n
0xb000019e | Returning signature or signature size from encrypted app bundle\r\n
0xb000019f | Signature or signature size returned from encrypted app bundle\r\n
0xb00001a0 | Adding signature to encrypted app bundle\r\n
0xb00001a1 | Signature added to encrypted app bundle\r\n
0xb00001a2 | Removing signature from encrypted app bundle\r\n
0xb00001a3 | Signature removed from encrypted app bundle\r\n
0xb00001a4 | Creating or sizing encrypted bundle indirect data\r\n
0xb00001a5 | Encrypted bundle indirect data created or sized\r\n
0xb00001a6 | Verifying encrypted bundle indirect data\r\n
0xb00001a7 | Encrypted bundle indirect data verified\r\n
0xb00001a8 | Adding payload files, file count = %1\r\n
0xb00001a9 | Payload files added\r\n
0xb00001aa | Processing payload file, file name = %1, content type = %2, compression = %3\r\n
0xb00001ab | Payload file processed\r\n
0xb00001ac | Adding reference package\r\n
0xb00001ad | Reference package added\r\n
0xb00001ae | error %1: The package with file name "%2" and package full name "%3" is not valid in the bundle because the bundle contains another package with the same package full name.\r\n
0xb00001af | Adding publisher bridging artifact to package\r\n
0xb00001b0 | Added publisher bridging artifact to package\r\n
0xb00001b1 | Adding publisher bridging artifact to bundle\r\n
0xb00001b2 | Added publisher bridging artifact to bundle\r\n
0xb00003e8 | error %1: App manifest validation error: Line %2, Column %3, Reason: Attribute "Id" with value "%4" on elements "Class" and "TreatAsClass" must be unique accross the package\r\n
0xb00003e9 | error %1: App manifest validation error: Line %2, Column %3, Reason: Attribute "Id" with value "%4" on element "ProgId" must be unique accross the package\r\n
0xb00003ea | error %1: App manifest validation error: Line %2, Column %3, Reason: Attribute "Id" with value "%4" on element "TypeLib" must be unique accross the package\r\n
0xb00003eb | error %1: App manifest validation error: Line %2, Column %3, Reason: Attribute "%4" with value "%5" on element "%6" must be define on attribute "Id" on element "%7"\r\n
0xb00003ec | error %1: App manifest validation error: Line %2, Column %3, Reason: Element "TypeLib" must match attributes "Id" and "VersionNumber" on element "TypeLib" on extension "windows.comInterface"\r\n
0xb00003ed | error %1: App manifest validation error: Line %2, Column %3, Reason: Attribute "Clsid" with value "%4" must define an Element "Class" on element "SurrogateServer" with the same attribute "Id" on extension "windows.comServer"\r\n
0xb00003ee | error %1: The XML in the publisher bridging artifact is not valid: Line %2, Column %3, Reason: %4\r\n
0xb00003ef | error %1: The namespace "%2" of the root <Publisher> element in the publisher bridging artifact is not recognized.\r\n
0xb00003f0 | error %1: The XML in the publisher bridging artifact doesn't contain a valid root Publisher element.\r\n
0xd0000001 | None\r\n
0xd0000002 | Normal\r\n
0xd0000003 | Maximum\r\n
0xd0000004 | Fast\r\n
0xd0000005 | Super fast\r\n
0xd0000006 | Low\r\n
0xd0000007 | Medium\r\n
0xd0000008 | High\r\n
0xf0000001 | Verify signature\r\n
