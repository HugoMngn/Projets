# question 1:
def sapin(n):
    for i in range(0, n, 1):
        print((n-i-1)*".", (2*i+1)*"^", (n-i-1)*".")


sapin(int(input("combien de dimension? ")))


# question 2:
def compte(chaine, char):
    tot = int(0)
    z = len(chaine)
    for i in chaine:
        if i == char:
            tot = int(tot+1)
    print(char, "apparait:", tot, "fois sur", z, "caractères.")
    return (tot)


compte(str(input("rentrez une chaine de caractere (a,b,c,d uniquement): ")),
       str(input("rentrez la lettre rechercher: ")))


def frequence(chaine):
    z = len(chaine)
    frequence = [round(compte(chaine, 'a')/z, 3),  round(compte(chaine, 'b') / z, 3),
                 round(compte(chaine, 'c')/z, 3), round(compte(chaine, 'd')/z, 3)]
    print("Frequence pour a, b, c & d: ", frequence)


frequence(str(input("rentrez une chaine de caractere (a,b,c,d uniquement): ")))


# question 3:
def chiffre_cesar(texte, decalage):
    code = ""
    for l in texte:
        if l.isalpha():
            new = (ord(l) - ord('a') + decalage) % 26 + ord('a')
        else:
            new = ord(l)
        code += chr(new)
    print(texte, "devient :", code)
    return code


chiffre_cesar(str(input("rentrer le message a codé (minuscule seulement): ")),
              int(input("entrer le décalage: ")))


def dechiffre_cesar(message_chiffre, decalage):
    trad = ""
    for l in message_chiffre:
        if l.isalpha():
            new = (ord(l) - ord('a') - decalage) % 26 + ord('a')
        else:
            new = ord(l)
        trad += chr(new)
    print(message_chiffre, "est :", trad)
    return trad


dechiffre_cesar(str(input("rentrer le message a décodé (minuscule seulement): ")),
                int(input("entrer le décalage: ")))
