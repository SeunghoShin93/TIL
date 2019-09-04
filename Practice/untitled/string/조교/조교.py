
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

N, K = map(int, input().split())

raw_score = [list(map(int, input().split())) for a in range(N)]

for b in raw_score:
    b[0] *= 0.35
    b[1] *= 0.45
    b[2] *= 0.2

new_score = []
for c in range(N):
    new_score.append(sum(raw_score[c]))

    # new_score = sorted(new_score, reverse=True)
