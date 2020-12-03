from dataclasses import dataclass
import pathlib


@dataclass
class ParsedPassword:
    letter: str
    min_occ: int
    max_occ: int
    password: str
    is_valid: bool = False

    def __post_init__(self):
        letter_count = self.password.count(self.letter)
        if self.min_occ <= letter_count <= self.max_occ:
            self.is_valid = True
        else:
            self.is_valid = False


def parse_password(unparsed_password: str) -> ParsedPassword:
    occurences, letter, password_str = unparsed_password.split(" ")

    parsed_pw = ParsedPassword(
        letter=letter.strip(":"),
        min_occ=int(occurences.split("-")[0]),
        max_occ=int(occurences.split("-")[-1]),
        password=password_str.strip()
    )
    return parsed_pw


def main():
    parsed_passwords = [
        parse_password(p)
        for p in pathlib.Path("puzzle_input.txt").read_text().split('\n')
        if p
    ]
    print(sum([1 for p in parsed_passwords if p.is_valid]))


if __name__ == '__main__':
    main()