from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def demo():
    ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save the visit
    with open("ip_logs.txt", "a") as file:
        file.write(f"IP: {ip} | Time: {timestamp}\n")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Get Caught!! :P</title>
        <style>
                @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700&display=swap');

            body {{
                font-family: "Orbitron", sans-serif;
                background: #FF0000;
                color: #BDF2FF;
                text-align: center;
                padding-top: 100px;
            }}

            .box {{
                max-width: 650px;
                margin: auto;
                background: #0000FF;
                padding: 40px;
                border-radius: 15px;
            }}

            .ip {{
                font-size: 32px;
                font-weight: bold;
                margin: 20px;
            }}

            .warning {{
                color: #FF0000;
            }}
        </style>
        
    </head>

    <body>

        <div class="box">

            <h1>IP Logger</h1>

            <p>
                Your browser connected to my server.
            </p>

            <p>
                The server was able to obtain your IP address >:P
            </p>

            <div class="ip">
                {ip}
            </div>

            <p class="warning">
                This is the end of you. MWAHAHAHA >:D
            </p>

            <hr>

            <p>
                An IP address does not automatically reveal your exact
                physical location or identity but it does allow for me to know who you are to an extent. PLUS! Most of the time, if I managed to find your IP it means I have a fair bit information on you.
            </p>

            <p>
                VPNs, proxies, mobile networks and shared networks
                can change or obscure the address a server observes, however, despite being a layer of security companies, servers and websites can still know your IP. 
            </p>
            <p>
            Only Tor and many more can fully anonymise you. Even then though, if the governments go to extremes you can be found!
            </p>
            <p>
            Trust no one ( ͡° ͜ʖ ͡°) and 
            Sleep with one eye open AHAHAHA XD
            </p>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)