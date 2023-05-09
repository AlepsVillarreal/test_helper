import pyautogui
import time
from helper_functions import read_yaml

config = read_yaml(r".\config.yaml")

screenshot_save_directory = config['APP']['SCREENSHOTS_FOLDER']


def take_screenshot():
    timestamp = time.strftime('%Y%m%d%H%M%S')
    screenshot_name = screenshot_save_directory + "\\" + f'screenshot_{timestamp}.png'
    # absolute_screenshot_name = '\\'.join(screenshot_save_directory, screenshot_name)
    print(screenshot_name)
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_name)
    print(f'Screenshot saved as {screenshot_name}')


def main():
    while True:
        take_screenshot()
        time.sleep(30)


if __name__ == '__main__':
    main()
