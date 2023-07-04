class repuesto{
    id;
    nombre;
    precio;

    setId(id){
        this.id = id;
    }
    getId(){
        return this.id;
    }
    setNombre(nombre){
        this.nombre = nombre;
    }
    setPrecio(precio){
        this.precio = precio;
    }
    getNombre(){ return this.nombre; }
    getPrecio(){ return this.precio; }
}