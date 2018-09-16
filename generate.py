# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse, parseString
from certificate import Certificate

def load_svg(name=''):
    file_obj = open('certificate_dg.svg', 'r').read()
    doc = parseString(file_obj)  # parseString also exists
    for text in doc.getElementsByTagName('text'):
        id = text.getAttribute('id')
        if id == 'name':
            tspan = text.childNodes[0]
            tspan.childNodes[0].nodeValue = name

        print(text.toxml())

    return doc.toxml()

def load_settings():
    pass

def load_csv():
    import ipdb; ipdb.set_trace()
    lista = []
    with open('caxiasdosul2.csv', 'r') as file:
        for line in file:
            lista.append(line)

    return lista

def main():
    lista = load_csv()

    for cert in lista:
        svg = load_svg(cert)
        certificado = Certificate(svg)
        certificado.save()


main()
