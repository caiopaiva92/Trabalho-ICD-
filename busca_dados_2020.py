from bs4 import BeautifulSoup
import requests

html = requests.get('https://web.archive.org/web/20200202095248/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam').text
soup = BeautifulSoup(html, 'html.parser')

# Pega apenas a div da seção dos sistemas operacionais (cada seção tem seu id específico)
# Os ids tem que ser os details para funcionar, só trocar o id para a que você quer
div_os = soup.find('div', id='osversion_details')

titulos = div_os.find_all('div', class_='stats_col_mid')
porcentagens = div_os.find_all('div', class_='stats_col_right')
incs_decs = div_os.find_all('div', class_='stats_col_right2')

for titulo, porcentagem, inc_dec in zip(titulos, porcentagens, incs_decs):
    if titulo.text:
        print(f"{titulo.text}, {porcentagem.text}, {inc_dec.text}")