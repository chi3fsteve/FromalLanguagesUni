"""
With LD representing 0 and LDD representing 1, translate the generated code into binary.
The decoder is supposed to use no variable other then the one that is being processed.
"""

# import random

while True:
    ch = input()
    if ch == "D":
        continue
    elif ch == "L":
        while True:
            ch = input()
            if ch == "L":
                continue
            elif ch == "D":
                ch = input()
                if ch == "L":
                    print("0")
                    continue
                elif ch == "D":
                    ch = input()
                    if ch == "L":
                        print("1")
                        continue
                    elif ch == "D":
                        break

"""Below is the first version of the algorithm I created, before I figured out how to
structure it correctly (so it fits the description)"""

# code = "".join(random.choices(population=['LD', 'LDD', 'L', 'D'], weights=[0.49, 0.49, 0.1, 0.1], k=20))
# print(code)

# state = "START"
#
# for i in range(len(code)):
#     if state == "START":
#         if code[i] == "D":
#             continue
#         elif code[i] == "L":
#             state = "ONE"
#             continue
#     elif state == "ONE":
#         if code[i] == "L":
#             continue
#         elif code[i] == "D":
#             state = "TWO"
#             continue
#     elif state == "TWO":
#         if code[i] == "L":
#             print("0")
#             state = "ONE"
#             continue
#         elif code[i] == "D":
#             print("1")
#             state = "THREE"
#             continue
#     elif state == "THREE":
#         if code[i] == "L":
#             state = "ONE"
#             continue
#         elif code[i] == "D":
#             state = "START"
#             continue
