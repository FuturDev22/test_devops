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

        stage('Security Scan') {
            steps {
                script {
                    // Lancer un scan via l'API OWASP ZAP
                    def target_url = 'https://tnhldapp0144.interpresales.mysoprahronline.com/GP4You/login'
                    def zap_api_url = "http://owasp_zap:8084/JSON/ascan/action/scan/?url=${target_url}"
                    def scan_response = sh(script: "curl -s ${zap_api_url}", returnStdout: true).trim()

                    if (scan_response.contains('"code":"OK"')) {
                        echo "Scan started successfully."
                    } else {
                        error "Failed to start scan. Response: ${scan_response}"
                    }

                    // Attendre que le scan soit terminé
                    sleep 60
                }
            }
        }

        stage('Generate Report') {
            steps {
                script {
                    // Récupérer le rapport OWASP ZAP
                    def report_url = 'http://owasp_zap:8084/OTHER/core/other/htmlreport/'
                    sh "curl -s ${report_url} -o zap_report.html"
                }
            }
        }

        stage('Publish Reports') {
            steps {
                // Publier le rapport OWASP ZAP dans Jenkins
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'zap_report.html',
                    reportName: 'OWASP ZAP Report'
                ])
            }
        }

        stage('Run Tests on Edge') {
            steps {
                script {
                    sh 'docker exec selenium-pytest-container-bdd-qa /bin/bash -c "source venv/bin/activate && coverage run -m pytest --browser edge ./tests/test_login_bdd.py --alluredir allure-results && coverage xml -o coverage.xml" | tee edge_tests.log'
                    sh 'docker cp selenium-pytest-container-bdd-qa:/app/coverage.xml /var/jenkins_home/workspace/4you_devops_test_bdd_pipeline_3'
                    sh 'sleep 10'
                    sh 'docker-compose stop edge-video && docker-compose rm -f edge-video'
                }
            }
        }

        stage('Run Tests on chrome') {
            steps {
                script {
                    sh 'docker exec selenium-pytest-container-bdd-qa /bin/bash -c "source venv/bin/activate && pytest --browser chrome ./tests/test_login_bdd.py --cov --alluredir allure-results" | tee chrome_tests.log'
                    sh 'sleep 10'
                    sh 'docker-compose stop chrome-video && docker-compose rm -f chrome-video'
                }
            }
        }

        stage('Run Tests on firefox') {
            steps {
                script {
                    sh 'docker exec selenium-pytest-container-bdd-qa /bin/bash -c "source venv/bin/activate && pytest --browser firefox ./tests/test_login_bdd.py --cov --alluredir allure-results" | tee firefox_tests.log'
                    sh 'sleep 10'
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
                    sh 'docker cp selenium-pytest-container-bdd-qa:/app/allure-results /var/jenkins_home/workspace/4you_devops_test_bdd_pipeline_3'
                    allure([includeProperties: false, jdk: '', properties: [], reportBuildPolicy: 'ALWAYS', results: [[path: 'allure-results']]])
                }
            }
        }
    }
}
