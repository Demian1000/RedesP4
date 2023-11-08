# Práctica 04

Démian Alejandro Monterrubio Acosta 317529180  
Victor Emiliano Cruz Hernández 318091166

## Uso:

El programa es un cliente HTTP capaz de establecer conexión con cualquier servidor web
usando el protocolo HTTP, y de llevar a cabo solicitudes GET y HEAD; el programa se
ejecuta de la siguiente manera:

```shell
$ python3 practica4.py <host> <http_method> <url> <user_agent> <encoding> <connection>
```

Parámetros:

\<host>: la dirección IP del servidor HTTP o a su nombre de dominio.  
\<http_method>: método de HTTP que se usará para enviar la solicitud, puede ser GET o HEAD.  
\<url>: archivo o recurso solicitado al servidor web.  
\<user_agent>: un número del 1 al 3, que corresponde a las siguientes opciones.  
1. "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"  
2. "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"  
3. "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"

\<encoding>: codificación de la respuesta, puede ser gzip, deflate o identity.  
\<connection>: forma del establecimiento de la conexión, puede ser keep-alive o close.

## Ejecución:

Desde línea de comandos:
```shell
$ python3 practica4.py <host> <http_method> <url> <user_agent> <encoding> <connection>
```

Usando Docker:
```shell
$ sudo docker build -t redes:4 .
$ sudo docker run --interactive --tty redes:p4 /bin/sh
$ python /opt/practica4.py <host> <http_method> <url> <user_agent> <encoding> <connection>
```

## Ejemplos:

```shell
$ python3 /opt/practica4.py prropanzon.tech HEAD / 1 identity close
```

```shell
$ python3 /opt/practica4.py google.com GET / 2 identity keep-alive
```

```shell
$ python3 /opt/practica4.py youtube.com GET /watch?v=IaLGdRx7prA&t=102s 3 identity close
```

## Preguntas:

1. ¿Cuál es la función de los métodos HTTP HEAD, GET, POST, PUT y DELETE?

    POST: crea un recurso.  
    PUT: actualiza un recurso existente.  
    GET: solicita un recurso.  
    DELETE: elimina un recurso.  
    HEAD: solicita el encabezado de un recurso.

2. ¿Investigue y enliste junto con su significado las categorías de estado que usa HTTP?

    100 - 199 códigos de respuesta informativos.  
    200 - 299 códigos de éxito.  
    300 - 399 Códigos de redirección.  
    400 - 499 códigos de errores del lado del cliente.  
    500 - 599 códigos de errores del lado del servidor.

3. ¿Para qué se usan los campos *encoding* y *conection*?

    Accept-Enconding: este campo se utiliza para que el cliente le indique al servidor el tipo de compresión con el que se mandará la información.

    Connection: este campo determina si la conexión es persistente, o se cerrará cuando termine la petición.
