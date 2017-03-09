from input import *
from solution import *
from output import *


def main():
    input_files = ["me_at_the_zoo.in"]

    for file in input_files:
        print("Working on: [" + file + "]")

        import_input("inputs/" + file)
        print("- Import finished")

        solve()
        print("- Solve finished")

        export_output("outputs/" + file.replace(".in", ".out"))
        print("- Export finished")

        print()


if __name__ == '__main__':
    main()
