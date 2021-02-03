from flask import Flask, render_template, request

app = Flask(__name__, template_folder="src/views") # (Mostra a origem , por padrão procura a pasta template)

@app.route("/", methods=["GET","POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html") 
    elif(request.method == "POST"):
        n1 = request.form["num1"] 
        n2 = request.form["num2"]
        opc = request.form["opc"]
        if(n1 != "" and n2 != "" and opc != ""):
            v = [opc, n1, n2]
            return { "Resultado" : verify(v) } # só renderiza em str/json
        else:
            return {"Alert":"Há campo vazio"}
    else:
        return "Você está acessando via outro Verbo"


def verify(v):
    switcher = {
                "soma": str(int(v[1])+int(v[2])), 
                "subt": str(int(v[1])-int(v[2])), 
                "mult": str(int(v[1])*int(v[2])), 
                "divi": str(int(v[1])//int(v[2])) 
                }
    return switcher.get(v[0], "default")


# @app.route("/<int:id>")
# def home_id(id):
#     return str(id+1) # No final precisa retornar como string


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

@app.errorhandler(405) # erro de verbo
def not_found2(error):
    return {"Mensagem":"O verbo não existe"}



app.run(port=5005, debug=True)  # (posso escolher a porta, debug atualiza automaticamente)
