import unittest
from Product import Product

# Testes para apply_discount
def test_apply_discount_success():
    product = Product("Arroz", 100)
    new_price = product.apply_discount(10)
    assert new_price == 90
    assert product.price == 90


def test_apply_discount_failure():
    product = Product("Feijão", 50)
    with pytest.raises(ValueError) as excinfo:
        product.apply_discount(150)  # Desconto inválido
    assert str(
        excinfo.value) == "Discount percentage must be between 0 and 100"


# Testes para update_name
def test_update_name_success():
    product = Product("Macarrão", 30)
    new_name = product.update_name("Espaguete")
    assert new_name == "Espaguete"
    assert product.name == "Espaguete"


def test_update_name_failure():
    product = Product("Café", 20)
    with pytest.raises(ValueError) as excinfo:
        product.update_name("")  # Nome inválido
    assert str(excinfo.value) == "Product name must be a non-empty string"


if __name__ == '__main__':
    unittest.main()