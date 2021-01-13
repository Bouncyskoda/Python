from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
# set player to 0,0,0
mc.player.setPos(0,0,0)
# CLEAR AN AREA WITH AIR TO BUILD
air = 0
mc.setBlocks(-24,0,-36,24,64,36,air) # clear some air                                               
x, y, z = mc.player.getPos()
xyzString = str(x)+" , "+str(y)+" , "+str(z)
print(xyzString)
# mc.setBlock (x,y,z, material_number) 

# Lay blocks flat on ground
mc.setBlock(0,0,0,35,0) 	# WHITE   0,  0,  0
mc.setBlock(1,0,1,35,1) 	# ORANGE  2,  0,  2
mc.setBlock(-1,0,1,35,6) 	# PINK   -2,  0,  2
mc.setBlock(-1,0,-1,35,3) 	# BLUE   -2,  0, -2
mc.setBlock(1,0,-1,35,4)  	# YELLOW  2,  0, -2
mc.setBlock(1,1,1,35,2)		# PURPLE
mc.setBlock(3,2,2,35,4)		# YELLOW
mc.setBlock(5,4,5,35,2)		# PURPLE
mc.setBlock(8,5,8,35,2)		# PURPLE
mc.setBlock(10,3,9,35,9)	# CYAN
mc.setBlock(10,3,11,35,3)	# BLUE
mc.setBlock(10,4,15,35,7)	# GRAY
mc.setBlock(14,4,15,35,8)	# LIGHT GRAY
mc.setBlock(15,4,15,41)		# GOLD


#  Lay block in the air 
mc.setBlock(0,2,2,35,0) 	# WHITE   0,  0,  0
mc.setBlock(1,3,2,35,1) 	# ORANGE  2,  0,  2
mc.setBlock(-1,3,2,35,6) 	# PINK   -2,  0,  2
mc.setBlock(-1,1,2,35,3) 	# BLUE   -2,  0, -2
mc.setBlock(1,1,2,35,4)  	# YELLOW  2,  0, -2
mc.setBlock(1,1,5,35,3)  	# BLUE 
mc.setBlock(1,0,4,35,3)  	# BLUE 
mc.setBlock(2,1,1,35,8) 	# LIGHT GRAY
mc.setBlock(2,1,2,35,7)		# MAGENTA
mc.setBlock(2,1,0,35,5)		# GREEN
mc.setBlock(3,8,3,35,2)		# PURPLE
mc.setBlock(2,7,3,35,1)		# ORANGE
mc.setBlock(1,8,3,35,0)		# WHITE
mc.setBlock(4,7,3,35,9)		# CYAN	
mc.setBlock(5,8,3,35,3)		# BLUE
mc.setBlock(0,7,3,35,2)		# PURPLE

	 

mc.player.setPos(0,0,-5)
