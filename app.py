# -*- coding: UTF-8 -*-

import os

class Configuracao():
    folder_svg = ''
    img = ''
    folder_pdf = ''

    def __init__(self, folder_svg='', folder_pdf=""):
        self.folder_pdf = folder_pdf
        self.folder_svg = folder_svg

    def generate_dir(self):
        try:
            os.mkdir(self.folder_pdf)
            os.mkdir(self.folder_svg)
        except:
            print("Diretórios já criados")
