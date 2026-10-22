# System Alert Monitoring and WhatsApp Notification System

## Project Overview

The **System Alert Monitoring and WhatsApp Notification System** is a Python-based desktop application that monitors CPU, RAM, and disk usage in real time. It sends WhatsApp notifications when system resource usage exceeds the user-defined alert limits and stores monitoring details in a MySQL database.

The application uses Tkinter to provide a graphical user interface, Psutil to monitor system resources, PyWhatKit to send WhatsApp notifications, and MySQL to store system monitoring records.

## Features

- Real-Time CPU Usage Monitoring
- RAM Usage Monitoring
- Disk Usage Monitoring
- Custom CPU, RAM, and Disk Alert Limits
- WhatsApp Alert Notifications
- MySQL Database Integration
- Automatic Storage of Monitoring Records
- Graphical User Interface Using Tkinter
- MySQL Password Masking
- Automatic Database and Table Creation

## Technologies Used

- Python
- Tkinter
- MySQL
- MySQL Connector
- Psutil
- PyWhatKit
- Datetime

## Database

**Database Name:** `system_alert_db`

**Table Name:** `System_Monitoring`

The database stores the following information:

- CPU usage percentage
- RAM usage percentage
- Disk usage percentage
- Alert type
- Alert message
- Alert date and time

The program automatically creates the database and monitoring table when the MySQL connection is successful.

## How to Run

1. Install Python and MySQL on your computer.
2. Install the required Python packages using the following command:

   `pip install psutil mysql-connector-python pywhatkit`

3. Ensure that the MySQL server is running.
4. Open the Python source code in Python IDLE or a code editor.
5. Run the program.
6. Enter your WhatsApp number, CPU alert limit, RAM alert limit, disk alert limit, and MySQL password.
7. Click **Start Monitoring** to begin monitoring the system.
8. When any resource usage reaches or exceeds its configured limit, the application attempts to send a WhatsApp alert and saves the monitoring details in MySQL.

## Source Code

Click the link below to view the complete Python source code.

[**View Python Source Code**](https://github.com/Reeshurajesh/System-Alert-Monitoring-And-watsapp-Notification-System/blob/5d6e3ec2472812dd942110bf3d10940cd6abe49f/System%20Alert%20Monitoring%20And%20Watsapp%20Notification%20System.py)

## Project Screenshots

### 1. System Monitoring Interface

![System Monitoring Interface](gui-output.png)

### 2. WhatsApp Alert Notification

![WhatsApp Alert Notification](whatsapp-alert.png)

### 3. MySQL Normal Records

![MySQL Normal Records](mysql-normal-records.png)

### 4. MySQL Alert Records

![MySQL Alert Records](mysql-alert-records.png)

## Author

**Reeshma Devi R**
