import random

num = random.randint(1, 99)
digit = random.randint(0, 9)
counter = 0
if (num % 10 == digit):  # check tens
    counter = counter + 1
if (int(num / 10) == digit):  # check ones
    counter = counter + 1
