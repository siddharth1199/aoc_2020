import sys


def parse_input(path):
    with open(path) as f:
        inst = [line.strip().split(' ') for line in f]
    return inst


def part_1(instructions):
    hz, depth = 0, 0

    for comm, units in instructions:

        if comm == 'forward':
            hz += int(units)

        elif comm == 'down':
            depth += int(units)

        elif comm == 'up':
            depth -= int(units)

    print('Part 1 = ', hz * depth)


def part_2(instructions):
    horizontal, depth = 0, 0
    aim = 0

    for comm, units in instructions:

        if comm == 'forward':
            horizontal += int(units)
            depth += int(units) * aim

        elif comm == 'down':
            aim += int(units)

        elif comm == 'up':
            aim -= int(units)

    print('Answer 2: ', horizontal * depth)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python [script.py] [input.txt]')
    else:
        inst = parse_input(str(sys.argv[1]))
        part_1(inst)
        part_2(inst)
