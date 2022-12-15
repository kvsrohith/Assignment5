
Requests:
_________

1. /movies
2. /movies/id
3. /movies/id/sales
4. /movies/id/sales/sale_id

-Setup the project with the app.py and JSON file in a single folder.

-In the docker terminal, use command "touch Dockerfile" to create the Dockerfile and setup the environment of the docker file.

-Create Docker Image by running : "docker build -t docker-python ."

-Check the image created using "docker images"

-Run the app image inside a container using "docker run -d -p 8080:8080 docker-python"

-Check running docker container by "docker ps"
