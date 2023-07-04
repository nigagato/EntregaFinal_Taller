def total(request):
    tot = 0
    try:        
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                tot += int(value["total"])
    except:
        tot = 0
    return {"total":tot}


def cantidades(request):
    cant = 0
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            cant +=int(value["cantidad"])
    return {"cantidades":cant}
