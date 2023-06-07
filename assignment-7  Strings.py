

            #Answer --------- 1


def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]

        if s_char in s_map:
            if s_map[s_char] != t_char:
                return False
        else:
            s_map[s_char] = t_char

        if t_char in t_map:
            if t_map[t_char] != s_char:
                return False
        else:
            t_map[t_char] = s_char

    return True

s = "egg"
t = "add"
print(isIsomorphic(s, t))





            #Answer --------- 2



def isStrobogrammatic(num):
    strob_pairs = ["00", "11", "69", "96", "88"]
    left = 0
    right = len(num) - 1

    while left <= right:
        pair = num[left] + num[right]
        if pair not in strob_pairs:
            return False
        left += 1
        right -= 1

    return True

num = "69"
print(isStrobogrammatic(num))





            #Answer ---------- 3


def addStrings(num1, num2):
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    carry = 0
    result = ""

    while p1 >= 0 or p2 >= 0 or carry != 0:
        digit_sum = carry

        if p1 >= 0:
            digit_sum += int(num1[p1])
            p1 -= 1

        if p2 >= 0:
            digit_sum += int(num2[p2])
            p2 -= 1

        carry = digit_sum // 10
        digit = digit_sum % 10

        result = str(digit) + result

    return result

num1 = "11"
num2 = "123"
print(addStrings(num1, num2))



               #Answer ---------- 4



def reverseWords(s):
    words = s.split()
    reversed_words = []

    for word in words:
        reversed_word = ''.join(list(word)[::-1])
        reversed_words.append(reversed_word)

    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


s = "Let's take LeetCode contest"
print(reverseWords(s))


                #Answer ------- 5


def reverseStr(s, k):
    result = ""

    for i in range(0, len(s), 2 * k):
        if i + k <= len(s):
            result += s[i:i+k][::-1]
        else:
            result += s[i:][::-1]

       
        if i + 2 * k <= len(s):
            result += s[i+k:i+2*k]

    return result

s = "abcdefg"
k = 2
print(reverseStr(s, k))



              #Aanswer ------- 6


def reverseStr(s, k):
    result = ""

    for i in range(0, len(s), 2 * k):
        if i + k <= len(s):
            result += s[i:i+k][::-1]
        else:
            result += s[i:][::-1]

       
        if i + 2 * k <= len(s):
            result += s[i+k:i+2*k]

    return result

s = "abcdefg"
k = 2
print(reverseStr(s, k))




                 #Aanswer ------- 7


def processString(string):
    result = []
    for char in string:
        if char != '#':
            result.append(char)
        elif result:
            result.pop()
    return ''.join(result)


def backspaceCompare(s, t):
    return processString(s) == processString(t)

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))






                 #Aanswer ------- 8




def checkStraightLine(coordinates):
    # Step 1
    if len(coordinates) < 3:
        return True
    
    # Step 2
    x1, y1 = coordinates[0]
    
    # Step 3
    for i in range(1, len(coordinates)):
        x2, y2 = coordinates[i]
        if x2 - x1 == 0:
            slope = float('inf')
        else:
            slope = (y2 - y1) / (x2 - x1)
            
        if i > 1 and slope != prev_slope:
            return False
        
        prev_slope = slope
        x1, y1 = x2, y2
    
    # Step 4
    return True
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))












