import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

def mostrar_vista_salud():
    # ==============================================================================
    # 1. ESTILOS NEÓN Y TEXTOS BRILLANTES (CSS PREMIUM)
    # ==============================================================================
    st.markdown('''
        <style>
            /* Forzar que todos los títulos e inputs sean blanco brillante */
            label, div[data-testid="stWidgetLabel"] p, h3 {
                color: #ffffff !important;
                font-weight: 600 !important;
                letter-spacing: -0.5px;
            }
            .stMarkdown p, p, span {
                color: #ced4da !important;
            }
            
            /* Tarjeta contenedora oscura para los indicadores */
            .tarjeta-indicadores {
                background-color: #1a1a1e !important;
                border: 1px solid rgba(255, 255, 255, 0.05) !important;
                border-radius: 16px !important;
                padding: 24px !important;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
                margin-top: 10px;
            }
            
            /* Número de IMC gigante en Verde Neón */
            [data-testid="stMetricValue"] div {
                color: #00ff66 !important;
                font-size: 4rem !important;
                font-weight: 900 !important;
                text-shadow: 0 0 20px rgba(0, 255, 102, 0.4);
            }
            
            /* Diseño estético para el botón de guardar */
            .stButton > button {
                background: linear-gradient(135deg, #ff8811 0%, #ff4a4a 100%) !important;
                color: white !important;
                font-weight: 700 !important;
                border: none !important;
                padding: 10px 24px !important;
                border-radius: 10px !important;
                transition: all 0.3s ease !important;
                width: 100% !important;
                margin-top: 15px;
            }
            .stButton > button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 5px 15px rgba(255, 136, 17, 0.4) !important;
            }
        </style>
    ''', unsafe_allow_html=True)

    st.markdown('<h2 style="color: #ffffff; font-weight: 900; font-size: 2.8rem; letter-spacing: -1.5px;">❤️ Health & Performance</h2>', unsafe_allow_html=True)
    st.write("Gestiona tus parámetros biométricos y mantén un registro de tu evolución temporal.")
    st.markdown("<br>", unsafe_allow_html=True)

    # ==============================================================================
    # 2. CONFIGURACIÓN INICIAL DE ENTRADAS (VALORES POR DEFECTO REUTILIZABLES)
    # ==============================================================================
    # Valores base iniciales seguros para adultos
    peso_defecto = 70.0
    meta_defecto = 65.0

    # ==============================================================================
    # 3. DISTRIBUCIÓN DE COLUMNAS PRINCIPALES (INPUTS Y ANÁLISIS)
    # ==============================================================================
    col_inputs, col_stats = st.columns([1, 1.2])
    
    with col_inputs:
        st.markdown("### 📝 Registro Métrico")
        peso_actual = st.number_input("Tu peso actual (kg):", min_value=35.0, max_value=250.0, value=peso_defecto, step=0.1, key="salud_p_act")
        altura = st.number_input("Tu altura (metros):", min_value=1.20, max_value=2.30, value=1.70, step=0.01, key="salud_a_act")
        peso_meta = st.number_input("Tu peso objetivo (kg):", min_value=35.0, max_value=250.0, value=meta_defecto, step=0.1, key="salud_p_met")

        # ==============================================================================
        # 4. GESTIÓN DEL HISTORIAL DE PESO (BASE DE DATOS LOCAL EN CSV)
        # ==============================================================================
        archivo_csv = "historico_peso.csv"
        
        # Si el archivo no existe, creamos una línea de tiempo limpia separada por semanas
        if not os.path.exists(archivo_csv):
            df_inicial = pd.DataFrame({
                "Fecha": [
                    (datetime.now() - pd.Timedelta(weeks=3)).strftime("%Y-%m-%d"),
                    (datetime.now() - pd.Timedelta(weeks=2)).strftime("%Y-%m-%d"),
                    (datetime.now() - pd.Timedelta(weeks=1)).strftime("%Y-%m-%d"),
                    datetime.now().strftime("%Y-%m-%d")
                ],
                "Peso": [peso_actual + 2.5, peso_actual + 1.8, peso_actual + 0.9, peso_actual],
                "Meta": [peso_meta] * 4
            })
            df_inicial.to_csv(archivo_csv, index=False)

        # Cargar los datos actuales guardados
        df_historico = pd.read_csv(archivo_csv)
        
        # BOTÓN DE GUARDADO SEMANAL PERSISTENTE
        if st.button("Guardar Registro de esta Semana 💾"):
            nueva_fecha = datetime.now().strftime("%Y-%m-%d")
            
            # Si ya registraste peso hoy, actualiza el valor; si no, añade una nueva fila
            if nueva_fecha in df_historico["Fecha"].values:
                df_historico.loc[df_historico["Fecha"] == nueva_fecha, "Peso"] = peso_actual
                df_historico.loc[df_historico["Fecha"] == nueva_fecha, "Meta"] = peso_meta
            else:
                nuevo_registro = pd.DataFrame({"Fecha": [nueva_fecha], "Peso": [peso_actual], "Meta": [peso_meta]})
                df_historico = pd.concat([df_historico, nuevo_registro], ignore_index=True)
            
            df_historico.to_csv(archivo_csv, index=False)
            st.toast("¡Registro guardado con éxito! 🚀", icon="✅")
            st.rerun()
            
    with col_stats:
        st.markdown("### 🩺 Análisis Clínico")
        st.markdown('<div class="tarjeta-indicators">', unsafe_allow_html=True)
        
        # Cálculo matemático estándar de IMC para adultos
        imc = peso_actual / (altura ** 2)
        st.metric(label="Índice de Masa Corporal (IMC)", value=f"{imc:.1f}")
        
        # Mensajes con pautas generales basados en rangos de consenso médico para adultos
        if imc < 18.5:
            st.info("💡 Tu IMC se encuentra en el rango de bajo peso. Considera consultar con un profesional de la salud para estructurar un plan de alimentación adecuado.")
        elif 18.5 <= imc < 25.0:
            st.success("🌱 ¡Excelente! Tu IMC se encuentra dentro del rango estándar considerado saludable.")
        elif 25.0 <= imc < 30.0:
            st.warning("⚡ Tu IMC se sitúa en el rango de sobrepeso. Mantener hábitos activos ayuda a estabilizar tus métricas corporales.")
        else:
            st.error("🚨 Tu IMC se encuentra en el rango de obesidad. Se recomienda un chequeo con un especialista para diseñar metas personalizadas y seguras.")
            
        st.markdown('</div>', unsafe_allow_html=True)

    # ==============================================================================
    # 5. GRÁFICO PREMIUM COMPLETAMENTE OSCURO CON PLOTLY
    # ==============================================================================
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### 📈 Evolución Histórica Real")
    st.write("Línea Neón representa tus pesajes guardados; Línea Coral marca tu meta fija:")
    
    # Ordenamos los registros cronológicamente para que la línea fluya bien hacia el futuro
    df_historico = df_historico.sort_values("Fecha")
    
    # Creación del gráfico interactivo con Plotly Dark
    fig = px.line(
        df_historico, 
        x="Fecha", 
        y=["Peso", "Meta"],
        labels={"value": "Kilogramos (kg)", "variable": "Métrica"},
        template="plotly_dark"
    )
    
    # Modificación de colores: Verde Neón para tu peso e historial, Coral brillante para la meta
    fig.update_traces(line=dict(color="#00ff66", width=4), selector=dict(name="Peso"))
    fig.update_traces(line=dict(color="#ff4a4a", width=2, dash="dash"), selector=dict(name="Meta"))
    
    # Ajustes profundos de layout para integrarlo al diseño oscuro mate del main.py
    fig.update_layout(
        paper_bgcolor="#121214", # Fondo del bloque idéntico al de tu main
        plot_bgcolor="#1a1a1e",  # Fondo interior de la gráfica oscuro mate
        font=dict(color="#ffffff", family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"),
        xaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)", title_text="Semanas de Control"),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)", title_text="Peso (kg)"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=10, b=20)
    )
    
    # Renderizar el gráfico interactivo en la pantalla de Streamlit
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    mostrar_vista_salud()
