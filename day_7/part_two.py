import pathlib
from dataclasses import dataclass
from textwrap import dedent
from typing import List


def main():
    rules = pathlib.Path('puzzle_input.txt').read_text()
    all_bags = bag_builder(rules)
    bag_count = bag_handler(all_bags, target_bag='shiny gold')
    print(bag_count)


@dataclass
class Bag:
    color: str
    contents: List['Bag']
    count: int = 1


def bag_builder(rules: str):
    bags = {}
    for bag in rules.split("\n"):
        if bag.strip():
            bag_color, bag_contents = bag.split("bags contain")
            bags[bag_color.strip()] = Bag(
                color=bag_color.strip(),
                count=1,
                contents=parse_contents(bag_contents)
            )
    return bags


def parse_contents(unparsed_contents) -> List[Bag]:
    bag_contents = []
    for bag in unparsed_contents.split(", "):

        if "no other" in bag:
            break

        bag_count, *bag_color, _ = bag.strip().split("bag")[0].split(" ")
        bag_contents.append(Bag(
            color=" ".join(bag_color).strip(),
            contents=[],
            count=int(bag_count)
        ))

    return bag_contents


def bag_handler(bags, target_bag):
    bag_count = 0

    def count_contents(target):
        nonlocal bag_count
        for bag_contents in bags[target].contents:
            if not bag_contents:
                pass
            bag_count += bag_contents.count
            for x in range(0, bag_contents.count):
                count_contents(bag_contents.color)

    count_contents(target_bag)
    return bag_count


if __name__ == '__main__':
    main()
