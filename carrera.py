import streamlit as st
import carrera_datos

def mostrar_malla_curricular():
    carrera_datos.inicializar_estados_carrera()
    
    st.markdown('''
        <style>
            div[data-testid="stWidgetLabel"] p, label {
                color: rgba(255, 255, 255, 0.6) !important;
                font-size: 0.85rem !important;
            }
            .bloque-materia-vertical {
                background-color: #1a1a1e;
                border: 2px solid rgba(255, 255, 255, 0.08);
                border-radius: 14px;
                padding: 18px;
                margin-bottom: 5px;
                transition: all 0.3s ease;
            }
            .bloque-materia-vertical:hover {
                transform: translateY(-3px);
                border-color: #ffffff !important;
            }
            .bloque-aprobada { background-color: #112217 !important; border: 2px solid #00ff66 !important; }
            .bloque-aprobada:hover { box-shadow: 0 8px 20px rgba(0, 255, 102, 0.25) !important; }
            
            .bloque-pendiente { background-color: #261212 !important; border: 2px solid #ff3333 !important; }
            .bloque-pendiente:hover { box-shadow: 0 8px 20px rgba(255, 51, 51, 0.25) !important; }
            
            .bloque-cursando { background-color: #262012 !important; border: 2px solid #ffcc00 !important; }
            .bloque-cursando:hover { box-shadow: 0 8px 20px rgba(255, 204, 0, 0.25) !important; }

            .bloque-bloqueada { background-color: #121214 !important; border: 2px dashed rgba(255, 255, 255, 0.04) !important; opacity: 0.4; padding: 18px; border-radius: 14px; margin-bottom: 15px; }
        </style>
    ''', unsafe_allow_html=True)
    
    st.markdown("### 📊 Mapeo del Plan de Estudios (Lic. en Economía)")
    
    materias = carrera_datos.obtener_materias()
    opciones = ["No cursada", "Cursando", "Promocionada", "Final pendiente", "Final Aprobado"]
    
    # 🔑 AGREGADO: Añadimos "4° Año" a las pestañas de navegación
    lista_anios = ["1° Año", "2° Año", "3° Año", "4° Año"]
    tabs = st.tabs(lista_anios)
    
    for idx, anio_t in enumerate(lista_anios):
        with tabs[idx]:
            filtradas = [m for m in materias if m["anio"] == anio_t]
            
            for k in range(0, len(filtradas), 2):
                c1, c2 = st.columns(2)
                
                with c1:
                    m = filtradas[k]
                    desbloqueada = carrera_datos.comprobar_desbloqueo_cadena(m["codigo"], st.session_state.estados_carrera)
                    if desbloqueada:
                        estado = st.session_state.estados_carrera[m["codigo"]]
                        clase = "bloque-materia-vertical"
                        if estado in ["Final Aprobado", "Promocionada"]: clase += " bloque-aprobada"
                        elif estado == "Final pendiente": clase += " bloque-pendiente"
                        elif estado == "Cursando": clase += " bloque-cursando"
                        
                        st.markdown(f'<div class="{clase}"><div style="color:#ffffff !important; font-size:1.1rem; font-weight:700;">{m["codigo"]} - {m["nombre"]}</div></div>', unsafe_allow_html=True)
                        actual = st.selectbox("Estado de cursada:", opciones, index=opciones.index(estado), key=f"c_{m['codigo']}")
                        if actual != estado:
                            st.session_state.estados_carrera[m["codigo"]] = actual
                            st.rerun()
                    else:
                        st.markdown(f'<div class="bloque-bloqueada"><span style="color:#6c757d !important; font-weight:600;">🔒 {m["codigo"]} — {m["nombre"]}</span></div>', unsafe_allow_html=True)
                        
                with c2:
                    if k + 1 < len(filtradas):
                        m = filtradas[k+1]
                        desbloqueada = carrera_datos.comprobar_desbloqueo_cadena(m["codigo"], st.session_state.estados_carrera)
                        if desbloqueada:
                            estado = st.session_state.estados_carrera[m["codigo"]]
                            clase = "bloque-materia-vertical"
                            if estado in ["Final Aprobado", "Promocionada"]: clase += " bloque-aprobada"
                            elif estado == "Final pendiente": clase += " bloque-pendiente"
                            elif estado == "Cursando": clase += " bloque-cursando"
                            
                            st.markdown(f'<div class="{clase}"><div style="color:#ffffff !important; font-size:1.1rem; font-weight:700;">{m["codigo"]} - {m["nombre"]}</div></div>', unsafe_allow_html=True)
                            actual = st.selectbox("Estado de cursada:", opciones, index=opciones.index(estado), key=f"c_{m['codigo']}")
                            if actual != estado:
                                st.session_state.estados_carrera[m["codigo"]] = actual
                                st.rerun()
                        else:
                            st.markdown(f'<div class="bloque-bloqueada"><span style="color:#6c757d !important; font-weight:600;">🔒 {m["codigo"]} — {m["nombre"]}</span></div>', unsafe_allow_html=True)
