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


### Programa  para la pagina detalle del libro
@app.route('/libro/<isbn>')
def detalles_libro(isbn):

    isbns=[]

    for libro in biblioteca:
        isbns.append(libro["isbn"])

    if isbn not in isbns:
        abort(404)
    else:
        for libro in biblioteca:
            if libro["isbn"]==isbn:
                if libro["status"]=="MEAP":
                    meap="ESTE LIBRO NO SE HA PUBLICADO"
                    return render_template("template1.html",meap=meap)
                else:
                    img=libro["thumbnailUrl"]      
                    npag=libro["pageCount"]
                    desc_larga=[libro["longDescription"]]
                    desc_corta=[libro["shortDescription"]]

                    ### Autores
                    nautores=""

                    for autor in libro["authors"]:
                        nautores=nautores+autor+", "
                    
                    nautores=nautores[:len(nautores)-2]
                    ###################################

                    
                    if len(libro["categories"]) != 0:

                        autores=libro["authors"]
                        categorias=libro["categories"]

                        if len(libro["longDescription"]) == 0 and len(libro["shortDescription"]) == 0:
                            return render_template("template1.html",titulo=libro["title"],npag=npag,autores=nautores,categorias=categorias,imagen=img)
                        elif len(libro["longDescription"]) != 0:
                            desc_larga=libro["longDescription"]
                            return render_template("template1.html",titulo=libro["title"],npag=npag,desc_larga=desc_larga,autores=nautores,categorias=categorias,imagen=img)
                        elif len(libro["shortDescription"]) != 0:
                            desc_corta=libro["shortDescription"]
                            return render_template("template1.html",titulo=libro["title"],npag=npag,desc_corta=desc_corta,autores=nautores,categorias=categorias,imagen=img)
                        else:
                            desc_corta=libro["shortDescription"]
                            return render_template("template1.html",titulo=libro["title"],npag=npag,desc_corta=desc_corta,autores=nautores,categorias=categorias,imagen=img)

                    else:

                        if len(libro["longDescription"]) == 0 and len(libro["shortDescription"]) == 0:
                            return render_template("template1.html",titulo=libro["title"],npag=npag,autores=nautores,imagen=img)
                        elif len(libro["longDescription"]) != 0:
                            desc_larga=libro["longDescription"]
                            return render_template("template1.html",titulo=libro["title"],npag=npag,desc_larga=desc_larga,autores=nautores,imagen=img)
                        elif len(libro["shortDescription"]) != 0:
                            desc_corta=libro["shortDescription"]
                            return render_template("template1.html",titulo=libro["title"],npag=npag,desc_corta=desc_corta,autores=nautores,imagen=img)
                        else:
                            desc_corta=libro["shortDescription"]
                            return render_template("template1.html",titulo=libro["title"],npag=npag,desc_corta=desc_corta,autores=nautores,imagen=img)

     

	
app.run(debug=True)
