# Pruebas con LLama 3.2 Vision

Este proyecto tiene como objetivo probar el modelo LLama 3.2 Vision, permitiendo a los usuarios analizar imágenes y generar respuestas basadas en la API de Groq. El propósito es facilitar la implementación y prueba de modelos de visión con distintas configuraciones y niveles de consumo de tokens.

## Créditos

Este proyecto fue desarrollado por [Tech-Watt](https://github.com/Tech-Watt), con el fin de proporcionar una guía sencilla para la configuración y uso de LLama 3.2 Vision.

## Instalación

#### Clonación del repositorio

Clona el repositorio y accede a la carpeta del proyecto.

Aquí tienes un ejemplo de los comandos que realizarías en una terminal:

```bash
git clone https://github.com/Tech-Watt/How-to-setup-LLAMA3.2.git
```

Por otro lado, si usas un software externo, este es el enlace del repositorio:\
[https://github.com/Tech-Watt/How-to-setup-LLAMA3.2.git](https://github.com/Tech-Watt/How-to-setup-LLAMA3.2.git)

#### Creación del entorno virtual

Se recomienda crear un entorno virtual antes de correr el programa de pruebas.

Para ello, sigue los siguientes pasos según tu sistema operativo:

- **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

- **Linux / macOS**:

```bash
python3 -m venv venv
source venv/bin/activate
```

Luego, instala las dependencias dentro del entorno virtual:

```bash
pip install -r requirements.txt
```

#### Cuenta Groq y API-key

Para obtener la clave de acceso al API, gratuita al momento de esta prueba en la siguiente web:

[https://groq.com/](https://groq.com/)

Una vez registrado, debes ir a la sección Developers y luego cliquear en Free API Key.

Eso te redireccionará a [https://console.groq.com/keys](https://console.groq.com/keys)

Dentro de esa web, buscas la seccion API Keys y Crear API Key.

Teniendo su API Key, debes copiarla y pegarla en un nuevo archivo .env que debes crear en el directorio principal del repositorio clonado, de la siguiente forma:

```env
grok_key = tu-api-key
api_key = tu-api-key
```

Una vez hayas introducido tus claves, deberías poder el programa de pruebas sin problemas.

## Uso

Para utilizar este pequeño programa de prueba, debes cambiar el nombre del image\_path, por la imagen que quieras analizar.

Por otro lado, para cambiar el input, debes cambiar el texto que se enviará a través de la API, en la variable "text".

Una vez hecho eso, solo basta con ejecutar el modelo con el siguiente comando:

```bash
python main.py
```

Lo que resultará en una respuesta por parte del modelo.

## Modelos disponibles

Existen dos modelos disponibles que puedes utilizar dependiendo de tus necesidades:

```python
# Modelo por defecto (menor costo de tokens)
completion = client.chat.completions.create(
    # Modelo por defecto (menor costo de tokens)
    model="llama-3.2-11b-vision-preview",
    # Modelo de mayor capacidad (mayor costo de tokens)
    # model="llama-3.2-90b-vision-preview",
    ... # Otros parámetros necesarios
)
```

El modelo `llama-3.2-11b-vision-preview` es más eficiente en términos de consumo de tokens, mientras que `llama-3.2-90b-vision-preview` ofrece mejor rendimiento a cambio de un mayor costo en tokens.

