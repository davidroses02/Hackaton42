from urllib.parse import urlparse
from s_amazon import get_reviews
from feelings import main

def user_interface():
    print("""\033[1;36m _  _     __                                              _                                
( )( )  /'__`\                                           ( )_               _              
| || | (_)  ) )      ___    _     ___ ___     __    ___  | ,_)   _ _  _ __ (_)   _     ___ 
| || |_   /' /     /'___) /'_`\ /' _ ` _ `\ /'__`\/' _ `\| |   /'_` )( '__)| | /'_`\ /',__)
(__ ,__)/' /( )   ( (___ ( (_) )| ( ) ( ) |(  ___/| ( ) || |_ ( (_| || |   | |( (_) )\__, \\
   (_) (_____/'   `\____)`\___/'(_) (_) (_)`\____)(_) (_)`\__)`\__,_)(_)   (_)`\___/'(____/
                                                                                           \033[0m""")
    print("""\n\n\033[1;32mDescripcion:\n \033[1;33m\t-> La finalidad de esta aplicación es dar valor a los comentarios de distintas plataformas.
    \t-> Utilizamos web scrapping para recoger la información y distintas librerías para el análisis de la información y la presentación de la misma. \033[0m""", end="\n\n")
    
    print("\033[1;94m\nDisponemos de las siguientes opciones para verificar los comentarios:\033[0m\n\t\033[1;97m1: Amazon Store.\033[0m", end="\n\n")
    
    select = input("\033[1;96mInserte una opción:\n>>> ")
    while select.isnumeric() == False or int(select) != 1:
        select = input("Inserte una opción:\n>>> ")
    url = input("Inserte el enlace al producto de amazon:\n>>> ")
    # insertar funcion para escanear los comentarios
    try:
        print("\n\n\033[1;92mScanning reviews ...")
        main(url)
        print("Done!\033[0m")
    except:
        print("\033[1;91mBROKEN LINK!!!! Exiting...\033[0m")
    #list_r = get_reviews(url)
    #for r in list_r:
    #    open('list.txt', 'a').write(r + '\n')
           
if __name__ == '__main__':
    user_interface()