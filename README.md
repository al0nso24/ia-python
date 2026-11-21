# ia-python

Asistente conversacional de terminal en español. El programa mantiene el historial de la conversación durante la ejecución y envía los mensajes a la API de chat de OpenRouter usando el modelo configurado en el código.

## Requisitos

- Python instalado. El repositorio no especifica una versión mínima.
- Una clave de API para utilizar el servicio de OpenRouter.

## Instalación

Desde la carpeta del proyecto, crea y activa un entorno virtual (opcional, pero recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias que utiliza el programa:

```powershell
python -m pip install requests python-dotenv
```

El repositorio no contiene un archivo de dependencias como `requirements.txt`; estos paquetes se identifican a partir de las importaciones de `agenteIA.py`.

## Configuración

Crea un archivo `.env` en la carpeta del proyecto y añade tu clave:

```dotenv
API_KEY=tu_clave_de_openrouter
```

`agenteIA.py` carga las variables de ese archivo mediante `python-dotenv` y utiliza `API_KEY` como credencial para las solicitudes a OpenRouter. No compartas ni subas el archivo `.env` al repositorio.

## Ejecución

```powershell
python agenteIA.py
```

Escribe un mensaje cuando aparezca `Tú:`. Para terminar, escribe `salir`, `bye`, `adiós` o `adios`.

## Estructura

```text
.
└── agenteIA.py   # Bucle de conversación y solicitudes a OpenRouter
```

El modelo configurado en el código es `arcee-ai/trinity-large-preview:free`. El programa conserva el historial en memoria mientras se ejecuta; no se configura almacenamiento persistente.
