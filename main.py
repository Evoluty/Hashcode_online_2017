from output import *


def main():
    input_files = ["file1", "file2", "file3"]

    for file in input_files:
        print("Working on: [" + file + "]")

        import_input("inputs/" + file)
        print("- Import finished")

        solve()
        print("- Solve finished")

        export_output("outputs/" + file)
        print("- Export finished")

        print()


if __name__ == '__main__':
    main()
