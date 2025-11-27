import os, time
import mouse
import numpy as np
import cv2
import pyautogui as pg

class error_handler:

    def _E1030_handler(self, threshold: float = 0.80):
        """ 處理E1030 """
            
        folder = r".\RPA\E1030"
        i = 1
        image_full_name = os.path.join(folder, str(i) + ".jpg")
        while os.path.exists(image_full_name):
            # 螢幕截圖
            screen_shot = cv2.cvtColor(np.array(pg.screenshot()), cv2.COLOR_RGB2BGR)
            # 樣板按鈕
            template = cv2.imread(image_full_name)
            # 使用cv2比對按鈕位置
            res = cv2.matchTemplate(screen_shot, template, cv2.TM_CCOEFF_NORMED)
            conf = res.max()
            if conf < threshold:
                time.sleep(1)
                continue
            loc = np.where(res == conf)
            if loc:
                h, w, _ = template.shape
                mouse.move(x = loc[1] + 0.5 * w, y = loc[0] + 0.5 * h, absolute = True)
                mouse.click('left')
                time.sleep(0.5)
            i += 1
            image_full_name = os.path.join(folder, str(i) + ".jpg")
    
class rpa_ws:

    def __init__(self) -> None:


        error_handler()._E1030_handler()

        
if __name__ == "__main__":
    rpa_ws()
# # left click
# mouse.click('left')

# # right click
# mouse.click('right')

# # middle click
# mouse.click('middle')
# mouse.move(x = 100, y = 100, absolute = False, duration = 0.2)
# # mouse.on_click(lambda: print("Left Button clicked."))
# # mouse.on_right_click(lambda: print("Right Button clicked."))
# mouse.get_position()

