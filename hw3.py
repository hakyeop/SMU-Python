def get_fixed_price(p):
    fp=int(p*(100/(100-discount_rate)))
    return fp

global discount_rate
discount_rate=int(input('할인율은? '))
ap=int(input('A 상품의 할인된 가격은? '))
bp=int(input('B 상품의 할인된 가격은? '))
print('A 상품의 정가는 ', get_fixed_price(ap), '원')
print('B 상품의 정가는 ', get_fixed_price(bp), '원')
