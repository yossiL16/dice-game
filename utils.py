import  random


def roll_two_d6():
    toss_result = []
    toss_result.append(random.randint(1,6))
    toss_result.append(random.randint(1,6))

    return toss_result

def is_bust(score):

    if score > 100:
        return False

def is_exact_100(score):
    if score == 100:
        return True

def closer_to_target(a, b , target = 100):

    if (target - a) > (target - b):
        print(2)
    elif (target - b) > (target - a):
        print(1)
    else:
        return None





