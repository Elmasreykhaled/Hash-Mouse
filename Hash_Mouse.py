import hashlib

# main body
def main():
    while True:
        print("please choose from The following Options(1,2,3)\n1)Encrypt\n2)Decrypt\n3)quit")
        option = int(input("Please Enter The Number You had choose \n>>"))
        if option == 1:
            text = input("Please Enter Your text >>")
            while text == "":
                print("Error, Empty Text <???>")
                text = input("Please Enter Your text >>")
                if text != "":
                    break
            hash_type = input('Please Enter Type >>')
            while hash_type == "":
                print("Error, Empty Type <???>")
                hash_type = input("Please Enter Your Type >>")
                if hash_type != "":
                    break
            hashed_text = encrypt_text(text, hash_type)
            print("Done\n", hashed_text, "\n")
        elif option == 2:
            hash_text = input("Please Enter Your hash text >>")
            while hash_text == "":
                print("Error, Empty Text <???>")
                hash_text = input("Please Enter Your hash text >>")
                if hash_text != "":
                    break
            hash_type = input('Please Enter Type >>')
            while hash_type == "":
                print("Error, Empty Type <???>")
                hash_type = input("Please Enter Your Type >>")
                if hash_type != "":
                    break
            word_list = input("Please Enter The wordlist path >>")
            while word_list == "":
                print("Error, Empty path <???>")
                word_list = input("Please Enter The wordlist path >>")
                if word_list != "":
                    break
            lines = read_from_playlist(word_list)
            for line in lines:
                line = line.rstrip("\n")
                hash_from_wordlist = encrypt_text(line, hash_type)
                if hash_from_wordlist == hash_text:
                    print(f"Founded \n {hash_from_wordlist} ----> {line} \n")
                    break
            else:
                print("Not Found in your wordlist Try some salt. \n")
        elif option == 3:
            break
    print("Thank you")

#Functions

def encrypt_text(in_text, hash_type):
    enc_text = in_text.encode('utf-8')
    new_hash = hashlib.new(hash_type)
    new_hash.update(enc_text)
    hash_text = new_hash.hexdigest()
    return hash_text

def read_from_playlist(path):
    file = open(path, "r")
    return file.readlines()


if __name__ == '__main__':
    main()
