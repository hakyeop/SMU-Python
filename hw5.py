def read_single_digit(n):
    if ord(n) == 48:
        return '영'
    elif ord(n) == 49:
        return '일'
    elif ord(n) == 50:
        return '이'
    elif ord(n) == 51:
        return '삼'
    elif ord(n) == 52:
        return '사'
    elif ord(n) == 53:
        return '오'
    elif ord(n) == 54:
        return '육'
    elif ord(n) == 55:
        return '칠'
    elif ord(n) == 56:
        return '팔'
    elif ord(n) == 57:
        return '구'

def read_number(n):
    c1=read_single_digit(n[0:1])
    c2=read_single_digit(n[1:2])
    c3=read_single_digit(n[2:3])
    return (c1+' '+c2+' '+c3)

n=str(input('세 자리 정수 입력: '))
p=read_number(n)
print(p)
