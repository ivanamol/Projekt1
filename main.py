# """
# projekt1.py: první projekt do Engeto Online kurzu Tester s Pythonem

# author: Ivana Molnárová
# email: ivaryd@post.cz
# """

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users_passwords = """
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+ """

users_edit = users_passwords.replace("+", "").replace("-", "").replace(" ", "").split("\n")
users_edit2 = [element.lstrip("|").rstrip("|").split("|") for element in users_edit if element]
users = dict(users_edit2[1:])

username = input("username: ")
password = input("password: ")

if users.get(username) == password:
    print("-" * 40)
    print(f"""Welcome to the app, {username}
We have {len(TEXTS)} texts to be analyzed.
{"-" * 40}""")
    if TEXTS:
        text_entry = 1
    else:
        text_entry = 0
    choice_user = input(f"Enter a number btw. {text_entry} and {len(TEXTS)} to select: ")
    print("-" * 40)
    if not choice_user.isdigit():
        print("Zadali jste jiný vstup než číslo.")
    elif int(choice_user) not in range(1,len(TEXTS)+1):
        print("Takové číslo textu není v zadání.")
    elif choice_user:
        index = int(choice_user) - 1
        print(f"There are {len(TEXTS[index].split())} words in the selected text")
        titlecase = [word for word in TEXTS[index].split() if word.istitle()]
        print(f"There are {len(titlecase)} titlecase words.")
        uppercase = [word for word in TEXTS[index].split() if word.isupper()]
        print(f"There are {len(uppercase)} uppercase words.")
        lowercase = [word for word in TEXTS[index].split() if word.islower()]
        print(f"There are {len(lowercase)} lowercase words.")
        numeric = [int(word) for word in TEXTS[index].split() if word.isdigit()]
        print(f"There are {len(numeric)} numeric strings.")
        print(f"The sum of all the numbers {sum(numeric)}")
        print("-" * 40)
        print(f"""LEN|  OCCURENCES  |NR.
{"-" * 40}""")
        occurrence = [len(word) for word in TEXTS[index].replace(",","").replace(".","").split()]
        frequency = dict()
        for i in range(1, max(occurrence)+1):
            frequency = {str(i): occurrence.count(i)}
            print(f"""{i}|""".rjust(4) + f"""{'*' * frequency.get(str(i))}""".ljust(20) + f"""|{frequency.get(str(i))}""")
else:
    print("unregistered user, terminating the program..")