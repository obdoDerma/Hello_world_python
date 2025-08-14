pipeline {
    agent any

    stages {
        stage('Build and Run') {
            steps {
                echo 'Building and running the Python project...'
                sh 'python3 --version'
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 app.py'
            }
        }
    }
}
