def main():
    n = 10
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(0, n):
        c = a + b
        print(c)
        a = b
        b = c

# ... a b c  #c = a + b
#       a b c #c = a + b
#         a b c ....

main()
