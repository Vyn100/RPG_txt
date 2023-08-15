# Gère les dialogues et les interactions avec les PNJ.

def start_dialogue(character, dialogue):
    print(f"{character.name}: {dialogue}")

def ask_question(question, options):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = int(input("Choisissez une option : "))
    return choice
