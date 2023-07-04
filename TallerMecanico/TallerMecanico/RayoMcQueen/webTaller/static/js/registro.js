class registro{
    nombre;
    password;
    email;


    //mutadores
    setNombre(nombre){
        this.nombre=nombre;
    }
    
    setEmail(email){
        this.email=email;
    }
    setPassword(pass){
        this.password=pass;
    }
    
    //accesadores
    getNombre(){ return this.nombre;}
    getEmail(){ return this.email;}
    getPassword(){ return this.password;}
}  