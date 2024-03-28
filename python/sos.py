
import smtplib
import getpass

def send_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
    finally:
        server.quit()

def main():
    # Replace with your email credentials and receiver's email address
    sender_email = "your_email@gmail.com"
    sender_password = getpass.getpass("Enter your email password: ")
    receiver_email = "receiver_email@example.com"

    subject = "Emergency SOS Alert!"
    body = "This is an emergency SOS alert. Immediate action may be required."

    send_email(sender_email, sender_password, receiver_email, subject, body)

if __name__ == "__main__":
    main()
