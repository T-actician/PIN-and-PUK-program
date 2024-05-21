
def main():
    pin = '1234'
    puk = '4567'
    pin_count = 0
    puk_count = 0
    max_pin_attempts = 3
    max_puk_attempts = 5
    blocked = False

    while not blocked:
        if pin_count < max_pin_attempts:
            user_pin = input("Enter PIN to unlock the phone:")
            if user_pin == pin:
                print("PIN accepted, Nokia!")
                break
            else:
                pin_count += 1
                if pin_count < max_pin_attempts:
                    print(f"Incorrect PIN! Trials remaining: {max_pin_attempts - pin_count}")
                else:
                    print("PIN blocked!")
        else:
            while puk_count < max_puk_attempts:
                user_puk = input("Enter PUK to unlock:")
                if user_puk == puk:
                    print("PUK accepted!")
                    pin_count = 0
                    break
                else:
                    puk_count += 1
                    if puk_count < max_puk_attempts:
                        print(f"Incorrect PUK! Trials remaining: {max_puk_attempts - puk_count}")

            if puk_count >= max_puk_attempts:
                print("Line permanently blocked!")
                blocked = True


if __name__ == '__main__':
    main()


