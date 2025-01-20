# OTP Verification System

This repository contains two Python scripts that implement an OTP (One-Time Password) verification system. The first script generates and sends a 6-digit OTP to a user's email, and the second script provides a graphical user interface (GUI) for OTP input and verification using `tkinter`.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Command-Line OTP System](#command-line-otp-system)
  - [GUI OTP System](#gui-otp-system)
- [Security Notes](#security-notes)
- [License](#license)

## Overview
This OTP Verification System consists of two components:

1. **OTP Generation and Email Sending**: 
    - A Python script that generates a random 6-digit OTP and sends it to a user's email address using Gmail's SMTP server.
    - It uses the `smtplib` and `ssl` libraries to establish a secure connection with Gmail's SMTP server.

2. **GUI for OTP Verification**:
    - A Tkinter-based graphical user interface (GUI) that allows users to enter their email address and received OTP.
    - This GUI communicates with the same email system to send OTP and verify user input.

## Prerequisites

- Python 3.x
- The following Python libraries:
  - `smtplib` (built-in Python library)
  - `ssl` (built-in Python library)
  - `tkinter` (built-in Python library for GUI, usually comes with Python)
  - `random` (built-in Python library)
  - `string` (built-in Python library)
  
You can install any necessary libraries with `pip` (for example, `pip install secure-smtplib` if needed).


