import cv2

from window import MetinWindow
import pyautogui
import time
import cv2 as cv
from vision import Vision, Metin50Filter, Metin45Filter


def command_pause():
    time.sleep(0.2)


def main():
    pyautogui.countdown(3)
    aeldra = MetinWindow('Razathor')
    vision = Vision()
    # vision.init_control_gui()
    mt50_filter = Metin50Filter()
    mt45_filter = Metin45Filter()

    count = {'p': 0, 'n': 0}

    while True:
        loop_time = time.time()
        screenshot = aeldra.capture()
        # screenshot_BW = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        processed_screenshot = vision.apply_hsv_filter(screenshot, hsv_filter=mt45_filter)

        # processed_screenshot = vision.apply_hsv_filter(screenshot, hsv_filter=mt50_filter)
        processed_screenshot_BW = cv2.cvtColor(processed_screenshot, cv2.COLOR_BGR2GRAY)

        cv.imshow('Video Feed', processed_screenshot_BW)
        # cv.imshow('Video Feed', processed_screenshot)
        # print(f'{round(1 / (time.time() - loop_time),2)} FPS')

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        key = cv.waitKey(1)
        if key == ord('q'):
            cv.destroyAllWindows()
            break

        # press 'p' with the output window focused to save positive img.
        # waits 1 ms every loop to process key presses
        elif key == ord('p'):
            success = cv.imwrite(r'C:\Users\oxan\PycharmProjects\Metin2CloudBot\metin_farm_bot\classifier\positive_2023_19_3_01/{}.jpg'.format(int(loop_time)), processed_screenshot_BW)
            if success:
                count['p'] += 1
                print(f'Saved positive sample. {count["p"]} total.')
            else:
                print(f'Couldn\'t save positive sample. {count["n"]} total.')


        # press 'n' with the output window focused to save positive img.
        # waits 1 ms every loop to process key presses
        elif key == ord('n'):
            success = cv.imwrite(r'C:\Users\oxan\PycharmProjects\Metin2CloudBot\metin_farm_bot\classifier\negative_2023_19_3_01/{}.jpg'.format(int(loop_time)), processed_screenshot_BW)
            if success:
                count['n'] += 1
                print(f'Saved negative sample. {count["n"]} total.')
            else:
                print(f'Couldn\'t save negative sample. {count["n"]} total.')


if __name__ == '__main__':
    main()

