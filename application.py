# from wsgiref import simple_server
from flask import Flask, request, app
from flask import Response
from flask_cors import CORS
from ran_for_deploy import predObj

# importing the necessary dependencies
from flask import Flask, render_template, request
# from flask_cors import cross_origin
# import pickle


application = Flask(__name__)
CORS(application)
application.config['DEBUG'] = True

@application.route('/',methods=['GET'])  # route to display the home page
# @cross_origin()
def homePage():
    return render_template("index.html")


# class ClientApi:~

#     def __init__(self):
#         self.predObj = predObj()

@application.route("/predict_api", methods=['POST'])
def predictRoute():
    try:
        if request.json['data'] is not None:
            data = request.json['data']
            print('data is:     ', data)
            pred=predObj()
            res = pred.predict_log(data)
            print('result is        ',res,type(res))
            return Response(f'{res}')
    except ValueError:
        return Response("Value not found")
    except Exception as e:
        print('exception is   ',e)
        return Response(e)

@application.route("/predict", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            CRIM=float(request.form['CRIM'])
            ZN = float(request.form['ZN'])
            INDUS = float(request.form['INDUS'])
            CHAS = float(request.form['CHAS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            AGE = float(request.form['AGE'])
            DIS = float(request.form['DIS'])
            RAD = float(request.form['RAD'])
            TAX = float(request.form['TAX'])
            PTRATIO = float(request.form['PTRATIO'])
            B = float(request.form['B'])
            LSTAT = float(request.form['LSTAT'])

            predict_dict ={"CRIM": CRIM,
                "ZN": ZN,
                "INDUS" : INDUS,
                "CHAS": CHAS,
                "NOX": NOX,
                "RM":RM,
                "AGE":AGE,
                "DIS":DIS,
                "RAD": RAD,
                "TAX": TAX,
                "PTRATIO":PTRATIO,
                "B":B,
                "LSTAT":LSTAT
    }
            pred2=predObj()
            res = pred2.predict_log(predict_dict)
            print('result is        ',res[0])
            # showing the diagnosed results in a UI
            return render_template('results.html',prediction=round(res[0],3))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    # clntApp = ClientApi()
    # host = '0.0.0.0'
    # port = 5000
    application.run(debug=True)
    #httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    #httpd.serve_forever()