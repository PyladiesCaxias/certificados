# -*- coding: UTF-8 -*-
from convert import convert_to_pdf

class Certificate():
    xml = ''
    xml_dom = ''
    name_svg = ''
    name_pdf = ''
    name = ''
    app = None

    def __init__(self, name='', app=None, xml_dom=''):
        self.xml_dom = xml_dom
        if xml_dom:
            self.xml = xml_dom.toxml()
        self.name = name
        self.name_svg = name + '.svg'
        self.name_pdf = name + '.pdf'
        self.app = app

    def replace_text_name(self):
        for text in self.xml_dom.getElementsByTagName('text'):
            id = text.getAttribute('id')
            if id == 'name':
                tspan = text.childNodes[0]
                if len(self.name) < 16:
                    x = float(tspan.getAttribute('x'))
                    x += 50
                    print(x)
                    tspan.setAttribute('x', str(x))
                tspan.childNodes[0].nodeValue = self.name

        self.xml = self.xml_dom.toxml()

    def replace_color():
        pass

    def replace_logo():
        pass

    def save_pdf(self):
        self.replace_text_name()
        try:
            if self.app.folder_svg and self.app.folder_pdf:
                path_svg = self.app.folder_svg + '/' + self.name_svg
                path_pdf = self.app.folder_pdf + '/' + self.name_pdf

                file_obj = open(path_svg, 'w')
                file_obj.write(self.xml)
                file_obj.close()
                convert_to_pdf(path_svg, path_pdf)
            else:
                file_obj = open(self.name_svg, 'w')
                file_obj.write(self.xml)
                file_obj.close()
                convert_to_pdf(self.name_svg, self.name_pdf)
            print("Gerado certificado para ", self.name)
        except:
            print("Problemas ao gerar o pdf")
