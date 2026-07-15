from flask import Flask,request,render_template,redirect,url_for,jsonify

app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "<h1>Welcome to the Flask Application!</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h1>This is the index page!</h1>"


#variable rules
@app.route('/sucess/<int:score>')
def sucess(score):
    return "the person has passed and the score is:"+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is:"+str(score)


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    math = float(data["math"])
    science = float(data["science"])
    history = float(data["history"])

    average = (math + science + history) / 3

    return jsonify({
        "average_marks": average
    })












#@app.route('/form',methods=["GET","POST"])
#def form():
#    if request.method=="GET":
#        return render_template("form.html")
#    else:
 #       math=float(request.form["math"])
 #       science=float(request.form["science"])
#        history=float(request.form["history"])
 #       average_marks=(math+science+history)/3
 #       res=""
 #       if average_marks>=50:
 #           res="sucess"
 #       else:
 #           res="fail"
 #       return redirect(url_for(res,score=average_marks))
  #      return render_template("form.html", score=average_marks)


if __name__=="__main__":
    app.run(debug=True)