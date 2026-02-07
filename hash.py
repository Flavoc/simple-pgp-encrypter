import gnupg
from pynput import keyboard
import pyperclip
import pyautogui
import os


def hashing(clear):

    # replace with yours pgp public key 
    publickey = """
    -----BEGIN PGP PUBLIC KEY BLOCK-----

    mDMEaVQAqhYJKwYBBAHaRw8BAQdA0865ZdtJ8XD2gx18LkmhhyczmFgVdHgGQ3pw
    qAHfT2O0BHJ1dXSImQQTFgoAQRYhBO9+MrEDM00aTCkf87IyfCdY5lh7BQJpVACq
    AhsDBQkFpJwGBQsJCAcCAiICBhUKCQgLAgQWAgMBAh4HAheAAAoJELIyfCdY5lh7
    HJQA/jxF6sF7tieKovtWzvNgaiUY0K8szfJpzEyCGlBlGtYOAQD8XSAcVybjGwBB
    awXivdmm+M/VMhmD1yVuTDXf1oALB7g4BGlUAKoSCisGAQQBl1UBBQEBB0CqjmvL
    q9Y29bQH346MTdbXIVs7V+uyhQx+4HcFO/DTJAMBCAeIfgQYFgoAJhYhBO9+MrED
    M00aTCkf87IyfCdY5lh7BQJpVACqAhsMBQkFpJwGAAoJELIyfCdY5lh7KGwBAK99
    7r5OSVLuNrcC8W/sSWGfZbqk9dpa3V/EEi5s2ovEAP9Mby95ocyNaLhw9ng8pmpd
    wuKqiRYTY6WBLJwALtz5Aw==
    =FokO
    -----END PGP PUBLIC KEY BLOCK-----
    """
    certificateid = "B2327C2758E6587B" # - replace with yours certificate id

    gpg = gnupg.GPG()
    gpg.import_keys(publickey)
    hashed = gpg.encrypt(clear, recipients=certificateid) 
    pyperclip.copy(str(hashed))

global clicked
clicked = False

def copyANDpaste(key):
    global clicked 
    global listener 

    if key == keyboard.Key.ctrl_r and clicked == False:
        clicked = True
        listener.stop()
        pyautogui.hotkey('ctrl', 'a')
        previous = pyperclip.paste()
        pyautogui.hotkey('ctrl', 'c')
        clear = pyperclip.paste()
        hashing(clear)
        pyautogui.hotkey('ctrl', 'v') 
        pyperclip.copy(previous)
        listener = keyboard.Listener(on_press=copyANDpaste, on_release=unclicked)
        listener.start()

def emergencybutton(key):
    if key == keyboard.Key.insert:
        os._exit(0)
        
def unclicked():
    global clicked
    clicked = False

emergencythread = keyboard.Listener(on_press=emergencybutton)
emergencythread.start()

global listener
listener = keyboard.Listener(on_press=copyANDpaste, on_release=unclicked) 
listener.start()

emergencythread.join()
listener.join()
