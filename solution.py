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
    the way to the bottom right without touching previously travelled
    on cells in the grid.

    For example: if str is "r?d?drdd" then your program should output
    the final correct string that will allow a path to be formed from the
    top left of a 5x5 grid to the bottom right. For this input, your program
    should therefore return the string rrdrdrdd. There will only ever be one
    correct path and there will always be at least one question mark within
    the input string.
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
    and the second element being a list of available weights
    as positive integers.
    Your goal is to determine if you can balance the scale by using the least
    amount of weights from the list, but using at most only 2 weights.
    For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this means
    there is a balance scale with a weight of 5 on the left side and 9 on
    the right side.
    It is in fact possible to balance this scale by adding a 6 to the left
    side from the list of weights and adding a 2 to the right side.
    Both scales will now equal 11 and they are perfectly balanced.
    Your program should return a comma separated string of the weights
    that were used from the list in ascending order, so for this example
    your program should return the string 2,6

    There will only ever be one unique solution and the list of available
    weights will not be empty. It is also possible to add two weights to only
    one side of the scale to balance it. If it is not possible to balance the
    scale then your program should return the string not possible.
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
    for i, _ in enumerate(ws):
        if key + ws[i] in ws[i+1::]:
            return "{},{}".format(ws[i], key + ws[i])
        if key - ws[i] in ws[i+1::]:
            return "{},{}".format(ws[i], key - ws[i])


def VowelSquare(strArr):
    """Have the function VowelSquare(strArr) take the strArr parameter being
    passed which will be a 2D matrix of some arbitrary size filled with
    letters from the alphabet, and determine if a 2x2 square composed entirely
    of vowels exists in the matrix. For example: strArr is 
    ["abcd", "eikr", "oufj"]
    then this matrix looks like the following:

    a b c d
    e i k r
    o u f j

    Within this matrix there is a 2x2 square of vowels starting in the second row
    and first column, namely, ei, ou. If a 2x2 square of vowels is found your program
    should return the top-left position (row-column) of the square, so for this example
    your program should return 1-0. If no 2x2 square of vowels exists, then return
    the string not found. If there are multiple squares of vowels, return the one that
    is at the most top-left position in the whole matrix. The input matrix will
    at least be of size 2x2.
    """
    # code goes here
    vowels = 'aeiou'
    for i in range(len(strArr) - 1):
        for j in range(len(strArr[0]) - 1):
            if strArr[i][j] in vowels \
                    and strArr[i][j+1] in vowels \
                    and strArr[i+1][j] in vowels \
                    and strArr[i+1][j+1] in vowels:
                return str(i)+'-'+str(j)
    return 'not found'


def ClosestEnemyII(strArr):
    """Have the function ClosestEnemyII(strArr) read the matrix of numbers
    stored in strArr which will be a 2D matrix that contains only the integers
    1, 0, or 2. Then from the position in the matrix where a 1 is,
    return the number of spaces either left, right, down, or up you
    must move to reach an enemy which is represented by a 2.
    You are able to wrap around one side of the matrix to the other as well.
    For example: if strArr is ["0000", "1000", "0002", "0002"]
    then this looks like the following:

    0 0 0 0
    1 0 0 0
    0 0 0 2
    0 0 0 2

    For this input your program should return 2 because the closest enemy (2)
    is 2 spaces away from the 1 by moving left to wrap to the other side
    and then moving down once. The array will contain any number of 0's
    and 2's, but only a single 1. It may not contain any 2's at all as well,
    where in that case your program should return a 0.
    """
    # code goes here
    enemies = []
    moves = []
    width = len(strArr)
    hight = len(strArr[0])
    for i, i_val in enumerate(strArr):
        for j, j_val in enumerate(i_val):
            if j_val == '1':
                px, py = (i, j)
            if j_val == '2':
                enemies.append((i, j))
    if not enemies:
        return 0
    for x, y in enemies:
        diff_x = abs(x - px)
        diff_y = abs(y - py)
        moves.append(min(diff_x, width - diff_x) + min(diff_y, hight - diff_y))
    return min(moves)


def QuestionsMarks(str):
    """Have the function QuestionsMarks(str) take the str string parameter,
    which will contain single digit numbers, letters, and question marks,
    and check if there are exactly 3 question marks between every pair of
    two numbers that add up to 10. If so, then your program should return
    the string true, otherwise it should return the string false.
    If there aren't any two numbers that add up to 10 in the string,
    then your program should return false as well.

    For example: if str is "arrb6???4xxbl5???eee5" then your program should
    return true because there are exactly 3 question marks between 6 and 4,
    and 3 question marks between 5 and 5 at the end of the string.
    """
    # code goes here
    dig_idxs = [idx for idx, _ in enumerate(str) if str[idx].isdigit()]
    has_ten = False
    if len(dig_idxs) <= 1:
        return 'false'
    for i in range(len(dig_idxs) - 1):
        d_x = dig_idxs[i]
        d_y = dig_idxs[i+1]
        if int(str[d_x]) + int(str[d_y]) == 10:
            has_ten = True
            if str[d_x:d_y:].count('?') != 3:
                return 'false'
    return 'true' if has_ten else 'false'


# keep this function call here
print(QuestionsMarks('9???1???9??1???9'))
