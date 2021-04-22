N = int(input())

def setting(data):
    return data[1]

grade = []
for i in range(N):
    input_data = input().split()
    grade.append((input_data[0],int(input_data[1])))

grade = sorted(grade,key=setting)

for student in grade:
    print(student[0], end=' ')
    