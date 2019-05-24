#!/usr/local/bin/zsh
openapi-generator generate -i playground_application/openapi/uber.yaml -g python-flask -o . -DpackageName=playground_application -Dmodels -DsupportingFiles
