# System Alert Monitoring and WhatsApp Notification System

## 📌 Project Overview

The **System Alert Monitoring and WhatsApp Notification System** is a Python-based desktop application that monitors CPU, RAM, and disk usage in a computer system.

The application allows users to set custom alert limits for CPU, RAM, and disk usage. When resource usage reaches or exceeds the specified limits, the application generates an alert and attempts to send a WhatsApp notification containing the current system usage details.

The application also integrates with a MySQL database to store system monitoring records, alert types, alert messages, and timestamps for future reference.

## 🎯 Objectives

- To monitor CPU, RAM, and disk usage.
- To set custom resource usage alert limits.
- To generate alerts when resource usage exceeds configured limits.
- To send system alert notifications through WhatsApp.
- To store monitoring records and alert details in a MySQL database.
- To develop a simple and user-friendly desktop application.
- To gain practical experience in Python programming, GUI development, and database connectivity.

## ✨ Features

- **Real-Time Resource Monitoring:** Monitors CPU, RAM, and disk usage periodically.
- **Custom Alert Limits:** Allows users to configure individual CPU, RAM, and disk thresholds.
- **WhatsApp Notifications:** Attempts to send alerts through WhatsApp when configured limits are reached.
- **MySQL Integration:** Automatically creates the database and monitoring table if they do not exist.
- **Monitoring History:** Stores resource usage values, alert information, and timestamps.
- **Graphical User Interface:** Uses Tkinter to provide a simple desktop interface.
- **Password Masking:** Hides the MySQL password entered in the application.
- **Periodic Updates:** Repeats system monitoring while the application is running.
- **Alert Status Display:** Displays detected alerts, such as CPU HIGH, RAM HIGH, and DISK HIGH.
- **Normal Status Tracking:** Stores records when system resource usage is within the configured limits.

## 🛠️ Technologies Used

- **Python** – Core application programming.
- **Tkinter** – Desktop graphical user interface.
- **psutil** – Collects CPU, RAM, and disk usage information.
- **MySQL** – Stores system monitoring records.
- **mysql-connector-python** – Connects Python with MySQL.
- **PyWhatKit** – Attempts to send WhatsApp notifications.
- **datetime** – Records the date and time of monitoring events.


## 📋 System Requirements

- Python 3.x
- MySQL Server
- Internet connection for WhatsApp notifications
- A WhatsApp account and WhatsApp Web access
- A computer capable of running Python desktop applications

## 📦 Installation

### 1. Install Python

Install Python 3.x on your computer and make sure Python is available from Command Prompt or the terminal.

### 2. Install the Required Libraries

Open Command Prompt or a terminal and execute:

```bash
pip install psutil mysql-connector-python pywhatkit
```

### 3. Configure MySQL

Make sure your MySQL Server is running.

The application automatically creates the following database and table after a successful connection:

- **Database:** `system_alert_db`
- **Table:** `system_monitoring`

Enter your MySQL root password in the application's MySQL Password field.

### 4. Run the Application

Open the folder containing the Python source file and execute:

```bash
python "System Alert Monitoring and WhatsApp Notification System.py"
```

Make sure the command matches the actual filename saved on your computer.

## ⚙️ How the Project Works

1. Launch the System Alert Monitoring application.
2. Enter the WhatsApp phone number with the appropriate country code.
3. Set the CPU usage alert limit.
4. Set the RAM usage alert limit.
5. Set the disk usage alert limit.
6. Enter the MySQL password.
7. Click the **Start Monitoring** button.
8. The application connects to MySQL and creates the database and table if necessary.
9. CPU, RAM, and disk usage values are collected and displayed in the GUI.
10. The application compares the current usage values against the configured limits.
11. If a limit is reached or exceeded, the application identifies the corresponding alert type.
12. The application attempts to send the alert details through WhatsApp.
13. Monitoring records are inserted into the MySQL database.
14. The monitoring process repeats periodically while the application remains running.

## 🗄️ Database Structure

**Database Name:** `system_alert_db`

**Table Name:** `system_monitoring`

| Column | Description |
|---|---|
| `id` | Unique record identifier generated automatically |
| `cpu_usage` | CPU usage percentage |
| `ram_usage` | RAM usage percentage |
| `disk_usage` | Disk usage percentage |
| `alert_type` | Alert category or NORMAL status |
| `alert_message` | Description of the alert or normal status |
| `alert_time` | Date and time of the monitoring record |

### SQL Query to View Monitoring Records

Use the following SQL commands in MySQL Workbench to view the stored monitoring data:

```sql
USE system_alert_db;

SELECT * FROM system_monitoring;
```

### Example Alert Types

- `NORMAL` – System usage is within the configured limits.
- `CPU HIGH` – CPU usage has reached or exceeded its configured limit.
- `RAM HIGH` – RAM usage has reached or exceeded its configured limit.
- `DISK HIGH` – Disk usage has reached or exceeded its configured limit.
- Multiple alert types can appear together when more than one limit is exceeded.

## 📊 Expected Results

- Displays CPU, RAM, and disk usage percentages in the application window.
- Detects high resource usage based on user-defined limits.
- Displays the detected alert status in the GUI.
- Attempts to send WhatsApp notifications for detected alerts.
- Stores normal and alert monitoring records in MySQL.
- Records resource usage values, alert types, alert messages, and timestamps.
- Provides a simple interface for monitoring system resource usage.

## 🔐 Security Considerations

- The MySQL password is hidden while being entered into the application.
- Avoid publishing personal WhatsApp numbers or database passwords in public screenshots or source code.
- For production applications, use a dedicated MySQL account with limited permissions instead of the root account.
- Do not store database passwords directly in publicly accessible source code.

## ⚠️ Important Notes

- WhatsApp notifications depend on WhatsApp Web access, browser interaction, and internet connectivity.
- Enter valid numeric values for all alert limits.
- The application uses the `/` disk path for disk usage monitoring. This may need adjustment for other operating systems.
- The current implementation suppresses repeated WhatsApp notifications while the alert type remains unchanged.
- WhatsApp notification delivery may fail if WhatsApp Web is unavailable or the sending process encounters an error.
- Monitoring records are stored in MySQL after each successful monitoring cycle.
- The application is intended for educational and practical learning purposes.

## 👩‍💻 Author

**Reeshma Devi R**

Data Analytics Student

**Skills Used:** Python | MySQL | Tkinter | System Monitoring | WhatsApp Notifications

## 🎓 Project Purpose

This project was developed as a practical learning project to gain hands-on experience in Python programming, desktop GUI development, system resource monitoring, MySQL database connectivity, and WhatsApp notifications.

It demonstrates how system resource monitoring can be combined with database storage and messaging notifications to create a simple desktop monitoring solution.

**Project:** System Alert Monitoring and WhatsApp Notification System

**Developed using:** Python, Tkinter, MySQL, psutil, and PyWhatKit
