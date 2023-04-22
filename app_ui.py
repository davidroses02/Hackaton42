from urllib.parse import urlparse
from s_amazon import get_reviews

def user_interface():
    print(""" _  _     __                                              _                                
( )( )  /'__`\                                           ( )_               _              
| || | (_)  ) )      ___    _     ___ ___     __    ___  | ,_)   _ _  _ __ (_)   _     ___ 
| || |_   /' /     /'___) /'_`\ /' _ ` _ `\ /'__`\/' _ `\| |   /'_` )( '__)| | /'_`\ /',__)
(__ ,__)/' /( )   ( (___ ( (_) )| ( ) ( ) |(  ___/| ( ) || |_ ( (_| || |   | |( (_) )\__, \\
   (_) (_____/'   `\____)`\___/'(_) (_) (_)`\____)(_) (_)`\__)`\__,_)(_)   (_)`\___/'(____/
                                                                                           """)
    print("\n\n Descripcion\n textotextotextotextotextotextotextotextotextotextotextotextotextotextotextotexto", end="\n\n")
    
    print("\nDisponemos de las siguientes opciones para verificar los comentarios:\n\t1: Amazon Store.", end="\n\n")
    
    select = input("Inserte una opción:\n>>> ")
    while select.isnumeric() == False or int(select) != 1:
        select = input("Inserte una opción:\n>>> ")
    url = input("Inserte el enlace al producto de amazon:\n>>> ")
    #insertar funcion para escanear los comentarios
    list_r = get_reviews(url)
    for r in list_r:
        open('list.txt', 'a').write(r + '\n')
           
    
user_interface()