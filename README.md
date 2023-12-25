# Uso de C en Python

Lo siguiente es un ejemplo de cómo podemos utilizar C en python para el desempeño de un código.

## Requerimientos

Para el desarrollo de este ejemplo se utilizó una máquina virtual de linux en windows, para la cual fue necesario instalar lo siguiente:

- Python:
```bash
sudo apt-get install python3
```
- Pip:
```bash
sudo apt-get install python3-pip
```
- Compilador de C:
```bash
sudo apt-get install gcc
```

Para comparar también utilizamos numpy:
```bash
pip3 install numpy
```

## Ejecución

Podemos compilar el código C para luego poder importarlo de la siguiente forma:

```bash
gcc -shared -fPIC -o libmodulo.so modulo.c
```

## Resultados

```bash
python3 main.py
Time for C: 0.4412848949432373
Time for numpy: 0.49985694885253906
```