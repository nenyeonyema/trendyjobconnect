#!/usr/bin/python3
""" Main entry to our flask app
"""
from website import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True, port=8000)
