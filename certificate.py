# -*- coding: UTF-8 -*-
from convert import convert_to_pdf

class Certificate():
    xml = ''
    name_svg = ''
    name_pdf = ''

    def __init__(self, xml='', name=''):
        self.xml = xml
        self.name_svg = name + '.svg'
        self.name_pdf = name + '.pdf'

    def generate_certificado():
        pass

    def find_text():
        pass

    def replace_color():
        pass

    def replace_logo():
        pass

    def save(self):
        file_obj = open(self.name_svg, 'w')
        file_obj.write(self.xml)
        file_obj.close()
        convert_to_pdf(self.name_svg, self.name_pdf)
