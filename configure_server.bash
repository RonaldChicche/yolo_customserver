#!/bin/bash

# Actualizar la lista de paquetes
echo "Actualizando la lista de paquetes..."
sudo apt-get update

# Instalar libGL.so.1 para ambos, sistemas de 32 bits y 64 bits
echo "Instalando libGL.so.1..."
sudo apt-get install -y libgl1-mesa-glx

echo "La instalación de libGL.so.1 se completó con éxito."

# go to the home directory
cd ~

# gitclone the darknet repository
echo "Clonando el repositorio de darknet..."
git clone https://github.com/ultralytics/yolov5.git