from dataclasses import dataclass
import pathlib
from typing import Optional


def main():
    passport_data = pathlib.Path("puzzle_input.txt").read_text()
    print(len(passport_parser(passport_data)))


@dataclass
class PassportFields:
    byr = 'birth_year'
    iyr = 'issue_year'
    eyr = 'expiration_year'
    hcl = 'hair_color'
    hgt = 'height'
    ecl = 'eye_color'
    pid = 'passport_id'
    cid = 'country_id'


class Passport:
    def __init__(
            self,
            passport_id: int,
            birth_year: int,
            issue_year: int,
            expiration_year: int,
            hair_color: str,
            height: str,
            eye_color: str,
            country_id: Optional[int] = None
    ):
        self._passport_id = passport_id
        self._birth_year = birth_year
        self._issue_year = issue_year
        self._expiration_year = expiration_year
        self._hair_color = hair_color
        self._height = height
        self._eye_color = eye_color
        self._country_id = country_id


def passport_parser(passport_data: str):
    passport_data = passport_data.replace('\n', ' ')
    unparsed_passport_data = [
        x.strip().split(' ')
        for x in passport_data.split('  ')
        if x.strip()
    ]
    passports = []
    for passport_group in unparsed_passport_data:
        passport_fields = {}
        for key_value_pair in passport_group:
            key, value = key_value_pair.split(":")
            passport_fields[getattr(PassportFields, key)] = value
        try:
            passports.append(Passport(**passport_fields))
        except TypeError:
            pass

    return passports


if __name__ == '__main__':
    main()
