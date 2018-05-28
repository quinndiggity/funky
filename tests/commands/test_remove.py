"""Tests for remove command."""

import json
import os
import unittest.mock as mock

import pytest

from localalias import commands
import shared

pytestmark = pytest.mark.usefixtures("debug_mode")


@pytest.fixture
def remove_cmd(cmd_args):
    """Builds and returns 'remove' command."""
    cmd = commands.Remove(cmd_args.alias, color=cmd_args.color)
    return cmd


def test_remove(cleandir, fake_db, remove_cmd):
    """Tests remove command."""
    remove_cmd()
    loaded_aliases = shared.load_aliases()
    assert remove_cmd.alias not in loaded_aliases


def test_remove_db(cleandir, alias_dict, fake_db):
    """Tests that local alias database is removed when last alias is removed."""
    assert os.path.isfile(commands.Command.LOCALALIAS_DB_FILENAME)

    for alias in alias_dict:
        remove_cmd = commands.Remove(alias)
        remove_cmd()

    assert not os.path.isfile(commands.Command.LOCALALIAS_DB_FILENAME)