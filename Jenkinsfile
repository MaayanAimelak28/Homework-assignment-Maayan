pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the repository to fetch the latest code
                git 'https://github.com/MaayanAimelak28/Homework-assignment.git'
            }
        }
        stage('Setup Environment') {
            steps {
                // Setting up the environment using Vagrant to spin up the required VMs
                sh 'vagrant up'
            }
        }
        stage('Test Environment') {
            steps {
                // Running tests using a Python script to verify that the environment worked correctly
                sh 'python3 scripts/test.py'
            }
        }
    }
}


