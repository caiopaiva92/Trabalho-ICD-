from csv_creator import csv_creator

# Exemplo pegando apenas os sistemas operacionais de janeiro de 2020
link = 'https://web.archive.org/web/20200202095248/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam'
id = 'osversion_details'
csv_creator(link, id, "Janeiro", 2020)