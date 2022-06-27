from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def instrucciones():
    return "Api rest para el calculo de la conversion entre las unidades del sistema inlges de longitud a cm"


@app.route('/imc/<string:peso>&<string:altura>')
def calculoImc(peso, altura):
    imc = float(peso) / float(altura) **2

    if imc < 18.5:
        return jsonify({"Su imc es" : imc, "Clasificacion" :"Bajo peso"})
    if imc > 18.5 and imc < 25 :
        return jsonify({"Su imc es" : imc, "Clasificacion" :"Peso normal"})
    if imc >= 25 and imc <= 29:
        return jsonify({"Su imc es" : imc, "Clasificacion" :"Sobrepeso"})
    if imc >= 30 and  imc <= 40:
        return jsonify({"Su imc es" : imc, "Clasificacion" :"Obesidad"})
    else :
        return jsonify({"Su imc es" : imc, "Clasificacion" : "Valor fuera de las clasificaciones actuales"})

@app.route('/hbh/<string:peso>&<string:estatura>&<string:edad>') 
def harrisBenedictHombre(peso, estatura, edad):
    geb = 66.5 + 13.75 * float(peso) + 5.0 * float(estatura) - 6.79 * float(edad)
    return jsonify({"Su gasto energetico basal es" : geb})

@app.route('/hbm/<string:peso>&<string:estatura>&<string:edad>') 
def harrisBenedictMujer(peso, estatura, edad):
    geb = 655 + 9.56 * float(peso) + 1.85 * float(estatura) - 4.68 * float(edad)
    return jsonify({"Su gasto energetico basal es" : geb})

if __name__ == '__main__':
    app.run(debug=True, port=4000)

