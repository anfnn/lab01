def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(f"Наибольший общий делитель: {gcd(num1, num2)}")
