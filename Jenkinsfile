pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    git credentialsId: 'sopra', url: 'https://github.com/FuturDev22/test_devops.git', branch: 'main'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('selenium-pytest-project-qa-bdd')
                }
            }
        }

        stage('Prepare Selenium Grid test Environment') {
            steps {
                script {
                    // Arrêter et démarrer Selenium Grid à l'aide de Docker Compose
                    sh 'docker-compose stop'
                    sh 'sleep 5'
                    sh 'docker-compose up -d --build'
                    sh 'sleep 25'
                }
            }
        }
        
        stage('Run Tests on Edge') {
            steps {
                script {
                    sh 'docker exec selenium-pytest-container-bdd-qa /bin/bash -c "source venv/bin/activate && coverage run -m pytest --browser edge ./tests/test_login_bdd.py --alluredir allure-results && coverage xml -o coverage.xml" | tee edge_tests.log'
                    sh 'docker cp selenium-pytest-container-bdd-qa:/app/coverage.xml /var/jenkins_home/workspace/4you_devops_test_bdd_pipeline_3'
                    sh'sleep 10'
                    sh 'docker-compose stop edge-video && docker-compose rm -f edge-video'
                }
            }
        }


        stage('Run Tests on chrome') {
            steps {
                script {
                    sh 'docker exec selenium-pytest-container-bdd-qa /bin/bash -c "source venv/bin/activate && pytest --browser chrome ./tests/test_login_bdd.py --cov --alluredir allure-results" | tee chrome_tests.log'
                    sh'sleep 10'
                    sh 'docker-compose stop chrome-video && docker-compose rm -f chrome-video'
                }
            }
        }

        stage('Run Tests on firefox') {
            steps {
                script {
                    sh 'docker exec selenium-pytest-container-bdd-qa /bin/bash -c "source venv/bin/activate && pytest --browser firefox ./tests/test_login_bdd.py --cov --alluredir allure-results" | tee firefox_tests.log'
                    sh'sleep 10'
                    sh 'docker-compose stop firefox-video && docker-compose rm -f firefox-video'
                }
            }
        }

        stage('Run OWASP ZAP Scan') {
            steps {
                script {
                    sh 'docker exec owasp-zap zap-cli report -o zap_report.html -f html'
                }
                archiveArtifacts artifacts: 'zap_report.html', allowEmptyArchive: true
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
                    sh 'docker cp selenium-pytest-container-bdd-qa:/app/allure-results /var/jenkins_home/workspace/4you_devops_test_bdd_pipeline_3'
                    allure([includeProperties: false, jdk: '', properties: [], reportBuildPolicy: 'ALWAYS', results: [[path: 'allure-results']]])
                }
            }
        }
    }
}
