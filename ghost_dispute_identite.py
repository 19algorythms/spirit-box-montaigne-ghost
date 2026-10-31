# v14-identite
import re, requests

M = ["montaigne-sceptique:latest", "montaigne-confiant:latest"]
N = ["Sceptique", "Confiant"]
O = {"temperature": 0.65, "top_p": 0.9, "repeat_penalty": 1.18,
     "num_ctx": 4096, "num_predict": 1400}
SUJET = "Qui etes-vous ?"

def tour(m, p):
    r = requests.post("http://localhost:11434/api/generate",
        json={"model": m, "prompt": p, "stream": False, "think": False,
              "options": O, "keep_alive": "30m"})
    d = r.json()
    xs = [v for v in d.values() if isinstance(v, str)]
    x = max(xs, key=len) if xs else ""
    rep = re.sub(r"<think>.*?</think>", "", x, flags=re.S).strip()
    if len(rep) < 20:
        raise SystemExit("ECHEC extraction")
    return rep

p = "Deux voix se presentent devant toi. Premiere voix, a toi : " + SUJET
f = open("transcript2.txt", "w", encoding="utf-8")
f.write("Sujet : " + SUJET + "\n")
for i in range(8):
    rep = tour(M[i % 2], p)
    print("[" + N[i % 2] + "] OK - " + str(len(rep.split())) + " mots")
    f.write("\n[" + N[i % 2] + "] " + rep + "\n")
    f.flush()
    p += "\n\nL'autre voix : " + rep + "\n\nA toi (reponds en 2 ou 3 phrases courtes) :"
f.close()
print("Termine -> transcript2.txt")