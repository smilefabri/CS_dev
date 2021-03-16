from tqdm import tqdm
import time

"""
    install : pip install tqdm

    description: serve per creare una barra di caricamento "bar progress"

    link: https://github.com/tqdm/tqdm

"""

for i in tqdm(range(10)):
    time.sleep(0.2)