class Carro:
    def __init__(self,request) :
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        
        self.carro=carro


    def agregar(self,producto):
        if(str(producto.id_Producto) not in self.carro.keys()):
            self.carro[producto.id_Producto]={
                "producto_id":producto.id_Producto,
                "nombre":producto.nombre_P,
                "precio":producto.precio,
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id_Producto):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=value["precio"]+producto.precio
                    break
        self.guardar_carro()
    

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self,producto):
        producto.id_Producto=str(producto.id_Producto)
        if producto.id_Producto in self.carro:
            del self.carro[producto.id_Producto]
            self.guardar_carro()

    def restar_producto(self,producto):
        for key, value in self.carro.items():
            if key==str(producto.id_Producto):
                value["cantidad"]=value["cantidad"]-1 
                value["precio"]=value["precio"]-producto.precio
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break  
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
         
    