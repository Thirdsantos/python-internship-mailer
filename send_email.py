"""
    Developer: Alfred
    Purpose: Tired of emailing them one by one lol
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

# Email account info (DO NOT hardcode real credentials in public code)
YOUR_EMAIL = ""          # e.g. "youremail@gmail.com"
APP_PASSWORD = ""        # e.g. "your16charapppassword"

CSV_FILE = "company.csv"  # default CSV filename


def send_internship_emails():
    """
    Reads a CSV file with columns: company,email
    and sends a personalized internship inquiry email to each address.
    """
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # expects headers: company,email

        for row in reader:
            company = row.get("company", "").strip()
            email = row.get("email", "").strip()

            if not company or not email:
                print(f"Skipping row with missing data: {row}")
                continue

            # 1. Create the email object
            msg = MIMEMultipart()
            msg["From"] = YOUR_EMAIL
            msg["To"] = email
            msg["Subject"] = "Internship Inquiry – Software / Machine Learning"

            # 2. Email body template – users can customize this
            body = f"""Dear {company} Team,

My name is [Your Name], and I am a student currently seeking an internship opportunity to grow in software development, machine learning, and cloud technologies. I would like to ask if {company} has any available internship roles for a Software Developer Intern or Machine Learning Intern, now or in the near future.

I’ve attached my CV for your reference. You may also learn more about me here:
LinkedIn: [your LinkedIn URL]
Portfolio: [your portfolio URL]
GitHub: [your GitHub URL]

Thank you for your time and consideration. I look forward to the possibility of contributing to your team.

Best regards,
[Your Name]
"""

            msg.attach(MIMEText(body, "plain"))

            # 3. Send via Gmail SMTP
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(YOUR_EMAIL, APP_PASSWORD)
                    server.send_message(msg)
                print(f"Email sent successfully to {company} ({email})")
            except Exception as e:
                print(f"Error sending to {company} ({email}): {e}")


if __name__ == "__main__":
    send_internship_emails()
