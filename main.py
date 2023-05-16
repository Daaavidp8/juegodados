import juego
"""Iniciador del Joc"""
x = juego.Juego(str(input("Introdueix el nom del primer jugador: ")),
                str(input("Introdueix el nom del segon jugador: ")),
                str(input("Introdueix el nom del tercer jugador: ")),
                int(input("Introdueix el nombre de cares per el primer dau: ")),
                int(input("Introdueix el nombre de cares per el segon dau: ")),
                int(input("Introdueix el nombre de cares per el tercer dau: ")),
                int(input("Introdueix el nombre de cares per el cuart dau: ")),
                int(input("Introdueix el nombre de llançaments: ")),
                input("¿Vols vore els resultats intermitjans per pantalla? (S/N): "))

x.jugar()
x.mostrarPuntuaciones()
