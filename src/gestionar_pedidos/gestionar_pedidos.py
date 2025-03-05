class Pedido:
    def __init__(self, numero_orden, nombre_cliente, productos, estado="Pendiente"):
        self.numero_orden = numero_orden
        self.nombre_cliente = nombre_cliente
        self.productos = productos
        self.estado = estado

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def __repr__(self):
        return f"Pedido({self.numero_orden}, {self.nombre_cliente}, {self.productos}, {self.estado})"


class GestionPedidos:
    def __init__(self):
        self.pedidos = []
        self.pedidos_dict = {}

    def agregar_pedido(self, numero_orden, nombre_cliente, productos):
        pedido = Pedido(numero_orden, nombre_cliente, productos)
        self.pedidos.append(pedido)
        self.pedidos_dict[numero_orden] = pedido

    def actualizar_estado(self, numero_orden, nuevo_estado):
        if numero_orden in self.pedidos_dict:
            self.pedidos_dict[numero_orden].actualizar_estado(nuevo_estado)

    def listar_pedidos(self):
        return self.pedidos

    def listar_pedidos_pendientes(self):
        return [pedido for pedido in self.pedidos if pedido.estado == "Pendiente"]

    def buscar_pedido(self, numero_orden):
        return self.pedidos_dict.get(numero_orden, None)


if __name__ == "__main__":
    gestion = GestionPedidos()
    gestion.agregar_pedido(1, "Mario", ["Pizza", "Coca Cola"])
    gestion.agregar_pedido(2, "Luigi", ["Pasta", "Agua"])
    
    print("Todos los pedidos:", gestion.listar_pedidos())
    print("Pedidos pendientes:", gestion.listar_pedidos_pendientes())
    
    gestion.actualizar_estado(1, "Listo")
    print("Pedido actualizado:", gestion.buscar_pedido(1))