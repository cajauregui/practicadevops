pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        ECR_REGISTRY = "729318851051.dkr.ecr.us-east-2.amazonaws.com"
        ECR_REPO = "practicadevops"
        IMAGE_TAG = "latest"
    }

    stages {
    
        stage('Unit Tests') {
            steps {
                sh "/usr/bin/pip install -q pytest"
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

        stage('Clean') {
            steps {
                sh 'docker rmi $ECR_REGISTRY/$ECR_REPO:$IMAGE_TAG || true'
            }
        }
    }
}
