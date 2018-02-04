from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def puzzle1():
    return render_template("puzzle1.html")

@app.route('/puzzle2')
def puzzle2():
    return render_template("puzzle2.html")

@app.route('/letsgo')
def puzzle3():
    return render_template("puzzle3.html")

@app.route('/hiddenwonder')
def puzzle4():
    return render_template("puzzle4.html")

@app.route('/slumber')
def puzzle5():
    return render_template("puzzle5.html")

@app.route('/lettersforme')
def puzzle6():
    return render_template("puzzle6.html")

if __name__ == "__main__":
    app.run()
