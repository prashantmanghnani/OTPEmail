import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
import tkinter as tk
from tkinter import messagebox, ttk

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
        smtp_username = "prashantmanghnani40@gmail.com"
        smtp_password = "veni jbxp zjtk xxjw"

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=context)
        server.login(smtp_username, smtp_password)

        # Compose the email message
        message = MIMEMultipart()
        message["From"] = smtp_username
        message["To"] = smtp_username  # Send to the same email
        message["Subject"] = "OTP Verification"
        body = f"Your OTP is: {generated_otp}"
        message.attach(MIMEText(body, "plain"))

        # Send the email
        server.sendmail(smtp_username, smtp_username, message.as_string())  # Sending to the same email
        messagebox.showinfo("OTP Sent", f"OTP sent to {email}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

    finally:
        server.quit()

# Function to verify if the entered OTP matches the generated OTP
def verify_otp():
    global generated_otp
    user_otp = otp_entry.get()
    if user_otp == generated_otp:
        messagebox.showinfo("OTP Verification", "OTP verified. Access granted.")
    else:
        messagebox.showerror("OTP Verification", "Invalid OTP. Access denied.")
        restart_process()

# Function to restart the OTP verification process
def restart_process():
    email_entry.delete(0, tk.END)
    otp_entry.delete(0, tk.END)
    global generated_otp
    generated_otp = None

# Create the main window
window = tk.Tk()
window.title("OTP Verification System")
window.geometry("900x400")
window.configure(bg="#f0f0f0")

# Create a style object
style = ttk.Style()
style.theme_use("clam")

# Create a frame for the input fields
input_frame = ttk.Frame(window, padding=20)
input_frame.pack(pady=20)

# Create labels and entry fields
email_label = ttk.Label(input_frame, text="Email Address:", font=("Helvetica", 12))
email_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
email_entry = ttk.Entry(input_frame, font=("Helvetica", 12))
email_entry.grid(row=0, column=1, padx=10, pady=10)

otp_label = ttk.Label(input_frame, text="OTP:", font=("Helvetica", 12))
otp_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
otp_entry = ttk.Entry(input_frame, font=("Helvetica", 12))
otp_entry.grid(row=1, column=1, padx=10, pady=10)

# Create buttons
button_frame = ttk.Frame(window)
button_frame.pack(pady=20)

send_button = ttk.Button(button_frame, text="Send OTP", command=lambda: send_otp(email_entry.get()), style="Accent.TButton")
send_button.grid(row=0, column=0, padx=10)

verify_button = ttk.Button(button_frame, text="Verify OTP", command=verify_otp, style="Accent.TButton")
verify_button.grid(row=0, column=1, padx=10)

# Run the main loop
window.mainloop()
