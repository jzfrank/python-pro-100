from flask import Flask
import random 

app = Flask(__name__)

# Assets
GREETING_IMG = 'https://media0.giphy.com/media/nWZoYczdgBVmyXkeB2/200w.webp?cid=ecf05e472k8iwo10qa0u108c3m6sxjar4xadu5qpm8bexpee&rid=200w.webp&ct=g'
FOUND_IMG = 'https://media3.giphy.com/media/C95viypu1o24M/giphy.webp?cid=ecf05e47zd1bfqmn9cn3ur2gst2ku999ymk44r6sukbnq2xc&rid=giphy.webp&ct=g'
LOW_IMG = 'https://media3.giphy.com/media/6uMqzcbWRhoT6/200.webp?cid=ecf05e47met67updmyn89u92qpj29cewaaiflc4wg5eanfwq&rid=200.webp&ct=g'
HIGH_IMG = 'https://media2.giphy.com/media/jedetunLBSvoESa3cS/giphy.webp?cid=ecf05e47zd1bfqmn9cn3ur2gst2ku999ymk44r6sukbnq2xc&rid=giphy.webp&ct=g'
# target number
LOWER_BOUND = 0
UPPER_BOUND = 100
NUMBER = random.choice(range(LOWER_BOUND, UPPER_BOUND + 1))
print("NUMBER:", NUMBER)


@app.route("/")
def home_greeting():
    return f'''
            <h1 style='text-align:center;color:blue'>Guess a number between {LOWER_BOUND} and {UPPER_BOUND}</h1>
            <img style='display:block;margin:auto'
                src={GREETING_IMG}
                width=400/>
    '''


@app.route("/<int:number>")
def check_guess(number):
    if number == NUMBER:
        return f'''
        <h1 style='text-align:center;color:green'>You found me!</h1>
        <img style='display:block;margin:auto'
        src={FOUND_IMG}
        width=400/>
        '''
    elif number < NUMBER:
        return f'''
        <h1 style='text-align:center;color:red'>Too low, try again!</h1>
        <img style='display:block;margin:auto'
        src={LOW_IMG}
        width=400/>
        '''
    else:
        return f'''
        <h1 style='text-align:center;color:red'>Too high, try again!</h1>
        <img style='display:block;margin:auto'
        src={HIGH_IMG}
        width=200/>
        '''


if __name__ == "__main__":
    app.run(debug=True)
