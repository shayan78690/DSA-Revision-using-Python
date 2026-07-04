def removeChar(s, i):

    if i == len(s):
        return ""

    if s[i] == 'a':
        return removeChar(s, i + 1)

    return s[i] + removeChar(s, i + 1)
