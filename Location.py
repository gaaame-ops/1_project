import info_all
from random import randint, choice
from Randoma import Random_C, Randomas

class Village:
    shop = False
    the_forge = False
    hotel = False
    def __init__(self, shop=False, the_force=False, hotel=False):
        self.shop = shop
        self.the_forge = the_force
        self.hotel = hotel


    def outline_of_the_village(self, a):
        print(f"Из далека виднеется силует {a}")
        self.village_in()

    def village_in(self):
        print("Вы прибыли в деревню")
        if self.shop == False and self.the_forge == False and self.hotel == False:
            print("А деревня маловата тут ловить нечего")
        else:
            if self.shop == True:
                pass 
            elif self.the_forge == True:
                pass
            else:
                pass

    def for_Event(self, arr, arr_2, d, price_index, soon=0, Fine=0):
        if soon == 0:
            if Fine == 0:
                for i in arr.keys():
                    if i == d:
                        a = arr[d]
                        a_rn = choice(a)
                        print(f"--> Предмет: {a_rn} | Цена: {arr_2[price_index]} монеты")
                        return a_rn, arr_2[price_index]
            elif Fine == 1:
                choice_item = choice(arr)
                print(f"--> Предмет: {choice_item} | Цена: {arr_2[price_index]} монеты")
                return choice_item, arr_2[price_index]
            elif Fine == 2:
                for i in arr.keys():
                    a = []
                    a.append(i)
                a_rn = choice(a)
                print(f"--> Предмет: {a_rn} | Цена: {arr_2[price_index]} монеты")
                return a_rn, arr_2[price_index]
        else:
            print("--> Пустая полка")
            return "Пустота", 0

    def Weapon_give(self):
        classes = Randomas().Rndm_class()

        if classes == "common":
            return self.for_Event(info_all.specification, info_all.catalog_price, "common", 0)

        elif classes == "uncommon":
            return self.for_Event(info_all.specification, info_all.catalog_price, "uncommon", 1)

        elif classes == "rare":
            return self.for_Event(info_all.specification, info_all.catalog_price, "rare", 2)

        elif classes == "epic":
            return self.for_Event(info_all.specification, info_all.catalog_price, "epic", 3)

        elif classes == "mythical":
            return self.for_Event(info_all.specification, info_all.catalog_price, "mythical", 4)
        
        else:
            return self.for_Event(info_all.food_list_4, info_all.catalog_price, "epic", 4, 1)
        
    def Item_give(self):
        classes = Randomas().Rndm_class()
        if classes == "common":
            return self.for_Event(info_all.common_items, info_all.catalog_price, "common", 0, 0, 1)

        elif classes == "uncommon":
            return self.for_Event(info_all.uncommon_items, info_all.catalog_price, "uncommon", 1, 0, 1)

        elif classes == "rare":
            return self.for_Event(info_all.rare_items, info_all.catalog_price, "rare", 2, 0, 1)

        elif classes == "epic":
            return self.for_Event(info_all.epic_items, info_all.catalog_price, "epic", 3, 0, 1)

        elif classes == "mythical":
            return self.for_Event(info_all.mythical_items, info_all.catalog_price, "mythical", 4, 0, 1)
        
        else:
            return self.for_Event(info_all.food_list_4, info_all.catalog_price, "epic", 4, 1)
        
    def Foods_give(self):
        classes = Randomas().Rndm_class()
        if classes == "common":
            return self.for_Event(info_all.food_list_1, info_all.catalog_price, "common", 0, 0, 2)

        elif classes == "uncommon":
            return self.for_Event(info_all.food_list_2, info_all.catalog_price, "uncommon", 1, 0, 2)
        
        elif classes == "rare":
            return self.for_Event(info_all.food_list_3, info_all.catalog_price, "rare", 2, 0, 2)

        elif classes == "epic":
            return self.for_Event(info_all.food_list_4, info_all.catalog_price, "epic", 3, 0, 2)
        
        else:
            return self.for_Event(info_all.food_list_4, info_all.catalog_price, "epic", 4, 1)
        
    def other(self):
        print("|Информация->1| |Скупка товара->2| ", end="")
        choice_other = int(input())
        if choice_other == 1:
            pass
        elif choice_other == 2:
            pass

    def save_catalog(self, shop_type=0):
            catalog = []
            prices = []

            for i in range(1, 9):
                print(i, end=" ")
                if shop_type == 0: 
                    item, price = self.Weapon_give()
                    catalog.append(item)
                    prices.append(price)
                elif shop_type == 1:
                    item, price = self.Item_give()
                    catalog.append(item)
                    prices.append(price)
                elif shop_type == 2:
                    item, price = self.Foods_give()
                    catalog.append(item)
                    prices.append(price)
                
                return catalog, prices

    def market(self):
        print("Снизу вы можете увидеть наш католог")
        print("Добро пожаловать в магазин")

    
        for i in info_all.shop_catalog:
            print(i, end=" ")

        choice_catalog = int(input("--->" ))
        print("Если нечего интерестного не нашёл ---> назад <---")


        def shop_logic():
            catalog_random = Random_C()
            catalog, prices = self.save_catalog()
            if i == 8:
                choice_i = input()
                if choice_i == "назад":
                    self.market()
                print(f"Вы точно хотите приобрести предмет {catalog[int(choice_i)-1]} за {prices[int(choice_i)-1]} монет?")
                choise_init = input("Ответ да/нет?: ")
                if choise_init == "да":
                    print("Сделка успешна")
                    return catalog[int(choice_i)-1], prices[int(choice_i)-1]
                elif choise_init == "нет":
                        print("Тогда иди прочь")    
                    
 
        def items_shop():
            self.save_catalog(1)
            shop_logic()
        def foods_shop():
            self.save_catalog(2)
            shop_logic()
    
        if choice_catalog == 1:
            self.save_catalog(0)
            shop_logic()
        elif choice_catalog == 2:
            items_shop()
        elif choice_catalog == 3:
            foods_shop()
        else:
            pass



Vill = Village()
Vill.market()
