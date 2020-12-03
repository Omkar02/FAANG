# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Medium')


def bullsAndCows(secret, guess):
    map_s = {}
    map_g = {}
    cows = 0
    bulls = 0
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
        else:
            if guess[i] in map_s and map_s[guess[i]] > 0:
                cows += 1
                map_s[guess[i]] -= 1
            else:
                map_g[guess[i]] = map_g.get(guess[i], 0) + 1

            if secret[i] in map_g and map_g[secret[i]] > 0:
                cows += 1
                map_g[secret[i]] -= 1
            else:
                map_s[secret[i]] = map_s.get(secret[i], 0) + 1

    return f'{bulls}A{cows}B'


secret = "1807"
guess = "7810"
# Output: "1A3B"

print(bullsAndCows(secret, guess))
