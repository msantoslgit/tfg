# tfg
Project to develop natural language to SQL querys using Python and OpenAI API

# Historial 

## Día 1
- Crear cuenta en OpenAI con un mail como usuario
- Obtenemos 5$ de créditos gratis
- Ponemos el username y la contraseña dentro del proyecto en la ruta:
- - Path_to_project.parent()\secret\openai

## Día 2
- Hemos creado un bucle para poder preguntar al chat y que nos responda.
- Se guarda las preguntas y las respuestas para seguir la conversación

## Día 3
- Establecer las tareas y definiciones en Trello 
- - https://trello.com/b/7xhBEhmx/cha-t-fg
- Empezar el módulo lector de la DB 
- Hemos creado un método lector de la BD que pregunta por que carpeta dentro de source queremos acceder
- Se leen todos los archivos .txt de la carpeta donde estarán las tablas. 

## Día 4/5 
- Tutorial de OpenAI API 

## Dia 6
- Se han completado la clase TokenPricing para saber el coste que tendrá la consulta siguiente basado en el numero de tokens de pregunta más respuesta
- Se ha completado la clase OpenAIChat, definiendo en una clase los métodos para ir enlazando llamadas a la api 
- Se carga el modelo inicial de "Prompt" desde un fichero 
- Los notebooks están al día 


## Dia 7
- 
- Se han creado las funciones en el notebook para SqlFluff
- Creado el método para elegir que errores queremos cambiar 
- Se han creado los notebooks para SqlFluff

## 
- 
- Pensar en el testing / accuracy 
