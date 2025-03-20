def check_is_palindrome(number):
    if number == number[::-1]:
        num = int(number)
        for x in range(100, 1000):
            if num % x == 0:
                y = num // x
                if 100 <= y <= 999:
                    return True
    return False


def closest_smaller_palindrome(number):
    number = str(number)
    while True:
        number = str(number)
        if number == number[::-1] and check_is_palindrome(number):
            return str(number)
        else:
            number = int(number)
            number -= 1


def main():
    t = int(input().strip())
    numbers = []
    if 1 <= t <= 100:
        for i in range(t):
            n = int(input().strip())
            if 101101 <= n <= 1000000:
                n = str(n)
                numbers.append(n)

    palindrome = []
    for number in numbers:
        if check_is_palindrome(number):
            palindrome.append(number)
        else:
            close_pal = closest_smaller_palindrome(number)
            palindrome.append(close_pal)

    for pal in palindrome:
        print(pal)


if __name__ == '__main__':
    main()
