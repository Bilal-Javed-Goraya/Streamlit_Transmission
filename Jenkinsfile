pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'streamlit-app'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image from the Dockerfile
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Authenticate with Docker Hub and push the image
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                script {
                    // Pull the Docker image on the deployment server and run it
                    sh 'docker pull docker.io/streamlit-app'
                    sh 'docker run -d -p 8501:8501 --name streamlit-app docker.io/streamlit-app'
                }
            }
        }
    }

    post {
        always {
            // Clean up any resources if necessary (e.g., remove containers/images)
            cleanWs()
        }
    }
}
