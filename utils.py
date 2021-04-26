from random import randint


def card_correct(data):
    return True
    '''if len(data) == 3:
        if data[0].isalnum() and data[0] == 16:
            if len(data[2]) == 3:
                if len(data[1]) == 5 and data[1][:2].isalnum() and data[1][3:].isalnum() and data[1][2] == "/":
                    return True
'''


def generate_dice():
    a = randint(1, 6)
    b = randint(1, 6)

    d = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅",
    }

    return (a, b, d[a] + d[b])
