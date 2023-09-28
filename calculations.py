x1 = 1.0                                # line 1 -- x1 should be 1.0 ok
x2 = ((x1 ** 2) + 4) % 2                # line 2 -- x2 should be 1.0 ok
x3 = (x2 * 2.0) ** 9 ** 0.5 / 4         # line 3 -- x3 should be 2.0 ok
x4 = 10 ** x3 / 200                     # line 4 -- x4 should be 0.5 ok
x5 = x4 * (1.19 - .8 ** 2)              # line 5 -- x5 should be 0.35
x6 = int(x5 ** 4 * 160000 / 49)         # line 6 -- x6 should be 48
x7 = x6 ** 2 / 12.8                     # line 7 -- x7 should be 180.0
x8 = int(2 ** x7) >> 179                # line 8 -- x8 should be 2
x9 = (x8 | 9) / (1 / 2)                 # line 9 -- x9 should be 22.0
x10 = (x9 * (-10.11 + 15.61)) ** 0.5    # line 10 -- x10 should be 11.0

print("The answer is: ", x5)
