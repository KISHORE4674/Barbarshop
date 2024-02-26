import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import time

def send_email(receiver_email, subject, message):
    # Set up the SMTP server
    smtp_server = 'your_smtp_server_address'
    port = 587  # Change the port according to your SMTP server configuration
    sender_email = 'your_email@example.com'
    password = 'your_email_password'

    # Create a MIMEText object to represent the email message
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject
    email_message.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_message.as_string())

def main():
    # Set the details for the email reminder
    receiver_email = input("Enter your email address: ")
    subject = "Barber Shop Appointment Reminder"
    message = "This is a reminder for your upcoming appointment at the barber shop."

    # Get the date and time for the appointment
    appointment_date = input("Enter the date of your appointment (YYYY-MM-DD): ")
    appointment_time = input("Enter the time of your appointment (HH:MM AM/PM): ")
    appointment_datetime = datetime.strptime(appointment_date + '12_03_2024 ' + appointment_time, '%Y-%m-%d %I:%M %p')

    # Set the reminder time
    reminder_time = appointment_datetime - timedelta(days=1)  # Send the reminder 1 day before the appointment

    # Get the current time
    current_time = datetime.now()

    # Calculate the time difference to set the reminder
    time_difference = reminder_time - current_time

    # If the reminder time has not passed, schedule the reminder
    if time_difference.days >= 0:
        print(f"Reminder set for {reminder_time}")
        time.sleep(time_difference.total_seconds())
        send_email(receiver_email, subject, message)
        print("Reminder email sent successfully.")
    else:
        print("The appointment time has already passed. No reminder set.")

if __name__ == "__main__":
    main()
