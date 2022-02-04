import random
import pyautogui
import time

time.sleep(5)
Zone = ["Morgue", "Hospital", "Casa", "Deposito", "Exteriores", "Oficinas"]
Place = ["Habitacion", "Pasillo","Hall", "Area descampada", "Atrio", "Dormitorio"]
Modifier = ["Oscuro", "Iluminado", "Con niebla", "Con luces intermitentes"]
x = ["Realista", "Ireal"]

numba = 7

while numba != 0:
    pyautogui.typewrite(random.choice(Zone) + " " + random.choice(Place) + " " + random.choice(Modifier) + " " + random.choice(x))
    pyautogui.press("Enter")
    numba -= 1