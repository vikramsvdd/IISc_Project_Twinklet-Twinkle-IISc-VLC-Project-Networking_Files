# Vikram-twinkle-Networking-files

This is just the networking part of my IISc project , I did the smartphone-flashlight Project after i first completed this!







The Process is as follows, as soon as the client/reciever (vikram-client-1.py) recieves a data packet (in reality client recieves data from twinklet, but in the client program, i voluntarily give a data) , The  Local Server  is the program (vikram-local-server-1.py) and central server is the program  (vikram-central-server-1.py), in my case the local server and central servers are Raspberry pis. All the 3 machines (the client, local and central server) are connected through Internet using SSH protocol.  So firstly client transfers message to the local server and in my case, local server just acts as a dumb machine and just routes the message to the central-server, which is the CPU of the entire network. Central Sever recieves the data, cross-checks with its list of employees database (winkle.db , winkle.py is the python file that generates the database) and if the employee is not present in the db, it returns a negative authentication status to local sever , which in turn passes that to the client. On the other hand, if the employee is a valid one, then the central sever marks attendance for that particular date for that particular employee and returns a postive authentication to local server and in turn to client and the reciever interfaces with the physical lock and opens the door. Also, there are several functions assisting the central server in the database management , like attendance.py and attendancefunctions.py. The gui.py functions gives an user-friendly view to help administrators process the attendance activities. It has 3 options, 1.Real time display: It displays the current month database and facilitates a monitoring of the latest activities that had taken place. 2.Query Database : Filter some specific content to your desire from the database and 3.Generate Attendance Sheet : For a particular month or a specific period. 

I also tried the same process by using RDP instead of SSH and experienced the same process.
