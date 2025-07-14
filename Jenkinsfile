pipeline {
    agent any

    environment {
        SONAR_SCANNER_HOME = tool 'SonarQubeScanner'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/hritikpatle/Jenkins_pipline_project'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'python3 -m unittest discover tests'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    sh "${SONAR_SCANNER_HOME}/bin/sonar-scanner"
                }
            }
        }

        stage('Build Package') {
            steps {
                sh 'zip -r demo-package.zip index.html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'demo-package.zip', fingerprint: true
            junit 'tests/*.xml'
        }
    }
}

