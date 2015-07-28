@echo off
rem Third argument is any inject code you want.

rem Read the contents of PYTHON_PATH into %PYTHON_PATH%:
set /P PYTHON_PATH=<PYTHON_PATH

%PYTHON_PATH% inject.py base.localAvatar.collisionsOff()
pause
