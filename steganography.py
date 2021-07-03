import encode, decode


def main():
    a = int(input("1. encode\n2. decode"))
    if (a == 1):
        encode.encode()
    elif (a == 2):
        print("Decoded Word :  " + decode.decode())
    else:
        raise Exception("wrong input")


if __name__ == '__main__':
    # Calling main function
    main()
