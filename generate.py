# -*- coding: UTF-8 -*-

from certificate import Certificate
from app import Configuracao
import os
import json


def load_settings(file='settings.json'):
    with open(file) as f:
        data = json.load(f)
    return data

def main():
    app = load_settings()
    config = Configuracao(
        folder_svg=app['folder_svg'],
        folder_pdf=app['folder_pdf'],
        base_svg=app['base_svg'],
        list_csv=app['list_csv'],
        color=app['color'],
        logo=app['logo'],
        signature_path=app['signature_path'],
        signature_name=app['signature_name'],
        signature_description=app['signature_description'],
        time=app['time'],
        date_event=app['date_event']
    )
    config.load_svg()  # Load file svg and create xml.dom element 
    lista = config.load_csv()
    config.generate_dir()  # Cria pastas

    for cert in lista:
        certificado = Certificate(name=cert, app=config, xml_dom=config.xml_dom)
        certificado.save_pdf()
    print(len(lista), " - Certificados gerados")


main()
