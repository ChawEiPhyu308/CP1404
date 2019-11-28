import random


def main():
    score = int(input("Please enter your score."))
    calc_result(score)
    print(random.randint(1, 100))


def calc_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif 50 < score < 90:
        print("Passable")
    elif 90 <= score <= 100:
        print("Excellent")
    else:
        print("Bad")

while True:
    main()
