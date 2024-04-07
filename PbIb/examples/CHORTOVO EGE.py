from fnmatch import *
count = 0
for i in range (498915816123, 408015016023, -12300):
    if fnmatch(str(i), '4?8?15?16?23'):
        if i % 123 == 42:
                if count <= 1:
                    print(i)
                count += 1
print(count)
