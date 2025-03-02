pipeline {
    agent any

    stages {
        stage('checkout repo') {
            steps {
                checkout scm
            }
        }
        stage('build docker image and run') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
        stage('Test Application') {
            steps {
                echo 'Running e2e tests...'
                // The pipeline will fail if the python script returns a non-zero exit code.
                sh 'python tests/e2e.py'
            }
        }
        stage('Terminate and Push') {
            steps {
                script {
                    echo 'Terminating containers...'
                    sh 'docker-compose down'

                    // Optionally tag and push an image to a Docker registry
                    // Example for Docker Hub; adjust registry/image names as needed
                    echo 'Tagging and pushing Docker image...'
                    sh """
                    docker tag main-score:latest hagai211/main-score:latest
                    docker push hagai211/main-score:latest
                    """
                
                }
            }

        }
    }
}
