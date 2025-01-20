from logging import ERROR

from flask import Flask, render_template_string

from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        # Read the score from the file
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read().strip()

        # Create an HTML template for displaying the score
        html_template = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Scores Game</title>
            </head>
                <body>
                    <h1>The score is</h1>
                    <div id='score'> {score}</div>
                </body>
        </html>
        """
        # Render the HTML with the score
        return render_template_string(html_template, score=score), 200

    except FileNotFoundError:
        html_template_error = f"""
                <!DOCTYPE html>
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                        <body>
                            <h1>The score is</h1>
                            <div id='score'> {ERROR}</div>
                        </body>
                </html>
                """
        return html_template_error, BAD_RETURN_CODE

    except Exception as e:
        return f"An error occurred: {str(e)}", 500


if __name__ == '__main__':
    app.run(port=30000)
