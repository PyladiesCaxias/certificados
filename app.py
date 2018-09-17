# -*- coding: UTF-8 -*-

import os
from xml.dom.minidom import parse, parseString


class Configuracao():
    folder_svg = ''
    folder_pdf = ''
    base_svg = ''
    xml_dom = ''
    list_csv = ''
    color = ''
    logo = ''
    signature_path = ''
    signature_name = ''
    signature_description = ''
    time = ''
    date_event = ''

    def __init__(self, folder_svg='', folder_pdf="", base_svg="", list_csv="",
            color="", logo="", signature_path="", signature_name="",
            signature_description="", time="", date_event=""):

        self.folder_pdf = folder_pdf
        self.folder_svg = folder_svg
        self.base_svg = base_svg
        self.list_csv = list_csv
        self.color = color
        self.logo = logo
        self.signature_path = signature_path
        self.signature_name = signature_name
        self.signature_description = signature_description
        self.time = time
        self.date_event = date_event
        self.xml_dom = None

    def replace_logo(self):
        for text in self.xml_dom.getElementsByTagName('text'):
            id = text.getAttribute('id')
            if id == 'name':
                tspan = text.childNodes[0]
                if len(self.name) < 16:
                    x = float(tspan.getAttribute('x'))
                    x += 50
                    tspan.setAttribute('x', str(x))
                tspan.childNodes[0].nodeValue = self.name

        self.xml = self.xml_dom.toxml()

    def replace_color(self):
        for text in self.xml_dom.getElementsByTagName('text'):
            id = text.getAttribute('id')
            if id == 'name':
                tspan = text.childNodes[0]
                if len(self.name) < 16:
                    x = float(tspan.getAttribute('x'))
                    x += 50
                    tspan.setAttribute('x', str(x))
                tspan.childNodes[0].nodeValue = self.name

        self.xml = self.xml_dom.toxml()

    def replace_signature_path(self):
        for text in self.xml_dom.getElementsByTagName('text'):
            id = text.getAttribute('id')
            if id == 'name':
                tspan = text.childNodes[0]
                if len(self.name) < 16:
                    x = float(tspan.getAttribute('x'))
                    x += 50
                    tspan.setAttribute('x', str(x))
                tspan.childNodes[0].nodeValue = self.name

        self.xml = self.xml_dom.toxml()

    def generate_dir(self):
        try:
            os.mkdir(self.folder_pdf)
            os.mkdir(self.folder_svg)
        except:
            print("Diretórios já criados")

    def load_svg(self):
        doc = None
        try:
            file_obj = open(self.base_svg, 'r').read()
            doc = parseString(file_obj)  # parseString also exists
            self.xml_dom = doc
            if self.color:
                pass
            if self.logo:
                pass
            if self.signature_path:
                pass
            if self.signature_name:
                pass
            if self.signature_description:
                pass
            if self.time:
                pass
            if self.date_event:
                pass
            print("Load Svg")
        except:
            print("Failed load svg")

    def load_csv(self):
        lista = []
        try:
            with open(self.list_csv, 'r') as file:
                for line in file:
                    lista.append(line)
            print("Load Lista csv")
        except:
            print("Failed load csv")
        return lista
