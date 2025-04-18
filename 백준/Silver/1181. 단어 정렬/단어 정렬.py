import sys

n = int(sys.stdin.readline())
words = [input() for _ in range(n)]


words.sort()        # 알파벳 순서로 정렬
words.sort(key=len)     # 단어 길이 순서로 정렬

print_words = []

# 중복된 단어는 한 번만 출력
for i in words:
    if i in print_words:
        pass
    else:
        print(i)
        print_words.append(i)