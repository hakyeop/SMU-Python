def buy(shopping_bag):
    item = str(input("상품명? "))
    if item=='':
        return False
    q= int(input("수량은? "))
    shopping_bag[item]=q
    print(f' 장바구니에 {item} {q}개가 담겼습니다.')
    print()

def show(shopping_bag):
    print()
    print('>>> 장바구니 보기: ' ,end='')
    print(shopping_bag)
    print()

def find(shopping_bag):
    print('[검색]')
    s=str(input('장바구니에서 확인하고자 하는 상품은? '))
    if shopping_bag.get(s) == None:
        print(f'장바구니에 {s}은(는) 없습니다.')
    else:
        q=shopping_bag.get(s)
        print(f'{s}은(는) {q}개 담겨 있습니다.')

shopping_bag = {}
print('[구입]')
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
