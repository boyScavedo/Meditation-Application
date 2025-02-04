import output
import file_reader
import time

# TODO: Add docstrings and documentation before pushing to github


def program():
    timer = output.timer_input()

    final_time = time.time() + timer
    epoch_time = time.time()

    elapsed_time = output.timer_ongoing(final_time, epoch_time, timer)

    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday

    file_reader.file_writer(year, month, day, elapsed_time)


program()
while True:
    choice = input("\nAgain? (y/n): ")
    match (choice):
        case "y":
            program()
        case "n":
            print("Exiting")
            break
        case _:
            print("Wrong input! Exiting")
            break
