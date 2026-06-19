from bs4 import BeautifulSoup
import requests
import time

def csv_creator(links_meses, ano):
    ids_categorias = [('osversion_details', 'OS Version'), ('cat0_details', 'System RAM'), ('cat1_details', 'Intel CPU Speeds'), ('cat2_details', 'Physical CPUs'), ('cat3_details', 'Video Card Description'), ('cat4_details', 'VRAM'), ('cat5_details', 'Primary Display Resolution'), ('cat6_details', 'Multi-Monitor Desktop Resolution')]

    with open(f'dados_{ano}.csv', 'w', encoding='utf-8') as f:
                f.write('Categoria, Especificação, Porcentagens, Incrementos/Decrementos, Mês, Ano\n')

    for link, mes in links_meses:
        time.sleep(3)
        html = requests.get(link).text
        soup = BeautifulSoup(html, 'html.parser')

        for id_, categoria in ids_categorias:
            # Pega apenas a div do id especificado (Os ids tem que ser os details para funcionar)
            div = soup.find('div', id=f'{id_}')

            titulos = div.find_all('div', class_='stats_col_mid')
            porcentagens = div.find_all('div', class_='stats_col_right')
            incs_decs = div.find_all('div', class_='stats_col_right2')

            with open(f'dados_{ano}.csv', 'a+', encoding='utf-8') as f:
                for titulo, porcentagem, inc_dec in zip(titulos, porcentagens, incs_decs):
                    f.write(f"{categoria}, {titulo.text.strip()}, {porcentagem.text.strip()}, {inc_dec.text.strip()}, {mes}, {ano}\n")