## Hardware

Esta carpeta contiene los scripts en MicroPython para la Raspberry Pi Pico orientados a pruebas con módulos LoRa en 433 MHz.

### Archivos
- `emisor.py`: transmite paquetes de prueba con identificador, contador y coordenadas simuladas.
- `receptor.py`: escucha los paquetes recibidos y valida el contenido del mensaje.

### Requisitos
- Raspberry Pi Pico con MicroPython.
- Módulo LoRa en 433 MHz.
- Conexión SPI correcta entre la Pico y el módulo.

### Uso
- Cargar `emisor.py` en la Pico emisora.
- Cargar `receptor.py` en la Pico receptora.
- Verificar que ambos lados usen la misma configuración de radio.

### Nota
El historial de cambios, correcciones y observaciones de pruebas se mantiene en `CHANGELOG.md`.
