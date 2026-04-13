@echo off
setlocal

powershell -ExecutionPolicy Bypass -File "%~dp0install_dependencies.ps1"
exit /b %errorlevel%
