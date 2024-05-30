def main(input_file, output_file):
    # Read integers from input file, preserving order
    integers = []
    max_integer = 1026
    seen_integers = []  # To keep track of seen integers
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Check if the line is not empty
                try:
                    integer = int(line)
                    integers.append(integer)
                    if integer > max_integer:
                        max_integer = integer
                except ValueError:
                    pass  # Ignore non-integer values

    # Create a boolean array to mark seen integers
    seen = [False] * (max_integer + 1)
    unique_integers = []
    # Traverse the list of integers to find unique integers and mark them as seen
    for integer in integers:
        if not seen[integer]:
            unique_integers.append(integer)
            seen[integer] = True

    # Sort the list of unique integers in increasing order
    for i in range(len(unique_integers)):
        for j in range(i + 1, len(unique_integers)):
            if unique_integers[i] > unique_integers[j]:
                unique_integers[i], unique_integers[j] = unique_integers[j], unique_integers[i]

    # Write unique integers to output file, in increasing order
    with open(output_file, 'w') as f:
        for integer in unique_integers:
            f.write(str(integer) + '\n')

if __name__ == "__main__":
    input_file = "sample_04.txt"
    output_file = "sample_output_04.txt"
    main(input_file, output_file)