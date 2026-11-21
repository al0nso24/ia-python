# ia-python

Asistente conversacional para terminal escrito en Python. Mantiene el
historial de la conversación durante la ejecución y utiliza la API de chat
de [OpenRouter](https://openrouter.ai/) para generar respuestas en español.

## Características

- Conversación interactiva desde la terminal.
- Respuestas en español mediante un modelo configurable.
- Historial de mensajes conservado mientras el programa está activo.
- Lectura segura de la clave API desde un archivo `.env`.
- Comandos de salida sencillos.

## Requisitos

- Python 3
- Conexión a Internet
- Una clave API de OpenRouter

## Instalación

1. Clona el repositorio y entra en su carpeta:

   ```powershell
   git clone https://github.com/al0nso24/ia-python.git
   cd ia-python
   ```

2. Crea y activa un entorno virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instala las dependencias:

   ```powershell
   python -m pip install requests python-dotenv
   ```

## Configuración

Crea un archivo `.env` en la raíz del proyecto:

```dotenv
API_KEY=tu_clave_de_openrouter
```

Puedes obtener la clave desde el panel de OpenRouter. No compartas el valor
de `API_KEY` ni lo subas a GitHub.

## Uso

Ejecuta el asistente:

```powershell
python agenteIA.py
```

Escribe tu pregunta después de `Tú:`. Para finalizar la sesión, escribe:

- `salir`
- `bye`
- `adiós`
- `adios`

Ejemplo:

```text
Tú: Explícame qué es una API
Asistente: Una API es...
Tú: salir
Nos vemos pronto :D
```

## Personalización

El modelo predeterminado está definido dentro de `agenteIA.py`:

```python
"model": "arcee-ai/trinity-large-preview:free"
```

Puedes reemplazarlo por otro identificador de modelo disponible en
OpenRouter. El programa habilita razonamiento ampliado mediante el
parámetro `reasoning`.

## Estructura del proyecto

```text
.
├── agenteIA.py   # Punto de entrada y lógica de conversación
└── README.md     # Documentación del proyecto
```

## Resolución de problemas

| Problema | Posible solución |
|---|---|
| `ModuleNotFoundError` | Activa el entorno virtual y ejecuta `python -m pip install requests python-dotenv`. |
| Error de autorización | Comprueba que `.env` contiene una clave válida en `API_KEY`. |
| No aparece una respuesta | Verifica tu conexión, el estado de la API de OpenRouter y el identificador del modelo. |

La conversación se conserva únicamente en memoria y se pierde al cerrar
el programa. No utiliza almacenamiento persistente ni base de datos.
