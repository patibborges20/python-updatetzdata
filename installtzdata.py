import sys, os, string
import paramiko
import platform


servers = ['NORMA', '192.168.1.2', '187.52.5.3']
def centos6And7Update():
    try :
        update = "yum update -y tzdata"
        stdin, stdout, stderr = ssh.exec_command(update)
        print 'Sucesso no update'
    except:
            print 'erro ao fazer update'


def centos5Update():
    update = "cd /tmp;wget https://data.iana.org/time-zones/releases/tzdata2018f.tar.gz --no-check-certificate; tar -xvzf tzdata2018f.tar.gz; zic -d zoneinfo southamerica;cp zoneinfo/America/Sao_Paulo /usr/share/zoneinfo/America/Sao_Paulo"
    check = "zdump -v /usr/share/zoneinfo/America/Sao_Paulo | grep 2018"
    for server in servers:
        try:
            stdin, stdout, stderr = ssh.exec_command(update)
            print "Instalado no servidor " + server


        except:
            print "Erro no servidor" + server
            pass

def centosCheck():
    check = "zdump -v /usr/share/zoneinfo/America/Sao_Paulo | grep 2018"
    stdin, stdout, stderr = ssh.exec_command(check)
    print "Verifique se foi atualizado para 4 de novembro"
def checkRelease():
    system = platform.dist()
    family = system[0]
    release = system[0].split('.')
    release= release[0]
    igniteUpdate(family,release)


def igniteUpdate(family,release):
    if family == 'centos' and release == 5:
        print "Centos 5"
        centos5Update()
    if family == 'centos' and release == 6 or release == 7:
        print "Centos 6"
        centos6And7Update()
    else:
        print "Familia desconhecida"


def accessServer():
    for server in servers:
        print 'iniciando'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, username='root', password='xs$en@c-RS')
        stdin, stdout, stderr = checkRelease()
        stdin, stdout, stderr =centosCheck()
        stdin.write('xy\n')
        stdin.flush()
        stdin.close()
        print stdout.readlines()
accessServer()
