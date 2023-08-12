import sys
import os
def _resolve_captcha(self):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    api_key = os.getenv('1abc234de56fab7c89012d34e56fa7b8', '59cf0add01e1fa16e946773a3f5bc079')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey='6LdJtY8UAAAAADTgIWYnG_VKkfNqqB-w8CdQFL7Y',
            url='https://phptravels.org/register.php')

    except Exception as e:
        sys.exit(e)

    else:
        sys.exit(str(result))
