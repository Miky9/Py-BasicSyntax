#!/usr/bin/python
# -*- coding: utf-8 -*-
from engine import scene, options, get
import config

name = get("Než začneš hrát, řekni mi své jméno: ")

def intro():

    scene((
    	'Škvírami v dřevěném zátarasu na jediném okně v krčmě prosvítal do místnosti pramínek světla.',
    	'Seděl jsem založenýma rukama na židli a vyčkával.',
    	'Ticho přerušil zvuk dopadající čepele do dřeva.',
    	'Protivník se konečně ukázal.',
    	'%s: Kolik si vsadíš?' % (name),
    	'Muž: Na kolik se ceníš?',
    	'Muž vyhlížel nebezpečně.',
    	'Jeho celkový vjem potulného bezdomovce doplňoval křivý nos a žluté zuby, když se posměšně usmál.',
    ))

    options( "Na kolik se ceníš?: ", ("Deset zlatých", "Dvacet zlatých"), (pay_ten, pay_twenty))

def pay_ten():

	scene((
		'%s: Co takhle deset zlatých?' % (name),
		'Muž: Tak málo?',
		'Podivil se a promnul si oči.',
		'Muž: Nevadí, půjdu na tebe zlehka.',
		'Poplácal mě po zádech a já pomalu vstal.'
	))

	fight()

def pay_twenty():

	scene((
		'%s: Dám ti do těla za dvacet zlaťáků.' % (name),
		'Muž: Teda, ty si věříš!',
		'Zasmál se muž hlasitě.',
		'Muž: Mno dobře, jak myslíš.',
		'Muž: Koukej si těch dvacet zasloužit!'
	))

	fight()

def fight():

	scene((
		'Vyšli jsme ven z krčmi a připravili se k pěstnímu souboji.',
		'%s: Na tři?' % (name),
		'Muž: Tři!',
		'A muž vyrazil.'
	))

	options("Bojuj!: ", ('Bránit se', 'Zaútočit'), (fight_defence, fight_attack))

def fight_defence():

	scene((
		'Nestihl jsem pořádně zareagovat a instinktivně přesunul paže před obličej.',
		'Nic jsem neviděl a než jsem se nadál, už jsem ležel na zemi s nožem u krku.'
	))

	after_fight()

def fight_attack():

	scene((
		'Ihned jsem zaregistroval, co muž chystal a místo abys se snažil útoku vyhnout, vyrazil jsem vpřed.',
		'To útočníka zarazilo, ale pokračoval.',
		'Mířil jsem dlaní na mužovu bradu, aby šel k zemi, místo toho jsem se znenadání ocitnul za ním.',
		'Nejhorší je nechat protivníka dostat se vám za záda...',
		'Ucítil jsem chladnou čepel na zádech.',
		'Muž: Promiň, těch dvacet zlatých si nezasloužíš.'
	))

	after_fight()

def after_fight():

	scene((
		'Muž: Mám pro tebe nabídku.',
		'%s: Jakou?' % (name),
		'Už jsem se vzpamatoval z neočekávané prohry a oklepával zničenou látku, kterou jsem nosil místo šatů.',
		'Muž: Chtěl bys naučit pár triků?',
		'-- KONEC UKÁZKY --'
	))

