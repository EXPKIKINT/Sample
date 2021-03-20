from sys import exit
import time
#Maps on the game
def Warehouse ():
  print("You see 4 doors which one do you take")
  Select = input(">")
  if Select == "1":
    print("As you walked through the door")
    time.sleep(0.1)
    print("You see a bunch of gold bars\n>Take One  >Proceed")
    Door_One = input(">")
    if  "Take One" in Door_One or "TakeOne" in Door_One or "takeOne" in Door_One or "take one" in Door_One or "takeone" in Door_One:
      Dead("You're bastard!")
    elif Door_One == "Proceed":
      print("You've Enter the dark room!")
      time.sleep(1)
      print(">Turn on your flashlight  >Go back")
    else:
      print("I don't know what it means")
      exit(0)
      Step = input(">")
      if "Turn on the flashlight" or "Turnontheflashlight" in Step:
       Boss_One()
      elif Step == "Go back":
        Warehouse ()
      else:
        print("I don't know what it means")
        
        
  if Select == "2":
    print("While you enter the room you see a Unknown creature shadow\n>Hide  >Inspect")
    Door_Two = input (">")
    if "inspect" in Door_Two or "Inspect" in Door_Two:
      Dead("The unknown creature is running towards to you")
    elif "Hide" in Door_Two or "hide" in Door_Two:
      Unknown_Creature = False 
      while True:
        print("You hide inside the box!")
        Tab = input("[Press any to continue]")
        print("You hide few minutes but the creature did not move\n>Get out the box  >Stay")
        INt = input (">")
        if INt == "Stay" in INt and not Unknown_Creature:
          print("While you stay in the box the creature moved near at the box")
          Unknown_Creature = False
          Moved_near()
        elif INt == "Get out the box" in INt and not Unknown_Creature:
          print("You get out in the box!\nThe Unknown Creature Shadow is near at the box!\n >Inspect >Run")
        else:
          print("I don't know what it means")
          exit(0)
          if INt == "Inspect":
            print("It's just an imagination")
            Unknown_Creature = False
            Warehouse ()
          elif INt == "Run":
            Warehouse ()
          else:
            print("I don't know what it's means")
            exit (0)
    else:
      print("I don't know what it means")
      Warehouse ()

  if Select == "3":

     print("While you enter the door 3 you see a cute dog \n > Approach  > Give him a food")
     Tamed = input(">")
     if "Approach" in Tamed or "approach" in Tamed:
        print("While you approach to the dog it vigorously attack to you!")
        Dead("You bitten by a dog!")
     elif "Give him a food" in Tamed or "give hime a food" in Tamed:
        print("You a have new pet !")
        time.sleep(1)
        print("Please give the name of the dog!")
        Dog = []
        Dog_name = input("[Name of the dog]  >")
        Dog.append(Dog_name)
        print("The name of the dog is",Dog)
        print ("The dog is playing a bone while you entering back  to the room, such a active dog!")
        time.sleep(2)
        Warehouse ()
     else:
        print ("I don't know what it means")
        exit(0)
  
  if Select == "4":
    print("You enter a empty white room!")
    time.sleep(1)
    print("> inspect  >Exit")
    Choice = input(">")
    if "inspect" in Choice or "Inspect" in Choice:
      print("While you inspect the white empty room, there was a hidden room under the floor! \n > Go inside  > Go back")
      Hidden = input (">")
      if Hidden == "Go inside":
        print("While you go inside the hidden room , there are many foods and gold! \n > Take one  > Go back")
        Stake = input(">")
        if Stake == "Take one":
          print("The bag is full of foods and golds!")
          time.sleep(1)
          print(" [ Going back to main doors ] \n ")
          
          Warehouse ()
        elif Stake == "Go back":
          Warehouse ()
        else:
          print("I don't know what it means")
          exit(0)
      elif Hidden == "Go back":
        Warehouse ()
      else:
        print("I don't know what it means")
        exit(0)

#Extension in warehouse map
def Boss_One():
  print("Hmmmm")
  time.sleep(1)
  print("Why are you here?\n>Finding Food  >Holysh*t")
  Express = input(">")
  if Express == "Finding Food":
    print("Well i will give you a bunch of food if you want..\n>Thanks >Nahh")
    Express_One = input (">")
    if Express_One == "Nahh":
      print("You're bag if full of bunch of chocolates")
    elif Express_One == "Thanks":
      Dead("Don't expect me! Kid!")
      
def Moved_near():
   time.sleep(2)
   print("While the Creature is near to you what should you do?\n> Don't Move > Run")
   Choices = input(">")
   if "Don't Move" or "Don'tMove" or "dontmoved" in Choices:
      print("While you waiting the creature moves away and never comeback")
      time.sleep(1)
      print("Good Job!")
      Warehouse()
   elif "Run" or "run" in Choices:
      Dead("You stumbled and you killed your self")
      exit(0)
   else:
      print("I don't know what it means")
      exit(0)
      
def Dead(why):
  print(why,"Good job!")
  exit(0)
Warehouse()
