from machine import Pin, SPI
import time

# ==========================================
# 1. CONFIGURACIÓN DE PINES
# ==========================================
led = Pin(25, Pin.OUT)
cs = Pin(17, Pin.OUT, value=1)
rst = Pin(14, Pin.OUT, value=1)
spi = SPI(0, baudrate=500000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(19), miso=Pin(16))

def write_reg(reg, val):
    cs.value(0)
    spi.write(bytes([reg | 0x80, val]))
    cs.value(1)

def read_reg(reg):
    cs.value(0)
    spi.write(bytes([reg & 0x7F]))
    val = spi.read(1)[0]
    cs.value(1)
    return val

def iniciar_lora_433mhz_estricto():
    rst.value(0)
    time.sleep_ms(20)
    rst.value(1)
    time.sleep_ms(20)
    
    chip_id = read_reg(0x42)
    if chip_id != 0x12:
        print(f"\n❌ [ ERROR CRÍTICO ] SPI Emisor roto. Reg 0x42 = {hex(chip_id)}")
        while True:
            led.toggle()
            time.sleep_ms(100)
            
    print(f"\n[ OK ] SPI Sano. Configurado para MÁXIMO ALCANCE (SF12).")
    
    write_reg(0x01, 0x00) # Sleep FSK
    time.sleep_ms(10)
    write_reg(0x01, 0x80) # LoRa Sleep
    time.sleep_ms(10)
    write_reg(0x01, 0x81) # LoRa Standby
    time.sleep_ms(10)
    
    write_reg(0x06, 0x6C) # 433 MHz
    write_reg(0x07, 0x80)
    write_reg(0x08, 0x00)
    
    # === CONFIGURACIÓN DE PENETRACIÓN EXTREMA (SF12) ===
    write_reg(0x1D, 0x78) # BW=125kHz, Coding Rate=4/8
    write_reg(0x1E, 0xC4) # Spreading Factor=12, CRC Activado
    write_reg(0x26, 0x0C) # Low Data Rate Optimize (Vital para SF12)
    
    write_reg(0x09, 0xFF) # Potencia Max
    write_reg(0x0E, 0x00) 
    write_reg(0x0F, 0x00) 

def transmitir_lora(mensaje):
    write_reg(0x01, 0x81) # Standby
    write_reg(0x0D, 0x00) # Reset FIFO
    
    payload = mensaje.encode('utf-8')
    write_reg(0x22, len(payload))
    
    cs.value(0)
    spi.write(bytes([0x00 | 0x80]))
    spi.write(payload)
    cs.value(1)
    
    write_reg(0x01, 0x83) # TX
    
    timeout = 300 
    while timeout > 0:
        flags = read_reg(0x12)
        if flags & 0x08: # TxDone
            break
        time.sleep_ms(10)
        timeout -= 1
        
    write_reg(0x12, 0xFF)
    
    if timeout == 0:
        print("   |-- [ ADVERTENCIA ] Timeout. El chip no irradió.")
    else:
        print("   |-- [ LORAWAN ] Paquete enviado!")

# ==========================================
# 3. BUCLE PRINCIPAL
# ==========================================
latitud_base = 16.7230
longitud_base = -93.1015
paso = 0.0002 
ID_COLLAR = "PET_01"
contador_envios = 1

print("--- Emisor Homologado (SF12 Ultra-Alcance) ---")
iniciar_lora_433mhz_estricto()

while True:
    lat = latitud_base + (contador_envios * paso * 0.5)
    lon = longitud_base - (contador_envios * paso * 0.3)
    mensaje_gps = f"{ID_COLLAR},{contador_envios},{lat:.4f},{lon:.4f}"
    
    print(f"[ GPS ] Disparando Paquete #{contador_envios}...")
    transmitir_lora(mensaje_gps)
    
    led.toggle()
    contador_envios += 1
    time.sleep(5)