"""Der Roboter aus Ebenen für die Webseite: dieselben Teile wie in der App
(sudoku-app/Design/Roboter-Ebenen), bewegt mit CSS.

`rig(mood, pre, alt)` liefert das HTML, `css()` die Regeln für roboter.css.
Lage der Ebenen in Einheiten der Leinwand 592,1 × 690,8 (wie Rig in RobotView.swift).
Gesichter wechseln über Zeitpläne, die hier in Keyframes übersetzt werden.
"""

W, H = 592.1, 690.8
CX = 296.0
NECK = (296.0, 399.2)
SHOULDER = (382.9, 436.0)
ANT_FOOT = (296.0, 114.9)
BALL = (296.0, 58.8)
HIP_Y, FEET_Y = 560.0, 681.0

L = {
    "beinR": (195.5, 525.5, 97, 156), "beinL": (297.8, 525.5, 96, 156),
    "rumpf": (194.1, 375.2, 203, 198), "stab": (271.7, 42.2, 50, 80),
    "kugel": (266.6, 29.3, 60, 60), "kopf": (105.2, 101.1, 383, 305),
    "arm-haengend": (351.6, 405.0, 89, 184), "arm-wink": (337.4, 271.5, 88, 198),
    "arm-jubel": (347.3, 324.2, 157, 146),
}
FACE = (135.2, 110.5, 322, 254)

# Je Stimmung: Arm (beide Seiten gleich, links gespiegelt), Dauer des Gesichter-Zyklus,
# Zeitfenster der Gesichter in Sekunden.
def _sprechen():
    folge = "1 2 1 f 2 1 2 2 1 f 1 2 1 2 f 1 2 1 2 1 f 2 1 f".split()
    out, t = {"sprechen1": [], "sprechen2": [], "freundlich": [], "blinzeln": []}, 0.0
    for s in folge:
        out[{"1": "sprechen1", "2": "sprechen2", "f": "freundlich"}[s]].append((t, t + 0.11))
        t += 0.11
    out["freundlich"] += [(t, 3.3), (3.43, 4.2)]
    out["blinzeln"].append((3.3, 3.43))
    return out

MOODS = {
    "happy": dict(arm="arm-haengend", dauer=12, faces={
        "freundlich": [(0, 1.6), (1.73, 3), (4.4, 6.2), (6.33, 6.5), (6.62, 8)],
        "blinzeln": [(1.6, 1.73), (6.2, 6.33), (6.5, 6.62)],
        "seite": [(3, 4.4)], "froehlich": [(8, 12)]}),
    "wave": dict(arm="arm-haengend", armr="arm-wink", dauer=5, faces={
        "freundlich": [(0, 1.9), (2.03, 3.6), (4.1, 5)], "blinzeln": [(1.9, 2.03)], "zwinkern": [(3.6, 4.1)]}),
    "cheer": dict(arm="arm-jubel", dauer=2.34, faces={"jubeln": [(0, 1.56)], "lachen": [(1.56, 2.34)]}),
    "talk": dict(arm="arm-haengend", dauer=4.2, faces=_sprechen()),
}


def _pct(v, total):
    return "%.3f%%" % (100 * v / total)


def _box(n, box):
    x, y, w, h = box
    return 'class="r %s" style="left:%s;top:%s;width:%s"' % (n, _pct(x, W), _pct(y, H), _pct(w, W))


def rig(mood, pre, alt=""):
    m = MOODS[mood]
    img = lambda n, box=None, cls=None: '<img %s src="%simg/roboter/rig/%s.webp" alt="" loading="lazy">' % (_box(cls or "t-" + n, box or L[n]), pre, n)
    faces = "".join(img("face-" + f, FACE, "f f-%s-%s" % (mood, f)) for f in m["faces"])
    armr, arml = m.get("armr", m["arm"]), m["arm"]
    aria = ' role="img" aria-label="%s"' % alt if alt else ' aria-hidden="true"'
    return (
        '<div class="rig rig-%s"%s><div class="r-koerper">' % (mood, aria)
        + img("beinR") + img("beinL")
        + '<div class="r-oben">' + img("rumpf")
        + '<div class="r-kopf"><div class="r-antenne">' + img("stab") + '<i class="r-glow"></i>' + img("kugel") + "</div>"
        + img("kopf") + faces + "</div>"
        + '<div class="r-arm r-arm-r">' + img(armr, cls="a t-" + armr) + "</div>"
        + '<div class="r-arm r-arm-l">' + img(arml, cls="a t-" + arml) + "</div>"
        + "</div></div></div>"
    )


def _origin(n):
    x, y, w, h = L[n]
    return "%s %s" % (_pct(SHOULDER[0] - x, w), _pct(SHOULDER[1] - y, h))


def _face_keyframes(mood, face, dauer, fenster):
    """Sichtbar in den Zeitfenstern, sonst unsichtbar; Wechsel in 1 ms, damit nichts überblendet."""
    an = lambda t: 1 if any(a <= t < b for a, b in fenster) else 0
    punkte = sorted(set([0.0, float(dauer)] + [float(x) for w in fenster for x in w]))
    body = []
    for t in punkte:
        if t > 0:
            body.append((100 * (t - 0.001) / dauer, an(t - 0.002)))
        if t < dauer:
            body.append((100 * t / dauer, an(t)))
    body.append((100.0, an(dauer - 0.002)))
    name = "f-%s-%s" % (mood, face)
    kf = "".join("%.3f%%{opacity:%d}" % (p, o) for p, o in body)
    return "@keyframes %s{%s}\n.rig .%s{animation:%s %ss linear infinite}\n" % (name, kf, name, name, dauer)


def css():
    o = lambda x, y: "%s %s" % (_pct(x, W), _pct(y, H))
    out = ["/* Erzeugt von tools/roboter.py. Roboter aus Ebenen, dieselben Teile wie in der App. */",
           ".rig{position:relative;aspect-ratio:%.1f/%.1f;width:100%%;max-width:170px;margin:0 auto}" % (W, H),
           ".rig .r-koerper,.rig .r-oben,.rig .r-kopf,.rig .r-antenne,.rig .r-arm{position:absolute;inset:0}",
           ".rig img.r{position:absolute;height:auto;max-width:none;margin:0;display:block}",
           ".rig .f{opacity:0}",
           ".rig .r-koerper{transform-origin:%s}" % o(CX, FEET_Y),
           ".rig .r-oben{transform-origin:%s;animation:r-atmen 3.4s ease-in-out infinite}" % o(CX, HIP_Y),
           ".rig .r-kopf{transform-origin:%s;animation:r-nicken 3.4s ease-in-out -.8s infinite}" % o(*NECK),
           ".rig .r-antenne{transform-origin:%s;animation:r-wippen 2.7s ease-in-out infinite alternate}" % o(*ANT_FOOT),
           ".rig .r-glow{position:absolute;left:%s;top:%s;width:%s;aspect-ratio:1;border-radius:50%%;"
           "background:radial-gradient(circle,rgba(107,237,189,.85) 0%%,rgba(107,237,189,0) 65%%);"
           "animation:r-gluehen 3.7s ease-in-out infinite alternate}" % (_pct(BALL[0] - 55, W), _pct(BALL[1] - 55, H), _pct(110, W)),
           ".rig .r-arm-l{transform:scaleX(-1);transform-origin:%s}" % o(CX, 0),
           ]
    for n in ("arm-haengend", "arm-wink", "arm-jubel"):
        out.append(".rig .a.t-%s{transform-origin:%s}" % (n, _origin(n)))
    out += [
        ".rig .a.t-arm-haengend{animation:r-pendeln 5s ease-in-out infinite alternate}",
        # Winken aus der Schulter, Körper wiegt sich mit
        ".rig-wave .r-arm-r .a{animation:r-winken .39s ease-in-out infinite alternate}",
        ".rig-wave .r-koerper{animation:r-wiegen .78s ease-in-out infinite alternate}",
        # Jubeln: Sprung, Landung mit Stauchen, Fäuste und Antenne im Takt
        ".rig-cheer .r-koerper{animation:r-sprung .78s infinite}",
        ".rig-cheer .a{animation:r-jubel .39s ease-in-out infinite alternate}",
        ".rig-cheer .r-antenne{animation:r-wippen-stark .78s ease-in-out infinite}",
        # Trösten: Kopf schief, spricht leise
        ".rig-talk .r-kopf{animation:r-schief 6s ease-in-out infinite}",
        "@keyframes r-atmen{0%,100%{transform:none}50%{transform:scaleY(1.012)}}",
        "@keyframes r-nicken{0%,100%{transform:translateY(-.36%)}50%{transform:translateY(.36%)}}",
        "@keyframes r-wippen{from{transform:rotate(-3.5deg)}to{transform:rotate(3.5deg)}}",
        "@keyframes r-wippen-stark{0%,100%{transform:rotate(-8deg)}50%{transform:rotate(9deg)}}",
        "@keyframes r-gluehen{from{opacity:.35}to{opacity:.85}}",
        "@keyframes r-pendeln{from{transform:rotate(-2deg)}to{transform:rotate(2deg)}}",
        "@keyframes r-winken{from{transform:rotate(9deg)}to{transform:rotate(41deg)}}",
        "@keyframes r-wiegen{from{transform:rotate(.4deg)}to{transform:rotate(2deg)}}",
        "@keyframes r-jubel{from{transform:rotate(-17deg)}to{transform:rotate(-3deg)}}",
        "@keyframes r-schief{0%,100%{transform:rotate(3deg)}50%{transform:rotate(6deg) translateY(-.3%)}}",
        "@keyframes r-sprung{"
        "0%{transform:none;animation-timing-function:cubic-bezier(.2,.7,.4,1)}"
        "31%{transform:translateY(-4.34%);animation-timing-function:cubic-bezier(.6,0,.8,.3)}"
        "62%{transform:none;animation-timing-function:ease-out}"
        "78%{transform:scale(1.033,.945)}"
        "100%{transform:none}}",
    ]
    for mood, m in MOODS.items():
        for face, fenster in m["faces"].items():
            out.append(_face_keyframes(mood, face, m["dauer"], fenster).rstrip())
    # Weniger Bewegung: alles steht, je Stimmung nur das Grundgesicht
    still = ["@media (prefers-reduced-motion:reduce){",
             ".rig *{animation:none!important}",
             ".rig .f{opacity:0!important}"]
    for mood, m in MOODS.items():
        base = next(iter(m["faces"]))
        still.append(".rig .f-%s-%s{opacity:1!important}" % (mood, base))
    still.append("}")
    out += still
    return "\n".join(out) + "\n"
