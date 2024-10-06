

# from typing import ItemsView


# class Item:
#     def __init__(self,nome,valor) :
#         self.__nome = nome
#         self.__valor = valor



# def valor_total_compra_desconto(qtde,check,*items) :
#     soma = 0
#     if check == "Livro" :
#         for n in items :
#             soma +=(((n*97)/100)*qtde)
#         return  soma
#     elif check == "Brinquedo" :
#         for n in items :
#           soma +=(((n*95)/100)*qtde)
#         return  soma
#     elif check == "Eletronico" :
#         for n in items :
#           soma +=(((n*92)/100)*qtde)
#         return  soma
    


# def calculate_values_without_discount(qtde,*items) :
#     soma = 0.00
#     for n in items :
#         soma +=n * qtde
#     return soma


# class Livro(Item) :
#     def __init__(self, nome, valor):
#         super().__init__(nome, valor)
#         self.valor = valor
#         self.nome = nome
       


# class Brinquedo(Item):
#     def __init__(self, nome, valor):
#       super().__init__(nome, valor) 
#       self.valor = valor
#       self.nome = nome
       


#     def total_sem_desconto(self):
#         return (self.valor)
   

# class Eletronico(Item):
#     def __init__(self, nome, valor):
#         super().__init__(nome, valor)
#         self.valor = valor
#         self.nome =  nome


# class CestaCompras (Item):
#     def __init__(self):
#         self.itens = {}

#     def adicionar_item(self,Item,qtde) :
#         self.itens[Item] = qtde
    
#     def relatorio_final(self) :
#         for item, qtde in self.itens.items():
#             print("%s, %s, %i, %0.2f, %0.2f, %0.2f" % (item.__class__.__name__,item.nome, qtde,item.valor,calculate_values_without_discount(qtde,item.valor),valor_total_compra_desconto(qtde,item.__class__.__name__,item.valor)))
        





from typing import ItemsView


class Item:
    def __init__(self,nome,valor) :
        self.__nome = nome
        self.__valor = valor



        

def valor_total_compra_desconto(qtde,check,*items) :
    soma = 0
    if check == "Livro" :
        for n in items :
            soma +=(((n*97)/100)*qtde)
        return  soma
    elif check == "Brinquedo" :
        for n in items :
           soma +=(((n*95)/100)*qtde)
           
        return  soma
    elif check == "Eletronico" :
        for n in items :
          soma +=(((n*92)/100)*qtde)
        return  soma


def calculate_values_without_discount(qtde,*items) :
    soma = 0
    for n in items :
        soma +=n * qtde
    return soma


class Livro(Item) :
    def __init__(self, nome, valor):
        super().__init__(nome, valor)
        self.valor = valor
        self.nome = nome
       


class Brinquedo(Item):
    def __init__(self, nome, valor):
       super().__init__(nome, valor) 
       self.valor = valor
       self.nome = nome
       


    def total_sem_desconto(self):
        return (self.valor)
   

class Eletronico(Item):
    def __init__(self, nome, valor):
        super().__init__(nome, valor)
        self.valor = valor
        self.nome =  nome


class CestaCompras (Item):
    def __init__(self):
        self.itens = {}

    def adicionar_item(self,Item,qtde) :
        self.itens[Item] = qtde
    
    def relatorio_final(self) :
        def valor_total_compra_desconto1(*funct) :
            soma = 0
            for n in funct :
                soma +=n
            return soma
        p = 0
        output = []
        for item, qtde in self.itens.items():
            out = []
            p += valor_total_compra_desconto1(valor_total_compra_desconto(qtde,item.__class__.__name__,item.valor))
            out.extend([item.__class__.__name__,item.nome, qtde,item.valor,calculate_values_without_discount(qtde,item.valor),valor_total_compra_desconto(qtde,item.__class__.__name__,item.valor)])
            output.append(out)

        print("%.2f"%(p))
        for i in output :
            for out in i:
                if type(out) is float:
                    print("%.2f" % out, end=" ")
                else: print(out, end=" ")
            print("")
       
# print("%s, %s, %i, %0.2f, %0.2f, %0.2f" % 