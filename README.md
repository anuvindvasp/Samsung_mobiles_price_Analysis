# Samsung Mobiles Price Analysis
![image](https://github.com/user-attachments/assets/6fbf2ff9-9a44-4f7e-bdd0-1f3a4525b0bc)



## Introduction
Samsung mobile's data Analysis using Python.

Scrape various product details including reviews of product from Flipcart and store it in a dataframe and do an initial data exploration and find out the statistical analysis of those product price and other features

### Data Source : Web scraping
### Notebook : Jupyter Notebook
### Data Visualization : Matplotlib,Seaborn
# Analysis
### Data Cleaning:
Removed currency symbols and commas from the 'Price' column. Cleaned 'Battery' column to extract only numeric values.

### Data Exploration:
Found descriptive statistics for 'Price', 'Rating', and 'Battery' columns. Plotted distributions and relationships between variables using seaborn and matplotlib.

### Price Analysis:
Average price of Samsung mobiles is approximately ₹36,789. Most expensive mobile's price is ₹1,64,999, while the lowest priced one is ₹11,348. Majority of phones fall within the ₹15,999 range.

### Rating Analysis:
Maximum rating of Samsung mobiles is 5. Average and most common rating is 4.2. Rating tends to increase with price, but slightly decreases when the rating is maximum.

### Battery Analysis:
Maximum battery capacity is 6000 mAh, while the minimum is 3300 mAh. Most common battery capacity is 5000 mAh for Samsung mobiles.

### Camera Analysis:
Most common rear camera resolution is 50MP. Second-largest number of phones have a combination of 50MP + 2MP + 13MP Front Camera. The top camera resolution is 200MP for the rear and 12MP for the front.

### Correlation Analysis:
Battery and Price show a negative strong correlation. There is no significant correlation between Rating and Price.

## Conclusion
The analysis of Samsung mobile phones from the dataset reveals several key insights. The average price of Samsung mobiles is approximately ₹36,789, with the most expensive phone priced at ₹164,999 and the least expensive at ₹11,348. The distribution of prices indicates that a majority of phones fall within the range of ₹20,000 to ₹40,000, with some outliers priced much higher. Rating seems to have a positive correlation with price, indicating that higher-priced phones tend to have higher ratings, though there is a slight decrease in ratings for the most expensive phones. In terms of battery capacity, the most common capacity is 5000 mAh, with a range from 3300 mAh to 6000 mAh. Camera configurations vary, with 50MP rear cameras being the most common, followed by combinations like 50MP + 2MP + 13MP Front Camera. Additionally, there is a negative strong correlation between battery capacity and price, while no significant correlation is observed between rating and price.
