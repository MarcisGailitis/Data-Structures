def isReversal(bracket):
    brackets = {'{': '}', '(': ')', '[': ']'}
    try:
        return brackets[bracket]
    except:
        return False


def isBrackets(in_str):
    stack = list()
    for item in in_str:

        # check if 1st element is closing bracket, is so break
        if isReversal(item) == False and len(stack) == 0:
            stack.append(item)
            return False

        # check if closing bracket is related to last item in list, otherwise False
        elif len(stack) != 0 and isReversal(item) == False and isReversal(stack[-1]) != item:
            stack.append(item)
            return False

        # check if 1st element is closing bracket, is so break
        elif len(stack) != 0 and isReversal(stack[-1]) == item:
            stack.pop()

        else:
            stack.append(item)

    return True if len(stack) == 0 else False


print(isBrackets('(('))
print(isBrackets('()'))
print(isBrackets('((([)))'))
print(isBrackets('(({})([]))'))
print(isBrackets('(({)(}[]))'))
