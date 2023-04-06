import random

number = random.randint(1,100)
end = False
resp="o"
resp_not ="n"


print("Bienvenue au jeux de hasard \u2764 !".upper())
question = str(input("Veux tu jouer avec moi ? : "))
response = str(question)

if response==resp:
    name = str(input("Entrez votre pseudo : "))
    while not end:
        user_response = int(input("Entrez un nombre entre 1 et 100 : "))
        user_response = int(user_response)

        if user_response > number:
            print(f"C'est moins {name} ! ")
        elif user_response < number:
            print(f"C'est plus {name} ! ")
        else:
            print(f"Vous avez gagner bravo {name} \u2764 !")
            end = True
elif response == resp_not:
    print("Merci et Aurevoir \u2764 !")
else:
    print("Répondez par oui(o) ou non(n) !")






