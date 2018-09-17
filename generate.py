# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse, parseString
from certificate import Certificate
from app import Configuracao
import os

def load_svg(file_name='svg/certificate_dg.svg'):
    file_obj = open(file_name, 'r').read()
    doc = parseString(file_obj)  # parseString also exists
    return doc

def load_settings():
    pass

def load_csv(file_name='caxiasdosul2.csv'):
    lista = []
    with open(file_name, 'r') as file:
        for line in file:
            lista.append(line)

    return lista

def main():
    lista = load_csv()
    config = Configuracao("files_svg", "files_pdf")
    config.generate_dir()
    for cert in lista:
        svg = load_svg()
        certificado = Certificate(name=cert, app=config, xml_dom=svg)
        certificado.save_pdf()
    print(len(lista), " - Certificados gerados")


main()
