import pyautogui
import time

# 定义监控函数
def monitor_chrome():
    while True:
        # 获取所有窗口的信息
        windows = pyautogui.getWindows()
        for window in windows:
            if "Chrome" in window.title:
                # 如果发现 Chrome 窗口，则激活该窗口
                pyautogui.click(window.left + 10, window.top + 10)
                
                # 寻找 Aw, Sanp 错误提示框
                if pyautogui.locateOnScreen('error.png', grayscale=True, confidence=0.9) is not None:
                    print("Something went wrong while displaying this page.")
                    # 重新加载网页
                    pyautogui.hotkey('ctrl', 'r')
                    
                break
        time.sleep(1)

# 运行监控函数
monitor_chrome()

