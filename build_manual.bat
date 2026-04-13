@echo off
setlocal EnableExtensions EnableDelayedExpansion

set "REPO_ROOT=%~dp0"
set "VENV_PYTHON_EXE=%REPO_ROOT%.venv\Scripts\python.exe"
set "LOCAL_PYTHON_EXE=%LocalAppData%\Programs\Python\Python312\python.exe"
set "PYTHON_CMD="
set "PYTHON_LABEL="
set "BUNDLED_PYTHON_EXE="
set "AUTO_SETUP_RAN=0"

call :resolve_python
if errorlevel 1 exit /b 1

pushd "%REPO_ROOT%"

call :ensure_dependencies
if errorlevel 1 (
  set "BUILD_STATUS=1"
  popd
  exit /b !BUILD_STATUS!
)

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
    call !PYTHON_CMD! "tools\manual_publisher\manual_publisher.py" --mode "!BUILD_TYPE!" --version "!BUILD_VERSION!" --language "!BUILD_LANGUAGE!"
  ) else (
    call !PYTHON_CMD! "tools\manual_publisher\manual_publisher.py" --mode "!BUILD_TYPE!"
  )
) else (
  call !PYTHON_CMD! "tools\manual_publisher\manual_publisher.py" %*
)

set "BUILD_STATUS=%errorlevel%"
popd
exit /b %BUILD_STATUS%

:resolve_python
set "PYTHON_CMD="
set "PYTHON_LABEL="
set "BUNDLED_PYTHON_EXE="

for /d %%D in ("%REPO_ROOT%runtime\Python*") do (
  if exist "%%~fD\python.exe" if not defined BUNDLED_PYTHON_EXE set "BUNDLED_PYTHON_EXE=%%~fD\python.exe"
)

if exist "%VENV_PYTHON_EXE%" (
  set "PYTHON_CMD="%VENV_PYTHON_EXE%""
  set "PYTHON_LABEL=%VENV_PYTHON_EXE%"
) else if defined BUNDLED_PYTHON_EXE (
  set "PYTHON_CMD="%BUNDLED_PYTHON_EXE%""
  set "PYTHON_LABEL=%BUNDLED_PYTHON_EXE%"
) else if exist "%LOCAL_PYTHON_EXE%" (
  set "PYTHON_CMD="%LOCAL_PYTHON_EXE%""
  set "PYTHON_LABEL=%LOCAL_PYTHON_EXE%"
)

if not defined PYTHON_CMD (
  python --version >nul 2>&1
  if not errorlevel 1 (
    set "PYTHON_CMD=python"
    set "PYTHON_LABEL=python"
  )
)

if not defined PYTHON_CMD (
  py -3 --version >nul 2>&1
  if not errorlevel 1 (
    set "PYTHON_CMD=py -3"
    set "PYTHON_LABEL=py -3"
  )
)

if defined PYTHON_CMD exit /b 0

echo Nessun interprete Python compatibile trovato per la build.
echo.
echo Percorsi controllati:
echo   - .venv\Scripts\python.exe
echo   - runtime\Python*\python.exe
echo   - %LocalAppData%\Programs\Python\Python312\python.exe
echo   - comando python nel PATH
echo   - launcher py -3
echo.
echo Installa Python 3 e poi rilancia build_manual.bat.
exit /b 1

:ensure_dependencies
call !PYTHON_CMD! -c "import sphinx, myst_parser, sphinx_book_theme, sphinx_copybutton, sphinx_design, sphinxcontrib.video" >nul 2>&1
if not errorlevel 1 exit /b 0

if "!AUTO_SETUP_RAN!"=="1" (
  echo Le dipendenze Python richieste dal publisher non risultano installate per !PYTHON_LABEL! anche dopo il setup automatico.
  echo Controlla l'output di installer\install_dependencies.bat e riprova.
  exit /b 1
)

echo Ambiente Python non pronto per la build su !PYTHON_LABEL!.
echo Avvio automaticamente installer\install_dependencies.bat per preparare la .venv locale...
call installer\install_dependencies.bat
if errorlevel 1 (
  echo Setup automatico fallito.
  exit /b 1
)

set "AUTO_SETUP_RAN=1"
call :resolve_python
if errorlevel 1 exit /b 1

call !PYTHON_CMD! -c "import sphinx, myst_parser, sphinx_book_theme, sphinx_copybutton, sphinx_design, sphinxcontrib.video" >nul 2>&1
if not errorlevel 1 exit /b 0

echo Le dipendenze Python richieste dal publisher non risultano installate per !PYTHON_LABEL! anche dopo il setup automatico.
echo Controlla l'output di installer\install_dependencies.bat e riprova.
exit /b 1
