import random 

def start_game():
    name = input("Welcome~ Please enter your name: ")
    print("Hi {}, let the game begins!".format(name))
    #https://docs.python.org/2/library/random.html
    random_number = random.randrange(1,99) 

    while True:
        answer = input("Please enter a number: ")
        answer = int(answer)
        too_low = answer < random_number
        too_high = answer > random_number
    
        if answer == random_number:
            print("CONGRATULATIONS {}!! {} is the CORRECT Guess!!".format(name, answer))
            break
        
        elif too_low:
            print("Too Low")
            continue
            
        elif too_high:
            print("Too High")
            continue
        
start_game() 