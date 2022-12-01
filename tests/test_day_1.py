import pytest


from src.day_1 import calorie_parser, find_top_elf, find_top_three_total_calories, Elf


@pytest.fixture
def calorie_list():
    with open("tests/resources/day_1_input", "r") as f:
        return f.read()


def test_calorie_parser():
    calorie_list = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    parsed_elves = calorie_parser(calorie_list)
    assert len(parsed_elves) == 5
    assert parsed_elves[0] == Elf(id=0, carried_calories=6000)
    assert parsed_elves[4] == Elf(id=4, carried_calories=10000)


def test_pipeline_top_elf(calorie_list):
    parsed_elves = calorie_parser(calorie_list)
    top_elf = find_top_elf(parsed_elves)
    assert top_elf == Elf(id=188, carried_calories=67016)


def test_pipeline_top_three(calorie_list):
    parsed_elves = calorie_parser(calorie_list)
    total_calories_top_three = find_top_three_total_calories(parsed_elves)
    assert total_calories_top_three == 200116
