# practicadevops
Simple Pagina HTML para practica DevOps
# 🌐 practica devops

Una página HTML sencilla con CI/CD completo utilizando:

- Docker
- Jenkins
- GitHub
- Tests unitarios simulados (Python)
- AWS ECR
- Elastic Beanstalk (Docker)

---

## 📁 Estructura del proyecto
practicadevops/
├── index.html # Página principal con html sencilla
├── Dockerfile # Imagen que sirve HTML con nginx
├── Jenkinsfile # Pipeline CI/CD para Jenkins
├── Dockerrun.aws.json # Config para Elastic Beanstalk
└── test/
└── test_python.py # Test unitario simulado


---

## 🚀 ¿Qué hace este proyecto?

1. **Sirve una página HTML sencilla con Docker (nginx)**
2. Ejecuta un test unitario para verificar que `index.html` existe
3. Construye una imagen Docker y la sube a Amazon ECR
4. Despliega la imagen en Elastic Beanstalk (Docker y balanceadores de carga y escalado automatico)

---

## 🐳 Docker

### Ejecutar localmente

docker build -t practicadevops .
docker run -p 8080:80 practicadevops

## Test Unitarios

## Estos tests son simulados
pip install pytest
pytest test/

🔁 Jenkins CI/CD

Pipeline definido en Jenkinsfile:
Clona el repositorio
Ejecuta los tests
Construye y etiqueta la imagen
Push a Amazon ECR
(Opcional) Despliegue a Elastic Beanstalk
Asegúrate de configurar credenciales AWS en Jenkins (con IAM Role o AWS CLI).

## Elastic beanstalk

1. Crea un archivo para despliegue
zip deploy.zip Dockerrun.aws.json

2. Subir a EB
En AWS Console:
Ve a Elastic Beanstalk
Crea una aplicación nueva (Docker)
Sube el ZIP
EB descargará la imagen desde ECR y la ejecutará

🛠️ Requisitos

Repositorio GitHub o el de tu preferencia
Docker
Python + pytest
Jenkins
AWS CLI configurado
ECR Repository creado (simple-html)
Elastic Beanstalk (plataforma Docker)

🧠 Recursos útiles

Docker https://docs.docker.com/
AWS ECR https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html
AWS Elastic Beanstalk
Jenkins https://www.jenkins.io/

📌 Autor

Proyecto generado por [Christian Jauregui]
Contacto: [jauregui_christian@hotmail.com]