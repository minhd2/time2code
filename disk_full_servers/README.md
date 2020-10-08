Problem Statement: You are given a log file with server, date, and disk_uage. Please output names of servers with it's disk_usage if it is over 85%.

Input: log file with content like
server1 07-10-2020 disk_usage 90%
server2 07-10-2020 disk_usage 45.5%
server3 07-10-2020 disk_usage 65%
server4 07-10-2020 disk_usage 23.5%
server5 07-10-2020 disk_usage 96.5%
...
 
Output: print out names of servers and its disk_usage whose disk_usage is over 85%
server1, 90%
server5, 96.5%
 
Note: the percentages can be integer (e.g. 50%) or a decimal number with one fraction digit (e.g. 45.5%)

Knowledge Used:
1) Parsing through log with conditional

