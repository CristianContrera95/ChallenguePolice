# ChallenguePolice

## Principales decisiones:

 ## Docker:
Lo ideal no es meter una base de datos en el mismo docker, por tal motivo mi Dockerfile es solo para la API.
Cree un docker compose para levantar un mongo local y probar la api.

La arquitectura para esta api podria ser deployar el Dockerfile en AWS con ECS y ECR. 
Para el mongo podriamos usar MongoDB Atlas.


## Ejecutar la API:

Recomiendo clonar el repo en su entorno local y ejecutar el docker-compose:  

     docker-compose up -d

PAra la interfaz del CRUD de las entidades se puede usar el swaggger de FASTAPI, disponible una vez levantado el proyecto:
http://0.0.0.0:8000/docs#/ 

Y luego usar postman para probar la API de Tickets:
 ticket

    GET
    /ticket/get_tickets
    Get Tickets


    POST
    /ticket/load_ticket
    New Ticket


## Nota Final:
Realmente se me complico los tiempos para dedicarle mas a este challenge, pero estas son mis circunstancias actuales en mi trabajo.
Estoy Super disponible a charlar o explicar todo lo que no llegue a hacer, completar o documentar en un a meeting.

muchas gracias por revisar esto!