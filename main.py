import pyautogui
import pydirectinput
from time import sleep
import threading
import os
import time
import psutil
import win32gui
import win32con
import win32process
import random
import requests
import ctypes
import genkey
import tkinter as tk
import keyboard

start = False
script_thread = None

def find_img(img, window_rect, confidence=0.7): 
    if start:
        try:
            image = pyautogui.locateOnScreen(f'./images/{img}.jpg', confidence=confidence, region=window_rect)
            if image:
                return True
        except:
            pass

def click(x, y):
    if start:
        target_x = x + random.randint(-10, 10)
        target_y = y + random.randint(-10, 10)
        pyautogui.moveTo(target_x, target_y, duration=0.7)
        pydirectinput.click()
        sleep(0.5)

def click_completed():
    if find_img('completed', (986, 144, 40, 33)):
        click(1092, 156)

def click_claim():
    if find_img('claim', (1026, 577, 38, 36)):
        click(1041, 594)

def click_accept():
    if find_img('accept', (707, 614, 44, 31)):
        click(728, 628)

def click_mission():
    if find_img('auto1', (1200, 416, 49, 31)):
        click(1092, 156)
        if find_img('travel', (1172, 139, 30, 24)):
            click(1183, 158)

def click_skip():
    if find_img('skip', (1204, 54, 55, 24)):
        click(1235, 57)
    elif find_img('skip2', (1213, 260, 40, 33)):
        pyautogui.moveTo(1231, 267, duration=0.2)
        pydirectinput.click()
    elif find_img('skip3', (680, 646, 34, 36)):
        click(698, 662)

def click_back():
    if find_img('back', (1208, 65, 37, 30)):
        pydirectinput.press('esc')

def close_menu():
    if find_img('menu', (1206, 194, 43, 35)):
        click(1226, 85)

def click_fast_travel():
    if find_img('fast', (606, 290, 33, 22)):
        click(681, 428)

def click_ok():
    if find_img('ok', (624, 652, 34, 22)):
        click(635, 660)

def click_ok2():
    if find_img('ok2', (655, 411, 64, 31)):
        click(683, 424)

def leave():
    if find_img('leave', (0, 0, 1280, 720)):
        click(640, 620)
        sleep(10)
        click(1228, 579)
        sleep(3)
        click(685, 424)
        sleep(0.5)
        click(685, 424)
        wait_bag()
        buy_potions()

def click_reconnect():
    if find_img('reconnect', (645, 438, 92, 32)):
        click(681, 453)

def buy_potions():
    if start:
        pydirectinput.press('4')
        back = find_img('back', (1208, 65, 37, 30))
        timeout = 0
        while not back:
            back = find_img('back', (1208, 65, 37, 30))
            sleep(1)
            timeout += 1
            if timeout == 25:
                return
        if timeout != 25:
            sleep(3)
            pyautogui.click(149, 183)
            sleep(3)
            pyautogui.click(706, 400)
            sleep(3)
            pyautogui.click(681, 492)
            sleep(3)
            click_back()

def revive():
    if find_img('revive', (684, 601, 88, 34)):
        sleep(4)
        click(722, 618)
        sleep(0.5)
        click(722, 618)
        wait_bag()
        buy_potions()

def equip():
    search_tutorials()
    sleep(2)
    if find_img('bag', (1164, 61, 38, 37)):
        pydirectinput.press('i')
        start_time = time.time()
        timeout = 20 
        back = find_img('back', (1208, 65, 37, 30))
        while not back and time.time() - start_time < timeout:
            back = find_img('back', (1208, 65, 37, 30))
            sleep(1)
        sleep(3)
        if find_img('auto_equip', (1132, 652, 90, 27)):
            click(1167, 664)
            sleep(3)
        click_back()
        global time_to_equip
        time_to_equip = 0

def damage():
    if find_img('damage', (979, 129, 51, 28)):
        pydirectinput.click(1228, 152)

def wait_bag():
    bag = find_img('bag', (1164, 61, 38, 37))
    while not bag:
        bag = find_img('bag', (1164, 61, 38, 37), 0.5)
        sleep(1)
    sleep(5)

def search_tutorials():
    if find_img('tutorial1', (859, 556, 156, 56)): #Quest de clicar na poção
        pyautogui.click(934, 660) #Clica na poção
    if find_img('tutorial2', (832, 134, 439, 61)): #Quest de equipar equipamento
        pyautogui.click(1180, 77) #Clica na bag
    if find_img('tutorial3', (745, 153, 231, 61)):
        posicao = pyautogui.locateOnScreen(f'./images/equipamento_quest.jpg', confidence=0.7, region=(977, 146, 288, 435))
        center = pyautogui.center(posicao)
        pyautogui.click(center)
        sleep(0.5)
        pyautogui.click(center)
        sleep(5)
        pyautogui.click(1226, 73) #Clica pra fechar
    if find_img('tutorial4', (832, 134, 439, 61)): #Clica no Menu
        pyautogui.click(1228, 77)
    if find_img('tutorial5', (1069, 58, 200, 41)): #Clica em Mounts
        pyautogui.click(1177, 148)
    if find_img('tutorial6', (875, 130, 209, 37)): #Clica na montaria de andar
        pyautogui.click(977, 222)
    if find_img('tutorial7', (987, 589, 283, 32)): #Clica em equipar
        pyautogui.click(1160, 665)
        sleep(3)
        pyautogui.click(1226, 73) #Clica pra fechar
    if find_img('tutorial8', (990, 134, 192, 32)): #Clica na montaria de voar
        pyautogui.click(1084, 222)
    if find_img('tutorial9', (1062, 573, 199, 46)): #Clica na equipar
        pyautogui.click(1160, 665)
        sleep(4)
        pyautogui.click(1226, 73) #Clica pra fechar
    if find_img('tutorial10', (1075, 62, 194, 31)): #Clica em Mounts
        pyautogui.click(1177, 148)
    if find_img('tutorial11', (830, 554, 359, 51)): #Clica na Town
        pyautogui.click(1228, 580)
        sleep(3)
        pyautogui.click(687, 425)
    if find_img('tutorial12', (1109, 140, 146, 32)): #Clica em bag
        pyautogui.click(1180, 77) #Clica na bag
    if find_img('tutorial13', (933, 123, 179, 31)): #Clica consumables
        pyautogui.click(1163, 134)
    if find_img('tutorial14', (692, 166, 275, 33)):
        posicao = pyautogui.locateOnScreen(f'./images/book_quest.jpg', confidence=0.7, region=(977, 146, 288, 435))
        center = pyautogui.center(posicao)
        pyautogui.click(center)
        sleep(0.5)
        pyautogui.click(center)
        sleep(8)
        pyautogui.click(1226, 73) #Clica pra fechar
    if find_img('tutorial15', (0, 0, 1300, 800)): #Clica em menu
        pyautogui.click(1228, 77)
    if find_img('tutorial16', (0, 0, 1300, 800)): #Clica em skill
        pyautogui.click(1084, 146)
    if find_img('tutorial17', (0, 0, 1300, 800)): #Clica em edit skills
        pyautogui.click(1176, 665)
    if find_img('tutorial18', (0, 0, 1300, 800)): #Clica na habilidade
        pyautogui.click(1110, 264)
        sleep(4)
        pyautogui.click(829, 214)
        sleep(3)
        pyautogui.click(1226, 73) #Clica pra fechar
    if find_img('tutorial19', (0, 0, 1300, 800)): #Ativa a skill
        pyautogui.moveTo(505, 647)
        pyautogui.mouseDown(button='right')
        pyautogui.moveTo(505, 669, duration=0.5)
        pyautogui.mouseUp(button='right')
    if find_img('tutorial20', (1049, 137, 222, 39)): #Clica em menu
        print(find_img('tutorial20', (1049, 137, 222, 39)))
        pyautogui.click(1228, 77)
    if find_img('tutorial21', (0, 0, 1300, 800)): #Clica em avatar
        pyautogui.click(1131, 148)
    if find_img('tutorial22', (0, 0, 1300, 800)): #Clica no avatar
        pyautogui.click(960, 200)
        sleep(4)
        pyautogui.click(1160, 665)
        sleep(3)
        pyautogui.click(1226, 73)
    if find_img('tutorial23', (993, 140, 276, 55)): #Clica em bag
        pyautogui.click(1180, 80)
    if find_img('tutorial24', (546, 155, 451, 58)): #Clica em equipamento
        pyautogui.click(1018, 183)
    if find_img('tutorial25', (427, 450, 216, 36)): #Clica em dismantle
        pyautogui.click(531, 523)
        sleep(3)
        pyautogui.click(686, 468) #clica em ok
        sleep(2)
        pyautogui.click(1226, 73)
    if find_img('tutorial26', (997, 266, 177, 34)): #Clica em crafting
        pyautogui.click(1084, 207)
    if find_img('tutorial27', (326, 304, 274, 41)): #Clica no tipo
        pyautogui.click(158, 312)
        sleep(4)
        pyautogui.click(420, 240)
        sleep(3)
        pyautogui.click(1150, 660)
        sleep(5)
        pyautogui.click(700, 610)
    if find_img('tutorial28', (960, 138, 309, 74)): #Clica em bag
        pyautogui.click(1181, 77)
    if find_img('tutorial29', (515, 151, 455, 57)): #Clica no item
        pyautogui.click(1017, 180)
    if find_img('tutorial30', (605, 450, 170, 38)): #Clica em enhance
        pyautogui.click(690, 525)
    if find_img('tutorial31', (916, 522, 222, 54)): #Clica na boonstone
        pyautogui.click(1020, 630)
        sleep(4)
        pyautogui.click(512, 665) #clica em enhance
        sleep(3)
        pyautogui.click(1226, 73) #Clica pra fechar

def alert():
    if find_img('alert', (0, 0, 800, 386)):
        click(537, 440)

def ajustar_janela_projectlh():
    alvo = "projectlh.exe"
    largura, altura = 1280, 720
    x, y = 0, 0

    def get_pids(nome_processo):
        pids = []
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] and proc.info['name'].lower() == nome_processo.lower():
                pids.append(proc.info['pid'])
        return pids

    def manipular_janelas(pid_alvos):
        def callback(hwnd, _):
            try:
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                if pid in pid_alvos and win32gui.IsWindowVisible(hwnd):
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                    win32gui.MoveWindow(hwnd, x, y, largura, altura, True)
                    win32gui.SetForegroundWindow(hwnd)
            except:
                pass
        win32gui.EnumWindows(callback, None)

    pids_alvo = get_pids(alvo)
    if pids_alvo:
        manipular_janelas(pids_alvo)

def set_configs():
    search_tutorials()
    sleep(2)
    bag = find_img('bag', (1164, 61, 38, 37))
    if bag:
        click(1228, 75)
        sleep(2)
        click(1223, 487)
        sleep(3)
        ground_on = find_img('ground_on', (1187, 256, 58, 58))
        if ground_on:
            click(1050, 281)
        saving_off = find_img('saving_off', (738, 528, 72, 60))
        if not saving_off:
            click(818, 556)

def initial_actions():
    ajustar_janela_projectlh()
    sleep(2)
    set_configs()

def toggle_start_pause():
    if start:
        pause_script()
    else:
        start_script()
    sleep(1)

# Associa F8 ao controle de pausa
keyboard.add_hotkey('F10', toggle_start_pause)

def run():
    sleep(2)
    initial_actions()
    last_equip_time = time.time()
    last_quest_time = time.time()
    while True:
        if not start:
            break
        quest = find_img('quest', (1200, 416, 50, 30))
        if quest:
            current_time = time.time()
            if current_time - last_quest_time >= 150:
                click(1100, 148)
                pydirectinput.press('t')
                last_quest_time = current_time
            sleep(2)
        else:
            last_quest_time = time.time()
            try:
                for i in range(3):
                    click_completed()
                    click_claim()
                    for j in range(3):
                        click_skip()
                    click_accept()
                    click_mission()
                    click_fast_travel()
                click_back()
                search_tutorials()
                close_menu()
                damage()
                revive()
                leave()
                click_reconnect()
                click_ok()
                click_ok2()
                alert()
                current_time = time.time()
                if current_time - last_equip_time >= 600:
                    api_response = requests.get('https://theotokos-mateus-athos-projects.vercel.app/usuarios').text
                    if not (genkey.get_hwid() in api_response or genkey.get_new_hwid() in api_response):
                        ctypes.windll.user32.MessageBoxW(0, "Access denied. Unauthorized user", "Authentication error", 0x10)
                        while True:
                            sleep(300)
                    equip()
                    last_equip_time = current_time
            except:
                pass

def thread(target):
    t = threading.Thread(target=target)
    t.start()

# GUI

def start_script():
    global start, script_thread
    if not start:
        start = True
        update_interface()
        if script_thread is None or not script_thread.is_alive():
            script_thread = threading.Thread(target=run, daemon=True)
            script_thread.start()

def pause_script():
    global start
    if start:
        start = False
        update_interface()

def update_interface():
    if start:
        start_button.pack_forget()
        pause_button.pack()
        status_label.config(text="Status: Running")
    else:
        pause_button.pack_forget()
        start_button.pack()
        status_label.config(text="Status: Paused")

def on_close():
    global start
    start = False
    root.destroy()
    os._exit(0)

# Verifica autenticacao antes de abrir interface
api_response = requests.get('https://theotokos-mateus-athos-projects.vercel.app/usuarios').text
if genkey.get_hwid() in api_response or genkey.get_new_hwid() in api_response:
    root = tk.Tk()
    root.title("AutomateApp")
    root.geometry("250x105+506+725")
    root.resizable(False, False)
    root.iconbitmap("images/logo.ico")
    root.configure(bg="#1e1e1e")
    root.lift()
    root.attributes('-topmost', True)
    root.after(1000, lambda: root.attributes('-topmost', False))
    
    status_label = tk.Label(root, text="Status: Paused", font=("Arial", 17), fg="white", bg="#1e1e1e")
    status_label.pack(pady=10)

    start_button = tk.Button(root, text="Start (Press F10)", font=("Arial", 14), width=17, command=start_script,
                         fg="white", bg="#2e2e2e", activebackground="#444", activeforeground="white")
    pause_button = tk.Button(root, text="Pause (Press F10)", font=("Arial", 14), width=17, command=pause_script,
                         fg="white", bg="#2e2e2e", activebackground="#444", activeforeground="white")

    root.protocol("WM_DELETE_WINDOW", on_close)
    update_interface()
    root.mainloop()
else:
    ctypes.windll.user32.MessageBoxW(0, "Access denied. Unauthorized user", "Authentication error", 0x10)