from flask import Flask, request, jsonify
from PIL import Image
import io
import numpy as np
import base64


# Importar el modelo
from yolo_flavor import YoloModel

# Crear el modelo
app = Flask(__name__)
model = YoloModel(name='epoch_100', version='best', online=False, device='cpu')


@app.route('/yolo_predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Obtener la imagen
        image = request.files['image']
        # Convertir la imagen a un array de numpy
        file = request.files['image']
        image = Image.open(io.BytesIO(file.read()))
        # Hacer la predicción
        results, image_scored = model.score_frame(image)
        # Preparar imagen para enviar
        image_pil = Image.fromarray(image_scored[0])

        # Convertir la imagen PIL a una cadena de texto codificada en base64
        buffer = io.BytesIO()
        image_pil.save(buffer, format='PNG')
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')


        # Crear la respuesta
        response = jsonify({'results': results[0], 'image_scored': image_base64})

        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)