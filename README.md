# Proyecto: API para Migración de Datos y Visualización con Power BI

Este repositorio contiene una solución completa que incluye una API desarrollada en **Flask** para la migración de datos desde archivos **CSV** hacia una base de datos **MySQL**. Además, se crearon consultas SQL para el análisis de los datos y un **dashboard interactivo en Power BI** para la visualización de la información.

---

## Características Principales
1. **Desarrollo de una API RESTful**:
   - La API permite la subida de archivos CSV mediante una ruta POST.
   - Se migran y estructuran los datos en una base de datos MySQL.
   - Se incluye un método para inicializar la base de datos y procesar los archivos.

2. **Estructura de la Base de Datos**:
   - Se migraron las siguientes tablas:
     - `challenges` - Contiene información de los retos.
     - `profiles` y `profiles___hoja_1` - Datos de perfiles de usuarios.
     - `resumes` y `resumes___resumes` - Contiene información de videos subidos por los usuarios.
     - `users` y `users___users` - Datos generales de usuarios.

3. **Consultas SQL**:
   - Query 1: Número de retos creados en los últimos 3 meses con estado "published".
   - Query 2: Lista de usuarios con el objetivo *be_discovered* y videos válidos subidos en los últimos 7 meses.
   - Query 3: Top 3 usuarios con el mayor número de vistas en sus perfiles.

4. **Dashboard en Power BI**:
   - Se conectó la base de datos MySQL a Power BI.
   - Se generaron visualizaciones gráficas para responder a las consultas anteriores:
     - Número de retos publicados por fecha y objetivo.
     - Proporción de usuarios con videos subidos (objetivo: *be_discovered*).
     - Top 3 usuarios con más vistas en sus perfiles.
