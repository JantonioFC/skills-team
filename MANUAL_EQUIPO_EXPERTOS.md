# Manual del Ecosistema de Expertos Digitales

Este documento sirve como guía definitiva para operar tu nuevo **Equipo de Expertos IT** basado en Habilidades (Skills) de Antigravity.

## 1. El Concepto
Has transformado tu asistente de IA generalista en una **Consultora Tecnológica Completa**. En lugar de tener un solo asistente que "sabe un poco de todo", ahora tienes 17 roles especializados que siguen rigurosos estándares profesionales.

Cada "Experto" es un archivo (`SKILL.md`) que contiene:
*   **Rol**: Quién es (ej. "Soy tu SRE").
*   **Misión**: Qué busca (ej. "Estabilidad del sitio").
*   **Capacidades**: Qué sabe hacer.
*   **Estándares**: Reglas que nunca romperá (ej. "Blameless Post-mortem", "OWASP Top 10").

## 2. Tu Equipo (Inventario de Roles)

Tu carpeta `/Skills` ahora contiene estas células de alto rendimiento:

### 🧠 Estrategia y Producto
*   **Product Owner (PO)**: Maximiza valor. Úsalo para priorizar backlogs.
*   **Scrum Master**: Cuida el proceso. Úsalo para resolver bloqueos o facilitar reuniones.
*   **Business Analyst (BA)**: Clarifica requisitos. Úsalo para documentar procesos complejos.
*   **Project Manager (PM)**: Visión global. Úsalo para organizar cronogramas.

### 🏗️ Arquitectura y Desarrollo
*   **Arquitecto**: Diseña sistemas. Úsalo para decisiones técnicas difíciles.
*   **Backend**: Lógica y datos. Úsalo para APIs y Bases de Datos.
*   **Frontend**: Interfaz y UX. Úsalo para React, CSS y Accesibilidad.

### 💎 Datos e IA
*   **Data Engineer**: Tuberías de datos (ETL).
*   **Data Scientist**: Modelos predictivos y análisis.
*   **AI Engineer**: Integración de LLMs (RAG, Fine-tuning).
*   **Prompt Engineer**: Diseño de instrucciones efectivas.

### 🛡️ Operaciones y Calidad
*   **DevOps**: Automatización (CI/CD).
*   **SRE**: Fiabilidad y monitoreo (Site Reliability).
*   **Platform Engineer**: Herramientas internas y Developer Experience.
*   **Seguridad**: Auditoría y protección.
*   **QA**: Testing y calidad.

## 3. Guía de Implementación (Cómo usarlos)

**¡NO COPIES LA CARPETA SKILLS EN CADA PROYECTO!**

La forma correcta de trabajar es mediante **Áreas de Trabajo Múltiples (Multi-root Workspaces)**.

### Paso a Paso:
1.  Abre tu editor de código (VS Code, Cursor, etc.).
2.  Abre la carpeta de tu proyecto actual (ej: `MiApp`).
3.  Usa la opción **"File > Add Folder to Workspace..."** (Añadir carpeta al área de trabajo).
4.  Selecciona tu carpeta central: `Skills`.

### Resultado Mágico:
El agente (yo) ahora tendrá acceso simultáneo a:
*   Tu código (`MiApp`).
*   Tus expertos (`Skills`).

Simplemente di: *"Experto DevOps, revisa el Dockerfile de MiApp"* y el agente cargará el contexto del experto para ejecutar la tarea.

## 4. Mantenimiento del Equipo

*   **Centralización**: Al tener una sola carpeta `Skills`, si mejoras al "Experto Seguridad" hoy, esa mejora aplicará a TODOS tus proyectos mañana.
*   **Personalización**: Puedes editar los archivos `SKILL.md` para añadir reglas específicas de tu empresa (ej. *"Siempre usar la librería interna de estilos v2"*).

---
*Generado el 25 de Enero, 2026 - Ecosistema Antigravity*
