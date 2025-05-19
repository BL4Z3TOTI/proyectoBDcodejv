import re

texto = "Esto tiene ba9, una be7 y también bx2."
patron = r"\bb[aeiou]\d\b"
coincidencias = re.findall(patron, texto)
print(coincidencias)
