import cv2
import keyboard
import pyautogui
import numpy as np


# Qtde de frames por segundos
fps = 30

# Configuração para capturar as dimensões da tela
screen_width, screen_height = pyautogui.size()

# Codec permite compactar e renderizar videos digitalmente
codec = cv2.VideoWriter_fourcc(*"XVID")

# Formato de saída do vídeo
video = cv2.VideoWriter('video.avi', codec, fps, (screen_width, screen_height))

while True:
    # Captura de tela usando pyautogui
    img = pyautogui.screenshot()
    
    # Conversão da captura de tela para um array numpy e em seguida para um array OpenCV
    frame = np.array(img)

    # Convertendo o padrão do opencv BGR e transforma em RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Gravação do frame no vídeo
    video.write(frame)

    # Condição de saída, por exemplo, pressionar a tecla 'q' para encerrar a gravação
    if keyboard.is_pressed("esc"):
        break

# Liberando recursos
video.release()
cv2.destroyAllWindows()
