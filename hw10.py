import os

filename = 'score.bin'


def input_scores():
    lst=[]
    i=0
    while True:
        q=int(input(f'#{i+1}? '))
        if q < 0:
            break
        lst.append(q)
        i+=1
    return lst

def get_average(lst):
    s=0
    avg=0
    for i in range(len(lst)):
        s=s+lst[i]
    avg=s/len(lst)

    return avg

def show_scores(lst, avg):
    print('개인점수: ', end='')
    for i in range(len(lst)):
        print(lst[i], end=' ')
    print()
    print(f'평균: {avg:.1f}')

if os.path.exists(filename):
    with open('score.bin', 'r') as file:
        print('파일 읽기\n')
        print('[점수 출력]')
        print(file.read())
        
else:
    print('[점수 입력]')
    lst=input_scores()
    print('\n[점수 출력]')
    avg=get_average(lst)
    with open('score.bin', 'w') as file:
        file.write(f'개인점수:{lst}\n평균: {avg:.1f}')
    show_scores(lst, avg)
    
