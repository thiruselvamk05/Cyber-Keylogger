💬 Project Description
  
  This project is a Python-based keylogger tool designed strictly for educational and cybersecurity awareness purposes.

⚙️ Features
✅ Graphical User Interface (GUI) with Start and Stop buttons

✅ Encrypted keystroke logging to protect and demonstrate secure data handling

✅ Clipboard content capture (demonstrates how attackers may target copy-paste data)

✅ Periodic screenshots for activity tracking awareness

✅ Automatic emailing of encrypted logs every 3 minutes

✅ Manual "Send Log Now" button for immediate email testing


🚨 Ethical Disclaimer
This tool is intended only for educational testing and self-research on your own devices.
⚠️ Unauthorized use on others' systems without consent is illegal and unethical.


💡 Learning Objectives
Understand how keyloggers capture input data

Learn about encryption of sensitive logs

Explore periodic automated data exfiltration via email

Gain awareness of security risks and countermeasures


🛠 Setup & Usage

1️⃣ Install requirements:
bash
pip install -r requirements.txt

2️⃣ Generate your encryption key (only once):
bash
python encrypt_util.py

3️⃣ Start the keylogger:
bash
python keylogger_with_gui.py

4️⃣ Use the GUI to start, stop, and send logs manually.



💻 Steps to run the full project

✅ 1️⃣ Install Python dependencies
Open Command Prompt or PowerShell inside your project folder and run:
bash
pip install -r requirements.txt

✅ 2️⃣ Generate your encryption key (only once)
Run this command once to create secret.key:
bash
python encrypt_util.py

➡️ This will create a file:
C:\Users\user\Desktop\keylogger_project\secret.key

✅ 3️⃣ Start the keylogger GUI
bash
python keylogger_with_gui.py

✅ 4️⃣ Use the GUI
When the window opens:
✅ Click Start Logger → It will start logging keystrokes, clipboard, screenshots, and auto email logs.

🟥 Click Stop Logger → It will stop all logging.

📧 Click Send Log Now → It will manually email your current log.txt.



📂 Output files
Encrypted keystrokes: logs/log.txt

Screenshots: screenshots/

Encryption key: secret.key (⚠️ Keep private)



📂 Folder Structure

keylogger_project/
├── email_util.py
├── encrypt_util.py
├── keylogger_with_gui.py
├── secret.key          # Encryption key (NOT uploaded to GitHub)
├── logs/
│   └── log.txt
├── screenshots/
├── requirements.txt
└── README.md
