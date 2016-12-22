#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 22/12/2016
# Version : 0.23
 
"""
"""
 
__version__ = "0.2.3"
 
from mrpi1 import led
from mrpi1 import ledToggle

from mrpi1 import firmwareVersion
from mrpi1 import switch

from mrpi1 import battery
from mrpi1 import temperature
from mrpi1 import groundSensor
from mrpi1 import ambiantLight
from mrpi1 import proxSensor

from mrpi1 import forward
from mrpi1 import controlEnable
from mrpi1 import controlDisable
from mrpi1 import forwardC
from mrpi1 import back
from mrpi1 import backC
from mrpi1 import stop
from mrpi1 import turnLeft
from mrpi1 import turnLeftC
from mrpi1 import turnRight
from mrpi1 import turnRightC
from mrpi1 import forward_mm
from mrpi1 import back_mm
from mrpi1 import turnRight_degree
from mrpi1 import turnLeft_degree

#from mrpi1 import robotGo

from mrpi1 import robotPositionX
from mrpi1 import robotPositionY

from mrpi1 import motorRight
from mrpi1 import motorLeft

from mrpi1 import encoderLeft
from mrpi1 import encoderRight

from mrpi1 import irReceiver

from mrpi1 import acceleroX
from mrpi1 import acceleroY
from mrpi1 import acceleroZ

from mrpi1 import playWav
from mrpi1 import playMp3
from mrpi1 import playTxt
from mrpi1 import play

from mrpi1 import writeCommand
from mrpi1 import readData

from mrpi1 import serial2Write