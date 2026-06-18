from bs4 import BeautifulSoup
import requests

def csv_creator(link, id_, mes, ano):
    html = requests.get(link).text
    soup = BeautifulSoup(html, 'html.parser')

    # Pega apenas a div do id especificado (Os ids tem que ser os details para funcionar)
    div = soup.find('div', id=f'{id_}')

    titulos = div.find_all('div', class_='stats_col_mid')
    porcentagens = div.find_all('div', class_='stats_col_right')
    incs_decs = div.find_all('div', class_='stats_col_right2')

    with open(f'dados_{ano}.csv', 'a+', encoding='utf-8') as f:
        f.write('Título, Porcentagens, Incrementos/Decrementos, Mês, Ano\n')
        for titulo, porcentagem, inc_dec in zip(titulos, porcentagens, incs_decs):
            f.write(f"{titulo.text.strip()}, {porcentagem.text.strip()}, {inc_dec.text.strip()}, {mes}, {ano}\n")