pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-2"
        ECR_REGISTRY = "729318851051.dkr.ecr.us-east-2.amazonaws.com"
        ECR_REPO = "practicadevops"
        IMAGE_TAG = "latest"
        EB_APP_NAME = 'practicadevops'
        EB_ENV_NAME = 'practicadevops'
        VERSION_LABEL = "${env.BUILD_ID}"
        ZIP_FILE = 'application.zip'
    }

    stages {
    
        stage('Unit Tests') {
            steps {
                sh '''
                    echo "Aqui las pruebas simuladas de un html que se ejecutan en el contenedor"
                '''
            }
        }

        stage('Build Docker Imagen') {
            steps {
                sh '''
                    docker build -t $ECR_REPO:$IMAGE_TAG .
                    docker tag $ECR_REPO:$IMAGE_TAG $ECR_REGISTRY/$ECR_REPO:$IMAGE_TAG
                '''
            }
        }

        stage('Push ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REGISTRY
                    docker push $ECR_REGISTRY/$ECR_REPO:$IMAGE_TAG
                '''
            }
        }

        stage('Empaquetar ZIP') {
            steps {
                sh 'zip -r application.zip . -x "*.git*"'
            }
        }

        stage('Deploy a Elastic Beanstalk') {
            steps {
                sh '''
                    # Actualizar entorno con nueva versión
                    aws elasticbeanstalk update-environment \
                    --application-name $EB_APP_NAME \
                    --environment-name $EB_ENV_NAME \
                    --version-label $VERSION_LABEL \
                    --region $AWS_REGION
                    '''
                }
            }

        stage('Clean') {
            steps {
                sh 'docker rmi $ECR_REGISTRY/$ECR_REPO:$IMAGE_TAG || true'
            }
        }
    }
}
