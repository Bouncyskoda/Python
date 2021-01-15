from mcpi.minecraft import Minecraft
from mcpi import block
import random
import time


mc = Minecraft.create()
# set player to 0,0,0
mc.player.setPos(0,0,0)
# CLEAR AN AREA WITH AIR TO BUILD
air = 0
mc.setBlocks(-24,0,-36,24,64,36,air) # clear some air                                               
mc.player.setPos(0,0,0)
for n in range (0,70):

	h = random.randint(0,10) #x
	k = random.randint(0,10)	#y
	l = random.randint(0,12)	#z
	c = random.randint(1,15)	#color
	mc.setBlock(h,k,l,35,c)
	time.sleep(5)
