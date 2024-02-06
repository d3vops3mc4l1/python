# by pamartin FEB-06-2024
# Este Script es para automatizar tareas de revision de servidores del datacenter linux.
# actualizar_servidores.py
import paramiko

def actualizar_servidor(ip, usuario, clave_privada):
    # Conectarse al servidor
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=usuario, key_filename=clave_privada)

    # Ejecutar comandos de actualización
    comandos = [
        'df -h',
        'ls -la  /var/www/',
        'touch /home/ubuntu/emcalindex.html'
        # Agrega aquí los comandos específicos de actualización que necesites
    ]

    for comando in comandos:
        stdin, stdout, stderr = ssh.exec_command(comando)
        print(stdout.read().decode('utf-8'))

    # Cerrar conexión SSH
    ssh.close()

# Llamada a la función para cada servidor
servers = [
    {'ip': '54.166.62.104', 'usuario': 'ubuntu', 'clave_privada': '/var/lib/jenkins/workspace/python-server-aws/claveadonde.pem'},
    # Agrega aquí la información de tus otros servidores
]

for server in servers:
    actualizar_servidor(server['ip'], server['usuario'], server['clave_privada'])
