import socket
import sys

# Lista con los user agents posibles
user_agents = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
]

# Cadena con lasinstrucciones para usar el programa
instructions = f"""Instrucciones de uso:
El programa es un cliente HTTP capaz de establecer conexión con cualquier servidor web
usando el protocolo HTTP, y de llevar a cabo solicitudes GET y HEAD; el programa se
ejecuta de la siguiente manera:

python3 practica4.py <host> <http_method> <url> <user_agent> <encoding> <connection>

Parámetros:

<host>: la dirección IP del servidor HTTP o a su nombre de dominio.
<http_method>: método de HTTP que se usará para enviar la solicitud, puede ser GET o HEAD.
<url>: archivo o recurso solicitado al servidor web.
<user_agent>: un número del 1 al 3, que corresponde a las siguientes opciones.
    1- {user_agents[0]}
    2- {user_agents[1]}
    3- {user_agents[2]}
<encoding>: codificación de la respuesta, puede ser gzip, deflate o identity.
<connection>: forma del establecimiento de la conexión, puede ser keep-alive o close.
"""

def use():
    """
    Imprime las instrucciones del programa y termina su ejecución.
    """
    print(instructions)
    sys.exit(1)

def processArguments():
    """
    Recibe los argumentos, los valida y realiza la solicitud HTTP.
    """
    print("")

    if len(sys.argv) != 7:
        print("Número de argumentos incorrecto.\n")
        use()

    # Validamos el http_method
    if sys.argv[2] != "GET" and sys.argv[2] != "HEAD":
        print("Error en el http method.\n")
        use()

    # Validamos el índice del user agent
    if sys.argv[4] != "1" and sys.argv[4] != "2" and sys.argv[4] != "3":
        print("Error en el user agent.\n")
        use()

    # Validamos el encoding
    if sys.argv[5] != "gzip" and sys.argv[5] != "deflate" and sys.argv[5] != "identity":
        print("Error en el encoding.\n")
        use()
    
    # Validamos connection
    if sys.argv[6] != "keep-alive" and sys.argv[6] != "close":
        print("Error en el tipo de conexión.\n")
        use()

    return sys.argv[1:]


def constructHTTPRequest(host_server, http_method, url, u_agent, encoding, con):
    """
    Construye una cadena para lasolicitud HTTP con los parámetros dados.
    """

    # Construcción de la solicitud
    version = "HTTP/1.1"
    request_line = f"{http_method} {url} {version}\r\n"

    # Construcción de las cabeceras
    host = f"Host: {host_server}"
    user_agent = f"User-Agent: {user_agents[int(u_agent)-1]}"
    accept_encoding = f"Accept-Encoding: {encoding}"
    accept_language = "Accept-Language: en-US"
    connection = f"Connection: {con}"
    header_lines = f"{host}\r\n{user_agent}\r\n{accept_encoding}\r\n{accept_language}\r\n{connection}\r\n"

    # Petición HTTP
    p = f"{request_line}{header_lines}\r\n"
    print(p)
    return p


def TCPconeection(host_server, HTTP_request):
    """
    Comienza una conexión TCP con host_server, y realiza le
    manda la solicitud HTTP_request.
    """

    # Crea un socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conexión entre el cliente y servidor por el puerto 80
    s.connect((host_server,80))

    # Envía la petición HTTP al servidor
    s.send(HTTP_request.encode())

    # Imprime en pantalla la información que recibe del servidor
    while True:
        HTTP_response = s.recv(1024)
        if not HTTP_response: break
        print(HTTP_response)

    # Se cierra la conexión con el servidor
    s.close()

    print("\n\nConexión con el servidor finalizada\n")


# Ejecutamos el programa
args = processArguments()
HTTP_request = constructHTTPRequest(*args)
TCPconeection(args[0], HTTP_request)