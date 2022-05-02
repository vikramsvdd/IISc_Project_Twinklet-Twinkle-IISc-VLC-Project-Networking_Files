#!/bin/bash

export SSHPASS=raspberry

sshpass -e rsync -avz -e ssh pi@10.32.26.20:/home/pi/Desktop/Integrate_DB_UDP/Multiuser/Delay_Stats/Twinkle_Delay_Stats_Database.db /home/pi/Desktop/Integrate_DB_UDP/Delay_Statistics/ 

sshpass -e rsync -avz -e ssh pi@10.32.26.20:/home/pi/Desktop/Integrate_DB_UDP/Multiuser/Delay_Stats/checkpoint_delay.npy /home/pi/Desktop/Integrate_DB_UDP/Delay_Statistics/ 

