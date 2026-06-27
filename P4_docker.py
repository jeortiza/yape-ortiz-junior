# ============================================================
# PASO 2: Conectar Python al MongoDB en Docker (local)
# ============================================================
from pymongo import MongoClient

# Conexión al contenedor Docker (localhost, no Atlas)
client_docker = MongoClient(
    "mongodb://admin:yape2026@localhost:27017/",
    authSource="admin"
)

db_local = client_docker["yape_local"]
col_local = db_local["comerciantes_test"]

# Insertar un comerciante de prueba
col_local.insert_one({
    "nombre_comercio": "Bodega Test Docker",
    "tipo": "bodega",
    "distrito": "Lima",
    "monto_mensual_soles": 1500.00,
    "yape_activo": True,
    "entorno": "docker_local"   # Campo que indica que es entorno local
})

# Verificar
doc = col_local.find_one({"nombre_comercio": "Bodega Test Docker"})
print("✅ Documento guardado en MongoDB Docker:")
print(f"   Nombre:   {doc['nombre_comercio']}")
print(f"   Entorno:  {doc['entorno']}")
print(f"   ID:       {doc['_id']}")

# Mostrar todos los documentos en la colección
print(f"\nTotal documentos en Docker: {col_local.count_documents({})}")