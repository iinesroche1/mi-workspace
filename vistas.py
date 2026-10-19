# vistas.py
import streamlit as st
import datetime

# Importación de las fracciones y componentes separados
from componentes.dashboard_uni import render_dashboard
from componentes.correlatividades import render_correlatividades
from componentes.pomodoro import render_pomodoro
from componentes.estadisticas import render_estadisticas
from plan_estudios import PLAN_FCE_ECONOMIA

def inicializar_horas_si_vacio():
    if "horas_estudio" not in st.session_state.db:
        st.session_state.db["horas_estudio"] = [
            {"fecha": str(datetime.date.today() - datetime.timedelta(days=2)), "materia": "8.1.1 - Introducción a la Economía y Estructura Argentina", "horas": 4.0},
            {"fecha": str(datetime.date.today() - datetime.timedelta(days=1)), "materia": "8.1.5 - Matemática I", "horas": 3.0}
        ]

def inicializar_plan_si_vacio():
    if "materias" not in st.session_state.db or not st.session_state.db["materias"]:
        st.session_state.db["materias"] = {}
        for codigo, info in PLAN_FCE_ECONOMIA.items():
            st.session_state.db["materias"][codigo] = {
                "nombre": info["nombre"],
                "anio": info["anio"],
                "estado": "No Cursada"
            }

def aplicar_estilos_interiores_uni():
    st.markdown('''
        <style>
            /* --- ENCABEZADOS PRINCIPALES --- */
            .wrapper-header-uni { margin-top: 10px; margin-bottom: 25px; }
            .titulo-seccion-uni { color: #ffffff !important; font-family: -apple-system, sans-serif !important; font-size: 2.5rem !important; font-weight: 800 !important; }
            .subtitulo-seccion-uni { color: #8b8b93 !important; font-size: 1.05rem !important; }

            /* --- ELEMENTOS DE TEXTO GLOBALES --- */
            h3, p, span, label, div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"] p { 
                color: #ffffff !important; 
                font-family: -apple-system, sans-serif !important; 
            }
            
            /* --- CONTRASTE DE LOS SELECTORES (NOMBRES EN BLANCO) --- */
            div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
                color: #ffffff !important;
                font-weight: 600 !important;
                font-size: 1rem !important;
            }
            div[data-testid="stSelectbox"] svg { fill: #ffffff !important; }
            div[data-testid="stNumberInput"] label p, div[data-testid="stSelectbox"] label p { 
                color: #ffffff !important; 
                font-weight: 600 !important; 
                font-size: 1.05rem !important; 
            }

            /* --- NAVEGACIÓN POR PESTAÑAS (TABS) --- */
            div[data-testid="stTabs"] button {
                color: #8b8b93 !important; font-size: 1.1rem !important; font-weight: 600 !important;
                background-color: transparent !important; border: none !important; transition: all 0.3s ease;
            }
            div[data-testid="stTabs"] button[aria-selected="true"] { color: #ff7b00 !important; border-bottom: 2px solid #ff7b00 !important; }

            /* --- TARJETAS COMPONENTES --- */
            .progress-container { background-color: #1a1a1e; border: 1px solid rgba(255,255,255,0.04); border-radius: 16px; padding: 24px; margin-bottom: 25px; }
            .progress-header { display: flex; justify-content: space-between; margin-bottom: 14px; }
            .progress-title-text { color: #00ff66 !important; font-size: 1.1rem !important; font-weight: 700 !important; }
            .progress-stats-text { color: #ffffff !important; font-size: 1.1rem !important; font-weight: 700 !important; }
            
            .materia-card { border-radius: 14px; padding: 20px; min-height: 140px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 8px 24px rgba(0,0,0,0.4); border: 1px solid rgba(255, 255, 255, 0.03); }
            .state-no-cursada { background-color: #141416 !important; border-left: 5px solid #3a3a3c !important; }
            .state-cursando { background-color: #2b2513 !important; border-left: 5px solid #ffcc00 !important; }
            .state-cursada-o-final-pendiente { background-color: #2d1616 !important; border-left: 5px solid #ff453a !important; }
            .state-final-aprobado { background-color: #132d1f !important; border-left: 5px solid #30d158 !important; }
            .state-bloqueada { background-color: #0f0f11 !important; border: 1px dashed rgba(255,255,255,0.03) !important; opacity: 0.3; }
            .materia-code { font-size: 0.8rem; color: #8e8e93 !important; font-weight: 700; }
            .materia-name { font-size: 1.1rem; font-weight: 700; margin-top: 8px; margin-bottom: 15px; color: #ffffff !important; }
            
            .metric-card-pro { background: #1a1a1e; border: 1px solid rgba(255,255,255,0.04); border-radius: 14px; padding: 20px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.4); margin-bottom: 10px; }
            .metric-card-pro h5 { color: #8b8b93 !important; font-size: 0.9rem !important; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px; }
            .metric-card-pro p { color: #ffffff !important; font-size: 2.2rem !important; font-weight: 800 !important; }

            div[data-testid="stSelectbox"] > div, div[data-testid="stNumberInput"] > div { background-color: rgba(0,0,0,0.4) !important; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 8px !important; }
            div[data-testid="stProgress"] > div > div { background-color: #30d158 !important; }
            div[data-testid="stRadio"] label p { color: #ffffff !important; font-size: 1.05rem !important; font-weight: 600 !important; }

            /* --- TEXTO DE NOTIFICACIONES EN NEGRO --- */
            div[data-testid="stToast"] { background-color: #ffffff !important; border: 1px solid #ff7b00 !important; border-radius: 10px !important; box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important; }
            div[data-testid="stToast"] div { color: #000000 !important; font-weight: 700 !important; font-family: -apple-system, sans-serif !important; }

            /* --- BOTONES PREMIUM UNIFICADOS --- */
            div.stButton > button {
                background-color: #1a1a1e !important; color: #ffffff !important; border: 1px solid rgba(255,255,255,0.08) !important;
                border-radius: 10px !important; padding: 0.65rem 1.5rem !important; font-size: 0.95rem !important; font-weight: 700 !important;
                letter-spacing: 0.02em !important; box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important; transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important; width: 100% !important;
            }
            div.stButton > button:hover {
                background-color: #222227 !important; color: #ff7b00 !important; border-color: #ff7b00 !important; box-shadow: 0 0 20px rgba(255, 123, 0, 0.35) !important; transform: translateY(-2px) !important;
            }
        </style>
    ''', unsafe_allow_html=True)

def vista_calculadora_horas():
    inicializar_plan_si_vacio()
    inicializar_horas_si_vacio()
    aplicar_estilos_interiores_uni()
    
    st.markdown('''
        <div class="wrapper-header-uni">
            <h2 class="titulo-seccion-uni">🎓 Workspace Universitario</h2>
            <p class="subtitulo-seccion-uni">> Plan VIII (2017) — Licenciatura en Economía FCE UNLP</p>
        </div>''', unsafe_allow_html=True)

    # REORGANIZACIÓN: Ahora se despliegan 4 pestañas nativas, lideradas por el Dashboard
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📋 Correlatividades", "⏳ Pomodoro Clock", "📈 Horas de Estudio"])

    with tab1:
        render_dashboard()
    with tab2:
        render_correlatividades()
    with tab3:
        render_pomodoro()
    with tab4:
        render_estadisticas()

# Mantenemos el puente de compatibilidad intacto abajo de todo
vista_university = vista_calculadora_horas
vista_universidad = vista_calculadora_horas
