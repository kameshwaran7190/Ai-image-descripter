
import google.generativeai as genai
from flask import Flask,render_template,request
import PIL.Image

genai.configure(api_key="AIzaSyBAQ7w4d2fRt_Vy_nFmOa3RtvHeGEgdY34")
model = genai.GenerativeModel('gemini-pro-vision')
app=Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate',methods=["POST","GET"])
def gen():
        data=request.files['im']
        im=PIL.Image.open(data)

        descript = model.generate_content(["write a story or content for article or anything about it for 800 lines", im])

        respon = model.generate_content(["tittle in 1 line",im])
        tittle=respon.text
        des=descript.text

        return render_template('result.html',tittle=tittle,des=des)




if __name__=='__main__':
    app.run(debug=True)








