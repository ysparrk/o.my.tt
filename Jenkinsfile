pipeline {
    // 스테이지 별로 다른 거
    agent any

    // 3분 주기로 pipeline 구동
    triggers {
        pollSCM('*/3 * * * *')
    }

    // 환경변수
    environment {
      // AWS 명령어를 자유롭게 쓰기 위함
      AWS_ACCESS_KEY_ID = credentials('awsAccessKeyId')
      AWS_SECRET_ACCESS_KEY = credentials('awsSecretAccessKey')
      // 서울
      AWS_DEFAULT_REGION = 'ap-northeast-2'
      HOME = '.' // Avoid npm root owned
    }

    // pipeline 구성
    stages {
        // 레포지토리를 다운로드 받음
        stage('Prepare') {
            agent any
            
            steps {
                echo 'Clonning Repository'
                // git pull 
                git url: 'https://github.com/ysparrk/o.my.tt.git',
                    branch: 'master',
                    credentialsId: 'git_token_for_jenkins'
            }

            post {
                // If Maven was able to run the tests, even if some of the test
                // failed, record the test results and archive the jar file.
                success {
                    echo 'Successfully Cloned Repository'
                }

                always { 
                  echo "i tried..."
                }

                cleanup {  // 완료
                  echo "after all other post condition"
                }
            }
        }
      
        // aws s3 에 파일을 올림
        stage('Deploy Frontend') {
          steps {
            echo 'Deploying Frontend'
            // 프론트엔드 디렉토리의 정적파일들을 S3 에 올림, 이 전에 반드시 EC2 instance profile 을 등록해야함.
            dir ('./website'){
                sh '''
                aws s3 sync ./ s3://ysparrk
                '''
            }
          }

          post {
              // If Maven was able to run the tests, even if some of the test
              // failed, record the test results and archive the jar file.
              success {
                  echo 'Successfully Cloned Repository'

                  mail  to: 'youngseo0703@gmail.com',
                        subject: "Deploy Frontend Success",
                        body: "Successfully deployed frontend!"

              }

              failure {
                  echo 'I failed :('

                  mail  to: 'youngseo0703@gmail.com',
                        subject: "Failed Pipelinee",
                        body: "Something is wrong with deploy frontend"
              }
          }
        }

        stage('Lint Backend') {
            // Docker plugin and Docker Pipeline 두개를 깔아야 사용가능!
            agent {
              docker {
                image 'node:latest'
              }
            }
            
            steps {
              dir ('./server'){
                  sh '''
                  npm install&&
                  npm run lint
                  '''
              }
            }
        }
        
        stage('Test Backend') {
          agent {
            docker {
              image 'node:latest'
            }
          }
          steps {
            echo 'Test Backend'

            dir ('./server'){
                sh '''
                npm install
                npm run test
                '''
            }
          }
        }
        // docker build
        stage('Bulid Backend') {
          agent any
          steps {
            echo 'Build Backend'

            dir ('./server'){ // server 라는 이름으로 빌드
                sh """
                docker build . -t server --build-arg env=${PROD}
                """
            } // multi 배포 환경에서 관리하는 것이 중요 -> arg
          }

          post {
            failure { // 빌드하다 실패하면 error 메세지 띄우고, 나머지 파이프라인 종료한다
              error 'This pipeline stops here...'
            }
          }
        }
        
        // 배포
        stage('Deploy Backend') {
          agent any

          steps {
            echo 'Build Backend'

            dir ('./server'){ // 원래 떠있던 이미지 지우고 실행
                sh '''
                // docker rm -f $(docker ps -aq) 
                docker run -p 80:80 -d server
                '''
            }
          }

          post {
            success {
              mail  to: 'youngseo0703@gmail.com',
                    subject: "Deploy Success",
                    body: "Successfully deployed!"
                  
            }
          }
        }
    }
}
