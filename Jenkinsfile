pipeline {
    agent any
    environment {
        // Declare the Docker Hub credentials, replacing 'dockerhub-credentials' with the ID you set in Jenkins
        DOCKER_CREDENTIALS = credentials('dockerhub-credentials')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm  // This checks out your code from the repository
            }
        }
        
        stage('Build') {
            steps {
                script {
                    // Using Docker registry credentials to interact with Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        // Build your Docker image here
                        def customImage = docker.build("your-image-name:${env.BUILD_ID}")
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Pushing the built Docker image to Docker Hub
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image("your-image-name:${env.BUILD_ID}").push()
                    }
                }
            }
        }

        // Additional stages can go here like Test, Deploy, etc.
    }
    post {
        always {
            // Clean up Docker images or perform other necessary post-actions
            echo 'Cleaning up Docker images...'
            sh 'docker system prune -f'
        }
    }
}
