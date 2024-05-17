





french = {"hello": "bonjour", 
          "yes": "oui", 
          "no": "non", 
          "yellow": "jaune", 
          "dog": "chien", 
          "table": "table", 
          "book": "livre"}

german = {"hello": "hallo", 
          "yes": "jawohl", 
          "no": "nein", 
          "yellow": "gelb", 
          "dog": "hund", 
          "table": "tisch", 
          "book": "buchen"}

word = input("Please enter an English word.\nI will give you the French and German translations: ")

foundIt = False

for key in french:
    if (word == key):
        foundIt = True
        break

if (foundIt):
    print("The French translation is %s.\nThe German translation is %s." % (french[word], german[word]))
else:
    print("The English word %s isn't in my vocabulary!" % (word))