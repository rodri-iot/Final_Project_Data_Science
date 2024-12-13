# Step 0: Importar librerias y modelos
# Librerías principales -------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Preprocesamiento y transformaciones ----------------------------------
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    FunctionTransformer, 
    OneHotEncoder, 
    StandardScaler
)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import PowerTransformer

# Modelos de Machine Learning ------------------------------------------
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from xgboost import XGBClassifier

# Métricas de evaluación ----------------------------------------------
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    recall_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# Búsqueda de hiperparámetros ------------------------------------------
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV

# Visualización interactiva --------------------------------------------
import plotly.express as px

# Manejo de datos externos ---------------------------------------------
import requests
from io import StringIO
import os
from PIL import Image

# Serialización del modelo ---------------------------------------------
from joblib import dump

# Streamlit ------------------------------------------------------------
import streamlit as st

# Cargar df_raw

# Obtener la ruta absoluta del directorio donde está el script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta absoluta al archivo CSV
data_path = os.path.join(BASE_DIR, "../data/raw_2/bank-full.csv")

# Intentar cargar el archivo CSV
try:
    df_raw = pd.read_csv(data_path, sep=';')
    print("Archivo cargado exitosamente.")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta: {data_path}")
except Exception as e:
    print(f"Ocurrió un error al cargar el archivo: {e}")

# Cargar df_clean
# Construir la ruta absoluta al archivo CSV
data_clean_path = os.path.join(BASE_DIR, "../data/processed/df_clean_bank.csv")

# Intentar cargar el archivo CSV
try:
    df_clean = pd.read_csv(data_clean_path, index_col=0)
    print("Archivo cargado exitosamente.")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en la ruta: {data_clean_path}")
except Exception as e:
    print(f"Ocurrió un error al cargar el archivo: {e}")

# EDA ------------------------------------------------------------------
df = df_clean.copy()
# Crear data set de entrenamiento y test
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)



# Configuración de la página -------------------------------------------
st.set_page_config(
    page_title="MKT-Bancario - ML",
    page_icon="📊",
    layout="wide"
    )

# Carátula principal
st.title("🚀 El Rescate de las Campañas Perdidas")

# Menú desplegable para carátula
with st.expander("Presentación"):
    st.markdown("""
        ### Proyecto Final - Bootcamp Data Science
        #### Autores: Alejandro Diaz y Rodrigo Pinedo
        **4Geeks Academy**
    """)

    # Construir la ruta absoluta del archivo de imagen
    image_path = os.path.join(BASE_DIR, "../streamlit/caratula.png")

    # Imagen principal
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img_resized = img.resize((256, 256))  # Redimensionar a 256x256
        st.image(img_resized, use_container_width=False, caption="Decisiones basadas en evidencias, impulsadas por datos.")
    else:
        st.error(f"No se encontró la imagen en la ruta: {image_path}")

    # Subtítulo motivacional
    st.markdown("""
    #### **¿Qué encontrarás en este proyecto?**
    - Exploración de datos reales de campañas bancarias.
    - Visualizaciones interactivas para entender patrones.
    - Modelos de Machine Learning que optimizan decisiones estratégicas.
    """)

    # Call to Action
    if st.button("Comienza tu viaje"):
        st.success("¡Navega por las secciones para descubrir más!")

# Sidebar para la navegación
st.sidebar.title("Navegación")
menu = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "Inicio",
        "El Rescate de las Campañas Perdidas",
        "La misión del rescate",
        "Desafíos abordados",
        "Herramientas y metodologías",
        "Hallazgos Clave",
        "Análisis Exploratorio de Datos (EDA)",
        "Resultados",
        "Puesta en acción"
    ]
)

# Sección: Inicio
if menu == "Inicio":
    st.title("🚀 El Rescate de las Campañas Perdidas")
    st.markdown("""
    # Inicio
    """)

    # Construir la ruta absoluta del archivo de imagen
    image_inicio = os.path.join(BASE_DIR, "../streamlit/inicio.png")
    
    # Crear las tres columnas
    col1, col2, col3 = st.columns([1, 1, 1])

    # Contenido de la columna izquierda
    with col1:
        st.markdown("#### Anteriormente")
        st.markdown("- Decisiones basadas en suposiciones")
        st.markdown("- Incertidumbre elevada")
        st.markdown("- Rendimientos ineficientes")
        st.markdown("")
        st.markdown("#### Limitaciones de anteriores")
        st.markdown("- Parece complicado")
        st.markdown("- Desconocimiento")

    # Contenido de la columna central (imagen)
    with col2:
        if os.path.exists(image_inicio):
            img = Image.open(image_inicio)
            img_resized = img.resize((256, 256))  # Redimensionar a 256x256
            st.image(img_resized, use_container_width=False)
        else:
            st.error(f"No se encontró la imagen en la ruta: {image_inicio}")
        st.markdown("#### Apoyo de herramientas tecnológicas")
        st.markdown("Decisiones basadas en evidencias, impulsadas por datos.")

    # Contenido de la columna derecha
    with col3:
        st.markdown("#### Apoyo de la Ciencia de Datos")
        st.markdown("- Decisiones basadas en evidencias")
        st.markdown("- Mayor ventaja competitiva")
        st.markdown("")
        st.markdown("")
        st.markdown("#### Ventajas")
        st.markdown("- Enfrentar el futuro con confianza")
        st.markdown("- Cambios estructurados")

    # Mensaje de bienvenida adicional
    st.markdown("#### Haz clic en el menú lateral para explorar las secciones.")


# Sección 1: El Rescate de las Campañas Perdidas
elif menu == "El Rescate de las Campañas Perdidas":
    st.title("1. El Rescate de las Campañas Perdidas")
    st.markdown("""
    ### El Problema
    *"El banco enfrenta el reto de mejorar el desempeño de sus campañas 
    de marketing telefónico, que actualmente tienen una baja tasa de éxito."*
    """)
    # Construir la ruta absoluta del archivo de imagen
    image_s_1 = os.path.join(BASE_DIR, "../streamlit/s_1.png")
    
    # Crear las tres columnas
    col1, col2 = st.columns([1, 1])

    # Contenido de la columna izquierda
    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")

        # Imagen gerente
        if os.path.exists(image_s_1):
            img = Image.open(image_s_1)
            img_resized = img.resize((256, 256))  # Redimensionar a 256x256
            st.image(img_resized, use_container_width=False)
        else:
            st.error(f"No se encontró la imagen en la ruta: {image_s_1}")

        st.markdown("""
                    - Solo el 11.7% de las campañas tienen éxito.
                    - Se evidencia que el dataset se encuentra desbalanceado.
        """)

    # Contenido de la columna central (imagen)
    with col2:
        # Conteo de valores de la variable objetivo
        target_counts = df_raw['y'].value_counts().reset_index()
        target_counts.columns = ['Target', 'Count']

        # Crear el gráfico interactivo con Plotly
        fig = px.pie(
            target_counts, 
            names='Target', 
            values='Count', 
            title='Distribución de la Variable Objetivo',
            color_discrete_map={'no': '#FF6F61', 'yes': '#6A89CC'}  # Mapear colores
        )

        # Ajustar tamaño de las fuentes
        fig.update_traces(textinfo='percent+label', textfont_size=12)

        # Mostrar en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("**Nota:** *Haz clic en el menú lateral para explorar las secciones.*")

# Sección 2: La Misión del Rescate
elif menu == "La misión del rescate":
    st.title("2. La Misión del Rescate")

    # Construir la ruta absoluta del archivo de imagen
    img_2_0 = os.path.join(BASE_DIR, "../streamlit/s_2.png")

    # Construir columnas
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("### **Objetivo:**")
        st.markdown("""
        Predecir cuando un cliente del banco realizará un depósito a plazo.

        A través de identificar patrones en los datos históricos para 
        optimizar las campañas y mejorar la tasa de éxito.
    """)
        
    with col2:

        # Imagen principal
        if os.path.exists(image_path):
            img = Image.open(img_2_0)
            img_resized = img.resize((256, 256))  # Redimensionar a 256x256
            st.image(img_resized, use_container_width=False)
        else:
            st.error(f"No se encontró la imagen en la ruta: {image_path}")
    
    st.markdown("**Nota:** *Haz clic en el menú lateral para explorar las secciones.*")

# Sección 3: Desafíos abordados
elif menu == "Desafíos abordados":
    st.title("3. Desafíos abordados")
    st.markdown("""
    El análisis afrontó desafíos interesantes para procesar los datos, permitiendo
    mejorar el poder predictivo de las características.
    """)
        # Construir columnas
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        # Crear tabla con las variables y su tipo de dato
        data_types = pd.DataFrame({
            'Tipo de Dato': df_raw.dtypes.astype(str)  # Convertir a string para visualización
        })

        # Mostrar la tabla en Streamlit
        st.write(data_types)
        
        
    with col2:
        st.markdown("#### Info dataset original")
        st.markdown("""
            - Dataset Original:
            - Registros: 45,211
            - Variables: 16 características
            - Meta: 1 objetivo a predecir (y)
        """)
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("#### Info dataset limpiol")
        st.markdown("""
            - Dataset Original:
            - Registros: 45,211
            - Variables: 16 características
            - Meta: 1 objetivo a predecir (y)
        """)

    with col3:
        # Crear tabla df_clean
        data_types2 = pd.DataFrame({
            'Tipo de Dato': df_clean.dtypes.astype(str)  # Convertir a string para visualización
        })

        # Mostrar la tabla en Streamlit
        st.write(data_types2)

    st.markdown("**Nota:** *Haz clic en el menú lateral para explorar las secciones.*")


# Sección 4: Herramientas y metodologías
elif menu == "Herramientas y metodologías":
    st.title("4. Herramientas y metodologías")
    st.markdown("Todo lo utilizado para el proyecto se describe a continuación:")
    # Crear columnas
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:    
        st.markdown("""
            **Herramientas:**
            - Pandas
            - Numpy
            - Seaborn
            - Matplotlib
            - Sklearn
            - Joblib
            - Python
            - Jupyter
            - Streamlit
        """)

    with col2:
        # Construir la ruta absoluta del archivo de imagen
        img_4_0 = os.path.join(BASE_DIR, "../streamlit/s_4.png")

        # Imagen principal
        if os.path.exists(image_path):
            img = Image.open(img_4_0)
            img_resized = img.resize((256, 256))  # Redimensionar a 256x256
            st.image(img_resized, use_container_width=False)
        else:
            st.error(f"No se encontró la imagen en la ruta: {image_path}")

    with col3:    
        st.markdown("""
            **Metodologias:**
            - Estadística descriptiva e inferencial
            - Análisis exploratorio de datos
            - Transformación de datos (log, Yeo-Johnson, clasificación y binarias)
            - Encodear características
            - Modelos de Machine Learning (Random Forest, XGBoost y LGBM)
            - Mejoramiento de hiperparametros de los modelos ML
            - Técnicas de evaluación de modelos ML
        """)

    st.markdown("**Nota:** *Haz clic en el menú lateral para explorar las secciones.*")


# Sección 5: Hallazgos Clave
elif menu == "Hallazgos Clave":
    st.title("5. Hallazgos Clave")
    st.markdown("""
    En este apartado explicaremos las características que tuvieron comportamientos a considerarse:  
    """)

    # Crear columnas Var_1
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("#### **Age**")
        st.markdown(""""
            Los datos mayores a 70 años son outliers que pueden 
            sesgar el análisis, por lo que los eliminamos para 
            garantizar un modelo más robusto.
        """)

    with col2:
        # Crear el boxplot usando Plotly Express
        fig = px.box(
            df_raw, 
            x='age', 
            title="Distribución de Edad de los Clientes",
            labels={'age': 'Edad'},  # Etiquetas personalizadas
            template="plotly_white",  # Tema visual limpio
            color_discrete_sequence=["#636EFA"]  # Color del boxplot
        )

        # Añadir anotaciones narrativas
        fig.update_layout(
            xaxis=dict(
                title="Edad de los Clientes",
                title_standoff=20  # Separación del título del eje X
            ),
            yaxis_title="",  # Eliminar etiquetas del eje Y
            annotations=[
                dict(
                    x=0.5, y=-0.3, xref="paper", yref="paper", showarrow=False,
                    text="Los outliers representan edades que se desvían significativamente del rango típico."
                )
            ],
            height=400,  # Ajustar altura del gráfico
            title_x=0  # Centrar el título
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    # Crear columnas Var_2
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:

        # Gráfico original
        fig_original = px.histogram(
            df_raw,
            x='balance',
            nbins=30,
            title="Distribución Original",
            labels={'balance': 'Balance'},
            color_discrete_sequence=['blue'],
            template='plotly_white'
        )
        fig_original.update_layout(title_x=0)

        # Gráfico transformado con Yeo-Johnson
        fig_transformed = px.histogram(
            df_clean,
            x='balance_yeojohnson',
            nbins=30,
            title="Distribución Transformada (Yeo-Johnson)",
            labels={'balance_yeojohnson': 'Balance Transformado (Yeo-Johnson)'},
            color_discrete_sequence=['orange'],
            template='plotly_white'
        )
        fig_transformed.update_layout(title_x=0)

        # Mostrar ambos gráficos en Streamlit        
        st.plotly_chart(fig_original, use_container_width=True)

    with col2:
        st.plotly_chart(fig_transformed, use_container_width=True)


    with col3:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("#### **Balance**")
        st.markdown(""""
            Presentaba una distribución sesgada con outliers
            extremos, lo que dificultaba el modelado. Aplicamos 
            la transformación Yeo-Johnson para normalizar los datos.
        """)

    # Crear columnas Var_3
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("#### **Campaign**")
        st.markdown("""
            Las campañas tenían una distribución altamente sesgada. 
            La transformación logarítmica permitió comprimir la 
            escala y mejorar la estabilidad del modelo.
        """)
    with col2:

        # Gráfico Original
        fig_original = px.histogram(
            df_raw,
            x='campaign',
            nbins=30,
            title="Distribución Original de Campaign",
            labels={'campaign': 'Número de Campañas'},
            color_discrete_sequence=['blue'],
            template='plotly_white'
        )
        fig_original.update_layout(title_x=0)

        # Gráfico Transformado (Log-Transform)
        fig_log_transform = px.histogram(
            df_clean,
            x='campaign_log',
            nbins=30,
            title="Distribución Transformada (Log-Transform)",
            labels={'campaign_log': 'Log Transform de Campañas'},
            color_discrete_sequence=['green'],
            template='plotly_white'
        )
        fig_log_transform.update_layout(title_x=0)

        # Mostrar gráficos lado a lado en Streamlit
        st.plotly_chart(fig_original, use_container_width=True)

    with col3:
            st.plotly_chart(fig_log_transform, use_container_width=True)


    # Crear columnas Var_4
    col1, col2 = st.columns([2, 1])

    with col1:
        # Crear el histograma usando Plotly Express
        fig = px.histogram(
            df_clean, 
            x='quarter', 
            title="Distribución de Trimestres",
            labels={'quarter': 'Trimestre'},  # Etiqueta personalizada para el eje X
            color_discrete_sequence=['#636EFA'],  # Color del gráfico
            template='plotly_white',  # Tema visual limpio
            text_auto=True  # Mostrar conteos encima de las barras
        )

        # Personalizar el diseño
        fig.update_layout(
            title_x=0,  # Título alineado a la izquierda
            xaxis_title="Trimestre",  # Etiqueta del eje X
            yaxis_title="Conteo",  # Etiqueta del eje Y
            bargap=0.2  # Espacio entre barras
        )

        # Mostrar en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("#### **Month**")
        st.markdown("""
            Agrupamos los meses en trimestres para simplificar el 
            análisis y capturar estacionalidad en las campañas.
        """)

    # Crear columnas Var_5
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("#### **Pdays**")
        st.markdown("""
            Convertimos pdays en una variable binaria (contactado/no 
            contactado) para simplificar el análisis y mejorar la 
            interpretabilidad.
        """)
    with col2:
        # Preparar los datos para el gráfico
        contact_counts = df_clean['pdays_tran'].value_counts().reset_index()
        contact_counts.columns = ['Contactado', 'Frecuencia']

        # Crear el gráfico de barras usando Plotly Express
        fig = px.bar(
            contact_counts,
            x='Contactado',
            y='Frecuencia',
            title='Distribución de Contactados y No Contactados',
            labels={'Contactado': 'Contactado (1) o No Contactado (0)', 'Frecuencia': 'Frecuencia'},  # Etiquetas personalizadas
            template='plotly_white',  # Tema visual limpio
            color_discrete_sequence=['blue', 'red'] 
        )

        # Personalizar el diseño
        fig.update_layout(
            title_x=0,  # Título alineado a la izquierda
            xaxis=dict(
                tickmode='array', 
                tickvals=[0, 1], 
                ticktext=['No Contactado (0)', 'Contactado (1)']  # Etiquetas personalizadas para el eje X
            ),
            bargap=0.2  # Espacio entre las barras
        )

        # Mostrar en Streamlit
        st.plotly_chart(fig, use_container_width=True)


# Sección 6: Análisis Exploratorio de Datos (EDA)
elif menu == "Análisis Exploratorio de Datos (EDA)":
    st.title("Análisis Exploratorio de Datos (EDA)")
    st.markdown("""
    Nuestro objetivo es transformar campañas ineficientes en estrategias optimizadas usando Ciencia de Datos:
    1. Identificar patrones clave en los datos.
    2. Segmentar clientes según su probabilidad de aceptación.
    3. Maximizar la tasa de éxito y reducir el costo.
    """)
    # Obtener la ruta absoluta del directorio donde está el script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta absoluta del archivo de imagen
    img_3_0 = os.path.join(BASE_DIR, "../streamlit/inicio.png")

    # Imagen principal
    if os.path.exists(image_path):
        img = Image.open(img_3_0)
        img_resized = img.resize((256, 256))  # Redimensionar a 256x256
        st.image(img_resized, use_container_width=False, caption="Decisiones basadas en evidencias, impulsadas por datos.")
    else:
        st.error(f"No se encontró la imagen en la ruta: {image_path}")
    st.markdown("### Haz clic en el menú lateral para explorar las secciones.")


# Sección 7: Resultados
elif menu == "Resultados":
    st.title("7. Resultados")
    st.markdown("""
        Entrenamos tres modelos de ML para elegir el que mejor rendimiento tiene:
        - Random Forest
        - XGBoost
        - LGBM
    """)

    # Crear columnas
    col1, col2 = st.columns([2, 1])    

    with col1:
        # Datos de la tabla
        data = {
            "Model": ["Random Forest", "XGBoost", "LightGBM"],
            "Accuracy": [0.840805, 0.838122, 0.833762],
            "F1-Score (Class 1)": [0.543297, 0.544368, 0.538055],
            "Recall (Class 1)": [0.841948, 0.859841, 0.860835],
        }

        df_eval = pd.DataFrame(data)

        # Crear la tabla con Plotly
        import plotly.graph_objects as go
        table_fig = go.Figure(data=[go.Table(
            header=dict(
                values=list(df_eval.columns),
                fill_color=["#d9ead3", "#fce5cd", "#cfe2f3", "#d9d2e9"],
                align="center",
                font=dict(size=14, color="black"),
            ),
            cells=dict(
                values=[df_eval[col] for col in df_eval.columns],
                fill_color="white",
                align="center",
                font=dict(size=12, color="black"),
                height=30  # Altura de las celdas
            ),
        )])

        # Ajustar altura y diseño general
        table_fig.update_layout(
            height=400,  # Altura total del gráfico
            margin=dict(l=0, r=0, t=10, b=10),  # Reducir márgenes para compactar
        )

        # Mostrar la tabla en Streamlit
        st.plotly_chart(table_fig)

    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("**Evaluación de los modelos de ML:**")
        st.markdown("""
            La métrica para determinar el mejor modelo a aplicar,
            es *Recall*. Debido a que nuestro dataset está desbalanceado.
        """)

    # Crear columnas
    col1, col2 = st.columns([1, 2])

    with col1:
        # Mostrar texto debajo de la gráfica
        st.markdown("""
            El modelo de clasificación predice con 86% de precisión si un cliente aceptará hacer el depósito a plazo fijo.
        """)
    
    with col2:
        # Crear el gráfico de líneas con Plotly
        df_melted = df_eval.melt(
            id_vars=["Model"], 
            value_vars=["Accuracy", "F1-Score (Class 1)", "Recall (Class 1)"],
            var_name="Metric", 
            value_name="Score"
        )
        line_fig = px.line(
            df_melted,
            x="Model", y="Score", color="Metric",
            title="Comparación de Modelos de ML",
            markers=True,
        )

        # Personalizar el diseño del gráfico
        line_fig.update_layout(
            title=dict(font=dict(size=18, family="Arial", color="black")),
            xaxis_title="Modelo",
            yaxis_title="Puntaje",
            legend_title="Métricas",
            margin=dict(l=0, r=0, t=50, b=10),  # Ajustar márgenes del gráfico
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(line_fig, use_container_width=True)


# Sección 8: Puesta en acción
elif menu == "Puesta en acción":
    st.title("8. Puesta en acción")
    
    # Crear columnas
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("""
        - El equipo de marketing podrá enfocar sus esfuerzos en clientes identificados como potenciales.
        - Gracias al proyecto el banco podrá utilizar sus recursos de marketing de manera eficiente.
        - El banco podrá tomar mejor decisiones con mayor confianza.
        """)

    with col2:
        # Construir la ruta absoluta del archivo de imagen
        img_8_0 = os.path.join(BASE_DIR, "../streamlit/s_8.png")

        # Imagen principal
        if os.path.exists(image_path):
            img = Image.open(img_8_0)
            img_resized = img.resize((256, 256))  # Redimensionar a 256x256
            st.image(img_resized, use_container_width=False)
        else:
            st.error(f"No se encontró la imagen en la ruta: {image_path}")
    st.markdown("**Nota:** *Haz clic en el menú lateral para explorar las secciones.*")

