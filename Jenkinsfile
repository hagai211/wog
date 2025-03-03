pipeline {
    agent any

    stages {
        stage('checkout repo') {
            steps {
                checkout scm
            }
        }
        stage('build docker image') {
            steps {
                sh 'docker build -t scores-server .'
            }
        }
        stage('run docker image') {
            steps {
                // Creates a dummy Scores.txt file
                sh 'docker run -d -p 8777:30000 -v "./Scores.txt:/scores/Scores.txt" scores-server'
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
        stage('Finalize') {
            steps {
                script {
                    echo 'Terminating containers...'
                    sh "docker stop \$(docker ps -q --filter ancestor=scores-server:latest) || true"
                    // Tag Image and push to docker hub
                    echo 'Tagging and pushing Docker image...'
                    sh """
                    docker tag scores-server hagai211/scores-server:latest
                    docker push hagai211/scores-server:latest
                    """
                
                }
            }

        }
    }
}
