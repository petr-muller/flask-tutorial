import subprocess
import tempfile

import click


def register(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands"""
        pass

    @translate.command()
    def update():
        """Update all languages"""
        with tempfile.NamedTemporaryFile() as temp_messages:
            try:
                subprocess.run(
                    [
                        "pybabel",
                        "extract",
                        "-F",
                        "babel.cfg",
                        "-k",
                        "_l",
                        "-o",
                        temp_messages.name,
                        ".",
                    ],
                    check=True,
                )
                subprocess.run(
                    ["pybabel", "update", "-i", temp_messages.name, "-d", "app/translations"],
                    check=True,
                )
            except subprocess.CalledProcessError as exc:
                raise RuntimeError(exc)

    @translate.command()
    def compile():
        """Compile all translations"""
        try:
            subprocess.run(["pybabel", "compile", "-d", "app/translations"], check=True)
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(exc)

    @translate.command()
    @click.argument("lang")
    def init(lang):
        """Initialize a new language"""
        with tempfile.NamedTemporaryFile() as temp_messages:
            try:
                subprocess.run(
                    [
                        "pybabel",
                        "extract",
                        "-F",
                        "babel.cfg",
                        "-k",
                        "_l",
                        "-o",
                        temp_messages.name,
                        ".",
                    ],
                    check=True,
                )
                subprocess.run(
                    ["pybabel", "init", "-i", temp_messages.name, "-d", "app/translations", "-l", lang],
                    check=True,
                )
            except subprocess.CalledProcessError as exc:
                raise RuntimeError(exc)
