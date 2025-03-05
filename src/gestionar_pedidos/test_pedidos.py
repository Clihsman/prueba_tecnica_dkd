import unittest
from gestionar_pedidos import GestionPedidos, Pedido

class TestGestionPedidos(unittest.TestCase):
    def setUp(self):
        self.gestion = GestionPedidos()
        self.gestion.agregar_pedido(1, "Mario", ["Pizza", "Coca Cola"])
        self.gestion.agregar_pedido(2, "Luigi", ["Pasta", "Agua"])

    def test_agregar_pedido(self):
        self.assertEqual(len(self.gestion.listar_pedidos()), 2)

    def test_actualizar_estado(self):
        self.gestion.actualizar_estado(1, "Listo")
        self.assertEqual(self.gestion.buscar_pedido(1).estado, "Listo")

    def test_listar_pedidos_pendientes(self):
        self.assertEqual(len(self.gestion.listar_pedidos_pendientes()), 2)
        self.gestion.actualizar_estado(1, "Listo")
        self.assertEqual(len(self.gestion.listar_pedidos_pendientes()), 1)

    def test_buscar_pedido(self):
        pedido = self.gestion.buscar_pedido(1)
        self.assertIsNotNone(pedido)
        self.assertEqual(pedido.nombre_cliente, "Mario")

if __name__ == "__main__":
    unittest.main()