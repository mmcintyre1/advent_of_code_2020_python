from dataclasses import dataclass
import pathlib


@dataclass
class ParsedPassword:
    letter: str
    match_index: int
    exclusion_index: int
    password: str
    is_valid: bool = False

    def __post_init__(self):
        match_letters = self.password[self.match_index - 1] + self.password[self.exclusion_index - 1]
        if match_letters.count(self.letter) == 1:
            self.is_valid = True
        else:
            self.is_valid = False


def parse_password(unparsed_password: str) -> ParsedPassword:
    occurences, letter, password_str = unparsed_password.split(" ")

    parsed_pw = ParsedPassword(
        letter=letter.strip(":"),
        match_index=int(occurences.split("-")[0]),
        exclusion_index=int(occurences.split("-")[-1]),
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
