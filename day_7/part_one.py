import pathlib
from dataclasses import dataclass
from typing import List


def main():
    rules = pathlib.Path('puzzle_input.txt').read_text()
    all_bags = bag_builder(rules)
    matching_bags = bag_handler(all_bags, target_bag='shiny gold')
    print(len(matching_bags))


@dataclass
class Bag:
    color: str
    contents: List['Bag']
    count: int = 1


def bag_builder(rules: str):
    bags = []
    for bag in rules.split("\n"):
        if bag.strip():
            bag_color, bag_contents = bag.split("bags contain")
            bags.append(Bag(
                color=bag_color.strip(),
                count=1,
                contents=parse_contents(bag_contents)
            ))
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
            count=bag_count
        ))

    return bag_contents


def bag_handler(bags, target_bag):
    containing_bags = []

    def find_parent_bag(target):
        for bag in bags:
            if not bag.contents:
                pass
            for contents in bag.contents:
                if contents.color == target:
                    containing_bags.append(bag.color)
                    find_parent_bag(bag.color)

    find_parent_bag(target_bag)

    return set(containing_bags)


if __name__ == '__main__':
    main()
