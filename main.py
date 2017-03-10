from input import import_input
from solution import solve
from output import export_output
from ranking import rank


def main():
    total = 0
    input_files = []
    input_files.append("me_at_the_zoo.in")
    # input_files.append("trending_today.in")
    # input_files.append("videos_worth_spreading.in")
    # input_files.append("kittens.in")

    for file in input_files:
        print("Working on: [{}]".format(file))

        import_input("inputs/{}".format(file))
        print("- Import finished")

        solve()
        print("- Solve finished")

        export_output("outputs/{}".format(file.replace(".in", ".out")))
        print("- Export finished")

        print()

        print("Ranking ...")
        score = rank("inputs/{}".format(file), "outputs/{}".format(file.replace(".in", ".out")))
        print("Score: {}".format(score))
        total += score

    print("Your final score is: {}".format(total))


if __name__ == '__main__':
    main()
