## aphostres.dll

Path: %SystemRoot%\System32\APHostRes.dll

### 10.0.10586.0

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000013 | Trace\r\n
0xb0000001 | Error: HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb0000002 | Error Propagated: HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb00003e8 | Request Manager exceeded maximum requests limit and will start rejecting older requests\r\n
0xb00003e9 | Scheduling function (Step) failed with result %1\r\n
0xb00003ea | Authentication error (%1) detected for request [%2-%3]\r\n
0xb00003ec | RPC Registration failed with error code %1\r\n
0xb00003ee | Request Manager was initialized correctly\r\n
0xb00003ef | Request [%2-%3] failed with error code %1\r\n
0xb00003f0 | Request [%2-%3] permanently failed with error code %1\r\n
0xb00003f1 | Requests (#%1) are pending execution during shutdown\r\n
0xb00003f4 | Request Manager entered battery saving mode\r\n
0xb00003f5 | Request Manager recovered from battery saving mode\r\n
0xb00003f6 | Request Manager entered low-memory mode\r\n
0xb00003f7 | Request Manager recovered from low-memory mode\r\n
0xb00003f8 | Request Manager entered no connectivity mode, suspending activity\r\n
0xb00003f9 | Request Manager detected connection recovery, retrying\r\n
0xb00003fa | Fetch more requested for feed which reached the end and can't fetch any more data\r\n
0xb00003fb | Fetch more was requested for empty or new feed, normal feed fetch will be performed\r\n
0xb00003fc | Failed to add the comment to the database after succesful post\r\n
0xb00003fd | Request Manager found matching request to cancel [%1-%2] (request is not executing)\r\n
0xb00003fe | Request Manager found matching executing request to cancel [%1-%2], sending cancelation to provider\r\n
0xb00003ff | Request [%1-%2] was canceled succesfully\r\n
0xb0000404 | Upload file job to alubm (id: %1-%2-%3) has exceeded the maximum number of retry\r\n
0xb0000405 | Request Manager queued request [%1-%2]\r\n
0xb0000406 | Request Manager is executing request [%1-%2]\r\n
0xb0000407 | Request Manager completed request [%1-%2] with success\r\n
0xb000040a | Refresh requested for a feed that satisfies freshness requirement.\r\n
0xb00005dc | RM::[PERFMARKER] Single Step BEGIN\r\n
0xb00005dd | RM::[PERFMARKER] Single Step END\r\n
0xb00005de | RM::[PERFMARKER] Execute request BEGIN (rmguid:%1)(handle:%2)\r\n
0xb00005df | RM::[PERFMARKER] Execute request END (rmguid:%1)(handle:%2)\r\n
0xb00007d0 | Sending notification failed for endpoint %1 with error code %2\r\n
0xb00007d4 | SNAS Initialized successfully\r\n
0xb00007d5 | SNAS Uninitialized\r\n
0xb0000803 | Provider [%1] failed to initialize with HR: %2\r\n
0xb0000804 | Provider [%1] failed to late-initialize HR: %2\r\n
0xb0000805 | Failed to CoCreate provider [%1], HR: %2\r\n
0xb000080d | Job [%1] submitted with id %2\r\n
0xb0001388 | SNService - Service Started\r\n
0xb0001389 | SNService - Failed to Initialize\r\n
0xb000138b | SNService - Critical error during SNService startup, HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb000138c | SNService - Request Manager Database failed to initialze, 0x%1\r\n
0xb000138d | SNService - Service Stopped\r\n
0xb0001b59 | Job [%1] completed execution and will not be rescheduled\r\n
0xb0001b5a | Job [%1] failed, error [%2] and will remain inactive in the queue\r\n
0xb0001b5b | Job [%1] completed all requests for given state and will be rescheduled for execution, allowExecutionInSeconds [%2] onlyWhenConnectionChanged [%3]\r\n
0xb0001b5c | Job Dispatcher exceeded maximum number of jobs and will cancel oldest jobs in the queue\r\n
0xb0001b5d | Job [%1] expired and will be removed from the queue\r\n
0xb0001b5e | Job [%1] SNJobType:[%2] Executing \r\n
0xb0001b5f | Synchronous failure in job execution for job [%1, SNJobType:%2], error [%3]\r\n
0xb0001b60 | Job [%1] failed to update in database, error [%2]\r\n
0xb0001b61 | Job [%1] of type %2 was submitted to Job Dispatcher\r\n
0xb0001b62 | Job [%1] failed to be submitted to Job Dispatcher, error %2\r\n
0xb0001b63 | Request for job [%1] failed to be submitted to Job Dispatcher, error %2\r\n
0xb0001b64 | Canceling job [%1]\r\n
0xb0001b65 | Job dispatcher received retry message from Connection Manager\r\n
0xb0001b66 | Job dispatcher received time based retry message and will retry failed jobs\r\n
0xb0001b67 | Job dispatcher received time based retry message and will retry failed jobs, error %1\r\n
0xb0001b68 | Job dispatcher created new volume\r\n
0xb0001b6e | Unexpected job dispatcher failure occured, HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb0001b6f | Failed to cancel job, hr = %1\r\n
0xb0001b70 | Failed to add job %1 to the queue, hr = %2\r\n
0xb0001b71 | Job [%1, SNJobType: %2] executed [%3] exceeding time limit; execution time = %4; (ActivityList entry = #%5/%6)\r\n
0xb0001b72 | Job [%1] seems rogue (exceeded max step limit) and will be removed from the queue\r\n
0xb0001b73 | Job [%1] seems rogue (exceeded delayed retry limit) and will be removed from the queue\r\n
0xb0001b74 | Job [%1, SNJobType: %2] executed [%3] within time limit; execution time = %4;  (ActivityList entry = #%5/%6)\r\n
0xb0001b75 | Completing job [%1, SNJobType:%2]\r\n
0xb0001b76 | Exceeded maximum number of jobs in the queue, will remove old job [%1]; (ActivityList entry #%2/%3)\r\n
0xb0002134 | Setting Room background picture, deleting remote room picture (Step) failed with result %1\r\n
0xb0002135 | Setting Room background picture, uploading room picture (Step) failed with result %1\r\n
0xb0002136 | Download Room background picture, download room picture metadata (Step) failed with result %1\r\n
0xb0002137 | Download Room background picture, download room picture binary (Step) failed with result %1\r\n
0xd0000001 | DownloadHomeFeed\r\n
0xd0000002 | DownloadFeed\r\n
0xd0000003 | DownloadDashboardFeed\r\n
0xd0000004 | DownloadAlbumItems\r\n
0xd0000005 | DownloadAlbumCover\r\n
0xd0000006 | DownloadImage\r\n
0xd0000007 | RichConnectData\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | NotStarted\r\n
0xd000000a | Started\r\n
0xd000000b | Completed\r\n
0xd000000c | Cancelled\r\n
0xd000000d | Failed\r\n

### 10.0.14393.0

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0x70000013 | Trace\r\n
0xb0000001 | Error: HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb0000002 | Error Propagated: HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb00003e8 | Request Manager exceeded maximum requests limit and will start rejecting older requests\r\n
0xb00003e9 | Scheduling function (Step) failed with result %1\r\n
0xb00003ea | Authentication error (%1) detected for request [%2-%3]\r\n
0xb00003ec | RPC Registration failed with error code %1\r\n
0xb00003ee | Request Manager was initialized correctly\r\n
0xb00003ef | Request [%2-%3] failed with error code %1\r\n
0xb00003f0 | Request [%2-%3] permanently failed with error code %1\r\n
0xb00003f1 | Requests (#%1) are pending execution during shutdown\r\n
0xb00003f4 | Request Manager entered battery saving mode\r\n
0xb00003f5 | Request Manager recovered from battery saving mode\r\n
0xb00003f6 | Request Manager entered low-memory mode\r\n
0xb00003f7 | Request Manager recovered from low-memory mode\r\n
0xb00003f8 | Request Manager entered no connectivity mode, suspending activity\r\n
0xb00003f9 | Request Manager detected connection recovery, retrying\r\n
0xb00003fa | Fetch more requested for feed which reached the end and can't fetch any more data\r\n
0xb00003fb | Fetch more was requested for empty or new feed, normal feed fetch will be performed\r\n
0xb00003fc | Failed to add the comment to the database after succesful post\r\n
0xb00003fd | Request Manager found matching request to cancel [%1-%2] (request is not executing)\r\n
0xb00003fe | Request Manager found matching executing request to cancel [%1-%2], sending cancelation to provider\r\n
0xb00003ff | Request [%1-%2] was canceled succesfully\r\n
0xb0000404 | Upload file job to alubm (id: %1-%2-%3) has exceeded the maximum number of retry\r\n
0xb0000405 | Request Manager queued request [%1-%2]\r\n
0xb0000406 | Request Manager is executing request [%1-%2]\r\n
0xb0000407 | Request Manager completed request [%1-%2] with success\r\n
0xb000040a | Refresh requested for a feed that satisfies freshness requirement.\r\n
0xb00005dc | RM::[PERFMARKER] Single Step BEGIN\r\n
0xb00005dd | RM::[PERFMARKER] Single Step END\r\n
0xb00005de | RM::[PERFMARKER] Execute request BEGIN (rmguid:%1)(handle:%2)\r\n
0xb00005df | RM::[PERFMARKER] Execute request END (rmguid:%1)(handle:%2)\r\n
0xb00007d0 | Sending notification failed for endpoint %1 with error code %2\r\n
0xb00007d4 | SNAS Initialized successfully\r\n
0xb00007d5 | SNAS Uninitialized\r\n
0xb0000803 | Provider [%1] failed to initialize with HR: %2\r\n
0xb0000804 | Provider [%1] failed to late-initialize HR: %2\r\n
0xb0000805 | Failed to CoCreate provider [%1], HR: %2\r\n
0xb000080d | Job [%1] submitted with id %2\r\n
0xb0001388 | SNService - Service Started\r\n
0xb0001389 | SNService - Failed to Initialize\r\n
0xb000138b | SNService - Critical error during SNService startup, HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb000138c | SNService - Request Manager Database failed to initialze, 0x%1\r\n
0xb000138d | SNService - Service Stopped\r\n
0xb000138e | SNService - Setting CPU rate cap to %1%%\r\n
0xb0001b59 | Job [%1] completed execution and will not be rescheduled\r\n
0xb0001b5a | Job [%1] failed, error [%2] and will remain inactive in the queue\r\n
0xb0001b5b | Job [%1] completed all requests for given state and will be rescheduled for execution, allowExecutionInSeconds [%2] onlyWhenConnectionChanged [%3]\r\n
0xb0001b5c | Job Dispatcher exceeded maximum number of jobs and will cancel oldest jobs in the queue\r\n
0xb0001b5d | Job [%1] expired and will be removed from the queue\r\n
0xb0001b5e | Job [%1] SNJobType:[%2] Executing \r\n
0xb0001b5f | Synchronous failure in job execution for job [%1, SNJobType:%2], error [%3]\r\n
0xb0001b60 | Job [%1] failed to update in database, error [%2]\r\n
0xb0001b61 | Job [%1] of type %2 was submitted to Job Dispatcher\r\n
0xb0001b62 | Job [%1] failed to be submitted to Job Dispatcher, error %2\r\n
0xb0001b63 | Request for job [%1] failed to be submitted to Job Dispatcher, error %2\r\n
0xb0001b64 | Canceling job [%1]\r\n
0xb0001b65 | Job dispatcher received retry message from Connection Manager\r\n
0xb0001b66 | Job dispatcher received time based retry message and will retry failed jobs\r\n
0xb0001b67 | Job dispatcher received time based retry message and will retry failed jobs, error %1\r\n
0xb0001b68 | Job dispatcher created new volume\r\n
0xb0001b6e | Unexpected job dispatcher failure occured, HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb0001b6f | Failed to cancel job, hr = %1\r\n
0xb0001b70 | Failed to add job %1 to the queue, hr = %2\r\n
0xb0001b71 | Job [%1, SNJobType: %2] executed [%3] exceeding time limit; execution time = %4; (ActivityList entry = #%5/%6)\r\n
0xb0001b72 | Job [%1] seems rogue (exceeded max step limit) and will be removed from the queue\r\n
0xb0001b73 | Job [%1] seems rogue (exceeded delayed retry limit) and will be removed from the queue\r\n
0xb0001b74 | Job [%1, SNJobType: %2] executed [%3] within time limit; execution time = %4;  (ActivityList entry = #%5/%6)\r\n
0xb0001b75 | Completing job [%1, SNJobType:%2]\r\n
0xb0001b76 | Exceeded maximum number of jobs in the queue, will remove old job [%1]; (ActivityList entry #%2/%3)\r\n
0xb0001b77 | Added activity with handle [%1] to the submission list of activity with handle [%2]\r\n
0xb0001b78 | Added work with handle [%1] to the submission list of activity with handle [%2]\r\n
0xb0001b79 | Added request with handle [%1] to the submission list of activity with handle [%2]\r\n
0xb0001b7a | Removed submission with handle [%1] from the submission list of activity with handle [%2]\r\n
0xb0001b7b | Submission with handle [%1] completed but was not removed from submission list of activity with handle [%2]\r\n
0xb0002134 | Setting Room background picture, deleting remote room picture (Step) failed with result %1\r\n
0xb0002135 | Setting Room background picture, uploading room picture (Step) failed with result %1\r\n
0xb0002136 | Download Room background picture, download room picture metadata (Step) failed with result %1\r\n
0xb0002137 | Download Room background picture, download room picture binary (Step) failed with result %1\r\n
0xd0000001 | DownloadHomeFeed\r\n
0xd0000002 | DownloadFeed\r\n
0xd0000003 | DownloadDashboardFeed\r\n
0xd0000004 | DownloadAlbumItems\r\n
0xd0000005 | DownloadAlbumCover\r\n
0xd0000006 | DownloadImage\r\n
0xd0000007 | RichConnectData\r\n
0xd0000008 | Invalid\r\n
0xd0000009 | NotStarted\r\n
0xd000000a | Started\r\n
0xd000000b | Completed\r\n
0xd000000c | Cancelled\r\n
0xd000000d | Failed\r\n

### 10.0.15063.0, 10.0.16299.15, 10.0.17134.1, 10.0.17763.1, 10.0.18362.1, 10.0.19041.1, 10.0.22000.1

Message identifier | Message string
--- | ---
0x30000001 | Start\r\n
0x30000002 | Stop\r\n
0x50000002 | Error\r\n
0x50000003 | Warning\r\n
0x50000004 | Information\r\n
0x50000005 | Verbose\r\n
0xb0000001 | Error: HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb0000002 | Error Propagated: HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb00007d0 | Sending notification failed for endpoint %1 with error code %2\r\n
0xb00007d4 | SNAS Initialized successfully\r\n
0xb00007d5 | SNAS Uninitialized\r\n
0xb0000803 | Provider [%1] failed to initialize with HR: %2\r\n
0xb0000804 | Provider [%1] failed to late-initialize HR: %2\r\n
0xb0000805 | Failed to CoCreate provider [%1], HR: %2\r\n
0xb000080d | Job [%1] submitted with id %2\r\n
0xb0000faa | SNASJob: Initializing SNAS job [%1]\r\n
0xb0000fab | SNASJob: Job [%1] matches the empty filter\r\n
0xb0000fac | SNASJob: Job [%1] matches the filter\r\n
0xb0000fad | Activity: Submission failed and will be rolled back\r\n
0xb0000fae | Activity: Remaining schedule executions %1\r\n
0xb0000faf | Activity: Remaining execution steps %1\r\n
0xb0000fb0 | Activity: Remaining delayed executions %1\r\n
0xb0000fb1 | Activity: Schedule was triggered for activity %1\r\n
0xb0000fb2 | Activity: Canceling pending requests submitted by job [%1]\r\n
0xb0000fb3 | Dispatcher: Subscribed for schedule %1\r\n
0xb0000fb4 | Dispatcher: Connectivity events already subscribed, ignoring request\r\n
0xb0000fb5 | Dispatcher: Starting connectivity events subscription\r\n
0xb0000fb6 | Dispatcher: Stoping connectivity events subscription\r\n
0xb0000fb7 | Dispatcher: Starting timer with frequency (%1)\r\n
0xb0000fb8 | Dispatcher: Stopping opportunistic timer (%1)\r\n
0xb0000fb9 | JobList: Adding job [%1] failed, error %2\r\n
0xb0000fba | JobList: Adding child activity failed, error %1\r\n
0xb0000fbb | JobList: Removing job [%1] from the list of jobs\r\n
0xb0000fbc | JobList: Job [%1] not found on the main list\r\n
0xb0000fbd | JobList: Job [%1] not found in the job->wrapper index\r\n
0xb0000fbe | Sched: Last request completed for job [%1]\r\n
0xb0000fbf | Sched: Iterating over job [%1]\r\n
0xb0000fc0 | Sched: Activity [%1] seems rogue and will be removed from the queue\r\n
0xb0000fc1 | Sched: Call to AboutToExecute failed, activity can't execute\r\n
0xb0000fc2 | Sched: Executing activity [%1]\r\n
0xb0000fc3 | Sched: Activity can't execute at the moment as determined by calling AboutToExecute\r\n
0xb0000fc4 | Sched: Activity [%1] needs DB update, updating\r\n
0xb0000fc5 | Sched: Incoming message ready to be processed\r\n
0xb0000fc6 | Sched: Processing incoming message\r\n
0xb0000fc7 | Sched: Job scheduler state change to 'uninitializing', winding down the message queue\r\n
0xb0000fc8 | Sched: All pre-existing messages has been processed\r\n
0xb0000fc9 | Sched: Job scheduler state change to 'shutting down', canceling all the jobs\r\n
0xb0000fca | Sched: Waiting for jobs to stop executing\r\n
0xb0000fcb | Sched: All jobs are deleted, final shutdown stage\r\n
0xb0000fcc | Sched: Job scheduler not initialized, ignoring\r\n
0xb0000fcd | Sched: Attempting to post message to scheduler while uninitializing\r\n
0xb0000fce | Sched: Ignoring request from canceled job\r\n
0xb0000fcf | Sched: Request completed for job [%1], %2\r\n
0xb0000fd0 | Sched: Job [%1] matches the filter and will be canceled\r\n
0xb0000fd1 | Sched: Trailing message processed\r\n
0xb0000fd2 | Job: Removing persistent job from the registry\r\n
0xb0000fd3 | Job: Invalid job state persisted (executing). Restoring to idle\r\n
0xb0000fd4 | Sched: Schedule %1 advised with cookie %2\r\n
0xb0000fd5 | Sched: Unadvising schedule %1\r\n
0xb0000fd6 | Sched: Received call from schedule %1\r\n
0xb0000fd7 | APHost: Calling CoFreeUnusedLibrariesEx\r\n
0xb0000fd8 | SNAS: Attempting to execute request with correlation id = %1\r\n
0xb0000fd9 | SNAS: SNAS instance invalid, actual %1\r\n
0xb0000fda | SNAS: Service was not initialized\r\n
0xb0000fdb | SNAS: Unadvising all notifications\r\n
0xb0000fdc | SNAS: Request group completed\r\n
0xb0001388 | SNService - Service Started\r\n
0xb0001389 | SNService - Failed to Initialize\r\n
0xb000138b | SNService - Critical error during SNService startup, HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb000138c | SNService - Request Manager Database failed to initialze, 0x%1\r\n
0xb000138d | SNService - Service Stopped\r\n
0xb000138e | SNService - Setting CPU rate cap to %1%%\r\n
0xb0001b59 | Job [%1] completed execution and will not be rescheduled\r\n
0xb0001b5a | Job [%1] failed, error [%2] and will remain inactive in the queue\r\n
0xb0001b5b | Job [%1] completed all requests for given state and will be rescheduled for execution, onlyWhenConnectionChanged [%2]\r\n
0xb0001b5c | Job Dispatcher exceeded maximum number of jobs and will cancel oldest jobs in the queue\r\n
0xb0001b5d | Job [%1] expired and will be removed from the queue\r\n
0xb0001b5e | Job [%1] SNJobType:[%2] Executing \r\n
0xb0001b5f | Synchronous failure in job execution for job [%1, SNJobType:%2], error [%3]\r\n
0xb0001b60 | Job [%1] failed to update in database, error [%2]\r\n
0xb0001b61 | Job [%1] of type %2 was submitted to Job Dispatcher\r\n
0xb0001b62 | Job [%1] failed to be submitted to Job Dispatcher, error %2\r\n
0xb0001b63 | Request for job [%1] failed to be submitted to Job Dispatcher, error %2\r\n
0xb0001b64 | Canceling job [%1]\r\n
0xb0001b65 | Job dispatcher received retry message from Connection Manager\r\n
0xb0001b66 | Job dispatcher received time based retry message and will retry failed jobs\r\n
0xb0001b67 | Job dispatcher received time based retry message and will retry failed jobs, error %1\r\n
0xb0001b6e | Unexpected job dispatcher failure occured, HRESULT: %1 Location: %2 Line Number: %3\r\n
0xb0001b6f | Failed to cancel job, hr = %1\r\n
0xb0001b70 | Failed to add job %1 to the queue, hr = %2\r\n
0xb0001b71 | Job [%1, SNJobType: %2] executed [%3] exceeding time limit; execution time = %4; (ActivityList entry = #%5/%6)\r\n
0xb0001b72 | Job [%1] seems rogue (exceeded max step limit) and will be removed from the queue\r\n
0xb0001b73 | Job [%1] seems rogue (exceeded delayed retry limit) and will be removed from the queue\r\n
0xb0001b74 | Job [%1, SNJobType: %2] executed [%3] within time limit; execution time = %4;  (ActivityList entry = #%5/%6)\r\n
0xb0001b75 | Completing job [%1, SNJobType:%2]\r\n
0xb0001b76 | Exceeded maximum number of jobs in the queue, will remove old job [%1]; (ActivityList entry #%2/%3)\r\n
0xb0001b77 | Added activity with handle [%1] to the submission list of activity with handle [%2]\r\n
0xb0001b78 | Added work with handle [%1] to the submission list of activity with handle [%2]\r\n
0xb0001b79 | Added request with handle [%1] to the submission list of activity with handle [%2]\r\n
0xb0001b7a | Removed submission with handle [%1] from the submission list of activity with handle [%2]\r\n
0xb0001b7b | Submission with handle [%1] completed but was not removed from submission list of activity with handle [%2]\r\n
0xb0001b7c | Child activity with id [%1] is about to be removed but it's parent activity is null\r\n
