from django.shortcuts import render, HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
import os

def convertemp(mm):
    """
    Converte milimetros em pontos - Criação de Relatórios

    :param mm: milimetros
    :return: pontos
    """
    return mm / 0.352777


def index(request):
    print(request.POST)
    return render(request, 'catalogo/index.html')


def mostra_fotos(request):
    pasta = 'C:\Catalogo\A03'
    caminho = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    catalogo = []
    for itens in caminho:
        catalogo.append(itens)


    response = HttpResponse(content_type='application/pdf')
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    coluna = 5
    linha = 260
    foto = 0
    for index, itens in enumerate(catalogo):
        print(index)
        lista_separada=itens.split('\\')
        nome_arquivo = lista_separada[-1].split('.')
        foto += 1
        pdf.drawImage(itens, convertemp(coluna), convertemp(linha), convertemp(50), convertemp(35),
                      preserveAspectRatio=False, anchor='n')
        # pdf.roundRect(convertemp(coluna), convertemp(linha+5), convertemp(50), convertemp(35), 5)
        pdf.setFont("Times-Roman", 9)
        pdf.drawCentredString(convertemp(coluna+25), convertemp(linha-5), nome_arquivo[0])
        coluna += 50
        if foto % 4 == 0:
            coluna = 5
            linha -= 41.5
        if foto == 28:
            foto = 0
            linha = 260
            pdf.showPage()


    pdf.setTitle('Catalogo.pdf')
    pdf.save()
    buffer.seek(0)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response



    return render(request, 'catalogo/catalogo.html', {'catalogo': catalogo})
