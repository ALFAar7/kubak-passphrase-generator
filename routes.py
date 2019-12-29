from flask import Flask, render_template, request
from passgencore import PassGen
#from elasticapm.contrib.flask import ElasticAPM


app = Flask(__name__)
#apm = ElasticAPM(app, SERVER_URL='http://localhost:8200', SECRET_TOKEN='xxVpmQB2HMzCL9PgBHVrnxjNXXw5J7bd79DFm6sjBJR5HPXDhcF8MSb3vv4bpg44')


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/<name>")
def index_route(name):
  return render_template("index.html", name=index)


@app.route("/generator/<name>", methods=['GET','POST'])
def generator_route(name):
    return render_template("generator.html", name=generator)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html')


@app.route("/generator", methods=['GET','POST'])
def generator():
    if request.method == "GET":
        return render_template("generator.html")
    elif request.method == "POST":
        gender = request.form['gender']
    else:
        return render_template("generator.html")

    if gender == 'auto':
        pass_var = PassGen.auto_gen()
        return render_template("generator.html", formvar=pass_var)
    elif gender == 'lenght':
        lenght_num = request.form['lname']
        pass_var = PassGen.len_gen(lenght_num)
        return render_template("generator.html", formvar=pass_var)
    elif gender == 'spchar':
        lenght_num = request.form['olname']
        lenght_spchar = request.form['osname']
        pass_var = PassGen.spc_gen(lenght_num, lenght_spchar)
        return render_template("generator.html", formvar=pass_var)
    else:
        pass_var = PassGen.auto_gen()
        return render_template("generator.html", formvar=pass_var)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port='8080')
  # app.run()
