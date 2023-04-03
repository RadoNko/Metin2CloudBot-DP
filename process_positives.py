import pyautogui
import time
from samples import Samples


def main():
    pyautogui.countdown(3)
    size = (20, 32)
    samples = Samples('pos.txt', desired_size=size)
    # samples.display_images(resized=True)
    # samples.generate_negs_from_samples(f'classifier/negs_from_pos_{int(time.time())}')
    samples.export_samples(f'classifier/sample_export_{int(time.time())}', resized=True)


    print('Done')

if __name__ == '__main__':
    main()

