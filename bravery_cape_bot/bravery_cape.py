from utils.window import MetinWindow, OskWindow
import utils.utils as ut
import pyautogui
import time
from screeninfo import get_monitors


def command_pause():
    time.sleep(0.2)


def main():
    pyautogui.countdown(3)
    osk = OskWindow('On-Screen Keyboard')
    aeldra = MetinWindow('Aeldra.to - Zeta')
    osk.move_window(x=0, y=0)
    testkeys = True

    if testkeys:
        for m in get_monitors():
            print(str(m))
        osk.test_keys()
    else:
        for i in range(1000):
            print(f'\nIteration {i}:')

            print('Pulling mobs')
            command_pause()
            osk.pull_mobs()

            print('Start hitting')
            osk.start_hitting()
            command_pause()

            print('Kill mobs')
            time.sleep(7)

            print('Stop hitting')
            osk.stop_hitting()
            command_pause()

            print('Picking up')
            osk.pick_up()
            command_pause()

    print('Done')


if __name__ == '__main__':
    # utils.countdown()
    main()

