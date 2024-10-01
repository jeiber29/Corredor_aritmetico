# Corredor Aritmético

Autor: Jeiber Dev

## Descripción

`Corredor Aritmético` es un juego educativo desarrollado en Python utilizando la biblioteca Pygame. El objetivo del juego es ayudar al jugador a avanzar respondiendo correctamente a operaciones matemáticas. Hay tres niveles de dificultad que desafiarán tus habilidades aritméticas en sumas, restas, multiplicaciones y divisiones.

# El juego cuenta con dos personajes:

Jugador: Avanza hacia la meta si aciertas la respuesta.
Enemigo: Avanza cuando fallas, compitiendo por llegar a la meta antes que tú.

# Niveles de dificultad:

Nivel Básico: Operaciones de suma y resta.
Nivel Medio: Incluye multiplicaciones.
Nivel Difícil: Operaciones de suma, resta, multiplicación y división.

# Mecánica del juego:

Selecciona entre tres opciones de respuesta para resolver una operación aritmética.
Cada respuesta correcta mueve al jugador más cerca de la meta, mientras que las respuestas incorrectas benefician al enemigo.
El primero en llegar a la meta gana la partida.

# Características:

Interfaz visual con imágenes para el jugador, enemigo y meta.
Fondo interactivo y sonidos de retroalimentación para las selecciones y el final del juego.
Tres niveles de dificultad.
Sistema de reintento tras perder o ganar.
Instalación y Ejecución

# Requisitos:

Python 3.8 o superior.
Pygame.

# Para instalar Pygame:

pip install pygame

# Ejecución: 

Asegúrate de que los archivos de imágenes (fondo.png, jugador.png, enemigo.png, meta.png, pista.png) y los sonidos (sonido_boton.wav, felicitaciones_sonido.wav, perdedor_sonido.wav) estén en el mismo directorio que el archivo del código fuente.

# Ejecuta el archivo del juego:

python corredor_aritmetico.py

### `Descripción de Funciones `

# iniciar_juego()

Inicia el juego mostrando el menú principal donde el jugador puede seleccionar el nivel de dificultad: básico, medio o difícil. También proporciona opciones para salir del juego.

# mostrar_menu()

Dibuja el menú principal en la pantalla del juego. Este menú permite al jugador elegir el nivel de dificultad o salir del juego. Utiliza imágenes y sonidos para hacer la experiencia interactiva.

# generar_operacion(dificultad)

Genera una operación matemática basada en el nivel de dificultad. En el nivel básico, las operaciones incluyen solo sumas y restas, mientras que en niveles más altos incluyen multiplicaciones y divisiones.

# generar_opciones(correcta)

Crea tres opciones de respuesta, una de las cuales es la correcta, mientras que las otras dos son distractores. El jugador selecciona una opción para avanzar.

# `niveles(dificultad)`

Controla el flujo y la lógica del juego según el nivel de dificultad seleccionado. Llama a las funciones relevantes para iniciar y gestionar las rondas de preguntas matemáticas, el movimiento de los personajes y las condiciones de victoria o derrota. Utiliza la dificultad (básico, medio, difícil) para determinar qué tipo de operaciones matemáticas se presentan al jugador y cómo responde el enemigo.


# salir()
Cierra el juego de forma segura y libera todos los recursos utilizados, como imágenes y sonidos.


## Derechos de Autor

Este juego fue creado por Jeiber Javier Blanco Torres (Jeiber Dev). Todos los derechos reservados.
