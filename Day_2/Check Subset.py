for i in range (int(input())):
                    _, a = input(), set(input().split())
                    _, b = input(), set(input().split())
                    print(b.intersection(a) == a)