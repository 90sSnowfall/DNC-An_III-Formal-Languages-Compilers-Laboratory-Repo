import time
def is_palindrome(palindrome):
    return palindrome == palindrome[::-1]

def generate_palindromes(length):
    alphabet = ['0', '1', '2']
    palindromes = []
    def generate_recursive(prefix, remaining_length):
        if remaining_length == 0:
            palindromes.append(prefix)
            return
        for symbol in alphabet:
            new_prefix = prefix + symbol
            generate_recursive(new_prefix, remaining_length - 1)
            if remaining_length != length:  # avoid duplicates for odd-length palindromes
                generate_recursive(symbol + prefix, remaining_length - 1)
    generate_recursive('', length)
    return palindromes

for length in range(1, 6):
    palindromes = []
    print(f"Palindroms of length {length}:")
    palindromes_temp = generate_palindromes(length)
    for palindrome in palindromes_temp:
        if(is_palindrome(palindrome) == False): continue
        palindromes.append(palindrome)
    temp_set = set(palindromes)
    palindromes = list(temp_set)
    for index in palindromes:
        print(index)
        time.sleep(0.5)
    print()

