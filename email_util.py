import yagmail
import os

def send_email(subject, body, attachments=[]):
    sender_email = "ichigoo2224@gmail.com"
    app_password = "zrkk aovq kgmc kbmh"
    receiver_email = "ichigoo2224@gmail.com"

    try:
        yag = yagmail.SMTP(sender_email, app_password)

        valid_attachments = [f for f in attachments if os.path.exists(f)]

        print(f"📎 Valid attachments: {valid_attachments}")

        if not valid_attachments:
            print("⚠️ No valid attachments to send.")
        else:
            yag.send(
                to=receiver_email,
                subject=subject,
                contents=body,
                attachments=valid_attachments
            )
            print("✅ Email sent with attachment!")

    except Exception as e:
        print("❌ Failed to send email:", e)
