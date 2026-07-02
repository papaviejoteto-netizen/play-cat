from machine import Pin, SPI
import time

# ==========================================
# 1. CONFIGURACIÓN DE PINES
# ==========================================
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

def iniciar_lora_receptor():
    rst.value(0)
    time.sleep_ms(20)
    rst.value(1)
    time.sleep_ms(20)
    
    chip_id = read_reg(0x42)
    if chip_id != 0x12:
        print(f"\n [ ERROR FÍSICO ] SPI roto. Reg 0x42 = {hex(chip_id)}")
        while True: time.sleep(1)
            
    print("[ OK ] SPI Sano. Configurando para MÁXIMO ALCANCE (SF12)...")
    
    write_reg(0x01, 0x00) # Sleep
    time.sleep_ms(10)
    write_reg(0x01, 0x80) # LoRa Sleep
    time.sleep_ms(10)
    write_reg(0x01, 0x81) # LoRa Standby
    time.sleep_ms(10)
    
    write_reg(0x06, 0x6C) # 433 MHz
    write_reg(0x07, 0x80)
    write_reg(0x08, 0x00)
    
    # === CONFIGURACIÓN DE RADIO (Sincronizado a SF12) ===
    write_reg(0x1D, 0x78) 
    write_reg(0x1E, 0xC4) 
    write_reg(0x26, 0x0C) # Optimización SF12
    
    write_reg(0x0E, 0x00) 
    write_reg(0x0F, 0x00) 
    
    write_reg(0x01, 0x85) # RxContinuous
    time.sleep_ms(100)    

# ==========================================
# 2. BUCLE PRINCIPAL
# ==========================================
print("--- Receptor Oficial (SF12 Ultra-Alcance) ---")
iniciar_lora_receptor()
print("[ OK ] Antena encendida. Escaneando...\n")

while True:
    flags = read_reg(0x12)
    
    if flags > 0:
        write_reg(0x12, 0xFF) 
        if flags & 0x40: 
            num_bytes = read_reg(0x13) 
            if num_bytes > 0 and num_bytes != 0x7F:
                current_addr = read_reg(0x10)
                write_reg(0x0D, current_addr)
                
                cs.value(0)
                spi.write(bytes([0x00 & 0x7F]))
                payload = spi.read(num_bytes)
                cs.value(1)
                
                try:
                    mensaje = payload.decode('utf-8').replace('\x00', '').strip()
                    if "," in mensaje:
                        print(f"\n ENLACE LOGRADO -> {mensaje}")
                        print("-" * 50)
                except: pass
    time.sleep_ms(50)