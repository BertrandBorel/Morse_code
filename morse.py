'''Morse avec Python
Objectifs =   - traduire une prhase en morse
              - traduire du morse en phrase'''


# 1 : traduire une phrase en morse
    # alphabet en morse
    # dans un dico
    # pour chaque lettre, chercher l'équivalent en morse
    # traduire


# dictionnaire contenant le code morse
code_morse = { 
                # lettres :
                "A" : "._", "B":"_...", "C":"_._.", "D":"_..", "E":".", "F":".._.", "G":"__.", "H":"....", "I":"..", 
                "J":".___", "K":"_._", "L":"._..", "M":"__", "N":"_.", "O":"___", "P":".__.", "Q":"__._", "R":"._.",
                 "S":"...", "T":"_", "U":".._", "V":"..._", "W":".__", "X":"_.._", "Y":"_.__", "Z":"__..", 
                 # espace (*2) de séparation des mots :
                 " ":"  ",
                 # chiffres :
                 "1":".____", "2":"..___", "3":"...__", "4":"...._", "5":".....", "6":"_....", "7":"__...", "8":"___..", "9":"____.", "0":"_____"
                 
                 }


test = "Ceci est un test"
# adapter format lettre
test_2 = test.upper()
sortie = ""

for x in test_2 :
    sortie = sortie + x + " "

print(sortie)

mn = ""

for x in sortie :
    if x == " ":
        pass
    else :
        valeur = code_morse[x]
        # lol = sortie.replace(x, valeur)
        mn = mn + valeur + " "

print(mn)







# # traduire l'inverse
# #avec test_2
# for x in test_2 :
#     # cle = .keys()[code_morse.values().index(x)] 
#     # print(cle)
#     # print(list(code_morse.keys())[list(code_morse.values()).index(x)])
#     print(x)