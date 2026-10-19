"""
Command - mi app personal (Streamlit)

Estructura de páginas (cada una se abre dentro de la anterior):

  Command (inicio)
  ├── Universidad
  │     └── <una página por carrera>  (resumen, materias y tareas)
  ├── Salud
  │     ├── Días sin contaminación
  │     └── Peso
  └── <páginas que crees con el botón +>
        └── <y dentro de cada una, más páginas>
"""

import calendar
import html
import json
import re
import uuid
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Command")

# ---------- Estilo: tipografía, colores y componentes ----------
st.markdown(
    """
    <style>
    /* Paleta "Firenze": verde, amarillo, naranja, óxido y marrón.
       Para cambiar los colores de toda la app, edita solo este bloque. */
    :root {
        --vivo: #B34A29;          /* color principal (óxido) */
        --vivo-oscuro: #8D2D00;   /* color principal al pasar el mouse */
        --vivo-suave: #F9E6DC;    /* fondo suave del color principal */
        --tinta: #2B1A10;         /* texto principal */
        --gris: #7A6A5C;          /* texto secundario */
        --linea: #EADFC8;         /* bordes finos */
        --borde-boton: #DCCDB0;
        --fondo-suave: #F4EEDF;   /* celdas vacías, barras */
        --verde: #4A8C67;
        --verde-texto: #2F7050;
        --verde-suave: #DCEFE4;
        --amarillo-suave: #FFF3B8;
        --amarillo-texto: #8A6D00;
        --naranja: #FBA93B;
        --naranja-suave: #FFE9CC;
        --naranja-texto: #B45F00;
        --rojo-texto: #B34A29;
        --rojo-suave: #F8DDD2;
    }

    /* Tipografía de toda la app (los íconos de Streamlit quedan fuera) */
    .stApp *:not([data-testid="stIconMaterial"]) {
        font-family: "Times New Roman", Times, serif !important;
    }

    /* Se oculta el botón Deploy */
    .stAppDeployButton, [data-testid="stAppDeployButton"] {
        display: none;
    }

    /* ----- Encabezados ----- */
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
        letter-spacing: -0.03em;
        line-height: 1.05;
        color: var(--tinta);
        margin: 0.5rem 0 0.2rem 0;
    }
    .titulo-command span, .titulo-pagina span {
        color: var(--vivo);
    }
    .titulo-pagina {
        font-size: clamp(2rem, 8vw, 3.2rem);
        font-weight: 800;
        letter-spacing: -0.02em;
        line-height: 1.1;
        color: var(--tinta);
        margin: 0.4rem 0 0.3rem 0;
    }
    .subtitulo-command {
        font-size: 1.25rem;
        color: var(--gris);
        margin-bottom: 2rem;
    }
    .titulo-pagina + .subtitulo-command {
        font-size: 1.1rem;
        margin-bottom: 1.4rem;
    }

    /* ----- Tarjetas ----- */
    [class*="st-key-tarjeta_"] {
        background: #FFFFFF;
        border: 1px solid var(--linea);
        border-radius: 20px;
        padding: 1.3rem;
        box-shadow: 0 4px 18px rgba(43, 26, 16, 0.07);
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }
    [class*="st-key-tarjeta_"]:hover {
        transform: translateY(-4px);
        border-color: var(--vivo);
        box-shadow: 0 12px 28px rgba(179, 74, 41, 0.18);
    }
    .chip {
        width: 2.4rem;
        height: 2.4rem;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 0.95rem;
        margin-bottom: 0.8rem;
    }
    .chip-1 { background: var(--verde-suave); color: var(--verde-texto); }
    .chip-2 { background: var(--naranja-suave); color: var(--naranja-texto); }
    .chip-3 { background: var(--amarillo-suave); color: var(--amarillo-texto); }
    .chip-4 { background: var(--rojo-suave); color: var(--rojo-texto); }
    .tarjeta-titulo {
        font-size: 1.6rem;
        font-weight: 700;
        color: var(--tinta);
        line-height: 1.2;
    }
    .tarjeta-descripcion {
        color: var(--gris);
        font-size: 1rem;
        margin: 0.2rem 0 0.8rem 0;
    }
    .dato-grande {
        font-size: 2.4rem;
        font-weight: 800;
        color: var(--tinta);
        line-height: 1.1;
        margin: 0.1rem 0 0.9rem 0;
    }
    .dato-grande span {
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--gris);
    }
    .barra {
        height: 8px;
        background: var(--fondo-suave);
        border-radius: 999px;
        overflow: hidden;
        margin: 0.2rem 0 1rem 0;
    }
    .barra div {
        height: 100%;
        background: var(--vivo);
        border-radius: 999px;
    }

    /* ----- Botones ----- */
    .stButton > button {
        background: #FFFFFF;
        border: 1.5px solid var(--borde-boton);
        border-radius: 12px;
        padding: 0.55rem 1rem;
        transition: all 0.2s ease;
    }
    .stButton > button p {
        color: var(--tinta);
        font-weight: 600;
    }
    .stButton > button:hover {
        border-color: var(--vivo);
    }
    .stButton > button:hover p {
        color: var(--vivo);
    }
    /* Botón "Abrir" de las tarjetas: color principal */
    [class*="st-key-tarjeta_"] button {
        background: var(--vivo);
        border-color: var(--vivo);
    }
    [class*="st-key-tarjeta_"] button p {
        color: #FFFFFF;
    }
    [class*="st-key-tarjeta_"] button:hover {
        background: var(--vivo-oscuro);
        border-color: var(--vivo-oscuro);
    }
    [class*="st-key-tarjeta_"] button:hover p {
        color: #FFFFFF;
    }
    /* Botón + */
    .st-key-mas_paginas button {
        background: var(--vivo-suave);
        border: 2px dashed var(--vivo);
    }
    .st-key-mas_paginas button p {
        color: var(--vivo);
    }

    /* ----- Páginas interiores ----- */
    h1, h2, h3 {
        font-weight: 700;
        letter-spacing: -0.01em;
        color: var(--tinta);
    }
    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid var(--linea);
        border-radius: 16px;
        padding: 1rem 1.2rem;
    }

    /* Etiquetas de color (píldoras).
       Ojo: "pill-violeta" conserva su nombre pero usa el color principal. */
    .pill {
        display: inline-block;
        padding: 0.2rem 0.7rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 700;
        white-space: nowrap;
    }
    .pill-rojo { background: var(--rojo-suave); color: var(--rojo-texto); }
    .pill-ambar { background: var(--naranja-suave); color: var(--naranja-texto); }
    .pill-verde { background: var(--verde-suave); color: var(--verde-texto); }
    .pill-violeta { background: var(--vivo-suave); color: var(--vivo); }
    .pills { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 0.8rem; }

    /* Próximos vencimientos */
    .venc {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        background: #FFFFFF;
        border: 1px solid var(--linea);
        border-radius: 14px;
        padding: 0.8rem 1rem;
        margin-bottom: 0.5rem;
    }
    .venc-titulo { font-weight: 700; color: var(--tinta); }
    .venc-detalle { color: var(--gris); font-size: 0.9rem; }

    /* Racha: tarjeta principal */
    .hero {
        background: linear-gradient(135deg, #B34A29 0%, #E8862A 100%);
        border-radius: 24px;
        padding: 1.6rem 1.8rem;
        color: #FFFFFF;
        box-shadow: 0 14px 30px rgba(179, 74, 41, 0.28);
        margin-bottom: 1rem;
    }
    .hero-etiqueta {
        font-size: 0.9rem;
        font-weight: 700;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 0.12em;
    }
    .hero-numero {
        font-size: clamp(4.5rem, 20vw, 7rem);
        font-weight: 800;
        line-height: 1;
        margin: 0.3rem 0 0 0;
    }
    .hero-texto { font-size: 1.4rem; font-weight: 600; }
    .hero-pie { margin-top: 0.8rem; font-size: 1rem; opacity: 0.95; }

    /* Calendario del mes */
    .cal {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 6px;
        margin: 0.6rem 0 0.8rem 0;
    }
    .cal-nombre {
        text-align: center;
        font-size: 0.8rem;
        font-weight: 700;
        color: var(--gris);
    }
    .cal-dia {
        aspect-ratio: 1 / 1;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        background: var(--fondo-suave);
        color: var(--gris);
        font-size: 0.95rem;
    }
    .cal-fuera { background: transparent; }
    .cal-limpio { background: var(--verde-suave); color: var(--verde-texto); font-weight: 700; }
    .cal-incidente { background: var(--rojo-suave); color: var(--rojo-texto); font-weight: 700; }
    .cal-inicio { background: var(--naranja-suave); color: var(--naranja-texto); font-weight: 700; }
    .cal-hoy { outline: 2px solid var(--vivo); outline-offset: 1px; }
    .cal-titulo {
        text-align: center;
        font-weight: 700;
        font-size: 1.2rem;
        padding-top: 0.4rem;
    }
    .leyenda {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        font-size: 0.85rem;
        color: var(--gris);
        margin-bottom: 1rem;
    }
    .punto {
        display: inline-block;
        width: 0.7rem;
        height: 0.7rem;
        border-radius: 50%;
        margin-right: 0.35rem;
    }
    .punto-verde { background: var(--verde); }
    .punto-rojo { background: var(--rojo-texto); }
    .punto-violeta { background: var(--naranja); }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Archivos donde se guardan los datos ----------
CARPETA = Path(__file__).parent / "datos"
CARPETA.mkdir(exist_ok=True)

ARCHIVO_CARRERAS = CARPETA / "carreras.json"
ARCHIVO_PAGINAS = CARPETA / "paginas.json"
ARCHIVO_RACHA = CARPETA / "racha.json"
ARCHIVO_INCIDENTES = CARPETA / "incidentes.csv"
ARCHIVO_PESO = CARPETA / "peso.csv"
ARCHIVO_META_PESO = CARPETA / "peso_meta.json"

CARRERA_INICIAL = "Economía - UNLP"
ESTADOS_MATERIA = ["Pendiente", "Cursando", "Final pendiente", "Aprobada"]
HITOS = [1, 3, 7, 14, 30, 60, 100, 180, 365, 500, 730, 1000]
MESES = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
]


# =====================================================================
# COMPONENTES VISUALES REUTILIZABLES
# =====================================================================
def encabezado(pildora, titulo, subtitulo=""):
    """Encabezado de las páginas interiores: píldora + título grande + subtítulo."""
    sub = (
        f'<div class="subtitulo-command">{html.escape(subtitulo)}</div>'
        if subtitulo
        else ""
    )
    st.markdown(
        f'<div class="pildora">{html.escape(pildora)}</div>'
        f'<div class="titulo-pagina">{html.escape(titulo)}<span>.</span></div>'
        f"{sub}",
        unsafe_allow_html=True,
    )


def mostrar_tarjetas(tarjetas, prefijo):
    """
    Dibuja tarjetas de a dos por fila.
    Cada tarjeta es una tupla: (titulo, descripcion, destino, html_extra)
    """
    for i in range(0, len(tarjetas), 2):
        columnas = st.columns(2)
        for j, (columna, (titulo, descripcion, destino, extra)) in enumerate(
            zip(columnas, tarjetas[i : i + 2])
        ):
            numero = i + j + 1
            color = (numero - 1) % 4 + 1  # cada tarjeta toma un color distinto
            with columna.container(key=f"tarjeta_{prefijo}{numero}"):
                st.markdown(
                    f'<div class="chip chip-{color}">{numero:02d}</div>'
                    f'<div class="tarjeta-titulo">{html.escape(titulo)}</div>'
                    f'<div class="tarjeta-descripcion">{html.escape(descripcion)}</div>'
                    f"{extra}",
                    unsafe_allow_html=True,
                )
                st.button(
                    "Abrir", key=f"abrir_{prefijo}{numero}", width="stretch",
                    on_click=abrir, args=(destino,),
                )


# =====================================================================
# PÁGINAS CREADAS POR MÍ (botón +)
# Se guardan como un árbol: cada página tiene nombre, notas y "hijos"
# (las páginas que están dentro de ella).
# =====================================================================
def cargar_paginas():
    if ARCHIVO_PAGINAS.exists():
        return json.loads(ARCHIVO_PAGINAS.read_text(encoding="utf-8"))
    return []


def guardar_paginas(paginas):
    ARCHIVO_PAGINAS.write_text(
        json.dumps(paginas, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def buscar_pagina(paginas, id_pagina):
    """Busca una página por su id, también dentro de las páginas hijas."""
    for pagina in paginas:
        if pagina["id"] == id_pagina:
            return pagina
        encontrada = buscar_pagina(pagina["hijos"], id_pagina)
        if encontrada:
            return encontrada
    return None


def crear_pagina(id_padre, nombre):
    """Crea una página nueva. Si id_padre es None, queda en el inicio."""
    paginas = cargar_paginas()
    nueva = {"id": uuid.uuid4().hex[:8], "nombre": nombre, "notas": "", "hijos": []}
    if id_padre is None:
        paginas.append(nueva)
    else:
        buscar_pagina(paginas, id_padre)["hijos"].append(nueva)
    guardar_paginas(paginas)


@st.dialog("Nueva página")
def dialogo_nueva_pagina(id_padre):
    nombre = st.text_input("Nombre de la página")
    if st.button("Crear"):
        nombre = nombre.strip()
        if not nombre:
            st.warning("Escribe un nombre.")
        else:
            crear_pagina(id_padre, nombre)
            st.rerun()


# =====================================================================
# NAVEGACIÓN
# La "ruta" es la lista de páginas que fuiste abriendo, una dentro de otra.
# Ejemplo: ["inicio", "universidad", "carrera:Economía - UNLP"]
# La página que se muestra es siempre la última de la lista.
# =====================================================================
if "ruta" not in st.session_state:
    st.session_state.ruta = ["inicio"]


def abrir(pagina):
    """Abre una página nueva dentro de la actual."""
    st.session_state.ruta.append(pagina)


def volver():
    """Vuelve a la página anterior."""
    if len(st.session_state.ruta) > 1:
        st.session_state.ruta.pop()


def etiqueta(pagina):
    """Nombre bonito de cada página, para mostrar arriba."""
    nombres = {
        "inicio": "Command",
        "universidad": "Universidad",
        "salud": "Salud",
        "racha": "Días sin contaminación",
        "peso": "Peso",
    }
    if pagina.startswith("carrera:"):
        return pagina.split(":", 1)[1]
    if pagina.startswith("pag:"):
        encontrada = buscar_pagina(cargar_paginas(), pagina.split(":", 1)[1])
        return encontrada["nombre"] if encontrada else "Página"
    return nombres[pagina]


def barra_superior():
    """Botón de volver + camino por el que llegaste (Command › Universidad › ...)."""
    ruta = st.session_state.ruta
    if len(ruta) > 1:
        st.button("← Volver", on_click=volver)
        st.caption(" › ".join(etiqueta(p) for p in ruta))


# =====================================================================
# PÁGINA PRINCIPAL
# =====================================================================
def pagina_inicio():
    st.markdown(
        '<div class="pildora">Panel personal</div>'
        '<div class="titulo-command">Command<span>.</span></div>'
        '<div class="subtitulo-command">¿A dónde vamos hoy?</div>',
        unsafe_allow_html=True,
    )

    # Tarjetas: primero las fijas, después las que yo creé
    tarjetas = [
        ("Universidad", "Carreras, materias y tareas", "universidad", ""),
        ("Salud", "Días sin contaminación y peso", "salud", ""),
    ]
    for pagina in cargar_paginas():
        tarjetas.append((pagina["nombre"], "Página personal", f"pag:{pagina['id']}", ""))

    mostrar_tarjetas(tarjetas, "inicio_")

    # Botón + para agregar páginas nuevas
    if st.button(
        "Agregar página", key="mas_paginas", icon=":material/add:", width="stretch"
    ):
        dialogo_nueva_pagina(None)


def pagina_personalizada(id_pagina):
    """Página creada con el botón +: tiene notas y puede tener páginas dentro."""
    paginas = cargar_paginas()
    pagina = buscar_pagina(paginas, id_pagina)
    if pagina is None:
        st.warning("Esta página ya no existe.")
        return

    encabezado("Página personal", pagina["nombre"])

    notas = st.text_area(
        "Notas", value=pagina["notas"], height=200, key=f"notas_{id_pagina}"
    )
    if st.button("Guardar notas", key=f"guardar_notas_{id_pagina}"):
        pagina["notas"] = notas
        guardar_paginas(paginas)
        st.success("Guardado")

    if pagina["hijos"]:
        st.subheader("Páginas")
        for hijo in pagina["hijos"]:
            st.button(
                hijo["nombre"], key=f"abrir_hijo_{hijo['id']}", width="stretch",
                on_click=abrir, args=(f"pag:{hijo['id']}",),
            )

    if st.button(
        "Agregar página dentro de ésta", key=f"mas_{id_pagina}",
        icon=":material/add:", width="stretch",
    ):
        dialogo_nueva_pagina(id_pagina)


# =====================================================================
# UNIVERSIDAD  →  carreras  →  resumen / materias / tareas
# =====================================================================
def slug(texto):
    """Convierte un nombre en algo seguro para usar como nombre de archivo."""
    return re.sub(r"\W+", "_", texto.lower()).strip("_")


def archivo_tareas(carrera):
    return CARPETA / f"tareas_{slug(carrera)}.csv"


def archivo_materias(carrera):
    return CARPETA / f"materias_{slug(carrera)}.csv"


def archivo_ajustes(carrera):
    return CARPETA / f"ajustes_{slug(carrera)}.json"


def cargar_carreras():
    """Lee la lista de carreras. La primera vez crea 'Economía - UNLP'."""
    if ARCHIVO_CARRERAS.exists():
        return json.loads(ARCHIVO_CARRERAS.read_text(encoding="utf-8"))
    carreras = [CARRERA_INICIAL]
    guardar_carreras(carreras)
    return carreras


def guardar_carreras(carreras):
    ARCHIVO_CARRERAS.write_text(
        json.dumps(carreras, ensure_ascii=False), encoding="utf-8"
    )


def cargar_total(carrera):
    """Cantidad total de materias del plan de estudios (0 si no se indicó)."""
    archivo = archivo_ajustes(carrera)
    if archivo.exists():
        return int(json.loads(archivo.read_text(encoding="utf-8")).get("total_materias", 0))
    return 0


def guardar_total(carrera, total):
    archivo_ajustes(carrera).write_text(
        json.dumps({"total_materias": int(total)}), encoding="utf-8"
    )


def cargar_materias(carrera):
    archivo = archivo_materias(carrera)
    if archivo.exists():
        df = pd.read_csv(archivo)
        df["anio"] = pd.to_numeric(df["anio"], errors="coerce")
        df["nota"] = pd.to_numeric(df["nota"], errors="coerce")
        return df
    return pd.DataFrame(
        {
            "materia": pd.Series(dtype="str"),
            "anio": pd.Series(dtype="float"),
            "estado": pd.Series(dtype="str"),
            "nota": pd.Series(dtype="float"),
        }
    )


def estadisticas_carrera(carrera):
    """Números de resumen de una carrera: aprobadas, promedio, finales, total."""
    df = cargar_materias(carrera)
    aprobadas = df[df["estado"] == "Aprobada"]
    notas = aprobadas["nota"].dropna()
    return {
        "aprobadas": len(aprobadas),
        "promedio": float(notas.mean()) if len(notas) else None,
        "finales": int((df["estado"] == "Final pendiente").sum()),
        "cargadas": len(df),
        "total": cargar_total(carrera),
    }


def cargar_tareas(archivo):
    if archivo.exists():
        df = pd.read_csv(archivo)
        df["fecha_entrega"] = pd.to_datetime(df["fecha_entrega"]).dt.date
        df["hecha"] = df["hecha"].astype(bool)
        return df
    return pd.DataFrame(
        {
            "materia": pd.Series(dtype="str"),
            "tarea": pd.Series(dtype="str"),
            "fecha_entrega": pd.Series(dtype="object"),
            "hecha": pd.Series(dtype="bool"),
        }
    )


def texto_dias(dias):
    """'en 3 días', 'mañana', 'hoy', 'vencida hace 2 días'..."""
    if dias < 0:
        return f"vencida hace {-dias} " + ("día" if dias == -1 else "días")
    if dias == 0:
        return "hoy"
    if dias == 1:
        return "mañana"
    return f"en {dias} días"


def html_vencimientos(df_tareas, maximo=6):
    """Lista de próximos vencimientos, con color según la urgencia."""
    hoy = date.today()
    pendientes = []
    for _, fila in df_tareas.iterrows():
        if pd.isna(fila["fecha_entrega"]) or bool(fila["hecha"]):
            continue
        materia = "" if pd.isna(fila["materia"]) else str(fila["materia"])
        tarea = "Sin título" if pd.isna(fila["tarea"]) else str(fila["tarea"])
        pendientes.append((fila["fecha_entrega"], materia, tarea))
    pendientes.sort(key=lambda x: x[0])

    filas = ""
    for fecha, materia, tarea in pendientes[:maximo]:
        dias = (fecha - hoy).days
        if dias <= 7:
            clase = "pill-rojo"
        elif dias <= 14:
            clase = "pill-ambar"
        else:
            clase = "pill-verde"
        detalle = f"{fecha:%d/%m/%Y}"
        if materia:
            detalle = f"{html.escape(materia)} · {detalle}"
        filas += (
            '<div class="venc"><div>'
            f'<div class="venc-titulo">{html.escape(tarea)}</div>'
            f'<div class="venc-detalle">{detalle}</div></div>'
            f'<span class="pill {clase}">{texto_dias(dias)}</span></div>'
        )
    return filas


def eliminar_carrera(nombre):
    """Quita la carrera de la lista y borra sus materias, tareas y ajustes."""
    restantes = [c for c in cargar_carreras() if c != nombre]
    guardar_carreras(restantes)
    # Si otra carrera usa los mismos archivos (nombres casi iguales), no se borran
    if any(slug(c) == slug(nombre) for c in restantes):
        return
    for archivo in (archivo_materias(nombre), archivo_tareas(nombre), archivo_ajustes(nombre)):
        archivo.unlink(missing_ok=True)


def borrar_carrera_elegida():
    """Se ejecuta al pulsar 'Eliminar carrera'."""
    eliminar_carrera(st.session_state.carrera_a_borrar)
    st.session_state.pop("carrera_a_borrar", None)
    st.session_state.confirmar_borrar_carrera = False


def pagina_universidad():
    encabezado("Universidad", "Mis carreras", "Avance, notas y tareas de cada una")
    carreras = cargar_carreras()

    if not carreras:
        st.info("Todavía no tienes carreras. Crea una con el botón de abajo.")

    tarjetas = []
    for nombre in carreras:
        est = estadisticas_carrera(nombre)
        if est["total"]:
            porcentaje = min(est["aprobadas"] / est["total"] * 100, 100)
            descripcion = f"{est['aprobadas']} de {est['total']} materias aprobadas"
            extra = f'<div class="barra"><div style="width:{porcentaje:.0f}%"></div></div>'
        elif est["cargadas"]:
            descripcion = f"{est['aprobadas']} materias aprobadas"
            extra = ""
        else:
            descripcion = "Todavía sin materias cargadas"
            extra = ""
        tarjetas.append((nombre, descripcion, f"carrera:{nombre}", extra))

    mostrar_tarjetas(tarjetas, "uni_")

    with st.expander("Crear otra carrera", icon=":material/add:"):
        nueva = st.text_input("Nombre de la carrera (ej: Contador - UBA)")
        if st.button("Crear carrera"):
            nueva = nueva.strip()
            if not nueva:
                st.warning("Escribe un nombre.")
            elif nueva in carreras:
                st.warning("Ya existe una carrera con ese nombre.")
            else:
                carreras.append(nueva)
                guardar_carreras(carreras)
                st.rerun()

    if carreras:
        with st.expander("Eliminar una carrera", icon=":material/delete:"):
            st.selectbox("Carrera a eliminar", carreras, key="carrera_a_borrar")
            st.caption(
                "Se borran también sus materias, tareas y ajustes. No se puede deshacer."
            )
            confirmar = st.checkbox("Sí, quiero eliminarla", key="confirmar_borrar_carrera")
            st.button(
                "Eliminar carrera", disabled=not confirmar,
                on_click=borrar_carrera_elegida,
            )


def pagina_carrera(carrera):
    encabezado("Carrera", carrera, "Resumen, materias y tareas")
    tab_resumen, tab_materias, tab_tareas = st.tabs(["Resumen", "Materias", "Tareas"])

    # Primero se procesan Materias y Tareas (para guardar), y después se arma
    # el Resumen, así siempre muestra los datos más recientes.

    # ----- Pestaña Materias -----
    with tab_materias:
        st.write("Agrega filas con el botón + de la tabla. La nota va de 0 a 10.")
        materias = cargar_materias(carrera)
        editado = st.data_editor(
            materias,
            key=f"materias_{carrera}",
            num_rows="dynamic",
            width="stretch",
            hide_index=True,
            column_config={
                "materia": st.column_config.TextColumn("Materia"),
                "anio": st.column_config.NumberColumn(
                    "Año", min_value=1, max_value=8, step=1, format="%d"
                ),
                "estado": st.column_config.SelectboxColumn(
                    "Estado", options=ESTADOS_MATERIA, default="Cursando"
                ),
                "nota": st.column_config.NumberColumn(
                    "Nota", min_value=0, max_value=10, step=0.5, format="%.1f"
                ),
            },
        )
        if st.button("Guardar materias"):
            limpio = editado.dropna(subset=["materia"]).copy()
            limpio["estado"] = limpio["estado"].fillna("Pendiente")
            limpio.to_csv(archivo_materias(carrera), index=False)
            st.success("Guardado")

    # ----- Pestaña Tareas -----
    with tab_tareas:
        st.write("Marca ✔ cuando termines una tarea.")
        tareas = cargar_tareas(archivo_tareas(carrera))
        tareas_editadas = st.data_editor(
            tareas,
            key=f"tareas_{carrera}",
            num_rows="dynamic",
            width="stretch",
            hide_index=True,
            column_config={
                "materia": "Materia",
                "tarea": "Tarea / examen",
                "fecha_entrega": st.column_config.DateColumn("Fecha", format="DD/MM/YYYY"),
                "hecha": st.column_config.CheckboxColumn("Hecha"),
            },
        )
        if st.button("Guardar tareas"):
            tareas_editadas.to_csv(archivo_tareas(carrera), index=False)
            st.success("Guardado")

    # ----- Pestaña Resumen -----
    with tab_resumen:
        est = estadisticas_carrera(carrera)
        df_tareas = cargar_tareas(archivo_tareas(carrera))
        tareas_pendientes = int((~df_tareas["hecha"].fillna(False).astype(bool)).sum())

        col1, col2 = st.columns(2)
        col1.metric(
            "Promedio",
            f"{est['promedio']:.2f}" if est["promedio"] is not None else "—",
        )
        col2.metric(
            "Aprobadas",
            f"{est['aprobadas']} de {est['total']}" if est["total"] else str(est["aprobadas"]),
        )
        col3, col4 = st.columns(2)
        col3.metric("Finales pendientes", est["finales"])
        col4.metric("Tareas pendientes", tareas_pendientes)

        if est["total"]:
            avance = min(est["aprobadas"] / est["total"], 1.0)
            st.progress(avance, text=f"{avance * 100:.0f}% de la carrera")
        else:
            st.caption("Indica el total de materias de tu plan para ver el avance.")

        with st.expander("Total de materias del plan de estudios"):
            nuevo_total = st.number_input(
                "Total de materias", min_value=0, max_value=200,
                value=est["total"], step=1, key=f"total_{carrera}",
            )
            if nuevo_total != est["total"]:
                guardar_total(carrera, nuevo_total)
                st.rerun()

        st.subheader("Próximos vencimientos")
        filas = html_vencimientos(df_tareas)
        if filas:
            st.markdown(filas, unsafe_allow_html=True)
        else:
            st.caption("No hay entregas pendientes con fecha.")