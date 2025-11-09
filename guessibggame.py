import random

def number_guessing_game(): 
     
    while True:
        print("WELCOME TO NUMBER GUESSING GAME-->THE RANGE VALUE SHOULD BE BETWEEN 1 TO 100")
        try:
            low =int(input("enter the low range value: "))
            high =int(input("enter the high input value: "))
            if low<1 or high > 100 or low>=high:
                print("enter a value within the range ")
                continue 
            break 
        except ValueError:
            print("enter a valid input")

    guess_num=random.randint(low,high)
    print(f"i am thinking a number between{low} and {high},can you guess it?")
    attempts=0

    while True:
        try:
            guess_user=int(input("enter the number you guess: "))
            attempts +=1
            if guess_user<guess_num:
                print("the guessed num is low ")
            elif guess_user>guess_num:
                print("the guessed num is high")
            else:
                print(f"CONGRATULATIONS! you guessed the num correctly {guess_num} in {attempts} attempts")
                break
        except ValueError:
            print("enter a valid input")

if __name__ == "__main__":
    number_guessing_game()




