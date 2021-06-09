class Frame:
    tmpFrame = []
    def checkFrame(self):
        for x,y,a in self.tmpFrame:
            # 기둥인 경우
            if a == 0:
                if y==0 or [x-1,y,1] in self.tmpFrame or [x,y,1] in self.tmpFrame or [x,y-1,0] in self.tmpFrame:
                    continue
                return False
            # 보인 경우
            if a == 1:
                if [x,y-1,0] in self.tmpFrame or [x+1,y-1,0] in self.tmpFrame or ([x-1,y,1] in self.tmpFrame and [x+1,y,1] in self.tmpFrame):
                    continue
                return False
        return True
    def build_column(self,x,y):
        self.tmpFrame.append([x,y,0])
    def build_beam(self,x,y):
        self.tmpFrame.append([x,y,1])
    def destroy_column(self,x,y):
        self.tmpFrame.remove([x,y,0])
    def destroy_beam(self,x,y):
        self.tmpFrame.remove([x,y,1])
    
def solution(n, build_frame):
    answer = [[]]
    fr = Frame()
    for x,y,a,b in build_frame:
        # 설치할 때
        if b == 1:
            if a == 0:
                fr.build_column(x,y)
                if fr.checkFrame() == False:
                    fr.destroy_column(x,y)
            else:
                fr.build_beam(x,y)
                if fr.checkFrame() == False:
                    fr.destroy_beam(x,y)
        # 삭제할 때
        if b == 0:
            if a == 0:
                fr.destroy_column(x,y)
                if fr.checkFrame() == False:
                    fr.build_column(x,y)
            else:
                fr.destroy_beam(x,y)
                if fr.checkFrame() == False:
                    fr.build_beam(x,y)
    answer = fr.tmpFrame
    answer.sort()
    return answer

n = 5
build_frame1 = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
answer = solution(n,build_frame2)
print(answer)