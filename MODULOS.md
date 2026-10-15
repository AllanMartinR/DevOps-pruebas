# Módulos de la tienda

Cada equipo trabaja **un solo archivo** dentro de `src/tienda/`. Cada archivo ya tiene
las funciones creadas con su docstring (las reglas exactas) y un `raise NotImplementedError`.
**Reemplacen ese `raise` por su código.** Las pruebas están en `tests/`.

| # | Equipo / Módulo | Archivo a editar | Pruebas | Rama de Git |
|---|---|---|---|---|
| 1 | Carrito | `src/tienda/carrito.py` | `tests/test_carrito.py` | `equipo-1-carrito` |
| 2 | Descuentos | `src/tienda/descuentos.py` | `tests/test_descuentos.py` | `equipo-2-descuentos` |
| 3 | Inventario | `src/tienda/inventario.py` | `tests/test_inventario.py` | `equipo-3-inventario` |
| 4 | Usuarios | `src/tienda/usuarios.py` | `tests/test_usuarios.py` | `equipo-4-usuarios` |
| 5 | Pagos | `src/tienda/pagos.py` | `tests/test_pagos.py` | `equipo-5-pagos` |
| 6 | Envíos | `src/tienda/envios.py` | `tests/test_envios.py` | `equipo-6-envios` |

Correr las pruebas de su módulo: `pytest tests/test_<modulo>.py -v`

**Sugerencia de reparto interno:** el Dev empieza por las funciones más fáciles (las primeras
de cada lista) y sube un push por función. El QA lee las pruebas para entender los casos
límite y el DevOps hace los commits/push y vigila el pipeline.

---

## Módulo 1 - Carrito (`carrito.py`)

Guarda productos con precio y cantidad. Estructura:
`{"pan": {"precio": 10.0, "cantidad": 2}}`

| Función | Qué hace |
|---|---|
| `crear_carrito()` | Devuelve un carrito vacío `{}` |
| `agregar_producto(carrito, nombre, precio, cantidad=1)` | Agrega producto; si ya existe suma cantidad y **conserva el precio original**. `precio <= 0` o `cantidad <= 0` -> `ValueError`. Devuelve el mismo carrito |
| `quitar_producto(carrito, nombre, cantidad=None)` | Sin cantidad elimina todo el producto. Si `cantidad` >= lo que hay, también lo elimina; si es menor, resta. No existe -> `KeyError`. `cantidad <= 0` -> `ValueError` |
| `calcular_total(carrito)` | Suma `precio * cantidad`, **redondeado a 2 decimales**. Vacío -> 0 |
| `contar_articulos(carrito)` | Total de unidades (suma de cantidades) |

## Módulo 2 - Descuentos (`descuentos.py`)

Todos los resultados van **redondeados a 2 decimales**. Ya existe el diccionario `CUPONES` (no lo cambien).

| Función | Qué hace |
|---|---|
| `aplicar_porcentaje(total, porcentaje)` | `200, 10 -> 180.0`. `total < 0` o porcentaje fuera de 0-100 -> `ValueError` |
| `aplicar_cupon(total, codigo)` | Aplica un cupón de `CUPONES` (`DEVOPS10`, `PROMO20`, `MEGA50`). Ignora mayúsculas y espacios. Cupón inexistente o no-texto -> `ValueError` |
| `descuento_por_volumen(total)` | >=1000 -> 15%, >=500 -> 10%, >=200 -> 5%, menos -> 0%. `total < 0` -> `ValueError` |
| `calcular_ahorro(total_original, total_final)` | `original - final`. Si `final > original` -> `ValueError` |

## Módulo 3 - Inventario (`inventario.py`)

Estructura: `{"pan": 20, "leche": 3}`

| Función | Qué hace |
|---|---|
| `crear_inventario()` | Devuelve `{}` |
| `agregar_stock(inventario, producto, cantidad)` | Suma unidades (crea el producto si no existe). `cantidad <= 0` -> `ValueError`. Devuelve el mismo inventario |
| `hay_stock(inventario, producto, cantidad=1)` | `True` si hay al menos esa cantidad. Producto inexistente -> `False`. `cantidad <= 0` -> `ValueError` |
| `reducir_stock(inventario, producto, cantidad)` | Resta unidades. `cantidad <= 0`, producto inexistente o stock insuficiente -> `ValueError` **sin modificar nada**. Si queda en 0, el producto sigue con valor 0 |
| `productos_bajo_stock(inventario, minimo=5)` | Lista (orden alfabético) de productos con stock **menor** que `minimo`, incluyendo los de 0 |

## Módulo 4 - Usuarios (`usuarios.py`)

| Función | Qué hace |
|---|---|
| `validar_correo(correo)` | `True` si: es texto, sin espacios, exactamente un `@`, hay texto antes y después, el dominio tiene al menos un `.`, no empieza/termina con `.` y no tiene `..` |
| `validar_password(password)` | `True` si: texto de 8+ caracteres, con mayúscula, minúscula, número y símbolo (`_` cuenta como símbolo), y sin espacios |
| `validar_registro(correo, password, confirmacion)` | Devuelve `(es_valido, errores)`. Códigos en este orden: `"correo_invalido"`, `"password_invalida"`, `"password_no_coincide"` |
| `normalizar_correo(correo)` | Quita espacios de los extremos y pasa a minúsculas. Si queda inválido -> `ValueError` |

Ejemplo: `validar_registro("ana", "abc", "abd")` -> `(False, ["correo_invalido", "password_invalida", "password_no_coincide"])`

## Módulo 5 - Pagos (`pagos.py`)

| Función | Qué hace |
|---|---|
| `validar_luhn(numero)` | Algoritmo de Luhn. Acepta espacios y guiones. `False` si no es texto, tiene no-dígitos o su longitud no está entre 13 y 19 |
| `detectar_marca(numero)` | Empieza con 4 -> `"visa"`; 51 a 55 -> `"mastercard"`; 34 o 37 -> `"amex"`; otro -> `"desconocida"`. No valida Luhn |
| `validar_vencimiento(mes, anio, mes_actual, anio_actual)` | `True` si no ha vencido. Mes fuera de 1-12 -> `False`. Vence al **final** del mes (el mes actual aún es válido) |
| `procesar_pago(numero, monto)` | `{"aprobado": bool, "motivo": str}`. Orden: `monto <= 0` -> `"monto_invalido"`; Luhn falla -> `"tarjeta_invalida"`; si no -> `True, "ok"` |

Números de prueba: `4111111111111111` (Visa), `5555555555554444` (Mastercard), `378282246310005` (Amex).

## Módulo 6 - Envíos (`envios.py`)

Ya existen `TARIFAS` y `DIAS` (no los cambien).

| Función | Qué hace |
|---|---|
| `calcular_costo(peso_kg, zona)` | Tarifa base de la zona + **20 por cada kg adicional** (una fracción cuenta como kg completo). `1.5 kg local -> 70.0`. Zona sin importar mayúsculas/espacios. Zona inválida, `peso <= 0` o `peso > 30` -> `ValueError`. Devuelve `float` |
| `envio_gratis(total_compra)` | `True` si `total_compra >= 999` |
| `dias_entrega(zona)` | Días según `DIAS`. Zona inválida -> `ValueError` |
| `costo_final(peso_kg, zona, total_compra)` | `0.0` si hay envío gratis y la zona **no** es internacional; si no, `calcular_costo`. Datos inválidos siempre dan `ValueError`, aunque el envío fuera gratis |

---

## Tips

- Lean el docstring de cada función: ahí están TODAS las reglas.
- Lean los tests de su módulo: son ejemplos de uso y de casos límite.
- Pueden llamar a otras funciones de su mismo archivo (por ejemplo `aplicar_cupon` puede usar `aplicar_porcentaje`).
- ¡Ojo! Puede haber casos que sus pruebas visibles no cubren. Piensen en los bordes: valores en el límite, textos raros, `None`.
