@echo off

:loop
  rem 运行你想要运行的程序，这里假设是my_program.exe
  python tw.py
  
  rem 生成一个1-10之间的随机数
  set /a random_num=%random% %% 10 + 1
  
  rem 等待随机秒数后继续执行循环
  timeout /t %random_num%
goto loop

