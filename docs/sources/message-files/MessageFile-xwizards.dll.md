## xwizards.dll

Path: %SystemRoot%\system32\xwizards.dll

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x00000051 | %1-%2
0x00000052 | %1-%2
0x00000053 | %1-%2
0x50000002 | Error
0x50000003 | Warning
0x50000004 | Information
0x90000001 | Microsoft-Windows-XWizards
0x90000002 | Application
0x00000001 | XML File Processing
0x00000002 | XML Process Error
0x00000003 | Usage: \r\n   xwizard ProcessXMLFile [/u] [/m] <filename> \r\nwhere:\r\n   /u = unattended (log parsing errors instead of showing them)\r\n   /m = additionally generate Vista setup manifest file section\r\n        (create resulting file in current directory as <filename>.man)\r\n   filename = XML file name\r\nexamples:\r\n   xwizard ProcessXMLFile myconfig.xml\r\n   xwizard ProcessXMLFile /m mysetup.xml
0x0000000b | RunWizard
0x0000000c | RunWizard Error
0x0000000d | Usage: \r\n   xwizard RunWizard [/u] [/t<?>] [/c<?>] [/f<?>] [/p<GUID>] <GUID> [/z [<?>] ]\r\nwhere:\r\n   /u = unattended (log errors instead of showing them)\r\n   /t = optional wizard type (duifixed, duiresize, wizard97, aerofixed, aeroresize)\r\n   /c = context flags\r\n   /f = user defined flags\r\n   /p = parent host GUID identifier ({<GUID>})\r\n   GUID = Wizard component GUID identifier ({<GUID>})\r\n   /z = user command line (should always be last, rest of line)\r\nexamples:\r\n   xwizard RunWizard {7071ECA0-663B-4bc1-A1FA-B97F3B917C55}\r\n   xwizard RunWizard /taerofixed /c1 /f3 {7071ECA0-663B-4bc1-A1FA-B97F3B917C55} /z/myoption1 /myoption2
0x0000000e | Usage: \r\n   xwizard RunPropertySheet [/u] [/c<?>] [/f<?>] [/p<GUID>] <GUID> [/z [<?>] ]\r\nwhere:\r\n   /u = unattended (log errors instead of showing them)\r\n   /c = context flags\r\n   /f = user defined flags\r\n   /p = parent host GUID identifier ({<GUID>})\r\n   GUID = Property sheet component GUID identifier ({<GUID>})\r\n   /z = user command line (should always be last, rest of line)\r\nexamples:\r\n   xwizard RunPropertySheet {7071ECA0-663B-4bc1-A1FA-B97F3B917C55}\r\n   xwizard RunPropertySheet /c1 /f3 {7071ECA0-663B-4bc1-A1FA-B97F3B917C55} /z/myoption1 /myoption2
0xc0000004 | XML parse error in file "%1" at line %2, column %3:\r\n%4\r\n"%5"
0xc0000005 | XML process error: \r\n%1 - %2
0xc000000f | Run Wizard Error: %1 - %2
0xc0000033 | %1
0xc0000034 | Unknown command line option [%1] found.

### 6.2.9200.16384, 6.3.9600.16384, 10.0.10586.0, 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1

Message identifier | Message string
--- | ---
0x00000001 | XML File Processing
0x00000002 | XML Process Error
0x00000003 | Usage: \r\n   xwizard ProcessXMLFile [/u] [/m] <filename> \r\nwhere:\r\n   /u = unattended (log parsing errors instead of showing them)\r\n   /m = additionally generate Vista setup manifest file section\r\n        (create resulting file in current directory as <filename>.man)\r\n   filename = XML file name\r\nexamples:\r\n   xwizard ProcessXMLFile myconfig.xml\r\n   xwizard ProcessXMLFile /m mysetup.xml
0x0000000b | RunWizard
0x0000000c | RunWizard Error
0x0000000d | Usage: \r\n   xwizard RunWizard [/u] [/t<?>] [/c<?>] [/f<?>] [/p<GUID>] <GUID> [/z [<?>] ]\r\nwhere:\r\n   /u = unattended (log errors instead of showing them)\r\n   /t = optional wizard type (wizard97, aero, dui, moderndui)\r\n   /c = context flags\r\n   /f = user defined flags\r\n   /p = parent host GUID identifier ({<GUID>})\r\n   GUID = Wizard component GUID identifier ({<GUID>})\r\n   /z = user command line (should always be last, rest of line)\r\nexamples:\r\n   xwizard RunWizard {7071ECA0-663B-4bc1-A1FA-B97F3B917C55}\r\n   xwizard RunWizard /taero /c1 /f3 {7071ECA0-663B-4bc1-A1FA-B97F3B917C55} /z/myoption1 /myoption2
0x0000000e | Usage: \r\n   xwizard RunPropertySheet [/u] [/c<?>] [/f<?>] [/p<GUID>] <GUID> [/z [<?>] ]\r\nwhere:\r\n   /u = unattended (log errors instead of showing them)\r\n   /c = context flags\r\n   /f = user defined flags\r\n   /p = parent host GUID identifier ({<GUID>})\r\n   GUID = Property sheet component GUID identifier ({<GUID>})\r\n   /z = user command line (should always be last, rest of line)\r\nexamples:\r\n   xwizard RunPropertySheet {7071ECA0-663B-4bc1-A1FA-B97F3B917C55}\r\n   xwizard RunPropertySheet /c1 /f3 {7071ECA0-663B-4bc1-A1FA-B97F3B917C55} /z/myoption1 /myoption2
0x00000051 | %1-%2
0x00000052 | %1-%2
0x00000053 | %1-%2
0x50000002 | Error
0x50000003 | Warning
0x50000004 | Information
0x90000001 | Microsoft-Windows-XWizards
0x90000002 | Application
0xc0000004 | XML parse error in file "%1" at line %2, column %3:\r\n%4\r\n"%5"
0xc0000005 | XML process error: \r\n%1 - %2
0xc000000f | Run Wizard Error: %1 - %2
0xc0000033 | %1
0xc0000034 | Unknown command line option [%1] found.
