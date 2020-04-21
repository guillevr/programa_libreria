from flask import Flask, render_template,abort
app = Flask(__name__)	

import json,random
with open("books.json") as fichero:
	datos=json.load(fichero)

##################################################################################
## Crearemos una lista donde almacenaremos todos los libros, incluyendo los que no 
## tienen algun tipo de informacion.

biblioteca=[]

for libro in datos:

    ## Comprobacion de que tiene titulo.
    try:
        titulo=libro["title"]
    except KeyError:
        titulo="No tiene título."

    ## Comprobacion de que tiene ISBN.
    try:
        isbn=libro["isbn"]
    except KeyError:
        isbn=libro["title"][:3] + str(random.randint(0000000, 9999999))

    ## Comprobacion de que tiene paginas.
    try:
        npag=libro["pageCount"]
    except KeyError:
        npag="No está registrado el número de páginas."
        
    ## Comprobacion de que tiene datos de publicacion.
    ## dp -> datos de publicacion
    try:
        dp=libro["publishedDate"]
    except KeyError:
        dp="No hay datos de publicacion."
    
    ## Comprobacion de que tiene imagen.
    try:
        img=libro["thumbnailUrl"]
    except KeyError:
        img="No hay datos de publicacion."
    
    ## Comprobacion de que tiene descripcion corta.
    try:
        des_cor=libro["shortDescription"]
    except KeyError:
        des_lar=[]
    
    ## Comprobacion de que tiene descripcion larga.
    try:
        des_lar=libro["longDescription"]
    except KeyError:
        des_lar=[]

    ## Comprobacion de que tiene un estado.
    try:
        estado=libro["status"]
    except KeyError:
        estado="No hay estado."    

    ## Comprobacion de que tiene autores.
    try:
        autores=libro["authors"]
    except KeyError:
        lautores=[]
        autores=lautores

    ## Comprobacion de que tiene categorias.
    try:
        categorias=libro["categories"]
    except KeyError:
        categoria=[]
        categorias=categoria

    dic={"title":titulo,"isbn":isbn,"pageCount":npag,"publishedDate":dp,"thumbnailUrl":img,"shortDescription":des_cor,"longDescription":des_lar,"status":estado,"authors":autores,"categories":categorias}
    
    biblioteca.append(dic)

##################################################################################

### Programa para mostrar la informacion de los libros.
@app.route('/',methods=["GET","POST"])
def inicio():

    ## tit_isbn -> en esta lista guardaremos los titulos y los isbn

    tit_isbn=[]

    for libro in biblioteca:
        dic={"titulo":libro["title"],"isbn":libro["isbn"]}
        tit_isbn.append(dic)

    return render_template("inicio.html",nombre="Guillermo Vizcaino",libros=tit_isbn)


