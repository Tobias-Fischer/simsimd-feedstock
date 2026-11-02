@echo on
copy "%RECIPE_DIR%\simsimd.py" "%SP_DIR%\simsimd.py"
if errorlevel 1 exit 1
