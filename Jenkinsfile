pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python manage.py test
                '''
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONAR_TOKEN = credentials('sonar-token')
            }
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh '''
                    . venv/bin/activate
                    sonar-scanner \
                      -Dsonar.projectKey=crud \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://localhost:9000 \
                      -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
