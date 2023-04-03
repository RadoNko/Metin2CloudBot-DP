import os
import pyautogui

def get_metin_needle_path():
    return 'C:/Users/oxan/PycharmProjects/Metin2CloudBot/utils/needle_metin.png'
# TODO tesseract
def get_tesseract_path():
    return r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_respawn_needle_path():
    return 'C:/Users/oxan/PycharmProjects/Metin2CloudBot/utils/needle_respawn.png'

def countdown():
    pyautogui.countdown(3)