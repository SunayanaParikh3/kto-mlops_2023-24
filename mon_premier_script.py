message = "C'est mon premier script !!!"
print(message)

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
more_than_seven = 0 
for prenom in prenoms:
    if len(prenom) > 7:
        more_than_seven += 1
        print("Prenom supérieur à 7 : " + prenom)
    else:
        print("Prenom inférieur ou égal à 7 : " + prenom)
print("Nombre de prénoms supérieurs à 7 : " + str(more_than_seven))


def saluer(nom: str) -> str:
    return "Bonjour " + nom

print(saluer("Alice")) 
print(saluer("Sunayana"))


"""
Count names with more than seven letters
"""
def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

prenoms = ["Sunayana", "krishna", "Suvarna", "Dhavalesh", "Khushboo", "Cassandre"]
print("Nombre de prénoms supérieurs à 7 : " + str(names(prenoms=prenoms)))