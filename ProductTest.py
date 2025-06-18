import unittest
from Product import Product  # Ajuste o nome do arquivo se necessário


class TestProduct(unittest.TestCase):

    # Teste de sucesso para o método apply_discount
    def test_apply_discount_success(self):
        # Cria um produto com nome, estoque e preço
        product = Product("Arroz", 10, 100)
        result = product.apply_discount(10)  # Aplica desconto de 10%

        # Verifica se o novo preço está correto
        self.assertEqual(result, 90)
        self.assertEqual(product.price, 90)
        self.assertTrue(product.price < 100)

    # Teste de falha para o método apply_discount
    def test_apply_discount_failure(self):
        # Cria um produto com nome, estoque e preço
        product = Product("Feijão", 5, 50)

        try:
            product.apply_discount(150)  # Desconto inválido (>100%)
            self.assertFalse(True)  # Se não lançar exceção, o teste falha
        except Exception as e:
            self.assertEqual(str(e),
                             "Discount percentage must be between 0 and 100")

    # Teste de sucesso para o método update_name
    def test_update_name_success(self):
        # Cria um produto com nome, estoque e preço
        product = Product("Macarrão", 15, 30)
        result = product.update_name("Espaguete")

        # Verifica se o nome foi alterado corretamente
        self.assertEqual(result, "Espaguete")
        self.assertEqual(product.name, "Espaguete")
        self.assertTrue(product.name == "Espaguete")

    # Teste de falha para o método update_name
    def test_update_name_failure(self):
        # Cria um produto com nome, estoque e preço
        product = Product("Café", 8, 20)

        try:
            product.update_name("")  # Nome inválido (string vazia)
            self.assertFalse(True)  # Se não lançar exceção, o teste falha
        except Exception as e:
            self.assertEqual(str(e), "Product name must be a non-empty string")

    # Teste usando assertFalse para verificar que o preço não aumentou
    def test_apply_discount_assert_false(self):
        # Cria um produto com nome, estoque e preço
        product = Product("Açúcar", 20, 200)
        product.apply_discount(10)  # Preço esperado: 180

        # Verifica que o preço final não é maior ou igual ao original
        self.assertFalse(product.price >= 200)


if __name__ == '__main__':
    unittest.main()
