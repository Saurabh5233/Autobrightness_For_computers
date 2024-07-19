# AUTOMATED BRIGHTTNESS LEVEL SETTINGS

# import time
# import threading
# import pyautogui
# import screen_brightness_control as sbc

# # Function to adjust screen brightness based on screen content
# def adjust_brightness():
#     while True:
#         # Capture a screenshot
#         screenshot = pyautogui.screenshot()

#         # Calculate average brightness of the screenshot
#         total_brightness = sum(screenshot.convert("L").getdata())
#         average_brightness = total_brightness / (screenshot.width * screenshot.height)

#         # Invert brightness: 100 - current_brightness
#         inverted_brightness = 100 - int(average_brightness / 256 * 100)

#         # Adjust brightness based on inverted average brightness
#         sbc.set_brightness(inverted_brightness)

#         # Adjusting the brightness frequently can strain CPU, so we sleep for a short duration
#         time.sleep(1)

# # Start a thread to continuously adjust brightness
# brightness_thread = threading.Thread(target=adjust_brightness)
# brightness_thread.daemon = True  # Daemonize the thread so it exits when the main thread exits
# brightness_thread.start()

# # Main loop (optional)
# while True:
#     # You can add additional functionality or keep the main thread running
#     time.sleep(1)  # Add a sleep to prevent high CPU usage

# MANUAL BRIGHTNESS LEVEL SETTINGS

import time
import threading
import pyautogui
import screen_brightness_control as sbc

# Function to adjust screen brightness based on screen content
def adjust_brightness(min_brightness, max_brightness):
    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Calculate average brightness of the screenshot
        total_brightness = sum(screenshot.convert("L").getdata())
        average_brightness = total_brightness / (screenshot.width * screenshot.height)

        # Map average brightness to the custom brightness range
        custom_brightness = map_value(average_brightness, 0, 255, min_brightness, max_brightness)

        # Adjust brightness based on custom brightness range
        sbc.set_brightness(int(custom_brightness))

        # Adjusting the brightness frequently can strain CPU, so we sleep for a short duration
        time.sleep(1)

# Function to map a value from one range to another
def map_value(value, from_min, from_max, to_min, to_max):
    return (value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

# Main function
def main():
    # Get user input for custom brightness limits
    # min_brightness = int(input("Enter the MAXIMUM brightness level (0-100): "))
    # max_brightness = int(input("Enter the MINIMUM brightness level (0-100): "))
    max_brightness = -10#Enter the MAXIMUM brightness level (0-100):
    min_brightness = 25#Enter the MINIMUM brightness level (0-100):

    # Start a thread to continuously adjust brightness
    brightness_thread = threading.Thread(target=adjust_brightness, args=(min_brightness, max_brightness))
    brightness_thread.daemon = True  # Daemonize the thread so it exits when the main thread exits
    brightness_thread.start()

    # Main loop (optional)
    while True:
        # You can add additional functionality or keep the main thread running
        time.sleep(1)  # Add a sleep to prevent high CPU usage

if __name__ == "__main__":
    main()

