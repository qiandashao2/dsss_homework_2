import random


def Generate_randam_integer(min, max):
    """
    It generates an integer in the range.

    Parameters:
        min/max: integer.


    returns:
        a random integer.
    """
    return random.randint(min, max)


def Operator():
    """
    It generates a random operator.

    returns :
        a random operator.

    """
    return random.choice(['+', '-', '*'])


def Result(n1, n2, op):
    """
    It gives the result of the program

    Parameters:
        n1: integer.
        The first operand.
        n2: integer.
        The second operand.
        op: operator.

    Returns:
        the result of the program.
    """
    p = f"{n1} {op} {n2}"
    if op == '+': a = n1 + n2
    elif op == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    It is a small quiz ,printing out some instructions and giving the feedback
    """
    score = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(t_q)):
        n1 = Generate_randam_integer(1, 10);
        n2 = Generate_randam_integer(1, 6);
        op = Operator()

        PROBLEM, ANSWER = Result(n1, n2, op)
        print(f"\nQuestion: {PROBLEM}")

        while True:
            try:
                useranswer = int(input("Your answer: "))
                break
            except ValueError:
                print("Please give me an integer!")


        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1) # When the answer is right then give the players one point.
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.") # When the answer is wrong then the player get #
            # nothing.

    print(f"\nGame over! Your score is: {score}/{t_q}")

if __name__ == "__main__":
    math_quiz()
