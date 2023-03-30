def rep_char(n):
    print('-'* n)

def draw_line_string(s):
    msg1=(' Hello '+s+',')
    msg2=(' Welcome to Seoul.')
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    nstr = nstr+1
    rep_char(nstr)
    print(msg1)
    print(msg2)
    rep_char(nstr)

s = input("Input his/her name: ")
draw_line_string(s)
