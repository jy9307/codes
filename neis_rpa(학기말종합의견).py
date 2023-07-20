from pywinauto import Application
from pywinauto import findwindows
import pyautogui

# procs = findwindows.find_elements()

# for proc in procs:
#     print(f"{proc} / 프로세스 : {proc.process_id}")

app = Application(backend='uia').connect(title_re =".*Microsoft.*Edge.*")
neis = app["4세대 지능형 나이스 시스템 외 페이지 1개 - 프로필 1 - Microsoft​ Edge', Chrome_WidgetWin_1"]

def content_add() :
    #조회/가져오기 버튼 들어간 이후
    pyautogui.sleep(1)
    
    pyautogui.click(405,480)
    pyautogui.click(1520,420)
    pyautogui.press("delete")
    pyautogui.press("space")

    pyautogui.click(1555,972, clicks=5)
    pyautogui.sleep(1)
    neis["반영"].click()
    neis["확인"].click()

# #1번
# pyautogui.click(822,597)
# pyautogui.press('tab')
# pyautogui.press('enter')
# content_add()
# #2번
# pyautogui.click(822,672)
# pyautogui.press('tab')
# pyautogui.press('enter')
# content_add()
# #3번
# pyautogui.click(822,752)
# pyautogui.press('tab')
# pyautogui.press('enter')
# content_add()
# #4번
# pyautogui.click(822,832)
# pyautogui.press('tab')
# pyautogui.press('enter')
# content_add()

#5번~끝번
for i in range(int(input("끝번호를 입력하세요"))-4) :
    pyautogui.sleep(0.5)
    pyautogui.click(822,912)
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.press('enter')
    content_add()
