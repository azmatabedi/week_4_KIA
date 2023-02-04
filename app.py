from flask import Flask,jsonify,request
app=Flask(__name__)
@app.route(rule='/',methods=['GET'])
def main():
    return "Hello World"

@app.route(rule='/Get_Data',methods=['GET'])
def Get_Data():


    
    return jsonify(
        {"course":"KIA",
        "name":"azmat abedi"
        })


@app.route(rule='/pagenation/<int:number>',methods=['GET'])
def pagenation(number):
    try:

        return f"page number:{number}",200
    except:
        return "sever failure",404




@app.route(rule='/post_data/',methods=['GET','POST'])
def post_data():
    try:
        if request.method=='GET':
            return "invalied request /get data"
        if request.method=="POST":
            data=request.get_json()
            return  jsonify( {"user_data":data
                })
    except:
        return "sever failure",404


if __name__=='__main__':
    app.run(host='0.0.0.0',port="8080",debug=True)