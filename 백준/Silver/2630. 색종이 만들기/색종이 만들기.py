import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

def divide_paper(x, y, size):
    global white, blue
    color = paper[x][y]
    same = True

    # 현재 영역이 모두 같은 색인지 검사
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != color:        # 다른 색이 있을 경우
                same = False
                break
        if not same:
            break

    # 모두 같을 색일 경우, 색종이 개수 +1
    if same:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        # 색이 섞여 있을 경우 4등분 하여 다시 divide_paper 수행
        half = size // 2
        divide_paper(x, y, half)            # 왼쪽 위
        divide_paper(x, y+half, half)       # 오른쪽 위
        divide_paper(x+half, y, half)       # 왼쪽 아래
        divide_paper(x+half, y+half, half)  # 오른쪽 아래

divide_paper(0, 0, n)     # 시작 위치 (0,0)

print(white)
print(blue)