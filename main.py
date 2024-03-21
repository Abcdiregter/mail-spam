import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from concurrent.futures import ThreadPoolExecutor
import sys

def send_email(to_email, subject="Test Email", body="This is a test email"):
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your_email@example.com"
    smtp_password = "your_password"

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)

        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()

        print(f"Email sent to {to_email} successfully.")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def main():
    emails = []
    with open('list.txt', 'r') as file:
        emails = [line.strip() for line in file.readlines()]

    thread_count = input("Enter the number of threads: ")
    try:
        thread_count = int(thread_count)
    except ValueError:
        print("Please enter a valid integer for the number of threads.")
        sys.exit(1)

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.map(send_email, emails)

if __name__ == "__main__":
    main()
