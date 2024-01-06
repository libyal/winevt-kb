## webauthn.dll

Path: %SystemRoot%\System32\webauthn.dll

### 10.0.16299.15

Message identifier | Message string
--- | ---
0x10000001 | WebAuthN\r\n
0x10000002 | Ctap\r\n
0x10000003 | Cbor\r\n
0x10000004 | Usb\r\n
0x10000005 | Nfc\r\n
0x10000006 | Test\r\n
0x10000007 | Ngc\r\n
0x3000000a | Start\r\n
0x3000000b | Stop\r\n
0x3000000c | Informational\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x50000010 | Success\r\n
0x70000001 | WebAuthN Ctap MakeCredential\r\n
0x70000002 | WebAuthN Ctap GetAssertion\r\n
0x70000003 | WebAuthN Ctap SendCommand\r\n
0x70000004 | WebAuthN Error\r\n
0x7000000a | WebAuthN Ngc MakeCredential\r\n
0x7000000b | WebAuthN Ngc GetAssertion\r\n
0x7000000c | Ngc MakeCredential Request\r\n
0x7000000d | Ngc MakeCredential Response\r\n
0x7000000e | Ngc GetAssertion Request\r\n
0x7000000f | Ngc GetAssertion Response\r\n
0x70000064 | Cbor Decode Error\r\n
0x70000065 | Cbor Encode MakeCredential Request\r\n
0x70000066 | Cbor Decode MakeCredential Response\r\n
0x70000067 | Cbor Encode GetAssertion Request\r\n
0x70000068 | Cbor Decode GetAssertion Response\r\n
0x700001f4 | Ctap Service\r\n
0x700001f5 | Ctap Command\r\n
0x700001f6 | Ctap Device Info\r\n
0x700001fe | Ctap Usb Provider Thread\r\n
0x700001ff | Ctap Usb Device Thread\r\n
0x70000200 | Ctap Usb Add\r\n
0x70000201 | Ctap Usb Remove\r\n
0x70000202 | Ctap Usb Changes\r\n
0x70000203 | Ctap Usb Switch To U2F\r\n
0x70000204 | Ctap Usb Connect\r\n
0x70000205 | Ctap Usb Send Receive\r\n
0x70000226 | Ctap Nfc Provider Thread\r\n
0x70000227 | Ctap Nfc Reader Thread\r\n
0x70000228 | Ctap Nfc Add Reader\r\n
0x70000229 | Ctap Nfc Skip Reader\r\n
0x7000022a | Ctap Nfc Transition Reader\r\n
0x7000022b | Ctap Nfc Send Message\r\n
0x7000022c | Ctap Nfc Send Request\r\n
0x7000022d | Ctap Nfc Switch To U2F\r\n
0x7000022e | Ctap Nfc SCardTransmit Request\r\n
0x700002bc | Ctap Test Provider Thread\r\n
0x90000001 | Microsoft-Windows-WebAuthN\r\n
0xb00003e8 | WebAuthN Ctap MakeCredential started.%n%nTransactionId: %1\r\n
0xb00003e9 | WebAuthN Ctap MakeCredential completed.%n%nTransactionId: %1\r\n
0xb00003ea | WebAuthN Ctap MakeCredential completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003eb | WebAuthN Ctap GetAssertion started.%n%nTransactionId: %1\r\n
0xb00003ec | WebAuthN Ctap GetAssertion completed.%n%nTransactionId: %1\r\n
0xb00003ed | WebAuthN Ctap GetAssertion completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003ee | WebAuthN Ctap SendCommand started.%n%nTransactionId: %1%nTicket: %3\r\n
0xb00003ef | WebAuthN Ctap SendCommand completed.%n%nTransactionId: %1\r\n
0xb00003f0 | WebAuthN Ctap SendCommand completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003fc | WebAuthN Ngc MakeCredential started.%n%nTransactionId: %1\r\n
0xb00003fd | WebAuthN Ngc MakeCredential completed.%n%nTransactionId: %1\r\n
0xb00003fe | WebAuthN Ngc MakeCredential completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003ff | WebAuthN Ngc GetAssertion started.%n%nTransactionId: %1\r\n
0xb0000400 | WebAuthN Ngc GetAssertion completed.%n%nTransactionId: %1\r\n
0xb0000401 | WebAuthN Ngc GetAssertion completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb0000410 | Ngc MakeCredential request.%n%nTransactionId: %1%nRpId: %2%nAccountId: %3%nClientDataHashAlgId: %4 ClientDataLength: %5 ClientDataHash: %7%nExcludeCredentialCount: %8%nCredentialParameterCount: %9\r\n
0xb0000411 | Ngc MakeCredential response.%n%nTransactionId: %1%nAttestationFormatType: %2%nRpIdHash: %4%nFlags: %5%nSignCount: %6%nAAGuid: %7%nCredentialId: %9%nU2fPublicKey: %10%nPublicKey: %12%nResponse: %14\r\n
0xb0000412 | Ngc GetAssertion request.%n%nTransactionId: %1%nRpId: %2%nClientDataHashAlgId: %3 ClientDataLength: %4 ClientDataHash: %6%nAllowCredentialCount: %7\r\n
0xb0000413 | Ngc GetAssertion response.%n%nTransactionId: %1%nRpIdHash: %3%nFlags: %4%nSignCount: %5%nCredentialId: %7%\r\n
0xb0000424 | WebAuthN error at: %2%n%nTransactionId: %1%nError: %3. %4\r\n
0xb000044c | Cbor decode error.%n%nTransactionId: %1%nFunction: %2%nCborError: %3 %4%nErrorOffset: %5 LineNumber: %6%nEncoded: %8\r\n
0xb000044d | Cbor encode MakeCredential request.%n%nTransactionId: %1%nRpId: %2%nAccountId: %3%nClientDataHashAlgId: %4 ClientDataLength: %5 ClientDataHash: %7%nRequireResidentKey: %8%nExcludeCredentialCount: %9%nCredentialParameterCount: %10%nRequest: %12\r\n
0xb000044e | Cbor decode MakeCredential response.%n%nTransactionId: %1%nAttestationFormatType: %2%nRpIdHash: %4%nFlags: %5%nSignCount: %6%nAAGuid: %7%nCredentialId: %9%nU2fPublicKey: %10%nPublicKey: %12%nResponse: %14\r\n
0xb000044f | Cbor encode GetAssertion request.%n%nTransactionId: %1%nRpId: %2%nClientDataHashAlgId: %3 ClientDataLength: %4 ClientDataHash: %6%nAllowCredentialCount: %7%nRequest: %9\r\n
0xb0000450 | Cbor decode GetAssertion response.%n%nTransactionId: %1%nRpIdHash: %3%nFlags: %4%nSignCount: %5%nCredentialId: %7%nResponse: %9\r\n
0xb00007d0 | Ctap service started successfully.\r\n
0xb00007d1 | Ctap service stopped successfully.\r\n
0xb0000834 | Ctap %1 started.%n%nTransactionId: %2%nFlags: %3%nTimeoutMilliseconds: %4%nTicket: %6%nRequest: %8\r\n
0xb0000835 | Ctap command started.%n%nRequest: %2\r\n
0xb0000836 | Ctap %1 completed.%n%nTransactionId: %2%nResponse: %4\r\n
0xb0000837 | Ctap %1 completed.%n%nTransactionId: %2%nError: %3. %4\r\n
0xb0000838 | Ctap device info.%n%nTransactionId: %1%nProviderName: %2%nDevicePath: %3%nManufacturer: %4%nProduct: %5%nAAGuid: %6%nU2fProtocol: %7\r\n
0xb0000898 | Ctap Usb provider thread started.%n%nTransactionId: %1\r\n
0xb0000899 | Ctap Usb provider thread completed.%n%nTransactionId: %1\r\n
0xb000089a | Ctap Usb provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00008a2 | Ctap Usb device thread started.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008a3 | Ctap Usb device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nAAGuid: %5%nU2fProtocol: %6\r\n
0xb00008a4 | Ctap Usb device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nAAGuid: %5%nU2fProtocol: %6%nState: %7%nStatus: %8%nError: %9. %10\r\n
0xb00008ac | Ctap Usb add device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008ad | Ctap Usb remove device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008ae | Ctap Usb device changes.%n%nTransactionId: %1\r\n
0xb00008af | Ctap Usb U2F device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008b0 | Ctap Usb connect to device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nDeviceErr: %5%nStatus: %6%nError: %7. %8\r\n
0xb00008b1 | Ctap Usb Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7\r\n
0xb00008b2 | Ctap Usb Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7%nError: %8. %9\r\n
0xb00008fc | Ctap Nfc provider thread started.%n%nTransactionId: %1\r\n
0xb00008fd | Ctap Nfc provider thread completed.%n%nTransactionId: %1\r\n
0xb00008fe | Ctap Nfc provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb0000906 | Ctap Nfc reader thread started.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000907 | Ctap Nfc reader thread completed.%n%nTransactionId: %1%nReader: %2%nAAGuid: %3%nU2fProtocol: %4\r\n
0xb0000908 | Ctap Nfc reader thread completed.%n%nTransactionId: %1%nReader: %2%nAAGuid: %3%nU2fProtocol: %4%nState: %5%nStatus: %6%nError: %7. %8\r\n
0xb0000910 | Ctap Nfc add reader.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000911 | Ctap Nfc skip reader for: %2.%n%nTransactionId: %1%nReader: %3%nDeviceInstanceId: %4\r\n
0xb0000912 | Ctap Nfc transition reader for: %2.%n%nTransactionId: %1%nReader: %3\r\n
0xb0000913 | Ctap Nfc send message warning for: %2.%n%nTransactionId: %1%nReader: %3%nApduStatus: %4%nDeviceStatus: %5%nSmartCardError: %6. %7\r\n
0xb0000914 | Ctap Nfc send request error for: %2.%n%nTransactionId: %1%nReader: %3%nApduStatus: %4%nDeviceStatus: %5%nError: %6. %7\r\n
0xb0000915 | Ctap Nfc U2F device.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000916 | Ctap Nfc send message at: %2.%n%nTransactionId: %1%nReader: %3\r\n
0xb0000917 | Ctap Nfc SCardTransmit Request:%n%nTransactionId: %1%nReader: %2%n%nRequest: %3 bytes%n%4%n%nResponse data: %5 bytes%n%6%n%nApdu Status: %7%n\r\n
0xb0000918 | Ctap Nfc SCardTransmit Request:%n%nTransactionId: %1%nReader: %2%n%nRequest: %3 bytes%n%4%n%nResponse data: %5 bytes%n%6%n%nApdu Status: %7%n%nError: %8. %9\r\n
0xb0000960 | Ctap Test provider thread started.%n%nTransactionId: %1\r\n
0xb0000961 | Ctap Test provider thread completed.%n%nTransactionId: %1\r\n
0xb0000962 | Ctap Test provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n

### 10.0.17134.1

Message identifier | Message string
--- | ---
0x10000001 | WebAuthN\r\n
0x10000002 | Ctap\r\n
0x10000003 | Cbor\r\n
0x10000004 | Usb\r\n
0x10000005 | Nfc\r\n
0x10000006 | Test\r\n
0x10000007 | Ngc\r\n
0x3000000a | Start\r\n
0x3000000b | Stop\r\n
0x3000000c | Informational\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x50000010 | Success\r\n
0x70000001 | WebAuthN Ctap MakeCredential\r\n
0x70000002 | WebAuthN Ctap GetAssertion\r\n
0x70000003 | WebAuthN Ctap SendCommand\r\n
0x70000004 | WebAuthN Error\r\n
0x7000000a | WebAuthN Ngc MakeCredential\r\n
0x7000000b | WebAuthN Ngc GetAssertion\r\n
0x7000000c | Ngc MakeCredential Request\r\n
0x7000000d | Ngc MakeCredential Response\r\n
0x7000000e | Ngc GetAssertion Request\r\n
0x7000000f | Ngc GetAssertion Response\r\n
0x70000064 | Cbor Decode Error\r\n
0x70000065 | Cbor Encode MakeCredential Request\r\n
0x70000066 | Cbor Decode MakeCredential Response\r\n
0x70000067 | Cbor Encode GetAssertion Request\r\n
0x70000068 | Cbor Decode GetAssertion Response\r\n
0x700000c8 | WNF Ctap Device State Info\r\n
0x700000c9 | WNF Ctap Device Change Notify Info\r\n
0x700001f4 | Ctap Service\r\n
0x700001f5 | Ctap Command\r\n
0x700001f6 | Ctap Device Info\r\n
0x700001fe | Ctap Usb Provider Thread\r\n
0x700001ff | Ctap Usb Device Thread\r\n
0x70000200 | Ctap Usb Add\r\n
0x70000201 | Ctap Usb Remove\r\n
0x70000202 | Ctap Usb Changes\r\n
0x70000203 | Ctap Usb Switch To U2F\r\n
0x70000204 | Ctap Usb Connect\r\n
0x70000205 | Ctap Usb Send Receive\r\n
0x70000226 | Ctap Nfc Provider Thread\r\n
0x70000227 | Ctap Nfc Reader Thread\r\n
0x70000228 | Ctap Nfc Add Reader\r\n
0x70000229 | Ctap Nfc Skip Reader\r\n
0x7000022a | Ctap Nfc Transition Reader\r\n
0x7000022b | Ctap Nfc Send Message\r\n
0x7000022c | Ctap Nfc Send Request\r\n
0x7000022d | Ctap Nfc Switch To U2F\r\n
0x7000022e | Ctap Nfc SCardTransmit Request\r\n
0x7000022f | Ctap Nfc Reader Manager Thread\r\n
0x700002bc | Ctap Test Provider Thread\r\n
0x90000001 | Microsoft-Windows-WebAuthN\r\n
0xb00003e8 | WebAuthN Ctap MakeCredential started.%n%nTransactionId: %1\r\n
0xb00003e9 | WebAuthN Ctap MakeCredential completed.%n%nTransactionId: %1\r\n
0xb00003ea | WebAuthN Ctap MakeCredential completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003eb | WebAuthN Ctap GetAssertion started.%n%nTransactionId: %1\r\n
0xb00003ec | WebAuthN Ctap GetAssertion completed.%n%nTransactionId: %1\r\n
0xb00003ed | WebAuthN Ctap GetAssertion completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003ee | WebAuthN Ctap SendCommand started.%n%nTransactionId: %1%nTicket: %3\r\n
0xb00003ef | WebAuthN Ctap SendCommand completed.%n%nTransactionId: %1\r\n
0xb00003f0 | WebAuthN Ctap SendCommand completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003fc | WebAuthN Ngc MakeCredential started.%n%nTransactionId: %1\r\n
0xb00003fd | WebAuthN Ngc MakeCredential completed.%n%nTransactionId: %1\r\n
0xb00003fe | WebAuthN Ngc MakeCredential completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003ff | WebAuthN Ngc GetAssertion started.%n%nTransactionId: %1\r\n
0xb0000400 | WebAuthN Ngc GetAssertion completed.%n%nTransactionId: %1\r\n
0xb0000401 | WebAuthN Ngc GetAssertion completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb0000410 | Ngc MakeCredential request.%n%nTransactionId: %1%nRpId: %2%nAccountId: %3%nClientDataHashAlgId: %4 ClientDataLength: %5 ClientDataHash: %7%nExcludeCredentialCount: %8%nCredentialParameterCount: %9\r\n
0xb0000411 | Ngc MakeCredential response.%n%nTransactionId: %1%nAttestationFormatType: %2%nRpIdHash: %4%nFlags: %5%nSignCount: %6%nAAGuid: %7%nCredentialId: %9%nU2fPublicKey: %10%nPublicKey: %12%nResponse: %14\r\n
0xb0000412 | Ngc GetAssertion request.%n%nTransactionId: %1%nRpId: %2%nClientDataHashAlgId: %3 ClientDataLength: %4 ClientDataHash: %6%nAllowCredentialCount: %7\r\n
0xb0000413 | Ngc GetAssertion response.%n%nTransactionId: %1%nRpIdHash: %3%nFlags: %4%nSignCount: %5%nCredentialId: %7%\r\n
0xb0000424 | WebAuthN error at: %2%n%nTransactionId: %1%nError: %3. %4\r\n
0xb000044c | Cbor decode error.%n%nTransactionId: %1%nFunction: %2%nCborError: %3 %4%nErrorOffset: %5 LineNumber: %6%nEncoded: %8\r\n
0xb000044d | Cbor encode MakeCredential request.%n%nTransactionId: %1%nRpId: %2%nUserId: %4%nClientDataHashAlgId: %5 ClientDataLength: %6 ClientDataHash: %8%nRequireResidentKey: %9%nExcludeCredentialCount: %10%nCredentialParameterCount: %11%nRequest: %13\r\n
0xb000044e | Cbor decode MakeCredential response.%n%nTransactionId: %1%nAttestationFormatType: %2%nRpIdHash: %4%nFlags: %5%nSignCount: %6%nAAGuid: %7%nCredentialId: %9%nU2fPublicKey: %10%nPublicKey: %12%nResponse: %14\r\n
0xb000044f | Cbor encode GetAssertion request.%n%nTransactionId: %1%nRpId: %2%nClientDataHashAlgId: %3 ClientDataLength: %4 ClientDataHash: %6%nAllowCredentialCount: %7%nRequest: %9\r\n
0xb0000450 | Cbor decode GetAssertion response.%n%nTransactionId: %1%nRpIdHash: %3%nFlags: %4%nSignCount: %5%nCredentialId: %7%nResponse: %9\r\n
0xb00007d0 | Ctap service started successfully.\r\n
0xb00007d1 | Ctap service stopped successfully.\r\n
0xb0000834 | Ctap %1 started.%n%nTransactionId: %2%nFlags: %3%nTimeoutMilliseconds: %4%nTicket: %6%nRequest: %8\r\n
0xb0000835 | Ctap command started.%n%nRequest: %2\r\n
0xb0000836 | Ctap %1 completed.%n%nTransactionId: %2%nResponse: %4\r\n
0xb0000837 | Ctap %1 completed.%n%nTransactionId: %2%nError: %3. %4\r\n
0xb0000838 | Ctap device info.%n%nTransactionId: %1%nProviderName: %2%nDevicePath: %3%nManufacturer: %4%nProduct: %5%nAAGuid: %6%nU2fProtocol: %7\r\n
0xb000083e | Ctap device device state info.%n%nTransport Type: %1%nWnfState: %2%nError: %3. %4%n\r\n
0xb000083f | Ctap device change notify info.%n%nTransport Type: %1%n\r\n
0xb0000898 | Ctap Usb provider thread started.%n%nTransactionId: %1\r\n
0xb0000899 | Ctap Usb provider thread completed.%n%nTransactionId: %1\r\n
0xb000089a | Ctap Usb provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00008a2 | Ctap Usb device thread started.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008a3 | Ctap Usb device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nAAGuid: %5%nU2fProtocol: %6\r\n
0xb00008a4 | Ctap Usb device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nAAGuid: %5%nU2fProtocol: %6%nState: %7%nStatus: %8%nError: %9. %10\r\n
0xb00008ac | Ctap Usb add device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008ad | Ctap Usb remove device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008ae | Ctap Usb device changes.%n%nTransactionId: %1\r\n
0xb00008af | Ctap Usb U2F device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008b0 | Ctap Usb connect to device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nDeviceErr: %5%nStatus: %6%nError: %7. %8\r\n
0xb00008b1 | Ctap Usb Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7\r\n
0xb00008b2 | Ctap Usb Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7%nError: %8. %9\r\n
0xb00008fc | Ctap Nfc provider thread started.%n%nTransactionId: %1\r\n
0xb00008fd | Ctap Nfc provider thread completed.%n%nTransactionId: %1\r\n
0xb00008fe | Ctap Nfc provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb0000906 | Ctap Nfc reader thread started.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000907 | Ctap Nfc reader thread completed.%n%nTransactionId: %1%nReader: %2%nAAGuid: %3%nU2fProtocol: %4\r\n
0xb0000908 | Ctap Nfc reader thread completed.%n%nTransactionId: %1%nReader: %2%nAAGuid: %3%nU2fProtocol: %4%nState: %5%nStatus: %6%nError: %7. %8\r\n
0xb000090a | Ctap Nfc reader manager thread started.%n%nTransactionId: %1%n\r\n
0xb000090b | Ctap Nfc reader manager thread completed.%n%nTransactionId: %1%nNumberOfTimesScardCancelCommandsSent: %2%n\r\n
0xb000090c | Cancelling Reader Threads.%n%nTransactionId: %1%n\r\n
0xb0000910 | Ctap Nfc add reader.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000911 | Ctap Nfc skip reader for: %2.%n%nTransactionId: %1%nReader: %3%nDeviceInstanceId: %4\r\n
0xb0000912 | Ctap Nfc transition reader for: %2.%n%nTransactionId: %1%nReader: %3\r\n
0xb0000913 | Ctap Nfc send message warning for: %2.%n%nTransactionId: %1%nReader: %3%nApduStatus: %4%nDeviceStatus: %5%nSmartCardError: %6. %7\r\n
0xb0000914 | Ctap Nfc send request error for: %2.%n%nTransactionId: %1%nReader: %3%nApduStatus: %4%nDeviceStatus: %5%nError: %6. %7\r\n
0xb0000915 | Ctap Nfc U2F device.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000916 | Ctap Nfc send message at: %2.%n%nTransactionId: %1%nReader: %3\r\n
0xb0000917 | Ctap Nfc SCardTransmit Request:%n%nTransactionId: %1%nReader: %2%n%nRequest: %3 bytes%n%4%n%nResponse data: %5 bytes%n%6%n%nApdu Status: %7%n\r\n
0xb0000918 | Ctap Nfc SCardTransmit Request:%n%nTransactionId: %1%nReader: %2%n%nRequest: %3 bytes%n%4%n%nResponse data: %5 bytes%n%6%n%nApdu Status: %7%n%nError: %8. %9\r\n
0xb0000960 | Ctap Test provider thread started.%n%nTransactionId: %1\r\n
0xb0000961 | Ctap Test provider thread completed.%n%nTransactionId: %1\r\n
0xb0000962 | Ctap Test provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n

### 10.0.17763.1

Message identifier | Message string
--- | ---
0x10000001 | WebAuthN\r\n
0x10000002 | Ctap\r\n
0x10000003 | Cbor\r\n
0x10000004 | Usb\r\n
0x10000005 | Nfc\r\n
0x10000006 | Test\r\n
0x10000007 | Ngc\r\n
0x10000008 | Ble\r\n
0x3000000a | Start\r\n
0x3000000b | Stop\r\n
0x3000000c | Informational\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x50000010 | Success\r\n
0x70000001 | WebAuthN Ctap MakeCredential\r\n
0x70000002 | WebAuthN Ctap GetAssertion\r\n
0x70000003 | WebAuthN Ctap SendCommand\r\n
0x70000004 | WebAuthN Error\r\n
0x7000000a | WebAuthN Ngc MakeCredential\r\n
0x7000000b | WebAuthN Ngc GetAssertion\r\n
0x7000000c | Ngc MakeCredential Request\r\n
0x7000000d | Ngc MakeCredential Response\r\n
0x7000000e | Ngc GetAssertion Request\r\n
0x7000000f | Ngc GetAssertion Response\r\n
0x70000064 | Cbor Decode Error\r\n
0x70000065 | Cbor Encode MakeCredential Request\r\n
0x70000066 | Cbor Decode MakeCredential Response\r\n
0x70000067 | Cbor Encode GetAssertion Request\r\n
0x70000068 | Cbor Decode GetAssertion Response\r\n
0x700000c8 | WNF Ctap Device State Info\r\n
0x700000c9 | WNF Ctap Device Change Notify Info\r\n
0x700001f4 | Ctap Service\r\n
0x700001f5 | Ctap Command\r\n
0x700001f6 | Ctap Device Info\r\n
0x700001fe | Ctap Usb Provider Thread\r\n
0x700001ff | Ctap Usb Device Thread\r\n
0x70000200 | Ctap Usb Add\r\n
0x70000201 | Ctap Usb Remove\r\n
0x70000202 | Ctap Usb Changes\r\n
0x70000203 | Ctap Usb Switch To U2F\r\n
0x70000204 | Ctap Usb Connect\r\n
0x70000205 | Ctap Usb Send Receive\r\n
0x70000212 | Ctap Ble Provider Thread\r\n
0x70000213 | Ctap Ble Device Thread\r\n
0x70000214 | Ctap Ble Switch To U2F\r\n
0x70000215 | Ctap Ble Function\r\n
0x70000216 | Ctap Ble Send Receive\r\n
0x70000226 | Ctap Nfc Provider Thread\r\n
0x70000227 | Ctap Nfc Reader Thread\r\n
0x70000228 | Ctap Nfc Add Reader\r\n
0x70000229 | Ctap Nfc Skip Reader\r\n
0x7000022a | Ctap Nfc Transition Reader\r\n
0x7000022b | Ctap Nfc Send Message\r\n
0x7000022c | Ctap Nfc Send Request\r\n
0x7000022d | Ctap Nfc Switch To U2F\r\n
0x7000022e | Ctap Nfc SCardTransmit Request\r\n
0x7000022f | Ctap Nfc Reader Manager Thread\r\n
0x700002bc | Ctap Test Provider Thread\r\n
0x90000001 | Microsoft-Windows-WebAuthN\r\n
0xb00003e8 | WebAuthN Ctap MakeCredential started.%n%nTransactionId: %1\r\n
0xb00003e9 | WebAuthN Ctap MakeCredential completed.%n%nTransactionId: %1\r\n
0xb00003ea | WebAuthN Ctap MakeCredential completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003eb | WebAuthN Ctap GetAssertion started.%n%nTransactionId: %1\r\n
0xb00003ec | WebAuthN Ctap GetAssertion completed.%n%nTransactionId: %1\r\n
0xb00003ed | WebAuthN Ctap GetAssertion completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003ee | WebAuthN Ctap SendCommand started.%n%nTransactionId: %1%nTicket: %3\r\n
0xb00003ef | WebAuthN Ctap SendCommand completed.%n%nTransactionId: %1\r\n
0xb00003f0 | WebAuthN Ctap SendCommand completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003fc | WebAuthN Ngc MakeCredential started.%n%nTransactionId: %1\r\n
0xb00003fd | WebAuthN Ngc MakeCredential completed.%n%nTransactionId: %1\r\n
0xb00003fe | WebAuthN Ngc MakeCredential completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003ff | WebAuthN Ngc GetAssertion started.%n%nTransactionId: %1\r\n
0xb0000400 | WebAuthN Ngc GetAssertion completed.%n%nTransactionId: %1\r\n
0xb0000401 | WebAuthN Ngc GetAssertion completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb0000410 | Ngc MakeCredential request.%n%nTransactionId: %1%nRpId: %2%nAccountId: %3%nClientDataHashAlgId: %4 ClientDataLength: %5 ClientDataHash: %7%nExcludeCredentialCount: %8%nCredentialParameterCount: %9\r\n
0xb0000411 | Ngc MakeCredential response.%n%nTransactionId: %1%nAttestationFormatType: %2%nRpIdHash: %4%nFlags: %5%nSignCount: %6%nAAGuid: %7%nCredentialId: %9%nU2fPublicKey: %10%nPublicKey: %12%nResponse: %14\r\n
0xb0000412 | Ngc GetAssertion request.%n%nTransactionId: %1%nRpId: %2%nClientDataHashAlgId: %3 ClientDataLength: %4 ClientDataHash: %6%nAllowCredentialCount: %7\r\n
0xb0000413 | Ngc GetAssertion response.%n%nTransactionId: %1%nRpIdHash: %3%nFlags: %4%nSignCount: %5%nCredentialId: %7%\r\n
0xb0000424 | WebAuthN error at: %2%n%nTransactionId: %1%nError: %3. %4\r\n
0xb000044c | Cbor decode error.%n%nTransactionId: %1%nFunction: %2%nCborError: %3 %4%nErrorOffset: %5 LineNumber: %6%nEncoded: %8\r\n
0xb000044d | Cbor encode MakeCredential request.%n%nTransactionId: %1%nRpId: %2%nUserId: %4%nClientDataHashAlgId: %5 ClientDataLength: %6 ClientDataHash: %8%nRequireResidentKey: %9%nExcludeCredentialCount: %10%nCredentialParameterCount: %11%nRequest: %13\r\n
0xb000044e | Cbor decode MakeCredential response.%n%nTransactionId: %1%nAttestationFormatType: %2%nRpIdHash: %4%nFlags: %5%nSignCount: %6%nAAGuid: %7%nCredentialId: %9%nU2fPublicKey: %10%nPublicKey: %12%nResponse: %14\r\n
0xb000044f | Cbor encode GetAssertion request.%n%nTransactionId: %1%nRpId: %2%nClientDataHashAlgId: %3 ClientDataLength: %4 ClientDataHash: %6%nAllowCredentialCount: %7%nRequest: %9\r\n
0xb0000450 | Cbor decode GetAssertion response.%n%nTransactionId: %1%nRpIdHash: %3%nFlags: %4%nSignCount: %5%nCredentialId: %7%nResponse: %9\r\n
0xb00007d0 | Ctap service started successfully.\r\n
0xb00007d1 | Ctap service stopped successfully.\r\n
0xb0000834 | Ctap %1 started.%n%nTransactionId: %2%nFlags: %3%nTimeoutMilliseconds: %4%nTicket: %6%nRequest: %8\r\n
0xb0000835 | Ctap command started.%n%nRequest: %2\r\n
0xb0000836 | Ctap %1 completed.%n%nTransactionId: %2%nResponse: %4\r\n
0xb0000837 | Ctap %1 completed.%n%nTransactionId: %2%nError: %3. %4\r\n
0xb0000838 | Ctap device info.%n%nTransactionId: %1%nProviderName: %2%nDevicePath: %3%nManufacturer: %4%nProduct: %5%nAAGuid: %6%nU2fProtocol: %7\r\n
0xb000083e | Ctap device device state info.%n%nTransport Type: %1%nWnfState: %2%nError: %3. %4%n\r\n
0xb000083f | Ctap device change notify info.%n%nTransport Type: %1%n\r\n
0xb0000898 | Ctap Usb provider thread started.%n%nTransactionId: %1\r\n
0xb0000899 | Ctap Usb provider thread completed.%n%nTransactionId: %1\r\n
0xb000089a | Ctap Usb provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00008a2 | Ctap Usb device thread started.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008a3 | Ctap Usb device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nAAGuid: %5%nU2fProtocol: %6\r\n
0xb00008a4 | Ctap Usb device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nAAGuid: %5%nU2fProtocol: %6%nState: %7%nStatus: %8%nError: %9. %10\r\n
0xb00008ac | Ctap Usb add device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008ad | Ctap Usb remove device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008ae | Ctap Usb device changes.%n%nTransactionId: %1\r\n
0xb00008af | Ctap Usb U2F device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008b0 | Ctap Usb connect to device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nDeviceErr: %5%nStatus: %6%nError: %7. %8\r\n
0xb00008b1 | Ctap Usb Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7\r\n
0xb00008b2 | Ctap Usb Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7%nError: %8. %9\r\n
0xb00008ca | Ctap Ble provider thread started.%n%nTransactionId: %1\r\n
0xb00008cb | Ctap Ble provider thread completed.%n%nTransactionId: %1\r\n
0xb00008cc | Ctap Ble provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00008d4 | Ctap Ble device thread started.%n%nTransactionId: %1%nDevicePath: %2%nPairedName: %3\r\n
0xb00008d5 | Ctap Ble device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nPairedName: %3%nAAGuid: %4%nU2fProtocol: %5\r\n
0xb00008d6 | Ctap Ble device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nPairedName: %3%nAAGuid: %4%nU2fProtocol: %5%nState: %6%nStatus: %7%nError: %8. %9\r\n
0xb00008de | Ctap Ble Function: %1 Location: %2%n%nError: %3. %4\r\n
0xb00008df | Ctap Ble U2F device.%n%nTransactionId: %1%nDevicePath: %2%nPairedName: %3\r\n
0xb00008e0 | Ctap Ble Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7\r\n
0xb00008e1 | Ctap Ble Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7%nLocation: %8%nError: %9. %10\r\n
0xb00008fc | Ctap Nfc provider thread started.%n%nTransactionId: %1\r\n
0xb00008fd | Ctap Nfc provider thread completed.%n%nTransactionId: %1\r\n
0xb00008fe | Ctap Nfc provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb0000906 | Ctap Nfc reader thread started.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000907 | Ctap Nfc reader thread completed.%n%nTransactionId: %1%nReader: %2%nAAGuid: %3%nU2fProtocol: %4\r\n
0xb0000908 | Ctap Nfc reader thread completed.%n%nTransactionId: %1%nReader: %2%nAAGuid: %3%nU2fProtocol: %4%nState: %5%nStatus: %6%nError: %7. %8\r\n
0xb000090a | Ctap Nfc reader manager thread started.%n%nTransactionId: %1%n\r\n
0xb000090b | Ctap Nfc reader manager thread completed.%n%nTransactionId: %1%nNumberOfTimesScardCancelCommandsSent: %2%n\r\n
0xb000090c | Cancelling Reader Threads.%n%nTransactionId: %1%n\r\n
0xb0000910 | Ctap Nfc add reader.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000911 | Ctap Nfc skip reader for: %2.%n%nTransactionId: %1%nReader: %3%nDeviceInstanceId: %4\r\n
0xb0000912 | Ctap Nfc transition reader for: %2.%n%nTransactionId: %1%nReader: %3\r\n
0xb0000913 | Ctap Nfc send message warning for: %2.%n%nTransactionId: %1%nReader: %3%nApduStatus: %4%nDeviceStatus: %5%nSmartCardError: %6. %7\r\n
0xb0000914 | Ctap Nfc send request error for: %2.%n%nTransactionId: %1%nReader: %3%nApduStatus: %4%nDeviceStatus: %5%nError: %6. %7\r\n
0xb0000915 | Ctap Nfc U2F device.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000916 | Ctap Nfc send message at: %2.%n%nTransactionId: %1%nReader: %3\r\n
0xb0000917 | Ctap Nfc SCardTransmit Request:%n%nTransactionId: %1%nReader: %2%n%nRequest: %3 bytes%n%4%n%nResponse data: %5 bytes%n%6%n%nApdu Status: %7%n\r\n
0xb0000918 | Ctap Nfc SCardTransmit Request:%n%nTransactionId: %1%nReader: %2%n%nRequest: %3 bytes%n%4%n%nResponse data: %5 bytes%n%6%n%nApdu Status: %7%n%nError: %8. %9\r\n
0xb0000960 | Ctap Test provider thread started.%n%nTransactionId: %1\r\n
0xb0000961 | Ctap Test provider thread completed.%n%nTransactionId: %1\r\n
0xb0000962 | Ctap Test provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n

### 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x10000001 | WebAuthN\r\n
0x10000002 | Ctap\r\n
0x10000003 | Cbor\r\n
0x10000004 | Usb\r\n
0x10000005 | Nfc\r\n
0x10000006 | Test\r\n
0x10000007 | Ngc\r\n
0x10000008 | Ble\r\n
0x3000000a | Start\r\n
0x3000000b | Stop\r\n
0x3000000c | Informational\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x50000010 | Success\r\n
0x70000001 | WebAuthN Ctap MakeCredential\r\n
0x70000002 | WebAuthN Ctap GetAssertion\r\n
0x70000003 | WebAuthN Ctap SendCommand\r\n
0x70000004 | WebAuthN Error\r\n
0x7000000a | WebAuthN Ngc MakeCredential\r\n
0x7000000b | WebAuthN Ngc GetAssertion\r\n
0x7000000c | Ngc MakeCredential Request\r\n
0x7000000d | Ngc MakeCredential Response\r\n
0x7000000e | Ngc GetAssertion Request\r\n
0x7000000f | Ngc GetAssertion Response\r\n
0x70000064 | Cbor Decode Error\r\n
0x70000065 | Cbor Encode MakeCredential Request\r\n
0x70000066 | Cbor Decode MakeCredential Response\r\n
0x70000067 | Cbor Encode GetAssertion Request\r\n
0x70000068 | Cbor Decode GetAssertion Response\r\n
0x700000c8 | WNF Ctap Device State Info\r\n
0x700000c9 | WNF Ctap Device Change Notify Info\r\n
0x700001f4 | Ctap Service\r\n
0x700001f5 | Ctap Command\r\n
0x700001f6 | Ctap Device Info\r\n
0x700001f7 | Ctap Function\r\n
0x700001fe | Ctap Usb Provider Thread\r\n
0x700001ff | Ctap Usb Device Thread\r\n
0x70000200 | Ctap Usb Add\r\n
0x70000201 | Ctap Usb Remove\r\n
0x70000202 | Ctap Usb Changes\r\n
0x70000203 | Ctap Usb Switch To U2F\r\n
0x70000204 | Ctap Usb Connect\r\n
0x70000205 | Ctap Usb Send Receive\r\n
0x70000212 | Ctap Ble Provider Thread\r\n
0x70000213 | Ctap Ble Device Thread\r\n
0x70000214 | Ctap Ble Switch To U2F\r\n
0x70000215 | Ctap Ble Function\r\n
0x70000216 | Ctap Ble Send Receive\r\n
0x70000226 | Ctap Nfc Provider Thread\r\n
0x70000227 | Ctap Nfc Reader Thread\r\n
0x70000228 | Ctap Nfc Add Reader\r\n
0x70000229 | Ctap Nfc Skip Reader\r\n
0x7000022a | Ctap Nfc Transition Reader\r\n
0x7000022b | Ctap Nfc Send Message\r\n
0x7000022c | Ctap Nfc Send Request\r\n
0x7000022d | Ctap Nfc Switch To U2F\r\n
0x7000022e | Ctap Nfc SCardTransmit Request\r\n
0x7000022f | Ctap Nfc Reader Manager Thread\r\n
0x700002bc | Ctap Test Provider Thread\r\n
0x90000001 | Microsoft-Windows-WebAuthN\r\n
0xb00003e8 | WebAuthN Ctap MakeCredential started.%n%nTransactionId: %1\r\n
0xb00003e9 | WebAuthN Ctap MakeCredential completed.%n%nTransactionId: %1\r\n
0xb00003ea | WebAuthN Ctap MakeCredential completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003eb | WebAuthN Ctap GetAssertion started.%n%nTransactionId: %1\r\n
0xb00003ec | WebAuthN Ctap GetAssertion completed.%n%nTransactionId: %1\r\n
0xb00003ed | WebAuthN Ctap GetAssertion completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003ee | WebAuthN Ctap SendCommand started.%n%nTransactionId: %1%nTicket: %3\r\n
0xb00003ef | WebAuthN Ctap SendCommand completed.%n%nTransactionId: %1\r\n
0xb00003f0 | WebAuthN Ctap SendCommand completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003fc | WebAuthN Ngc MakeCredential started.%n%nTransactionId: %1\r\n
0xb00003fd | WebAuthN Ngc MakeCredential completed.%n%nTransactionId: %1\r\n
0xb00003fe | WebAuthN Ngc MakeCredential completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00003ff | WebAuthN Ngc GetAssertion started.%n%nTransactionId: %1\r\n
0xb0000400 | WebAuthN Ngc GetAssertion completed.%n%nTransactionId: %1\r\n
0xb0000401 | WebAuthN Ngc GetAssertion completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb0000410 | Ngc MakeCredential request.%n%nTransactionId: %1%nRpId: %2%nAccountId: %3%nClientDataHashAlgId: %4 ClientDataLength: %5 ClientDataHash: %7%nExcludeCredentialCount: %8%nCredentialParameterCount: %9\r\n
0xb0000411 | Ngc MakeCredential response.%n%nTransactionId: %1%nAttestationFormatType: %2%nRpIdHash: %4%nFlags: %5%nSignCount: %6%nAAGuid: %7%nCredentialId: %9%nU2fPublicKey: %10%nPublicKey: %12%nResponse: %14\r\n
0xb0000412 | Ngc GetAssertion request.%n%nTransactionId: %1%nRpId: %2%nClientDataHashAlgId: %3 ClientDataLength: %4 ClientDataHash: %6%nAllowCredentialCount: %7\r\n
0xb0000413 | Ngc GetAssertion response.%n%nTransactionId: %1%nRpIdHash: %3%nFlags: %4%nSignCount: %5%nCredentialId: %7%\r\n
0xb0000424 | WebAuthN error at: %2%n%nTransactionId: %1%nError: %3. %4\r\n
0xb000044c | Cbor decode error.%n%nTransactionId: %1%nFunction: %2%nCborError: %3 %4%nErrorOffset: %5 LineNumber: %6%nEncoded: %8\r\n
0xb000044d | Cbor encode MakeCredential request.%n%nTransactionId: %1%nRpId: %2%nUserId: %4%nClientDataHashAlgId: %5 ClientDataLength: %6 ClientDataHash: %8%nRequireResidentKey: %9%nExcludeCredentialCount: %10%nCredentialParameterCount: %11%nRequest: %13\r\n
0xb000044e | Cbor decode MakeCredential response.%n%nTransactionId: %1%nAttestationFormatType: %2%nRpIdHash: %4%nFlags: %5%nSignCount: %6%nAAGuid: %7%nCredentialId: %9%nU2fPublicKey: %10%nPublicKey: %12%nResponse: %14\r\n
0xb000044f | Cbor encode GetAssertion request.%n%nTransactionId: %1%nRpId: %2%nClientDataHashAlgId: %3 ClientDataLength: %4 ClientDataHash: %6%nAllowCredentialCount: %7%nRequest: %9\r\n
0xb0000450 | Cbor decode GetAssertion response.%n%nTransactionId: %1%nRpIdHash: %3%nFlags: %4%nSignCount: %5%nCredentialId: %7%nResponse: %9\r\n
0xb00007d0 | Ctap service started successfully.\r\n
0xb00007d1 | Ctap service stopped successfully.\r\n
0xb0000834 | Ctap %1 started.%n%nTransactionId: %2%nFlags: %3%nTimeoutMilliseconds: %4%nTicket: %6%nRequest: %8\r\n
0xb0000835 | Ctap command started.%n%nRequest: %2\r\n
0xb0000836 | Ctap %1 completed.%n%nTransactionId: %2%nResponse: %4\r\n
0xb0000837 | Ctap %1 completed.%n%nTransactionId: %2%nError: %3. %4\r\n
0xb0000838 | Ctap device info.%n%nTransactionId: %1%nProviderName: %2%nDevicePath: %3%nManufacturer: %4%nProduct: %5%nAAGuid: %6%nU2fProtocol: %7\r\n
0xb0000839 | Ctap Function: %1 Location: %2%n%nError: %3. %4\r\n
0xb000083a | Ctap Name: %1 Value: %2\r\n
0xb000083e | Ctap device device state info.%n%nTransport Type: %1%nWnfState: %2%nError: %3. %4%n\r\n
0xb000083f | Ctap device change notify info.%n%nTransport Type: %1%n\r\n
0xb0000898 | Ctap Usb provider thread started.%n%nTransactionId: %1\r\n
0xb0000899 | Ctap Usb provider thread completed.%n%nTransactionId: %1\r\n
0xb000089a | Ctap Usb provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00008a2 | Ctap Usb device thread started.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008a3 | Ctap Usb device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nAAGuid: %5%nU2fProtocol: %6\r\n
0xb00008a4 | Ctap Usb device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nAAGuid: %5%nU2fProtocol: %6%nState: %7%nStatus: %8%nError: %9. %10\r\n
0xb00008ac | Ctap Usb add device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008ad | Ctap Usb remove device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008ae | Ctap Usb device changes.%n%nTransactionId: %1\r\n
0xb00008af | Ctap Usb U2F device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4\r\n
0xb00008b0 | Ctap Usb connect to device.%n%nTransactionId: %1%nDevicePath: %2%nManufacturer: %3%nProduct: %4%nDeviceErr: %5%nStatus: %6%nError: %7. %8\r\n
0xb00008b1 | Ctap Usb Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7\r\n
0xb00008b2 | Ctap Usb Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7%nError: %8. %9\r\n
0xb00008ca | Ctap Ble provider thread started.%n%nTransactionId: %1\r\n
0xb00008cb | Ctap Ble provider thread completed.%n%nTransactionId: %1\r\n
0xb00008cc | Ctap Ble provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb00008d4 | Ctap Ble device thread started.%n%nTransactionId: %1%nDevicePath: %2%nPairedName: %3\r\n
0xb00008d5 | Ctap Ble device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nPairedName: %3%nAAGuid: %4%nU2fProtocol: %5\r\n
0xb00008d6 | Ctap Ble device thread completed.%n%nTransactionId: %1%nDevicePath: %2%nPairedName: %3%nAAGuid: %4%nU2fProtocol: %5%nState: %6%nStatus: %7%nError: %8. %9\r\n
0xb00008de | Ctap Ble Function: %1 Location: %2%n%nError: %3. %4\r\n
0xb00008df | Ctap Ble U2F device.%n%nTransactionId: %1%nDevicePath: %2%nPairedName: %3\r\n
0xb00008e0 | Ctap Ble Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7\r\n
0xb00008e1 | Ctap Ble Send Receive:%n%nTransactionId: %1%nRequest Command: %2 Response Command: %5%nRequest: %4%nResponse: %7%nLocation: %8%nError: %9. %10\r\n
0xb00008fc | Ctap Nfc provider thread started.%n%nTransactionId: %1\r\n
0xb00008fd | Ctap Nfc provider thread completed.%n%nTransactionId: %1\r\n
0xb00008fe | Ctap Nfc provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
0xb0000906 | Ctap Nfc reader thread started.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000907 | Ctap Nfc reader thread completed.%n%nTransactionId: %1%nReader: %2%nAAGuid: %3%nU2fProtocol: %4\r\n
0xb0000908 | Ctap Nfc reader thread completed.%n%nTransactionId: %1%nReader: %2%nAAGuid: %3%nU2fProtocol: %4%nState: %5%nStatus: %6%nError: %7. %8\r\n
0xb000090a | Ctap Nfc reader manager thread started.%n%nTransactionId: %1%n\r\n
0xb000090b | Ctap Nfc reader manager thread completed.%n%nTransactionId: %1%nNumberOfTimesScardCancelCommandsSent: %2%n\r\n
0xb000090c | Cancelling Reader Threads.%n%nTransactionId: %1%n\r\n
0xb0000910 | Ctap Nfc add reader.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000911 | Ctap Nfc skip reader for: %2.%n%nTransactionId: %1%nReader: %3%nDeviceInstanceId: %4\r\n
0xb0000912 | Ctap Nfc transition reader for: %2.%n%nTransactionId: %1%nReader: %3\r\n
0xb0000913 | Ctap Nfc send message warning for: %2.%n%nTransactionId: %1%nReader: %3%nApduStatus: %4%nDeviceStatus: %5%nSmartCardError: %6. %7\r\n
0xb0000914 | Ctap Nfc send request error for: %2.%n%nTransactionId: %1%nReader: %3%nApduStatus: %4%nDeviceStatus: %5%nError: %6. %7\r\n
0xb0000915 | Ctap Nfc U2F device.%n%nTransactionId: %1%nReader: %2\r\n
0xb0000916 | Ctap Nfc send message at: %2.%n%nTransactionId: %1%nReader: %3\r\n
0xb0000917 | Ctap Nfc SCardTransmit Request:%n%nTransactionId: %1%nReader: %2%n%nRequest: %3 bytes%n%4%n%nResponse data: %5 bytes%n%6%n%nApdu Status: %7%n\r\n
0xb0000918 | Ctap Nfc SCardTransmit Request:%n%nTransactionId: %1%nReader: %2%n%nRequest: %3 bytes%n%4%n%nResponse data: %5 bytes%n%6%n%nApdu Status: %7%n%nError: %8. %9\r\n
0xb0000960 | Ctap Test provider thread started.%n%nTransactionId: %1\r\n
0xb0000961 | Ctap Test provider thread completed.%n%nTransactionId: %1\r\n
0xb0000962 | Ctap Test provider thread completed.%n%nTransactionId: %1%nError: %2. %3\r\n
