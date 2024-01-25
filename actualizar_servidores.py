# actualizar_servidores.py
import paramiko

def actualizar_servidor(ip, usuario, clave_privada):
    # Conectarse al servidor
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=usuario, key_filename=clave_privada)

    # Ejecutar comandos de actualización
    comandos = [
        'sudo apt-get update',
        'sudo apt-get upgrade -y'
        # Agrega aquí los comandos específicos de actualización que necesites
    ]

    for comando in comandos:
        stdin, stdout, stderr = ssh.exec_command(comando)
        print(stdout.read().decode('utf-8'))

    # Cerrar conexión SSH
    ssh.close()

# Llamada a la función para cada servidor
servers = [
    {'ip': '192.168.1.1', 'usuario': 'tu-usuario', 'clave_privada': 'ruta/a/tu/clave_privada.pem'},
    # Agrega aquí la información de tus otros servidores
]

for server in servers:
    actualizar_servidor(server['ip'], server['usuario'], server['clave_privada'])
