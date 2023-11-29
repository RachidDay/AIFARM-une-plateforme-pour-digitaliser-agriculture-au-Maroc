pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('c4f170c3-ba1e-4dd1-8895-a3f79266f6b8') 
        EC2_SSH_CREDENTIALS = credentials('1d356bbd-fb69-4a5d-8599-53a59133f90e') 
        IMAGE_TAG = "dayrachid/aifarm:latest" 
        EC2_HOST = "ec2-user@51.20.255.202" 
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(IMAGE_TAG)
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS) {
                        docker.image(IMAGE_TAG).push()
                    }
                }
            }
        }
        stage('Deploy to EC2') {
            steps {
                script {
                    sshagent([EC2_SSH_CREDENTIALS]) {
                        sh "ssh ${EC2_HOST} docker pull ${IMAGE_TAG} && docker stop aifarm || true && docker run -d --name aifarm -p 80:5000 ${IMAGE_TAG}"
                    }
                }
            }
        }
    }
}
