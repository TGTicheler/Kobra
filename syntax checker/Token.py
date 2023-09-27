LHAAK = 'LINKER HAAKJE'
RHAAK = 'RECHTER HAAKJE'
SLASH = 'SLASH'
VAR = 'VARIABELE'









class Token:
    def __init__(self, soort):
        self.soort = soort

    def __repr__(self):
        return f'{self.soort}'
