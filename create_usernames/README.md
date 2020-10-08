Problem Statement: You are given a file with the contents of employee informatino, first name, last name, employeeID, startdate. You want to add another column containing the username, if there is collision then increment the end with the next available number. Output everything into a new file.



input: a file with following content
 
Firstname Lastname EmployeeID StartDate
Kasey Cook 1 10/13/2000
Alya Ellis 2 10/14/2000
Raisa Grimes 3 10/15/2000
Kareem Dalby 4 10/16/2000
Karter Cook 5 10/17/2000
Kavan Cook 6 10/18/2000
Abubakar Parsons 7 10/19/2000
Hope Ortega 8 10/20/2000
Ty Neale 9 10/21/2000
Harun Wu 10 10/22/2000
 
output: a new file with username at the last column, the username is the first letter of the user and the lastname (e.g. Kasey Cook -> kcook). If there's collision for usernames, the new one should add the next available integer to its end (e.g. kcook, kcook2, kcook3) (we skip 1 to avoid confusion)
 
Firstname Lastname EmployeeID StartDate Username
Kasey Cook 1 10/13/2000 kcook
Alya Ellis 2 10/14/2000 aellis
Raisa Grimes 3 10/15/2000 rgrimes
Kareem Dalby 4 10/16/2000 kdalby
Karter Cook 5 10/17/2000 kcook2
Kavan Cook 6 10/18/2000 kcook3
Abubakar Parsons 7 10/19/2000 aparsons
Hope Ortega 8 10/20/2000 hortega
Ty Neale 9 10/21/2000 tneale
Harun Wu 10 10/22/2000 hwu
