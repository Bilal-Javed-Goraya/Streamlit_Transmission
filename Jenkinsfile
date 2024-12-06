pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'streamlit_workout'
        IMAGE_TAG = 'latest' // You can change the tag as needed (e.g., 1.0, 2.0, etc.)
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Login to Docker Hub using Jenkins credentials
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        // Login to Docker Hub
                        sh "docker login -u $DOCKER_USER -p $DOCKER_PASS"
                        
                        // Tag the image with the Docker Hub repository name
                        sh "docker tag $IMAGE_NAME:$IMAGE_TAG bilal625/$IMAGE_NAME:$IMAGE_TAG"
                        
                        // Push the image to Docker Hub
                        sh "docker push bilal625/$IMAGE_NAME:$IMAGE_TAG"
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images and other resources after the pipeline finishes
            echo "Cleaning up Docker images..."
            sh 'docker system prune -f'
        }
    }
}
