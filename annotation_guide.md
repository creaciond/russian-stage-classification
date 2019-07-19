# Annotation Guide

This is the guide handed out to the annotators; I used it myself to annotate all the plays.

## General ideas

TEI documentation page: [http://tei-c.org/release/doc/tei-p5-doc/en/html/ref-stage.html](http://tei-c.org/release/doc/tei-p5-doc/en/html/ref-stage.html)

Important:

1. If unsure about the direction, mark it as unknown.

2. Several types might be present at the very same direction.

3. Types are limited to the list:

_entrance, exit, business, delivery, modifier, location, setting + unknown_

No other type should be used.

4. [Trailers](https://tei-c.org/release/doc/tei-p5-doc/en/html/ref-trailer.html) — _занавес, конец_ — are not to be considered directions

## Types

### Entrance

TEI: _describes an entrance_.

Characters entering the stage. For the time being, this includes the line-up of already present characters (_те же и…_). Realistically, this should be `presence`, in opposition to `entrance` (save that one for later).

> Чацкий, Репетилов (вбегает с крыльца, при самом входе падает со всех ног и поспешно оправляется).

(Griboyedov, Gore ot uma)

> Входит Лариса, за ней человек с бутылкой шампанского в руках и стаканами на подносе.

(Griboyedov, Gore ot uma)

>Входят Огудалова и Лариса слева.

(Ostrovsky, Bespridannitsa)

### Exit

TEI: _describes an exit_.

Basically the opposite to `entrance`.

> Уезжает.

(Griboyedov, Gore ot uma)

> Лиза свечку роняет с испугу; _Молчалин скрывается к себе в комнату_.

(Griboyedov, Gore ot uma)

> _Вожеватов и Кнуров уходят._ Лариса подходит к Карандышеву.

(Ostrovsky, Bespridannitsa)

### Business

TEI: _describes stage business_.

An action undertaken by a character. Might be connected to a verb.

> Осматривается.

(Griboyedov, Gore ot uma)

> глядит в дверь налево

(Ostrovsky, Bespridannitsa)

> те же, Фоминишна и Тишка _(с вином на подносе)_

(Ostrovsky, Svoi ljudi)

> припадает к ее руке

(Chekhov, Djadja Vanja)

### Delivery

TEI: _describes how a character speaks._

May be a single adverb describing the manner of speaking, or a single noun in Dative (who does the character address?).

Concerns a communicative act (voice/silence etc.) — how something is delivered in a communicative way?

> со вздохом

(Griboyedov, Gore ot uma)

> хладнокровно

(Griboyedov, Gore ot uma)

> Тарелкин _(сконфуженный)_. Скажи ему, что некогда.... занят. 

(Sukhovo-Kobylin, Delo)

### Modifier
Usually result of other character’s actions. These might be changes of appearance (disguise, dressing as another character).

_A wild guess is that it's not really present in Russian drama._


### Location

TEI: _describes a location_.

Usually present in later plays. 

How to distinguish from `setting`: 

- `location` pinpoints a place at the scene where action takes place; 

- `setting` is more general; we expect it to be at the beginning of a scene/act (see below for details).

> еще в дверях

(Gogol, Revizor)

> _в зале у стола_, сердито

(Chekhov, Tri sestry)

### Setting

Such a direction would generally appear in the beginning of a scene or an act; in some cases, it just names the characters present on a stage — nevertheless, it’s still a setting.

Doesn’t usually include a verb (an active one), but may contain some “static”verbs (of standing, lying, etc.)

Indicators: sounds, weather, ...

> Чацкий, София, Лиза, Фамусов, толпа слуг со свечами.

(Griboyedov, Gore ot uma)

> У Фамусова в доме парадные сени; большая лестница из второго жилья, к которой примыкают многие побочные из антресолей; внизу справа (от действующих лиц) выход на крыльцо и швейцарская ложа; слева, на одном же плане, комната Молчалина. Ночь. Слабое освещение. Лакеи иные суетятся, иные спят в ожидании господ своих.

(Griboyedov, Gore ot uma)
> В доме Прозоровых. Гостиная с колоннами, за которыми виден большой зал. Полдень; на дворе солнечно, весело. В зале накрывают стол для завтрака.

(Chekhov, Tri sestry)

> За сценой цыгане запевают песню.

(Ostrovsky, Bespridannitsa)


