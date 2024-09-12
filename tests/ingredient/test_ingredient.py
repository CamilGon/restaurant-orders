from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingrediente1 = Ingredient("farinha")
    assert ingrediente1.name == "farinha"
    assert ingrediente1.restrictions == {Restriction.GLUTEN}

    ingrediente2 = Ingredient("presunto")
    assert ingrediente2.name == "presunto"
    assert ingrediente2.restrictions == {Restriction.ANIMAL_MEAT,
                                         Restriction.ANIMAL_DERIVED}

    assert repr(ingrediente1) == "Ingredient('farinha')"
    assert repr(ingrediente2) == "Ingredient('presunto')"

    assert ingrediente1 == Ingredient("farinha")
    assert ingrediente1 != ingrediente2

    assert hash(ingrediente1) == hash(Ingredient("farinha"))
    assert hash(ingrediente1) != hash(ingrediente2)

    ingrediente3 = Ingredient("água")
    assert ingrediente3.name == "água"
    assert ingrediente3.restrictions == set()

    assert ingrediente3 != ingrediente1
    assert ingrediente3 != ingrediente2
