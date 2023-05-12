class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2

    def show(self):
        print(f'좌측 상단 꼭지점이 ({self.__x1},{self.__y1})이고 우측 하단 꼭지점이 ({self.__x2},{self.__y2})인 사각형입니다.', end='')
        
    def getWidth(self, x1, x2):
        xa=x2-x1
        return xa

    def getHeight(self, y1, y2):
        ya = y2-y1
        return ya

    def getArea(self):
        xa=self.getWidth(self.__x1, self.__x2)
        ya=self.getHeight(self.__y1, self.__y2)
        a=xa*ya
        return a

    def getPerimeter(self):
        xa = self.getWidth(self.__x1, self.__x2)
        ya = self.getHeight(self.__y1, self.__y2)
        p=xa*2 + ya*2
        return p

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
