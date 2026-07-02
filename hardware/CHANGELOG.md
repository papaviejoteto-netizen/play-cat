## [0.1.1-alpha] - 2026-07-01
### Changed
- Se corrigieron detalles en la lógica de transmisión y recepción para estabilizar la comunicación entre la Pico y el módulo LoRa.
- Se ajustó la configuración de radio para trabajar con `Spread Factor SF12`, priorizando el mayor alcance posible sobre la velocidad de transmisión.
- Se mantuvo la configuración en 433 MHz con parámetros pensados para enlaces de largo alcance.

### Noted
- El código está preparado para pruebas de campo con MicroPython en Raspberry Pi Pico, pero esta versión aún no ha sido validada en campo.
- El GPS usado en pruebas previas sigue marcado como hardware con falla física y debe reemplazarse si se retoman lecturas reales.
- Si el enlace no responde, revisar cableado SPI, alimentación, antena y coincidencia exacta de parámetros entre emisor y receptor.

## [0.1.0-alpha] - 2026-07-01
### Added
- Integración de hardware: Script de prueba para Raspberry Pi Pico con LoRa y GPS.

### Noted
- **⚠️ Alerta de Hardware (GPS):** Se descarta el módulo GPS actual por falla física de fábrica (no fija satélites). Requiere reemplazo.
- **⚠️ Limitación de Alcance (LoRa):** La prueba de campo con la configuración inicial solo alcanzó ~50 metros. Se dejó pendiente revisar el Spreading Factor (SF), ancho de banda y ganancia de la antena para la siguiente iteración.