from typing import List

import logging


logging.basicConfig(level=logging.INFO)

# PART 1


def parse_text_file(filepath: str) -> List[int]:
    with open(filepath, 'r') as f:
        for line in f:
            return [int(string) for string in line.split(',')]


list_of_ints = parse_text_file('day-2.txt')

Program = List[int]


def run_intcode_program(
    list_of_ints: Program,
    noun: int = 12,
    verb: int = 2,
) -> Program:
    list_of_ints = list_of_ints[:]  # Make a copy
    list_of_ints[1] = noun
    list_of_ints[2] = verb

    for index in range(0, len(list_of_ints), 4):
        opcode = list_of_ints[index]

        if opcode == 99:
            return list_of_ints

        first_position = list_of_ints[index + 1]
        second_position = list_of_ints[index + 2]
        output_position = list_of_ints[index + 3]

        if opcode == 1:
            list_of_ints[output_position] = (
                list_of_ints[first_position] +
                list_of_ints[second_position]
            )
        if opcode == 2:
            list_of_ints[output_position] = (
                list_of_ints[first_position] *
                list_of_ints[second_position]
            )


logging.info(
    f'First value: {run_intcode_program(list_of_ints)[0]}'
)


# PART 2

EXPECTED_OUTPUT = 19690720


def find_noun_verb(list_of_ints: Program) -> Program:
    for noun in range(0, 100):
        for verb in range(0, 100):
            program = list_of_ints[:]  # Make a copy
            output = run_intcode_program(program, noun=noun, verb=verb)[0]
            if output == EXPECTED_OUTPUT:
                return (noun, verb)


noun, verb = find_noun_verb(list_of_ints)

logging.info(f'100 * noun + verb = {100 * noun + verb}')
