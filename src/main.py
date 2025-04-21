#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo principal del proyecto IA Luis.
Este archivo sirve como punto de entrada para la aplicación.
"""

import argparse
import sys
import logging

# Configuración del registro de eventos
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='IA Luis - Herramienta de IA')
    parser.add_argument('--model', type=str, default='default',
                        help='Modelo a utilizar')
    parser.add_argument('--input', type=str, required=False,
                        help='Archivo de entrada para procesar')
    parser.add_argument('--output', type=str, default='output.txt',
                        help='Archivo de salida para guardar resultados')
    parser.add_argument('--verbose', action='store_true',
                        help='Modo verboso')
    
    return parser.parse_args()

def main():
    """Función principal."""
    args = parse_arguments()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug('Modo verboso activado')
    
    logger.info(f'Iniciando IA Luis con modelo: {args.model}')
    
    # Aquí iría la lógica principal del programa
    # ...
    
    logger.info(f'Procesamiento completado. Resultados guardados en {args.output}')
    
    return 0

if __name__ == '__main__':
    sys.exit(main())