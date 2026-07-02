## [0.1.0-alpha] - 2026-07-01
### Added
- Integración de hardware: Script de prueba para Raspberry Pi Pico con LoRa y GPS.

### Changed / Noted (Notas de Desarrollo)
- **⚠️ Alerta de Hardware (GPS):** Se descarta el módulo GPS actual por falla física de fábrica (no fija satélites). Requiere reemplazo.
- **⚠️ Limitación de Alcance (LoRa):** La prueba de campo con la configuración actual solo alcanzó ~50 metros. Se requiere revisar el Spreading Factor (SF), ancho de banda y ganancia de la antena para la siguiente iteración.