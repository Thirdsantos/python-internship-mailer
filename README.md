# Bulk Internship Email Sender

I made this small project because I got **tired of emailing companies one by one** just to ask about internship opportunities. 😅  

So instead of manually copy–pasting the same message again and again, I wrote a **Python script that reads a CSV file and sends personalized emails** to multiple companies automatically.

I personally use this tool for my own internship outreach, and I decided to share it in case it helps other students too.

---

## ✨ What this script does

- Reads a CSV file containing:
  - `company` – company name  
  - `email` – company HR / careers / contact email  
- For each row, it:
  - Builds a **personalized email** (e.g. “Dear Trainocate Philippines Team”)
  - Sends the email using **Gmail SMTP** + **App Password**
- Prints in the terminal whether the email was sent successfully or if there was an error.

---

## 🧰 Tech Stack

- **Language:** Python 3.x  
- **Email:** Gmail SMTP (`smtp.gmail.com` with SSL)  
- **Libraries used (standard library only):**
  - `smtplib`
  - `email.mime` (`MIMEText`, `MIMEMultipart`)
  - `csv`

No external packages required. ✅

---

## ✅ Requirements

Before using this script, you need:

1. **Python 3.x** installed  
2. A **personal Gmail account**  
3. **2-Step Verification** enabled on your Google account  
4. A **Gmail App Password** generated  
5. A CSV file with your target companies and their emails  

---

## 🔐 Creating a Gmail App Password (Short Version)

1. Go to your **Google Account** → **Security**.  
2. Turn on **2-Step Verification** if it’s not yet enabled.  
3. After that, go back to **Security** and click **App passwords**.  
4. Choose:
   - App: `Mail`
   - Device: your current device (or any)
5. Click **Generate**.  
6. Copy the 16-character password (without spaces) — this is your `APP_PASSWORD`.

⚠️ **Never push your real email or app password to GitHub.**

---

## 📂 Project Structure

Example layout:

```text
.
├── send_email.py        # The Python script
├── company.csv    # CSV file with company names and emails
└── README.md
