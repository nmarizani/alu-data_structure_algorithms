def find_unique_integers(integers):
    unique_integers = []
    seen = [False] * (max(integers) + 1)  # Array to mark seen integers
    for num in integers:
        if not seen[num]:
            unique_integers.append(num)
            seen[num] = True
    return unique_integers

def custom_sort(integers):
    for i in range(len(integers)):
        for j in range(i + 1, len(integers)):
            if integers[i] > integers[j]:
                integers[i], integers[j] = integers[j], integers[i]

def main(input_file, output_file):
    # Read integers from input file, preserving order
    integers = []
    seen_integers = []  # To keep track of seen integers
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Check if the line is not empty
                try:
                    integer = int(line)
                    if integer not in seen_integers:
                        integers.append(integer)
                        seen_integers.append(integer)
                except ValueError:
                    pass  # Ignore non-integer values

    # Find unique integers and arrange them in increasing order
    unique_integers = find_unique_integers(integers)
    custom_sort(unique_integers)

    # Write unique integers to output file, in increasing order
    with open(output_file, 'w') as f:
        for integer in unique_integers:
            f.write(str(integer) + '\n')

if __name__ == "__main__":
    input_file = "small_sample_input_02.txt"
    output_file = "small_sample_output_02.txt"
    main(input_file, output_file)

