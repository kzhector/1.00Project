from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def render_the_map():
    return render_template('index.html')

#render all 23 maps
@app.route('/1992')
def render_1992():
    return render_template('map0.html')

@app.route('/1993')
def render_1993():
    return render_template('map1.html')

@app.route('/1994')
def render_1994():
    return render_template('map2.html')

@app.route('/1995')
def render_1995():
    return render_template('map3.html')

@app.route('/1996')
def render_1996():
    return render_template('map4.html')

@app.route('/1997')
def render_1997():
    return render_template('map5.html')

@app.route('/1998')
def render_1998():
    return render_template('map6.html')

@app.route('/1999')
def render_1999():
    return render_template('map7.html')

@app.route('/2000')
def render_2000():
    return render_template('map8.html')

@app.route('/2001')
def render_2001():
    return render_template('map9.html')

@app.route('/2002')
def render_2002():
    return render_template('map10.html')

@app.route('/2003')
def render_2003():
    return render_template('map11.html')

@app.route('/2004')
def render_2004():
    return render_template('map12.html')

@app.route('/2005')
def render_2005():
    return render_template('map13.html')

@app.route('/2006')
def render_2006():
    return render_template('map14.html')

@app.route('/2007')
def render_2007():
    return render_template('map15.html')

@app.route('/2008')
def render_2008():
    return render_template('map16.html')

@app.route('/2009')
def render_2009():
    return render_template('map17.html')

@app.route('/2010')
def render_2010():
    return render_template('map18.html')

@app.route('/2011')
def render_2011():
    return render_template('map19.html')

@app.route('/2012')
def render_2012():
    return render_template('map20.html')

@app.route('/2013')
def render_2013():
    return render_template('map21.html')

@app.route('/2014')
def render_2014():
    return render_template('map22.html')

@app.route('/2015')
def render_2015():
    return render_template('map23.html')

@app.route('/temporal')
def render_temporal():
    return render_template('temporal.html')

if __name__ == '__main__':
    app.run(debug=True,port = 3000)

