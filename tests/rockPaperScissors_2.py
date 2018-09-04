from random import choice

def winner():
          u = (input("Let's play Rock-Paper-Scissors : ）")).lower()
          c = choice(["rock","scissors","paper"])
          if c == u:
               print( "draw")
          elif (c == "rock" and u == "scissors") or (c == "scissors" and u == "paper") or (c == "paper" and u == "rock"):
               print("You lost")
          elif (u == "rock" and c == "scissors") or (u == "scissors" and c == "paper") or (u == "paper" and c == "rock"):
               print("You won")
          else:
               print("I don't understand : (")
               winner()

          while True:
                    temp = input("Do you wanna play again?").lower()
                    if temp == "yes":
                         winner()
                    elif temp == 'no':
                         break
                    else:
                         print("I don't understand : (")

winner()
