import smtplib
import time
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

# -------------------------
# YOUR DETAILS
# -------------------------
YOUR_EMAIL = "amanpandeyap1303@gmail.com"
YOUR_PASSWORD = "oggc xpem oqqs aogz"   # Gmail App Password

# ✅ Your Resume Link (NO ATTACHMENT)
RESUME_LINK = "https://portfolio-2pfo.onrender.com/static/Aman%20Pandey_3+%20Years_AWS_DevOps_Resume.pdf"

# -------------------------
# Recruiter Emails
# -------------------------
emails = [
    "pandeyaman1303@gmail.com",
    "u.getaman1303@gmail.com",
    "amanpandey4076@gmail.com",
    # Add more if needed
]

# -------------------------
# Send Email Function (Spam-Safe)
# -------------------------
def send_email(to_email):
    recipient_name = to_email.split("@")[0]

    subject = f"Aman Pandey | DevOps Engineer | Resume for {recipient_name}"

    plain_body = f"""Dear Hiring Manager,

Hope you're doing well.

I am applying for the DevOps Engineer position. I have 4+ years of experience in AWS, CI/CD, Linux, Docker, Kubernetes, and Cloud Automation.

You can download my resume from the link below:
{RESUME_LINK}

I would love to discuss how I can contribute to your organization.

Best Regards,  
Aman Kumar Pandey  
📞 +91-9555858544  
📧 amanpandeyap1303@gmail.com  
🌐 https://portfolio-2pfo.onrender.com/
"""

    html_body = f"""\
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <p>Dear Hiring Manager,</p>

        <p>
          I am applying for the <b>DevOps Engineer</b> position. I have <b>4+ years of experience</b> in AWS, CI/CD, Linux, Docker, Kubernetes, and Cloud Automation.
        </p>

        <p>
          👉 <a href="{RESUME_LINK}" target="_blank">Download My Resume</a>
        </p>

        <p>
          I would love to discuss how I can contribute to your organization.
        </p>

        <p>
          Best regards,<br>
          <b>Aman Kumar Pandey</b><br>
          📞 +91-9555858544<br>
          📧 <a href="mailto:amanpandeyap1303@gmail.com">amanpandeyap1303@gmail.com</a><br>
          🌐 <a href="https://portfolio-2pfo.onrender.com/" target="_blank">Portfolio</a>
        </p>
      </body>
    </html>
    """

    msg = EmailMessage()
    msg["From"] = f"Aman Kumar Pandey <{YOUR_EMAIL}>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg["Reply-To"] = YOUR_EMAIL
    msg["Message-ID"] = make_msgid(domain="portfolio-2pfo.onrender.com")
    msg["Date"] = formatdate(localtime=True)
    msg["X-Mailer"] = "Python smtplib"
    msg["List-Unsubscribe"] = f"<mailto:{YOUR_EMAIL}?subject=unsubscribe>"

    msg.set_content(plain_body)
    msg.add_alternative(html_body, subtype="html")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=60) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)

            # ✅ IMPORTANT: Envelope From set (Spam control)
            server.send_message(msg, from_addr=YOUR_EMAIL, to_addrs=[to_email])

        print(f"✅ Mail successfully sent to: {to_email}")
        return True

    except Exception as e:
        print(f"❌ Failed to send mail to {to_email}: {e}")
        return False


# -------------------------
# MAIN EXECUTION
# -------------------------
if __name__ == "__main__":

    print("✅ Sending test mail to yourself first...")
    send_email(YOUR_EMAIL)

    print("⏳ Waiting 5 seconds...")
    time.sleep(5)

    for email in emails:
        send_email(email)

        # ✅ 5 second gap between mails (Spam Safe)
        time.sleep(5)

    print("🎯 All mails processed successfully!")
