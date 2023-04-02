import os
import sys
import time

def _restart():
    os.execv(sys.executable, ['python'] + sys.argv)
    return

def _main():
    print("RUNNING MAIN .....")
    time.sleep(3)
    _restart()
    return

if __name__ == "__main__":
    _main()
