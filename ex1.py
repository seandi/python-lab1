# test

while True:

    n1 = input("Insert first number: ")
    if not n1:
        break
    n2 = input("Insert second number: ")
    if not n2:
        break
    try:
        n1 = float(n1)
        n2 = float(n2)
        print(n1, "+", n2, "=", n1+n2)
    except ValueError:
        print("Input number is not valid")
        continue

