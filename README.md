# url_params2json
Script de parsing que convierte un URL de búsqueda a un json con los parámetros equivalentes.

## Flags de configuración
El script posee solo 2 configuraciones, la primera (y obligatoria) es el URL a convertir, indicado con el flag `--url` o `-u` seguido del url completo obtenido de postman/insomnia.

La segunda es el nombre del archivo .json en caso de que se desee guardar el query en dicho archivo, para ello se usa el flag `--json` o `-j` seguido del nombre deseado.

## Instrucciones de uso
1. Clonar el repositorio localmente
2. Asegurarse de tener python instalado

Si se desea guardar el json resultante del query en un archivo .json, se debe ejecutar el siguiente comando: `python url_params2json.py --url <url_a_convertir> --json <nombre_archivo.json>`.

Si solo se desea observar en la terminal el json resultante del query, se debe ejecutar de esta forma: `python url_params2json.py --url <url_a_convertir>`.

## Ejemplos

### Guardando el archivo json
Target url: https://dmztw7bsqn61u9avp-1.a1.typesense.net/collections/senz_2022_airbyte_v2/documents/search?q=acetaminofen&query_by=nombre,caracteristicas&group_by=nog&filter_by=estatus%3A!%3D%5Bprescindido,desierto%5D%20%26%26%20modalidad%3A!%3DContrato%20Abierto%20Art%2046%20LCE%20%26%26%20(nombre%3A%5Bvial,100ml%5D%20%7C%7C%20caracteristicas%3A%5Bvial,100ml%5D%20%7C%7C%20unidad_medida%3A%5Bvial,100ml%5D)&per_page=250

Nombre del archivo json deseado: **miquery.json**

Comando: `python url_params2json.py --url https://dmztw7bsqn61u9avp-1.a1.typesense.net/collections/senz_2022_airbyte_v2/documents/search?q=acetaminofen&query_by=nombre,caracteristicas&group_by=nog&filter_by=estatus%3A!%3D%5Bprescindido,desierto%5D%20%26%26%20modalidad%3A!%3DContrato%20Abierto%20Art%2046%20LCE%20%26%26%20(nombre%3A%5Bvial,100ml%5D%20%7C%7C%20caracteristicas%3A%5Bvial,100ml%5D%20%7C%7C%20unidad_medida%3A%5Bvial,100ml%5D)&per_page=250 --json miquery.json`

### Sin guardar el archivo json
Target url: https://dmztw7bsqn61u9avp-1.a1.typesense.net/collections/senz_2022_airbyte_v2/documents/search?q=acetaminofen&query_by=nombre,caracteristicas&group_by=nog&filter_by=estatus%3A!%3D%5Bprescindido,desierto%5D%20%26%26%20modalidad%3A!%3DContrato%20Abierto%20Art%2046%20LCE%20%26%26%20(nombre%3A%5Bvial,100ml%5D%20%7C%7C%20caracteristicas%3A%5Bvial,100ml%5D%20%7C%7C%20unidad_medida%3A%5Bvial,100ml%5D)&per_page=250

Comando: `python url_params2json.py --url https://dmztw7bsqn61u9avp-1.a1.typesense.net/collections/senz_2022_airbyte_v2/documents/search?q=acetaminofen&query_by=nombre,caracteristicas&group_by=nog&filter_by=estatus%3A!%3D%5Bprescindido,desierto%5D%20%26%26%20modalidad%3A!%3DContrato%20Abierto%20Art%2046%20LCE%20%26%26%20(nombre%3A%5Bvial,100ml%5D%20%7C%7C%20caracteristicas%3A%5Bvial,100ml%5D%20%7C%7C%20unidad_medida%3A%5Bvial,100ml%5D)&per_page=250`