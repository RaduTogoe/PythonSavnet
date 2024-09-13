def permutari(s: str, answer: str = ""):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        ch = s[i]
        remaining = s[:i] + s[i + 1:]
        permutari(remaining, answer + ch)

permutari("abc")