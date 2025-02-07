import streamlit as st
import pandas as pd
import io
from io import BytesIO
import requests
from PIL import Image
import base64

# Tokens: Aproximadamente 4.5 tokens por palabra en español
TOKENS_POR_PALABRA = 4.5
ruta_imagen = "https://i.ibb.co/S7Zz453q/Hi-dimen.jpg"


ETAPAS = [
    {
        'nombre': 'Análisis y Preparación Inicial',
        'roles': [
            {
                'rol': 'Soporte Técnico', 
                'tarifa_defecto': 9000, 
                'min_horas': 10, 
                'max_horas': 20,
                'actividades': [
                    'Relevamiento de infraestructura técnica',
                    'Análisis de compatibilidad de datos',
                    'Definición de alcance específico'
                ]
            },
            {
                'rol': 'Product Owner', 
                'tarifa_defecto': 10000, 
                'min_horas': 10, 
                'max_horas': 15,
                'actividades': [
                    'Definición de requerimientos',
                    'Priorización de funcionalidades',
                    'Validación de objetivos'
                ]
            },
            {
                'rol': 'Analista de Negocio', 
                'tarifa_defecto': 8000, 
                'min_horas': 10, 
                'max_horas': 15,
                'actividades': [
                    'Documentación de procesos',
                    'Análisis de impacto',
                    'Mapeo de flujos de trabajo'
                ]
            }
        ]
    },
    {
        'nombre': 'Configuración de Infraestructura',
        'roles': [
            {
                'rol': 'Administrador de Base de Datos', 
                'tarifa_defecto': 9000, 
                'min_horas': 30, 
                'max_horas': 50,
                'actividades': [
                    'Preparación de servidores',
                    'Configuración de VPN',
                    'Instalación de herramientas'
                ]
            },
            {
                'rol': 'DevOps Engineer', 
                'tarifa_defecto': 10000, 
                'min_horas': 20, 
                'max_horas': 30,
                'actividades': [
                    'Configuración de pipelines',
                    'Automatización de despliegues',
                    'Configuración de monitoreo'
                ]
            },
            {
                'rol': 'Especialista en Seguridad', 
                'tarifa_defecto': 10000, 
                'min_horas': 20, 
                'max_horas': 20,
                'actividades': [
                    'Implementación de protocolos de seguridad',
                    'Configuración de cifrado',
                    'Análisis de vulnerabilidades'
                ]
            }
        ]
    },
    {
        'nombre': 'Desarrollo de Módulos',
        'roles': [
            {
                'rol': 'Data Scientist', 
                'tarifa_defecto': 9000, 
                'min_horas': 100, 
                'max_horas': 140,
                'actividades': [
                    'Desarrollo de módulo Happiness Index',
                    'Implementación de modelo de Sentiment Analysis',
                    'Entrenamiento de modelos de IA Generativa Loope'
                ]
            },
            {
                'rol': 'Programador', 
                'tarifa_defecto': 10000, 
                'min_horas': 100, 
                'max_horas': 140,
                'actividades': [
                    'Implementación de componentes backend',
                    'Desarrollo de APIs',
                    'Integración de módulos'
                ]
            }
        ]
    },
    {
        'nombre': 'Integración y Pruebas',
        'roles': [
            {
                'rol': 'Programador', 
                'tarifa_defecto': 10000, 
                'min_horas': 50, 
                'max_horas': 70,
                'actividades': [
                    'Pruebas de integración',
                    'Corrección de errores',
                    'Optimización de rendimiento'
                ]
            },
            {
                'rol': 'Data Scientist', 
                'tarifa_defecto': 9000, 
                'min_horas': 50, 
                'max_horas': 70,
                'actividades': [
                    'Validación de modelos',
                    'Ajuste de precisión',
                    'Evaluación de resultados'
                ]
            }
        ]
    },
    {
        'nombre': 'Implementación y Capacitación',
        'roles': [
            {
                'rol': 'Líder de Proyecto', 
                'tarifa_defecto': 10000, 
                'min_horas': 20, 
                'max_horas': 40,
                'actividades': [
                    'Coordinación de despliegue',
                    'Gestión de stakeholders',
                    'Planificación de rollout'
                ]
            },
            {
                'rol': 'Capacitador', 
                'tarifa_defecto': 8000, 
                'min_horas': 20, 
                'max_horas': 40,
                'actividades': [
                    'Preparación de material de capacitación',
                    'Sesiones de entrenamiento',
                    'Documentación de usuario'
                ]
            },
            {
                'rol': 'Soporte Técnico', 
                'tarifa_defecto': 9000, 
                'min_horas': 20, 
                'max_horas': 20,
                'actividades': [
                    'Soporte inicial',
                    'Resolución de incidencias',
                    'Configuración de entorno'
                ]
            }
        ]
    },
    {
        'nombre': 'Ajustes y Estabilización',
        'roles': [
            {
                'rol': 'Data Scientist', 
                'tarifa_defecto': 9000, 
                'min_horas': 20, 
                'max_horas': 30,
                'actividades': [
                    'Afinamiento de modelos',
                    'Análisis de rendimiento',
                    'Mejora continua'
                ]
            },
            {
                'rol': 'Programador', 
                'tarifa_defecto': 10000, 
                'min_horas': 20, 
                'max_horas': 30,
                'actividades': [
                    'Correcciones finales',
                    'Optimización de código',
                    'Preparación de versión estable'
                ]
            }
        ]
    }
]

def calcular_tokens_por_comentario(palabras_por_comentario=50):
    return palabras_por_comentario * TOKENS_POR_PALABRA

def generar_interfaz_dimensionamiento():
    
    response = requests.get(ruta_imagen)


    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
    
        # Convertir la imagen a base64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
    
        # Mostrar la imagen en Streamlit
        #st.image(image, caption="Imagen cargada desde URL")
    else:
        st.error("No se pudo cargar la imagen desde la URL")
    
    # Crear el HTML para una imagen responsiva
    st.markdown(
        f"""
        <style>
        .responsive-img {{
            width: 35%;
            max-width: 500px;
            height: auto;
        }}
        </style>
        <img src="data:image/png;base64,{img_str}" class="responsive-img">
        """,
        unsafe_allow_html=True
        )
    #st.title('Despliegue HI Work')
    
    
    # Configuración de consumo de GenAI
    st.sidebar.header('Consumo de GenAI')
    comentarios_por_mes = st.sidebar.number_input(
        'Comentarios procesados por mes', 
        min_value=0, value=50000, step=100
    )
    costo_tokens = st.sidebar.number_input(
        'Costo por 1000 tokens ($)', 
        min_value=0.0, value=0.01, step=0.001, format='%f'
    )
    
    tokens_por_comentario = calcular_tokens_por_comentario()
    tokens_procesados = (comentarios_por_mes * tokens_por_comentario) / 1000
    costo_genai = tokens_procesados * costo_tokens
    
    st.sidebar.markdown(f"**Tokens por comentario:** {tokens_por_comentario:.2f}")
    st.sidebar.markdown(f"**Estimado Mensual GenAI:** ${costo_genai:.2f}")

    # Lista para almacenar los datos del Excel
    datos_excel = []
    # Interfaz de dimensionamiento
    for etapa in ETAPAS:
        st.header(etapa['nombre'])
        
        # Mostrar actividades
        with st.expander('Actividades'):
            for rol_data in etapa['roles']:  # Iteramos sobre todos los roles
                st.markdown(f"**{rol_data['rol']}**")  # Nombre del rol
                for actividad in rol_data['actividades']:
                    st.markdown(f"- {actividad}")
        
        for rol_data in etapa['roles']:
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.write(f"**{rol_data['rol']}**")
            
            with col2:
                tarifa = st.number_input(
                    'Tarifa/Hora', 
                    min_value=0, 
                    value=rol_data['tarifa_defecto'],
                    key=f"{etapa['nombre']}_{rol_data['rol']}_tarifa"
                )
            
            with col3:
                min_horas = st.number_input(
                    'Horas Min', 
                    min_value=0, 
                    value=rol_data['min_horas'],
                    key=f"{etapa['nombre']}_{rol_data['rol']}_min"
                )
                max_horas = st.number_input(
                    'Horas Max', 
                    min_value=0, 
                    value=rol_data['max_horas'],
                    key=f"{etapa['nombre']}_{rol_data['rol']}_max"
                )
            
            # Agregar los datos al Excel
            for actividad in rol_data['actividades']:
                datos_excel.append([etapa['nombre'], actividad, rol_data['rol'], f"{min_horas}-{max_horas}", tarifa])    
    
    # Crear DataFrame para exportar a Excel
    df_excel = pd.DataFrame(datos_excel, columns=["Etapa", "Actividades", "Rol", "Hs", "Costo-hs"])
    
    # Generar el archivo Excel en memoria
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df_excel.to_excel(writer, index=False, sheet_name="Dimensionamiento")
    output.seek(0)

    # Botón de descarga
    st.download_button(
        label="📥 Descargar Excel",
        data=output,
        file_name="dimensionamiento.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    
    # Generación de totalizador
    totales_por_rol, totales_generales = generar_totalizador(ETAPAS)              
    mostrar_totalizador(totales_por_rol, totales_generales, costo_genai)

  

def generar_totalizador(etapas):
    totales_por_rol = {}
    totales_generales = {
        'horas_min': 0,
        'horas_max': 0,
        'costo_min': 0,
        'costo_max': 0
    }

    for etapa in etapas:
        for rol_data in etapa['roles']:
            rol = rol_data['rol']
            tarifa = st.session_state.get(
                f"{etapa['nombre']}_{rol}_tarifa", 
                rol_data['tarifa_defecto']
            )
            min_horas = st.session_state.get(
                f"{etapa['nombre']}_{rol}_min", 
                rol_data['min_horas']
            )
            max_horas = st.session_state.get(
                f"{etapa['nombre']}_{rol}_max", 
                rol_data['max_horas']
            )

            if rol not in totales_por_rol:
                totales_por_rol[rol] = {
                    'tarifa': tarifa,
                    'horas_min': 0,
                    'horas_max': 0,
                    'costo_min': 0,
                    'costo_max': 0
                }

            totales_por_rol[rol]['horas_min'] += min_horas
            totales_por_rol[rol]['horas_max'] += max_horas
            totales_por_rol[rol]['costo_min'] += min_horas * tarifa
            totales_por_rol[rol]['costo_max'] += max_horas * tarifa

            totales_generales['horas_min'] += min_horas
            totales_generales['horas_max'] += max_horas
            totales_generales['costo_min'] += min_horas * tarifa
            totales_generales['costo_max'] += max_horas * tarifa

    return totales_por_rol, totales_generales

def mostrar_totalizador(totales_por_rol, totales_generales, costo_genai):
    st.header('Resumen General')

    df_totales = pd.DataFrame.from_dict(totales_por_rol, orient='index')
    df_totales.index.name = 'Rol'
    df_totales = df_totales.reset_index()

    st.dataframe(df_totales, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Totales Generales")
        st.markdown(f"**Horas Mínimas:** {totales_generales['horas_min']}")
        st.markdown(f"**Horas Máximas:** {totales_generales['horas_max']}")
        st.markdown(f"**Costo Mínimo:** ${totales_generales['costo_min']:,.2f}")
        st.markdown(f"**Costo Máximo:** ${totales_generales['costo_max']:,.2f}")

    with col2:
        st.markdown("### Costos Adicionales")
        st.markdown(f"**Estimado Mensual GenAI:** ${costo_genai:.2f}")

    costo_total_min = totales_generales['costo_min'] + costo_genai
    costo_total_max = totales_generales['costo_max'] + costo_genai

    st.markdown(
        f"""
        <div style="background-color: #E0F2F1; padding: 10px; border-radius: 5px;">
            <h3 style="text-align: center;">Costo Total del Proyecto</h3>
            <p style="text-align: center;"><strong>Mínimo:</strong> ${costo_total_min:,.2f}</p>
            <p style="text-align: center;"><strong>Máximo:</strong> ${costo_total_max:,.2f}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    generar_interfaz_dimensionamiento()

if __name__ == '__main__':
    main()
