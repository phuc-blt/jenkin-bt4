pipeline {
    agent any
    environment {
        GITHUB_WEBHOOK_URL = 'https://bbc0-115-76-50-187.ngrok-free.app/github-webhook/'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/<username>/<repo>.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-app .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8080:8080 --name fastapi-app-container fastapi-app'
            }
        }
        stage('Notify GitHub via Webhook') {
            steps {
                // Gửi request đến webhook của GitHub
                sh """
                curl -X POST $GITHUB_WEBHOOK_URL
                """
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker exec fastapi-app-container pytest /app/app/tests.py'
            }
        }
    }
    post {
        always {
            sh 'docker stop fastapi-app-container || true'
            sh 'docker rm fastapi-app-container || true'
        }
    }
}
