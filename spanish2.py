"""Spanish infinitives trainer"""
import easygui as eg
import random

pronouns = ["i", "you", "he", "she", "it", "we", "you(pl)", "the"]
regular_verbs = {
    "aceptar": "to accept", "acompañar": "to accompany", "activar": "to activate", "adelantar": "to advance", "administrar": "to administer",
    "admirar": "to admire", "admitir": "to admit", "adoptar": "to adopt", "afirmar": "to affirm", "agarrar": "to grab",
    "alcanzar": "to reach", "alegrar": "to make happy", "alojar": "to accommodate", "ampliar": "to enlarge", "andar": "to walk",
    "anunciar": "to announce", "apagar": "to turn off", "aparecer": "to appear", "aplaudir": "to applaud", "aprender": "to learn",
    "asistir": "to attend", "asustar": "to scare", "atacar": "to attack", "atender": "to attend to", "atraer": "to attract",
    "aumentar": "to increase", "ayudar": "to help", "bailar": "to dance", "bañar": "to bathe", "bajar": "to go down",
    "barrer": "to sweep", "beber": "to drink", "buscar": "to search", "cambiar": "to change", "caminar": "to walk",
    "cantar": "to sing", "cargar": "to carry", "causar": "to cause", "celebrar": "to celebrate", "cerrar": "to close",
    "cocinar": "to cook", "colocar": "to place", "comenzar": "to begin", "comer": "to eat", "compartir": "to share",
    "comprar": "to buy", "conducir": "to drive", "conectar": "to connect", "conocer": "to know", "conseguir": "to get",
    "conservar": "to preserve", "construir": "to build", "contar": "to count", "contribuir": "to contribute", "controlar": "to control",
    "correr": "to run", "crear": "to create", "creer": "to believe", "cruzar": "to cross", "cuidar": "to take care of",
    "dar": "to give", "deber": "to owe", "decidir": "to decide", "dejar": "to leave", "demostrar": "to demonstrate",
    "destruir": "to destroy", "devolver": "to return", "dibujar": "to draw", "dirigir": "to direct", "discutir": "to discuss",
    "dividir": "to divide", "dormir": "to sleep", "duchar": "to shower", "dudar": "to doubt", "durar": "to last",
    "elegir": "to choose", "eliminar": "to eliminate", "emborrachar": "to get drunk", "empezar": "to start", "encontrar": "to find",
    "enseñar": "to teach", "entrar": "to enter", "enviar": "to send", "escalar": "to climb", "escoger": "to choose",
    "esconder": "to hide", "escribir": "to write", "escuchar": "to listen", "esperar": "to wait", "establecer": "to establish",
    "estacionar": "to park", "estar": "to be", "estudiar": "to study", "evitar": "to avoid", "examinar": "to examine",
    "exigir": "to demand", "explicar": "to explain", "explorar": "to explore", "fijar": "to fix", "firmar": "to sign",
    "ganar": "to win", "gastar": "to spend", "guardar": "to keep", "gustar": "to like", "hablar": "to speak",
    "hacer": "to do/make", "hallar": "to find", "heredar": "to inherit", "ignorar": "to ignore", "imaginar": "to imagine",
    "importar": "to import", "imprimir": "to print", "incluir": "to include", "informar": "to inform", "inscribir": "to enroll",
    "insistir": "to insist", "intentar": "to try", "interesar": "to interest", "introducir": "to introduce", "invitar": "to invite",
    "ir": "to go", "jugar": "to play", "juntar": "to gather", "lavar": "to wash", "llegar": "to arrive",
    "llevar": "to carry", "llorar": "to cry", "mantener": "to maintain", "manejar": "to handle/drive", "mandar": "to send",
    "mirar": "to look", "morder": "to bite", "mover": "to move", "nadar": "to swim", "necesitar": "to need",
    "negar": "to deny", "notar": "to notice", "obedecer": "to obey", "obtener": "to obtain", "ocurrir": "to occur",
    "ofrecer": "to offer", "oír": "to hear", "olvidar": "to forget", "operar": "to operate", "opinar": "to opine",
    "organizar": "to organize", "pagar": "to pay", "parecer": "to seem", "partir": "to divide", "pasar": "to pass",
    "patinar": "to skate", "pedir": "to ask for", "pegar": "to stick/hit", "pensar": "to think", "perder": "to lose",
    "permitir": "to permit", "pertenecer": "to belong", "pesar": "to weigh", "pintar": "to paint", "planear": "to plan",
    "poder": "to be able to", "poner": "to put", "practicar": "to practice", "preparar": "to prepare", "presentar": "to present",
    "probar": "to try/taste", "producir": "to produce", "proteger": "to protect", "proveer": "to provide", "quedar": "to stay/remain",
    "quemar": "to burn", "querer": "to want", "realizar": "to carry out", "rechazar": "to reject",
    "recibir": "to receive", "recomendar": "to recommend", "recordar": "to remember", "regresar": "to return", "reír": "to laugh",
    "repetir": "to repeat", "resolver": "to resolve", "responder": "to respond", "robar": "to rob", "romper": "to break",
    "salir": "to go out", "saltar": "to jump", "seguir": "to follow", "sentar": "to sit", "sentir": "to feel",
    "ser": "to be", "servir": "to serve", "soñar": "to dream", "subir": "to go up", "sugerir": "to suggest",
    "superar": "to overcome", "suspirar": "to sigh", "tener": "to have", "terminar": "to finish", "tocar": "to touch/play",
    "tomar": "to take/drink", "trabajar": "to work", "traducir": "to translate", "traer": "to bring", "tratar": "to treat",
    "usar": "to use", "utilizar": "to utilize", "vaciar": "to empty", "valorar": "to value", "ver": "to see",
    "viajar": "to travel", "vivir": "to live", "volver": "to return"
}
conjugations = {
    "ar": {
        "i": "o",
        "you": "as",
        "he": "a",
        "she": "a",
        "it": "a",
        "we": "amos",
        "you(pl)": "ais",
        "the": "an"
    },
    "er": {
        "i": "o",
        "you": "es",
        "he": "e",
        "she": "e",
        "it": "e",
        "we": "emos",
        "you(pl)": "eis",
        "the": "en"
    },
    "ir": {
        "i": "o",
        "you": "e",
        "he": "es",
        "she": "es",
        "it": "es",
        "we": "imos",
        "you(pl)": "is",
        "the": "en"}}

while True:
    infinitive = random.choice(list(regular_verbs.keys()))
    pronoun = random.choice(pronouns)
    ending = infinitive[-2] + infinitive[-1]
    new_word = ""
    if ending == "er":
        new_word = [infinitive.replace(ending, conjugations[ending][pronoun])]
    elif ending == "ar":
        new_word = [infinitive.replace(ending, conjugations[ending][pronoun])]
    elif ending == "ir":
        new_word = [infinitive.replace(ending, conjugations[ending][pronoun])]

    new_word = str(new_word).replace('[','').replace(']','').replace('\'','')

    answer = eg.enterbox(f"Your words is [{infinitive}], the pronoun is [{pronoun}],\nWhat is the new verb:")
    if answer == new_word:
        eg.msgbox("= That is correct =")
        print("Correct")
        print(f"Your answer was {answer} which is Correct\n"
              f"With the pronoun [{pronoun}] the word [{infinitive}] changes to [{new_word}]\n"
              f"Which means [{regular_verbs[infinitive]}]")
    if answer != new_word:
        eg.msgbox("= That is incorrect =")
        print("Incorrect")
        print(f"Your answer was {answer} which is Incorrect\n"
              f"With the pronoun [{pronoun}] the word [{infinitive}] changes to [{new_word}]\n"
              f"Which means [{regular_verbs[infinitive]}]")








# answer = verb replace ar with pronoun
