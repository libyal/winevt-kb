## vmbusres.dll

Path: %SystemRoot%\System32\vmbusres.dll

### 6.1.7600.16385, 6.1.7601.17514

Message identifier | Message string
--- | ---
0xc0050001 | HAL de PIC detectada. Para iniciar VMBus, debe actualizar el sistema para usar una HAL de APIC.\r\n
0xc0050002 | La partición primaria usa una versión distinta de VMBus. Debe instalar una versión de VMBus coincidente en esta instalación de invitado.\r\n
0xc0050003 | La partición secundaria %2 usa una versión distinta de VMBus (%3) que la primaria (%4). Debe instalar una versión de VMBus coincidente en esta instalación de invitado.\r\n
0xc0050004 | La partición secundaria %2 no proporciona la versión de VMBus. Debe instalar VMBus con la versión de protocolo %3 en esta instalación de invitado.\r\n
0xc0050005 | La partición secundaria %2 proporciona versiones de VMBus incorrectas demasiadas veces. No se registrarán los errores sucesivos para esa partición.\r\n

### 6.2.9200.16384, 6.3.9600.16384

Message identifier | Message string
--- | ---
0xc0050001 | Se detectó una capa de abstracción de hardware (HAL) de PIC en el sistema operativo invitado. Para ejecutarla con Hyper-V, el sistema operativo debe estar actualizado para usar una HAL de APIC.\r\n
0xc0050002 | Hyper-V está ejecutando una versión distinta de VMBus. Actualice los servicios de integración en el sistema operativo invitado para corregir este problema.\r\n
0xc0050003 | La máquina virtual %2 usa una versión distinta de VMBus (%3) que la versión esperada por Hyper-V (%4). Actualice los servicios de integración en el sistema operativo invitado de la máquina virtual para resolver este problema.\r\n
0xc0050004 | La máquina virtual %2 no proporcionó información de versión para VMBus. Esta versión de Hyper-V requiere VMBus con la versión de protocolo %3. Para instalar esta versión de VMBus, actualice los servicios de integración en el sistema operativo invitado\r\n
0xc0050005 | La máquina virtual %2 proporcionó información de versión incorrecta para VMBus demasiadas veces. La información de versión adicional no se registrará para esta máquina virtual.\r\n
