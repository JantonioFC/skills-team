---
name: Creador de Habilidades
description: Asistente para generar, estructurar y validar nuevas habilidades (skills).
---

# Creador de Habilidades

Esta habilidad actúa como un "Meta-Agente" diseñado para ayudarte a crear nuevas habilidades de manera consistente y correcta, siguiendo los estándares de Antigravity y Awesome Skills.

## Cómo Usarme

Cuando quieras crear una nueva habilidad, simplemente pídemelo en lenguaje natural. Yo me encargaré de guiarte o de realizar las acciones por ti.

### Flujo de Creación Estándar

1.  **Identificación**: Analizaré tu solicitud para determinar:
    *   **Nombre del Directorio**: `kebab-case` (ej: `analisis-de-datos`).
    *   **Nombre de la Habilidad**: Título legible (ej: "Análisis de Datos").
    *   **Descripción**: Resumen de una línea para el frontmatter.
    *   **Instrucciones**: El contenido detallado del prompt.

2.  **Generación de Archivos**:
    Crearé la siguiente estructura en tu directorio de skills:
    ```text
    /tu-directorio-de-skills/
    └── nombre-del-directorio/
        └── SKILL.md
    ```

3.  **Formato SKILL.md**:
    Me aseguraré de que el archivo `SKILL.md` tenga el siguiente formato obligatorio:
    ```markdown
    ---
    name: Nombre de la Habilidad
    description: Descripción breve de la habilidad.
    ---
    
    # Nombre de la Habilidad
    
    [Instrucciones detalladas, ejemplos y reglas aquí]
    ```

### Herramientas de Validación

He incluido un script de validación extraído de *Antigravity Awesome Skills* para asegurar que tus habilidades funcionen correctamente.

*   **Ubicación**: `scripts/validate_skills.py`
*   **Ejecución**: Puedes pedirme que valide tus skills ejecutando este script.

## Referencias

Esta habilidad se basa en las mejores prácticas documentadas en:
*   [Antigravity Docs](https://antigravity.google/docs/skills)
*   [Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills)
