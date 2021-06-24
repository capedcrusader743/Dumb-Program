import webbrowser
import time
from ctypes import *

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

while True:
    duration = get_idle_duration()
    if duration > 30:
        webbrowser.open('https://listenonrepeat.com/?v=RYhKUKzD6IQ&s=0&e=3603#%E5%85%8E%E7%94%B0%E3%81%BA%E3%81%93%E3%82%89_Usada_Pekora_BGM_(1_HOUR)_%5B60_FPS%5D')
        break
