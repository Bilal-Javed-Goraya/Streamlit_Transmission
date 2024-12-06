pipeline {
    agent any
    
    environment {
        // Define environment variables
        PROJECT_DIR = "/var/lib/jenkins/workspace/streamlit-app"
        REQUIREMENTS_FILE = "$PROJECT_DIR/requirements.txt"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from the Git repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image for the Streamlit app
                    echo 'Building Docker image for Streamlit app...'
                    sh '''
                        docker build -t streamlit-app .
                    '''
                }
            }
        }

        stage('Run Tests (optional)') {
            steps {
                script {
                    // Run your tests if any
                    // Assuming you're using pytest, otherwise skip this stage
                    echo 'Running tests (optional)...'
                    sh '''
                        docker run --rm streamlit-app pytest
                    '''
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                script {
                    // Deployment stage (run your Docker image on a remote server)
                    echo 'Deploying Streamlit app...'
                    sh '''
                        # Assuming you have SSH access to the server and Docker installed
                        ssh user@your-server "
                            cd /path/to/streamlit-app && 
                            docker pull streamlit-app && 
                            docker run -d -p 8501:8501 streamlit-app"
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
