# Coding Standards Lab Report

## Introduction

Los estándares de código son fundamentales en el desarrollo de software profesional, ya que garantizan consistencia, legibilidad y mantenibilidad del código. Para este laboratorio, elegí Flake8 como herramienta de análisis por las siguientes razones:

1. **Cumplimiento de PEP8**: Flake8 verifica el cumplimiento del estándar PEP8 de Python, que es ampliamente reconocido y adoptado en la comunidad.
2. **Integración con CI/CD**: Facilidad de integración con GitHub Actions para automatización.
3. **Reportes HTML**: A través de flake8-html, genera reportes visuales detallados y navegables.
4. **Extensibilidad**: Soporta plugins para análisis adicionales si se requieren.

## Herramientas utilizadas

- Flake8 (verificación de estándares PEP8)
- flake8-html (generación de reportes HTML)
- GitHub Actions (CI/CD, verificación automática)

## Repositorio

- URL: https://github.com/Tburgos11/Worshop2
- Branch: main

## Steps performed

1. Ran Flake8 on `student_original.py` and captured the errors.
2. Fixed the code and created `student_fixed.py`.
3. Ran Flake8 on the fixed code and compared results.

## Findings (before)

Se ejecutó `flake8` sobre `student_original.py`. Errores detectados (resumen):

```
c:\Users\Thomas Burgos\Documents\Worshop2\student_original.py:2:2: E111 indentation is not a multiple of 4
c:\Users\Thomas Burgos\Documents\Worshop2\student_original.py:2:19: E231 missing whitespace after ','
c:\Users\Thomas Burgos\Documents\Worshop2\student_original.py:2:22: E231 missing whitespace after ','
c:\Users\Thomas Burgos\Documents\Worshop2\student_original.py:3:3: E111 indentation is not a multiple of 4
c:\Users\Thomas Burgopos\Documents\Worshop2\student_original.py:3:10: E225 missing whitespace around operator
... (lista completa en el reporte HTML)
```

Se generó un reporte HTML en `flake8_report_before/index.html` y páginas individuales para el archivo:

`flake8_report_before/.Users.Thomas Burgos.Documents.Worshop2.student_original.report.html`

Resumen: el archivo original contenía múltiples problemas de formato (indentación, espacios alrededor de operadores, falta de líneas en blanco) que afectan la legibilidad y mantienen el proyecto fuera de PEP8.

## Desarrollo

### Instalación y configuración

1. Creación del entorno virtual e instalación de dependencias:
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Configuración de GitHub Actions:
   - Archivo: `.github/workflows/lint.yml`
   - Ejecuta Flake8 en cada pull request

### Análisis del código original

El código original (`student_original.py`) presentaba múltiples violaciones de PEP8:

1. **Problemas de indentación**:
   - No uso consistente de 4 espacios
   - Mezcla de tabulaciones y espacios

2. **Espaciado**:
   - Falta de espacios después de comas
   - Operadores sin espacios alrededor

3. **Estructura**:
   - Falta de líneas en blanco entre métodos
   - Falta de líneas después de definiciones de clase

4. **Nombrado**:
   - Clase en minúsculas (`class student`)
   - Métodos con CamelCase en lugar de snake_case

### Correcciones implementadas

Las principales correcciones en `student_fixed.py` incluyen:

1. **Estandarización de indentación**:
   - 4 espacios consistentes
   - Eliminación de tabulaciones

2. **Mejoras en el código**:
   - Validación de parámetros
   - Tipos explícitos (type hints)
   - Mensajes de error descriptivos

3. **Estructura mejorada**:
   - Espaciado correcto alrededor de operadores
   - Líneas en blanco entre métodos
   - Documentación de métodos

## Findings (after)

Se ejecutó `flake8` sobre `student_fixed.py`. No se reportaron errores por Flake8 en la ejecución actual.

Reporte HTML generado en `flake8_report_after/index.html`.

La versión corregida cumple con las reglas chequeadas por Flake8 (PEP8 relevantes) y elimina los problemas de estilo detectados en la versión original.

## Conclusión

El uso de herramientas automatizadas de verificación de estándares como Flake8 es fundamental para:

1. **Detección temprana**: Identificar problemas de estilo antes de que lleguen a producción.
2. **Consistencia**: Mantener un estilo uniforme en todo el código base.
3. **Productividad**: Automatizar la verificación ahorra tiempo en revisiones.
4. **Calidad**: Código más legible y mantenible.

## Recomendaciones

1. **Integración con IDE**:
   - Configurar Flake8 en Visual Studio Code
   - Habilitar formateo automático al guardar

2. **Proceso de desarrollo**:
   - Ejecutar Flake8 antes de cada commit
   - Usar pre-commit hooks para automatización

3. **Estándares de equipo**:
   - Documentar excepciones a PEP8 si son necesarias
   - Mantener archivo de configuración `.flake8` en el repo

4. **CI/CD**:
   - Mantener GitHub Actions para verificación continua
   - Considerar agregar más linters (pylint, black) según necesidad
