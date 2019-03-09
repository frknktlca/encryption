
#encryption all vowel and reverse the sentence

print("""
****************************************
Encryption Algorithm v1.1
****************************************

1- Encryption **************************
2- Decoded *****************************
3- Quit ********************************

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
        f=e.replace("o", "/")
        g=f.replace("ö", "&")
        h=g.replace("u", "=")
        i=h.replace("ü", "?")
        j=i.replace(" ", "%20")
        print("Crypted Sentence: ",j[::-1])
        print("****************************************")

    elif x == "2":

        a = input("Write the Sentence for Decode: ")
        b = a.replace("!", "a")
        c = b.replace("'", "e")
        d = c.replace("^", "ı")
        e = d.replace("+", "i")
        f = e.replace("/", "o")
        g = f.replace("&", "ö")
        h = g.replace("=", "u")
        i = h.replace("?", "ü")
        j = i.replace("02%", " ")
        print("Decoded Sentence: ", j[::-1])
        print("****************************************")


    elif x == "3":
        break

    else:
        print("Wrong Number!! Choose Again!!")
        print("****************************************")