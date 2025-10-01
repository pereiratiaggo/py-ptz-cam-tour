import os
import itertools
import time
from Camera import Camera

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv('.env')

ip = str(os.getenv('PTZ_CAM_IP', '127.0.0.1'))
port = int(os.getenv('PTZ_CAM_PORT', 80))
user = str(os.getenv('PTZ_CAM_USERNAME', 'username'))
password = str(os.getenv('PTZ_CAM_PASSWORD', 'password'))

timeout_global = int(os.getenv('PTZ_TIMEOUT_GLOBAL', 1800))
timeout_to_next_preset = int(os.getenv('PTZ_TIMEOUT_TO_NEXT_PRESET', 60))
timeout_to_first_exec = int(os.getenv('PTZ_TIMEOUT_TO_FIRST_EXEC', 300))

for seconds in range(timeout_to_first_exec, 0, -1):
    print(f"Aguardando {seconds}s antes do primeiro pre-set...", end='\r')
    time.sleep(1)
print("\n")

camera = Camera(ip, port, user, password)
p_len = len(camera.get_presets())
if p_len < 2:
    raise Exception(
        "Você precisa de pelo menos 2 presets configurados na câmera.")

print(f"Iniciando ciclo infinito entre presets...\n")
while True:
    counter = 1
    for preset in camera.presets:
        print(f"Counter: {counter} | p_len: {p_len}\n")
        print(f"Movendo para preset: {preset.Name}")
        camera.move_to_preset(preset)
        if(counter == p_len):
            print(f'Aguardando {timeout_global}s')
            time.sleep(timeout_global)
            counter = 1
        else:
            counter += 1
            print(f'Aguardando {timeout_to_next_preset}s')
            time.sleep(timeout_to_next_preset)