def run_length_encoding(chars):
    n = len(chars)
    
    if n == 0:
        return 0

    count = 1
    prev = n - 1

    for curr in range(n - 2, -1, -1):
        if chars[curr] == chars[prev]:
            count += 1
            chars.pop(curr)
        else:
            chars[prev] = chars[prev]
            chars.insert(prev + 1, str(count))
            count = 1
        prev -= 1

    chars[prev] = chars[prev]
    chars.insert(prev + 1, str(count))

    return len(chars)

# Example usage:
input_chars = ["a", "a", "a", "b", "b", "c", "c", "c", "d"]
encoded_length = run_length_encoding(input_chars)
print(input_chars)  # The input_chars array is modified in place
print(encoded_length)
