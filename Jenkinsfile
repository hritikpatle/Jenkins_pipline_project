pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/hritikpatle/Jenkins_pipline_project'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('SonarCloud Analysis') {
            steps {
                withSonarQubeEnv('SonarCloud') {
                    sh 'mvn sonar:sonar -Dsonar.projectKey=your_project_key -Dsonar.organization=your_org -Dsonar.login=$SONAR_TOKEN'
                }
            }
        }
    }
}
