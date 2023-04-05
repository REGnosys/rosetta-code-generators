python -m venv .pyenv || goto error
call .pyenv\Scripts\activate.bat || goto error
python -m pip install --upgrade pip || goto error
python -m pip install "setuptools>=62.0" || goto error
python -m pip install yapf || goto error
python -m pip install pytest || goto error
rem python setup.py develop
python -m pip install -e . || goto error


echo.
echo.
echo ***************************************************************************
echo *                                                                         *
echo *                                 SUCCESS!!!                              *
echo *                                                                         *
echo *             Finished installing dependenceis and the cdm module!        *
echo *                                                                         *
echo ***************************************************************************
echo.
goto end

:error
echo.
echo.
echo ***************************************************************************
echo *                                                                         *
echo *                         INITIALISATION FAILED!                          *
echo *                                                                         *
echo ***************************************************************************
echo.
exit /B -1
goto end

:end