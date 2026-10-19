import streamlit as st

def cargar_estilos_globales():
    st.markdown(
        """
        <style>
        :root {
            --vivo: #B34A29;          
            --vivo-oscuro: #8D2D00;   
            --vivo-suave: #F9E6DC;    
            --tinta: #2B1A10;         
            --gris: #7A6A5C;          
            --linea: #EADFC8;         
            --borde-boton: #DCCDB0;
            --fondo-suave: #F4EEDF;   
            --verde: #4A8C67;
            --verde-suave: #DCEFE4;
            --amarillo: #FBA93B;
            --amarillo-suave: #FFE9CC;
        }
        .stApp {
            background-color: var(--fondo-suave) !important;
        }
        .stApp *:not([data-testid="stIconMaterial"]) {
            font-family: "Times New Roman", Times, serif !important;
        }
        .pildora {
            display: inline-block;
            background: var(--vivo-suave);
            color: var(--vivo);
            font-size: 0.85rem;
            font-weight: 700;
            padding: 0.3rem 0.9rem;
            border-radius: 999px;
            margin-top: 1.5rem;
        }
        .titulo-command {
            font-size: clamp(3rem, 12vw, 5.2rem);
            font-weight: 800;
            color: var(--tinta);
            margin: 0.5rem 0 0.2rem 0;
        }
        .titulo-pagina {
            font-size: clamp(2rem, 8vw, 3.2rem);
            font-weight: 800;
            color: var(--tinta);
            margin: 0.4rem 0 0.3rem 0;
        }
        .titulo-pagina span {
            color: var(--vivo);
        }
        .subtitulo-command {
            font-size: 1.25rem;
            color: var(--gris);
            margin-bottom: 2rem;
        }
        .tarjeta {
            background: #FFFFFF;
            border: 1px solid var(--linea);
            border-radius: 20px;
            padding: 1.3rem;
            box-shadow: 0 4px 18px rgba(43, 26, 16, 0.07);
            margin-bottom: 1rem;
        }
        .tarjeta-titulo {
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--tinta);
        }
        .barra-progreso-contenedor {
            background-color: #EADFC8;
            border-radius: 10px;
            height: 24px;
            width: 100%;
            margin-bottom: 1.5rem;
            overflow: hidden;
            border: 1px solid var(--borde-boton);
        }
        .barra-progreso-relleno {
            background: linear-gradient(90deg, var(--vivo) 0%, #E8862A 100%);
            height: 100%;
            text-align: center;
            color: white;
            font-weight: bold;
            line-height: 24px;
            transition: width 0.5s ease;
        }
        .semaforo {
            display: inline-block;
            width: 14px;
            height: 14px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .semaforo-rojo { background-color: var(--vivo); box-shadow: 0 0 8px var(--vivo); }
        .semaforo-amarillo { background-color: var(--amarillo); box-shadow: 0 0 8px var(--amarillo); }
        .semaforo-verde { background-color: var(--verde); box-shadow: 0 0 8px var(--verde); }
        </style>
        """,
        unsafe_allow_html=True
    )

