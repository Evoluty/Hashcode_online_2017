from input import *
from solution import *
from output import *


def main():
    input_files = []
    input_files.append("me_at_the_zoo.in")
    input_files.append("trending_today.in")
    input_files.append("videos_worth_spreading.in")
    input_files.append("kittens.in")

    for file in input_files:
        print("Working on: [{}]".format(file))

        import_input("inputs/{}".format(file))
        print("- Import finished")

        solve()
        print("- Solve finished")

        export_output("outputs/{}".format(file.replace(".in", ".out")))
        print("- Export finished")

        print()


if __name__ == '__main__':
    main()
