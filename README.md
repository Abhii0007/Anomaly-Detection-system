Intrusion Anomaly Detection System (IADS)

Project Authentication PASSWORD = 'abhi'

#-----------------------------------Overview--------------------------------
The Intrusion Anomaly Detection System (IADS) is a Python-based 
desktop application developed using the Qt Framework (PySide6) 
and Windows APIs. The system monitors suspicious or unauthorized 
activities on your device and alerts users via a Telegram bot using the BotFather API.

Key Features:
Real-time monitoring of network packets using scapy.
System resource monitoring (CPU, memory, etc.) using psutil.
Platform and environment information tracking using platform.
Alert system for suspicious activities via Telegram Bot API.

Tech Stack:-
Python Version: 3.11.0
Framework: Qt (PySide6, version 6.7.1)
OS Compatibility: Windows 10/11
Dependencies:
sys, time, threading, os, csv, requests, socket.
psutil for system monitoring.
scapy for network packet sniffing.
platform for system information.


#----------------------------------------Installation--------------------------------

Prerequisites
Ensure Python 3.11.0 is installed on your system. You can download it from Python.org.

Steps to Install Required Modules
Run the following commands in your terminal to install the required Python modules:

Install PySide6 (version 6.7.1):
pip install PySide6==6.7.1

Install psutil:
pip install psutil

Install scapy:
pip install scapy

Install requests:
pip install requests


Install platform (built-in):
No separate installation required. It is included in Python's standard library.

Install csv (built-in):
No separate installation required. It is included in Python's standard library.

#----------------------------------------How to Run--------------------------------

Clone or download the repository containing the project files.
Navigate to the project directory.
CMD = python main.py


#----------------------------------------How it works--------------------------------
Monitoring System:
The system continuously monitors the device’s resource usage, including CPU, memory, and running processes.
Network Activity Sniffing:
The system captures network packets to detect anomalies or unauthorized activities.
Alerting:
If suspicious activity is detected, an alert is sent to the user through Telegram using the BotFather API.



Telegram Alert connection using Telegram Bot:-
1.Open Telegram and search for BotFather.
2.Use /newbot command to create a new bot.
3.Copy the provided API token.
4.Paste the token into the designated section in your code.


Contribution:-
Contributions are welcome! If you want to enhance the system or fix issues, please fork the repository and submit a pull request.
