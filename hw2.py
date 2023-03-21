def exchange(m):
    fh=m//500
    tmp1=m%500
    oh=tmp1//100
    tmp2=tmp1%100
    ft=tmp2//50
    tmp3=tmp2%50
    t=tmp3//10
    print("500원 동전의 개수: ", fh)
    print("100원 동전의 개수: ", oh)
    print("50원 동전의 개수: ", ft)
    print("10원 동전의 개수: ", t)

def get_integer(prompt):
    b=int(input(prompt))
    return m

m=get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(m)
