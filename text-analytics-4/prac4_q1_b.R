library(wordcloud)
library(tm)
wordcloud("It’s tempting jump straight mining, first, need get data ready. 
	This involves closer look attributes data values. Real-world data typically noisy, 
	enormous volume (often several gigabytes more), may originate hodge-podge heterogenous sources. 
	This chapter getting familiar data. Knowledge data useful data preprocessing (see Chapter 3), 
	first major task data mining process. You want know following: What types attributes fields make data? 
	What kind values attribute have? Which attributes discrete, continuous-valued? What data look like? 
	How values distributed? Are ways visualize data get better sense all? Can spot outliers? Can measure 
	similarity data objects respect others? Gaining insight data help subsequent analysis. “So learn data 
	that’s helpful data preprocessing?” We begin Section 2.1 studying various attribute types. These include
	 nominal attributes, binary attributes, ordinal attributes, numeric attributes. Basic statistical descriptions
	  used learn attribute’s values, described Section 2.2. Given temperature attribute, example, determine mean 
	  (average value), median (middle value), mode (most common value). These measures central tendency, 
	  give us idea “middle” center distribution.",
min.freq=1, colors=brewer.pal(6,"Dark2"), random.order=FALSE)