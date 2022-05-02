#!/bin/bash

export SSHPASS=raspberry

sshpass -e rsync -avz -e ssh pi@10.32.26.20:/home/pi/Desktop/Delay_Statistics/TCP/TCP_Delay_Stats_Integrate_DB/Multiuser/Delay_Stats/Twinkle_Delay_Stats_Database.db /home/pi/Desktop/Delay_Statistics/TCP/TCP_Delay_Stats_Integrate_DB/Delay_Statistics/ 

sshpass -e rsync -avz -e ssh pi@10.32.26.20:/home/pi/Desktop/Delay_Statistics/TCP/TCP_Delay_Stats_Integrate_DB/Multiuser/Delay_Stats/checkpoint_delay.npy /home/pi/Desktop/Delay_Statistics/TCP/TCP_Delay_Stats_Integrate_DB/Delay_Statistics/ 

