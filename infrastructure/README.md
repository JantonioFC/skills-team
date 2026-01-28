# Infraestructura y Herramientas (MCP)

Esta carpeta actúa como la "Sala de Máquinas" del Equipo de Expertos. Aquí residen los servidores del **Model Context Protocol (MCP)**, scripts compartidos y herramientas de infraestructura que dan superpoderes a los Agentes.

## Estructura

- **`mcp-servers/`**: Contiene los servidores MCP que exponen recursos y herramientas a los agentes.
    - *Ejemplo*: Conectores a bases de datos, herramientas de sistema, integraciones con APIs.
- **`scripts/`**: Scripts de utilidad general compartidos por múltiples expertos.

## Filosofía

Mientras que las carpetas de `experto-*` contienen el "cerebro" (prompts, instrucciones, roles), esta carpeta contiene el "cuerpo" (herramientas ejecutables).
