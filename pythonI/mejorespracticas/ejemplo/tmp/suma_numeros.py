"""
SYNOPSIS
    python <suma_numeros.py> -inputfile <file>

DESCRIPTION
    Un script que calcula la suma de todos los números de un archivo.
    El archivo debe tener un número por línea. 

OPTIONS
    -inputfile
        La ruta al archivo que contiene los números que se sumarán.

EXAMPLES
    Ejemplo de uso:
        python suma_numeros.py -inputfile numbers.txt
"""

import os
import argparse

def get_file_data(file_path):
    """Lee los datos del archivo.

    Args:
        file_path (str): La ruta al archivo.

    Raises:
        FileNotFoundError: Si el archivo no existe.

    Returns:
        list: Lista con una línea por elemento.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("¡Error! Archivo no encontrado")

    with open(file_path, 'r') as file:
        return file.readlines()

def validate_data(data):
    """Valida que los datos sean números.

    Args:
        data (list): Los datos a validar.

    Raises:
        ValueError: Si los datos no son números en base 10.

    Returns:
        list: Lista de números.
    """
    try:
        return [float(num.strip()) for num in data]
    except ValueError:
        raise ValueError("¡Error! Introducir números de base 10")

def calculate_sum(numbers):
    """Suma una lista de números.

    Args:
        numbers (list): Lista de números a sumar.

    Returns:
        float: La suma de los números.
    """
    return sum(numbers)

def print_result(numbers, result):
    """Imprime los resultados con el formato especificado.

    Args:
        numbers (list): Los números que se sumaron.
        result (float): El resultado de la suma.
    """
    print(" + ".join([str(num) for num in numbers]) + " = " + str(result))

def sum_numbers(file_path):
    """Función principal que suma números de un archivo.

    Args:
        file_path (str): La ruta al archivo.
    """
    try:
        file_data = get_file_data(file_path)
        numbers = validate_data(file_data)
        result = calculate_sum(numbers)
        print_result(numbers, result)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calcula la suma de números de un archivo.')
    parser.add_argument('-inputfile', dest='inputfile', required=True, help='Ruta del archivo que contiene los números.')
    args = parser.parse_args()

    sum_numbers(args.inputfile)