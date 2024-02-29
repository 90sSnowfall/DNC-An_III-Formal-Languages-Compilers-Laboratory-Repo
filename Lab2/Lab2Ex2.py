def generate_strings(iterations):
    strings = {"a", "b"}
    for index in range(iterations):
        new_strings = set()
        for string in strings:
            new_strings.add("a" + string + "a")
            new_strings.add("b" + string + "b")
        strings = new_strings
        print("Iteration "+ str(index) +": ", strings)

iterations = generate_strings(3)