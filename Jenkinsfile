pipeline {
    agent any

    stages {
        stage('Generate Sketch') {
            steps {
                echo 'Generating sketch with Python...'
                sh 'python3 simple_sketch.py'
            }
        }
    }
}
