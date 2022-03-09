pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'sudo bash .Jenkinsfile/run_python.sh'
            }
        }
    }
}
