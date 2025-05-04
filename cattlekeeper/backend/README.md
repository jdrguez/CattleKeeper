# Backend Cattlekeeper

```
cattlekeeper/                  # Proyecto raíz
├── manage.py
├── cattlekeeper/             # Configuración del proyecto (settings, urls)
│
├── accounts/                 # Usuarios y autenticación
├── products/                 # Productos a la venta
├── orders/                   # Pedidos y pagos
├── farm/                     # Granja del usuario
│   ├── models.py             # Animales, producción, salud, etc.
│   ├── animals/              # Gestión de animales (altas, bajas, razas, historial)
│   ├── health/               # Historial sanitario, vacunas, visitas veterinarias
│   ├── production/           # Producción (leche, carne, huevos, etc.)
│   ├── expenses/             # Costos, gastos, inversiones
│
└── stats/                    # Reportes y dashboards
```

### Descripción

#### 1. accounts/
Modelos: User personalizado si necesitas más campos (como nombre granja, etc.)
Vistas: login, logout, registro (django.contrib.auth.views + formularios propios)
URLs: /login/, /register/, /logout/, /profile/

#### 2. products/
Modelos: Producto, Categoría
Vistas: Listado de productos (usado luego por Vue), detalles
URLs: /products/, /products/<id>/

#### 3. orders/
Modelos: Orden, OrdenItem, Pago
Vistas: Agregar al carrito, ver carrito, confirmar compra
URLs: /cart/, /checkout/

#### 4. farm/ (con submódulos o apps internas si crece mucho)
Modelos:
Animal: especie, raza, fecha de nacimiento, peso
HealthRecord: fecha, diagnóstico, tratamiento, animal relacionado
Production: litros de leche, kg de carne, etc.
Expense: categoría, monto, fecha
URLs: /farm/animals/, /farm/production/, etc.

#### 5. stats/
Vistas que agregan contexto con filtros por usuario
Generan datos para los futuros gráficos de Vue
Rutas como /stats/overview/, /stats/expenses/

## Orden

### ✅ 1. Crea la aplicación de usuarios (accounts)
Antes de hacer cualquier cosa, necesitas la funcionalidad de registro, inicio de sesión y gestión de perfiles. Esta aplicación será la base para que los usuarios puedan acceder a la plataforma, y es crucial para que las demás aplicaciones puedan asociarse a un usuario autenticado.

Tareas en esta fase:

Crear el modelo User (si decides personalizarlo) o usar el modelo User de Django.
Configurar las vistas de registro, login, logout.
Crear las URLs relacionadas (/login/, /register/, /profile/).
Implementar la autenticación de usuario (por ejemplo, usando el sistema de sesiones de Django).

## ✅ 2. Crea la aplicación de productos (products)
Una vez que los usuarios pueden registrarse e iniciar sesión, el siguiente paso es la gestión de productos. Esto es fundamental para simular el catálogo de tu tienda ganadera.

Tareas en esta fase:

Crear el modelo Product (con campos como nombre, descripción, precio, stock, etc.).
Crear vistas que muestren los productos (por ejemplo, una vista de lista de productos).
Configurar las URLs relacionadas (/products/, /products/<id>/).

## ✅ 3. Crea la aplicación de pedidos (orders)
Cuando los usuarios estén listos para comprar productos, necesitarás gestionar los carritos de compras y pedidos. Es importante tener esta aplicación después de products para que la gente pueda comprar algo de tu catálogo.

Tareas en esta fase:

Crear el modelo Order, OrderItem (para los productos en cada pedido).
Implementar vistas para agregar productos al carrito, ver el carrito y realizar el checkout.
Conectar el proceso de pago (aunque solo lo simules por ahora).
Crear las URLs de pedido (/cart/, /checkout/).

## ✅ 4. Crea la aplicación de la granja (farm)
Esta aplicación es fundamental para gestionar la parte personalizada de cada usuario: su granja, los animales, y la producción de su granja. Debes crearla después de los productos y pedidos, ya que necesitarás que cada usuario esté registrado y haya hecho algún pedido antes de agregar sus datos de granja.

Tareas en esta fase:

Crear el modelo Animal (para cada animal de la granja).
Crear los modelos de producción, salud, gastos, etc.
Implementar vistas que permitan al usuario ver y agregar estos datos.
Configurar las URLs relacionadas (/farm/animals/, /farm/production/, etc.).

## ✅ 5. Crea la aplicación de estadísticas (stats)
Finalmente, para dar un valor adicional al usuario y ayudarlo a monitorear su granja, la aplicación de estadísticas mostrará los reportes de producción, salud, costos y otros indicadores.

Tareas en esta fase:

Crear las vistas de estadísticas basadas en los datos de los modelos de farm y orders.
Implementar vistas para mostrar datos procesados (como gráficos de producción, análisis de gastos).
Configurar las URLs para mostrar estadísticas.

## ✅ 6. Configura la capa de APIs (si necesitas)
A medida que avanzas con el backend, podrías pensar en una capa API si más adelante te conectarás con un frontend de Vue.js. Sin embargo, esta parte la puedes dejar para cuando tu backend esté en su mayoría listo, para que no tengas que crear API REST mientras las vistas de HTML y lógica interna estén en progreso.

📝 Resumen del orden:
accounts/ (Usuarios, autenticación, roles)
products/ (Catálogo de productos)
orders/ (Carrito de compras, pedidos)
farm/ (Gestión de la granja: animales, salud, producción)
stats/ (Reportes, gráficos y análisis)
API (Si decides hacerla, cuando todo esté funcionando)
