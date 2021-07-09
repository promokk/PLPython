def patternMatch(text: str, pattern: str) -> str:
    n, m = len(text), len(pattern)
    if m == 0:
        return "OK" if n == 0 else "KO"
    i, j = 0, 0
    indexText, indexPattern = -1, -1
    while i < n:
        if j < m and text[i] == pattern[j]:
            i += 1
            j += 1
        elif j < m and pattern[j] == "*":
            indexText = i
            indexPattern = j
            j += 1
        elif indexPattern >= 0:
            i = indexText + 1
            j = indexPattern + 1
            indexText += 1
        else:
            return "KO"
    while j < m and pattern[j] == "*":
        j += 1
    return "OK" if j == m else "KO"

def main():
    print(patternMatch("aaaa", "a*"))
    print(patternMatch("abbb", "a*"))
    print(patternMatch("zzde", "a*"))
    print(patternMatch("ffghzdes", "*zde*"))
    print(patternMatch("", "*"))

if __name__ == '__main__':
    main()