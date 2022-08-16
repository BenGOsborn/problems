from collections import deque

def is_balanced(s):
    stack = deque()

    for elem in s:
        if elem in ['(', '[', '{']:
            if elem == "(":
                stack.append(")")
            elif elem == "[":
                stack.append("]")
            else:
                stack.append("}")
        else:
            if len(stack) == 0 or stack.pop() != elem:
                return False

    return len(stack) == 0

def main():
    print(is_balanced("}][}}(}][))]"))
    print(is_balanced("[](){()}"))
    print(is_balanced("()"))
    print(is_balanced("({}([][]))[]()"))
    print(is_balanced("{)[](}]}]}))}(())("))
    print(is_balanced("([[)"))

if __name__ == "__main__":
    main()