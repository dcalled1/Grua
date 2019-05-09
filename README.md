# Controlador para grúa

El proyecto pretende ofrecer una interfaz para el manejo de una grúa de 3 estaciones presente en el Laboratorio De Telemática de la [Universidad EAFIT](http://www.eafit.edu.co/).

## Comenzando 🚀

Clone o descargue el repositorio para continuar.


### Pre-requisitos 📋

#### Hardware
- [Arduino Mega 2560](https://store.arduino.cc/usa/mega-2560-r3).

#### Software
- [IDE de Arduino](https://www.arduino.cc/en/Main/Software).
- [Python 3 (versión sugerida: 3.7.3)](https://www.python.org/downloads/). Para acceder a una guía detallada de cómo descargar e instalar Python, haga click [aquí](https://es.wikihow.com/instalar-Python).
- La librería pySerial (para comunicación Serial) para Python. Para instalarla debe ejecutar `pip install pyserial` (o `pip install --user pyserial` en caso de tener Python instalado localmente) en su terminal de comandos (recordar que debe tener Python instalado y agregado al PATH).

### Instalación 🔧

1. Abra el archivo [ControladorGrua.ino](https://github.com/dcalled1/Grua/blob/master/ControladorGrua/ControladorGrua.ino) con el IDE de Arduino. Luego, en Herramientas, seleccione la placa `Arduino/Genuino Mega or Mega 2560`.
2. Conecte su Arduino mediante el puerto USB, y posteriormente, conecte y configure los pines del Arduino para que concidan con los de la Grúa.
3. Nuevamente en Herramientas, seleccione el puerto que le corresponde a su placa. Tenga en cuenta cuál puerto escogió, más adelante se utilizará.
![Selección de puerto](https://aprendiendoarduino.files.wordpress.com/2017/05/puerto_arduino1.png)
4. Compile y suba el código a su Arduino. Ya puede cerrar el IDE de Arduino.
Si la grúa esta encendida y se mueve hacia la derecha y luego hacia la izquierda, significa que vamos bien.
5. Abra el archivo [InterfazGrua.py](https://github.com/dcalled1/Grua/blob/master/InterfazGrua.py) en su editor de código o IDE favorito, lueg, en la línea 7, cambie `'COM7'` por el código del puerto que usted identificó en en paso 3 (Para el ejemplo, la línea debería quedar `port = 'COM4'`).
6. Ejecute el programa de la interfaz escribiendo en su terminal `python InterfazGrua.py` (o un IDE que ejecute código en Python, si lo dispone).

¡Listo!, ya puede probar su grúa.

**Nota:** Al momento de ejecutar el programa de Python, es recomendable NO tener abierto el IDE de Arduino o cualquier otro programa que utilice los puertos seriales.

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Deployment 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS


## Autores ✒️

* **David Calle Daza** - *201710031010* - [dcalled1](https://github.com/dcalled1)
* **Felipe Ríos** - *código* - [friosl](https://github.com/friosl)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.

---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊