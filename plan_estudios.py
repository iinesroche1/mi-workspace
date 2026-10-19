# plan_estudios.py

# Base de datos oficial con las correlatividades del Plan VIII (2017) de la FCE UNLP
PLAN_FCE_ECONOMIA = {
    "8.1.0": {"nombre": "Matemática Inicial y Técnicas de Estudio", "anio": 1, "req_cursada": [], "req_final": []},
    "8.1.1": {"nombre": "Introducción a la Economía y Estructura Argentina", "anio": 1, "req_cursada": [], "req_final": []},
    "8.1.2": {"nombre": "Contabilidad I (Bases y Fundamentos)", "anio": 1, "req_cursada": [], "req_final": []},
    "8.1.3": {"nombre": "Administración I (Intro. a las Organizaciones)", "anio": 1, "req_cursada": [], "req_final": []},
    "8.1.4": {"nombre": "Microeconomía I", "anio": 1, "req_cursada": ["8.1.0", "8.1.1"], "req_final": []},
    "8.1.5": {"nombre": "Matemática I", "anio": 1, "req_cursada": ["8.1.0", "8.1.1"], "req_final": []},
    "8.1.6": {"nombre": "Laboratorio de Datos", "anio": 1, "req_cursada": ["8.1.0", "8.1.1"], "req_final": []},
    "8.1.7": {"nombre": "Historia Económica Mundial y Argentina", "anio": 1, "req_cursada": ["8.1.0", "8.1.1"], "req_final": []},
    
    "8.2.1": {"nombre": "Macroeconomía I", "anio": 2, "req_cursada": ["8.1.1"], "req_final": []},
    "8.2.2": {"nombre": "Matemática para Economistas I", "anio": 2, "req_cursada": ["8.1.5"], "req_final": []},
    "8.2.3": {"nombre": "Interpretación de los Estados Contables", "anio": 2, "req_cursada": ["8.1.2"], "req_final": []},
    "8.2.4": {"nombre": "Matemática para Economistas II", "anio": 2, "req_cursada": ["8.2.2"], "req_final": []},
    "8.2.5": {"nombre": "Estadística para Economistas", "anio": 2, "req_cursada": ["8.1.5", "8.1.6"], "req_final": []},
    "8.2.6": {"nombre": "Finanzas Públicas", "anio": 2, "req_cursada": ["8.1.4"], "req_final": []},
    "8.2.7": {"nombre": "Comportamiento Estratégico", "anio": 2, "req_cursada": ["8.1.4"], "req_final": []},
    
    "8.3.1": {"nombre": "Microeconomía II", "anio": 3, "req_cursada": ["8.2.2"], "req_final": []},
    "8.3.2": {"nombre": "Econometría I", "anio": 3, "req_cursada": ["8.2.5"], "req_final": []},
    "8.3.3": {"nombre": "Estructura Social Argentina", "anio": 3, "req_cursada": ["8.2.2"], "req_final": []},
    "8.3.4": {"nombre": "Cálculo Financiero", "anio": 3, "req_cursada": ["8.2.3"], "req_final": []},
    "8.3.5": {"nombre": "Economía Espacial y Ambiental", "anio": 3, "req_cursada": ["8.2.5"], "req_final": []},
    "8.3.6": {"nombre": "Historia del Pensamiento Económico", "anio": 3, "req_cursada": ["8.2.1"], "req_final": []},
    "8.3.7": {"nombre": "Macroeconomía II", "anio": 3, "req_cursada": ["8.2.1", "8.2.4"], "req_final": []},
    "8.3.8": {"nombre": "Econometría II", "anio": 3, "req_cursada": ["8.3.2"], "req_final": []},
    "8.3.9": {"nombre": "Organización Industrial", "anio": 3, "req_cursada": ["8.2.7", "8.3.1"], "req_final": []},
    "8.3.10": {"nombre": "Mercado de Capitales", "anio": 3, "req_cursada": ["8.2.5", "8.3.4"], "req_final": []},
    "8.3.11": {"nombre": "Economía Laboral", "anio": 3, "req_cursada": ["8.3.2"], "req_final": []},
    "8.3.12": {"nombre": "Materia Optativa", "anio": 3, "req_cursada": [], "req_final": []},
    
    "8.4.1": {"nombre": "Desarrollo Económico", "anio": 4, "req_cursada": ["8.3.1", "8.3.2"], "req_final": []},
    "8.4.2": {"nombre": "Moneda, Crédito y Bancos", "anio": 4, "req_cursada": ["8.3.7"], "req_final": []},
    "8.4.3": {"nombre": "Comercio Internacional", "anio": 4, "req_cursada": ["8.3.1"], "req_final": []},
    "8.4.4": {"nombre": "Economía de las Instituciones", "anio": 4, "req_cursada": ["8.3.1"], "req_final": []},
    "8.4.5": {"nombre": "Finanzas de Empresas", "anio": 4, "req_cursada": ["8.3.4"], "req_final": []},
    "8.4.6": {"nombre": "Finanzas Internacionales", "anio": 4, "req_cursada": ["8.3.7", "8.3.2"], "req_final": []},
    "8.4.7": {"nombre": "Economía del Sector Público", "anio": 4, "req_cursada": ["8.3.1", "8.3.8"], "req_final": []},
    "8.4.8": {"nombre": "Política Económica", "anio": 4, "req_cursada": ["8.3.7", "8.3.8"], "req_final": []},
    "8.4.9": {"nombre": "Economía de los Ciclos y Crisis", "anio": 4, "req_cursada": ["8.3.7", "8.3.8"], "req_final": []}
}
