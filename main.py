# """
# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Richard Harsanik
# email: richard.harsanik@gmail.com
# discord: nakazeny#6042
# """
import random 
import time

def random_number() -> int:
    num_1 = random.randrange(1000,9999)
    return num_1

def input_number_func() -> int:
    while True:
        try:
            num = int(input("Enter a 4-digit number: "))               
            if len(str(num)) != 4:
                 raise ValueError
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main_game():
    cas_1 = time.time()
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    number = random_number()
    print(number)
    input_number = input_number_func()
    guess_count = 0
    with open("statistiky.txt", mode='w') as file:
        while input_number != number:
            guess_count += 1 
            bull_count = 0
            cow_count = 0
            for i in range(4):
                if str(input_number) [i] in str(number) and str(input_number).find(str(number)[i]) == i:
                    bull_count += 1 
                elif str(input_number)[i] in str(number):
                    cow_count += 1 
            file.write(f"{guess_count}.{input_number}: {bull_count} bulls,{cow_count} cows\n")    
            print(f"{bull_count}bulls,{cow_count}cows")
            input_number = input_number_func()
        file.write(f"You guessed the number in {guess_count} attempts!")
        print("Correct, you've guessed the right number in", guess_count, "guesses!")
        if guess_count <= 5:
            print("That's amazing!")
        elif guess_count > 5 and guess_count <= 10:
            print("That's average.")
        else:
            print("That's not so good.")
        cas_2 = time.time()
        duration = cas_2 - cas_1
    print("The game took", duration,"seconds to complete")
if __name__ == "__main__":   
    main_game()
