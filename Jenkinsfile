pipeline {
    agent any

    environment {
        WORKSPACE = '/var/jenkins_home/workspace/4you_devops_test_bdd_pipeline_3'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'sopra', url: 'https://github.com/FuturDev22/test_devops.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('selenium-pytest-project-qa-bdd')
                }
            }
        }

        stage('Prepare Selenium Grid Test Environment') {
            steps {
                script {
                    // Restart Selenium Grid using Docker Compose
                    sh 'docker-compose down'
                    sh 'docker-compose up -d --build'
                    sleep 25
                }
            }
        }
       
        stage('Run ZAP Baseline Scan') {
            steps {
                script {
                    sh """
                    docker run --rm --name zap --network devops -v \$(pwd):/zap/wrk -u zap -p 8083:8083 \
                    -t ghcr.io/zaproxy/zaproxy zap-baseline.py -t https://tnhldapp0144.interpresales.mysoprahronline.com/GP4You/login \
                    -r zap-report.html -d -port 8083
                    """
                }
            }
        }
        
        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'zap-report.html', allowEmptyArchive: true
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '',
                    reportFiles: 'zap-report.html',
                    reportName: 'OWASP ZAP Report'
                ])
            }
        }
        
        stage('Run Tests on Edge') {
            steps {
                script {
                    sh 'docker exec selenium-pytest-container-bdd-qa /bin/bash -c "source venv/bin/activate && coverage run -m pytest --browser edge ./tests/test_login_bdd.py --alluredir allure-results && coverage xml -o coverage.xml" | tee edge_tests.log'
                    sh "docker cp selenium-pytest-container-bdd-qa:/app/coverage.xml ${WORKSPACE}"
                    sh 'docker-compose stop edge-video && docker-compose rm -f edge-video'
                }
            }
        }

        stage('Run Tests on Chrome') {
            steps {
                script {
                    sh 'docker exec selenium-pytest-container-bdd-qa /bin/bash -c "source venv/bin/activate && pytest --browser chrome ./tests/test_login_bdd.py --cov --alluredir allure-results" | tee chrome_tests.log'
                    sh 'docker-compose stop chrome-video && docker-compose rm -f chrome-video'
                }
            }
        }

        stage('Run Tests on Firefox') {
            steps {
                script {
                    sh 'docker exec selenium-pytest-container-bdd-qa /bin/bash -c "source venv/bin/activate && pytest --browser firefox ./tests/test_login_bdd.py --cov --alluredir allure-results" | tee firefox_tests.log'
                    sh 'docker-compose stop firefox-video && docker-compose rm -f firefox-video'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'sonarqube'
                    withSonarQubeEnv('sonarqube') {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=testing \
                            -Dsonar.sources=./tests \
                            -Dsonar.host.url=http://sonarqube:9000 \
                            -Dsonar.login=sqa_421c1c3215045f8c9c84f88166be7aae228e13b8 \
                            -Dsonar.python.coverage.reportPaths=coverage.xml"
                    }
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    sh "docker cp selenium-pytest-container-bdd-qa:/app/allure-results ${WORKSPACE}"
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }
}
