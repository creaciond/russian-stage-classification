# Project workflow

## Autumn semester, 2018

**November**

- [x] _Literature analysis_ — it seems that there is some existing work in the field, so I'd better get acquainted with that. The majority of works I’ve seen so far treat this problem in the light of information retrieval, they are generating a search query out of the texts — which can help in highlighting the most important words. There’s also plenty of works regarding tweets classification

_UPD Dec 10:_ at least I got in gathered!

- [x] _Analysing other TEI corpora_ — there is a certain corpus (a Shakespeare corpus, for sure; probably, also a French one?) which already have their <stage> annotations; it might be worthy to contact them and ask whether that was done manually or with some programming
  
- [x] _Preprocessing enhancement_  — preprocessing for quantitative research didn't treat NEs (named entities) as proper names. This time, all named entities should have the same "special" word (`ИМЯ`) and the same POS tag (`PROPN`).

**December**

- [x] _Data (re)annotation_ — probably the previous annotation was inconsistent and it would be nice to take another look at it; also, the machine learning algorithms (not to mention neural networks!) need quite a lot of data, so probably I should annotate another couple of plays — that shouldn’t take long; I believe I also need to annotate a separate play or two for a test set

_UPD May:_ it's FINALLY over!

- [x] _Data analysis_ — after annotating, I should definitely take a very intent look at the types and discover as many trends as possible

- [x] _Feature extraction_ — last year, we did morphology and some kind of semantics; this year, I want to do semantics based on vector models, and also some syntax analysis. There’s some problem with that, as there are several syntax parsers for Russian, and I have to decide which one works best for the case

## Winter/spring semester, 2019

**January**

- [x] _First attempts?_ — I should take a look at what we’ve done for my 3rd year paper, take into consideration the September meetup feedback and try to do something with that

- [x] _Rule-based classification_ — we have some super-typical directions, such as _уходит_ for exit or _входит_ for entry; we can separate those by applying certain rules; at least, that would cut off several types

**February**

- [x] _Machine learning_ — creating and running new models based on machine learning algorithms; some work is already done, and this is the time to compare different models/algorithms

**March**

- [x] _Combining rules and machine learning_ — at this point, we should get an idea of how well different models are working, so probably some combinations will be more resultative?

**April, May**

- [x] Finishing what has to be finished and writing the whole thing in a proper manner 
  
## Important dates

|**Module**|**Event**                    |**Date**             |
|:--------:|:---------------------------:|:-------------------:|
|3rd       |Project Proposal presentation|March 26, 2019|
|4th       |Written paper deadline       |June 4, 2019|
|4th       |Final thesis presentation    |June 18, 2019|
