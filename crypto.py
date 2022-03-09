from affine import Affine
from vigenere import Vigenere
from hill import Hill



menu_options = {
    1: "Mã hoá bằng Affine",
    2: "Giải mã bằng Affine",
    3: "Mã hoá bằng Vigenere",
    4: "Giải mã bằng Vigenere",
    5: "Mã hoá bằng Hill",
    6: "Giải mã bằng Hill",
    0: "Exit"
}


def print_menu():
    for key in menu_options.keys():
        print(key, "--", menu_options[key])


def option1():
    a = Affine()
    key = []

    print("Hãy nhập giá trị của key k=[a, b]:")
    tmp = ["a", "b"]
    for element in tmp:
        ele = int(input(element + "= "))
        key.append(ele)
    print("Đây là Key: [{}, {}]".format(key[0],key[1]))

    plaintxt = input("Hãy nhập bản rõ: ")

    print("Đây là bản mã: " + a.enc(plain_text=plaintxt, key=key))


def option2():
    a = Affine()
    key = []

    print("Hãy nhập giá trị của key k=[a, b]:")
    tmp = ["a", "b"]
    for element in tmp:
        ele = int(input(element + "= "))
        key.append(ele)
    print("Đây là Key: [{}, {}]".format(key[0],key[1]))

    ciphertxt = input("Hãy nhập bản mã: ")

    print("Đây là bản rõ: " + a.dec(cipher_text=ciphertxt, key=key))


def option3():
    #print(vig.enc("Information security", "cipher", 6))
    v = Vigenere()
    key = input("Hãy nhập giá trị của key k='string': ")

    m = int(input("Hãy nhập m tương ứng với key: "))

    plaintxt = input("Hãy nhập bản rõ: ")

    print("Đây là bản mã: " + v.enc(plain_text=plaintxt, key=key,m=m))


def option4():
    v = Vigenere()
    key = input("Hãy nhập giá trị của key k='string': ")

    m = int(input("Hãy nhập m tương ứng với key: "))

    ciphertxt = input("Hãy nhập bản mã: ")

    print("Đây là bản rõ: " + v.dec(cipher_text=ciphertxt, key=key,m=m))


def option5():
    h = Hill()

    key = []
    print("Hãy nhập giá trị của key k=[a, b][c, d]:")
    tmp = ["a", "b", "c", "d"]
    run = 0
    a = []  
    for element in tmp:
        ele = int(input(element + "= "))
        a.append(ele)
        run += 1
        if run == 2:
            key.append(a)
            run = 0
            a=[]
    print("Đây là Key: [{}, {}][{}, {}]".format(key[0][0],key[0][1],key[1][0],key[1][1]))

    plaintxt = input("Hãy nhập bản rõ: ")

    print("Đây là bản mã: " + h.enc(plain_text=plaintxt, key=key))


def option6():
    h = Hill()

    key = []
    print("Hãy nhập giá trị của key k=[a, b][c, d]:")
    tmp = ["a", "b", "c", "d"]
    run = 0
    a = []  
    for element in tmp:
        ele = int(input(element + "= "))
        a.append(ele)
        run += 1
        if run == 2:
            key.append(a)
            run = 0
            a=[]
    print("Đây là Key: [{}, {}][{}, {}]".format(key[0][0],key[0][1],key[1][0],key[1][1]))

    ciphertxt = input("Hãy nhập bản mã: ")
    
    print("Đây là bản rõ: " + h.dec(cipher_text=ciphertxt, key=key))


if __name__ == "__main__":
    while True:
        print_menu()
        option = ""
        try:
            option = int(input("Enter your choice: "))
        except:
            print("Wrong input. Please enter a number ...")
        # Check what choice was entered and act accordingly
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        if option == 4:
            option4()
        elif option == 5:
            option5()
        elif option == 6:
            option6()
        elif option == 0:
            print("Thanks message before exiting")
            exit()
        else:
            print("Invalid option. Please enter a number between 1 and 4.")
