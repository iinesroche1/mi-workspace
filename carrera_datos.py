import streamlit as st

def inicializar_estados_carrera():
    if "estados_carrera" not in st.session_state:
        st.session_state.estados_carrera = {
            # 1° Año
            "8.1.0": "No cursada", "8.1.1": "No cursada", "8.1.2": "No cursada", "8.1.3": "No cursada",
            "8.1.4": "No cursada", "8.1.5": "No cursada", "8.1.6": "No cursada", "8.1.7": "No cursada",
            # 2° Año
            "8.2.1": "No cursada", "8.2.2": "No cursada", "8.2.3": "No cursada", "8.2.4": "No cursada",
            "8.2.5": "No cursada", "8.2.6": "No cursada", "8.2.7": "No cursada",
            # 3° Año
            "8.3.1": "No cursada", "8.3.2": "No cursada", "8.3.3": "No cursada", "8.3.4": "No cursada",
            "8.3.5": "No cursada", "8.3.6": "No cursada", "8.3.7": "No cursada", "8.3.8": "No cursada",
            "8.3.9": "No cursada", "8.3.10": "No cursada", "8.3.11": "No cursada",
            # 4° Año
            "8.4.1": "No cursada", "8.4.2": "No cursada", "8.4.3": "No cursada", "8.4.4": "No cursada",
            "8.4.5": "No cursada", "8.4.6": "No cursada", "8.4.7": "No cursada", "8.4.8": "No cursada",
            "8.4.9": "No cursada"
        }

def comprobar_desbloqueo_cadena(codigo, mapa_estados):
    # Tabla completa de correlatividades incluyendo las materias de 4° año de tus planillas
    requisitos = {
        "8.1.0": [], "8.1.1": [], "8.1.2": [], "8.1.3": [],
        "8.1.4": ["8.1.0", "8.1.1"], "8.1.5": ["8.1.0", "8.1.1"], "8.1.6": ["8.1.0", "8.1.1"], "8.1.7": ["8.1.0", "8.1.1"],
        "8.2.1": ["8.1.1"], "8.2.2": ["8.1.5"], "8.2.3": ["8.1.2"], "8.2.4": ["8.2.2"], "8.2.5": ["8.1.5", "8.1.6"], "8.2.6": ["8.1.4"], "8.2.7": ["8.1.4"],
        "8.3.1": ["8.2.2"], "8.3.2": ["8.2.5"], "8.3.3": ["8.2.2"], "8.3.4": ["8.2.3"], "8.3.5": ["8.2.5"], "8.3.6": ["8.2.1"], "8.3.7": ["8.2.1", "8.2.4"], "8.3.8": ["8.3.2"], "8.3.9": ["8.2.7", "8.3.1"], "8.3.10": ["8.2.5", "8.3.4"], "8.3.11": ["8.3.2"],
        # Correlatividades estrictas de 4° Año
        "8.4.1": ["8.3.1", "8.3.2"],
        "8.4.2": ["8.3.7"],
        "8.4.3": ["8.3.1"],
        "8.4.4": ["8.3.1"],
        "8.4.5": ["8.3.4"],
        "8.4.6": ["8.3.7", "8.3.2"],
        "8.4.7": ["8.3.1", "8.3.8"],
        "8.4.8": ["8.3.7", "8.3.8"],
        "8.4.9": ["8.3.7", "8.3.8"]
    }
    reqs = requisitos.get(codigo, [])
    for req in reqs:
        if mapa_estados.get(req, "No cursada") == "No cursada":
            return False
    return True

def obtener_materias():
    return [
        # 1° Año
        {"codigo": "8.1.0", "nombre": "Matemática Inicial y Técnicas de Estudio", "anio": "1° Año"},
        {"codigo": "8.1.1", "nombre": "Introducción a la Economía", "anio": "1° Año"},
        {"codigo": "8.1.2", "nombre": "Contabilidad I (Bases y Fundamentos)", "anio": "1° Año"},
        {"codigo": "8.1.3", "nombre": "Administración I", "anio": "1° Año"},
        {"codigo": "8.1.4", "nombre": "Microeconomía I", "anio": "1° Año"},
        {"codigo": "8.1.5", "nombre": "Matemática I", "anio": "1° Año"},
        {"codigo": "8.1.6", "nombre": "Laboratorio de Datos", "anio": "1° Año"},
        {"codigo": "8.1.7", "nombre": "Historia Económica Mundial y Argentina", "anio": "1° Año"},
        # 2° Año
        {"codigo": "8.2.1", "nombre": "Macroeconomía I", "anio": "2° Año"},
        {"codigo": "8.2.2", "nombre": "Matemática para Economistas I", "anio": "2° Año"},
        {"codigo": "8.2.3", "nombre": "Interpretación de los Estados Contables", "anio": "2° Año"},
        {"codigo": "8.2.4", "nombre": "Matemática para Economistas II", "anio": "2° Año"},
        {"codigo": "8.2.5", "nombre": "Estadística para Economistas", "anio": "2° Año"},
        {"codigo": "8.2.6", "nombre": "Finanzas Públicas", "anio": "2° Año"},
        {"codigo": "8.2.7", "nombre": "Comportamiento Estratégico", "anio": "2° Año"},
        # 3° Año
        {"codigo": "8.3.1", "nombre": "Microeconomía II", "anio": "3° Año"},
        {"codigo": "8.3.2", "nombre": "Econometría I", "anio": "3° Año"},
        {"codigo": "8.3.3", "nombre": "Estructura Social Argentina", "anio": "3° Año"},
        {"codigo": "8.3.4", "nombre": "Cálculo Financiero", "anio": "3° Año"},
        {"codigo": "8.3.5", "nombre": "Economía Espacial y Ambiental", "anio": "3° Año"},
        {"codigo": "8.3.6", "nombre": "Historia del Pensamiento Económico", "anio": "3° Año"},
        {"codigo": "8.3.7", "nombre": "Macroeconomía II", "anio": "3° Año"},
        {"codigo": "8.3.8", "nombre": "Econometría II", "anio": "3° Año"},
        {"codigo": "8.3.9", "nombre": "Organización Industrial", "anio": "3° Año"},
        {"codigo": "8.3.10", "nombre": "Mercado de Capitales", "anio": "3° Año"},
        {"codigo": "8.3.11", "nombre": "Economía Laboral", "anio": "3° Año"},
        # 4° Año
        {"codigo": "8.4.1", "nombre": "Desarrollo Económico", "anio": "4° Año"},
        {"codigo": "8.4.2", "nombre": "Moneda, Crédito y Bancos", "anio": "4° Año"},
        {"codigo": "8.4.3", "nombre": "Comercio Internacional", "anio": "4° Año"},
        {"codigo": "8.4.4", "nombre": "Economía de las Instituciones", "anio": "4° Año"},
        {"codigo": "8.4.5", "nombre": "Finanzas de Empresas", "anio": "4° Año"},
        {"codigo": "8.4.6", "nombre": "Finanzas Internacionales", "anio": "4° Año"},
        {"codigo": "8.4.7", "nombre": "Economía del Sector Público", "anio": "4° Año"},
        {"codigo": "8.4.8", "nombre": "Política Económica", "anio": "4° Año"},
        {"codigo": "8.4.9", "nombre": "Economía de los Ciclos y las Crisis", "anio": "4° Año"}
    ]
