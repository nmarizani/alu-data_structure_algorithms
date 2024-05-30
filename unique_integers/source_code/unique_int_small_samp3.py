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

    # Sort the list of integers in increasing order
    custom_sort(integers)

    # Write unique integers to output file, in increasing order
    with open(output_file, 'w') as f:
        for integer in integers:
            f.write(str(integer) + '\n')

if __name__ == "__main__":
    input_file = "small_sample_input_03.txt"
    output_file = "small_sample_output_03.txt"
    main(input_file, output_file)