# https://www.programiz.com/python-programming/examples/prime-number
def is_prime(num):
    # define a flag variable
    flag = False

    if num == 0 or num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            print(num, "is not a prime number")
            return False
        else:
            print(num, "is a prime number")
            return True


def is_circular_prime(n):
    list_n = list(map(int, str(n)))
    liRes = []
    for i in range(len(list_n)):
        liRes.extend(list_n[i:] + list_n[:i])
        num = int(''.join(map(str, liRes)))

        if (is_prime(num)):
            liRes.clear()
            continue
        else:
            print(is_prime(num))
            liRes.clear()
            return False

    return True


is_circular_prime(197)  # True
is_circular_prime(23)  # False
is_circular_prime(13)  # True
is_circular_prime(89)  # False
is_circular_prime(1193)  # True