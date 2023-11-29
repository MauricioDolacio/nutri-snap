import json, requests, os
import reconhecimento as rec 
from flask import Flask, make_response, jsonify, request

path_inicial = os.path.dirname(__file__)
tipo_comida = 'Fruta'


def Consult(food):    
    try:                          
        request = requests.get(f"https://api.edamam.com/api/nutrition-data?app_id=345f851a&app_key=0dbb040ae0b77d131e69498dd31dde25&nutrition-type=cooking&ingr=100 g {food}")
        response_info = json.loads(request.content)
        nutrients=response_info['totalNutrients']
    except:
        return -1                   

    def ConsultJson(info): 
        try:
            return {
                'total':nutrients[info]['quantity'],
                'unit': nutrients[info]['unit']
            }
        except:
            return {
                'total':0,
                'unit': 'g'
            }
    dict={                          
        "Food":food,
        "Kcal": ConsultJson('ENERC_KCAL'),
        "Carb": ConsultJson('CHOCDF'),
        "Protein": ConsultJson('PROCNT'),
        "TotalFat": ConsultJson('FAT'),
        "FatSAT": ConsultJson('FASAT'),
        "Sodium": ConsultJson('NA'),
        "VitA": ConsultJson('VITA_RAE'),
        "VitB6": ConsultJson('VITB6A'),
        "VitC": ConsultJson('VITC')
        }           
    return dict

app = Flask(__name__)

UPLOAD_FOLDER = path_inicial
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST'])

def Main():
    file = request.files['picture']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'Fruta.jpg'))

    result_index = rec.model_prediction('Fruta.jpg')
    with open('labels.txt') as f:
        content = f.readlines()
        label = []
        for i in content:
            label.append(i[:-1])
            f.close()

    return make_response(
        jsonify(Consult(label[result_index]))
    )

app.run('localhost')
