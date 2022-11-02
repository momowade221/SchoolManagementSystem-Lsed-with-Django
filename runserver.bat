REM set root=C:\ProgramData\Anaconda3

REM call %root%\Scripts\activate.bat %root%

call conda activate base

call python manage.py runserver

pause