pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        
        stage('Start and Test App') {
            steps {
                script {
                    echo 'Starting Flask application in the background...'
                    sh 'python3 app.py > app.log 2>&1 &'

                    // Wait for the server to start
                    sleep 5

                    echo 'Testing the /plot endpoint...'
                    // Use curl to check if the app is running
                    sh 'curl http://localhost:5000/plot'
                    
                    echo 'Stopping the application...'
                    sh 'killall python3'
                }
            }
        }
    }
}
