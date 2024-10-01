import pygame
import sys
import random

# Inicializar Pygame
pygame.init()
pygame.mixer.init()  # Inicializar el mixer de Pygame para manejar el sonido

# Cargar el sonido
sonido_seleccion = pygame.mixer.Sound("sonido_boton.wav")  # Asegúrate de que el archivo esté en el mismo directorio
sonido_felicitaciones = pygame.mixer.Sound("felicitaciones_sonido.wav")
sonido_perdedor = pygame.mixer.Sound("perdedor_sonido.wav")
# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
GRIS_CLARO = (200, 200, 200)
FUCIA = (255, 0, 255)

# Configurar seleccion nivel
seleccion_nivel = 0

# Configurar pantalla
ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))

# Título del juego
pygame.display.set_caption("Corredor Aritmético")

# Cargar la imagen de fondo
fondo_img = pygame.image.load("fondo.png")  # Asegúrate de que el archivo esté en el mismo directorio
fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))  # Ajustar el tamaño de la imagen al tamaño de la ventana

# Configurar fuente
fuente = pygame.font.Font(None, 74)
fuente_pequena = pygame.font.Font(None, 40)

# Definir posiciones iniciales
jugador_inicial_x = 50  # Posición inicial del jugador en el eje X
jugador_pos_y = ALTO // 2  # Centrado verticalmente
enemigo_inicial_x = 50  # Posición inicial del enemigo
enemigo_pos_y = ALTO // 2 + 100  # Debajo del jugador

# Cargar imágenes del jugador y el enemigo
jugador_img = pygame.image.load("jugador.png")
enemigo_img = pygame.image.load("enemigo.png")
meta_img = pygame.image.load("meta.png")
pista_img = pygame.image.load("pista.png")

# Cargar la imagen de felicitación
felicitacion_img = pygame.image.load("felicitaciones.png")
felicitacion_img = pygame.transform.scale(felicitacion_img, (400, 200))  # Ajustar al tamaño de la subventana

# Cargar la imagen de perdedor
perdedor_img = pygame.image.load("perdedor.png")
perdedor_img = pygame.transform.scale(perdedor_img, (400, 200))  # Ajustar al tamaño de la subventana


# Mensaje de felicitaciones o sigue intente 
mensaje_final_juego = ""

# Escalar las imágenes (si es necesario)
jugador_img = pygame.transform.scale(jugador_img, (80, 80))  
enemigo_img = pygame.transform.scale(enemigo_img, (80, 80))
meta_img = pygame.transform.scale(meta_img, (80, 80))
pista_img = pygame.transform.scale(pista_img, (500 , 40))

# Función para generar una operación aleatoria (suma o resta)
def generar_operacion():
    operador = random.choice(['+', '-'])
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    if operador == '-':  # Evitar resultados negativos
        num1, num2 = max(num1, num2), min(num1, num2)
    
    operacion = f"{num1} {operador} {num2}"
    resultado_correcto = eval(operacion)
    return operacion, resultado_correcto


# Función para generar una operación aleatoria (suma, resta o multiplicación)
def generar_operacion_medio():
    operador = random.choice(['+', '-', '*'])  
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)

    if operador == '-':  # Evitar resultados negativos
        num1, num2 = max(num1, num2), min(num1, num2)

    operacion = f"{num1} {operador} {num2}"
    resultado_correcto = eval(operacion)
    return operacion, resultado_correcto

# Función para generar una operación aleatoria (suma, resta, multiplicación o división)
def generar_operacion_dificil():
    operador = random.choice(['+', '-', '*', '/'])  
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)

    if operador == '-':  # Evitar resultados negativos
        num1, num2 = max(num1, num2), min(num1, num2)
    elif operador == '/':  
        num1 = num1 * num2  # Esto garantiza que el resultado sea un entero
     
    operacion = f"{num1} {operador} {num2}"
    resultado_correcto = int(eval(operacion))
    return operacion, resultado_correcto

# Función para generar opciones de respuesta
def generar_opciones(resultado_correcto):
    opciones = [resultado_correcto]
    while len(opciones) < 3:
        opcion = random.randint(resultado_correcto - 20, resultado_correcto + 20)
        if opcion != resultado_correcto and opcion not in opciones:
            opciones.append(opcion)
    random.shuffle(opciones)
    return opciones

# Función para dibujar un botón con texto, y devolver el rectángulo
def dibujar_boton(texto, fuente, color_fondo, x, y, ancho, alto, color_texto=NEGRO):
    rect = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(screen, color_fondo, rect)  # Dibujar rectángulo del botón
    texto_superficie = fuente.render(texto, True, color_texto)
    texto_rect = texto_superficie.get_rect(center=(x + ancho // 2, y + alto // 2))
    screen.blit(texto_superficie, texto_rect)
    return rect

def mostrar_ventana_felicidades(seleccion_nivel,ganador_perdedor):
    ventana_abierta = True

    if ganador_perdedor == 1:
        mensaje_final_juego = "¡Felicidades, llegaste a la meta!"
        imagen_msj = felicitacion_img
        sonido_felicitaciones.play()
    else:
        mensaje_final_juego = "Perdiste, el enemigo llegó primero."
        imagen_msj = perdedor_img
        sonido_perdedor.play()
    
    while ventana_abierta:
        # Dibujar la imagen de felicitación como fondo
        screen.blit(imagen_msj, (ANCHO // 2 - 200, ALTO // 2 - 100))

        # Dibujar el mensaje de felicitación (opcional, si quieres sobreponer texto sobre la imagen)
        mensaje = fuente_pequena.render(mensaje_final_juego, True, FUCIA)
        mensaje_rect = mensaje.get_rect(center=(ANCHO // 2, ALTO // 2 - 50))
        screen.blit(mensaje, mensaje_rect)

        # Dibujar el botón de "Reintentar"
        boton_reintentar = dibujar_boton("Reintentar", fuente_pequena, VERDE, ANCHO // 2 - 100, ALTO // 2 + 20, 200, 50)

        # Obtener la posición del mouse
        mouse_pos = pygame.mouse.get_pos()

        # Verificar si se ha hecho clic en el botón de reintentar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_reintentar.collidepoint(mouse_pos):
                    ventana_abierta = False  # Cierra la subventana
                    niveles(seleccion_nivel)  # Reinicia el nivel

        pygame.display.flip()


# Función para manejar los niveles
def niveles(seleccion_nivel):
    global jugador_pos_x, enemigo_pos_x
    # Restablecer posiciones al inicio del nivel
    jugador_pos_x = jugador_inicial_x
    enemigo_pos_x = enemigo_inicial_x
    meta_pos_x = 550
    if seleccion_nivel == 1:
        operacion, resultado_correcto = generar_operacion()  
        opciones = generar_opciones(resultado_correcto) 
    elif seleccion_nivel == 2:
        operacion, resultado_correcto = generar_operacion_medio()  
        opciones = generar_opciones(resultado_correcto) 
    else:
        operacion, resultado_correcto = generar_operacion_dificil()  
        opciones = generar_opciones(resultado_correcto) 

    while True:
        screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
        # Dibujar el jugador y el enemigo en sus posiciones actuales
        screen.blit(pista_img, (jugador_inicial_x, jugador_pos_y + 45))
        screen.blit(meta_img, (meta_pos_x, jugador_pos_y))
        screen.blit(jugador_img, (jugador_pos_x, jugador_pos_y))
        screen.blit(pista_img, (jugador_inicial_x, enemigo_pos_y + 45))
        screen.blit(meta_img, (meta_pos_x, enemigo_pos_y))
        screen.blit(enemigo_img, (enemigo_pos_x, enemigo_pos_y))
        
        # Dibujar el texto "Selecciona tu respuesta"
        texto_seleccion = fuente_pequena.render("Selecciona tu respuesta", True, BLANCO)
        texto_rect = texto_seleccion.get_rect(center=(ANCHO // 2, ALTO // 3 - 100))  # Ajustar posición vertical
        screen.blit(texto_seleccion, texto_rect)

        # Dibujar el texto "Jugador 1"
        texto_seleccion = fuente_pequena.render("Jugador 1", True, NEGRO)
        texto_rect = texto_seleccion.get_rect(center=(jugador_inicial_x +70, jugador_pos_y))  # Ajustar posición vertical
        screen.blit(texto_seleccion, texto_rect)

        # Dibujar el texto "Jugador 2"
        texto_seleccion = fuente_pequena.render("Jugador 2", True, NEGRO)
        texto_rect = texto_seleccion.get_rect(center=(enemigo_inicial_x + 70, enemigo_pos_y))  # Ajustar posición vertical
        screen.blit(texto_seleccion, texto_rect)

        # Dibujar la operación matemática
        dibujar_boton(f"{operacion} =", fuente_pequena, FUCIA, ANCHO // 2 - 100, ALTO // 3 - 50, 200, 50, NEGRO)
        
        # Obtener posición del mouse
        mouse_pos = pygame.mouse.get_pos()

        # Dibujar las opciones de respuesta en horizontal y detectar si el mouse está sobre alguna
        color_opcion1 = VERDE if pygame.Rect(ANCHO // 4 - 75, ALTO // 2 - 95, 150, 75).collidepoint(mouse_pos) else GRIS_CLARO
        color_opcion2 = VERDE if pygame.Rect(ANCHO // 2 - 75, ALTO // 2 - 95, 150, 75).collidepoint(mouse_pos) else GRIS_CLARO
        color_opcion3 = VERDE if pygame.Rect((ANCHO // 4) * 3 - 75, ALTO // 2 - 95, 150, 75).collidepoint(mouse_pos) else GRIS_CLARO

        rect_opcion1 = dibujar_boton(str(opciones[0]), fuente_pequena, color_opcion1, ANCHO // 4 - 75, ALTO // 2 - 95, 150, 75)
        rect_opcion2 = dibujar_boton(str(opciones[1]), fuente_pequena, color_opcion2, ANCHO // 2 - 75, ALTO // 2 - 95, 150, 75)
        rect_opcion3 = dibujar_boton(str(opciones[2]), fuente_pequena, color_opcion3, (ANCHO // 4) * 3 - 75, ALTO // 2 - 95, 150, 75)

        # Dibujar el botón "Atrás"
        color_boton_atras = VERDE if pygame.Rect(ANCHO - 150, ALTO - 100, 100, 50).collidepoint(mouse_pos) else GRIS_CLARO
        boton_atras = dibujar_boton("Atrás", fuente_pequena, color_boton_atras, ANCHO - 150, ALTO - 100, 100, 50)

        # Revisar eventos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar cuál opción fue seleccionada
                if rect_opcion1.collidepoint(mouse_pos):
                    sonido_seleccion.play()  # Reproducir sonido
                    if opciones[0] == resultado_correcto:
                        jugador_pos_x += 50  # Mover al jugador a la derecha
                    else:
                        enemigo_pos_x += 50  # Mover al enemigo a la derecha
                elif rect_opcion2.collidepoint(mouse_pos):
                    sonido_seleccion.play()  # Reproducir sonido
                    if opciones[1] == resultado_correcto:
                        jugador_pos_x += 50  # Mover al jugador a la derecha
                    else:
                        enemigo_pos_x += 50  # Mover al enemigo a la derecha
                elif rect_opcion3.collidepoint(mouse_pos):
                    sonido_seleccion.play()  # Reproducir sonido
                    if opciones[2] == resultado_correcto:
                        jugador_pos_x += 50  # Mover al jugador a la derecha
                    else:
                        enemigo_pos_x += 50  # Mover al enemigo a la derecha
                
                
                if seleccion_nivel == 1:
                    operacion, resultado_correcto = generar_operacion()  
                    opciones = generar_opciones(resultado_correcto) 
                elif seleccion_nivel == 2:
                    operacion, resultado_correcto = generar_operacion_medio()  
                    opciones = generar_opciones(resultado_correcto) 
                elif seleccion_nivel == 3:
                    operacion, resultado_correcto = generar_operacion_dificil()  
                    opciones = generar_opciones(resultado_correcto) 
                
                if jugador_pos_x == 550:
                    mostrar_ventana_felicidades(seleccion_nivel,1)  # Mostrar la subventana cuando el jugador llega a la meta
                    return
                elif enemigo_pos_x == 550:
                    mostrar_ventana_felicidades(seleccion_nivel,2)  # Mostrar la subventana cuando el jugador llega a la meta
                    return
                
                # Si se presiona el botón "Atrás", regresar al menú principal
                if boton_atras.collidepoint(mouse_pos):
                    sonido_seleccion.play()  # Reproducir sonido
                    return  # Esto terminará el nivel y volverá al menú principal
            
        pygame.display.flip()


# Función para mostrar el menú principal
def menu_principal():
    while True:
        
        screen.blit(fondo_img, (0, 0))  # Dibujar el fondo
        titulo = fuente.render("Corredor Aritmético", True, NEGRO)
        titulo_rect = titulo.get_rect(center=(ANCHO // 2, ALTO // 2 - 150))
        screen.blit(titulo, titulo_rect)

        # Obtener posición del mouse
        mouse_pos = pygame.mouse.get_pos()

        # Botones del menú
        color_boton_basico = VERDE if pygame.Rect(ANCHO // 2 - 100, 200, 200, 75).collidepoint(mouse_pos) else GRIS_CLARO
        color_boton_medio = VERDE if pygame.Rect(ANCHO // 2 - 100, 300, 200, 75).collidepoint(mouse_pos) else GRIS_CLARO
        color_boton_dificil = VERDE if pygame.Rect(ANCHO // 2 - 100, 400, 200, 75).collidepoint(mouse_pos) else GRIS_CLARO
        color_boton_salir = VERDE if pygame.Rect(ANCHO // 2 - 75, 500, 150, 75).collidepoint(mouse_pos) else GRIS_CLARO

        boton_basico = dibujar_boton("Nivel Básico", fuente_pequena, color_boton_basico, ANCHO // 2 - 100, 200, 200, 75)
        boton_medio = dibujar_boton("Nivel Medio", fuente_pequena, color_boton_medio, ANCHO // 2 - 100, 300, 200, 75)
        boton_dificil = dibujar_boton("Nivel Difícil", fuente_pequena, color_boton_dificil, ANCHO // 2 - 100, 400, 200, 75)
        boton_salir = dibujar_boton("Salir", fuente_pequena, color_boton_salir, ANCHO // 2 - 75, 500, 150, 75)

        # Revisar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_basico.collidepoint(mouse_pos):
                    sonido_seleccion.play()  # Reproducir sonido al seleccionar
                    niveles(seleccion_nivel = 1)  # Entrar al nivel básico

                elif boton_medio.collidepoint(mouse_pos):
                    sonido_seleccion.play()  # Reproducir sonido
                    niveles(seleccion_nivel = 2)

                elif boton_dificil.collidepoint(mouse_pos):
                    sonido_seleccion.play()  # Reproducir sonido
                    niveles(seleccion_nivel = 3)
                
                elif boton_salir.collidepoint(mouse_pos):
                    sonido_seleccion.play()  # Reproducir sonido
                    # Pausar por 0.2 segundos
                    pygame.time.delay(200)
                    pygame.quit()  # Cerrar el juego
                    sys.exit()
                
            
        pygame.display.flip()

# Iniciar el juego en el menú principal
menu_principal()


print(type(42.0))
x = 2.5e6
print(x)

for i in range(1, 5): 
    print(i, "multiplicado por 8 =", i * 8)