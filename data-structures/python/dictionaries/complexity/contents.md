# Computational complexity of dictionaries

## Video
Learn more about the speed of dictionaries in this video:

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_mjatxx9k&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_t24tqi37)

## Reading
The time complexity for getting an item out of a dictionary $$O(1)$$. This means that the time the following command takes:  

    >>> basket['apple']
    6

does not depend on the size of basket. No matter if `basket` contains 10 items or 1,000,000 items, it takes roughly the same time to compute.

The same goes for other types of lookup, like the `in` operation. With dictionaries the `in` operations is $$O(1)$$. So also for the computation time of the following command it does not matter how big `basket` is:

    >>> if 'banana' in basket:
    ...   print("We've got bananas!")
    ...
    We've got bananas!

This is a big difference with list. With lists, the operation `in` is $$O(N)$$.

That lookup times for dictionaries are an $$O(1)$$ operation is a *strange and counter-intuitive* fact, and why this is true is well beyond the scope of this text, but it should give you an idea of the power of
dictionaries and why they are used so often: Checking if a key is present in a
dictionary or retrieving the value stored with that key are both **constant
time** $$O(1)$$ operations, irrespective of the number of elements
stored in that dictionary.
