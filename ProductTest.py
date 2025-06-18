import unittest
from Product import Product 

class TestProduct(unittest.TestCase):

    # O setUp sendo chamado antes dos testes
    def setUp(self):
        print("\nIniciando um novo teste...")
        # Criando diferentes produtos para cada cenário
        self.product1 = Product(1, "Arroz", 10, 100.0)
        self.product2 = Product(2, "Feijão", 10, 50.0)
        self.product3 = Product(3, "Macarrão", 10, 30.0)
        self.product4 = Product(4, "Café", 10, 20.0)
        self.product5 = Product(5, "Açúcar", 5, 10.0)
        self.product6 = Product(6, "Farinha", 10, 15.0)

    # O tearDown sendo chamado depois dos testes
    def tearDown(self):
        print("Teste finalizado!")

    # Teste de sucesso para increase_stock
    def test_increase_stock_success(self):
        self.product1.increase_stock(5)
        self.assertEqual(self.product1.stock, 15)
        self.assertTrue(self.product1.stock > 10)

    # Teste de falha para increase_stock (valor negativo ou zero)
    def test_increase_stock_failure(self):
        with self.assertRaises(Exception) as context:
            self.product2.increase_stock(0)
        self.assertEqual(str(context.exception), "O número deve ser positivo")

        with self.assertRaises(Exception) as context:
            self.product2.increase_stock(-3)
        self.assertEqual(str(context.exception), "O número deve ser positivo")

    # Teste de sucesso para decrease_stock
    def test_decrease_stock_success(self):
        self.product3.decrease_stock(4)
        self.assertEqual(self.product3.stock, 6)
        self.assertTrue(self.product3.stock < 10)

    # Teste de falha para decrease_stock (valor negativo ou estoque insuficiente)
    def test_decrease_stock_failure_negative_quantity(self):
        with self.assertRaises(Exception) as context:
            self.product4.decrease_stock(0)
        self.assertEqual(str(context.exception), "O número deve ser positivo")

    def test_decrease_stock_failure_insufficient_stock(self):
        with self.assertRaises(Exception) as context:
            self.product5.decrease_stock(10)
        self.assertEqual(str(context.exception), "O estoque deve ser positivo")

    # Teste extra usando assertFalse
    def test_decrease_stock_assert_false(self):
        self.product6.decrease_stock(3)
        self.assertFalse(self.product6.stock == 10)

if __name__ == '__main__':
    unittest.main()