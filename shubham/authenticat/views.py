from django.shortcuts import render

import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCHtq_sCiVd0PTKJBTtSK7sk9F-m6nf-LA",
  'authDomain': "projector-82c6b.firebaseapp.com",
  'databaseURL': "https://projector-82c6b.firebaseio.com",
  'projectId': "projector-82c6b",
  'storageBucket': "projector-82c6b.appspot.com",
  'messagingSenderId': "263780088826",
  'appId': "1:263780088826:web:89dc086406b11d1b",
  "type": "service_account",
  "project_id": "projector-82c6b",
  "private_key_id": "f333fe375cc8146bfb4699ab0c45ded9442bb564",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCmTR1TLAKCkdmu\nMM1G2LoJAh+eMZEJw+0E+uwL8JltuJ394j5rWZtNAWrXdSR1n4zQ0d1Jouz6uVSl\n/F98oiuECfE3uFetDCr4lTGEm1lLe3XWMagA1Y9ph8T6CFxM5YdoxezMlrzE2PVM\ny/M6QhkbZMdUS5fqv8yCKb1VBcZFFBP4jCGeatRQMt3V0ugnL8BiX0dlOis8tFlN\nG8JkFePy/zR6ZiVFFDEzWJsFFDJUFVljdU2wdaWC/3mH1JWO2VJagjVR5FgLobp/\nu+n2bfE2MMGCDrySG7J7E0mJsgQ6J80aGtkM6LRjEwmDf+/P8lewOOa+HYGzkpJ/\nNqgsYoIbAgMBAAECggEAOuFq1Jvsd5Z0YDxfMgpiM/ZQg45BMBfyv6SoFsIlULfh\nGJcWSqP7XJR347lSI2NOVFE57GyHQ26DDhIBLPuuNJ3gjj3yrQ512HXahn0KbLNV\n0XTbaxAyKscrcuuq4n8SJoKNiRKF25yFnZ9IiwQEJ7LS8IGjVDZ8jkmBA617udED\n6MWhWWvdhdrobceoZWyaEesulFviGimovb/z25ZhBA0ic94tOBTWTnO5O/a5Gy+o\nD04hPFjbWSTXft2RezTuteoOhPKkh66HVp8nIqHk74pq+dTqiC/9FSBeMi1vQuxt\n7/0GrAZFxEiocv6HzHqOLQMxzffsyzHLWHPq2dEKYQKBgQDTqa5K+hTtpm++e456\nJ306vt0TaRnjSUU6QYRz2naKh91gP+H9zA/QnsUOYFcGyaL6Q8tl6E21Y42FnMTQ\nzybst2rib3iBq7Wo8OHG5Q7T1bNdwER/JjnM1o7DWRirwYbyol1FDH0qZpcDPbC5\nLBfi1Sx4EcsU738dCvCJpfULNQKBgQDJIvCdU718jgspfrfOdK0C5Zodv41YFH2F\nFMMy33mzEIJFMO7ZbOcXr1dQoTWAbS4Q76t89YsDj+5krKZLEq3rMCrTGBIl9cyS\nAjm0MVrLdIg3zOl67UnxPJMjh836KSctNR189DrMo5RJwHV3NrFuG8XK79KBNT3i\nV9Fm98yyDwKBgQCZuPlRkNEUTDWJ5Rh0FSv5N1c+Wq2nibZSefTlYzuGnugjmCHc\nfpDZ1gWNzGBIGLdaBVS6nX2aiEPnTxUOBfTiJM/mxkiB/KBBoziGiCM9rE3Jf/L/\nWVbPMuCadaHaVAJbQ5pzpH9fBQUWIH6x7Zknb+UNCvcwLERoZmKNxc7zJQKBgDtK\ngHFwOQBZgvLVdut2O3YKJtc0Gz9msuWjDDOX6vEdIbmxxgbz8l9qAaw0CWh1RsoZ\nTI0GeNcw+45T0qV4uSoGRel6RAdKoOY9n7L9hY1KKcmBLyZcgpqJR7qGkvJ2ZSUP\nbkTiXd7rLZBcGoRs6/rQVwsOjRgnkLmDN6hJzd6DAoGAX1ehpGvV+jAsrKQFHyDI\nQ5dCXMoketFj7fpv3Fsj/MIPGTMCxOxqwaXYQaPPiP7fs7XJGlxTFNxheNtF1kVm\nmJirDAzEqUXivPsp9mJxwml01yTJlQY1rq38gdfWENKQQlyvWOIEMpzx0KlK8qjF\nuT/OagoMMUZWaVfvTqpemjk=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-dq7c7@projector-82c6b.iam.gserviceaccount.com",
  "client_id": "112597872325717784399",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-dq7c7%40projector-82c6b.iam.gserviceaccount.com"
}

firebase = pyrebase.initialize_app(config)
