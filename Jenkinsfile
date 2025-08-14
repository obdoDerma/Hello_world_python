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
                    echo 'Starting Flask application...'
                    sh 'python3 app.py > app.log 2>&1 &'

                    // Wait for the server to start (you might need to adjust this)
                    sleep 5

                    echo 'Testing the /plot endpoint...'
                    // Use curl to hit the /plot endpoint and save the output
                    sh 'curl http://localhost:5000/plot > plot_output.html'
                    
                    // Display the output in the Jenkins log
                    sh 'cat plot_output.html'

                    echo 'Stopping the application...'
                    sh 'killall python3'
                }
            }
        }
    }
}
