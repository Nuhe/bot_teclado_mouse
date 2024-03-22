import pyautogui
import keyboard

class botardo:

    def pantalla_tamano(self):
        ancho, alto = pyautogui.size()

        return ancho, alto # Toma cada dato [0][1] | [x, y] para determinar el posicionamiento del mouse. 
    
    def click(self, posx, posy):
        pyautogui.click(x=posx, y=posy) 
    
    def press_keys(self, keys):
        keyboard.press_and_release(keys)

bot = botardo()    