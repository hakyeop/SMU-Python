d = {}
print('[구입]')
while True:
    item = str(input("상품명? "))
    if item=='':
        break
    q= int(input("수량은? "))
    d[item]=q
    
    print(f' 장바구니에 {item} {q}개가 담겼습니다.')

print('>>> 장바구니 보기: ' ,end='')
print(d)
print('\n')

print('[검색]')
s=str(input('장바구니에서 확인하고자 하는 상품은? '))
print(f'{s}은(는)', d.get(s),'개 담겨 있습니다.')
