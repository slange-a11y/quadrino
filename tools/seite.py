#!/usr/bin/env python3
"""Erzeugt die Verkaufsseite index.html (de) und en/index.html. Aufruf: python3 tools/seite.py

Aufbau nach dem Muster erfolgreicher App-Seiten: Gefühl statt Funktionsliste,
ein Ziel (kostenlos testen), Knopf oben und am Ende, Vergleich mit anderen
Sudoku-Apps, Einwände in Fragen und Antworten. Keine erfundenen Bewertungen.
"""
import re
KIDS = "katze hund fuchs panda frosch eule hase pinguin loewe dino roboter rakete einhorn baer koala schmetterling".split()
ADULT = "kompass fueller springer kristall mond blatt welle berg kranich sanduhr zahnrad feder stern raute anker tasse".split()
MED = "first4 first6 first9 nohint5 streak3 solved10 stars25 perfect".split()
TESTEN = "https://testflight.apple.com/join/FUYYN7MQ"
TESTEN_EN = "https://testflight.apple.com/join/FUYYN7MQ"
CSSV = "202611091659"

T = {
 "de": dict(
  lang="de", pre="", title="Quadrino Sudoku", sub="Sudoku für iPhone und iPad",
  desc="Quadrino ist das Sudoku für die ganze Familie: Kinder lernen spielend mit ihrem Roboter, Erwachsene finden ihre ruhigen Minuten. Ohne Werbung, ohne Abo, ohne Datensammeln.",
  ogdesc="Das Sudoku für die ganze Familie. Ohne Werbung, ohne Abo, ohne Datensammeln.",
  testen=TESTEN, cta="Kostenlos testen", cta_nav="Testen", wie="So funktioniert’s",
  cta_hinweis="Quadrino ist gerade in der Testphase. Der Knopf öffnet Apples TestFlight, dort installierst du die Testversion. Dein Feedback fließt direkt in die App. Die Plätze sind begrenzt, bald gibt es Quadrino im App Store.",
  banner_alt="Cremefarbene Spielkacheln und ein kleiner Roboter links, ein Raster aus Glaskacheln rechts",
  h1="Das Sudoku, das die ganze Familie liebt.",
  intro="Kinder lernen spielend mit ihrem kleinen Roboter. Erwachsene finden ihre ruhigen zehn Minuten am Tag. Und keiner muss sich durch Werbung klicken.",
  vertrauen=["Ohne Werbung", "Ohne Abo", "Ohne Datensammeln", "Für iPhone und iPad", "Deutsch und Englisch"],
  robot_alt="Der Roboter winkt",
  ver_h="Sudoku-Apps gibt es viele. Familientaugliche kaum.",
  ver_p="Die bekannten Sudoku-Apps leben von Werbung. Mitten im Rätsel läuft ein Clip, und wer Ruhe will, zahlt dort 12,99 € bis 17,99 €, nur damit die Werbung verschwindet. Für Kinder ist das nichts.",
  ver_th=("", "Viele Sudoku-Apps", "Quadrino"),
  ver=[("Werbung", "mitten im Spiel", "keine, nie"),
       ("Preis", "gratis mit Werbung, 12,99 € bis 17,99 € ohne", "4,99 € einmal, für die ganze Familie"),
       ("Abo", "oft", "keins"),
       ("Daten", "Werbe-Tracking über Apps hinweg", "bleiben bei dir, in deiner iCloud"),
       ("Kinder", "selten mitgedacht", "eigene Welt mit Roboter und Eltern-Ecke"),
       ("Schwere Rätsel", "manchmal nur durch Raten lösbar", "immer mit Logik lösbar")],
  kind_h="Für Kinder: ein Freund, der mitdenkt",
  kind_p1="Der kleine Roboter erklärt, was Reihe, Spalte und Block bedeuten. Er liest vor, freut sich mit und bleibt freundlich, wenn eine Zahl nicht passt. So wird aus Rätseln ein Erfolgserlebnis.",
  kind_p2="Es geht los mit 4×4. Nach fünf gelösten Rätseln wartet die nächste Stufe, bis hin zum großen 9×9. Für jeden Erfolg gibt es einen Sticker.",
  rob=[("happy", "begrüßt"), ("cheer", "jubelt"), ("oops", "tröstet")],
  kind_shots=[("kind-begruessung", "Begrüßung im Kindermodus mit Roboter"), ("kind-spiel", "4×4-Rätsel mit Einführung durch den Roboter")],
  zitat="Spielen, lernen, stolz sein. Ganz ohne Werbung dazwischen.",
  erw_h="Für Erwachsene: zehn ruhige Minuten",
  erw_p1="Glas und Metall, keine Ablenkung. Alle Größen und vier Stufen bis experte, Merkzahlen, Zeit und Bestzeiten. Jeden Tag wartet ein neues Rätsel des Tages.",
  erw_p2="Und wenn du hängst: Die Glühbirne verrät nicht einfach die Zahl. Sie nennt die Technik, mit der du selbst draufkommst. So wirst du mit jedem Rätsel besser.",
  tech=["Einzige Möglichkeit", "Versteckter Einer", "Eingesperrte Kandidaten", "Nacktes Paar", "Verstecktes Paar", "X-Wing"],
  erw_shots=[("erw-begruessung", "Begrüßung im Erwachsenenmodus mit Glaskacheln"), ("erw-hinweis", "Der Hinweis nennt die Technik Versteckter Einer")],
  gew_h="Das Gefühl, wenn die letzte Zahl sitzt",
  gew_p="Eine Lichtwelle läuft über das Brett. Für Kinder regnet es Konfetti, der Roboter jubelt, ein neuer Sticker kommt dazu. Erwachsene sehen ihre Zeit hochzählen und wissen sofort, ob es eine neue Bestzeit war.",
  gew_alt=("Gewinnmoment für Kinder mit Konfetti und drei Sternen", "Gewinnmoment für Erwachsene mit Zeit und neuer Bestzeit"),
  fam_h="Eine App. Die ganze Familie.",
  fam_p="Jeder bekommt sein eigenes Profil mit eigenem Bild, eigenen Sternen und eigenem Tempo. Der Fortschritt liegt in deiner privaten iCloud und ist auf iPhone und iPad gleich. Ein einziger Kauf gilt über die Familienfreigabe für alle.",
  preis_h="Einmal 4,99 €. Für immer. Für alle.",
  preis_p="Zum Ausprobieren bleiben 4×4 und das Rätsel des Tages immer frei, dazu zwei Rätsel jeder anderen Stufe. Wenn es euch gefällt, schaltet ein einziger Kauf alles frei. Kein Abo, das sich verlängert. Keine Werbung, die man wegkaufen muss.",
  preis_note="Bei Kinderprofilen fragt die App vor dem Kauf nach Mama oder Papa.",
  betrag="4,99 €", kauf_alt="Kaufseite „Quadrino komplett“ mit Preis",
  faq_h="Häufige Fragen",
  faq=[("Ist Quadrino wirklich ohne Werbung?", "Ja. Es gibt keine Werbung, keine Werbe-Netzwerke und keine Analyse-Werkzeuge in der App. Das bleibt auch so."),
       ("Brauche ich ein Konto?", "Nein. Profile legst du in der App an. Wenn du bei iCloud angemeldet bist, gleicht Quadrino über deine private iCloud zwischen deinen Geräten ab."),
       ("Ab welchem Alter geht das?", "Wer Zahlen von 1 bis 4 kennt, kann mit 4×4 anfangen. Auf Wunsch zeigt Quadrino bei 4×4 und 6×6 Tiere statt Zahlen. Der Roboter führt beim ersten Rätsel jeder Größe Schritt für Schritt durch."),
       ("Gibt es ein Abo?", "Nein. Einmal 4,99 €, dann ist alles frei, über die Familienfreigabe für die ganze Familie."),
       ("Was passiert mit unseren Daten?", "Nichts. Die App sammelt keine Daten. Profile und Fortschritt liegen auf deinem Gerät und in deiner eigenen iCloud, wir als Anbieter sehen davon nichts."),
       ("Läuft es auf dem iPad?", "Ja. Auf dem iPad im Querformat liegt das Brett links und die Zahlen rechts, so spielt es sich besonders angenehm.")],
  schluss="Probier Quadrino aus. Mit deinem Kind oder ganz für dich.",
  nav_foot=[("support.html", "Support"), ("datenschutz.html", "Datenschutz")], lang_link=("en/", "English"),
 ),
 "en": dict(
  lang="en", pre="../", title="Quadrino Sudoku", sub="Sudoku for iPhone and iPad",
  desc="Quadrino is the Sudoku for the whole family: children learn with their little robot, adults find their quiet minutes. No ads, no subscription, no data collection.",
  ogdesc="The Sudoku for the whole family. No ads, no subscription, no data collection.",
  testen=TESTEN_EN, cta="Try it free", cta_nav="Try it", wie="How it works",
  cta_hinweis="Quadrino is in testing right now. The button opens Apple's TestFlight, where you install the beta. Your feedback goes straight into the app. Spots are limited; Quadrino is coming soon to the App Store.",
  banner_alt="Cream play tiles and a small robot on the left, a grid of glass tiles on the right",
  h1="The Sudoku the whole family loves.",
  intro="Children learn with their little robot. Adults find their quiet ten minutes a day. And nobody has to click through ads.",
  vertrauen=["No ads", "No subscription", "No data collection", "For iPhone and iPad", "German and English"],
  robot_alt="The robot waves",
  ver_h="There are plenty of Sudoku apps. Few are fit for families.",
  ver_p="The well-known Sudoku apps live on advertising. A clip plays in the middle of a puzzle, and if you want peace you pay €12.99 to €17.99 there just to make the ads go away. That's no place for children.",
  ver_th=("", "Many Sudoku apps", "Quadrino"),
  ver=[("Ads", "in the middle of a game", "none, ever"),
       ("Price", "free with ads, €12.99 to €17.99 without", "€4.99 once, for the whole family"),
       ("Subscription", "often", "none"),
       ("Data", "ad tracking across apps", "stays with you, in your iCloud"),
       ("Children", "rarely considered", "their own world with robot and parents' corner"),
       ("Hard puzzles", "sometimes only by guessing", "always solvable by logic")],
  kind_h="For children: a friend who thinks along",
  kind_p1="The little robot explains what row, column and block mean. It reads aloud, cheers along and stays friendly when a number doesn't fit. Puzzles turn into moments of success.",
  kind_p2="It starts with 4×4. After five solved puzzles the next level waits, all the way up to the big 9×9. Every achievement earns a sticker.",
  rob=[("happy", "says hello"), ("cheer", "cheers"), ("oops", "comforts")],
  kind_shots=[("kind-begruessung", "Welcome screen in kids mode with the robot"), ("kind-spiel", "4×4 puzzle with the robot's introduction")],
  zitat="Play, learn, be proud. With no ads in between.",
  erw_h="For adults: ten quiet minutes",
  erw_p1="Glass and metal, no distractions. All sizes and four levels up to expert, notes, time and best times. A new puzzle of the day waits every day.",
  erw_p2="And when you're stuck, the bulb doesn't just give away the number. It names the technique that gets you there yourself. You get better with every puzzle.",
  tech=["Naked single", "Hidden single", "Locked candidates", "Naked pair", "Hidden pair", "X-Wing"],
  erw_shots=[("erw-begruessung", "Welcome screen in adult mode with glass tiles"), ("erw-hinweis", "The hint names the technique Hidden single")],
  gew_h="The feeling when the last number is in",
  gew_p="A wave of light runs across the board. Children get confetti, a cheering robot and a new sticker. Adults watch their time count up and see right away whether it was a new best.",
  gew_alt=("Winning moment for children with confetti and three stars", "Winning moment for adults with time and a new best"),
  fam_h="One app. The whole family.",
  fam_p="Everyone gets their own profile with their own picture, their own stars and their own pace. Progress lives in your private iCloud and is the same on iPhone and iPad. A single purchase covers everyone through Family Sharing.",
  preis_h="€4.99 once. For good. For everyone.",
  preis_p="To try it, 4×4 and the puzzle of the day stay free for good, plus two puzzles of every other level. If you like it, a single purchase unlocks everything. No subscription that renews. No ads you have to pay to remove.",
  preis_note="On child profiles the app asks for a parent before buying.",
  betrag="€4.99", kauf_alt="Purchase screen “Quadrino Complete” with price",
  faq_h="Questions",
  faq=[("Is Quadrino really free of ads?", "Yes. There are no ads, no ad networks and no analytics tools in the app. That won't change."),
       ("Do I need an account?", "No. You create profiles in the app. If you're signed in to iCloud, Quadrino syncs through your private iCloud between your devices."),
       ("What age is it for?", "Anyone who knows the numbers 1 to 4 can start with 4×4. If you like, Quadrino shows animals instead of numbers for 4×4 and 6×6. The robot guides step by step through the first puzzle of every size."),
       ("Is there a subscription?", "No. €4.99 once, then everything is open, for the whole family through Family Sharing."),
       ("What happens to our data?", "Nothing. The app collects no data. Profiles and progress live on your device and in your own iCloud; we as the developer see none of it."),
       ("Does it run on iPad?", "Yes. On iPad in landscape the board sits on the left and the numbers on the right, which makes it especially pleasant to play.")],
  schluss="Give Quadrino a try. With your child or just for you.",
  nav_foot=[("support.html", "Support"), ("privacy.html", "Privacy")], lang_link=("../", "Deutsch"),
 ),
}

BUEHNE = '''<div class="buehne" aria-hidden="true">
  <i style="width:96px;height:96px;left:2%;top:14%;--d:46s;--x:30px;--y:80px;--r0:-8deg;--r1:10deg"></i>
  <i style="width:64px;height:64px;left:91%;top:10%;--d:38s;--x:-30px;--y:90px;--r0:12deg;--r1:-6deg"></i>
  <i style="width:130px;height:130px;left:89%;top:48%;--d:58s;--x:-30px;--y:-60px;--r0:6deg;--r1:-14deg"></i>
  <i style="width:80px;height:80px;left:1%;top:60%;--d:52s;--x:40px;--y:-90px;--r0:-14deg;--r1:4deg"></i>
  <i style="width:48px;height:48px;left:95%;top:30%;--d:34s;--x:-20px;--y:60px;--r0:20deg;--r1:-10deg"></i>
  <i style="width:100px;height:100px;left:3%;top:86%;--d:64s;--x:30px;--y:-70px;--r0:-4deg;--r1:16deg"></i>
  <i style="width:58px;height:58px;left:93%;top:78%;--d:44s;--x:-30px;--y:-50px;--r0:8deg;--r1:-12deg"></i>
</div>'''

SKRIPT = '''<script>
// Abschnitte gleiten beim Scrollen herein. Was beim Laden schon zu sehen ist, bleibt sofort stehen.
(function () {
  if (!("IntersectionObserver" in window) || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  document.documentElement.classList.add("js");
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("da"); io.unobserve(e.target); } });
  }, { rootMargin: "0px 0px -8% 0px" });
  document.querySelectorAll("section, .band").forEach(function (el) {
    if (el.getBoundingClientRect().top < innerHeight) return;
    el.classList.add("gleiten"); io.observe(el);
  });
})();
</script>'''

def page(t):
    p = t["pre"]
    img = lambda src, alt, cls="phone", w=230, h=500: '<img class="%s" width="%d" height="%d" src="%simg/%s.jpg" alt="%s" loading="lazy">' % (cls, w, h, p, src, alt)
    vertrauen = "".join("<li>%s</li>" % x for x in t["vertrauen"])
    th = "".join("<th>%s</th>" % x for x in t["ver_th"])
    ver = "\n".join('            <tr><th scope="row">%s</th><td data-label="%s">%s</td><td data-label="%s">%s</td></tr>' % (r[0], t["ver_th"][1], r[1], t["ver_th"][2], r[2]) for r in t["ver"])
    rob = "\n".join('        <figure><img src="%simg/roboter/%s.png" width="150" height="150" alt="" loading="lazy"><figcaption>%s</figcaption></figure>' % (p, m, c) for m, c in t["rob"])
    tech = "".join("<li>%s</li>" % x for x in t["tech"])
    av = "\n".join(['        <img class="kind" src="%simg/avatar/%s.jpg" width="72" height="72" alt="" loading="lazy">' % (p, n) for n in KIDS] +
                   ['        <img class="erw" src="%simg/avatar/%s.jpg" width="72" height="72" alt="" loading="lazy">' % (p, n) for n in ADULT])
    medk = "".join('<img src="%simg/medaille/K-%s.png" width="52" height="52" alt="" loading="lazy">' % (p, m) for m in MED)
    faq = "\n".join("      <details><summary>%s</summary><p>%s</p></details>" % qa for qa in t["faq"])
    foot = "".join('<a href="%s">%s</a>' % x for x in t["nav_foot"])
    knopf = '<a class="cta" href="%s">%s</a>' % (t["testen"], t["cta"])
    return f'''<!doctype html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["ogdesc"]}">
<meta property="og:image" content="https://slange-a11y.github.io/quadrino/img/teaser.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="{p}icon.png">
<link rel="stylesheet" href="{p}style.css?v={CSSV}">
</head>
<body>
{BUEHNE}
<div class="kopf">
<div class="wrap">
  <header class="top">
    <img src="{p}icon.png" width="48" height="48" alt="">
    <div>
      <div class="name">Quadrino</div>
      <div class="sub">{t["sub"]}</div>
    </div>
    <div class="cta-klein"><a class="cta" href="{t["testen"]}">{t["cta_nav"]}</a></div>
  </header>
</div>
</div>

<div class="hero">
  <img src="{p}img/banner.jpg" width="1536" height="1024" srcset="{p}img/banner-768.jpg 768w, {p}img/banner.jpg 1536w" sizes="(max-width: 800px) 100vw, 1240px" alt="{t["banner_alt"]}">
</div>

<div class="wrap">
  <div class="intro intro-zeile">
    <div>
      <h1>{t["h1"]}</h1>
      <p>{t["intro"]}</p>
      <div class="cta-zeile">{knopf}<a class="cta leise" href="#so">{t["wie"]}</a></div>
      <ul class="vertrauen">{vertrauen}</ul>
    </div>
    <img src="{p}img/roboter/wave.png" width="150" height="150" alt="{t["robot_alt"]}">
  </div>

  <section id="so">
    <h2>{t["ver_h"]}</h2>
    <p>{t["ver_p"]}</p>
    <div class="tabelle">
      <table class="vergleich">
        <thead><tr>{th}</tr></thead>
        <tbody>
{ver}
        </tbody>
      </table>
    </div>
  </section>
</div>

<div class="band creme">
  <div class="wrap">
    <section>
      <div class="split">
        <div>
          <h2>{t["kind_h"]}</h2>
          <p>{t["kind_p1"]}</p>
          <p>{t["kind_p2"]}</p>
          <div class="roboter drei">
{rob}
          </div>
          <div class="medaillen">{medk}</div>
        </div>
        <div class="phones">{img(*t["kind_shots"][0])}{img(*t["kind_shots"][1])}</div>
      </div>
    </section>
  </div>
</div>

<div class="wrap">
  <section>
    <p class="zitat">{t["zitat"]}</p>
  </section>

  <section>
    <div class="split links">
      <div class="phones">{img(*t["erw_shots"][0])}{img(*t["erw_shots"][1])}</div>
      <div>
        <h2>{t["erw_h"]}</h2>
        <p>{t["erw_p1"]}</p>
        <p>{t["erw_p2"]}</p>
        <ul class="techniken">{tech}</ul>
      </div>
    </div>
  </section>

  <section>
    <div class="gewinn">
      {img("kind-gewonnen", t["gew_alt"][0])}
      {img("erw-gewonnen", t["gew_alt"][1])}
      <div>
        <h2>{t["gew_h"]}</h2>
        <p>{t["gew_p"]}</p>
      </div>
    </div>
  </section>
</div>

<div class="band graphit">
  <div class="wrap">
    <section>
      <h2>{t["fam_h"]}</h2>
      <p>{t["fam_p"]}</p>
      <div class="avatare">
{av}
      </div>
    </section>
  </div>
</div>

<div class="wrap">
  <section>
    <div class="preis-zeile">
      <div>
        <h2>{t["preis_h"]}</h2>
        <div class="preis">
          <div class="betrag">{t["betrag"]}</div>
          <div>
            <p>{t["preis_p"]}</p>
            <p class="note">{t["preis_note"]}</p>
          </div>
        </div>
        <div class="cta-zeile">{knopf}</div>
      </div>
      {img("kaufseite", t["kauf_alt"])}
    </div>
  </section>

  <section class="narrow fragen">
    <h2>{t["faq_h"]}</h2>
{faq}
  </section>

  <section class="schluss">
    <p class="zitat">{t["schluss"]}</p>
    <div class="cta-zeile">{knopf}</div>
    <p class="cta-hinweis">{t["cta_hinweis"]}</p>
  </section>

  <footer>
    <span>© 2026 Silvio Lange</span>
    {foot}
    <a class="lang" href="{t["lang_link"][0]}">{t["lang_link"][1]}</a>
  </footer>
</div>
{SKRIPT}
</body>
</html>
'''

if __name__ == "__main__":
    import os, time
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    CSSV = time.strftime("%Y%m%d%H%M")
    open("index.html", "w").write(page(T["de"]))
    open("en/index.html", "w").write(page(T["en"]))
    for u in ["support.html", "datenschutz.html", "en/support.html", "en/privacy.html"]:
        s = open(u).read(); open(u, "w").write(re.sub(r'style\.css\?v=\d+"', 'style.css?v=%s"' % CSSV, s))
    print("Seiten geschrieben, Stylesheet-Version", CSSV)
