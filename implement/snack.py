### Dummy DOSMS Game ###
direction = ['N','E','S','W']
N = 2
move_queue = []
apple = []
class Snake:
    queue = []
    toward = 0
    def __init__(self):
        self.queue.append((0,0))
        self.toward = 1
    def turn(self,c):
        if c == 'D':
            self.toward += 1
            if self.toward > 3:
                self.toward = 0
        if c == 'L':
            self.toward -= 1
            if self.toward < 0:
                self.toward = 3
    def crashDetect(self,loc):
        # 뱀의 머리가 뱀과 부딫힐 경우
        if loc in self.queue:
            return True
        # 뱀의 머리가 벽과 부딫힐 경우
        if loc[0]<0 or loc[0]>=N or loc[1]<0 or loc[1]>=N:
            return True
        return False
    def eatApple(self):
        if direction[self.toward] =='N':
            tempHead = (self.queue[-1][0]-1,self.queue[-1][1])
            if self.crashDetect(tempHead) == False:
                self.queue.append(tempHead)
            else:
                return False
        elif direction[self.toward] =='E':
            tempHead = (self.queue[-1][0],self.queue[-1][1]+1)
            if self.crashDetect(tempHead) == False:
                self.queue.append(tempHead)
            else:
                return False
        elif direction[self.toward] =='S':
            tempHead = (self.queue[-1][0]+1,self.queue[-1][1])
            if self.crashDetect(tempHead) == False:
                self.queue.append(tempHead)
            else:
                return False
        elif direction[self.toward] =='W':
            tempHead = (self.queue[-1][0],self.queue[-1][1]-1)
            if self.crashDetect(tempHead) == False:
                self.queue.append(tempHead)
            else:
                return False
        return True
    def move(self):
        if direction[self.toward] =='N':
            tempHead = (self.queue[-1][0]-1,self.queue[-1][1])
            if self.crashDetect(tempHead) == False:
                self.queue.append(tempHead)
            else:
                return False
        elif direction[self.toward] =='E':
            tempHead = (self.queue[-1][0],self.queue[-1][1]+1)
            if self.crashDetect(tempHead) == False:
                self.queue.append(tempHead)
            else:
                return False
        elif direction[self.toward] =='S':
            tempHead = (self.queue[-1][0]+1,self.queue[-1][1])
            if self.crashDetect(tempHead) == False:
                self.queue.append(tempHead)
            else:
                return False
        elif direction[self.toward] =='W':
            tempHead = (self.queue[-1][0],self.queue[-1][1]-1)
            if self.crashDetect(tempHead) == False:
                self.queue.append(tempHead)
            else:
                return False
        self.queue.pop(0)
        return True

# 입력 받기
N = int(input())
K = int(input())
for _ in range(K):
    i, j = map(int, input().split())
    apple.append((i-1,j-1))
L = int(input())
for _ in range(L):
    tmp = input().split()
    x = int(tmp[0])
    l = tmp[1]
    move_queue.append((x,l))


sn = Snake()    # snake 클래스 선언
flag = True
time = 0
while flag==True:
    # 회전
    if len(move_queue) > 0:
        if time == move_queue[0][0]:
            sn.turn(move_queue[0][1])
            move_queue.pop(0)
    # 사과가 있으면 사과 먹기
    if sn.queue[-1] in apple:
        apple.remove(sn.queue[-1])
        flag = sn.eatApple()
    # 사과가 없으면 그냥 이동
    else:
        flag = sn.move()
    time += 1

print(time)
