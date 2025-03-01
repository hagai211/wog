pipeline {
    agent any

    stages {
        stage('Create a new file') {
            steps {
                sh 'touch new_file.txt'
            }
        }
        stage('Print messege') {
            steps {
                echo 'Hello from pipeline'
            }
        }
    }
}
