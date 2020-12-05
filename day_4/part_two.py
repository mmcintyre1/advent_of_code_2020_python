from collections import namedtuple
from dataclasses import dataclass
import pathlib
import re


def main():
    passport_data = pathlib.Path("puzzle_input.txt").read_text()
    print(len(passport_parser(passport_data)))


def is_valid_year(year, start=1900, end=2000) -> bool:
    try:
        return start <= int(year) <= end
    except ValueError:
        return False


YearRange = namedtuple('year_range', ['start', 'end'])


@dataclass
class PassportValidation:
    birth_year = YearRange(1920, 2002)
    issue_year = YearRange(2010, 2020)
    expiration_year = YearRange(2020, 2030)
    passport_id_pattern = re.compile('^[0-9]{9}$')
    hair_color_pattern = re.compile('^#[a-fA-F0-9]{6}$')
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


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
    pv = PassportValidation

    def __init__(self, passport_id, birth_year, issue_year, expiration_year, hair_color, height, eye_color,
                 country_id=None):
        self.passport_id = self.validate_pattern(passport_id, self.pv.passport_id_pattern)
        self.birth_year = self.validate_year(
            birth_year, start=self.pv.birth_year.start, end=self.pv.birth_year.end
        )
        self.issue_year = self.validate_year(
            issue_year, start=self.pv.issue_year.start, end=self.pv.issue_year.end
        )
        self.expiration_year = self.validate_year(
            expiration_year, start=self.pv.expiration_year.start, end=self.pv.expiration_year.end
        )
        self.hair_color = self.validate_pattern(hair_color, self.pv.hair_color_pattern)
        self.height = self.validate_height(height)
        self.eye_color = self.validate_membership(eye_color, self.pv.eye_colors)
        self.country_id = country_id

    @staticmethod
    def validate_pattern(text, pattern):
        if not re.match(pattern, text):
            raise ValueError(f"{text} does not match {pattern}")

    @staticmethod
    def validate_year(year, start=1900, end=2000):
        if not start <= int(year) <= end:
            raise ValueError(f"{year} is not between {start} and {end}")

    @staticmethod
    def validate_height(height):
        measure_constraints = {
            'cm': (150, 193),
            'in': (59, 76)
        }
        m = height[-2:]
        h = int(height[:-2])
        try:
            if not measure_constraints[m][0] <= h <= measure_constraints[m][1]:
                raise ValueError(f'Height in {m} must fall between {measure_constraints[m]}')
        except KeyError:
            raise ValueError('No unit of measurement supplied.')

    @staticmethod
    def validate_membership(item, group):
        if item not in group:
            raise ValueError(f"{item} not in {group}")


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
            print(passport_fields)
            passports.append(Passport(**passport_fields))
        except (TypeError, ValueError) as e:
            pass

    return passports


if __name__ == '__main__':
    main()
