# Condor Magic commands

## First submission

```
# hello-chtc.sub
# My very first HTCondor submit file
#
# Specify the HTCondor Universe (vanilla is the default and is used
#  for almost all jobs) and your desired name of the HTCondor log file,
#  which is where HTCondor will describe what steps it takes to run 
#  your job. Wherever you see $(Cluster), HTCondor will insert the 
#  queue number assigned to this set of jobs at the time of submission.
universe = vanilla
log = hello-chtc_$(Cluster).log
#
# Specify your executable (single binary or a script that runs several
#  commands), arguments, and a files for HTCondor to store standard
#  output (or "screen output").
#  $(Process) will be a integer number for each job, starting with "0"
#  and increasing for the relevant number of jobs.
executable = hello-chtc.sh
arguments = $(Process)
output = hello-chtc_$(Cluster)_$(Process).out
error = hello-chtc_$(Cluster)_$(Process).err
#
# Specify that HTCondor should transfer files to and from the
#  computer where each job runs. The last of these lines *would* be
#  used if there were any other files needed for the executable to use.
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
# transfer_input_files = file1,/absolute/pathto/file2,etc
#
# Tell HTCondor what amount of compute resources
#  each job will need on the computer where it runs.
request_cpus = 1
request_memory = 1GB
request_disk = 1MB
#
# Tell HTCondor to run 3 instances of our job:
queue 3
```

```
#!/bin/bash
#
# hello-chtc.sh
# My very first CHTC job
#
# print a 'hello' message to the job's terminal output:
echo "Hello CHTC from Job $1 running on `whoami`@`hostname`"
#
# keep this job running for a few minutes so you'll see it in the queue:
sleep 180
```

## Sleep


```
# sleep.sub -- simple sleep job

executable              = sleep.sh
log                     = sleep.log
output                  = outfile.txt
error                   = errors.txt
should_transfer_files   = Yes
when_to_transfer_output = ON_EXIT

request_gpus = 1
request_memory = 1GB
request_disk = 1MB

queue
```

```
#!/bin/bash
# file name: sleep.sh

TIMETOWAIT="6"
echo "sleeping for $TIMETOWAIT seconds"
/bin/sleep $TIMETOWAIT
```
