
import win32api, win32con
import time
def lclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

import win32com.client

site="http://goo.gl/forms/1fRLPHIaRs"
def mousepos(point):

    win32api.SetCursorPos((point[0],point[1]))

def opwin(site):
    shell=win32com.client.Dispatch("WScript.Shell")
    shell.Run("chrome")
    mousepos((119, 42))
    lclick()
    shell.SendKeys(site)
    shell.SendKeys("~")
    time.sleep(6)
    mousepos((394,494))
    lclick()
    shell.SendKeys("Sandeep")
    time.sleep(1)
    mousepos((394,604))
    lclick()
    shell.SendKeys("KF11574")
    time.sleep(1)
    mousepos((394,710))
    lclick()
    shell.SendKeys("Saif")
    time.sleep(1)
    mousepos((1356,732))
    for i in range(0,17):
        lclick()
        time.sleep(0.3)
    mousepos((394,160))
    lclick()
    shell.SendKeys("KF1178")
    time.sleep(1)
    mousepos((394,269))
    lclick()
    shell.SendKeys("Sashikant")
    time.sleep(1)
    mousepos((394,377))
    lclick()
    shell.SendKeys("KF2178")
    time.sleep(1)
    mousepos((394,486))
    lclick()
    shell.SendKeys("Subho")
    time.sleep(1)
    mousepos((394,596))
    lclick()
    shell.SendKeys("KF1778")
    time.sleep(1)
    mousepos((430,688))
    lclick()
    time.sleep(1)
    print("The Form has been Submitted")


opwin(site)
