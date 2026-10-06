# This file must be used with "source bin/activate.csh" *from csh*.
# You cannot run it directly.

# Created by Davide Di Blasi <davidedb@gmail.com>.
# Ported to Python 3.3 venv by Andrew Svetlov <andrew.svetlov@gmail.com>

alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; unsetenv VIRTUAL_ENV_PROMPT; test "\!:*" != "nondestructive" && unalias deactivate'

# Unset irrelevant variables.
deactivate nondestructive

setenv VIRTUAL_ENV /home/airfiel/Documents/cours/master/m1-1/ia/package-python-TD1/vanillecorrectRepo/Algo_groupe2/Algo_groupe2/test_env

set _OLD_VIRTUAL_PATH="$PATH"
setenv PATH "$VIRTUAL_ENV/"bin":$PATH"
setenv VIRTUAL_ENV_PROMPT test_env


if ($?prompt) then
    set _OLD_VIRTUAL_PROMPT="$prompt"

    if (! "$?VIRTUAL_ENV_DISABLE_PROMPT") then
        set prompt = "("test_env") $prompt:q"
    endif
endif

alias pydoc python -m pydoc

rehash
