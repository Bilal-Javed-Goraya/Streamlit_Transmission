pipeline {
    agent any
    
    environment {
        // Define environment variables
        PROJECT_DIR = "/var/lib/jenkins/workspace/streamlit-app"
        VENV_DIR = "$PROJECT_DIR/venv"
        REQUIREMENTS_FILE = "$PROJECT_DIR/requirements.txt"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from the Git repository
                checkout scm
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    // Set up the virtual environment for the project
                    sh '''
                        python3 -m venv $VENV_DIR
                        source $VENV_DIR/bin/activate
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install the required dependencies from the requirements.txt file
                    sh '''
                        source $VENV_DIR/bin/activate
                        pip install -r $REQUIREMENTS_FILE
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run your tests (if any). Assuming you're using pytest for testing
                    // If no tests, you can skip this or add linting/validation
                    sh '''
                        source $VENV_DIR/bin/activate
                        pytest
                    '''
                }
            }
        }

        stage('Build Docker Image (optional)') {
            steps {
                script {
                    // Build Docker image for the Streamlit app (if you're using Docker)
                    sh '''
                        docker build -t streamlit-app .
                    '''
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                script {
                    // Deployment stage. Here, you can use SSH or Docker commands to deploy
                    // the Streamlit app to a server.
                    // Example: using SSH to deploy
                    sh '''
                        ssh user@your-server "cd /path/to/streamlit-app && git pull && source venv/bin/activate && streamlit run app.py"
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}
