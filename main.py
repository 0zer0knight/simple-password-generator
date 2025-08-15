#password generator
import random
import string
def main():
    ulangprogram = True

    def ulang():
        nonlocal ulangprogram
        userulang = int(input('1,untuk ulang \n2.untuk exit = '))
        if userulang == 1:
            ulangprogram = True
        else:
            ulangprogram = False

    #mainfunction        
    def pwgenerator(length):

        if length <= 10:
            print("panjang harus lebih dari 10 \n")
        else:
            password = ''
            password += string.ascii_letters
            password += string.punctuation
            password += string.digits
            pw = []

            for i in range(1, length):
                randomchar = random.choice(password)
                pw.append(randomchar)
            
            finalpw = "".join(pw)

            return finalpw
        
    
    while ulangprogram == True:
        print("selamat datang di program password generator")

        askuser = int(input('masukan panjang password = '))
        pw = pwgenerator(askuser)
        print(f"password anda sudah dibuat \n {pw} \n\n")

        ulang()




if __name__ == "__main__":
    main()
