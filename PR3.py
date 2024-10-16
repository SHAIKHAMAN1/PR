def generate_pattern(input_string):
    pattern = ""
    prev_char = ""
    count = 1
    for char in input_string:
        if char == prev_char:
            count += 1
        else:
            if prev_char:
                pattern += prev_char + str(count)
            prev_char = char
            count = 1
        
    pattern += prev_char + str(count)
    return pattern

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    pattern = generate_pattern(input_string)
    print("Generated Pattern:", pattern)