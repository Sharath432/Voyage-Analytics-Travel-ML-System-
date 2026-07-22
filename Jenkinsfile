pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Repository') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Pipeline Success') {
            steps {
                echo 'Repository cloned successfully.'
                echo 'Jenkins Pipeline Executed Successfully.'
            }
        }
    }
}