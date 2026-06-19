from csv_creator import csv_creator

# Exemplo pegando apenas os dados de 2020
link_mes = [('https://web.archive.org/web/20200202095248/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Janeiro'), 
           ('https://web.archive.org/web/20200316152704/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Fevereiro'), 
           ('https://web.archive.org/web/20200407072208/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Março'), 
           ('https://web.archive.org/web/20200505150638/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Abril'), 
           ('https://web.archive.org/web/20200608014405/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Maio'), 
           ('https://web.archive.org/web/20200808140607/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Julho'), 
           ('https://web.archive.org/web/20200908144606/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Agosto'), 
           ('https://web.archive.org/web/20201009143637/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Setembro'), 
           ('https://web.archive.org/web/20201104192639/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Outubro'), 
           ('https://web.archive.org/web/20201209234627/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Novembro'), 
           ('https://web.archive.org/web/20210105073410/https://store.steampowered.com/hwsurvey/Steam-Hardware-Software-Survey-Welcome-to-Steam', 'Dezembro')]

csv_creator(link_mes, 2020)