import mss
import mss.tools

with mss.mss() as sct:
    # Captura toda a tela
    sct.shot(output="screenshot.png")

    # Ou, para capturar uma parte específica da tela
    monitor = sct.monitors[1]  # Altere o índice conforme necessário
    region = {'left': monitor['left'], 'top': monitor['top'], 'width': 800, 'height': 600}
    sct_img = sct.grab(region)
    mss.tools.to_png(sct_img.rgb, sct_img.size, output="screenshot_part.png")
