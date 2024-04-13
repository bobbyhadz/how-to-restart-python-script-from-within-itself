# How to restart a Python Script

import os
import sys


def restart():
    print('Restarting script...')

    os.execv(sys.executable, ['python'] + sys.argv)


restart()