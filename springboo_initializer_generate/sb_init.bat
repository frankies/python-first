@echo off
set "output=%cd%"
set "sdir=%~dp0"
Pushd %output%
cd /d %sdir%  
python springboot_main.py -o %output% --prog %~nx0 %*
popd
@echo on