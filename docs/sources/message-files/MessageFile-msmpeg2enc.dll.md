## msmpeg2enc.dll

Path: %SystemRoot%\system32\msmpeg2enc.dll

### 6.1.7600.16385

Message identifier | Message string
--- | ---
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x7000002a | MPEG-2 Encode/Mux for DLNA\r\n
0x90000001 | Microsoft-Windows-MPEG-2 Encode/Mux for DLNA\r\n
0xb0000000 | Starting. Video: %1 (%2,%3). Audio Channels: %4, Video Bit Rate: %5, Audio Bit Rate %6, Seek Offset %7ms\r\n
0xb0000001 | Stopping. Bytes Muxed: %1, Video Frames Received: %2, Video Frames Encoded: %3, Audio Bytes Received: %4, Audio Frames Encoded: %5\r\n
0xb0000002 | Error: %1\r\n
0xb0000003 | Video Frame Received.  Timestamp=%1, ID=%2\r\n
0xb0000004 | Video Frame Encoded.  Input Frame ID=%1, Input Timestamp=%2, Output Timestamp=%3\r\n
0xb0000005 | Audio Sample Received.  Timestamp=%1, Bytes in buffer=%2\r\n
0xb0000006 | Audio Frame Encoded\r\n

### 10.0.14393.0, 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1, 12.0.9200.16384, 12.0.9600.16384, 12.0.10586.0

Message identifier | Message string
--- | ---
0x1000002f | Events dealing with the control of the encoder.\r\n
0x10000030 | Events that deal with the processing of samples\r\n
0x10000031 | Response Time\r\n
0x10000034 | SQM\r\n
0x30000000 | Info\r\n
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x30000009 | Send\r\n
0x300000f0 | Receive\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x51000002 | Error\r\n
0x70000001 | Configuration of the encoder\r\n
0x70000002 | Task done by the video encoder\r\n
0x7100002a | MPEG-2 Encode/Mux for DLNA\r\n
0x90000001 | Events from the MPEG-2 Video Encoder MFT\r\n
0x91000001 | Microsoft-Windows-MPEG-2 Encode/Mux for DLNA\r\n
0xb0000000 | Input sample (%2) to stream #%1 submitted to MPEG-2 Video Encoder through the MFT. Flags: %3\r\n
0xb0000001 | Finished submission of sample to encoder. HR=%1\r\n
0xb0000002 | Process event method called on MFT for Input Stream #%1 with event %2\r\n
0xb0000003 | Processing of Event by the MFT has finished. HR=%1\r\n
0xb0000004 | Message %1 recieved by MFT through ProcessMessage with parameter %2\r\n
0xb0000005 | Finished processing message given to MPEG-2 Video Encoder MFT. HR=%1\r\n
0xb0000006 | Bitrate has been changed from %1 bps to %2 bps during the encoding process.\r\n
0xb0000007 | Start of producing an output sample on the MPEG-2 Video Encoder MFT. Output Buffer Count: %2   Start of Output Buffer Array: %3   Pointer to Output Buffer Status Flag: %4   Output Buffer Flags passed in: %1\r\n
0xb0000008 | Finished creating sample for output on the MPEG-2 Video Encoder MFT. HR=%1\r\n
0xb0000009 | Mpeg-2 Video Encoder MFT is Signaling that an output sample (Location: %1, Length: %2) is ready\r\n
0xb000000a | MPEG-2 Video Encoder is requesting for more input samples\r\n
0xb000000b | The MPEG-2 Video Encoder MFT has received the input from the application and is passing it into the encoder. Sample: %1  Sample Byte Length: %2  Stop Encoding: %3\r\n
0xb000000c | Encoder is being created with these settings:  Coding Mode: %1  Bitrate: %2 bps  Complexity: %3  Encoder Instance: %4\r\n
0xb1000000 | Starting. Video: %1 (%2,%3). Audio Channels: %4, Video Bit Rate: %5, Audio Bit Rate %6, Seek Offset %7ms\r\n
0xb1000001 | Stopping. Bytes Muxed: %1, Video Frames Received: %2, Video Frames Encoded: %3, Audio Bytes Received: %4, Audio Frames Encoded: %5\r\n
0xb1000002 | Error: %1\r\n
0xb1000003 | Video Frame Received.  Timestamp=%1, ID=%2\r\n
0xb1000004 | Video Frame Encoded.  Input Frame ID=%1, Input Timestamp=%2, Output Timestamp=%3\r\n
0xb1000005 | Audio Sample Received.  Timestamp=%1, Bytes in buffer=%2\r\n
0xb1000006 | Audio Frame Encoded\r\n
0xd0000001 | Constant Bit Rate\r\n
0xd0000002 | Variable Bit Rate - Peak Constrained\r\n
0xd0000003 | Variable Bit Rate - Quality Based\r\n
0xd0000004 | Flush Command\r\n
0xd0000005 | Drain Command\r\n
0xd0000006 | Set D3D Manager Command\r\n
0xd0000007 | Begin Streaming Command\r\n
0xd0000008 | End Streaming Command\r\n
0xd0000009 | End of Stream Notification\r\n
0xd000000a | Start of Stream Notification\r\n
0xd000000b | Insert Marker Command\r\n
0xd1000001 | (two channels mode\r\n
0xd1000002 | 1/0 mono mode\r\n
0xd1000003 | 2/0 stereo mode\r\n
0xd1000004 | Elementary Format\r\n
0xd1000005 | Video CD Format\r\n
0xd1000006 | SVCD Format\r\n
0xd1000007 | Transport Stream Format\r\n
0xf0000001 | Input Data Buffer Placeholder - Do not use\r\n
0xf0000002 | No Flags\r\n
0xf0000003 | Discard output when no buffer provided\r\n
