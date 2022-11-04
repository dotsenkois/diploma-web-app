pipeline {
  agent none
  options {
  skipStagesAfterUnstable()
  skipDefaultCheckout()
}
  environment { ... }
  stages {
    stage("Prepare container") {
      agent {
        docker {
          image 'openjdk:11.0.5-slim'
          args '-v $HOME/.m2:/root/.m2'
        }
      }
      stages {
        stage('Build') { ... }
        stage('Test') { ... }
        stage('Package') { ... }
      }
    }

    stage('Push images') {
      agent any
      when { branch 'master' }
      steps { ... }
    }

    stage('Trigger kubernetes') {
      agent any
      when { branch 'main' }
      steps { ... }
    }
  }
}