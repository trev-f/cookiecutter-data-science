from click.testing import CliRunner
from {{ cookiecutter.repo_name }}.cli import cli


def test_make_dataset():
    runner = CliRunner()
    result = runner.invoke(cli, ["make-dataset"])
    assert result.exit_code == 0
    assert "Make dataset!" in result.output
