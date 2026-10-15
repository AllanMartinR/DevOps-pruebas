# DevOps Express - Mini tienda en línea

Entre los 6 equipos construyen una tienda. **Cada equipo programa un módulo**.
Cada vez que hacen `push`, un pipeline de CI corre las pruebas automáticamente
y les dice si quedó en **verde** (pasó todo) o **rojo** (algo falla).

> Todo lo que deben programar y en qué archivo está en **[MODULOS.md](MODULOS.md)**.

## Roles dentro de cada equipo (3 personas)

| Rol | Qué hace |
|---|---|
| **Dev** | Programa las funciones del módulo |
| **QA** | Corre las pruebas, revisa casos límite y lee los errores |
| **DevOps** | Maneja Git (rama, commits, push) y vigila el pipeline |

## Arranque rápido (hacerlo ANTES de la clase)

Requisitos: **Python 3.10 o superior** y Git.

```bash
git clone <URL_DEL_REPO>
cd devops-express
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Creen SU rama (cambien por el nombre de su equipo/módulo, ver MODULOS.md)
git checkout -b equipo-1-carrito
```

## Flujo de trabajo

```bash
# 1. Programen en SU archivo dentro de src/tienda/
# 2. Corran SUS pruebas en local
pytest tests/test_carrito.py -v

# 3. Suban cambios (¡hagan push seguido! cada push mide su frecuencia de despliegue)
git add src/tienda/carrito.py
git commit -m "feat(carrito): implementa agregar_producto"
git push -u origin equipo-1-carrito      # la primera vez
git push                                  # las siguientes
```

Luego vayan a la pestaña **Actions** del repo, abran el último run de su rama y
revisen el resumen (pruebas aprobadas, fallidas y cobertura).

## Reglas

1. Solo editen **su** archivo de `src/tienda/`. No toquen `tests/`, `.github/` ni archivos de otros equipos.
2. No cambien nombres de funciones ni parámetros: las pruebas dependen de ellos.
3. El **nombre de la rama** debe ser exactamente el indicado en MODULOS.md. Así el pipeline sabe qué módulo probar.
4. Hagan commits pequeños y con mensajes claros. Es mejor 10 pushes pequeños que 1 enorme.
5. Si el pipeline se pone rojo, ¡arréglenlo rápido! Se mide cuánto tardan en recuperarse (MTTR).

## Estructura

```
src/tienda/        <- aquí programan (un archivo por equipo)
tests/             <- pruebas automáticas (NO tocar)
.github/workflows/ <- pipeline de CI (NO tocar)
MODULOS.md         <- qué hace cada módulo
```
