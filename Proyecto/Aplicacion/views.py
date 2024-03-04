# 
# This Works
# from django.shortcuts import render
# from django.http import HttpResponse
# from Aplicacion import models
# from django.template import loader
# import base64
# import io

from django.shortcuts import render
from Aplicacion import models
import base64
import io

def test_view(request):
    output = models.testMethodFromModelPY()
    
    
    buffer = io.BytesIO()
    output.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'index.html', {'graphic': graphic})






# def test_view(request):
#     output = models.testMethodFromModelPY()
#     return HttpResponse(output)


# def test_view(request):

#     # inputImage is the name attribute of the <input> tag in the html
#     inImg = request.FILES["inputImage"].read()

#     encoded = base64.b64encode(inImg).decode('ascii')
#     mime = "image/jpg"
#     mime = mime + ";" if mime else ";"
#     input_image = "data:%sbase64,%s" % (mime, encoded)        

#     return render(request, "../templates/index.html", {{ "input_image": input }})