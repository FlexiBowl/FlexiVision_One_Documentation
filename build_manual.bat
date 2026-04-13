@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "VENV_PYTHON_HOME=%~dp0.venv\Scripts"
set "BUNDLED_PYTHON_HOME=%~dp0runtime\Python312"
set "PYTHON_HOME=%VENV_PYTHON_HOME%"
if not exist "%PYTHON_HOME%\python.exe" set "PYTHON_HOME=%BUNDLED_PYTHON_HOME%"
if not exist "%PYTHON_HOME%\python.exe" set "PYTHON_HOME=%LocalAppData%\Programs\Python\Python312"
set "PATH=%PYTHON_HOME%;%PYTHON_HOME%\Scripts;%PATH%"

pushd "%~dp0"

if "%~1"=="" (
  set "BUILD_TYPE="
  set "BUILD_SCOPE="
  set "BUILD_VERSION="
  set "BUILD_LANGUAGE="
  set "BUILD_CANCELLED="

  for /f "usebackq tokens=1,* delims==" %%A in (`powershell -NoProfile -ExecutionPolicy Bypass -File "tools\manual_publisher\select_build_target.ps1"`) do (
    if /I "%%A"=="BUILD_TYPE" set "BUILD_TYPE=%%B"
    if /I "%%A"=="BUILD_SCOPE" set "BUILD_SCOPE=%%B"
    if /I "%%A"=="VERSION" set "BUILD_VERSION=%%B"
    if /I "%%A"=="LANGUAGE" set "BUILD_LANGUAGE=%%B"
    if /I "%%A"=="CANCELLED" set "BUILD_CANCELLED=%%B"
  )

  if /I "!BUILD_CANCELLED!"=="1" (
    echo Build annullato.
    set "BUILD_STATUS=0"
    popd
    exit /b !BUILD_STATUS!
  )

  if /I "!BUILD_SCOPE!"=="single" (
    "%PYTHON_HOME%\python.exe" "tools\manual_publisher\manual_publisher.py" --mode "!BUILD_TYPE!" --version "!BUILD_VERSION!" --language "!BUILD_LANGUAGE!"
  ) else (
    "%PYTHON_HOME%\python.exe" "tools\manual_publisher\manual_publisher.py" --mode "!BUILD_TYPE!"
  )
) else (
  "%PYTHON_HOME%\python.exe" "tools\manual_publisher\manual_publisher.py" %*
)

set "BUILD_STATUS=%errorlevel%"
popd
exit /b %BUILD_STATUS%
