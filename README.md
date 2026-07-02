Partes basados en el proyecto de quarkus-super-heroes

[https://github.com/quarkusio/quarkus-super-heroes](https://github.com/quarkusio/quarkus-super-heroes)

```text
mi-proyecto-super-scale/
├── .gitignore
├── README.md
├── CHANGELOG.md
│
├── backend/                  <-- Proyecto Padre de Microservicios (Java)
│   ├── pom.xml               <-- POM Padre (gestiona versiones comunes)
│   ├── rest-heroes/          <-- Submódulo Quarkus (Héroes)
│   │   ├── pom.xml
│   │   └── src/
│   └── rest-villains/        <-- Submódulo Quarkus (Villanos)
│       ├── pom.xml
│       └── src/
│
├── hardware/                 <-- Todo lo relacionado con electrónica
│   ├── firmware-arduino/     <-- Código C/C++ (.ino) para tus placas/sensores
│   │   ├── firmware-arduino.ino
│   │   └── README.md         <-- Notas de diagramas, pines y librerías (ej. HX711)
│   └── schematics/           <-- Diagramas de conexión o PCB (Fritzing, KiCad)
│
└── infrastructure/           <-- Tus archivos de despliegue
    └── docker-compose.yml    <-- Postgres, brokers, etc.