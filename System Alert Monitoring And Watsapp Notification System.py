import tkinter as tk
import psutil
import mysql.connector
import pywhatkit
from datetime import datetime

window = tk.Tk()
window.title("System Monitoring Alert System")
window.geometry("600x750")

title = tk.Label(
    window,
    text="System Alert Monitoring System",
    font= ("Arial", 18, "bold")
)

title.pack(pady=20)

phone_label = tk.Label(
    window,
    text="Watsapp Number:"
)
phone_label.pack()

phone_entry = tk.Entry(
    window,
    width=40
)
phone_entry.pack(pady=5)

cpu_label = tk.Label(
    window,
    text="CPU Alert Limit (%):"
)
cpu_label.pack()

cpu_entry = tk.Entry(
    window,
    width=40
)
cpu_entry.pack(pady=5)

ram_label = tk.Label(
    window,
    text="RAM Alert Limit (%):"
)
ram_label.pack()

ram_entry = tk.Entry(
    window,
    width=40
)
ram_entry.pack(pady=5)

disk_label = tk.Label(
    window,
    text="DISK Alert Limit(%):"
)
disk_label.pack()

disk_entry = tk.Entry(
    window,
    width=40
)
disk_entry.pack(pady=5)

mysql_label = tk.Label(
    window,
    text="Mysql Password:"
)
mysql_label.pack()

mysql_entry = tk.Entry(
    window,
    width=40,
    show="*"
)
mysql_entry.pack(pady=5)

cpu_usage = tk.Label(
    window,
    text="CPU Usage:-- %",
    font=("Arial",12)
)

cpu_usage.pack(pady=8)

ram_usage = tk.Label(
    window,
    text="RAM Usage:-- %",
    font=("Arial",12)
)
ram_usage.pack(pady=8)

disk_usage = tk.Label(
    window,
    text="DISK Usage:-- %",
    font=("Arial",12)
)
disk_usage.pack(pady=8)

status_label = tk.Label(
    window,
    text="Status: Waiting...",
    font=("Arial",12, "bold")
)
status_label.pack(pady=10)

connection= None

last_alert =""

def send_watsapp(message):

    phone = phone_entry.get().strip()

    if phone == "":
        status_label.config(text="Please enter WhatsApp number")
        return

    try:
        pywhatkit.sendwhatmsg_instantly(
            phone,
            message,
            wait_time=20,
            tab_close=False
        )

        status_label.config(
            text="WhatsApp message sent successfully"
        )

    except Exception as e:

        status_label.config(
            text="WhatsApp message failed"
        )

        print("WhatsApp Error:", e)
        
def connect_database():

    global connection

    password = mysql_entry.get()


    try:

        connection = mysql.connector.connect(
            host ="localhost",
            user = "root",
            password= password
        )

        mycursor = connection.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS system_alert_db")

        mycursor.execute("USE system_alert_db")

        mycursor.execute("""
                CREATE TABLE IF NOT EXISTS System_Monitoring(
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    cpu_usage DECIMAL(5,2),
                    ram_usage DECIMAL(5,2),
                    disk_usage DECIMAL(5,2),
                    alert_type VARCHAR(100),
                    alert_message VARCHAR(225),
                    alert_time DATETIME
                )
           """)
        connection.commit()

        mycursor.close()

        status_label.config(
            text ="Database Connected Successfully"
        )

        monitor_system()

    except mysql.connector.Error as e:
            status_label.config(
                text ="Database connection Failed"
            )

            print("Mysql Error:",e)

def monitor_system():

    global last_alert

    if connection is None:

        return
    try:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        cpu_limit = float(cpu_entry.get())
        ram_limit = float(ram_entry.get())
        disk_limit = float(disk_entry.get())

        cpu_usage.config(
            text =f"CPU usage:{cpu}%"
        )

        ram_usage.config(
            text =f"RAM usage:{ram}%"
        )

        disk_usage.config(
            text =f"DISK usage:{disk}%"
        )


        alerts=[]

        if cpu >= cpu_limit:
            alerts.append("CPU HIGH")

        if ram >= ram_limit:
            alerts.append("RAM HIGH")

        if disk >= disk_limit:
            alerts.append("DISK HIGH")

        if alerts:

            alert_type =",".join(alerts)


            alert_message =(f"system alert:{alert_type}")

            status_label.config(
                text = f"Alert: {alert_type}"
            )

            if alert_type != last_alert:

                watsapp_message =(
                    "System Alert\n"
                    f"CPU usage: {cpu}%\n"
                    f"RAM usage: {ram}%\n"
                    f"DISK usage: {disk}%\n"
                    f"Alert: {alert_type}\n"
                    f"Time: {datetime.now()}"
                )

                send_watsapp(watsapp_message)

                last_alert = alert_type
                    

        else:

            alert_type = "NORMAL"

            alert_message = "system usage is normal"

            status_label.config(
                text ="status: system normal"
            )

        mycursor = connection.cursor()

        query = (""" INSERT INTO system_monitoring(cpu_usage, ram_usage, disk_usage,alert_type, alert_message,alert_time)VALUES(%s,%s,%s,%s,%s,%s)""")

        values = (
            cpu,
            ram,
            disk,
            alert_type,
            alert_message,
            datetime.now()
        )

        mycursor.execute(query,values)

        connection.commit()

        mycursor.close()

        window.after(2000, monitor_system)

    except ValueError:

            status_label.config(
                text ="please enter valid limit values"
            )
            

button = tk.Button(
    window,
    text ="Start Monitoring",
    command = connect_database,
    width = 20,
    height =2
)

button.pack(pady=20)

window.mainloop()

        
    

        

    





