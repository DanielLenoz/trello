


# 📝 Trello Clone API con Django

Este proyecto es una API REST que simula el funcionamiento básico de **Trello**, desarrollada con **Django** y **Django REST Framework**.  
Permite crear tableros, listas y tarjetas, así como gestionar usuarios y organizar tareas de forma estructurada. 🔧



## 🖼️ Vista previa

<img width="1292" height="682" alt="image" src="https://github.com/user-attachments/assets/bbc36326-25a1-4f7c-82be-ea7a11c497b6" />

---

## 🚀 Características principales

- 🔄 Operaciones **CRUD** completas para:
  - Tableros (`Boards`)
  - Listas (`ListsTrello`)
  - Tarjetas (`Cards`)
  - Usuarios

- 🧠 Relación jerárquica:
  - Cada **Board** puede tener muchas **Listas**
  - Cada **Lista** puede tener muchas **Tarjetas**
  - Los usuarios pueden estar asignados a tableros

- 📅 Registro de fechas para creación y modificaciones
- 📚 Documentación automática con **Swagger UI** y **Redoc**
- 🛠 Base de datos **SQLite** para pruebas locales

---

## 🔧 Tecnologías utilizadas

- **Python 3.12.3**
- **Django**
- **Django REST Framework**
- **drf-spectacular** (documentación OpenAPI)
- **SQLite 3**

---

## 🗂️ Estructura de carpetas

```

TRELLO/
├── boards/         ← CRUD de tableros
├── cards/          ← CRUD de tarjetas
├── listsTrello/    ← CRUD de listas por tablero
├── users/          ← Gestión de usuarios
├── docs/           ← Documentación y rutas
├── trello/         ← Configuración principal del proyecto
├── db.sqlite3      ← Base de datos local
└── manage.py

````

---

## 🧪 Cómo usar este proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/DanielLenoz/trello.git
cd trello
````

### 2. Crea un entorno virtual y actívalo

```bash
python -m venv env
source env/bin/activate      # Linux/Mac
env\Scripts\activate         # Windows
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplica las migraciones

```bash
python manage.py migrate
```

### 5. Ejecuta el servidor

```bash
python manage.py runserver
```

---

## 🔗 Documentación API

Una vez el servidor esté corriendo, visita:

* 📘 Swagger UI: [`http://localhost:8000/api/schema/swagger-ui/`](http://localhost:8000/api/schema/swagger-ui/)
* 📙 Redoc: [`http://localhost:8000/api/schema/redoc/`](http://localhost:8000/api/schema/redoc/)

---

## 🧪 Endpoints principales

| Método | Endpoint            | Descripción                        |
| ------ | ------------------- | ---------------------------------- |
| GET    | `/api/boards/`      | Listar todos los tableros          |
| POST   | `/api/boards/`      | Crear un nuevo tablero             |
| PUT    | `/api/boards/{id}/` | Actualizar un tablero              |
| DELETE | `/api/boards/{id}/` | Eliminar un tablero                |
| POST   | `/api/lists/`       | Crear una lista dentro de un board |
| PUT    | `/api/lists/{id}/`  | Actualizar lista                   |
| DELETE | `/api/lists/{id}/`  | Eliminar lista                     |
| POST   | `/api/cards/`       | Crear una tarjeta en una cards     |
| PUT    | `/api/cards/{id}/`  | Actualizar cards                   |
| DELETE | `/api/cards/{id}/`  | Eliminar cards                     |
---

## ✨ Captura de ejemplo (JSON response)

```json
{
  "id": 1,
  "name": "Project Alpha",
  "users": [1, 2],
  "listsTrello": [
    {
      "id": 1,
      "name": "To Do",
      "cards": [
        {
          "id": 1,
          "title": "Setup Environment",
          "description": "Install necessary tools and dependencies."
        }
      ]
    }
  ]
}
```

### 🧪 Formulario interactivo de prueba

Django REST Framework proporciona una interfaz visual amigable donde puedes:

- Crear entidades desde un **formulario HTML** sin usar Postman
- Seleccionar múltiples usuarios asociados a una tarjeta
- Ver cómo se genera automáticamente el JSON para el `POST`
- Enviar datos directamente con el botón `POST`

📷 Ejemplo:

<img width="1292" height="682" alt="image" src="https://github.com/user-attachments/assets/a38dc625-39fe-42ed-a632-a57b6a25a45e" />


---

## 📌 Recomendaciones

* Utiliza herramientas como **Postman** o **Insomnia** para probar los endpoints.
* Revisa los modelos en cada app (`boards`, `cards`, `listsTrello`) para personalizar el comportamiento.
* Usa la documentación Swagger para navegar fácilmente por la API.

---

## 🙌 Autor

Desarrollado con pasión por [Daniel Lenoz](https://github.com/DanielLenoz) 💻

---

## 📄 Licencia

Este proyecto está bajo licencia **MIT**.
¡Libre de usar, modificar y compartir!

---


### ✅ ¿Qué falta por tu parte?

- Guarda las capturas de pantalla en: `docs/screenshots/` con los nombres:
  - `board-list.png`
  - `project-structure.png`
  - `swagger-ui.png`
- Asegúrate de generar el `requirements.txt` si aún no lo tienes:

```bash
pip freeze > requirements.txt
````
