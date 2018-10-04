import random
import time

def start_game(best_score = 6):
    print("""
    ////////////////////////////////////////////
    /////// WELCOME TO THE GUESSING GAME ///////
    ////////////////////////////////////////////
    /////////////// INSTRUCTIONS: //////////////
    // Guess a random number between 1 to 99 ///
    // Lesser the attempts the better you are //
    ////////////////////////////////////////////
    """)
    
    print("Best score so far: {} Attempt(s)".format(best_score))  
    time.sleep(2) #capture the attention of player to read the game instructions & best score.
    
    while True:
        commence_game = input("Press 'ENTER' to start the game ")
        try: #ensure that player only key 'enter' to commence the game
            if commence_game != '':
                raise ValueError #print statement not require, as input instruction is repetitive
            break
        except ValueError:
            continue

    time.sleep(1) #provide a brief waiting time for player before the next set of instructions 
    print("LET THE GAME BEGINS!")
    #https://docs.python.org/2/library/random.html
    random_number = random.randrange(1,100)  
    
    attempts = 0 #number of tries starts from 0
    
    while True:
        
        try: #exception raise to prevent player from entering a string
            answer = input("Please enter a numerical value between 0 to 99: ")
            answer = int(answer)
            if answer == str:
                raise ValueError
        except ValueError:
            print("Invalid entry, Please try again..")
            continue 
    
        try: #exception raise to prevent player from entering a number smaller than 0 or bigger than 99
            if answer <= 0 or answer >= 100:
                raise ValueError
        except ValueError:
            print("Invalid entry, Please try again..")
            continue
        
        attempts += 1 #attempts of += 1 placed below both the exceptions, as exception should not be counted as an attempt
        too_low = answer < random_number
        too_high = answer > random_number
    
        if answer == random_number:
            time.sleep(1.5)
            print("CONGRATULATIONS!! {} is the CORRECT Guess!!".format(answer))
            print("Your total attempts: {}".format(attempts))
            
            if attempts < best_score: #IF loop applied to update lastest best_score
                best_score = attempts 
                print("""
                *****************************************
                *** WOW!! YOU HAVE SET A NEW RECORD!! ***
                *****************************************
                """)
#googled tips on https://stackoverflow.com/questions/35873400/python-guessing-game explained by Developer: eskaev                
            else:
                best_score = min(attempts, best_score)
        
            question = input("Press 'Y' if you like to play again. If not press ANY key to end the game: ") 
            
            if question.upper() == "Y":
                print("""
                //////////////////////////////
                //// ...GAME RESETTING... ////
                //////////////////////////////
                """)
                
                time.sleep(3) #create a pause effect to signify a start of a new game session
                    
                start_game(best_score)
                
            else:
                time.sleep(2) #create an effect to suggest closure, set at 2 sec for pause effect (signifying to player that system is discontinuing the game) 
                print("""
                /////////////////////
                //// !GAME OVER! ////
                /////////////////////
                """) 
                break #end the nested IF loop
                   
            break #end the WHILE loop
        
        elif too_low:
            time.sleep(1.5)#creates the effect of anticipation
            print("It's higher")
            continue
            
        elif too_high:
            time.sleep(1.5) #creates the effect of anticipation
            print("It's lower")
            continue
            
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.        
    start_game()