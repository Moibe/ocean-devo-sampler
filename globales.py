import gradio as gr

version = "3.1.2"
env = "dev"
aplicacion = "sampler-dev"

seleccion_api = "eligeAOB" #eligeGratisOCosto , eligeAOB o eligeGratisOCosto
max_size = 20
#Quota o Costo
api_zero = ("Moibe/image-blend", "gratis")
api_cost = ("Moibe/image-blend", "costo")
#A o B
api_a = ("Moibe/sampler", "gratis") #Para music-sampler en particular aquí la diferencia será el formato: mp3
api_b = ("Moibe/music-separation", "gratis") #wav
#Gratis o Costo
api_gratis = ("Moibe/image-blend", "gratis")
api_costo = ("Moibe/image-blend", "costo")
process_cost = 0

seto = "sampler"
work = "picswap"
app_path = "/sampler-dev"
server_port=7810
#tema = tools.theme_selector()
tema = gr.themes.Default()
flag = "auto"