import gnupg
from pynput import keyboard
import pyperclip
import pyautogui


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

    gpg = gnupg.GPG()
    gpg.import_keys(publickey)
    hashed = gpg.encrypt(clear, 'B2327C2758E6587B') # - replace with yours certificate id
    pyperclip.copy(str(hashed))

def copyANDpaste(key):
    if key == keyboard.Key.ctrl_r:
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        clear = pyperclip.paste()
        hashing(clear)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    else:
        return
    
listener = keyboard.Listener(on_press=copyANDpaste)
listener.start()
listener.join()