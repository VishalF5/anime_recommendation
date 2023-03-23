from flask import Flask, request, render_template
import pickle
from pymongo import MongoClient

# pickle files
similarity = pickle.load(open("similarity.pickle", "rb"))
anime_names = pickle.load(open("name.pkl", "rb"))


# connect to the database
try:
    client = MongoClient("mongodb+srv://Vishal:Vishal22610@anime.7z766.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.get_database('Anime')
    records = db.Anime
except Exception as e:
    print("Unable to connect to the database:", e)


# mongodb function
def suggestion(i):
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

def home(i):
    myquery = ({'Index': i})
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


# Flask App
app = Flask(__name__)


# Home Route
@app.route("/", methods=["POST", "GET"])
def hello_world():
    index=[2,1,0,3,4,5,6,7,8,9,66,388,2927,101,598,877,22,14,23,26,31,39,48,209,1076,67,787,448,284,371,926,614]
    result_dict={}
    result_dict = {}

    for id in index:
    # Call the home function and unpack the returned values into a list
        value_list = list(home(id))
        # Use the ID as the key and the value list as the corresponding value in the dictionary
        result_dict[f"name{id}"] = value_list

        print(result_dict)

  
    return render_template("index_django.html", suggestions=anime_names,dicts=result_dict)


@app.route("/recommends", methods=["POST", "GET"])
def recommends():
    try:
        text = request.form["anime_search"]
        names = similarity.get(text)
        name1 = names[0]
        name2 = names[1]
        name3 = names[2]
        name4 = names[3]
        name5 = names[4]

        name, img, score, syn, dur, stud, rat = suggestion(text)
        name1, img1, score1, syn1, dur1, stud1, rat1 = suggestion(name1)
        name2, img2, score2, syn2, dur2, stud2, rat2 = suggestion(name2)
        name3, img3, score3, syn3, dur3, stud3, rat3 = suggestion(name3)
        name4, img4, score4, syn4, dur4, stud4, rat4 = suggestion(name4)
        name5, img5, score5, syn5, dur5, stud5, rat5 = suggestion(name5)

        return render_template('inner.html', suggestions=anime_names, img=img, name=name, score=score, dur=dur, rat=rat, syn=syn,
                                stud=stud, name1=name1, score1=score1, stud1=stud1, rat1=rat1, dur1=dur1, img1=img1,
                                name2=name2, score2=score2, stud2=stud2, rat2=rat2, dur2=dur2, img2=img2,
                                name3=name3, score3=score3, stud3=stud3, rat3=rat3, dur3=dur3, img3=img3,
                                name4=name4, score4=score4, stud4=stud4, rat4=rat4, dur4=dur4, img4=img4,
                                name5=name5, score5=score5, stud5=stud5, rat5=rat5, dur5=dur5, img5=img5)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)
