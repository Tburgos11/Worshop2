# Coding Standards Lab Report

## Introduction

(Write a short intro about code standards and tool choice)

## Tool used

- Flake8 (+ flake8-html for HTML reports)

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

## Changes made

(Show key diffs and explanation)

## Findings (after)

Se ejecutó `flake8` sobre `student_fixed.py`. No se reportaron errores por Flake8 en la ejecución actual.

Reporte HTML generado en `flake8_report_after/index.html`.

Conclusión: la versión corregida cumple con las reglas chequeadas por Flake8 (PEP8 relevantes) y elimina los problemas de estilo detectados en la versión original.

## Conclusion

(Lessons learned and recommendations)
