pipeline {
    agent none // No default agent; specify per stage

    environment {
        IMAGE_NAME = "harshalmeshram/flaskmarket:${BUILD_ID}"
        CONTAINER_NAME = "flask-market-container"
        APP_PORT = "5000"
    }

    stages {
        stage('Clone Repo') {
            agent any // Use default Jenkins agent for non-Docker steps
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/HarshalMeshram7/Flask-Market.git'
            }
        }

        stage('Build Docker Image') {
            agent {
                docker {
                    image 'docker:20.10' // Docker image with CLI
                    args '-v /var/run/docker.sock:/var/run/docker.sock --user root' // Run as root, mount Docker socket
                }
            }
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Login to DockerHub') {
            agent {
                docker {
                    image 'docker:20.10'
                    args '-v /var/run/docker.sock:/var/run/docker.sock --user root'
                }
            }
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
            agent {
                docker {
                    image 'docker:20.10'
                    args '-v /var/run/docker.sock:/var/run/docker.sock --user root'
                }
            }
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Remove Local Image') {
            agent {
                docker {
                    image 'docker:20.10'
                    args '-v /var/run/docker.sock:/var/run/docker.sock --user root'
                }
            }
            steps {
                sh 'docker rmi $IMAGE_NAME || true'
            }
        }

        stage('Pull and Run Container') {
            agent {
                docker {
                    image 'docker:20.10'
                    args '-v /var/run/docker.sock:/var/run/docker.sock --user root'
                }
            }
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