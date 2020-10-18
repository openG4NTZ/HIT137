import turtle
##### Binary Tree Class #####
class binary_Tree(object):
	# Initial function that holds initial coordinates of the tree
	def __init__(self,x,y):
		self.x=x
		self.y=y
	# adjust_position function changes direction and position of turtle
	# it is used for adjusting position of the tree
	def adjust_position(self,direction,x,y,angle):
		# this part of function adjust x coordinates (left - right)
		turtle.up()
		turtle.left(angle)
		turtle.forward(x)
		# this part of function adjust y coordinates ( Up - Down)
		if direction=="up":
			turtle.left(90)
			turtle.forward(y)
			turtle.right(90)
		elif direction=="down":
			turtle.right(90)
			turtle.forward(y)
			turtle.left(90)
		turtle.down()

	# draw_circle function drawn a circle within given direction, range, angle and distance
	# it is used for drawing tree nodes
	def draw_circle(self,direction,rng,angle,distance):
		for i in range(rng):
			if direction=="right":	# draws circle clockwise
				turtle.right(angle)
			elif direction=="left":	# draws circle anti-clockwise
				turtle.left(angle)  # bigger angle smaller circle
			turtle.forward(distance) # biggere distance bigger circle

	# draw_number function draws numbers from 0 to 9 inside the nodes.
	# After number is drawn position of turtle is adjusted
	def draw_number(self,number):
		if number=='1':
			turtle.forward(6)
			turtle.left(180)
			turtle.forward(3)
			turtle.right(90)
			turtle.forward(12)
			turtle.left(135)
			turtle.forward(5)
			self.adjust_position("down",10.54,8.46,135)
		elif number=='2':
			turtle.forward(7)
			turtle.left(180)
			turtle.forward(7)
			turtle.right(125)
			turtle.forward(10)
			turtle.left(5)
			self.draw_circle("left",12,20,1)
			self.adjust_position("down",11.17,7.33,60)
		elif number=='3':
			self.adjust_position("down",1,0,0)
			turtle.up()
			turtle.left(90)
			turtle.forward(1)
			turtle.right(90)
			turtle.down()
			turtle.right(60)
			self.draw_circle("left",12,20,1)
			turtle.right(115)
			turtle.forward(7)
			turtle.left(115)
			turtle.forward(6)
			turtle.left(90)
			turtle.forward(3)
			self.adjust_position("down",11.34,9.03,90)
		elif number=='4':
			self.adjust_position("down",4,0,0)
			turtle.left(90)
			turtle.forward(3)
			turtle.right(90)
			turtle.forward(2)
			turtle.left(180)
			turtle.forward(7)
			turtle.right(120)
			turtle.forward(10)
			turtle.right(150)
			turtle.forward(10)
			self.adjust_position("down",6,1.66,90)
		elif number=='5':
			turtle.forward(3)
			self.draw_circle("left",10,18,1)
			turtle.forward(2)
			turtle.right(90)
			turtle.forward(6)
			turtle.right(90)
			turtle.forward(6)
			self.adjust_position("down",6,12.31,0)
		elif number=='6':
			self.adjust_position("down",3,0,0)
			self.draw_circle("left",20,18,1)
			self.draw_circle("left",15,18,1)
			turtle.left(180)
			turtle.forward(6)
			self.draw_circle("right",10,15,1)
			self.adjust_position("down",5.32,9.63,60)
		elif number=='7':
			self.adjust_position("down",1,0,0)
			turtle.left(75)
			turtle.forward(12)
			turtle.left(105)
			turtle.forward(7)
			self.adjust_position("down",10.89,11.59,180)
		elif number=='8':
			self.adjust_position("down",3,0,0)
			self.draw_circle("left",20,18,1)
			self.draw_circle("left",10,18,1)
			turtle.right(180)
			turtle.forward(1)
			self.draw_circle("left",18,20,1)
			self.adjust_position("down",8,6.31,0)
		elif number=='9':
			self.adjust_position("down",2,0,0)
			turtle.left(75)
			turtle.forward(10)
			turtle.left(15)
			self.draw_circle("left",20,18,1)
			self.adjust_position("down",5.41,9.66,270)
		elif number=='0':
			self.adjust_position("up",8,3,0)
			turtle.right(90)
			self.draw_circle("right",12,15,1)
			turtle.forward(5)
			self.draw_circle("right",12,15,1)
			turtle.forward(5)
			self.adjust_position("down",5,3,90)

	# create_new_node creates new nodes and leaves on the tree
	# First it goes to location of new node
	# Then it draws a circle and the number inside the circle
	def create_new_node(self,x,y,number):
		turtle.up()
		turtle.goto(x,y) # goto new location of the node
		turtle.down()
		self.draw_circle("left",36,10,5)  # draw a circle for the node
		turtle.up()
		digit=len(str(selected_data)) # caculate the number of digit that will be written inside the circle
		if digit==4:
			turtle.goto(x-23,y+21)	# adjust the location of the number if it is 4 digit
		elif digit==3:
			turtle.goto(x-16,y+21)	# adjust the location of the number if it is 3 digit
		elif digit==2:
			turtle.goto(x-10,y+21)	# adjust the location of the number if it is 2 digit
		elif digit==1:
			turtle.goto((x-4),y+21)	# adjust the location of the number if it is 1 digit
		turtle.down()
		for z in number:
			self.draw_number(z)		# draw the number inside the circle
		turtle.up()
		turtle.goto(x,y)			# go back to starting point
		turtle.down()
	# create_new_edge creates new edge on the Tree depending on the side
	# First, it goes to  starting point
	# Then, it draws the edge depending on the side and layer of the tree
	def create_new_edge(self,x,y,edge,layer):
		turtle.up()
		turtle.goto(x,y)
		turtle.down()
		turtle.setheading(0)
		if edge== "left":			## if it is left edge draw "/"
			if layer ==1:			## if it is first layer draw bigger and wider
				turtle.right(170)
				turtle.forward(200)
			elif layer==2:
				turtle.right(130)
				turtle.forward(150)
			elif layer==3:
				turtle.right(110)
				turtle.forward(120)
		elif edge == "right":		## if it is right edge draw "\"
			if layer ==1:			## if it is first layer draw bigger and wider
				turtle.right(10)
				turtle.forward(200)
			elif layer==2:
				turtle.right(50)
				turtle.forward(150)
			elif layer==3:
				turtle.right(70)
				turtle.forward(120)
		turtle.setheading(0)

	# create_new_child creates new child on the tree,
	# First it draws new edge under the parent,
	# Then it draws new node and the new number in it
	# Finnaly, it saves the data which is written inside the node, and location of new child in Tdata and TXY
	def create_new_child(self,x,y,side,layer,newData,index1,index2):
		if side=="left":
			turtle.color("green")
		else:
			turtle.color("red")
		self.create_new_edge(x,y,side,layer)		# it draws new edge under the parent,
		self.create_new_node(turtle.position()[0]+4,turtle.position()[1]-57,newData) #it draws new node and the new number in it
		Tdata[index1][index2]=newData 				# save the data in Tdata to compare with next data
		Txy[index1][index2]=turtle.position()		# save the location of turtle to use when it is a parent
##### binary Tree Class #####

##### Constant Defines #####
Tree_first_level=1		# Tree level 1 it is used for identifying the which level we are drawing the child
Tree_second_level=2		# Tree level 2
Tree_third_level=3		# Tree level 3
x= 0					# x location in the Txy array
y= 1					# y locataion in the Txy array
Empty=0					# Empty means it is empty
##### Constant Defines #####

##### Local Variable Defines #####
# Txy holds location of Binary search tree nodes
# Tdata holds values of Binary search tree nodes
#####     0. layer        1. layer                  2. layer                            3. layer                    ######
Txy =   [ [(0,0)],     [(0,0),(0,0)],     [(0,0),(0,0),(0,0),(0,0)],    [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]]
Tdata = [   [0],           [0,0],                  [0,0,0,0],                         [0,0,0,0,0,0,0,0]                  ]
#####     0. layer        1. layer                  2. layer                            3. layer                    ######
##### Local Variable Defines #####

loadWindow = turtle.Screen()
loadWindow.bgcolor("#000000")
turtle.shape("turtle")
turtle.color("purple")
turtle.pensize(2)
turtle.speed(10) # turtle speed is chosen 10 to draw faster

# myTree new class is defined and starting point set to (x,y) --> (-10,250)
myTree=binary_Tree(-10,250)

print("-----------------------------------------------------------------")
print("- This application is developed to visualize Binary Search Tree -")
print("-----------------------------------------------------------------\n")
# get a sequence from user to draw binary tree
user_input=input("Insert an array to constructe BST.\n(Use coma between two values such as:8,4,12,2,6,10,14,1,3,5,7,9,11,13,15..) \nUser Input: ")
splited_data=user_input.split(",") # User input splited to separete numbers by checking comas in the string.

# for loop to read each number in splited_data
for i in range(len(splited_data)):
	selected_data=splited_data[i]	# select each item one by one
	if Tdata[0][0]==Empty:			# check if parent node is created
		myTree.create_new_node(myTree.x, myTree.y,selected_data)  # create new node at the starting location
		Txy[0][0]=turtle.position()		# Save the location of parent node
		Tdata[0][0]=selected_data		# Save the value of parent node

	###### After this point it searches a location to draw next child ##########
	elif int(selected_data)<int(Tdata[0][0]):			# check if new data is smaller than parent
		if Tdata[1][0]==Empty:								# check if there is no child under the parent
			myTree.create_new_child(Txy[0][0][x],Txy[0][0][y],"left",Tree_first_level,selected_data,1,0)    	# create new child on the first level under the parent on the left side
		else: 											# if there is already a child check second layer of tree
			if int(selected_data)<int(Tdata[1][0]): 		# check if new data is smaller than parent
				if Tdata[2][0]==Empty:							# check if there is no child under the parent
					myTree.create_new_child(Txy[1][0][x],Txy[1][0][y],"left",Tree_second_level,selected_data,2,0)       # create new child on the second level under the parent on the left side
				else:											# if there is already a child check third layer of the tree
					if int(selected_data)<int(Tdata[2][0]):		 	# check if new data is smaller than parent
						if Tdata[3][0]==Empty:							# check if there is no child under the parent
							myTree.create_new_child(Txy[2][0][x],Txy[2][0][y],"left",Tree_third_level,selected_data,3,0)	# create new child on the third level under the parent on the left side
					else:  											# check if new data is bigger than parent
						if Tdata[3][1]==Empty:							# check if there is no child under the parent
							myTree.create_new_child(Txy[2][0][x],Txy[2][0][y],"right",Tree_third_level,selected_data,3,1)  	# create new child on the third level under the parent on the right side
			else: 											# check if new data is bigger than parent
				if Tdata[2][1]==Empty: 							# check if there is no child under the parent
					myTree.create_new_child(Txy[1][0][x],Txy[1][0][y],"right",Tree_second_level,selected_data,2,1)	  	# create new child on the second level under the parent on the right side
				else: 											# if there is already a child check third layer of the tree
					if int(selected_data)>int(Tdata[2][1]):  		# check if new data is bigger than parent
						if Tdata[3][2]==Empty:							# check if there is no child under the parent
							myTree.create_new_child(Txy[2][1][x],Txy[2][1][y],"right",Tree_third_level,selected_data,3,2)  	# create new child on the third level under the parent on the right side
					else: 											# check if new data is smaller than parent
						if Tdata[3][3]==Empty:							# check if there is no child under the parent
							myTree.create_new_child(Txy[2][1][x],Txy[2][1][y],"left",Tree_third_level,selected_data,3,3) 	# create new child on the third level under the parent on the left side
	elif int(selected_data)>int(Tdata[0][0]):  			# check if new data is bigger than parent
		if Tdata[1][1]==Empty: 								# check if there is no child under the parent
			myTree.create_new_child(Txy[0][0][x],Txy[0][0][y],"right",Tree_first_level,selected_data,1,1)   	# create new child on the first level under the parent on the left side
		else: 												# if there is already a child check second layer
			if int(selected_data)>int(Tdata[1][1]):  			# check if new data is bigger than parent
				if Tdata[2][2]==Empty: 								# check if there is no child under the parent
					myTree.create_new_child(Txy[1][1][x],Txy[1][1][y],"right",Tree_second_level,selected_data,2,2)  	# create new child on the second level under the parent on the right side
				else: 											# if there is already a child check third layer
					if int(selected_data)>int(Tdata[2][2]):  		# check if new data is bigger than parent
						if Tdata[3][4]==Empty: 							# check if there is no child under the parent
							myTree.create_new_child(Txy[2][2][x],Txy[2][2][y],"right",Tree_third_level,selected_data,3,4) 	# create new child on the third level under the parent on the right side
					else:  											# check if new data is smaller than parent
						if Tdata[3][5]==Empty: 							# check if there is no child under the parent
							myTree.create_new_child(Txy[2][2][x],Txy[2][2][y],"left",Tree_third_level,selected_data,3,5) 	# create new child on the third level under the parent on the left side
			else:												# check if new data is smaller than parent
				if Tdata[2][3]==Empty: 								# check if there is no child under the parent
					myTree.create_new_child(Txy[1][1][x],Txy[1][1][y],"left",Tree_second_level,selected_data,2,3) 	# create new child on the second level under the parent on the left side
				else: 												# if there is already a child check third layer
					if int(selected_data)<int(Tdata[2][3]):  			# check if new data is smaller than parent
						if Tdata[3][6]==Empty: 								# check if there is no child under the parent
							myTree.create_new_child(Txy[2][3][x],Txy[2][3][y],"left",Tree_third_level,selected_data,3,6) 	# create new child on the third level under the parent on the left side
					else:  												# check if new data is bigger than parent
						if Tdata[3][7]==Empty: 								# check if there is no child under the parent
							myTree.create_new_child(Txy[2][3][x],Txy[2][3][y],"right",Tree_third_level,selected_data,3,7) 	# create new child on the third level under the parent on the right side
turtle.hideturtle()
delay = input("Press enter to finish.")
