
# from django.shortcuts import render
# from Aplicacion import models
# import base64
# import io

# def test_view(request):
#     # Verifica si un filtro fue seleccionado
#     filter_name = request.GET.get('filter', None)

#     # aplica el filtro seleccionado
#     if filter_name == 'smooth':
#         output = models.suavizado1()
#     elif filter_name == 'reset':
#         output = models.default_image()
#     elif filter_name == 'ruido1':
#         output = models.ruido1()
#     elif filter_name == 'ruido2':
#         output = models.ruido2()
#     elif filter_name == 'ruido3':
#         output = models.ruido3()
#     elif filter_name == 'ruido4':
#         output = models.ruido4()
#     elif filter_name == 'ruido5':
#         output = models.ruido5()
#     elif filter_name == 'ruido6':
#         output = models.ruido6()
#     elif filter_name == 'ruido7':
#         output = models.ruido7()
#     elif filter_name == 'ruido8':
#         output = models.ruido8()
#     elif filter_name == 'ruido9':
#         output = models.ruido9()
#     else:
#         # Valor predeterminado al cargar la pagina
#         output = models.default_image()

#     buffer = io.BytesIO()
#     output.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()
#     graphic = base64.b64encode(image_png).decode('utf-8')

#     return render(request, 'index.html', {'graphic': graphic})

from django.shortcuts import render
from Aplicacion import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import base64
import io

@csrf_exempt
def processImage(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        filter_name = request.POST.get('filter') 
        image_path = default_storage.save('uploaded_images/' + uploaded_file.name, ContentFile(uploaded_file.read()))
        print(image_path)
        #Load image
        imagen = Image.open(image_path)
        image_array = np.array(imagen)
        print(image_array)
        # aplica el filtro seleccionado
        if filter_name == 'smooth':
            output = models.suavizado1(image_array)
        elif filter_name == 'reset':
            output = models.default_image(image_array)
        elif filter_name == 'ruido1':
            output = models.ruido1(image_array)
        elif filter_name == 'ruido2':
            output = models.ruido2(image_array)
        elif filter_name == 'ruido3':
            output = models.ruido3(image_array)
        elif filter_name == 'ruido4':
            output = models.ruido4(image_array)
        elif filter_name == 'ruido5':
            output = models.ruido5(image_array)
        elif filter_name == 'ruido6':
            output = models.ruido6(image_array)
        elif filter_name == 'ruido7':
            output = models.ruido7(image_array)
        elif filter_name == 'ruido8':
            output = models.ruido8(image_array)
        elif filter_name == 'ruido9':
            output = models.ruido9(image_array)
        else:
            # Valor predeterminado al cargar la pagina
            output = models.default_image(image_array)
        
        JsonResponse({'result': 'success'})
        buffer = io.BytesIO()
        output.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png).decode('utf-8')

        return render(request, 'index.html', {'graphic': graphic})

    return JsonResponse({'result': 'error', 'message': 'Invalid request method'})