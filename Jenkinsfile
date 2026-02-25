pipeline{
  agent any
  stages{
    stage('clone'){
      steps{
        git branch:'main',url:'https://github.com/AmearShaik/calculator.git';
      }
    }
    stage('compile'){
      steps{
        sh 'javac calculator.java'
      }
    }
    stage('build'){
      steps{
        sh 'java calculator 10 5'
      }
    }
    stage('test'){
      steps{
        sh 'java calculator 10 -5'
      }
    }
    stage('deploy'){
      steps{
       echo 'Deployment completed'
      }
    }
  }
}
