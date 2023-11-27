def importe_total_carro(request):
    total = 0
    total_trans = 0
    productos_string = ""
    cadena_formateada="0" 
    lista_productos = []

    if request.user.is_authenticated:
        if "carro" in request.session:
            for key, value in request.session["carro"].items():
                total += value["precio"]

                # Obtener el nombre del producto y agregarlo a la cadena
                nombre_producto = value['nombre']
                cantidad=value['cantidad']
                productos_string += f"{nombre_producto} {cantidad},"
                
                lista_productos.append({
                    "nombre": nombre_producto,
                    "cantidad": cantidad,
                    "precio": value["precio"],
                })

            # Eliminar la coma adicional al final de la cadena
            productos_string = productos_string.rstrip(', ')
        
        
        total_trans = round(total * 0.0011, 2) # para la transformacion de CLP a USD
        if total > 0 :
            cadena_formateada = f"{total / 1000.0:,.3f}" # para dejarlo en decimales


    return {"importe_total_carro": total,"total_formateado":cadena_formateada,"valor_total": total_trans,
            "lista_producto": productos_string,"carrito": lista_productos}
