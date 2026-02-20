def read_numbers(filename):
    numbers = []
    
    try:
        with open(filename, "r") as file:
            print("File opened successfully")

            for line in file:
                line = line.strip()
                if line:
                    numbers.append(int(line))

        print("Data loaded")
        return numbers

    except FileNotFoundError:
        print("numbers.txt not found!")
        return []


def compute_values(numbers):
    total_values = len(numbers)
    total_sum = sum(numbers)

    if total_values != 0:
        average = total_sum / total_values
    else:
        average = 0

    print("Computation completed")
    return total_values, total_sum, average


def write_log(filename, count, total_sum, average):
    with open(filename, "a") as log:
        log.write("File opened successfully\n")
        log.write(f"Read {count} numbers\n")
        log.write(f"Sum: {total_sum}\n")
        log.write(f"Average: {average}\n")
        log.write("Processing completed\n")
        log.write("-------------------------\n")


numbers_list = read_numbers("numbers.txt")

if numbers_list:
    count, total_sum, average = compute_values(numbers_list)
    write_log("results.log", count, total_sum, average)