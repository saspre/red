
#uart.py

import Adafruit_BBIO.UART as UART
import os.path
# UARTS on the BBB
# UART    RX  TX  CTS RTS Device
# UART1   P9_26   P9_24   P9_20   P9_19   /dev/ttyO1
# UART2   P9_22   P9_21                   /dev/ttyO2
# UART3   P9_42   P8_36   P8_34           /dev/ttyO3
# UART4   P9_11   P9_13   P8_35   P8_33   /dev/ttyO4
# UART5   P8_38   P8_37   P8_31   P8_32   /dev/ttyO5


def loadUart(name):
    UART.setup(name)
   
def loadUartFromConfig(config):
    pass