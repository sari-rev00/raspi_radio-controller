import urllib.request
import json
from pynput.keyboard import Key, Listener

TEST = False

class StopApp(Exception): pass

class Client():
    def __init__(self):
        self.prev_movement = None
        return None

    def request_control(self, dict_data):
        if TEST:
            url = "http://127.0.0.1:8000/control"
        else:
            url = "http://192.168.0.56:8000/control"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        req = urllib.request.Request(url, json.dumps(dict_data).encode(), headers)
        with urllib.request.urlopen(req) as res:
            body = res.read()
        return body

    def on_press(self, key):
        # movement manegement =======================
        if key == Key.esc:
            raise StopApp(key)
        movement = None
        if key == Key.up:
            movement = 1
        elif key == Key.down:
            movement = 2
        elif key == Key.right:
            movement = 3
        elif key == Key.left:
            movement = 4
        elif key == Key.space:
            movement = 0
        # request control ===========================
        if movement and (self.prev_movement != movement):
            if TEST:
                print(movement)
            self.prev_movement = movement
            try:
                self.request_control(dict_data={"movement": movement})
            except Exception as e:
                print(e)
        return None
    
    def on_release(self, key):
        # movement manegement =======================
        movement = None
        if key in {Key.up, Key.down, Key.right, Key.left}:
            self.prev_movement = movement = 0
            if TEST:
                print(movement)
            try:
                self.request_control(dict_data={"movement": movement})
            except Exception as e:
                print(e)
        return None

    def loop(self):
        try:
            with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()
        except StopApp as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            dict_data = {"movement": 0} # stop
            self.request_control(dict_data=dict_data)

if __name__ == '__main__':
    print("dangomushi control crient: start")
    print("usage: up=forward, down=backward, right=rotate_right, left=rotate_left")
    client = Client()
    client.loop()
