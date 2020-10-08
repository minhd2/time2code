Problem Statement: You are given a contact list that has been messed up, spaces have been removed, with each attribute being in different columns. Each line contains usernames, phone_num, and start_date  

Input: File with the following content  
Tom415-123-456710/09/2019  
415-908-9999John10/10/2019  
10/10/2019549-000-1234Jack  
10/12/2019Mary312-999-1234  
Larry415-123-456910/31/2019  
415-908-1002Ken10/25/2019  
10/29/2019549-000-1231Pam  

Output: Create a new file with the folowing (sorted by name)  
Username Phone_num Start_date  
Jack 549-000-1234 10/10/2019  
John 415-908-9999 10/10/2019  
...  
...  

What knowledge is used for this:
1) Regex
2) String maniuplation
3) Outputting a file