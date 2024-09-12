import csv
from typing import Dict, Set
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self._load_data(source_path)

    def _load_data(self, source_path: str) -> None:
        dish_map: Dict[str, Dish] = {}
        with open(source_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                dish_name, price, ingredient_name, quantity = row
                price = float(price)
                quantity = int(quantity)
                if dish_name not in dish_map:
                    dish_map[dish_name] = Dish(dish_name, price)
                dish = dish_map[dish_name]
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, quantity)
        self.dishes = set(dish_map.values())
