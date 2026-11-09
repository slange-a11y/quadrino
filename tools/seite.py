#!/usr/bin/env python3
"""Erzeugt index.html (de) und en/index.html aus einer Vorlage. Aufruf: python3 tools/seite.py"""
KIDS = "katze hund fuchs panda frosch eule hase pinguin loewe dino roboter rakete einhorn baer koala schmetterling".split()
ADULT = "kompass fueller springer kristall mond blatt welle berg kranich sanduhr zahnrad feder stern raute anker tasse".split()
MED = "first4 first6 first9 nohint5 streak3 solved10 stars25 perfect".split()
ACT = ' class="active"'

T = {
 "de": dict(
  lang="de", pre="", nav=[("./","Start",True),("support.html","Support",False),("datenschutz.html","Datenschutz",False),("en/","English",False)],
  title="Quadrino Sudoku", sub="Sudoku für iPhone und iPad",
  desc="Quadrino ist ein Sudoku für iPhone und iPad, in dem Kinder und Erwachsene spielen: für Kinder mit Roboter und Stufen von 4×4 bis 9×9, für Erwachsene in Glas und Metall mit Hinweisen, die die Lösungstechnik nennen. Ohne Werbung, ohne Abo.",
  ogdesc="Ein Sudoku für Kinder und Erwachsene. Ohne Werbung, ohne Konto, ohne Abo.",
  banner_alt="Cremefarbene Spielkacheln und ein kleiner Roboter links, ein Raster aus Glaskacheln rechts",
  h1="Ein Sudoku für Kinder und Erwachsene.",
  intro="Kinder lernen mit einem kleinen Roboter, was Reihe, Spalte und Block bedeuten. Erwachsene spielen in derselben App bis 9×9 experte, und die Hinweise nennen die Technik, mit der man selbst draufkommt. Ohne Werbung, ohne Abo, ohne Datensammeln.",
  robot_alt="Der Roboter winkt",
  welten_h="Zwei Welten in einer App",
  welten_p="Beim Anlegen eines Profils wählst du Kind oder Erwachsen. Davon hängen Aussehen, Hilfen und Stufen ab, für jedes Profil einzeln.",
  kind_h="Für Kinder", kind_p="Ein Roboter erklärt, liest vor und freut sich mit. Es geht los mit 4×4, nach fünf gelösten Rätseln wird die nächste Stufe frei.",
  kind_li=["Einführung beim ersten Rätsel jeder Größe","Große Zahlentasten, gut zu treffen","Tiere statt Zahlen bei 4×4 und 6×6, wenn gewünscht","Eltern-Ecke hinter einer kleinen Rechenaufgabe"],
  erw_h="Für Erwachsene", erw_p="Ruhig, in Glas und Metall. Alle Größen und vier Stufen von leicht bis experte, Merkzahlen, Zeit und Bestzeiten.",
  erw_li=["Merkzahlen, die sich beim Setzen selbst aufräumen","Bestzeit je Stufe und eine Statistik der letzten 14 Tage","Rätsel des Tages, für alle Profile gleich"],
  shots=[("kind-begruessung","Begrüßung im Kindermodus mit Roboter"),("kind-spiel","4×4-Rätsel mit Einführung durch den Roboter"),("erw-begruessung","Begrüßung im Erwachsenenmodus mit Glaskacheln"),("erw-start","Startseite für Erwachsene mit Rätsel des Tages")],
  rob_h="Ein Roboter, der mitdenkt",
  rob_p="Im Kindermodus begleitet er jedes Rätsel. Er zeigt, wo man hinschauen soll, liest vor, wenn man möchte, und bleibt freundlich, auch wenn eine Zahl nicht passt.",
  rob=[("happy","begrüßt"),("wave","winkt"),("think","denkt mit"),("cheer","jubelt"),("oops","tröstet"),("proud","ist stolz")],
  hin_h="Hinweise, die erklären",
  hin_p1="Die Glühbirne verrät nicht einfach eine Zahl. Erst nennt sie die Technik und zeigt, wo du hinschauen sollst. Wer dann noch nicht weiterkommt, bekommt das Feld mit Begründung, erst zuletzt die Zahl. Gezählt wird das als ein Hinweis.",
  hin_p2="Schwere und Experten-Rätsel lassen sich immer mit diesen Techniken lösen. Raten ist nie nötig.",
  tech=["Einzige Möglichkeit","Versteckter Einer","Eingesperrte Kandidaten","Nacktes Paar","Verstecktes Paar","X-Wing"],
  hin_alt="9×9-Rätsel, der Hinweis nennt die Technik Versteckter Einer und hebt Reihe 7 hervor",
  gew_h="Gelöst!",
  gew_p="Wenn die letzte Zahl sitzt, läuft eine Lichtwelle über das Brett. Kinder bekommen Konfetti, Sterne und Sticker. Erwachsene sehen ihre Zeit hochzählen und wissen sofort, ob es eine neue Bestzeit war.",
  gew_med="Sticker für Kinder, Medaillen für Erwachsene:",
  gew_alt=("Gewinnmoment für Kinder mit Konfetti und drei Sternen","Gewinnmoment für Erwachsene mit Zeit und neuer Bestzeit"),
  prof_h="Jeder spielt mit eigenem Profil",
  prof_p="Jedes Familienmitglied hat eigene Sterne, eigene Stufen und ein eigenes Bild: 16 Tiere und Figuren für Kinder, 16 Objekte aus Glas und Metall für Erwachsene. Der Fortschritt liegt in deiner privaten iCloud und ist auf iPhone und iPad gleich.",
  mot_h="Jeden Tag ein anderes Startbild",
  mot_p="Beim Öffnen begrüßt dich Quadrino mit deinem Stand und dem Rätsel des Tages. Das Bild dahinter wechselt täglich.",
  mot=[("glas","Glas, für Erwachsene"),("metall","Metall, für Erwachsene"),("kacheln","Kacheln, für Kinder"),("werkstatt","Werkstatt, für Kinder")],
  preis_h="Was es kostet",
  preis_p="Laden ist kostenlos. 4×4 und das Rätsel des Tages bleiben immer frei, dazu zwei Rätsel jeder höheren Stufe zum Ausprobieren. Ein einziger Kauf schaltet alles frei, über die Familienfreigabe für die ganze Familie.",
  preis_note="Kein Abo, keine Werbung, kein Konto. Die App sammelt keine Daten. Bei Kinderprofilen fragt die App vor dem Kauf nach Mama oder Papa.",
  betrag="4,99 €", kauf_alt="Kaufseite „Quadrino komplett“ mit Preis",
  stand_h="Stand",
  stand_p='Quadrino wird gerade über TestFlight getestet. Sobald die App im App Store erscheint, steht der Link hier. Fragen und Wünsche gern über <a href="support.html">Support</a>.',
  foot=[("support.html","Support"),("datenschutz.html","Datenschutz")], lang_link=("en/","English"),
 ),
 "en": dict(
  lang="en", pre="../", nav=[("./","Home",True),("support.html","Support",False),("privacy.html","Privacy",False),("../","Deutsch",False)],
  title="Quadrino Sudoku", sub="Sudoku for iPhone and iPad",
  desc="Quadrino is a Sudoku for iPhone and iPad that children and adults share: for kids with a robot and levels from 4×4 to 9×9, for adults in glass and metal with hints that name the solving technique. No ads, no subscription.",
  ogdesc="One Sudoku for children and adults. No ads, no account, no subscription.",
  banner_alt="Cream play tiles and a small robot on the left, a grid of glass tiles on the right",
  h1="One Sudoku for children and adults.",
  intro="Children learn from a small robot what row, column and block mean. Adults play up to 9×9 expert in the same app, and the hints name the technique that gets you there yourself. No ads, no subscription, no data collection.",
  robot_alt="The robot waves",
  welten_h="Two worlds in one app",
  welten_p="When you create a profile, you choose child or adult. That decides the look, the help and the levels, separately for every profile.",
  kind_h="For children", kind_p="A robot explains, reads aloud and cheers along. It starts with 4×4; after five solved puzzles the next level opens.",
  kind_li=["Introduction at the first puzzle of every size","Big number keys that are easy to hit","Animals instead of numbers for 4×4 and 6×6, if wanted","Parents' corner behind a small sum"],
  erw_h="For adults", erw_p="Calm, in glass and metal. All sizes and four levels from easy to expert, notes, time and best times.",
  erw_li=["Notes that tidy themselves up as you place numbers","Best time per level and statistics for the last 14 days","Puzzle of the day, the same for every profile"],
  shots=[("kind-begruessung","Welcome screen in kids mode with the robot"),("kind-spiel","4×4 puzzle with the robot's introduction"),("erw-begruessung","Welcome screen in adult mode with glass tiles"),("erw-start","Adult home screen with today's puzzle")],
  rob_h="A robot that thinks along",
  rob_p="In kids mode it goes along with every puzzle. It shows where to look, reads aloud if you like, and stays friendly even when a number doesn't fit.",
  rob=[("happy","says hello"),("wave","waves"),("think","thinks along"),("cheer","cheers"),("oops","comforts"),("proud","is proud")],
  hin_h="Hints that explain",
  hin_p1="The bulb doesn't just give away a number. First it names the technique and shows you where to look. If you're still stuck, you get the cell with the reasoning, and only then the number. It all counts as one hint.",
  hin_p2="Hard and expert puzzles can always be solved with these techniques. You never have to guess.",
  tech=["Naked single","Hidden single","Locked candidates","Naked pair","Hidden pair","X-Wing"],
  hin_alt="9×9 puzzle, the hint names the technique and highlights row 7",
  gew_h="Solved!",
  gew_p="When the last number is in, a wave of light runs across the board. Children get confetti, stars and stickers. Adults watch their time count up and see right away whether it was a new best.",
  gew_med="Stickers for children, medals for adults:",
  gew_alt=("Winning moment for children with confetti and three stars","Winning moment for adults with time and a new best"),
  prof_h="Everyone plays with their own profile",
  prof_p="Each family member has their own stars, their own levels and their own picture: 16 animals and characters for children, 16 objects in glass and metal for adults. Progress lives in your private iCloud and is the same on iPhone and iPad.",
  mot_h="A different start picture every day",
  mot_p="When you open it, Quadrino greets you with your progress and the puzzle of the day. The picture behind changes daily.",
  mot=[("glas","Glass, for adults"),("metall","Metal, for adults"),("kacheln","Tiles, for children"),("werkstatt","Workshop, for children")],
  preis_h="What it costs",
  preis_p="The download is free. 4×4 and the puzzle of the day stay free for good, plus two puzzles of every higher level to try. A single purchase unlocks everything, shared with the whole family through Family Sharing.",
  preis_note="No subscription, no ads, no account. The app collects no data. On child profiles the app asks for a parent before buying.",
  betrag="€4.99", kauf_alt="Purchase screen “Quadrino Complete” with price",
  stand_h="Status",
  stand_p='Quadrino is currently being tested through TestFlight. As soon as it is in the App Store, the link will be here. Questions and wishes are welcome through <a href="support.html">Support</a>.',
  foot=[("support.html","Support"),("privacy.html","Privacy")], lang_link=("../","Deutsch"),
 ),
}

def page(t):
    p = t["pre"]
    nav = "\n".join('      <a%s href="%s">%s</a>' % (ACT if a else "", h, l) for h, l, a in t["nav"])
    li = lambda xs: "\n".join("          <li>%s</li>" % x for x in xs)
    sh = t["shots"]
    rob = "\n".join('        <figure><img src="%simg/roboter/%s.png" alt="" loading="lazy"><figcaption>%s</figcaption></figure>' % (p, m, c) for m, c in t["rob"])
    tech = "\n".join("          <li>%s</li>" % x for x in t["tech"])
    medk = "\n".join('          <img src="%simg/medaille/K-%s.png" alt="" loading="lazy">' % (p, m) for m in MED)
    mede = "\n".join('          <img src="%simg/medaille/E-%s.png" alt="" loading="lazy">' % (p, m) for m in MED)
    av = "\n".join(['        <img class="kind" src="%simg/avatar/%s.jpg" alt="" loading="lazy">' % (p, n) for n in KIDS] + ['        <img class="erw" src="%simg/avatar/%s.jpg" alt="" loading="lazy">' % (p, n) for n in ADULT])
    mot = "\n".join('      <figure><img src="%simg/motiv/%s.jpg" alt="" loading="lazy"><figcaption>%s</figcaption></figure>' % (p, m, c) for m, c in t["mot"])
    foot = "\n".join('    <a href="%s">%s</a>' % (h, l) for h, l in t["foot"])
    v = dict(t, p=p, nav_html=nav, kind_li_html=li(t["kind_li"]), erw_li_html=li(t["erw_li"]), rob_html=rob, tech_html=tech,
             medk=medk, mede=mede, av=av, mot_html=mot, foot_html=foot,
             s0=sh[0][0], a0=sh[0][1], s1=sh[1][0], a1=sh[1][1], s2=sh[2][0], a2=sh[2][1], s3=sh[3][0], a3=sh[3][1],
             ga0=t["gew_alt"][0], ga1=t["gew_alt"][1], ll0=t["lang_link"][0], ll1=t["lang_link"][1])
    return VORLAGE.format(**v)

VORLAGE = '''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{ogdesc}">
<meta property="og:image" content="https://slange-a11y.github.io/quadrino/img/teaser.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="{p}icon.png">
<link rel="stylesheet" href="{p}style.css">
</head>
<body>
<div class="wrap">
  <header class="top">
    <img src="{p}icon.png" alt="">
    <div>
      <div class="name">Quadrino</div>
      <div class="sub">{sub}</div>
    </div>
    <nav class="menu">
{nav_html}
    </nav>
  </header>
</div>

<div class="hero">
  <img src="{p}img/banner.jpg" srcset="{p}img/banner-768.jpg 768w, {p}img/banner.jpg 1536w" sizes="(max-width: 800px) 100vw, 1240px" alt="{banner_alt}">
</div>

<div class="wrap">
  <div class="intro intro-zeile">
    <div>
      <h1>{h1}</h1>
      <p>{intro}</p>
    </div>
    <img src="{p}img/roboter/wave.png" alt="{robot_alt}">
  </div>

  <section>
    <h2>{welten_h}</h2>
    <p>{welten_p}</p>
    <div class="welten">
      <div class="welt kind">
        <div class="phones">
          <img class="phone" src="{p}img/{s0}.jpg" alt="{a0}" loading="lazy">
          <img class="phone" src="{p}img/{s1}.jpg" alt="{a1}" loading="lazy">
        </div>
        <h3>{kind_h}</h3>
        <p>{kind_p}</p>
        <ul>
{kind_li_html}
        </ul>
      </div>
      <div class="welt erw">
        <div class="phones">
          <img class="phone" src="{p}img/{s2}.jpg" alt="{a2}" loading="lazy">
          <img class="phone" src="{p}img/{s3}.jpg" alt="{a3}" loading="lazy">
        </div>
        <h3>{erw_h}</h3>
        <p>{erw_p}</p>
        <ul>
{erw_li_html}
        </ul>
      </div>
    </div>
  </section>
</div>

<div class="band creme">
  <div class="wrap">
    <section>
      <h2>{rob_h}</h2>
      <p>{rob_p}</p>
      <div class="roboter">
{rob_html}
      </div>
    </section>
  </div>
</div>

<div class="wrap">
  <section>
    <div class="split">
      <div>
        <h2>{hin_h}</h2>
        <p>{hin_p1}</p>
        <p>{hin_p2}</p>
        <ul class="techniken">
{tech_html}
        </ul>
      </div>
      <div><img class="phone" src="{p}img/erw-hinweis.jpg" alt="{hin_alt}" loading="lazy"></div>
    </div>
  </section>

  <section>
    <div class="gewinn">
      <img class="phone" src="{p}img/kind-gewonnen.jpg" alt="{ga0}" loading="lazy">
      <img class="phone" src="{p}img/erw-gewonnen.jpg" alt="{ga1}" loading="lazy">
      <div>
        <h2>{gew_h}</h2>
        <p>{gew_p}</p>
        <p class="note">{gew_med}</p>
        <div class="medaillen">
{medk}
        </div>
        <div class="medaillen erw">
{mede}
        </div>
      </div>
    </div>
  </section>
</div>

<div class="band graphit">
  <div class="wrap">
    <section>
      <h2>{prof_h}</h2>
      <p>{prof_p}</p>
      <div class="avatare">
{av}
      </div>
    </section>
  </div>
</div>

<div class="wrap">
  <section>
    <h2>{mot_h}</h2>
    <p>{mot_p}</p>
    <div class="motive">
{mot_html}
    </div>
  </section>

  <section>
    <div class="preis-zeile">
      <div>
        <h2>{preis_h}</h2>
        <div class="preis">
          <div class="betrag">{betrag}</div>
          <div>
            <p>{preis_p}</p>
            <p class="note">{preis_note}</p>
          </div>
        </div>
      </div>
      <img class="phone" src="{p}img/kaufseite.jpg" alt="{kauf_alt}" loading="lazy">
    </div>
  </section>

  <section class="narrow">
    <h2>{stand_h}</h2>
    <p>{stand_p}</p>
  </section>

  <footer>
    <span>© 2026 Silvio Lange</span>
{foot_html}
    <a class="lang" href="{ll0}">{ll1}</a>
  </footer>
</div>
</body>
</html>
'''

if __name__ == "__main__":
    import os
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    open("index.html", "w").write(page(T["de"]))
    open("en/index.html", "w").write(page(T["en"]))
    print("index.html und en/index.html geschrieben")
