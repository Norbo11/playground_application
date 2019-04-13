#!/usr/local/bin/zsh
openapi-generator generate -i playground_application/openapi/openapi.yaml -g python-flask -o . -DpackageName=playground_application -Dmodels -DsupportingFiles
