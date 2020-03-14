## PHASE 1

We plan to use given APIs to monitor demographics, as well as an already-provided set of crime statistic datasets given by county websites. However, by scraping Yelp for lists of restaurants and their information, we can use their ratings to find any outstanding correlations to high and low crime rates.

The first file, "scraper.py", grabs a list of businesses from the top 10 yelp restaurants for Riverside, CA. We plan to use this extensively to grab EVERY restaurant on every page.

The second file, "scraper2.py", uses helpful code from ScrapeHero to grab the top restaurants given a set of arguments of the desired location and business type.

The file "scraper.py" runs through a default list of top restaurants in Riverside, CA and compiles each restaurant's link into a .csv file, entitled "output.csv". Run using python3 scraper.py.

Run scraper2.py "Riverside" "Restaurants" to output a .csv file of 30 restaurants and their data (ranking, name, review count, average rating, address, price, and url).

## PHASE 2

In terms of the datasets that we used, we used the restaurants in Riverside found through Yelp dataset and the Riverside Crime Reports dataset. The Riverside restaurants Yelp dataset displays the name, price, rating, number of reviews, and location of a restaurant. The Riverside Crime reports dataset displays the date, type, and location of a crime. 

In phase 2, we are cleaning out both our Yelp and Crime Reports datasets. In regards to the Crime Reports dataset, it had mostly categorical values so most of the cleaning was just dropping blank values as well as dropping columns irrelevant to our question at hand. In the end, our EDA for this portion consisted mostly of finding how often certain crimes occur as well as their frequencies.

We can see that other than the category "other", theft and assault were one of the highest common crime in Riverside. The most common premises of crime are highways and residential areas.

For the Yelp dataset, we found the distribution of prices and saw the correlation between the ratings and review counts, as five star restaurant with only one review has less weight than a four star restaurant with 1k+ reviews. We filtered out the number of reviews to remove the outliers and also mapped the distribution of rating as well.

From the cheaper restaurants in Yelp (indicated by a single dollar sign), we found that they are not as popular as most of them have under 200 reviews on their page.

You can run the code through Jupyter. We do have some nested folders so if an input does not display, try modifying the location of the directory of which the file is pointing to.

## PHASE 3

For this phase, you are asked to perform data analysis. This can include building a model to perform prediction (like applying linear regression or kNN) or clustering. You can also use the models for data analysis, not just ‘predictions’. For example, in linear regression we saw that the resulting coefficients tell us how the features are correlated to the target variable. So, this analysis might help you identify features of importance with respect to a target feature in the dataset.

For analysis, identify two hypotheses (or questions) you are curious about regarding your data and then proceed to use ML techniques to try to answer these questions. If you decide to build models for predictions or classification, be sure to setup your problem so that you have a training, validation and testing dataset and you evaluate at least two ML / Data Mining techniques and compare their results.

PHASE 3 README must:
identifies and describes the dataset and problem at a high-level

Summary of the data analysis process performed for Phase 3 and the results / observations obtained; Contain information about how to run your code (include any dependencies, etc.).
