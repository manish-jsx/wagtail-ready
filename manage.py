#!/usr/bin/env python


import os
import sys
from dotenv import load_dotenv

# Load environment variables before Django setup
load_dotenv()

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "cms.settings.dev" if os.environ.get("DEVELOPMENT") else "cms.settings.production",
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

