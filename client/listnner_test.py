from pynput.keyboard import Key, Listener

def on_press(key):
    if key == Key.esc:
        raise StopApp(key)
    print(key)
    if key == Key.up:
        movement = 1
    elif key == Key.down:
        movement = 2
    elif key == Key.right:
        movement = 3
    elif key == Key.left:
        movement = 4

def on_release(key):
    print(key)

class StopApp(Exception): pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except StopApp as e:
        print(e)
    except Exception as e:
        print(e)