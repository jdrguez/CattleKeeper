# Configuración del Entorno de Trabajo en Django

# Importante !!! Todo dentro de la carpeta backend


## 1. Instalación de Python

Asegúrate de tener Python instalado en tu máquina. Puedes verificarlo ejecutando:

```sh
python --version
```

Si no lo tienes instalado, descárgalo desde [python.org](https://www.python.org/downloads/).

---
## 3. Creación de un Entorno Virtual

Es recomendable usar un entorno virtual para aislar las dependencias del proyecto. Para crearlo, ejecutamos:

```sh
python -m venv .venv --prompt matraka
```

> **Nota:** Asegúrate de estar dentro de la carpeta del proyecto antes de ejecutar este comando.

---

## 4. Activación del Entorno Virtual

Para activar el entorno virtual:

- En **Linux/macOS**:

  ```sh
  source .venv/bin/activate
  ```

- En **Windows (CMD)**:

  ```sh
  .venv\Scripts\activate
  ```

- En **Windows (PowerShell)**:

  ```sh
  .venv\Scripts\Activate.ps1
  ```

Cuando el entorno virtual está activado, el nombre del proyecto aparecerá entre paréntesis en el prompt, indicando que el entorno está en uso.

---

## 5. Instalación de Dependencias

Si tienes un archivo `requirements.txt` con las dependencias necesarias, instálalas ejecutando:

```sh
pip install -r requirements.txt
```

---

Tu entorno de desarrollo para Django está listo para empezar a trabajar.
