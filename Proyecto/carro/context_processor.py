def importe_total_carro(request):
    total = 0
    numero_formateado = ""  
    
    if request.user.is_authenticated:
        if "carro" in request.session:
            for key, value in request.session["carro"].items():
                total = total + value["precio"]
    
    total_formateado = ""

    if total:
        # Formatear 'total' con puntos como separadores de miles
        total_formateado = "{:,.0f}".format(total).replace(',', '.')

    return {"importe_total_carro": total_formateado}
                

