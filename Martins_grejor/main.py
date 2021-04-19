import matplotlib.pyplot as plt
from websocket import create_connection
import json


plt.ion()
fig = plt.figure()
langs = ['C', 'C++', 'Java']
students = [23,17,35]

uri = "wss://ws-00bd5facfce0b76ac.wss.redditmedia.com/second-api?m=AQAAElNnYG4HsQsApOfGwaBwOOagCxS2gvVcxcNueKNTqMXIz0Bl"

ws = create_connection(uri)
while True:
    data = json.loads(ws.recv())
    cr = data["data"]["current_round"]
    fig.clear()


    if cr["status"] == "in_progress":
        for i, c in enumerate(cr["images"]):
            langs[i] = c["name"]
            students[i] = c["votes"]
        fig.suptitle(f"round: {cr['id']} to Reveal: {round(cr['secondsUntilVoteReveal'], 2)} Total votes: {cr['totalVotes']}")


    plt.bar(langs, students, color=(0.2, 0.4, 0.6, 0.6))
    fig.canvas.draw()
    fig.canvas.flush_events()

    print(langs, students)

