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
                script {
                    echo 'Running e2e tests...'

                    // Run the test script and capture the exit code
                    def exitCode = sh(script: '.venv/Scripts/python.exe tests/e2e.py', returnStatus: true)

                    if (exitCode == 0) {
                        echo "Test passed! ✅ Continue..."
                    } else {
                        echo "Test failed! ❌ Please check the logs."
                        error("Stopping pipeline due to failed tests.") // Fails the stage explicitly
                    }
                }
            }
        }
        stage('Terminate and Push') {
            steps {
                script {
                    echo 'Terminating containers...'
                    sh 'docker-compose down'
                    // Tag Image and push to docker hub
                    echo 'Tagging and pushing Docker image...'
                    sh """
                    docker tag wog-main-score hagai211/main-score:latest
                    docker push hagai211/main-score:latest
                    """
                
                }
            }

        }
    }
}
