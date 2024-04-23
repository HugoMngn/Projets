import requests
import socket
import ssl
from cryptography import x509
from cryptography.hazmat.backends import default_backend

url = "https://taisen.fr/"
response = requests.get(url)
url = "taisen.fr"
port = 80

domain_name = url.split('//')[-1].split('/')[0]
dns_ip = socket.gethostbyname(domain_name)
print("IP DNS:", dns_ip)
print("Nom DNS:", socket.getfqdn(dns_ip))
print(" ")

def get_source(url, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((url, port))
        source_ip, source_port = s.getsockname()
        s.close()
        return source_ip, source_port
    except socket.error as e:
        print(f"Une erreur s'est produite lors de la connexion : {e}")

def get_destination(url, port):
    destination_ip = socket.gethostbyname(url)
    return destination_ip, port



# Obtenir l'IP et le port source
source_ip, source_port = get_source(url, port)
print("IP source:", source_ip)
print("Port source:", source_port)
print("")

destination_ip, destination_port = get_destination(url, port)
print("IP destination:", destination_ip)
print("Port destination:", destination_port)
print("")



print("Headers:")
print("Sert à identificater et contrôler des requêtes et des réponses, contrôler des caches, gérer des cookies et de l'authentification, et contrôler de la sécurité.")
for header, value in response.headers.items():
    print(f"{header}: {value}")
print(" ")

content_type = response.headers.get('Content-Type')
print("Content-Type:", content_type)
print("Sert à identificater du type de contenu, traiter de façon approprié du contenu, et pour la sécurité.")
print(" ")

html_tags = response.text.split('<')
print("Balises Web:", html_tags)
print(" ")

with ssl.create_default_context().wrap_socket(socket.socket(), server_hostname=url) as s:
    s.connect((url, 443))
    cert = s.getpeercert()
print("")

print("Certificat du serveur :")
print(cert)
print("")


cert_chain = ssl.get_server_certificate((url, 443))
certificates = []
start = 0
while True:
    start_cert = cert_chain.find("-----BEGIN CERTIFICATE-----", start)
    if start_cert == -1:
        break
    end_cert = cert_chain.find("-----END CERTIFICATE-----", start_cert)
    if end_cert == -1:
        break
    cert = cert_chain[start_cert:end_cert + len("-----END CERTIFICATE-----")]
    certificates.append(x509.load_pem_x509_certificate(cert.encode(), default_backend()))
    start = end_cert + len("-----END CERTIFICATE-----")


print("Noms de l'émetteur et du sujet pour chaque certificat dans la chaîne :")
for i, cert in enumerate(certificates):
    print(f"Certificat {i + 1}:")
    print("Nom de l'émetteur:", cert.issuer.rfc4514_string())
    print("Nom du sujet:", cert.subject.rfc4514_string())
    print()



traceroute = socket.gethostbyname_ex(domain_name)
print("IP traversées:", traceroute[2])
print(" ")