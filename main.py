from time import sleep
import tkinter as tk
from functools import partial
import cv2 as cv
from captureAndDetect import CaptureAndDetect
from window import MetinWindow, OskWindow
from vision import Metin50Filter
from bot import MetinFarmBot


def main():
    # Choose which metin
    metin_selection = {'metin': 'Lvl. 45: Kámen stínu'}
    # metin_select(metin_selection)
    metin_selection = metin_selection['metin']
    # hsv_filter = Metin50Filter() if metin_selection != 'lv_90' else SnowManFilterRedForest()
    hsv_filter = Metin50Filter()

    # Countdown
    # utils.countdown()

    # Get window and start window capture
    metin_window = MetinWindow('Razathor')

    capt_detect = CaptureAndDetect(metin_window, 'classifier/cascade/cascade.xml', hsv_filter)

    # Initialize the bot
    bot = MetinFarmBot(metin_window, metin_selection)
    cleanup_gui()
    capt_detect.start()
    bot.start()

    while True:

        # Get new detections
        screenshot, screenshot_time,\
            detection, detection_time, detection_image = capt_detect.get_info()
        # print(detection)

        # Update bot with new image
        bot.detection_info_update(screenshot, screenshot_time, detection, detection_time)

        if detection_image is None:
            continue

        # Draw bot state on image
        overlay_image = bot.get_overlay_image()
        detection_image = cv.addWeighted(detection_image, 1, overlay_image, 1, 0)

        # Display image
        cv.imshow('Matches', detection_image)

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        key = cv.waitKey(1)

        if key == ord('q'):
            capt_detect.stop()
            bot.stop()
            cv.destroyAllWindows()
            break

    print('Done.')


def login_gui(username, password, pin):
    osk_window = OskWindow('On-Screen Keyboard')
    osk_window.move_window(x=-0, y=0)

    metin_window = MetinWindow('Razathor')
    metin_window.activate()

    username = list(username)
    password = list(password)
    pin = list(pin)

    for char in username:
        osk_window.press_key(button=char, mode='click')

    osk_window.press_key(button='Tab', mode='click')

    for char in password:
        osk_window.press_key(button=char, mode='click')

    osk_window.press_key(button='Tab', mode='click')

    for char in pin:
        osk_window.press_key(button=char, mode='click')

    osk_window.press_key(button="Enter", mode="click")
    sleep(3)
    metin_window.activate()

    metin_window.mouse_move(475*1.25, 700*1.25)
    sleep(0.1)
    metin_window.mouse_click()

def cleanup_gui():
    metin_window = MetinWindow('Razathor')
    metin_window.activate()

    osk_window = OskWindow('On-Screen Keyboard')
    osk_window.move_window(x=-0, y=0)
    osk_window.press_key("F", mode="down")
    sleep(0.1)

    metin_window.mouse_move(51 * 1.25, 422 * 1.25)
    sleep(0.1)
    metin_window.mouse_click()

    metin_window.mouse_move(1010 * 1.25, 20 * 1.25)
    sleep(0.1)
    metin_window.mouse_click()


def metin_select(metin_selection):
    metins = {'Lvl. 45: Kámen stínu': 'lv_40',
              'Lvl. 60: Kámen pádu': 'lv_60',
              'Lvl. 70: Kámen vraždy': 'lv_70',
              'Lvl. 90: Kámen Jeon-Un': 'lv_90'}

    def set_metin_cb(window, metin, metin_selection):
        metin_selection['metin'] = metin
        window.destroy()

    window = tk.Tk()
    window.title("Metin2 Bot")
    tk.Label(window, text='Select Metin:').pack(pady=5)

    for button_text, label in metins.items():
        tk.Button(window, text=button_text, width=30,
                  command=partial(set_metin_cb, window, label, metin_selection)) \
            .pack(padx=3, pady=3)

    window.mainloop()


if __name__ == '__main__':
    main()
