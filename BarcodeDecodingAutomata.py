import random

code = "".join(random.choices(population=['LD', 'LDD', 'L', 'D'], weights=[0.49, 0.49, 0.1, 0.1], k=20))
print(code)
