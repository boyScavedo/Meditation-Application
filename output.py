import time
import os


def timer_input():
    os.system("cls")
    choice = int(
        input("What time frame?\n1. Seconds\n2. Minute\n3. Minute & Second\n:")
    )
    match (choice):
        case 1:
            return int(input("How Many Seconds: "))
        case 2:
            return int(input("How Many Minutes: ")) * 60
        case 3:
            minute = int(input("How many minutes: ")) * 60
            seconds = int(input("How many seconds: "))
            return minute + seconds
        case _:
            print("Wrong Input")
            input()
            exit(0)


def timer_ongoing(final_time, epoch_time, timer):
    elapsed_time = 0
    remaining_time = timer
    while final_time >= epoch_time:
        os.system("cls")
        print("Remaining Time =", remaining_time, "Elapsed Time =", elapsed_time)
        elapsed_time += 1
        remaining_time -= 1
        epoch_time += 1
        time.sleep(1)
    os.system("cls")
    print("Timer Finished after", elapsed_time, "seconds")
    return elapsed_time


if __name__ == "__main__":
    timer = timer_input()
    final_time = time.time() + timer
    epoch_time = time.time()
    elapsed_time = timer_ongoing(final_time, epoch_time, timer)
    input()
