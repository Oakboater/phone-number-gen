import random
def phone_number():
    phone1 = ''.join(str(random.randint(0, 9)) for _ in range(3))
    phone2 = ''.join(str(random.randint(0, 9)) for _ in range(4))
    phonenumber = "(353)" + phone1 + "-" + phone2
    print(phonenumber)


if __name__ == "__main__":
    phone_number()