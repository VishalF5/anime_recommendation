
from flask import Flask,request,render_template
import pickle
#pickle files
similarity = pickle.load(open("similarity.pickle","rb"))
anime_names= pickle.load(open("name.pkl","rb"))
#mongodb function
def suggestion(i):
    from pymongo import MongoClient
    client = MongoClient(
        "mongodb+srv://Vishal:Vishal22610@anime.7z766.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.get_database('Anime')
    records = db.Anime

    myquery = ({'Name': i})
    mydoc = db.Anime.find(myquery)
    for x in mydoc:
        a = x
    name = a.get('Name')
    img = a.get('img_url')
    score = a.get('Score')
    syn = a.get('Synopsis')
    dur = a.get('Duration')
    stud = a.get('Studio')
    rat = a.get('Rating')
    return name, img, score, syn, dur, stud, rat

#home route
app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])

def hello_world():
    return render_template("index_django.html",suggestions=anime_names)

@app.route("/recommends", methods=["POST","GET"])
def recommends():
    try:
        text = request.form["movie"]
        names=similarity.get(text)
        name1=names[0]
        name2=names[1]
        name3 = names[2]
        name4 = names[3]
        name5 = names[4]

        name, img, score, syn, dur, stud, rat = suggestion(text)
        name1, img1, score1, syn1, dur1, stud1, rat1 = suggestion(name1)
        name2, img2, score2, syn2, dur2, stud2, rat2 = suggestion(name2)
        name3, img3, score3, syn3, dur3, stud3, rat3 = suggestion(name3)
        name4, img4, score4, syn4, dur4, stud4, rat4 = suggestion(name4)
        name5, img5, score5, syn5, dur5, stud5, rat5 = suggestion(name5)

        return render_template('inner.html',suggestions=anime_names,img=img, name=name, score=score, dur=dur, rat=rat,syn=syn,
                            stud=stud,name1=name1,score1=score1,stud1=stud1,rat1=rat1,dur1=dur1,img1=img1,
                            name2=name2,score2=score2,stud2=stud2,rat2=rat2,dur2=dur2,img2=img2,
                            name3=name3,score3=score3,stud3=stud3,rat3=rat3,dur3=dur3,img3=img3,
                            name4=name4,score4=score4,stud4=stud4,rat4=rat4,dur4=dur4,img4=img4,
                            name5=name5,score5=score5,stud5=stud5,rat5=rat5,dur5=dur5,img5=img5)
    except TypeError:
        return "Anime Not Found"


@app.route("/anime_info/<anime_name>", methods=["POST","GET"])
def anime_info(anime_name):
    name, img, score, syn, dur, stud, rat = suggestion(anime_name)
    names = similarity.get(anime_name)
    name1, img1, score1, syn1, dur1, stud1, rat1 = suggestion(names[0])
    name2, img2, score2, syn2, dur2, stud2, rat2 = suggestion(names[1])
    name3, img3, score3, syn3, dur3, stud3, rat3 = suggestion(names[2])
    name4, img4, score4, syn4, dur4, stud4, rat4 = suggestion(names[3])
    name5, img5, score5, syn5, dur5, stud5, rat5 = suggestion(names[4])
    return render_template('inner.html', suggestions=anime_names, img=img, name=name, score=score, dur=dur, rat=rat,syn=syn,
                           stud=stud,name1=name1,score1=score1,stud1=stud1,rat1=rat1,dur1=dur1,img1=img1,
                           name2=name2,score2=score2,stud2=stud2,rat2=rat2,dur2=dur2,img2=img2,
                           name3=name3,score3=score3,stud3=stud3,rat3=rat3,dur3=dur3,img3=img3,
                           name4=name4,score4=score4,stud4=stud4,rat4=rat4,dur4=dur4,img4=img4,
                           name5=name5,score5=score5,stud5=stud5,rat5=rat5,dur5=dur5,img5=img5)


if __name__=="__main__":
    app.run(host="0.0.0.0", port=7860 ,debug=True)