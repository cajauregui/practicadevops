# 🌐 Practica DevOps

Una página HTML sencilla con CI/CD completo utilizando:

- Docker
- Jenkins
- GitHub
- Tests unitarios simulados
- AWS ECR
- Elastic Beanstalk (Docker)

---

## 📁 Estructura del proyecto
practicadevops/
- index.html # Página principal con html sencilla
- Dockerfile # Imagen que sirve HTML con nginx
- Jenkinsfile # Pipeline CI/CD para Jenkins
- Dockerrun.aws.json # Config para Elastic Beanstalk

css/
- styles.css # Estilos con solo una etiqueta

---

## 🚀 ¿Qué hace este proyecto?

1. Sirve una página HTML sencilla con Docker (nginx)
2. Ejecuta un test simulado
3. Construye una imagen Docker y la sube a Amazon ECR
4. Empaqueta en zip y la sube a bucket S3 de AWS
5. Despliega la imagen en Elastic Beanstalk (Docker con escalado automatico)

---

## 🐳 Docker

### Ejecutar localmente

- docker build -t practicadevops .
- docker run -p 8080:80 practicadevops


🔁 Jenkins CI/CD aws

- Pipeline definido en Jenkinsfile:
- Clona el repositorio
- Ejecuta los tests
- Construye y etiqueta la imagen
- Push a Amazon ECR
- Despliegue a Elastic Beanstalk
- Empaqueta el proyecto en un ZIP
- Subi zip a bucket S3

NOTA:Asegúrate de configurar credenciales AWS en Jenkins (con IAM Role o AWS CLI).

## Elastic beanstalk

1. Crea un archivo para despliegue
zip deploy.zip Dockerrun.aws.json

2. Subir a EB

- Ve a Elastic Beanstalk
- Crea una aplicación nueva (Docker)
- Sube el ZIP
- EB descargará la imagen desde ECR y la ejecutará

🛠️ Requisitos

- Repositorio GitHub o el de tu preferencia
- Docker
- Jenkins
- AWS CLI configurado o asignar IAM Role a EC2 y EB
- ECR Repository creado (practicasdevops)
- Elastic Beanstalk (plataforma Docker)

🧠 Recursos útiles

- Docker https://docs.docker.com/
- AWS ECR https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html
- AWS Elastic Beanstalk https://aws.amazon.com/es/elasticbeanstalk/
- Jenkins https://www.jenkins.io/

📌 Autor

- Proyecto generado por [Christian Jauregui]
- Contacto: [jauregui_christian@hotmail.com]




