import sys

if len(sys.argv) < 2:
    print("Without nothing I aint doing anything")
    sys.exit()

string = ' '.join(sys.argv[1::])
print(string.swapcase()[::-1])