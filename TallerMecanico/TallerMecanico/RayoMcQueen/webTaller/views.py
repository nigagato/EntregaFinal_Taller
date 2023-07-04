from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout,authenticate,login as login_aut
from django.contrib.auth.decorators import login_required,permission_required
from .Carrito import *

# Create your views here.

def cerrar_sesion(request):
    categorias = Categoria.objects.all()
    repa= Reparacion.objects.filter(publicar=True).order_by("-nombre")[:3]
    logout(request)
    contexto = {'categorias':categorias,'reparaciones':repa}
    return render(request,"index.html",contexto)

def user_login(request):
    if request.method == 'POST':
        nom = request.POST.get("txtEmail")
        con = request.POST.get("pwdPass")
        usu = authenticate(request, username=nom, password=con)
        print(usu)
        if usu is not None and usu.is_active:
            login_aut(request,usu)
            categorias = Categoria.objects.all()
            repa= Reparacion.objects.all().order_by("-nombre")[:3]
            
            contexto = {'categorias':categorias,'reparaciones':repa}
            return render(request,"index.html",contexto)

    contexto = {'mensaje': 'Usuario/Contraseña Incorrecto'}
    return render(request, "login.html", contexto)

def index(request):
    categorias = Categoria.objects.all()
    repa = Reparacion.objects.filter(publicar=True).order_by("-nombre")[:3]
    contexto = {'categorias': categorias, 'reparaciones': repa}
    meca = request.user.groups.filter(name='mecanico').exists()
    superusuario = request.user.is_superuser
    contexto['meca'] = meca
    contexto['superusuario'] = superusuario
    return render(request, "index.html", contexto)

def galeria(request):
    reparaciones = Reparacion.objects.filter(publicar=True)
    repuestos = Repuesto.objects.filter(publicar=True)
    categorias = Categoria.objects.all()
    contar_reparaciones = Reparacion.objects.filter(publicar=True).count()
    contar_repuestos = Repuesto.objects.filter(publicar=True).count()
    contar = contar_reparaciones + contar_repuestos
    if request.method == 'POST':
        nom = request.POST.get("txtBuscar")
        reparaciones = Reparacion.objects.filter(nombre__contains=nom)
        contar_reparaciones = reparaciones.count()
        repuestos = Repuesto.objects.filter(nombre__contains=nom)
        contar_repuestos = repuestos.count()
        contar = contar_reparaciones + contar_repuestos
    contexto = {'reparaciones': reparaciones,'repuestos': repuestos,'cantidad': contar,'categorias': categorias}
    meca = request.user.groups.filter(name='mecanico').exists()
    superusuario = request.user.is_superuser
    contexto['meca'] = meca
    contexto['superusuario'] = superusuario
    return render(request, "galeria.html", contexto)

def filtro_descripcion(request):
    categorias = Categoria.objects.all()
    desc = request.POST.get("txtDesc")
    reparaciones = Reparacion.objects.filter(descripcion__contains=desc)
    contar = Reparacion.objects.filter(descripcion__contains=desc).count()
    contexto={'reparaciones':reparaciones,'cantidad':contar,'categorias':categorias}
    return render(request,"galeria.html",contexto)

def filtro_cate(request):
    cate = request.POST.get("cboCategoria")
    categorias = Categoria.objects.all()
    if cate=='Todos':
        reparaciones= Reparacion.objects.filter(publicar=True)
        contar = Reparacion.objects.filter(publicar=True).count()
    else:
        obj_cate = Categoria.objects.get(nombre=cate)
        reparaciones = Reparacion.objects.filter(categoria=obj_cate)
        contar = Reparacion.objects.filter(categoria=obj_cate).count()

    contexto={'reparaciones':reparaciones,'cantidad':contar,'categorias':categorias}
    return render(request,"galeria.html",contexto)

def filtro_categoria(request, id):
    cate = id
    categorias = Categoria.objects.all()
    if cate == 'Todos':
        reparaciones = Reparacion.objects.filter(publicar=True)
        contar = Reparacion.objects.filter(publicar=True).count()
    else:
        obj_cate = Categoria.objects.get(nombre=cate)
        reparaciones = Reparacion.objects.filter(categoria=obj_cate, publicar=True)
        contar = Reparacion.objects.filter(categoria=obj_cate, publicar=True).count()
    contexto = {'reparaciones': reparaciones, 'cantidad': contar, 'categorias': categorias}
    return render(request, "galeria.html", contexto)


def contacto(request):
    meca = request.user.groups.filter(name='mecanico').exists()
    superusuario = request.user.is_superuser
    usuario=request.user.username
    contexto={'usuario':usuario}
    contexto['meca'] = meca
    contexto['superusuario'] = superusuario
    return render(request,"contacto.html", contexto)

@login_required(login_url='/login/')
@permission_required('auth.add_user',login_url='/login/')
def registrarse(request):
    contexto={'mensaje':''}
    if request.POST:
        nombre=request.POST.get("txtNombre")
        email=request.POST.get("txtEmail")
        password=request.POST.get("pwdPass")
        usu = User()
        usu.set_password(password)
        usu.username=nombre
        usu.email=email
        try:
            usu.save()
            grupo=Group.objects.get(name='mecanico')
            usu.groups.add(grupo)
            contexto['mensaje']='Usuario registrado correctamente.'
            return render(request,"index.html",contexto)
        except:
            contexto["mensaje"]='Error al registrar usuario.'
    return render(request,"registrarse.html",contexto)


def registrar_normal(request):
    contexto={'mensaje':''}
    if request.POST:
        nombre=request.POST.get("txtNombre")
        email=request.POST.get("txtEmail")
        password=request.POST.get("pwdPass")
        usu = User()
        usu.set_password(password)
        usu.username=nombre
        usu.email=email
        try:
            usu.save()
            contexto['mensaje']='Usuario registrado correctamente.'
            return render(request,"index.html",contexto)
        except:
            contexto["mensaje"]='Error al registrar usuario.'
    return render(request,"registrar_normal.html",contexto)

def base(request):
    usuario=request.user.username
    meca = request.user.groups.filter(name='mecanico').exists()
    superusuario = request.user.is_superuser
    contexto={'usuario':usuario}
    contexto['meca'] = meca
    contexto['superusuario'] = superusuario
    return render(request,"base.html",contexto)

def agendar(request):
    return render(request,"agendar.html")

@login_required(login_url='/login/')
@permission_required(['webTaller.add_galeria', 'webTaller.view_galeria','webTaller.add_reparacion','webTaller.change_reparacion','webTaller.delete_reparacion','webTaller.view_reparacion'
                      ,'webTaller.add_repuesto','webTaller.change_repuesto','webTaller.delete_repuesto','webTaller.view_repuesto'],login_url='/login')
def admin_reparaciones(request):
    categorias=Categoria.objects.all()
    usuario=request.user.username
    usu = User.objects.get(username=usuario)
    reparaciones = Reparacion.objects.filter(usuario=usu)
    contexto={'categorias':categorias,'reparaciones':reparaciones}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        descripcion = request.POST.get("txtDescripcion")
        cate = request.POST.get("cboCategoria")
        foto= request.FILES.get("txtImg")
        obj_cate = Categoria.objects.get(nombre=cate)
        usu=request.user.username
        usuario = User.objects.get(username=usu)
        rep = Reparacion(
            nombre=nombre,
            descripcion=descripcion,
            categoria=obj_cate,
            foto=foto,
            usuario = usuario,
        )
        rep.save()
        contexto["mensaje"]="Grabo"
        return render(request,"admin_reparaciones.html",contexto)
    meca = request.user.groups.filter(name='mecanico').exists()
    superusuario = request.user.is_superuser
    contexto['meca'] = meca
    contexto['superusuario'] = superusuario
    return render(request,"admin_reparaciones.html",contexto)

@login_required(login_url='/login/')
@permission_required(['webTaller.add_galeria', 'webTaller.view_galeria','webTaller.add_reparacion','webTaller.change_reparacion','webTaller.delete_reparacion','webTaller.view_reparacion'
                      ,'webTaller.add_repuesto','webTaller.change_repuesto','webTaller.delete_repuesto','webTaller.view_repuesto'],login_url='/login')
def admin_repuestos(request):
    categorias=Categoria.objects.all()
    usuario=request.user.username
    usu = User.objects.get(username=usuario)
    repuestos = Repuesto.objects.filter(usuario=usu)
    contexto={'categorias':categorias,'repuestos':repuestos}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        descripcion = request.POST.get("txtDescripcion")
        cate = request.POST.get("cboCategoria")
        foto= request.FILES.get("txtImg")
        precio = request.POST.get("txtPrecio")
        obj_cate = Categoria.objects.get(nombre=cate)
        usu=request.user.username
        usuario = User.objects.get(username=usu)
        rep = Repuesto(
            nombre=nombre,
            descripcion=descripcion,
            categoria=obj_cate,
            foto=foto,
            usuario = usuario,
            precio=precio
        )
        rep.save()
        contexto["mensaje"]="Grabo"
        return render(request,"admin_repuestos.html",contexto)
    meca = request.user.groups.filter(name='mecanico').exists()
    superusuario = request.user.is_superuser
    contexto['meca'] = meca
    contexto['superusuario'] = superusuario
    return render(request,"admin_repuestos.html",contexto)

@login_required(login_url='/login/')
@permission_required(['webTaller.add_galeria', 'webTaller.view_galeria','webTaller.add_reparacion','webTaller.change_reparacion','webTaller.delete_reparacion','webTaller.view_reparacion'
                      ,'webTaller.add_repuesto','webTaller.change_repuesto','webTaller.delete_repuesto','webTaller.view_repuesto'],login_url='/login')
def lista_repuestos(request):
    categorias=Categoria.objects.all()
    usuario=request.user.username
    usu = User.objects.get(username=usuario)
    repuestos = Reparacion.objects.filter(usuario=usu)
    contexto={'categorias':categorias,'repuestos':repuestos}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        descripcion = request.POST.get("txtDescripcion")
        cate = request.POST.get("cboCategoria")
        foto= request.FILES.get("txtImg")
        precio = request.POST.get("txtPrecio")
        obj_cate = Categoria.objects.get(nombre=cate)
        usu=request.user.username
        usuario = User.objects.get(username=usu)
        rep = Reparacion(
            nombre=nombre,
            descripcion=descripcion,
            categoria=obj_cate,
            foto=foto,
            usuario = usuario,
            precio=precio
        )
        rep.save()
        contexto["mensaje"]="Grabo"
        return render(request,"lista_repuestos.html",contexto)
    return render(request,"lista_repuestos.html",contexto)

@login_required(login_url='/login/')
@permission_required(['webTaller.add_galeria', 'webTaller.view_galeria','webTaller.add_reparacion','webTaller.change_reparacion','webTaller.delete_reparacion','webTaller.view_reparacion'
                      ,'webTaller.add_repuesto','webTaller.change_repuesto','webTaller.delete_repuesto','webTaller.view_repuesto'],login_url='/login')
def lista_reparaciones(request):
    categorias=Categoria.objects.all()
    usuario=request.user.username
    usu = User.objects.get(username=usuario)
    reparaciones = Reparacion.objects.filter(usuario=usu)
    contexto={'categorias':categorias,'reparaciones':reparaciones}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        descripcion = request.POST.get("txtDescripcion")
        cate = request.POST.get("cboCategoria")
        foto= request.FILES.get("txtImg")
        precio = request.POST.get("txtPrecio")
        obj_cate = Categoria.objects.get(nombre=cate)
        usu=request.user.username
        usuario = User.objects.get(username=usu)
        rep = Reparacion(
            nombre=nombre,
            descripcion=descripcion,
            categoria=obj_cate,
            foto=foto,
            usuario = usuario,
            precio=precio
        )
        rep.save()
        contexto["mensaje"]="Grabo"
        return render(request,"lista_reparaciones.html",contexto)
    return render(request,"lista_reparaciones.html",contexto)

def ficha(request, nombre):
    reparacion = Reparacion.objects.get(nombre=nombre)
    galeria = Galeria.objects.filter(reparacion=reparacion)
    data = {'reparacion': reparacion,'galeria':galeria}
    return render(request,'fichas.html', data)

@login_required(login_url='/login/')
@permission_required(['webTaller.delete_reparacion','webTaller.delete_repuesto'],login_url='/login')
def eliminar(request,id):
    reparacion = Reparacion.objects.get(idReparacion=id)
    categorias= Categoria.objects.all()
    usuario=request.user.username
    usu = User.objects.get(username=usuario)
    reparaciones= Reparacion.objects.filter(usuario=usu)
    data={'categorias':categorias,'reparaciones':reparaciones}
    data['mensaje']=''
    try:
        reparacion.delete()
        data["mensaje"]= 'elimino'
    except:
        data["mensaje"]= 'no elimino'
    return render(request,"admin_reparaciones.html",data)

@login_required(login_url='/login/')
@permission_required(['webTaller.change_reparacion','webTaller.change_repuesto'],login_url='/login')
def modificar(request,id):
    reparacion = Reparacion.objects.get(idReparacion=id)
    categorias = Categoria.objects.all()
    data = {'reparacion':reparacion,'categorias':categorias}
    return render(request,"modificar.html",data)

@login_required(login_url='/login/')
@permission_required(['webTaller.change_reparacion','webTaller.change_repuesto'],login_url='/login')
def modificar_reparacion(request):
    if request.POST:
        id= request.POST.get("txtId")
        nombre = request.POST.get("txtNombre")
        descripcion = request.POST.get("txtDescripcion")
        cate = request.POST.get("cboCategoria")
        foto= request.FILES.get("txtImg")
        obj_cate = Categoria.objects.get(nombre=cate)
        usu=request.user.username
        usuario = User.objects.get(username=usu)
        rep = Reparacion.objects.get(idReparacion=id)
        rep.nombre = nombre
        rep.descripcion = descripcion
        rep.categoria = obj_cate
        if foto is not None:
            rep.foto = foto
        rep.usuario = usuario
        rep.save()
    return redirect('/admin_reparaciones/')


######################
@login_required(login_url='/login/')
@permission_required(['webTaller.delete_reparacion','webTaller.delete_repuesto'],login_url='/login')
def eliminar_repuesto(request,id):
    repuesto = Repuesto.objects.get(idRepuesto=id)
    categorias= Categoria.objects.all()
    usuario=request.user.username
    usu = User.objects.get(username=usuario)
    repuestos= Repuesto.objects.filter(usuario=usu)
    data={'categorias':categorias,'repuestos':repuestos}
    data['mensaje']=''
    try:
        repuesto.delete()
        data["mensaje"]= 'elimino'
    except:
        data["mensaje"]= 'no elimino'
    return render(request,"admin_repuestos.html",data)


##
@login_required(login_url='/login/')
@permission_required('webTaller.add_galeria',login_url='/login')
def grabar_galeria(request):
    if request.POST:
        id = request.POST.get("txtId")
        foto = request.FILES.get("txtFoto")
        reparacion = Reparacion.objects.get(idReparacion=id)
        gale= Galeria(
            foto= foto,
            reparacion=reparacion
        )
        gale.save()
    return redirect("/admin_reparaciones/")


#####

def agregar_articulo(request, id_articulo):
    carrito = Carrito(request)
    repuesto = Repuesto.objects.get(idRepuesto = id_articulo)
    carrito.agregar(repuesto)
    return redirect('/galeria/')

def agregar_articulo_carrito(request, id_articulo):
    carrito = Carrito(request)
    repuesto = Repuesto.objects.get(idRepuesto = id_articulo)
    carrito.agregar(repuesto)
    return redirect('/carrito/')

def quitar_articulo(request, id_articulo):
    carrito = Carrito(request)
    repuesto = Repuesto.objects.get(idRepuesto = id_articulo)
    carrito.quitar(repuesto)
    return redirect('/carrito/')

def vaciar(request):
    carrito = Carrito(request)
    carrito.vaciar()
    return redirect('/galeria/')

def eliminar_arti(request,id_articulo):
    carrito = Carrito(request)    
    repuesto = Repuesto.objects.get(idRepuesto = id_articulo)
    carrito.eliminar(repuesto)
    return redirect('/galeria/')    

def carrito(request):
    return render(request,"carrito.html")

def guardar_contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        email = request.POST.get('txtEmailMensaje')
        telefono = request.POST.get('txtTelefono')
        mensaje = request.POST.get('txtMensaje')
        contacto = Contacto(nombre=nombre, email=email, telefono=telefono, mensaje=mensaje)
        contacto.save()

        return redirect('/contacto/') 

    return redirect('/contacto/')