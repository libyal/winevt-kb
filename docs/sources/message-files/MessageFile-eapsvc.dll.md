## eapsvc.dll

Path: %SystemRoot%\system32\eapsvc.dll

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x000003e9 | Method not registered or method's registry data could not be accessed. LoadConfig: FriendlyName, ConfigCLSID both are empty\r\n
0x000003ea | Unable to parse malformed EAP packet\r\n
0x000003eb | Method not registered or registry value error: Function Name=LoadConfig, ArgumentName=%1\r\n
0x000003ec | Negotiation failed. No available EAP methods\r\n
0x000003ed | Negotiation failed. Proposed methods list from peer is invalid\r\n
0x000003ee | Negotiation failed. Requested EAP methods not available\r\n
0x000007d1 | Eap method friendly name can not be verified or %1 path could not be accessed; Error: type(%2), authId(%3), vendorId(%4), vendorType(%5)\r\n
0x000007d2 | Skipping: %1 validation failed. Error: typeId=%2, authorId=%3, vendorId=%4, vendorType=%5\r\n
0x00000bb9 | EAPHost failed to load. LoadLibraryW(%1) failed %2\r\n
0x00000bba | Could not find the requested EapMethod: TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0x00000be9 | Exceeded the maximum number(32) of Third Party EapHost processes. Running the current eap session in short lived Eap3Host process.\r\n
0x10000001 | Registry\r\n
0x10000002 | COM\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Authenticator\r\n
0x70000002 | Peer\r\n
0x70000003 | Common\r\n
0x90000001 | Microsoft-Windows-EapHost\r\n
0x90000002 | Application\r\n
0x90000003 | Microsoft-Windows-EapHost/Operational\r\n
0x90000004 | Microsoft-Windows-EapHost/Analytic\r\n
0x90000005 | Microsoft-Windows-EapHost/Debug\r\n
0xb00003fd | Method not registered or method's registry data could not be accessed. Unable to open registry key %1, error code %2\r\n
0xb00003fe | Method not registered or method's registry data could not be accessed. Query registry (%1) failed for method: TypeId=%2, AuthorId=%3, VendorId=%4, VendorType=%5\r\n
0xb00003ff | Method not registered or method's registry data could not be accessed. Validation failed for key (%1), Method Info: Type Id=%2, AuthorId=%3, vendorId=%4, vendorType=%5\r\n
0xb0000411 | Unable to Initialize COM library. An instance of EapHostAuthenticatorInvokeConfigUI() is already running. CoInitializeEx returned S_FALSE.\r\n
0xb0000412 | Unable to Initialize COM library. The wrong concurrency model was specified for EapHostAuthenticatorInvokeConfigUI(). COM Error: RPC_E_CHANGED_MODE.\r\n
0xb0000413 | Unable to Initialize COM library for EapHostAuthenticatorInitialize(). %n Error Description: %1\r\n
0xb0000414 | Invalid eatInnerEapMethodType returned by the EAP method. Attribute has incorrect format (%1)\r\n
0xb0000415 | Method does not support EapMethodAuthenticatorUpdateInnerMethodParams() API, but UpdateInnerMethodParams() called\r\n
0xb0000416 | Client's response: NAK=%1, Accept=%2\r\n
0xb0000417 | No preferred methods list provided by Peer\r\n
0xb0000418 | Session(%1), state(%2), receive packet id(%3), length(%4)\r\n
0xb0000419 | send packet id(%1), length(%2)\r\n
0xb000041a | SoH response found\r\n
0xb000041b | NAP exchange required, get SoH response from network policy server\r\n
0xb000041c | Method does not support stand-alone mode. Skipping EapMethod TypeId=%1, AuthorId=%2\r\n
0xb000041d | Unable to parse malformed EAP packet. ERROR_PPP_INVALID_PACKET returned\r\n
0xb000041e | NAK Response: Method (VenId(%2), VenType(%3), Type(%1))  present\r\n
0xb00007d3 | CoTaskMemAlloc() failed for SoH. SoH not saved.\r\n
0xb00007d4 | Could not initialize COM library in service control manager notification thread\r\n
0xb00007d5 | SoH change failed. EapQec::NotifySoHChange caught exception for %1: 0x%2\r\n
0xb00007d6 | ConfigSchema validation failed. Error  %1\r\n
0xb00007d7 | EapQec Listening thread handle is NULL\r\n
0xb00007d8 | Session(%1, %2) in use\r\n
0xb00007d9 | EAP method does not support %1.\r\n
0xb00007da | XML configuration problem;  Failed to find root element.\r\n
0xb00007db | XML configuration problem;  Invalid parameter passed.\r\n
0xb00007dc | Registry key validation successful\r\n
0xb00007dd | Client not NAP enabled. SoH change failed.\r\n
0xb00007de | No SoH response received for %1\r\n
0xb00007df | Notify SoH change succeeded.\r\n
0xb00007e0 | Notify SoH change failed with interface: %1.\r\n
0xb00007e1 | Session(%1): Received EAP-Failure after Identity exchange:  There is likely a problem with the authenticating user's account.\r\n
0xb00007e2 | Session(%1): Received EAP-Failure after EAP-Nak negotiation:  The client & server are not configured to support the same EAP methods. (Server offered EAP type %2; Client sent a Nak, and requested EAP type %3.)\r\n
0xb00007e3 | Method does not implement %1\r\n
0xb00007e4 | COM API %1 Failed.%n Error Description : %2\r\n
0xb00007e5 | Eap Host event log could not be opened. RegisterEventSource failed.%n Error Description : %1\r\n
0xb00007e6 | _beginthreadex failed.%n Error Description : %1\r\n
0xb00007e7 | Invalid XML document. Failed to selectSingleNode.%n Error Description : %1\r\n
0xb00007e8 | Unable to open %1 handle.%n Error Description : %2\r\n
0xb0000bcd | EAP methods not registered or registry data could not be accessed; Failed to open registry %1, Error Code: %2\r\n
0xb0000bce | EAP methods not registered or registry data could not be accessed; Failed to open method registry %2\\%1. Skip this type ID\r\n
0xb0000bcf | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1. Skip this author ID\r\n
0xb0000bd0 | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1\\254\\%2\\%3. Skip this vendor type\r\n
0xb0000bd1 | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1\\254\\%2. Skip this vendor ID\r\n
0xb0000bd2 | Skipping: Unable to add EAP method. Friendly name not present. TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0xb0000bd3 | XML configuration problem; Failed to get EapMethodType node %n. Error Description: %1\r\n
0xb0000bd4 | XML configuration problem; Data Type mismatch for %1\r\n
0xb0000bd5 | XML configuration problem; Bad method: TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0xb0000be1 | Could not load method. Out of memory\r\n
0xb0000be2 | Unable to add new method after re-initialization\r\n
0xb0000be3 | EAP Exception caught: authorId(%1), type(%2), vendorId(%3), vendorType(%4), error(%5)\r\n
0xb0000be4 | Exception caught: authorId(%1), type(%2), vendorId(%3), vendorType(%4), error(%5)\r\n
0xb0000be5 | Error %1, reading EAP method friendly name(muiRead). Friendly name retrieved from registry\r\n
0xb0000be6 | EAP method not found, re-initializing the library manager's EapMethodList data\r\n
0xb0000be7 | New method found after re-initializing EapMethodList data\r\n
0xb0000be8 | New EAP method added to EapMethodList: TypeId=%1, AuthorId=%2, VendorId=%3, VendorType=%4\r\n
0xb0000fa1 | %1\r\n
0xb0000fa2 | %1\r\n

### 6.2.9200.16384

Message identifier | Message string
--- | ---
0x000003e9 | Method not registered or method's registry data could not be accessed. LoadConfig: FriendlyName, ConfigCLSID both are empty\r\n
0x000003ea | Unable to parse malformed EAP packet\r\n
0x000003eb | Method not registered or registry value error: Function Name=LoadConfig, ArgumentName=%1\r\n
0x000003ec | Negotiation failed. No available EAP methods\r\n
0x000003ed | Negotiation failed. Proposed methods list from peer is invalid\r\n
0x000003ee | Negotiation failed. Requested EAP methods not available\r\n
0x000003ef | Exceeded the maximum number(32) of Third Party EapHost processes. Discarding the current eap session.\r\n
0x000007d1 | Eap method friendly name can not be verified or %1 path could not be accessed; Error: type(%2), authId(%3), vendorId(%4), vendorType(%5)\r\n
0x000007d2 | Skipping: %1 validation failed. Error: typeId=%2, authorId=%3, vendorId=%4, vendorType=%5\r\n
0x000007e9 | Exceeded the maximum number(32) of Third Party EapHost processes. Running the current eap session in short lived Eap3Host process.\r\n
0x00000bb9 | EAPHost failed to load. LoadLibraryW(%1) failed %2\r\n
0x00000bba | Could not find the requested EapMethod: TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0x10000001 | Registry\r\n
0x10000002 | COM\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Authenticator\r\n
0x70000002 | Peer\r\n
0x70000003 | Common\r\n
0x90000001 | Microsoft-Windows-EapHost\r\n
0x90000002 | Application\r\n
0x90000003 | Microsoft-Windows-EapHost/Operational\r\n
0x90000004 | Microsoft-Windows-EapHost/Analytic\r\n
0x90000005 | Microsoft-Windows-EapHost/Debug\r\n
0xb00003fd | Method not registered or method's registry data could not be accessed. Unable to open registry key %1, error code %2\r\n
0xb00003fe | Method not registered or method's registry data could not be accessed. Query registry (%1) failed for method: TypeId=%2, AuthorId=%3, VendorId=%4, VendorType=%5\r\n
0xb00003ff | Method not registered or method's registry data could not be accessed. Validation failed for key (%1), Method Info: Type Id=%2, AuthorId=%3, vendorId=%4, vendorType=%5\r\n
0xb0000411 | Unable to Initialize COM library. An instance of EapHostAuthenticatorInvokeConfigUI() is already running. CoInitializeEx returned S_FALSE.\r\n
0xb0000412 | Unable to Initialize COM library. The wrong concurrency model was specified for EapHostAuthenticatorInvokeConfigUI(). COM Error: RPC_E_CHANGED_MODE.\r\n
0xb0000413 | Unable to Initialize COM library for EapHostAuthenticatorInitialize(). %n Error Description: %1\r\n
0xb0000414 | Invalid eatInnerEapMethodType returned by the EAP method. Attribute has incorrect format (%1)\r\n
0xb0000415 | Method does not support EapMethodAuthenticatorUpdateInnerMethodParams() API, but UpdateInnerMethodParams() called\r\n
0xb0000416 | Client's response: NAK=%1, Accept=%2\r\n
0xb0000417 | No preferred methods list provided by Peer\r\n
0xb0000418 | Session(%1), state(%2), receive packet id(%3), length(%4)\r\n
0xb0000419 | send packet id(%1), length(%2)\r\n
0xb000041a | SoH response found\r\n
0xb000041b | NAP exchange required, get SoH response from network policy server\r\n
0xb000041c | Method does not support stand-alone mode. Skipping EapMethod TypeId=%1, AuthorId=%2\r\n
0xb000041d | Unable to parse malformed EAP packet. ERROR_PPP_INVALID_PACKET returned\r\n
0xb000041e | NAK Response: Method (VenId(%2), VenType(%3), Type(%1))  present\r\n
0xb000041f | Performance\r\n
0xb00007d3 | CoTaskMemAlloc() failed for SoH. SoH not saved.\r\n
0xb00007d4 | Could not initialize COM library in service control manager notification thread\r\n
0xb00007d5 | SoH change failed. EapQec::NotifySoHChange caught exception for %1: 0x%2\r\n
0xb00007d6 | ConfigSchema validation failed. Error  %1\r\n
0xb00007d7 | EapQec Listening thread handle is NULL\r\n
0xb00007d8 | Session(%1, %2) in use\r\n
0xb00007d9 | EAP method does not support %1.\r\n
0xb00007da | XML configuration problem;  Failed to find root element.\r\n
0xb00007db | XML configuration problem;  Invalid parameter passed.\r\n
0xb00007dc | Registry key validation successful\r\n
0xb00007dd | Client not NAP enabled. SoH change failed.\r\n
0xb00007de | No SoH response received for %1\r\n
0xb00007df | Notify SoH change succeeded.\r\n
0xb00007e0 | Notify SoH change failed with interface: %1.\r\n
0xb00007e1 | Session(%1): Received EAP-Failure after Identity exchange:  There is likely a problem with the authenticating user's account.\r\n
0xb00007e2 | Session(%1): Received EAP-Failure after EAP-Nak negotiation:  The client & server are not configured to support the same EAP methods. (Server offered EAP type %2; Client sent a Nak, and requested EAP type %3.)\r\n
0xb00007e3 | Method does not implement %1\r\n
0xb00007e4 | COM API %1 Failed.%n Error Description : %2\r\n
0xb00007e6 | _beginthreadex failed.%n Error Description : %1\r\n
0xb00007e7 | Invalid XML document. Failed to selectSingleNode.%n Error Description : %1\r\n
0xb00007e8 | Unable to open %1 handle.%n Error Description : %2\r\n
0xb0000bcd | EAP methods not registered or registry data could not be accessed; Failed to open registry %1, Error Code: %2\r\n
0xb0000bce | EAP methods not registered or registry data could not be accessed; Failed to open method registry %2\\%1. Skip this type ID\r\n
0xb0000bcf | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1. Skip this author ID\r\n
0xb0000bd0 | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1\\254\\%2\\%3. Skip this vendor type\r\n
0xb0000bd1 | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1\\254\\%2. Skip this vendor ID\r\n
0xb0000bd2 | Skipping: Unable to add EAP method. Friendly name not present. TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0xb0000bd3 | XML configuration problem; Failed to get EapMethodType node %n. Error Description: %1\r\n
0xb0000bd4 | XML configuration problem; Data Type mismatch for %1\r\n
0xb0000bd5 | XML configuration problem; Bad method: TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0xb0000be1 | Could not load method. Out of memory\r\n
0xb0000be2 | Unable to add new method after re-initialization\r\n
0xb0000be3 | EAP Exception caught: authorId(%1), type(%2), vendorId(%3), vendorType(%4), error(%5)\r\n
0xb0000be4 | Exception caught: authorId(%1), type(%2), vendorId(%3), vendorType(%4), error(%5)\r\n
0xb0000be5 | Error %1, reading EAP method friendly name(muiRead). Friendly name retrieved from registry\r\n
0xb0000be6 | EAP method not found, re-initializing the library manager's EapMethodList data\r\n
0xb0000be7 | New method found after re-initializing EapMethodList data\r\n
0xb0000be8 | New EAP method added to EapMethodList: TypeId=%1, AuthorId=%2, VendorId=%3, VendorType=%4\r\n
0xb0000fa1 | %1\r\n
0xb0000fa2 | %1\r\n

### 6.3.9600.16384

Message identifier | Message string
--- | ---
0x000003e9 | Method not registered or method's registry data could not be accessed. LoadConfig: FriendlyName, ConfigCLSID both are empty\r\n
0x000003ea | Unable to parse malformed EAP packet\r\n
0x000003eb | Method not registered or registry value error: Function Name=LoadConfig, ArgumentName=%1\r\n
0x000003ec | Negotiation failed. No available EAP methods\r\n
0x000003ed | Negotiation failed. Proposed methods list from peer is invalid\r\n
0x000003ee | Negotiation failed. Requested EAP methods not available\r\n
0x000003ef | Exceeded the maximum number(32) of Third Party EapHost processes. Discarding the current eap session.\r\n
0x000007d1 | Eap method friendly name can not be verified or %1 path could not be accessed; Error: type(%2), authId(%3), vendorId(%4), vendorType(%5)\r\n
0x000007d2 | Skipping: %1 validation failed. Error: typeId=%2, authorId=%3, vendorId=%4, vendorType=%5\r\n
0x000007e9 | Exceeded the maximum number(32) of Third Party EapHost processes. Running the current eap session in short lived Eap3Host process.\r\n
0x00000bb9 | EAPHost failed to load. LoadLibraryW(%1) failed %2\r\n
0x00000bba | Could not find the requested EapMethod: TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0x10000001 | Registry\r\n
0x10000002 | COM\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Authenticator\r\n
0x70000002 | Peer\r\n
0x70000003 | Common\r\n
0x90000001 | Microsoft-Windows-EapHost\r\n
0x90000002 | Application\r\n
0x90000003 | Microsoft-Windows-EapHost/Operational\r\n
0x90000004 | Microsoft-Windows-EapHost/Analytic\r\n
0x90000005 | Microsoft-Windows-EapHost/Debug\r\n
0xb00003fd | Method not registered or method's registry data could not be accessed. Unable to open registry key %1, error code %2\r\n
0xb00003fe | Method not registered or method's registry data could not be accessed. Query registry (%1) failed for method: TypeId=%2, AuthorId=%3, VendorId=%4, VendorType=%5\r\n
0xb00003ff | Method not registered or method's registry data could not be accessed. Validation failed for key (%1), Method Info: Type Id=%2, AuthorId=%3, vendorId=%4, vendorType=%5\r\n
0xb0000411 | Unable to Initialize COM library. An instance of EapHostAuthenticatorInvokeConfigUI() is already running. CoInitializeEx returned S_FALSE.\r\n
0xb0000412 | Unable to Initialize COM library. The wrong concurrency model was specified for EapHostAuthenticatorInvokeConfigUI(). COM Error: RPC_E_CHANGED_MODE.\r\n
0xb0000413 | Unable to Initialize COM library for EapHostAuthenticatorInitialize(). %n Error Description: %1\r\n
0xb0000414 | Invalid eatInnerEapMethodType returned by the EAP method. Attribute has incorrect format (%1)\r\n
0xb0000415 | Method does not support EapMethodAuthenticatorUpdateInnerMethodParams() API, but UpdateInnerMethodParams() called\r\n
0xb0000416 | Client's response: NAK=%1, Accept=%2\r\n
0xb0000417 | No preferred methods list provided by Peer\r\n
0xb0000418 | Session(%1), state(%2), receive packet id(%3), length(%4)\r\n
0xb0000419 | send packet id(%1), length(%2)\r\n
0xb000041a | SoH response found\r\n
0xb000041b | NAP exchange required, get SoH response from network policy server\r\n
0xb000041c | Method does not support stand-alone mode. Skipping EapMethod TypeId=%1, AuthorId=%2\r\n
0xb000041d | Unable to parse malformed EAP packet. ERROR_PPP_INVALID_PACKET returned\r\n
0xb000041e | NAK Response: Method (VenId(%2), VenType(%3), Type(%1))  present\r\n
0xb000041f | Performance\r\n
0xb00007d3 | CoTaskMemAlloc() failed for SoH. SoH not saved.\r\n
0xb00007d4 | Could not initialize COM library in service control manager notification thread\r\n
0xb00007d5 | SoH change failed. EapQec::NotifySoHChange caught exception for %1: 0x%2\r\n
0xb00007d6 | ConfigSchema validation failed. Error  %1\r\n
0xb00007d7 | EapQec Listening thread handle is NULL\r\n
0xb00007d8 | Session(%1, %2) in use\r\n
0xb00007d9 | EAP method does not support %1.\r\n
0xb00007da | XML configuration problem;  Failed to find root element.\r\n
0xb00007db | XML configuration problem;  Invalid parameter passed.\r\n
0xb00007dc | Registry key validation successful\r\n
0xb00007dd | Client not NAP enabled. SoH change failed.\r\n
0xb00007de | No SoH response received for %1\r\n
0xb00007df | Notify SoH change succeeded.\r\n
0xb00007e0 | Notify SoH change failed with interface: %1.\r\n
0xb00007e1 | Session(%1): Received EAP-Failure after Identity exchange:  There is likely a problem with the authenticating user's account.\r\n
0xb00007e2 | Session(%1): Received EAP-Failure after EAP-Nak negotiation:  The client & server are not configured to support the same EAP methods. (Server offered EAP type %2; Client sent a Nak, and requested EAP type %3.)\r\n
0xb00007e3 | Method does not implement %1\r\n
0xb00007e4 | COM API %1 Failed.%n Error Description : %2\r\n
0xb00007e6 | _beginthreadex failed.%n Error Description : %1\r\n
0xb00007e7 | Invalid XML document. Failed to selectSingleNode.%n Error Description : %1\r\n
0xb00007e8 | Unable to open %1 handle.%n Error Description : %2\r\n
0xb0000826 | EapHostPeerGetResult returned a failure.%nEap Method Friendly Name: %2%nReason code: %1%nRoot Cause String: %3%nRepair String: %4\r\n
0xb0000bcd | EAP methods not registered or registry data could not be accessed; Failed to open registry %1, Error Code: %2\r\n
0xb0000bce | EAP methods not registered or registry data could not be accessed; Failed to open method registry %2\\%1. Skip this type ID\r\n
0xb0000bcf | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1. Skip this author ID\r\n
0xb0000bd0 | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1\\254\\%2\\%3. Skip this vendor type\r\n
0xb0000bd1 | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1\\254\\%2. Skip this vendor ID\r\n
0xb0000bd2 | Skipping: Unable to add EAP method. Friendly name not present. TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0xb0000bd3 | XML configuration problem; Failed to get EapMethodType node %n. Error Description: %1\r\n
0xb0000bd4 | XML configuration problem; Data Type mismatch for %1\r\n
0xb0000bd5 | XML configuration problem; Bad method: TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0xb0000be1 | Could not load method. Out of memory\r\n
0xb0000be2 | Unable to add new method after re-initialization\r\n
0xb0000be3 | EAP Exception caught: authorId(%1), type(%2), vendorId(%3), vendorType(%4), error(%5)\r\n
0xb0000be4 | Exception caught: authorId(%1), type(%2), vendorId(%3), vendorType(%4), error(%5)\r\n
0xb0000be5 | Error %1, reading EAP method friendly name(muiRead). Friendly name retrieved from registry\r\n
0xb0000be6 | EAP method not found, re-initializing the library manager's EapMethodList data\r\n
0xb0000be7 | New method found after re-initializing EapMethodList data\r\n
0xb0000be8 | New EAP method added to EapMethodList: TypeId=%1, AuthorId=%2, VendorId=%3, VendorType=%4\r\n
0xb0000fa1 | %1\r\n
0xb0000fa2 | %1\r\n

### 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.18362.959, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x000003e9 | Method not registered or method's registry data could not be accessed. LoadConfig: FriendlyName, ConfigCLSID both are empty\r\n
0x000003ea | Unable to parse malformed EAP packet\r\n
0x000003eb | Method not registered or registry value error: Function Name=LoadConfig, ArgumentName=%1\r\n
0x000003ec | Negotiation failed. No available EAP methods\r\n
0x000003ed | Negotiation failed. Proposed methods list from peer is invalid\r\n
0x000003ee | Negotiation failed. Requested EAP methods not available\r\n
0x000003ef | Exceeded the maximum number(32) of Third Party EapHost processes. Discarding the current eap session.\r\n
0x000007d1 | Eap method friendly name can not be verified or %1 path could not be accessed; Error: type(%2), authId(%3), vendorId(%4), vendorType(%5)\r\n
0x000007d2 | Skipping: %1 validation failed. Error: typeId=%2, authorId=%3, vendorId=%4, vendorType=%5\r\n
0x000007e9 | Exceeded the maximum number(32) of Third Party EapHost processes. Running the current eap session in short lived Eap3Host process.\r\n
0x00000bb9 | EAPHost failed to load. LoadLibraryW(%1) failed %2\r\n
0x00000bba | Could not find the requested EapMethod: TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0x10000001 | Registry\r\n
0x10000002 | COM\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x70000001 | Authenticator\r\n
0x70000002 | Peer\r\n
0x70000003 | Common\r\n
0x90000001 | Microsoft-Windows-EapHost\r\n
0x90000002 | Application\r\n
0x90000003 | Microsoft-Windows-EapHost/Operational\r\n
0x90000004 | Microsoft-Windows-EapHost/Analytic\r\n
0x90000005 | Microsoft-Windows-EapHost/Debug\r\n
0xb00003fd | Method not registered or method's registry data could not be accessed. Unable to open registry key %1, error code %2\r\n
0xb00003fe | Method not registered or method's registry data could not be accessed. Query registry (%1) failed for method: TypeId=%2, AuthorId=%3, VendorId=%4, VendorType=%5\r\n
0xb00003ff | Method not registered or method's registry data could not be accessed. Validation failed for key (%1), Method Info: Type Id=%2, AuthorId=%3, vendorId=%4, vendorType=%5\r\n
0xb0000411 | Unable to Initialize COM library. An instance of EapHostAuthenticatorInvokeConfigUI() is already running. CoInitializeEx returned S_FALSE.\r\n
0xb0000412 | Unable to Initialize COM library. The wrong concurrency model was specified for EapHostAuthenticatorInvokeConfigUI(). COM Error: RPC_E_CHANGED_MODE.\r\n
0xb0000413 | Unable to Initialize COM library for EapHostAuthenticatorInitialize(). %n Error Description: %1\r\n
0xb0000414 | Invalid eatInnerEapMethodType returned by the EAP method. Attribute has incorrect format (%1)\r\n
0xb0000415 | Method does not support EapMethodAuthenticatorUpdateInnerMethodParams() API, but UpdateInnerMethodParams() called\r\n
0xb0000416 | Client's response: NAK=%1, Accept=%2\r\n
0xb0000417 | No preferred methods list provided by Peer\r\n
0xb0000418 | Session(%1), state(%2), receive packet id(%3), length(%4)\r\n
0xb0000419 | send packet id(%1), length(%2)\r\n
0xb000041a | SoH response found\r\n
0xb000041b | NAP exchange required, get SoH response from network policy server\r\n
0xb000041c | Method does not support stand-alone mode. Skipping EapMethod TypeId=%1, AuthorId=%2\r\n
0xb000041d | Unable to parse malformed EAP packet. ERROR_PPP_INVALID_PACKET returned\r\n
0xb000041e | NAK Response: Method (VenId(%2), VenType(%3), Type(%1))  present\r\n
0xb000041f | Performance\r\n
0xb00007d3 | CoTaskMemAlloc() failed for SoH. SoH not saved.\r\n
0xb00007d4 | Could not initialize COM library in service control manager notification thread\r\n
0xb00007d5 | SoH change failed. EapQec::NotifySoHChange caught exception for %1: 0x%2\r\n
0xb00007d6 | ConfigSchema validation failed. Error  %1\r\n
0xb00007d7 | EapQec Listening thread handle is NULL\r\n
0xb00007d8 | Session(%1, %2) in use\r\n
0xb00007d9 | EAP method does not support %1.\r\n
0xb00007da | XML configuration problem;  Failed to find root element.\r\n
0xb00007db | XML configuration problem;  Invalid parameter passed.\r\n
0xb00007dc | Registry key validation successful.\r\n
0xb00007dd | Client not NAP enabled. SoH change failed.\r\n
0xb00007de | No SoH response received for %1\r\n
0xb00007df | Notify SoH change succeeded.\r\n
0xb00007e0 | Notify SoH change failed with interface: %1.\r\n
0xb00007e1 | Session(%1): Received EAP-Failure after Identity exchange:  There is likely a problem with the authenticating user's account.\r\n
0xb00007e2 | Session(%1): Received EAP-Failure after EAP-Nak negotiation:  The client & server are not configured to support the same EAP methods. (Server offered EAP type %2; Client sent a Nak, and requested EAP type %3.)\r\n
0xb00007e3 | Method does not implement %1\r\n
0xb00007e4 | COM API %1 Failed.%n Error Description : %2\r\n
0xb00007e6 | _beginthreadex failed.%n Error Description : %1\r\n
0xb00007e7 | Invalid XML document. Failed to selectSingleNode.%n Error Description : %1\r\n
0xb00007e8 | Unable to open %1 handle.%n Error Description : %2\r\n
0xb0000826 | EapHostPeerGetResult returned a failure.%nEap Method Friendly Name: %2%nReason code: %1%nRoot Cause String: %3%nRepair String: %4\r\n
0xb0000827 | User Entered Credentials.\r\n
0xb0000828 | User Uses Saved Credentials.\r\n
0xb0000829 | EAP session is completing during the authentication phase.\r\n
0xb0000bcd | EAP methods not registered or registry data could not be accessed; Failed to open registry %1, Error Code: %2\r\n
0xb0000bce | EAP methods not registered or registry data could not be accessed; Failed to open method registry %2\\%1. Skip this type ID\r\n
0xb0000bcf | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1. Skip this author ID\r\n
0xb0000bd0 | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1\\254\\%2\\%3. Skip this vendor type\r\n
0xb0000bd1 | EAP methods not registered or registry data could not be accessed; Failed to open method registry %1\\254\\%2. Skip this vendor ID\r\n
0xb0000bd2 | Skipping: Unable to add EAP method. Friendly name not present. TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0xb0000bd3 | XML configuration problem; Failed to get EapMethodType node %n. Error Description: %1\r\n
0xb0000bd4 | XML configuration problem; Data Type mismatch for %1\r\n
0xb0000bd5 | XML configuration problem; Bad method: TypeId(%1), AuthorId(%2), VendorId(%3), VendorType(%4)\r\n
0xb0000be1 | Could not load method. Out of memory\r\n
0xb0000be2 | Unable to add new method after re-initialization\r\n
0xb0000be3 | EAP Exception caught: authorId(%1), type(%2), vendorId(%3), vendorType(%4), error(%5)\r\n
0xb0000be4 | Exception caught: authorId(%1), type(%2), vendorId(%3), vendorType(%4), error(%5)\r\n
0xb0000be5 | Error %1, reading EAP method friendly name(muiRead). Friendly name retrieved from registry\r\n
0xb0000be6 | EAP method not found, re-initializing the library manager's EapMethodList data\r\n
0xb0000be7 | New method found after re-initializing EapMethodList data\r\n
0xb0000be8 | New EAP method added to EapMethodList: TypeId=%1, AuthorId=%2, VendorId=%3, VendorType=%4\r\n
0xb0000fa1 | %1\r\n
0xb0000fa2 | %1\r\n
