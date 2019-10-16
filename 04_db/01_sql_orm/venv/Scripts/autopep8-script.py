#!"C:\Users\student\Desktop\바탕화면 정리\TIL\04_db\01_sql_orm\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'autopep8==1.4.4','console_scripts','autopep8'
__requires__ = 'autopep8==1.4.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('autopep8==1.4.4', 'console_scripts', 'autopep8')()
    )
