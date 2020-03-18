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

The Crime Report dataset is all the reported crimes in Riverside from the year 2018. It contains information about the crime report as well as the crime itself (location, date, crime type, etc). The Yelp restaurant dataset is all the restaurants in Riverside. It contains ratings, price, location, and more. We plan to use the datasets to compile information and find correlations between different areas in Riverside, the Riverside restaurants, and the number of crime reports issued per zone (North, West, East, Central).

Specifically, we are looking to see if the quality of the restaurants (as weighted by its price and ratings) affect the crime rate of a certain zone. We are also looking to see if restaurants tend to congregate around a certain zone and if that congregation somewhat due to the amount of crime in that zone.

We found the rate of crimes by finding each unique date of crime per crime zone and dividing dividing that number under the total number of crimes in that zone. From this we compared it with the amount of restaurants in a zone. We concluded that restaurants tend to congregate around zones with less crime.

To answer our first question, we took the average rating and price of all the restaurants per zone and compared it to the crime rate of a certain zone. We concluded that an unpopular restaurant with a high price point is less likely to have crime reports in that zone. Inversely, we can also say that a lower priced, popular restaurant is more likely to be in a crime-ridden zone. 