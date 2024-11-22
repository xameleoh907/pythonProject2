# "Учёт товаров"


class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file_shop = open(self.__file_name, 'r')
        print(file_shop.read())
        file_shop.close()


    def add(self, *products):
        add_products = products
        file_shop = open(self.__file_name, 'a')
        for product in add_products:
            with open(self.__file_name, 'r') as file:
                file_search = file.read()
                if product.name in file_search:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file_shop.write(product.__str__() + '\n')
        file_shop.close()
        pass


if __name__ == '__main__':

    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)
    #
    print(s1.get_products())