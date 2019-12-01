import logging
import math

from typing import List

logging.basicConfig(level=logging.INFO)

# PART 1 : What is the sum of the fuel requirements?


def parse_txt_file(filepath: str) -> List[int]:
    with open(filepath) as f:
        return [int(mass) for mass in f.readlines()]


mass_of_nodes = parse_txt_file('day-1.txt')


def fuel_required_given_mass(mass: int) -> int:
    return math.floor(mass / 3) - 2


def total_fuel_required(mass_of_nodes: List[int]) -> int:
    fuels_required = [fuel_required_given_mass(mass) for mass in mass_of_nodes]
    return sum(fuels_required)


logging.info(f'Total fuel required: {total_fuel_required(mass_of_nodes)}')


# PART 2: What is the sum of the fuel requirements for all the modules?

def get_fuel_required_for_all_modules(mass_of_nodes: List[int]) -> int:
    fuel_required_for_modules = []
    for mass in mass_of_nodes:
        fuel_required = fuel_required_given_mass(mass)
        fuel_required_for_modules.append(fuel_required_given_mass(mass))
        while fuel_required > 0:
            fuel_required = fuel_required_given_mass(fuel_required)
            if fuel_required > 0:
                fuel_required_for_modules.append(fuel_required)
    return sum(fuel_required_for_modules)


logging.info(
    f'Total fuel required for all modules: {get_fuel_required_for_all_modules(mass_of_nodes)}'
)