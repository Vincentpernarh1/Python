import math
class Ponto2D:
    def __init__(self, x = 0.0 , y = 0.0 ) :
        self.__x = x
        self.__y = y

    def getx(self) :
        return self.__x

    def gety(self):
        return self.__y


class Retangulo :
    width = 0.0
    height = 0.0
    def __init__(self,__esq_sup =  Ponto2D,__dir_inf =  Ponto2D) :
        self.dir_inf = __dir_inf
        self.esq_sup = __esq_sup

    def calcularArea(self) :
        self.width = abs((self.esq_sup.getx())  -  (self.dir_inf.getx()))
        self.height = abs((self.esq_sup.gety()) - (self.dir_inf.gety()))

        area =  (self.width) * (self.height)
        return area
        
    def calcularIntersecao(self,ret) :
        x5 = max(self.esq_sup.getx(),ret.esq_sup.getx())
        y5 = max(self.esq_sup.gety(),ret.esq_sup.gety())
        x6 = min(self.dir_inf.getx(),ret.dir_inf.getx())
        y6 = min(self.dir_inf.gety() ,ret.dir_inf.gety())

        if abs(x5) > abs(x6) or abs(y5) > abs(y6) :
            return None
        else :
            interSection = (abs(x5 - x6) * abs(y5 - y6))/2
            return interSection;
   
