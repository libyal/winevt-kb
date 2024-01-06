## mpio.sys

Path: %SystemRoot%\System32\drivers\mpio.sys

### 6.0.6000.16386, 6.1.7600.16385, 6.1.7601.17514

Message identifier | Message string
--- | ---
0x40070001 | %1 created.\r\n
0x40070002 | Added device to %1. DumpData contains the current number of paths.\r\n
0x40090025 | %2 is attempting an operation on %1. The Type is noted in the dump data.\r\n
0x80070003 | There was an error creating a device claimed by %2.\r\n
0x80070027 | Serial number for device %1 was built using VPD 0x80 information because %2 didn't provide one.\r\n
0x80080011 | %1 is currently in a degraded state. One or more paths have failed, though the process is\r\nnow complete.\r\n
0x80080012 | A Single Path Fail-Over is being attempted on %1.\r\n
0x80080014 | A Path Verification request to a device on %1 that is controlled by %2 has failed. This may\r\nindicate a Path Failure.\r\n
0x80080018 | A PnP operation was rejected, as %1 is not in a state where the request can be honoured.\r\n
0x80080019 | Requests that were queued to %1 have failed during resubmission.\r\n
0xc0080010 | A fail-over on %1 occurred.\r\n
0xc0080013 | An operation failed on %1 due to lack of memory.\r\n
0xc0080015 | The internal state of %1 is inconsistent. This indicates potential failures in this support.\r\n
0xc0080016 | A fail-over on %1 was attempted, however the attempt failed. The devices will be removed.\r\n
0xc0080017 | All paths have failed. %1 will be removed.\r\n
0xc008001a | Reference counts on either %1 or an object controller by it are incorrect. Removal of this object will not be possible.\r\n
0xc0090020 | %2 failed to return a Path to %1.\r\n
0xc0090021 | %2 returned a bogus Path to %1.\r\n
0xc0090022 | %2 failed final initialisation on %1.\r\n
0xc0090023 | %2 supplied an invalid ID for an operation on %1.\r\n
0xc0090024 | An unknown DSM supplied an invalid ID for an operation on %1.\r\n
0xc0090026 | A device under %1, being controlled by %2 was removed, but the DSM failed the operation.\r\n
