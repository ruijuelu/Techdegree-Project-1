import random 

def start_game(best_score = 6):
    print("~~Welcome to the Guessing Game!!~~\n **Best score so far: {} Attempts**".format(best_score))  
    
    name = input("Please enter your name: ")
    print("Hi {}, let the game begins!".format(name))
    #https://docs.python.org/2/library/random.html
    random_number = random.randrange(1,99)  
    
    attempts = 0 #number of tries starts from 0
    
    while True:
        
        try: #exception raise to prevent player from entering a string
            answer = input("Please enter a numerical value between 0 to 99: ")
            answer = int(answer)
            if answer == str:
                raise ValueError
        except ValueError:
            continue
    
        try: #exception raise to prevent player from entering a number smaller than 0 or bigger than 99
            if answer <= 0 or answer >= 100:
                raise ValueError
        except ValueError:
            print(random_number)
            print("Invalid entry, Please try again..")
            continue
        
        attempts += 1 #attempts of += 1 placed below both the exceptions, as exception should not be counted as an attempt
        print(attempts) #####remove it @ final check before FINAL SUBMISSION!!!####
        too_low = answer < random_number
        too_high = answer > random_number
    
        if answer == random_number:
            print("CONGRATULATIONS {}!! {} is the CORRECT Guess!!".format(name, answer))
            print("Your total attempts: {}".format(attempts))
            
            if attempts < best_score: #IF loop applied to update lastest best_score
                best_score = attempts 
                print("WOW!! You SET A NEW Record!!")
#googled tips on https://stackoverflow.com/questions/35873400/python-guessing-game explained by Developer: eskaev                
            else:
                best_score = min(attempts, best_score)
        
            question = input("Press 'Y' if you like to play again. Press any key to end the game: ") 
            
            if question.upper() == "Y":
                print("////Game Resetting////")
                    
                start_game(best_score)
                
            else:
                print("////GAME OVER!////") 
                break #end the nested IF loop
                   
            break #end the WHILE loop
        
        elif too_low:
            print(random_number)#####remove it @ final check before FINAL SUBMISSION!!!####
            print("It's Too Low")
            continue
            
        elif too_high:
            print(random_number)#####remove it @ final check before FINAL SUBMISSION!!!####
            print("It's Too High")
            continue
            
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.        
    start_game() 
