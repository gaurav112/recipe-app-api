"""
Test Custom Django management commands
"""
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error # noqa

from django.core.management import call_command
from django.db.utils import OperationalError # noqa
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):

    # Disabled: to enable add "test_" prefix
    def wait_for_db_ready(self, patched_check):
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])
