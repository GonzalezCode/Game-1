##################################################
#SETUP SECTION OF THE GAME
##################################################
def setup():
#this function draws our boat and places
#the turtle at the start position
  boat = makeWorld(500,500)
  turtle = makeTurtle(boat)
  drawBoat(turtle,boat)
  turnRight(turtle)
  room=setRoom("quay")
  moveTo(turtle,room['x'],room['y'])
  help()
  intro()
  return turtle
#end setup

def square(turtle,x,y):
#Function to draw a square, called by drawBoat
  penUp(turtle)
  moveTo(turtle,x,y)
  penDown(turtle)

  for x in range(0,4):
    forward(turtle,50)
    turnLeft(turtle)
#end square

def drawBoat(turtle,boat):
#Function to draw the representation of our boat
  #Make sure the pen is down
  penDown(turtle)

  #starting square
  square0 = square(turtle,140,275)

  #50x50 squares, spaced 10 apart, 5x3 grid
  for x in range(200,500,60):
    for y in range(215,395,60):
      square(turtle,x,y)
#end drawBoat


def help():
  print "At each point in the game you will be told which directions"
  print "you can go.  You MAY be able to go:"
  print "(R)ight,(L)eft,(U)p,(D)own,(E)xit, or ask for (H)elp. \n"

def intro():
  print "Let us pretend this is the year 1630, and that we have"
  print "purchased a passage on the Talbot, one of the English galleons"
  print "sailing from Southampton Harbour this spring with John Winthrop???s"
  print "fleet of eleven ships. We feel confident about this vessel because"
  print "she transported another group of Puritan planters to New England"
  print "last year in 1629. The Massachusetts Bay Company rented her for"
  print "the expedition.\n"
##################################################
#END --- SETUP SECTION OF THE GAME
##################################################



def choice(valid):
#Evaluate the players entry for validity
  #Add the exit and help choices to the list

  #Prompt and take the first letter of the input
  choice = requestString("What choice do you make?: ")

  #Evaluate that the choice is a valid choice
  while True:
    if choice in valid and choice!='x' and choice!='y':
      return valid[choice]
    elif choice == 'e':
      return choice
    elif choice == 'h':
      help()
      choice = requestString("SEE THE HELP MESSAGE: \n What choice do you make?: ")
    else:
      choice = requestString("What choice do you make?: ")
#end choice

def quay():
  #remove the options that are NOT valid for your room

  #Add the story about your room
  print "You are standing on the quay at the base on the"
  print "gangplank ready to board the talbot along with 120"
  print "passengers and 30 crew.  150 people in all.\n"
  print "Are they all as pure as their puritan credentials?\n"

  print "(U)P: You're only at the beginning"
  print "your only choice is to board the Talbot."
  print "(E)xit: or you can quit.\n"
#end quay

def deck():

  #Add the story about your room
  print "You are on the main deck of the Talbot."
  print "Welcome aboard!!!\n"

  print "(R)IGHT: Aft castle"
  print "(L)EFT: Forecastle"
  print "(D)OWN: Gun Deck"

  #based on the choice return where does the player move to?
  #CALL LOCATION FROM SETUP
#end room

def setRoom(name):
  "'Use dictionary to map values to room, x and y coordinates,function call, and room name to direction'"
  if name=="quay":
    return {"room":"quay",'x':115,'y':250,'call':quay(),'u':"deck"}
  elif name=="deck":
    return {"room":"deck",'x':175,'y':250,'call':deck(),'d':"quay",'r':"aftCastle",'l':"foreCastle"}
  elif name == "foreCastle":
    return {"room":"foreCastle",'x':175,'y':190,'call':foreCastle(),'u':"crew",'r':"deck"}
  elif name == "aftCastle":
    return {"room":"aftCastle",'x':175,'y':310,'call':aftCastle(),'u':"gunPowder",'l':"deck"}
  elif name == "gunDeck":
    return {"room":"gunDeck",'x':235,'y':250,'call':gunDeck(),'u':"tweenDeck",'d':"deck",'l':"crew",'r':"gunPowder"}
  elif name == "crew":
    return {"room":"crew",'x':235,'y':190,'call':crew(),'u':"bunk",'d':"foreCastle",'r':"gunDeck"}
  elif name == "gunPowder":
    return {"room":"gunPowder",'x':235,'y':310,'call':gunPowder(),'u':"passengers",'d':"aftCastle",'l':"gunDeck"}
  elif name == "tweenDeck":
    return {"room":"tweenDeck",'x':295,'y':250,'call':tweenDeck(),'u':"hold",'d':"gunDeck",'l':"bunk",'r':"passengers"}
  elif name == "bunk":
    return {"room":"bunk",'x':295,'y':190,'call':bunk(),'u':"food",'d':"crew",'r':"tweenDeck"}
  elif name == "passengers":
    return {"room":"passengers",'x':295,'y':310,'call':passengers(),'u':"livestock",'d':"gunPowder",'l':"tweenDeck"}
  elif name == "hold":
    return {"room":"hold",'x':355,'y':250,'call':hold(),'u':"ballast",'d':"tweenDeck",'l':"food",'r':"livestock"}
  elif name == "food":
    return {"room":"food",'x':355,'y':190,'call':food(),'u':"rum",'d':"bunk",'r':"hold"}
  elif name == "livestock":
    return {"room":"livestock",'x':355,'y':310,'call':livestock(),'u':"gold",'d':"passengers",'l':"hold"}
  elif name == "ballast":
    return {"room":"ballast",'x':415,'y':250,'call':ballast(),'d':"hold",'l':"rum",'r':"gold"}
  elif name == "rum":
    return {"room":"rum",'x':415,'y':190,'call':rum(),'r':"ballast",'d':"food"}
  elif name == "gold":
    return {"room":"gold",'x':415,'y':310,'call':gold(),'l':"ballast",'d':"livestock"}


def playGame():
  turtle = setup()
  room = setRoom("quay")
  result=''
  while result != 'e':
    room['call']													              	#return direction
    result=choice(room)
    if result != 'e':
      room=setRoom(result)													#set room to direction
      moveTo(turtle,room['x'],room['y'])

playGame()
