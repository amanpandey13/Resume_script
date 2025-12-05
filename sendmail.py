import smtplib
import time
import os
import mimetypes
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

# -------------------------
# YOUR DETAILS - update these
# -------------------------
YOUR_EMAIL = "amanpandeyap1303@gmail.com"
YOUR_PASSWORD = "oggc xpem oqqs aogz"  # App password ok for Gmail
RESUME_PATH = "Aman Pandey_4+ Years_AWS_DevOps_updated_Resume.pdf"

# Recruiter emails list (send individually)
emails = [
    "u.getaman1303@gmail.com",
    "ugetaman13@gmail.com",
    "amanpandey4076@gmail.com",
    "pandeyaman1303@gmail.com"
]

# Subject & plain text + HTML body (kept simple & professional)
subject = "Aman Pandey — AWS / DevOps Engineer (4+ years) — Resume"
plain_body = """Dear Hiring Manager,

Hope you're doing well.

I am writing to express my interest in the DevOps Engineer position at your esteemed organization. Please find attached my resume for your kind consideration. I believe my skills in AWS, CI/CD, automation, and infrastructure management make me a strong candidate for this role.

I would be grateful for the opportunity to discuss how I can contribute to your team. Please let me know if any further information or documents are required.

Thank you for your time and consideration.

Best regards,
Aman Kumar Pandey
+91-9555858544
amanpandeyap1303@gmail.com
Portfolio: https://portfolio-2pfo.onrender.com/
"""

html_body = """\
<html>
  <body>
    <p>Dear Hiring Manager,</p>
    <p>Hope you're doing well.</p>
    <p>I am writing to express my interest in the DevOps Engineer position at your esteemed organization. Please find attached my resume for your kind consideration. I believe my skills in AWS, CI/CD, automation, and infrastructure management make me a strong candidate for this role. 
    </p>
    <p>I would be grateful for the opportunity to discuss how I can contribute to your team. Please let me know if any further information or documents are required.
    </p>
    <p>Thank you for your time and consideration.</p>
    
    <p>Regards,<br>
       <b>Aman Kumar Pandey</b><br>
       +91-9555858544<br>
       <a href="mailto:amanpandeyap1303@gmail.com">amanpandeyap1303@gmail.com</a><br>
       <a href="https://portfolio-2pfo.onrender.com/">Portfolio</a>
    </p>
  </body>
</html>
"""

# -------------------------
# Utility to attach file safely
# -------------------------
def attach_file(msg, path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Resume not found: {path}")
    ctype, encoding = mimetypes.guess_type(path)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"
    maintype, subtype = ctype.split("/", 1)
    with open(path, "rb") as f:
        msg.add_attachment(f.read(), maintype=maintype, subtype=subtype,
                           filename=os.path.basename(path))

# -------------------------
# Send email function
# -------------------------
def send_email(to_email):
    msg = EmailMessage()
    # Friendly display name + email (use a real name)
    msg["From"] = "Aman Kumar Pandey <{}>".format(YOUR_EMAIL)
    msg["To"] = to_email
    msg["Subject"] = subject
    msg["Reply-To"] = YOUR_EMAIL
    # Useful headers that can help deliverability/tracing
    msg["Message-ID"] = make_msgid(domain="portfolio-2pfo.onrender.com")
    msg["Date"] = formatdate(localtime=True)
    msg["X-Mailer"] = "Python smtplib"
    # List-Unsubscribe (helps mailbox providers); mailto fallback
    msg["List-Unsubscribe"] = "<mailto:{}?subject=unsubscribe>".format(YOUR_EMAIL)

    # Add both plain and HTML alternatives
    msg.set_content(plain_body)
    msg.add_alternative(html_body, subtype="html")

    # Attach resume (optional: consider sending link instead of attachment)
    attach_file(msg, RESUME_PATH)

    # Send via Gmail SMTP SSL
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=60) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.send_message(msg)
        print(f"✔ Mail sent: {to_email}")
        return True
    except Exception as e:
        print(f"✖ Failed to send to {to_email}: {e}")
        return False

# -------------------------
# Main: send to all with delay
# -------------------------
if __name__ == "__main__":
    # Send a test to yourself first to check spam/junk
    print("Sending test mail to yourself first...")
    send_email(YOUR_EMAIL)
    # small pause
    time.sleep(5)

    for email in emails:
        success = send_email(email)
        # polite delay between sends reduces spam flags
        time.sleep(6)
