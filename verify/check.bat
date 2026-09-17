@echo off
:: ============================================================
::  Verify a GDPR Auditor finding's citation
::  Usage: drag a findings file onto this, OR double-click to
::         be prompted for the file path.
::
::  Checks that each citation in the file points to a real
::  line in reference/, and that the quoted text actually
::  appears there. Prints PASS or FAIL for each one, and if a
::  citation is wrong, shows what that line actually says.
::
::  This is a spot-check tool, not part of running a normal
::  audit. See verify\README.md for what a findings file
::  should look like.
:: ============================================================
setlocal

set "SCRIPT_DIR=%~dp0"
set "SCRIPT=%SCRIPT_DIR%check.py"

if "%~1"=="" goto promptfile
set "FINDINGS=%~1"
goto run

:promptfile
echo ============================================================
echo  GDPR Auditor - Citation Verifier
echo ============================================================
echo.
set /p FINDINGS=Drag and drop your findings file here, or type the full path:
set "FINDINGS=%FINDINGS:"=%"

:run
if not exist "%FINDINGS%" (
    echo.
    echo [ERROR] File not found: %FINDINGS%
    pause
    exit /b 1
)

where python >nul 2>nul
if errorlevel 1 (
    echo.
    echo [ERROR] Python was not found on this computer.
    echo This tool needs Python 3 installed to run. See verify\README.md.
    pause
    exit /b 1
)

echo.
python "%SCRIPT%" "%FINDINGS%"

echo.
pause
