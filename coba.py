

import re

email = "test@gmail.com"
pola_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(pola_email, email):
    print("Email valid")
else:
    print("Email tidak valid")



