from typing import NamedTuple


class Elf(NamedTuple):
    id: int
    carried_calories: int


def calorie_parser(raw_input: str) -> list[Elf]:
    chunks = raw_input.split("\n")

    elves: list[Elf] = []

    food_items: list[int] = []
    for chunk in chunks:
        if chunk == "":
            total_calories = sum(food_items)
            elf_id = len(elves)
            elves.append(Elf(id=elf_id, carried_calories=total_calories))
            food_items = []
        else:
            food_items.append(int(chunk))

    # Append our final elf.
    total_calories = sum(food_items)
    elf_id = len(elves)
    elves.append(Elf(id=elf_id, carried_calories=total_calories))

    return elves


def find_top_n_elves(elves: list[Elf], n: int = 1) -> list[Elf]:
    if n < 1:
        raise ValueError("Must be greater than 1.")
    sorted_elves = sorted(elves, key=lambda elf: elf.carried_calories, reverse=True)
    return sorted_elves[:n]


def find_top_three_total_calories(elves: list[Elf]) -> int:
    top_elves = find_top_n_elves(elves, n=3)
    return sum([x.carried_calories for x in top_elves])
