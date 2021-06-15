n = int(input())
scores = []
for i in range(n):
    tmp_line = list(input().split())
    name = tmp_line[0]
    korean = int(tmp_line[1])
    eng = int(tmp_line[2])
    math = int(tmp_line[3])
    scores.append((korean,eng,math,name))

scores.sort(key=lambda x: (-x[0],x[1],-x[2],x[3]))

for score in scores:
    print(score[3])
