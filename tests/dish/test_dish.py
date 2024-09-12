import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


def test_dish():
    # Testa a criação de um prato com um preço válido
    dish = Dish("Spaghetti", 19.99)
    assert dish.name == "Spaghetti"
    assert dish.price == 19.99

    # Testa que um TypeError é levantado se o preço não for um float
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Spaghetti", "19.99")

    # Testa que um ValueError é levantado se o preço for menor ou igual a zero
    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish("Spaghetti", 0)

    # Testa se __repr__ retorna o valor esperado
    dish = Dish("Spaghetti", 19.99)
    assert repr(dish) == "Dish('Spaghetti', R$19.99)"

    # Testa se __eq__ funciona corretamente
    dish1 = Dish("Spaghetti", 19.99)
    dish2 = Dish("Spaghetti", 19.99)
    dish3 = Dish("Pizza", 25.00)
    assert dish1 == dish2
    assert dish1 != dish3

    # Testa se __hash__ funciona corretamente
    dish1 = Dish("Spaghetti", 19.99)
    dish2 = Dish("Spaghetti", 19.99)
    dish3 = Dish("Pizza", 25.00)
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    # Testa se add_ingredient_dependency adiciona ingredientes corretamente
    dish = Dish("Spaghetti", 19.99)
    ingredient = Ingredient("cheese")
    dish.add_ingredient_dependency(ingredient, 100)
    assert ingredient in dish.get_ingredients()
    assert dish.recipe[ingredient] == 100

    # Testa se get_restrictions retorna as restrições corretas
    cheese = Ingredient("cheese")
    cheese.restrictions = {Restriction.LACTOSE}
    dish = Dish("Spaghetti", 19.99)
    dish.add_ingredient_dependency(cheese, 100)
    expected_restrictions = {Restriction.LACTOSE}
    assert dish.get_restrictions() == expected_restrictions

    # Testa se get_ingredients retorna os ingredientes corretos
    dish = Dish("Spaghetti", 19.99)
    dish.add_ingredient_dependency(cheese, 100)
    assert dish.get_ingredients() == {cheese}

    # Testa que um TypeError é levantado se o ingrediente não for do tipo
    dish = Dish("Spaghetti", 19.99)
    with pytest.raises(TypeError):
        dish.add_ingredient_dependency("not_an_ingredient", 100)

    # Testa que o método de receita retorna a quantidade correta do ingrediente
    dish = Dish("Spaghetti", 19.99)
    ingredient = Ingredient("cheese")
    dish.add_ingredient_dependency(ingredient, 100)
    assert dish.recipe.get(ingredient) == 100

    # Testa que get_restrictions retorna o set de restrições esperado
    dish = Dish("Spaghetti", 19.99)
    ingredient = Ingredient("cheese")
    ingredient.restrictions = {Restriction.LACTOSE}
    dish.add_ingredient_dependency(ingredient, 100)
    expected_restrictions = {Restriction.LACTOSE}
    assert dish.get_restrictions() == expected_restrictions

    # Testa que get_ingredients retorna o set de ingredientes esperado
    dish = Dish("Spaghetti", 19.99)
    ingredient = Ingredient("cheese")
    dish.add_ingredient_dependency(ingredient, 100)
    assert dish.get_ingredients() == {ingredient}
