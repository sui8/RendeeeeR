# Made by suiken-Developer
import tkinter as tk
from tkinter import messagebox as msg
import tkinter.ttk as ttk
import configparser
import pyautogui
import time

root = tk.Tk()
root.geometry("350x75")

Ver = "1.0.0"

root.title("RendeeeR!! Ver {0}".format(Ver))

frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=tk.NSEW, padx=5, pady=10)

conf = configparser.ConfigParser()
conf.read("Config.ini", encoding='utf-8')
c_time = conf['SETTING'].getfloat('Time')
c_kankaku = conf['SETTING'].getint('Range')
c_key = conf['SETTING'].get('Key')
c_success = conf['SETTING'].get('SuccessInfo')


def run():
    time.sleep(5)
    for i in range(c_kankaku):
        pyautogui.press(c_key)
        time.sleep(c_time)

    if c_success == "On":
        msg.showinfo("RendeeeeR!!", "入力完了")

label = ttk.Label(frame, text="実行5秒後に入力開始します")
button = ttk.Button(frame, text="実行", command=run)

label.grid(row=0, column=0)
button.grid(row=0, column=3)

root.mainloop()
