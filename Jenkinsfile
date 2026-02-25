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
        sh 'javac Calculator.java'
      }
    }
    stage('build'){
      steps{
        sh 'java Calculator 10 5'
      }
    }
    stage('test'){
      steps{
        sh 'java Calculator 10 -5'
      }
    }
    stage('deploy'){
      steps{
       echo 'Deployment completed'
      }
    }
  }
}
