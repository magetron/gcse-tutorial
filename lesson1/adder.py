def add(a, b):
    return a + b

def main():
    a = int(input('a:'))
    b = int(input('b:'))
    print('%d + %d = %d' % (a, b, add(a, b)))

main()
