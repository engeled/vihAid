<h1 align="center">VIHAID: Análisis de Datos Epidemiológicos</h1>

<p align="center">
  Análisis estadístico y visualización de datos sobre VIH/SIDA en Castilla y León (España) — Sistema de reportes interactivos en Python
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-blue">
  <img alt="Pandas" src="https://img.shields.io/badge/Pandas-Data%20Analysis-6f42c1">
  <img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-Visualizations-orange">
</p>

---

## Descripción del Proyecto

**VIHAID** es una aplicación de análisis epidemiológico que procesa y visualiza datos históricos de casos de VIH/SIDA registrados entre 1982 y 2022 en la comunidad autónoma de Castilla y León, España.

El sistema transforma datos crudos en información estadística interpretable mediante reportes gráficos que incluyen: distribución demográfica por sexo, análisis geográfico por provincias, tendencias temporales, promedios de edad por década y análisis de vías de transmisión.

> **Nota:** Este proyecto tiene fines exclusivamente educativos e informativos. No sustituye el asesoramiento médico profesional ni procedimientos de diagnóstico clínico.

---

## Marco Teórico

### Definiciones Epidemiológicas

**VIH (Virus de Inmunodeficiencia Humana)**  
Retrovirus que infecta células del sistema inmunológico, debilitando progresivamente las defensas del organismo contra infecciones y enfermedades.

**SIDA (Síndrome de Inmunodeficiencia Adquirida)**  
Etapa avanzada de la infección por VIH caracterizada por el deterioro significativo del sistema inmune y la aparición de infecciones oportunistas.

### Análisis de Datos en Salud Pública

El análisis epidemiológico de datos permite:
- Identificar tendencias temporales en la incidencia de casos
- Determinar distribuciones geográficas y detectar áreas de mayor prevalencia
- Caracterizar perfiles demográficos y grupos de riesgo
- Fundamentar estrategias de prevención y políticas de salud pública

### Metodología de Análisis

La aplicación procesa archivos CSV conteniendo datos estructurados y genera visualizaciones estadísticas utilizando:
- **Gráficos circulares (pie charts)**: Para representar proporciones y distribuciones porcentuales
- **Gráficos de barras**: Para comparaciones categóricas entre provincias y grupos
- **Gráficos de líneas**: Para análisis de series temporales y tendencias

---

## Funcionalidades del Sistema

<table><tr><td>
<img width="857" height="180" alt="Menú principal" src="https://github.com/user-attachments/assets/67cf9203-bcc7-47d5-97f7-c794f1d157ab" />
</td></tr></table>

El programa presenta una interfaz de menú interactivo que permite generar los siguientes reportes estadísticos:

<table><tr><td>
<img width="767" height="202" alt="Opciones de reportes" src="https://github.com/user-attachments/assets/b0f62021-e762-45bf-be1e-284c08928453" />
</td></tr></table>

---

## Reportes Estadísticos

### Reporte 1: Distribución por Sexo
Análisis porcentual de casos discriminados por sexo biológico mediante representación circular.

<table><tr><td>
<img width="1366" height="823" alt="Distribución por sexo" src="https://github.com/user-attachments/assets/97734f48-1a8e-4cb2-8355-76d6bd533369" />
</td></tr></table>

### Reporte 2: Análisis Geográfico Provincial
Cuantificación de casos por provincia con identificación de la región con mayor incidencia.

<table><tr><td>
<img width="1596" height="838" alt="Casos por provincia" src="https://github.com/user-attachments/assets/59ad9e8f-5cfb-4625-9886-a2f45785a5da" />
</td></tr></table>

### Reporte 3: Tendencias Temporales
Serie temporal que muestra la evolución anual de casos en el período 2000-2022.

<table><tr><td>
<img width="1605" height="824" alt="Tendencia anual" src="https://github.com/user-attachments/assets/ec791a72-2589-4393-96f2-5d7289b63647" />
</td></tr></table>

### Reporte 4: Edad Promedio por Década
Análisis longitudinal de la edad media de diagnóstico agrupada por períodos decenales.

<table><tr><td>
<img width="1562" height="865" alt="Edad promedio" src="https://github.com/user-attachments/assets/7cf883a1-d21c-485f-bcdd-2be48bb72b75" />
</td></tr></table>

### Reporte 5: Análisis de Vías de Transmisión
Frecuencia de grupos de riesgo según clasificación codificada del dataset.

<table><tr><td>
<img width="1636" height="942" alt="Grupos de riesgo" src="https://github.com/user-attachments/assets/0f991e38-5486-4250-b3b2-59012f53c802" />
</td></tr></table>

---

## Aplicaciones en Salud Pública

Este tipo de análisis epidemiológico tiene aplicaciones prácticas en:

**Diseño de Intervenciones Preventivas**  
La identificación de tendencias permite fundamentar campañas educativas y programas de prevención dirigidos.

**Planificación de Recursos Sanitarios**  
El análisis geográfico facilita la asignación eficiente de centros de diagnóstico, recursos terapéuticos y personal especializado en áreas de mayor prevalencia.

**Vigilancia Epidemiológica**  
Los perfiles demográficos y temporales apoyan sistemas de alerta temprana y formulación de políticas de salud pública.

**Investigación y Reporte Científico**  
La transformación de datos crudos en indicadores estadísticos estandarizados facilita la comunicación científica y la toma de decisiones basada en evidencia.

---

## Requisitos Técnicos

### Dependencias

- Python 3.x
- Bibliotecas necesarias:
  - `pandas` (análisis y manipulación de datos)
  - `matplotlib` (generación de visualizaciones)

### Instalación
```bash
pip install pandas matplotlib
```

---

## Licencia

Proyecto desarrollado con fines académicos y de investigación educativa.

---


**Curso:** Programación Orientado a Objetos         
**Grupo:** #         
**Ciclo:** 2023-2      
**Desarrollado durante:** Ago 2023 - Nov 2023
