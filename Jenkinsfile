pipeline {
    agent any

    environment {
        IMAGE_NAME = "harshalmeshram/flaskmarket:${BUILD_ID}"
        CONTAINER_NAME = "flask-market-container"
        APP_PORT = "5000"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/HarshalMeshram7/Flask-Market.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'sudo docker build -t $IMAGE_NAME . -S Harshal@112762'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Remove Local Image') {
            steps {
                sh 'docker rmi $IMAGE_NAME || true'
            }
        }

        stage('Pull and Run Container') {
            steps {
                sh '''
                    docker pull $IMAGE_NAME
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p $APP_PORT:5000 $IMAGE_NAME
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployed at http://<your-server-ip>:${APP_PORT}"
        }
        failure {
            echo '❌ Build or deployment failed. Check logs.'
        }
    }
}
