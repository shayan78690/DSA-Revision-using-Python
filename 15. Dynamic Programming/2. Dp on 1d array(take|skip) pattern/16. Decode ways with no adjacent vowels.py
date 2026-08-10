mod = 10**9 + 7

def isVowel(num):
    return num in [1, 5, 9, 15, 21]

def solve(s, n, index, lastVowel):
    if index == n:
        return 1

    if s[index] == "0":
        return 0

    count = 0

    one_digit = int(s[index])
    is_one_vowel = isVowel(one_digit)

    if not is_one_vowel or not lastVowel:
        count = (count + solve(
            s, n, index + 1, is_one_vowel
        )) % mod

    if index + 1 < n:
        two_digit = int(s[index:index+2])

        if 10 <= two_digit <= 26:
            is_two_vowel = isVowel(two_digit)

            if not is_two_vowel or not lastVowel:
                count = (count + solve(
                    s, n, index + 2, is_two_vowel
                )) % mod

    return count


s = input()
n = len(s)

print(solve(s, n, 0, False))



mod = 10**9 + 7

def isVowel(num):
    return num in [1, 5, 9, 15, 21]

def solve(s, n, index, lastVowel, dp):
    if index == n:
        return 1

    if s[index] == "0":
        return 0

    if dp[index][lastVowel] != -1:
        return dp[index][lastVowel]

    count = 0

    one_digit = int(s[index])
    is_one_vowel = isVowel(one_digit)

    if not is_one_vowel or not lastVowel:
        count = (count + solve(
            s, n, index + 1, is_one_vowel, dp
        )) % mod

    if index + 1 < n:
        two_digit = int(s[index:index+2])

        if 10 <= two_digit <= 26:
            is_two_vowel = isVowel(two_digit)

            if not is_two_vowel or not lastVowel:
                count = (count + solve(
                    s, n, index + 2, is_two_vowel, dp
                )) % mod

    dp[index][lastVowel] = count

    return count


s = input()
n = len(s)

dp = [[-1] * 2 for _ in range(n)]

print(solve(s, n, 0, False, dp))


mod = 10**9 + 7

def isVowel(num):
    return num in [1, 5, 9, 15, 21]


s = input()
n = len(s)

dp = [[0] * 2 for _ in range(n + 2)]

dp[n][0] = 1
dp[n][1] = 1

for index in range(n - 1, -1, -1):

    if s[index] == "0":
        continue

    for lastVowel in range(0, 2):

        count = 0

        one_digit = int(s[index])
        is_one_vowel = isVowel(one_digit)

        if not is_one_vowel or not lastVowel:
            count = (count + dp[index + 1][is_one_vowel]) % mod

        if index + 1 < n:

            two_digit = int(s[index:index+2])

            if 10 <= two_digit <= 26:

                is_two_vowel = isVowel(two_digit)

                if not is_two_vowel or not lastVowel:
                    count = (count + dp[index + 2][is_two_vowel]) % mod

        dp[index][lastVowel] = count

print(dp[0][0])
