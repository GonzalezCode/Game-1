def room():
  #remove the options that are NOT valid for your room
  valid = ['u','d','r','l']
  
  #Add the story about your room
  print "Your room's story"
  
  print "(R)IGHT: "
  print "(L)EFT: "
  print "(U)P: "
  print "(D)OWN: "
  
  #see what they decided to do
  result = choice(valid)
  print result
  
  #based on the choice return where does the player move to?
  #CALL LOCATION FROM SETUP
  if result == 'r':
    name =
    location(turtle,name)
    return name
  elif result == 'l':
    name = 
    location(turtle,name)
    return name
  elif result == 'u':
    name = 
    location(turtle,name)
    return name
  elif result == 'd':
    name =
    location(turtle,name)
    return name
#end room                                                                     