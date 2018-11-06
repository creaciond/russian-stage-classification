# Short Text Classification: a Case of Stage Directions in Russian Drama
This is a repository for bachelor's thesis written in School of Linguistics, NRU HSE, in academic year of 2018/19. 

## What is this about?

I already did a project on Russian Drama Corpus and its stage directions — it can be found here: [Stage Directions in Russian Drama](https://github.com/creaciond/russian-drama). It dealt more with the quantitative part of the research and exploring corpus trends; at this one, I want to focus on the part which deals more with computational linguistics and machine learning, that is to extract linguistic features and run several different models.

Russian Drama Corpus (or shortly, RusDraCor) can be found at [dracor-org/rusdracor](https://github.com/dracor-org/rusdracor); it is also available in a more user-friendly format at [Dracor website](https://dracor.org/rus).

## What's inside

Nothing so far :) But there will be:

* some Jupyter notebooks
* bibliography I used throughout the work (in repo Wiki)
* links to tutorials (in repo Wiki)
* probably some other Python code
* resulting dataset

## Roadmap and plans

**November**
[ ] _Literature analysis_ — it seems that there is some existing work in the field, so I'd better get acquainted with that. The majority of works I’ve seen so far treat this problem in the light of information retrieval, they are generating a search query out of the texts — which can help in highlighting the most important words. There’s also plenty of works regarding tweets classification
[ ] _Analysing other TEI corpora_ — there is a certain corpus (a Shakespeare corpus, for sure; probably, also a French one?) which already have their <stage> annotations; it might be worthy to contact them and ask whether that was done manually or with some programming

**December**
[ ] _Data (re)annotation_ — probably the previous annotation was inconsistent and it would be nice to take another look at it; also, the machine learning algorithms (not to mention neural networks!) need quite a lot of data, so probably I should annotate another couple of plays — that shouldn’t take long; I believe I also need to annotate a separate play or two for a test set
[ ] _Data analysis_ — after annotating, I should definitely take a very intent look at the types and discover as many trends as possible
[ ] _Feature extraction_ — last year, we did morphology and some kind of semantics; this year, I want to do semantics based on vector models, and also some syntax analysis. There’s some problem with that, as there are several syntax parsers for Russian, and I have to decide which one works best for the case

**January**
[ ] _First attempts?_ — I should take a look at what we’ve done for my 3rd year paper, take into consideration the September meetup feedback and try to do something with that
[ ] _Rule-based classification_ — we have some super-typical directions, such as _уходит_ for exit or _входит_ for entry; we can separate those by applying certain rules; at least, that would cut off several types

**February**
[ ] _Machine learning_ — creating and running new models based on machine learning algorithms; some work is already done, and this is the time to compare different models/algorithms
[ ] _Neural networks_ — run several experiments on neural networks of simple architecture; I doubt that the performance is going to be much better than simpler models, because the networks require so much more data (like, in some papers they use 10k examples for training — that’s approximately the half of stage directions we have in RusDraCor

**March**
[ ] _Neural networks p2_ — running all the popular network configurations on the same material
[ ] _Combining rules and machine learning_ — at this point, we should get an idea of how well different models are working, so probably some combinations will be more resultative?

**April, May**
[ ] Finishing what has to be finished and writing the whole thing in a proper manner 
  
## Important dates
|**Module**|**Event**                    |**Date**             |
|:--------:|:---------------------------:|:-------------------:|
|3rd       |Project Proposal presentation|TBA _(end of March?)_|
|4th       |Written paper deadline       |TBA                  |
|4th       |Final thesis presentation    |TBA _(early June?)_  |
