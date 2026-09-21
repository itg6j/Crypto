strings = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
message = input("[+] Enter message : ")
key = int(input("[+] Ener key : "))
choose = input("[+] Do you want Encrypt or decrypt : ")
if choose == "e" : 
    cipher = ""
    for i in message : 
        if i in strings : 
            x = strings.index(i)
            new_index = (x + key) % 26
            cipher += strings[new_index]
        else : 
            cipher += i
    print("[+] Encrypted message : ",cipher)
else : 
    cipher = ""
    for i in message : 
        if i in strings : 
            x = strings.index(i)
            new_index = (x - key) % 26
            cipher += strings[new_index]
        else : 
            cipher += i
    print("[+] Decrypted message : ",cipher)
