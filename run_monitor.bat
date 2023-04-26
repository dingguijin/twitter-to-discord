@echo off

:loop
  rem 运行你想要运行的程序，这里假设是my_program.exe
  python monitor_chrome.py
  
  rem 生成一个1-10之间的随机数
  set /a random_num=%random% %% 1000 + 500
  
  rem 等待随机秒数后继续执行循环
  timeout /t %random_num%
goto loop

