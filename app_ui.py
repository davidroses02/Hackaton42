from urllib.parse import urlparse
from s_amazon import get_reviews
from feelings import main

def user_interface():
    print(""" _  _     __                                              _                                
( )( )  /'__`\                                           ( )_               _              
| || | (_)  ) )      ___    _     ___ ___     __    ___  | ,_)   _ _  _ __ (_)   _     ___ 
| || |_   /' /     /'___) /'_`\ /' _ ` _ `\ /'__`\/' _ `\| |   /'_` )( '__)| | /'_`\ /',__)
(__ ,__)/' /( )   ( (___ ( (_) )| ( ) ( ) |(  ___/| ( ) || |_ ( (_| || |   | |( (_) )\__, \\
   (_) (_____/'   `\____)`\___/'(_) (_) (_)`\____)(_) (_)`\__)`\__,_)(_)   (_)`\___/'(____/
                                                                                           """)
    print("""\n\n Descripcion:\n La finalidad de esta aplicación es dar valor a los comentarios de distintas plataformas.
      Utilizamos web scrapping para recoger la información y distintas librerías para el análisis de la información y la presentación de la misma. """, end="\n\n")
    
    print("\nDisponemos de las siguientes opciones para verificar los comentarios:\n\t1: Amazon Store.", end="\n\n")
    
    select = input("Inserte una opción:\n>>> ")
    while select.isnumeric() == False or int(select) != 1:
        select = input("Inserte una opción:\n>>> ")
    url = input("Inserte el enlace al producto de amazon:\n>>> ")
    # insertar funcion para escanear los comentarios
    main(url)
    #list_r = get_reviews(url)
    #for r in list_r:
    #    open('list.txt', 'a').write(r + '\n')
           
if __name__ == '__main__':
    user_interface()