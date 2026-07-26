# Ajuste del modelo DenseNet169 para la clasificación de frutos de mango Kent

Repositorio de código y experimentos del artículo enviado al *Journal of Computer Science & Technology (JCS&T)*.

## Resumen
Ajuste del modelo **DenseNet169** mediante *transfer learning* para la clasificación binaria
(*Sano* / *Defectuoso*) de frutos de mango del cultivar **Kent** en la etapa de poscosecha,
siguiendo el marco **CRISP-ML(Q)**. Sobre el conjunto de prueba, el modelo seleccionado (EXP13)
alcanzó **exactitud 93,67 %, precisión 94,03 %, sensibilidad 93,67 % y F1-score 93,67 %**.

## Dataset
- Dataset del proyecto (Kaggle, versionado): https://www.kaggle.com/dsv/16370582
- Dataset público de origen (MangoFruitDDS): https://doi.org/10.17632/jvszp9cbpw.3

> El dataset NO se incluye en este repositorio; descárguelo desde Kaggle.

## Estructura del repositorio
```
ajusteModeloDenseNet169/
├── README.md
├── LICENSE
├── requirements.txt
├── notebooks/          # preprocesamiento y análisis exploratorio (EDA)
├── src/                # código fuente: funciones y utilidades
├── experimentos/       # registros de los 180 experimentos
├── configuraciones/    # configuraciones de hiperparámetros empleadas
└── resultados/         # métricas, matriz de confusión, Grad-CAM
```

## Requisitos del software
- Python 3.10
- TensorFlow 2.x / Keras
- Entorno: Google Colab (GPU NVIDIA T4, 15 GB VRAM)
- Roboflow (preprocesamiento y partición del dataset)
- Arquitectura base: DenseNet169 (pesos ImageNet)
- Semilla de reproducibilidad: `seed = 42`

## Instalación
```bash
git clone https://github.com/AjusteModeloDenseNet169/ajusteModeloDenseNet169.git
cd ajusteModeloDenseNet169
python -m venv venv
# Windows: venv\Scripts\activate   |   macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

## Ejecución
1. Descargar el dataset desde Kaggle y ubicarlo según se indique en los notebooks.
2. Ejecutar los notebooks de `notebooks/` (preprocesamiento y análisis exploratorio).
3. Ejecutar el entrenamiento (cabeza entrenable sobre la base DenseNet169 congelada).
4. Ejecutar la evaluación (métricas de prueba, matriz de confusión y Grad-CAM).

Fijar `seed = 42` (TensorFlow y NumPy) garantiza la reproducibilidad de los resultados.

## Licencia
Este proyecto se distribuye bajo la licencia MIT (ver el archivo `LICENSE`).

## Cómo citar
Rojas Cevallos, L. C.; Chamba Eras, L. A. *Ajuste del modelo DenseNet169 para la clasificación
de frutos de mango Kent.* Journal of Computer Science & Technology (JCS&T). [Año / DOI por asignar].

## Contacto
- Letty Cristina Rojas Cevallos — letty.rojas@unl.edu.ec — ORCID 0009-0007-5281-9391
- Luis Antonio Chamba Eras — lachamba@unl.edu.ec — ORCID 0000-0003-3069-9628
