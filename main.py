import streamlit as st
import vistas  # Importa tu archivo secundario de vistas
import salud  # Importa tu archivo secundario de salud

# ==============================================================================
# 0. CONFIGURACIÓN DE PÁGINA NATIVA (FUERZA EL MODO ANCHO EN STREAMLIT)
# ==============================================================================
st.set_page_config(layout="wide")

# ==============================================================================
# 1. INICIALIZACIÓN ABSOLUTA DEL ESTADO
# ==============================================================================
if "db" not in st.session_state:
    st.session_state.db = {}

if "modulo_activo" not in st.session_state:
    st.session_state.modulo_activo = None

# Manejo de clics mediante parámetros en la URL
params = st.query_params
if "ir_a" in params:
    st.session_state.modulo_activo = params["ir_a"]
    st.query_params.clear()
    st.rerun()

# Inicializaciones de tu base de datos secundaria si existen
if hasattr(vistas, 'inicializar_horas_si_vacio'):
    vistas.inicializar_horas_si_vacio()
if hasattr(vistas, 'inicializar_plan_si_vacio'):
    vistas.inicializar_plan_si_vacio()

# ==============================================================================
# 2. ESTILOS OSCUROS PREMIUM (PANTALLA COMPLETA Y MARGENES EXTENDIDOS)
# ==============================================================================
st.markdown('''
    <style>
        /* ELIMINA LOS MÁRGENES LATERALES DE STREAMLIT (OCUPA TODA LA COMPU) */
        .block-container {
            max-width: 100% !important;
            padding-left: 5rem !important;
            padding-right: 5rem !important;
            padding-top: 3rem !important;
        }

        /* Fondo general de la app */
        [data-testid="stAppViewContainer"], [data-testid="stHeader"] { 
            background-color: #121214 !important; 
        }
        
        /* Tipografías base */
        h1, h2, h3, h4, h5, h6, p, span, label, div { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        }

        /* Encabezado */
        .pildora-terminal { 
            background: #1c1414; color: #ff7b00; padding: 6px 14px; border-radius: 6px; 
            font-size: 0.8rem; font-weight: bold; display: inline-block; margin-bottom: 1rem; 
            border: 1px solid #ff7b0033; letter-spacing: 0.1em; text-transform: uppercase;
        }
        
        .titulo-terminal { 
            font-size: 4.5rem !important; 
            font-weight: 900 !important; 
            color: #ffffff !important; 
            margin-bottom: 0.5rem; 
            letter-spacing: -2px !important;
            line-height: 1.1 !important;
        }
        
        .sub-text { font-size: 1.1rem; color: #8b8b93 !important; margin-bottom: 2.5rem; }

        /* RECTÁNGULOS DE LAS TARJETAS */
        .tarjeta-link {
            text-decoration: none !important;
            display: block;
        }
        
        .tarjeta-container {
            background-color: #1a1a1e;
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: 20px; 
            padding: 30px; 
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            position: relative;
            overflow: hidden;
            box-shadow: 0 12px 40px rgba(0,0,0,0.6);
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), border-color 0.3s ease, box-shadow 0.3s ease;
        }

        /* Medidas de largo perfectas (Salud más corto) */
        .bg-uni, .bg-custom { 
            min-height: 310px; 
        }
        .bg-salud { 
            min-height: 260px; 
        }

        /* Capa oscura interna */
        .tarjeta-container::before {
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(180deg, rgba(26,26,30,0.88) 0%, rgba(26,26,30,0.98) 100%);
            z-index: 1;
        }

        .tarjeta-info {
            position: relative;
            z-index: 2;
        }
        
        .tarjeta-info p { 
            color: #a4a4ab !important; 
            line-height: 1.6; 
            font-size: 1rem; 
            margin-top: 14px;
        }

        /* TÍTULOS VIBRANTES EN UN SOLO RENGLÓN */
        .title-uni { 
            color: #ff4a4a !important; 
            font-size: 1.45rem; 
            font-weight: 700; 
            white-space: nowrap; 
            text-shadow: 0 0 10px rgba(255, 74, 74, 0.2); 
        }
        .title-salud { 
            color: #ff8811 !important; 
            font-size: 1.45rem; 
            font-weight: 700; 
            white-space: nowrap; 
            text-shadow: 0 0 10px rgba(255, 136, 17, 0.2); 
        }
        .title-custom { 
            color: #00ff66 !important; 
            font-size: 1.45rem; 
            font-weight: 700; 
            white-space: nowrap; 
            text-shadow: 0 0 10px rgba(0, 255, 102, 0.2); 
        }

        /* Imágenes de fondo sutiles */
        .bg-uni { background-image: url('https://unsplash.com'); }
        .bg-salud { background-image: url('https://unsplash.com'); }
        .bg-custom { background-image: url('https://unsplash.com'); }

        /* EFECTOS HOVER COMPLEMENTARIOS DIRECTOS */
        .tarjeta-link:hover .bg-uni { transform: translateY(-6px); border-color: #ff4a4a !important; box-shadow: 0 20px 40px rgba(255, 74, 74, 0.25) !important; }
        .tarjeta-link:hover .bg-salud { transform: translateY(-6px); border-color: #ff8811 !important; box-shadow: 0 20px 40px rgba(255, 136, 17, 0.25) !important; }
        .tarjeta-link:hover .bg-custom { transform: translateY(-6px); border-color: #00ff66 !important; box-shadow: 0 20px 40px rgba(0, 255, 102, 0.25) !important; }
    </style>
''', unsafe_allow_html=True)

# ==============================================================================
# 3. LÓGICA DE NAVEGACIÓN Y RENDERIZADO PRINCIPAL
# ==============================================================================
if st.session_state.modulo_activo is None:
    
    # Encabezado Principal
    st.markdown('<div class="pildora-terminal">Personal Workspace</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="titulo-terminal">Command.</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">> Tu centro de operaciones personal.</p>', unsafe_allow_html=True)

    # REPARTO ASIMÉTRICO EN PANTALLA COMPLETA
    col1, col2, col3 = st.columns([1.3, 0.9, 1.6])

    with col1:
        st.markdown('''
            <a href="/?ir_a=universidad" target="_self" class="tarjeta-link">
                <div class="tarjeta-container bg-uni">
                    <div class="tarjeta-info">
                        <h3 class="title-uni">🎓 Universidad</h3>
                        <p>Plan académico, mapa de correlatividades en grilla y reloj Pomodoro.</p>
                    </div>
                </div>
            </a>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
            <a href="/?ir_a=salud" target="_self" class="tarjeta-link">
                <div class="tarjeta-container bg-salud">
                    <div class="tarjeta-info">
                        <h3 class="title-salud">❤️ Salud</h3>
                        <p>Rastreador automático de racha celíaca y control de peso.</p>
                    </div>
                </div>
            </a>
        ''', unsafe_allow_html=True)

    with col3:
        st.markdown('''
            <a href="/?ir_a=custom" target="_self" class="tarjeta-link">
                <div class="tarjeta-container bg-custom">
                    <div class="tarjeta-info">
                        <h3 class="title-custom">📁 Personalizado</h3>
                        <p>Módulos dinámicos, bitácoras y herramientas externas creadas a tu medida.</p>
                    </div>
                </div>
            </a>
        ''', unsafe_allow_html=True)

# ==============================================================================
# 4. ENRUTAMIENTO SEGURO DE LOS MÓDULOS ACTIVOS
# ==============================================================================
else:
    # Botón flotante superior para volver al menú "Command."
    if st.button("⬅️ Volver al Centro de Operaciones"):
        st.session_state.modulo_activo = None
        st.rerun()
        
    st.markdown("---")

    if st.session_state.modulo_activo == "salud":
        salud.mostrar_vista_salud()
        
    elif st.session_state.modulo_activo == "universidad":
        # Llama a la función correcta dentro de vistas.py
        vistas.vista_universidad()
            
    elif st.session_state.modulo_activo == "custom":
        st.info("⚡ Módulo Personalizado: Espacio libre para tus futuras bitácoras.")
