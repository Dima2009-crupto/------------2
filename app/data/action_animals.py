import json

from app.data import list_files, open_files


def remove_animal(animall_index: int) -> str:
    animals = open_files.get_animals()
    animal = animals.pop(animall_index)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Тваринка '{animal}' успішно видалено."
    return msg


def cured_animal(animall_index: int) -> str:
    animls = open_files.get_animals()
    animal = animal.pop(animall_index)

    cured_animals = open_files.get_cured_animals()
    cured_animals.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animal, file)

    with open(list_files.CURED_ANIMALS, "w", encoding="utf-8") as file:
        json.dump(cured_animals, file)

    msg = f"Тваринка '{animal}' успішно вилікувана. Дякую за співпрацю."
    return msg


def add_animal(animal: str) -> str:
    animals = open_files.get_animals()

    if animal in animals:
        msg = f"Тваринка '{animal}' вже є у списку."
        return msg

    animals.append(animal)

    with open(list_files.ANIMALS, "w", encoding="utf-8") as file:
        json.dump(animals, file)

    msg = f"Тваринка '{animal}' успішно додана."
    return msg