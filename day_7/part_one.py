from dataclasses import dataclass
from textwrap import dedent
from typing import Dict, List


def main():
    rules = dedent("""
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    """)
    all_bags = rule_parser(rules)
    print(all_bags)
    # containing_colors = []
    # for bag_color, bag in all_bags.items():
    #     for contents in bag.contents:
    #         if contents.color == 'shiny gold':
    #             containing_colors.append(bag_color)


@dataclass
class Bag:
    color: str
    contents: List['Bag']
    count: int = 1


def rule_parser(rules: str) -> Dict[str, Bag]:
    bags = {}
    for rule in rules.split("\n"):
        if rule.strip():
            bag_color = rule.split("bags")[0].strip()
            unparsed_contents = rule.split("contain")[-1]
            bags[bag_color] = Bag(
                color=bag_color,
                count=1,
                contents=parse_contents(unparsed_contents)
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
            count=bag_count
        ))

    return bag_contents


def which_bagger(bags):
    pass


if __name__ == '__main__':
    main()
