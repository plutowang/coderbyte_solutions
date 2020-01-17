def LetterChanges(str):
    """Have the function LetterChanges(str) take the str
    parameter being passed and modify it using the following algorithm.
    Replace every letter in the string with the letter following it in the
    alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel
    in this new string (a, e, i, o, u) and finally return this modified string.

    """
    # code goes here
    vowels = ['a', 'i', 'o', 'e', 'u']
    result = ''
    for c in str:
        if c.isalpha():
            if c == 'z' or c == 'Z':
                c = 'A'
            else:
                c = chr(ord(c) + 1)
            if c in vowels:
                c = c.upper()
        result += c

    return result


def FirstReverse(str):
    # # opt1:
    # return str[::-1]
    # opt2:
    lst = list(str)
    lst.reverse()
    return ''.join(lst)


def FirstFactorial(num):

    # code goes here
    if num <= 1:
        return 1
    else:
        return num * (FirstFactorial(num - 1))

    return num


def LongestWord(sen):

    # code goes here
    word = ''
    for s in sen:
        if s.isalnum() or s.isalpha():
            word += s
        elif s.isspace():
            word += ' '

    return max(word.split(), key=len)


def SimpleAdding(num):
    """Have the function SimpleAdding(num) add up all the
    numbers from 1 to num. For example: if the input is 4
    then your program should return 10 because 1 + 2 + 3 + 4 = 10.
    For the test cases, the parameter num will be any number from 1 to 1000.
    """

    # code goes here
    return sum([x for x in range(num+1)])


def TimeConvert(num):
    """Have the function TimeConvert(num) take the num parameter
    being passed and return the number of hours and minutes the
    parameter converts to (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    """
    # code goes here
    m = num % 60
    h = (num - m) / 60
    return '{}:{}'.format(int(h), int(m))


def AlphabetSoup(str):

    # code goes here
    list_str = list(str)
    list_str.sort()
    return ''.join(list_str)


def CorrectPath(str):
    """??Have the function CorrectPath(str) read the str parameter
    being passed, which will represent the movements made in a 5x5
    grid of cells starting from the top left position. The characters
    in the input string will be entirely composed of: r, l, u, d, ?.
    Each of the characters stand for the direction to take within the grid,
    for example: r = right, l = left, u = up, d = down. Your goal is to
    determine what characters the question marks should be in order
    for a path to be created to go from the top left of the grid all
    the way to the bottom right without touching previously travelled on cells in the grid.

    For example: if str is "r?d?drdd" then your program should output
    the final correct string that will allow a path to be formed from the
    top left of a 5x5 grid to the bottom right. For this input, your program
    should therefore return the string rrdrdrdd. There will only ever be one
    correct path and there will always be at least one question mark within the input string.
    """
    # code goes here
    grid = []
    x = 0
    y = 4
    i = 0
    for move in str:
        if move == '?':
            for m in 'lurd':
                path = CorrectPath(str.replace('?', m, 1))
                i += 1
                if path:
                    return path
        else:
            if move == 'r':
                x += 1
            elif move == 'l':
                x -= 1
            elif move == 'u':
                y += 1
            elif move == 'd':
                y -= 1
            if (x, y) in grid:
                return
            grid.append((x, y))

            if x < 0 or y < 0 or x > 4 or y > 4:
                return

            if x == 4 and y == 0:
                return str


def ScaleBalancing(strArr):
    """Have the function ScaleBalancing(strArr) read 
    strArr which will contain two elements, the first being 
    the two positive integer weights on a balance scale (left and right sides) 
    and the second element being a list of available weights as positive integers.
    Your goal is to determine if you can balance the scale by using 
    the least amount of weights from the list, but using at most only 2 weights.
    For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this means 
    there is a balance scale with a weight of 5 on the left side and 9 on the right side.
    It is in fact possible to balance this scale by adding a 6 to the left
    side from the list of weights and adding a 2 to the right side. 
    Both scales will now equal 11 and they are perfectly balanced. 
    Your program should return a comma separated string of the weights 
    that were used from the list in ascending order, so for this example 
    your program should return the string 2,6

    There will only ever be one unique solution and the list of available weights 
    will not be empty. It is also possible to add two weights to only one side of 
    the scale to balance it. If it is not possible to balance the scale then your 
    program should return the string not possible.
    """
    # code goes here
    target = abs(eval(strArr[0])[0] - eval(strArr[0])[1])
    ws = eval(strArr[1])
    if target in ws:
        return str(target)

    bal = add_two(ws, target)
    if bal:
        return bal
    return "not possible"


def add_two(ws, key):
    for i in range(len(ws)):
        if key + ws[i] in ws[i+1::]:
            return "{},{}".format(ws[i], key + ws[i])
        if key - ws[i] in ws[i+1::]:
            return "{},{}".format(ws[i], key - ws[i])


# keep this function call here
print(ScaleBalancing(["[3, 7]", "[1, 2, 7]"]))
