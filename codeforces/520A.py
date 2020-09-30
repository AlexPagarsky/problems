n = int(input())
s = input()

def is_pangram(s: str) -> str:
    letters = set('abcdefghijklmnopqrstuvwxyz')

    for ch in s.lower():
        if ch in letters:
            letters.remove(ch)

    return 'NO' if len(letters) else 'YES'

print(is_pangram(s))