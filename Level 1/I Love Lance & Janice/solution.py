def solution(s):
    final = ''
    for char in s:
        if char.isalpha() and char.islower():
            char = chr(ord(char) - ((ord(char) - 109) * 2 - 1))
        final += char
    return final
