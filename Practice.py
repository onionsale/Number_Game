import random
secret_num = int(random.randint(0, 10))
attempt = int()
attempt_count = 1

print("Welcome to the number game! What is your name?")
name = input("Name: ")
print("Hi there " + name + ". Let's play!")

while secret_num != attempt:
    attempt = int((input("Guess a number: ")))
    if attempt > secret_num:
        attempt_count = attempt_count + 1
        print("Try guessing a lower number: ")
    if attempt < secret_num:
        attempt_count = attempt_count + 1
        print("Try guessing a higher number: ")

print("Congrats! You guessed the correct number in " + str(attempt_count) + " tries!")
