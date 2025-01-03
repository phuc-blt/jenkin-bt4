pipeline {
    agent any

    triggers {
        GenericTrigger(
            genericVariables: [
                [key: 'WEBHOOK_TRIGGER', value: '$.trigger', defaultValue: '']
            ],
            causeString: 'Triggered by webhook',
            token: 'push_up',
            printContributedVariables: true,
            printPostContent: true
        )
    }

    options {
        skipDefaultCheckout() // Prevent automatic checkout
    }

    stages {
        stage('Start Pipeline') {
            steps {
                script {
                    echo "Pipeline has been triggered."
                    withChecks('Start Pipeline') {
                        publishChecks name: 'Start Pipeline', status: 'IN_PROGRESS', summary: 'Pipeline execution has started.'
                    }
                }
            }
        }

        stage('Fetch Repository') {
            steps {
                script {
                    echo "Cloning the repository..."
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: '*/main']],
                        userRemoteConfigs: [[url: 'https://github.com/phuc-blt/jenkin-bt4.git']]
                    ])
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        echo "Building the Docker image..."
                        sh '''
                        docker build -t fastapi_app .
                        '''
                        withChecks('Build Docker Image') {
                            publishChecks name: 'Build Docker Image', status: 'COMPLETED', conclusion: 'SUCCESS',
                                         summary: 'Docker image built successfully.'
                        }
                    } catch (e) {
                        withChecks('Build Docker Image') {
                            publishChecks name: 'Build Docker Image', status: 'COMPLETED', conclusion: 'FAILURE',
                                         summary: 'Failed to build the Docker image.'
                        }
                        throw e
                    }
                }
            }
        }

        stage('Run FastAPI Container') {
            steps {
                script {
                    try {
                        echo "Starting FastAPI container..."

                        // Remove any previous container with the same name if it exists
                        sh '''
                        if docker ps -a --filter name=fastapi_container | grep -q fastapi_container; then
                            docker stop fastapi_container
                            docker rm fastapi_container
                        fi
                       
                        docker run --name fastapi_container -p 3000:80 -d fastapi_app
                        '''

                        // Check if the container started successfully
                        sh '''
                        docker ps -a --filter name=fastapi_container | grep -q fastapi_container
                        if [ $? -ne 0 ]; then
                            echo "FastAPI container failed to start!"
                            exit 1
                        fi
                        '''

                        withChecks('Run FastAPI Container') {
                            publishChecks name: 'Run FastAPI Container', status: 'COMPLETED', conclusion: 'SUCCESS',
                                         summary: 'FastAPI container is running successfully.'
                        }
                    } catch (e) {
                        withChecks('Run FastAPI Container') {
                            publishChecks name: 'Run FastAPI Container', status: 'COMPLETED', conclusion: 'FAILURE',
                                         summary: 'Failed to start the FastAPI container.'
                        }
                        throw e
                    }
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    try {
                        echo "Running unit tests..."

                        // Wait for the FastAPI container to be ready
                        sleep 10

                        // Run tests inside the container with updated PYTHONPATH
                        sh '''
                        docker exec fastapi_container sh -c "export PYTHONPATH=/app && pytest --junitxml=/app/reports/test-results.xml"
                        '''

                        withChecks('Run Unit Tests') {
                            publishChecks name: 'Run Unit Tests', status: 'COMPLETED', conclusion: 'SUCCESS',
                                         summary: 'All unit tests passed successfully.'
                        }
                    } catch (e) {
                        withChecks('Run Unit Tests') {
                            publishChecks name: 'Run Unit Tests', status: 'COMPLETED', conclusion: 'FAILURE',
                                         summary: 'Some unit tests failed.'
                        }
                        throw e
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                echo "Cleaning up resources..."
                sh '''
                docker stop fastapi_container || true
                docker rm fastapi_container || true
                docker rmi fastapi_app || true
                '''
                withChecks('Pipeline Completion') {
                    publishChecks name: 'Pipeline Completion', status: 'COMPLETED', conclusion: 'NEUTRAL',
                                 summary: 'Pipeline execution is complete. Resources have been cleaned up.'
                }
            }
        }
    }
}
