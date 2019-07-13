#-*-coding:UTF-8-*
from sys import exit
import random
import time
min = 1 
max = 6 
player = 0
bot = 0
print
("Welcome The Membre Game ! ")
print
player_name = input ("Enter your nickname please: ")
Cap = player_name.upper()
roll_again = "yes"
while roll_again == "yes": 
   if roll_again == "no":
      exit(0)
   print
   print ("Your Turn",player_name,)
   print
   time.sleep(1)
   print ("""Wait a few second...""")
      
   time.sleep (2)
   x = random.randint(min, max)
   y = random.randint(min, max)
   def dice (membrane):
     if membrane == 1:
      print (""" 
          _________
         |         |
         |         |  
         |    *    | 
         |         | 
         |_________|  """)         
     elif membrane == 2:
      print  ("""
          _________
         |         |
         |     *   |
         |         | 
         |   *     | 
         |_________|  """)
     elif membrane == 3:
      print ("""
          _________
         |         |
         |      *  |  
         |    *    | 
         |  *      | 
         |_________|  """) 
     elif membrane == 4:
      print ("""
          _________
         |         |
         |  *   *  |  
         |         | 
         |  *   *  | 
         |_________|  """) 
    
     elif membrane == 5:
      print (""" 
          _________
         |         |
         |  *   *  |  
         |    *    | 
         |  *   *  | 
         |_________|  """)
     elif membrane == 6:
      print ("""   
          _________
         |         |
         |  *   *  |  
         |  *   *  | 
         |  *   *  | 
         |_________|  """) 
   dice (x)
   print
   time.sleep(1)
   print
   print ("Computer's Turn")
   time.sleep(1)
   print
   print ("Rolling the die... ")
   time.sleep(2)
   dice(y)
   time.sleep(1)
   if player == bot:
      print
      print ("Ah! It's a draw",player_name,".")
      time.sleep(1)
      print
      print ("Input 'yes' to play again or 'no' to stop playing.")
      print
   elif player > bot:
      print
      print ("Congrats! You Won",player_name,"."), Cap
      time.sleep(1)
      print 
      print ("To play again, input 'yes'. To stop playing, input 'no'.")
      print
   elif player < bot:
      print
      print ("Sorry! You Lost. Try again",player_name,"."), Cap
      time.sleep(1)
      print  
      print ("To roll again, input 'yes'. To stop playing input 'no'.")
      print
   roll_again = input("Roll the die again? : ")
#Codded By Jrekin   
