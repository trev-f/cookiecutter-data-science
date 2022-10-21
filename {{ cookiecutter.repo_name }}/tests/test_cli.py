from click.testing import CliRunner
from {{ cookiecutter.repo_name }}.cli import cli


def test_say_hello():
    runner = CliRunner()
    result = runner.invoke(cli, ["say-hello"])
    assert result.exit_code == 0
    assert "Hello World" in result.output


def test_make_dataset():
    runner = CliRunner()
    result = runner.invoke(cli, ["make-dataset"])
    assert result.exit_code == 0
    assert "Make dataset!" in result.output
