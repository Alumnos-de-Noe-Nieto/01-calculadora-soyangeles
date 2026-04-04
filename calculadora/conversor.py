"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""

from calculadora.error import ExpresionInvalida
from calculadora.validaciones import (
    validar_orden_descendente,
    validar_repeticiones_icxm,
    validar_repeticiones_vld,
    validar_restas,
)
from calculadora.validaciones.alfabeto import validar_simbolos


def romano_a_entero(cadena: str) -> int:
    """
    Convierte una cadena de números romanos válida a su valor entero correspondiente.

    Nivel 6: Generación de Código - Conversión Romano → Entero

    💡 PISTA PRIMERO: Llama a todas las validaciones (Niveles 1-5) ANTES de convertir
    💡 PISTA: Usa validar_simbolos(cadena), validar_repeticiones_icxm(cadena), etc.
    💡 PISTA: Si alguna validación retorna False, lanza ExpresionInvalida con mensaje descriptivo (ej: 'contiene símbolos inválidos', 'repetición I/X/C/M', etc.)

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-5

    Returns:
        int: El valor entero correspondiente

    Examples:
        >>> romano_a_entero("I")
        1
        >>> romano_a_entero("V")
        5
        >>> romano_a_entero("IV")
        4
        >>> romano_a_entero("IX")
        9
        >>> romano_a_entero("XIV")
        14
        >>> romano_a_entero("MCMXCIV")
        1994
        >>> romano_a_entero("MMMCMXCIX")
        3999

    Raises:
        ExpresionInvalida: Si la cadena no es válida según las reglas de números romanos (símbolos inválidos, repeticiones inválidas, orden incorrecto, restas inválidas)
    """
    cadena = cadena.strip()

    if not validar_simbolos(cadena):
        raise ExpresionInvalida(f"'{cadena}' contiene símbolos inválidos")
    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida(f"'{cadena}' tiene repetición inválida de I/X/C/M")
    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida(f"'{cadena}' tiene repetición inválida de V/L/D")
    if not validar_orden_descendente(cadena):
        raise ExpresionInvalida(f"'{cadena}' no tiene orden descendente válido")
    if not validar_restas(cadena):
        raise ExpresionInvalida(f"'{cadena}' contiene restas inválidas")

    valores = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    resultado = 0
    valor_previo = 0

    for simbolo in reversed(cadena):
        valor_actual = valores[simbolo]
        if valor_actual < valor_previo:
            resultado -= valor_actual
        else:
            resultado += valor_actual
        valor_previo = valor_actual

    return resultado
