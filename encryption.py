#encoder
#crypte all vowel and reverse sentence

print("""
****************************************
Encryption Algorithm v1.0
****************************************

1- Encryption **************************
2- Quit ********************************

****************************************
""")

while True:
    x = input("Choose Number: ")
    print("****************************************")

    if x == "1":

        a = input("Write the Sentence: ")
        b=a.replace("a", "!")
        c=b.replace("e", "'")
        d=c.replace("ı", "^")
        e=d.replace("i", "+")
        f=e.replace("o", "%")
        g=f.replace("ö", "&")
        h=g.replace("u", "=")
        i=h.replace("ü", "?")
        j=i.replace(" ", "%20")
        print("Crypted Sentence: ",j[::-1])
        print("****************************************")

    elif x == "2":
        break

    else:
        print("Wrong Number!! Choose Again!!")
        print("****************************************")