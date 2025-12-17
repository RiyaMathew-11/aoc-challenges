maxJoltage = []


def find_largest_k_digits(sequence, k):

    n = len(sequence)
    result = []
    remaining_needed = k
    start_pos = 0
    
    while remaining_needed > 0:
        # Window end: position where we must choose by to have enough digits left
        window_end = n - remaining_needed + 1
        
        # Find the maximum digit in the valid window
        best_digit = sequence[start_pos]
        best_pos = start_pos
        
        for i in range(start_pos + 1, window_end):
            if sequence[i] > best_digit:
                best_digit = sequence[i]
                best_pos = i
        
        result.append(best_digit)
        start_pos = best_pos + 1
        remaining_needed -= 1
    
    return ''.join(result)

    



with open("input.txt", "r") as file:
    for line in file:
        battery = list(line.strip())
        maxJoltage.append(int(find_largest_k_digits(battery, 12)))

        
print(maxJoltage)
print(sum(maxJoltage))

# Answer: 173685428989126