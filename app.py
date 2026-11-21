from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def demo():
    ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # save the visit
    with open("ip_logs.txt", "a") as file:
        file.write(f"IP: {ip} | Time: {timestamp}\n")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Stay Safe!! </title>
        <style>
              
            body {{
                font-family: sans-serif;
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
                Your browser connected to this server
            </p>

            <p>
                The server was able to obtain your IP address
            </p>

            <div class="ip">
                {ip}
            </div>

            <p class="warning">
                Cautious use of the internet is mandatory.
                Never assume safety simply because your address is publicly available.
                Its not so easy to obtain but also not difficult with a couple steps. 
                Being mindful of your internet use can be one step more towards cyber-safety.
            </p>

            <hr>

            <p>
                An IP address does not automatically reveal your exact physical location or identity but it does allow for people to know who you are to an extent. 
                Additionally, most of the time, if someone managed to find your IP it means they have a fair bit information on you. This is the social engineering aspect of IP finding.
            </p>

            <p>
                VPNs, proxies, mobile networks and shared networks can change or obscure the address a server observes, however, despite there being a layer of security, companies, servers and websites can still know your IP address. 
            </p>
            <p>
            Only Tor and many more can fully anonymise you. Even then, however, if the those whom are searching for you go to extremes, you can be found!
            </p>
            <p>
            Be careful with what links you click on! And a repeat of above, always be careful --never assume saftey on the World Wide Web...
            </p>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
