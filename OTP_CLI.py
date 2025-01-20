import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string

# Function to generate a random 6-digit OTP
def generate_otp():
    otp = ''.join(random.choices(string.digits, k=6))
    return otp

# Function to send the OTP to the user's email
def send_otp(email):
    global generated_otp
    generated_otp = generate_otp()
    try:
        smtp_server = "smtp.gmail.com"  # Correct SMTP server address
        smtp_port = 587  # Correct port for STARTTLS
        smtp_username = "your_email@gmail.com"  # Replace with your email
        smtp_password = "your_app_specific_password"  # Replace with your app password

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=context)
        server.login(smtp_username, smtp_password)

        # Compose the email message
        message = MIMEMultipart()
        message["From"] = smtp_username
        message["To"] = email
        message["Subject"] = "OTP Verification"
        body = f"Your OTP is: {generated_otp}"
        message.attach(MIMEText(body, "plain"))

        # Send the email
        server.sendmail(smtp_username, email, message.as_string())
        print(f"OTP sent to {email}")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        server.quit()

# Function to verify if the entered OTP matches the generated OTP
def verify_otp(user_otp):
    global generated_otp
    if user_otp == generated_otp:
        print("OTP verified. Access granted.")
    else:
        print("Invalid OTP. Access denied.")

# Main flow
if __name__ == "__main__":
    email = input("Enter your email address: ")
    send_otp(email)

    # Simulate OTP input and verification
    user_otp = input("Enter the OTP sent to your email: ")
    verify_otp(user_otp)
