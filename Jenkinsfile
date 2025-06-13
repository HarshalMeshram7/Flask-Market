pipeline {
    agent any

    environment {
        IMAGE_NAME = "harshalmeshram/flaskmarket:${BUILD_ID}"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', credentialsId: 'github-creds', url: 'https://github.com/HarshalMeshram7/Flask-Market.git'
            }
    }


        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Remove Local Image (simulate pull step)') {
            steps {
                sh 'docker rmi $IMAGE_NAME'
            }
        }

        stage('Pull and Run Container') {
            steps {
                sh '''
                    docker pull $IMAGE_NAME
                    docker stop flask-container || true && docker rm flask-container || true
                    docker run -d --name flask-container -p 5000:5000 $IMAGE_NAME
                '''
            }
        }
    }
}
