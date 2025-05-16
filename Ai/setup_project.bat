@echo off
set "root=AI_Commerce_Project"

:: Create root directory
mkdir %root%
cd %root%

:: High-level folders
mkdir configs
mkdir data
mkdir data\raw
mkdir data\processed
mkdir models
mkdir notebooks

:: Source code structure
mkdir src
mkdir src\data
mkdir src\features
mkdir src\training
mkdir src\evaluation
mkdir src\inference
mkdir src\utils

:: API
mkdir api
mkdir api\routes
mkdir api\services

:: Frontend
mkdir web

:: Testing
mkdir tests

:: Deployment infrastructure
mkdir infra
mkdir infra\docker
mkdir infra\k8s
mkdir infra\ci_cd

:: Supporting folders
mkdir logs
mkdir scripts
mkdir docs

:: Create placeholder files
echo. > .gitignore
echo. > requirements.txt
echo. > Dockerfile
echo. > docker-compose.yml
echo. > README.md
echo. > setup.py

echo Project structure for %root% created successfully.
pause
