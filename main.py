import sys
import os
try:
    from main2 import main
except Exception:
    from main2 import main

def restart_program():
    pass

if __name__ == '__main__':
    while 1:
        ret = main()
        if not ret is None:
            break
        restart_program()
    print("-- program exit, code:", ret)
    sys.exit(ret)
