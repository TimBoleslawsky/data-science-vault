When designing websites and online stores a common problem is the display policy. What books, movies, search requests, ... can we display to increase and possibly maximize user engagement. Recommendation systems try to solve this problem by **personalizing the display policy**. 
## Objectives & Proxies
The objective of recommendation systems (for example increased profit or user engagement) are often long term or so-called delayed objectives. These objectives are usually not easy to specify and measures and therefore hard to optimize directly. 

This leads to the need of proxies. One example for such a proxy would be user ratings. User ratings are easy to measure and relate to an individual product directly. Therefore, a recommendation system (that has for example the objective of increasing profit) can try to do this by increasing user ratings. But it is important to note that we abstract significantly and should always be cautious here.  
## Approaches for Recommendation Systems
Most recommender systems are based on user ratings $𝑌$, user preferences $Θ$ and product features $𝑋$. But based on available data and requirements we can choose different approaches to creating a recommendation system. 
### Content-Based Filtering
This approach is based on a regression model. The basic idea is this: Each item (e.g., movies, books, products) is described by a set of **features** (e.g., movie genre, author, keywords). A user’s preferences are determined based on past interactions with items (e.g., ratings, purchases). Items with the most similar features to what the user previously liked are recommended.

This approach works specifically well when we have good metadata about items and individual user preferences and when users have unique preferences. Another advantage is that it can recommend new items. 
Some disadvantages are that we risk "filter bubbles" (users only see content similar to what they’ve already interacted with) and that if a user has no history we cannot make any predictions (cold start problem). 

Two other main problems are high dimensionality and non-uniform missingness. For more details on how to solve high dimensionality, look [[Approaches for creating Regression Models#**Dealing with Highly-Correlated and Unnecessary Features**|here]]. For details on how to handle non-uniform missingness, look [[Handling Missing Values|here]].
### Collaborative Filtering
The basic idea behind collaborative filtering is that users with similar histories  
give similar scores to the same products. This is especially useful, when we don't have detailed product features and therefore can't do a linear regression. 

We solve collaborative filtering by using **matrix decomposition**. Like with content-based filtering, we can use regularization to combat high dimensionality or combine collaborative filtering with content-based filtering all together. 

