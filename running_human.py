import time


def clear_screen():
    for x in range(1, 20):
        print("")


O = "o"
SECONDS = 0.5


def fat(is_fat):
    if is_fat:
        return "(      )"
    else:
        return "()"


def legs(is_walking):
    if is_walking:
        return "/\\"
    else:
        return "||"


is_fat = True
is_walking = False
while (True):
    time.sleep(0.7)
    clear_screen()
    for frame in range(1, 9):
        if frame == 1 or frame == 3 or frame == 5 or frame == 7:
            is_fat = True
            is_walking = False
        else:
            is_fat = True
            is_walking = True
        print("\t" * (frame - 1), O)
        print("\t" * (frame - 1), fat(is_fat))
        print("\t" * (frame - 1), legs(is_walking))
        time.sleep(SECONDS)
        clear_screen()
    # backwards:
    for frame in range(9, 1, -1):
        if frame == 1 or frame == 2 or frame == 4 or frame == 6 or frame == 8:
            is_fat = False
            is_walking = False
        else:
            is_fat = False
            is_walking = True
        print("\t" * (frame - 1), O)
        print("\t" * (frame - 1), fat(is_fat))
        print("\t" * (frame - 1), legs(is_walking))
        time.sleep(SECONDS)
        clear_screen()
    print("The end")
