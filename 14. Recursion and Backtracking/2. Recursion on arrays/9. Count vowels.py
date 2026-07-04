def countVowels(s, i):

    if i == len(s):
        return 0

    vowels = "aeiouAEIOU"

    if s[i] in vowels:
        return 1 + countVowels(s, i + 1)

    return countVowels(s, i + 1)
