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
        self._passport_id = passport_id
        self._birth_year = birth_year
        self._issue_year = issue_year
        self._expiration_year = expiration_year
        self._hair_color = hair_color
        self._height = height
        self._eye_color = eye_color
        self._country_id = country_id

    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, passport_id):
        if re.match('^[0-9]{9}$', passport_id) is None:
            raise ValueError(f'Password must match regex: ^[0-9]{9}$')
        self._passport_id = passport_id

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, birth_year):
        if not is_valid_year(birth_year, self.pv.birth_year.start, self.pv.birth_year.end):
            raise ValueError(f'Birth Year must fall between {self.pv.birth_year.start} and {self.pv.birth_year.end}')
        self._birth_year = birth_year

    @property
    def issue_year(self):
        return self._issue_year

    @issue_year.setter
    def issue_year(self, issue_year):
        if not is_valid_year(issue_year, self.pv.issue_year.start, self.pv.issue_year.end):
            raise ValueError(f'Issue Year must fall between {self.pv.issue_year.start} and {self.pv.issue_year.end}')
        self._issue_year = issue_year

    @property
    def expiration_year(self):
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        if not is_valid_year(expiration_year, self.pv.expiration_year.start, self.pv.expiration_year.end):
            raise ValueError(
                f'Expiration Year must fall between {self.pv.expiration_year.start} and {self.pv.expiration_year.end}'
            )
        self._expiration_year = expiration_year

    @property
    def hair_color(self):
        return self._hair_color

    @hair_color.setter
    def hair_color(self, hair_color):
        if re.match('^#[a-fA-F0-9]{6}$', hair_color) is None:
            raise ValueError(f'Hair color must match regex ^#[a-fA-F0-9]{6}$')
        self._hair_color = hair_color

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        measure_constraints = {
            'cm': (150, 193),
            'in': (59, 76)
        }
        m = height[-2:]
        h = int(height[:-2])
        if not measure_constraints[m][0] <= h <= measure_constraints[m][1]:
            raise ValueError(f'Height in {m} must fall between {measure_constraints[m]}')
        self._height = height

    @property
    def eye_color(self):
        return self._eye_color

    @eye_color.setter
    def eye_color(self, eye_color):
        if eye_color not in self.pv.eye_colors:
            raise ValueError(f'Eye color must be one of {self.pv.eye_colors}')
        self._eye_color = eye_color


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
        except (TypeError, ValueError) as e:
            print(e)
    print(passports)

    return passports


if __name__ == '__main__':
    main()
