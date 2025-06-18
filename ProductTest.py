        import unittest
        from Product import Product

        class TestProduct(unittest.TestCase):
            def setUp(self):
                self.product = Product(1, "PlayStation 5", 10, 4000)

            def tearDown(self):
                print(f"\nTest {self._testMethodName} finished. \nTear down executed")

            def test_increase_stock(self):
                #testando valor válido para função
                initial_stock = self.product.stock
                self.product.increase_stock(5)
                self.assertEqual(self.product.stock, initial_stock + 5)

                #testando valor invalido para função
                with self.assertRaises(Exception) as context:
                    self.product.increase_stock(-1)

            def test_decrease_stock(self):
                #testando valor válido para função
                initial_stock = self.product.stock
                self.product.decrease_stock(5)
                self.assertEqual(self.product.stock, initial_stock - 5)

                #testando valor inválido para função com numero maior que o disponível
                with self.assertRaises(Exception):
                    self.product.decrease_stock(20)

                #testando valor inválido para função com numero negativo
                with self.assertRaises(Exception):
                    self.product.decrease_stock(-1)

            def test_check_negative_stock(self):
                #testando valor válido para função
                with self.assertRaises(Exception):
                    self.product.check_negative_stock(-1)

                #testando se ele não mostra exceção quando o valor é positivo
                try:
                    self.product.check_negative_stock(5)
                except Exception as e:
                    self.fail(f"check_negative_stock raised unexpected Exception: {e}")

            def test_check_positive_number(self):
                #testando se ele não mostra exceção quando o valor é positivo
                try:
                    self.product.check_positive_number(5)
                except Exception as e:
                    self.fail(f"check_positive_number raised unexpected Exception: {e}")

                #testando valor inválido para função
                with self.assertRaises(Exception):
                    self.product.check_positive_number(-1)



        if __name__ == '__main__':
            unittest.main()
