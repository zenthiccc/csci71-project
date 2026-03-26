def is_balanced(s):
    state = "q0"
    stack = ["Z"]

    print("Processing " + s)

    for i in range(len(s)):
        char = s[i]
        remaining_input = s[i:]

        stack_str = ""
        for item in reversed(stack):
            stack_str = stack_str + item

        print("ID: (" + state + ", " + remaining_input + ", " + stack_str + ")")

        if state == "q0":
            if char == "!" and stack[-1] == "Z":
                stack.append("!")
                state = "q1"
            else:
                print("Invalid string. Failed at position " + str(i + 1) + ".")
                print("Remaining unprocessed input string: " + remaining_input)
                return False

        elif state == "q1":
            if char == "x":
                pass
            elif char == "<" or char == "{" or char == "[" or char == "(":
                stack.append(char)
            elif char == ">":
                if stack[-1] == "<":
                    stack.pop()
                else:
                    print("Invalid string. Failed at position " + str(i + 1) + ".")
                    print("Remaining unprocessed input string: " + remaining_input)
                    return False
            elif char == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    print("Invalid string. Failed at position " + str(i + 1) + ".")
                    print("Remaining unprocessed input string: " + remaining_input)
                    return False
            elif char == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    print("Invalid string. Failed at position " + str(i + 1) + ".")
                    print("Remaining unprocessed input string: " + remaining_input)
                    return False
            elif char == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    print("Invalid string. Failed at position " + str(i + 1) + ".")
                    print("Remaining unprocessed input string: " + remaining_input)
                    return False
            elif char == "!":
                if stack[-1] == "!":
                    stack.pop()
                    state = "q2"
                else:
                    print("Invalid string. Failed at position " + str(i + 1) + ".")
                    print("Remaining unprocessed input string: " + remaining_input)
                    return False
            else:
                print("Invalid string. Failed at position " + str(i + 1) + ".")
                print("Remaining unprocessed input string: " + remaining_input)
                return False

        elif state == "q2":
            print("Invalid string. Failed at position " + str(i + 1) + ".")
            print("Remaining unprocessed input string: " + remaining_input)
            return False

    stack_str = ""
    for item in reversed(stack):
        stack_str = stack_str + item

    print("ID: (" + state + ", E, " + stack_str + ")")

    if state == "q2" and len(stack) == 1 and stack[0] == "Z":
        print("q2 is a final state.")
        print(s + " is valid and has balanced brackets.")
        return True
    else:
        print("Invalid string. " + state + " is not a final state.")
        return False


def is_balanced_silent(s):
    state = "q0"
    stack = ["Z"]

    for i in range(len(s)):
        char = s[i]

        if state == "q0":
            if char == "!" and stack[-1] == "Z":
                stack.append("!")
                state = "q1"
            else:
                return False

        elif state == "q1":
            if char == "x":
                pass
            elif char == "<" or char == "{" or char == "[" or char == "(":
                stack.append(char)
            elif char == ">":
                if stack[-1] == "<":
                    stack.pop()
                else:
                    return False
            elif char == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif char == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif char == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif char == "!":
                if stack[-1] == "!":
                    stack.pop()
                    state = "q2"
                else:
                    return False
            else:
                return False

        elif state == "q2":
            return False

    if state == "q2" and len(stack) == 1 and stack[0] == "Z":
        return True
    else:
        return False


def evaluate(s):
    counts = [0]
    inner_string = s[1:-1]

    for char in inner_string:
        if char == "x":
            counts[-1] = counts[-1] + 1
        elif char == "<" or char == "{" or char == "[" or char == "(":
            counts.append(0)
        elif char == ">":
            val = counts.pop()
            counts[-1] = counts[-1] + (val * 2)
        elif char == "}":
            val = counts.pop()
            counts[-1] = counts[-1] + (val + 1)
        elif char == "]":
            val = counts.pop()
            counts[-1] = counts[-1] + 0
        elif char == ")":
            val = counts.pop()
            if val > 0:
                counts[-1] = counts[-1] + (val - 1)
            else:
                counts[-1] = counts[-1] + 0

    return counts[0]


def main1():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        clean_line = line.strip()
        if clean_line != "":
            is_balanced(clean_line)
            print("")


def main2():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        clean_line = line.strip()
        if clean_line != "":
            is_valid = is_balanced_silent(clean_line)

            if is_valid == True:
                answer = evaluate(clean_line)
                print(clean_line + " - Resulting number of x's: " + str(answer))
            else:
                print(clean_line + " - Invalid string.")


if __name__ == "__main__":
    main1()
    main2()
