"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status
"""


def main():

    score = float(input("Enter score: "))
    scores(score)


def scores(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
