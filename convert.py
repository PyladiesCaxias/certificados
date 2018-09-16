import cairosvg

def convert_to_pdf(file, file_name='new_pdf.pdf'):
    """
    """
    cairosvg.svg2pdf(
        file_obj=open(file, "rb"), write_to=file_name)

def convert_to_png(file, file_name='new_pdf.pdf'):
    """
    """
    cairosvg.svg2png(
        url=file, write_to=file_name)
