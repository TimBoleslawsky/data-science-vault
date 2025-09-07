
For our final report, we want to summarize all the concepts we learned and the takeaways of this course. The intended readers are our future selves. We imagine this report to be a guide to ourselves (or other data scientists) to use, when facing difficult real world problems. We want to help the reader to organize and structure their thinking process to hopefully make abstracting real world's problems into mathematical problems easier. For this reason, we call this final report “The Mathematical Thinking Handbook for Data Scientists”. 

We start this report with a short introduction of what mathematical thinking is and why it is important. Then we have two main parts. First we want to introduce the main concepts that we need to keep in mind, when thinking about abstracting real world problems into mathematical problems. Second, we want to provide key takeaways from this course to support the mathematical thinking process of the reader. Because we are preparing this especially for data scientists, we always want to make a connection to how a data scientist might find these concepts or takeaways helpful (Important note: we want to focus on the mathematical thinking process of data scientists, not the methodical knowledge of data scientists). 

## Introduction
Mathematical thinking is a structured, logical, and creative approach to solving problems. It enables us to abstract complex real-world scenarios into manageable mathematical models. For data scientists, mathematical thinking is essential—it provides the foundation for analyzing data, building models, and deriving insights. By embracing mathematical thinking, data scientists can tackle challenges systematically, adapt solutions iteratively, and communicate results effectively.

Mathematical thinking as a concept is composed of mathematical reasoning, mathematical modeling, and problem-solving: 

- Mathematical reasoning is about two things. First, clearly stating the problem, defining variables, and establishing conditions or assumptions. Second, exhaustively and incrementally drawing conclusions to come to a sound conclusion.
	
- Applied problems are not mathematical from the beginning. You must identify and formulate them as such. A model serves as a way to represent the complex reality in a convenient way, so that we can draw conclusions about it and gain access to mathematical and computational techniques. 
	
- When talking about problem-solving, we mean the process of identifying a challenge, understanding its context and underlying factors, generating potential solutions, and implementing the most effective strategy to resolve it.
## Part 1 - Fundamental Concepts Supporting Mathematical Thinking
This section explores key mathematical concepts, important to the mathematical thinking process. We also want to highlight interconnectivity and importance for data scientists to make clear what further implications the concepts have both in- and outside of data science.  
### Part 1.1 - Functions, Equations, and Geometry
Functions and equations serve as the building blocks of mathematical modeling. They allow us to express relationships between variables, while geometry allows us to map abstract ideas into tangible representations. All three concepts provide a language that allows us to formulate abstract real world problems into mathematical problems. 

Interconnectivity:
- Functions and equations provided the groundwork for optimization problems. Understanding the relationships between variables is crucial for finding maximum or minimum values in real-world scenarios.

Importance for data scientists:
- With a basic understanding of functions, analyzing data becomes much easier. As a data scientist, you should be able to look at a curve and roughly guess the function that describes this curve. 
- Understanding functions helps data scientists preprocess and transform data. For example, normalizing data or creating polynomial features for machine learning models requires working with mathematical functions.
- Data scientists always answer real world questions. Having a tool to translate these real world questions is very valuable. 
### Part 1.2 - Optimization Problems
Optimization problems illustrate how to find the best possible solution under given conditions. They provide us with means to formalize goals and constraints, enabling structured problem-solving.
While the applications of these problems can be almost anything, it is very useful to know the basic structure of optimization problems as a guide to modeling problems: 
- Objective function: This is the function to be optimized (minimized or maximized).
- Constraints: Conditions that the solution must satisfy, often represented as equations or inequalities.
- Variables: The input unknowns that change the value of the objective function. 

Interconnectivity:
- Optimization relies on functions to define objectives and constraints. Later, discrete mathematics introduced graph-based optimization, extending the scope of this concept.

Importance for data scientists:
- As a data scientist you should be able to understand the concept of optimization problems to better grasp problems such as balancing computational efficiency with model accuracy.
### Part 1.3 - Dynamic Systems
Dynamic systems focus on processes that change over time. These models break down complex behaviors into smaller, manageable components. Dynamic systems provide tools to analyze and predict changes over time. They help us understand how systems evolve and adapt, emphasizing the interconnectedness of variables.
When talking about dynamic problems, it is essential to understand the concept of the rate of change and how it is connected to the derivative. 

Interconnectivity:
- Dynamic systems intersected with probability and statistics when accounting for variability over time.
- Because the derivative is central to dynamic systems, a clear understanding of functions is necessary when talking about dynamic systems.

Importance for data scientists:
- Dynamic systems provide a framework for modeling processes that evolve over time, a common scenario in data science applications like time-series analysis or predictive maintenance. As a data scientist you should be comfortable with the concepts of the “rate of change” and what the importance of it is when analyzing changes over time. 
### Part 1.4 - Probability and Statistics
Probability and statistics allow us to quantify uncertainty and make informed decisions based on data. They are critical for drawing conclusions and evaluating risks making them the foundation of decision making in the mathematical thinking process. Both provide some form of reassurance to the conclusions we make in the mathematical thinking process (confidence in logic). They also emphasize a need for careful reasoning.

Interconnectivity:
- Probability is used in dynamic systems, for example in determining risks or forecasting outcomes. Statistical reasoning also supports optimization, where data-driven insights inform better solutions

Importance for data scientists: 
- The problems data scientists face often rely on hypothesis testing and other data-driven decision making to provide an answer. Both probability and statistics need to be understood to gain confidence for these answers and decisions. 

### Part 1.5 - Discrete Mathematics
Discrete mathematics focuses on structures like graphs and logical relationships. Discrete mathematics also bridges conceptual and applied problem-solving. Graph theory, in particular, provides tools to model relationships and solve optimization problems.

Interconnectivity:
- Discrete mathematics ties closely to optimization by providing frameworks like minimum spanning trees and shortest paths. It also complements dynamic systems by modeling complex networks.

Importance for data scientists:
- Discrete mathematics equips data scientists with the tools to model and solve problems involving discrete structures, such as relationships between entities or decision paths. These structures provided a bridge between programming and mathematical thinking.
## Part 2 - Key Takeaways to Support Mathematical Thinking
This section summarizes the lessons learned and their practical implications for data scientists. We also want to include one example problem that demonstrates each takeaway the best. This way the reader can remember (or look up) the specific problem and understand the takeaway in the context of a specific problem.
### Part 2.1 - Iterative Refinement Is Essential
Mathematical thinking is rarely about finding the solution immediately. Instead, it emphasizes refining initial models iteratively until they align with the problem’s requirements. Even if problems initially seem straightforward, their solutions usually require multiple layers of refinement. Initial assumptions are rarely perfect; revisiting and improving them leads to clarity and robustness. 

The iterative process also leads to more exhaustive solutions. By not being satisfied with a given solution, and by iterating methodically, solutions that may not have seemed possible, can be found. 

Relevance to Data Science:
- Refining models as new data or insights become available, mirrors the iterative process of problem-solving. In data science, iteration is central to developing models, refining features, and optimizing algorithms. 
  => Keep an iterative approach in mind and refine your solutions to ensure that models remain robust and accurate!

Example problem:
- The drug dosage problem is a great example for this concept. The drug dosage problem is about helping a drug company that wants to know how to calculate a suitable dose and time between doses to maintain a safe but effective concentration of a drug in the blood. 
- One initial assumption might be that the decrease rate of the drug in the blood is linear. This leads to a serviceable model that works, but only under some assumptions. By further improving on this model we can achieve a very realistic representation of this problem that works without these assumptions, emphasizing the importance of iterative refinement. 
### Part 2.2 - Communicate Clearly and Concisely
The ability to articulate solutions is as critical as finding them. Mathematical thinking is not just about finding solutions but also about communicating them clearly. Mathematical models must be presented clearly to stakeholders, whether through step-by-step explanations, visualizations, or reports. 

Writing out steps in problem solving enhances reproducibility and helps to clearly communicate a solution. Visual tools like graphs, charts, and diagrams in geometry and statistics serve as powerful aids in conveying complex ideas succinctly. But being clear and concise is not only helpful when communicating, it also makes the problem solving process itself more manageable. 

Relevance to Data Science:
- Data scientists always want to answer real world questions. Therefore the stakeholder, that we as data scientists want to present our answer to, is always another human. This means that the ability to present and communicate an answer is as important as the answer itself. Especially in interdisciplinary fields like data science, where mathematical insights inform decision-making.  
  => Keep the stakeholder in mind and present your findings accordingly!
  
Example problem:
- To illustrate this concept we will look at the restaurant problem. The restaurant problem is about person A, who wants to avoid person B, who wants to meet person A at lunchtime. Both persons have the option of going to a regular restaurant (20 min dining time) and to a fancy restaurant (50 min dining time).
- Now when reading this problem you might want to immediately jump to (for you) obvious conclusions. But it is very important to document and communicate your thinking process step by step, without leaving uncertainty. 

### Part 2.3 - Simplification Is Key
A hallmark of mathematical thinking is the ability to simplify complex problems without losing their essence. Simplifying complex problems into smaller components allows for easier analysis and implementation. Sometimes it goes even further than this and only simplification makes analysis even possible in the first place.  

Relevance to Data Science:
- It is again important to emphasize how close data scientists work with real world problems. Real world problems are usually very complex. Therefore data science frequently involves distilling large, complex datasets into actionable insights. To make this task manageable, start with simple solutions, but be careful not to lose information.  Simplification without losing essential information is crucial for creating interpretable models and visualizations!

Example problem:
- The map coloring problem is about how many colours you may need to colour a map so that neighbouring countries have different colours. When thinking about this problem without simplification tools in mind, it is almost impossible to come to a sensible conclusion. Only by abstracting this problem, for example, into a graph, can it become reasonably solvable.
### Part 2.4 - Exhaustiveness Leads to Better Results
The principle of being exhaustive—leaving no stone unturned—is often the key to arrive at a satisfying solution. Combining this with the iterative approach we already presented, leads to more precise and therefore better results. That being said, exhaustiveness needs to be paired with  intentionality to ensure efficiency.

Relevance to Data Science:
- Data science problems in general can be quite misleading and prone to false conclusions. Comprehensive exploration allows data scientists to uncover hidden patterns, correlations, and causal relationships that could impact decision-making. It ensures that insights are not based on partial or misleading data.  
  => Be exhaustive in your analysis without losing intentionality to find the truthful core of a problem without losing efficiency!

Example problem: 
- For an example of this concept, let’s look at the bridge problem. The bridge problem describes a connection between two cities via two roads that in the middle cross over a bridge. Each driver can now choose one of these roads and choose if they want to cross the bridge to get to the other road at the half-way mark. Now the question is, what would each driver do? What would the travel time be? And is there an equilibrium state that forms? 
- Initially this problem might seem somewhat obvious and arriving at a first solution might be simple. But by being exhaustive and looking from multiple different angles, it becomes apparent that every attempt to solve the problem provides new insights.
### Part 2.5 - Balancing Intuition and Rigor
Mathematical thinking requires both logical and creative approaches. This makes it versatile but also demands caution. Visualizing problems often provide intuitive insights. For instance, graphing functions helps us understand relationships between variables more clearly, bridging the gap between abstract equations and tangible interpretations. But missteps in statistical reasoning could lead to flawed conclusions, highlighting the importance of precision. Using intuition to guide initial problem-solving approaches, while ensuring accuracy and reliability through rigorous testing is a very valuable skill in mathematical thinking.

Relevance to Data Science:
- A key step in the data science process is Exploratory Data Analysis (EDA). Here this balance between intuition and rigor is immensely helpful, if done correctly. Intuition helps identify patterns, while statistical rigor ensures the validity of insights.  
  => Try to follow your intuition, but don’t trust it blindly!
  
Example problem: 
- The following kidney stone treatment problem is a great example showing the importance of rigor. The kidney stone treatment is best summarized by this table: 

|              | Treatment A                  | Treatment B                  |
| ------------ | ---------------------------- | ---------------------------- |
| Small stones | Group 1 <br><br>93% (81/87)  | Group 2<br><br>87% (234/270) |
| Large stones | Group 3<br><br>73% (192/263) | Group 4<br><br>69% (55/80)   |
| Overall      | 78% (273/350)                | 83% (289/350)                |

- Looking at the results of these tests, one initial assumption might be that treatment B is clearly better, because overall it successfully healed more patients than treatment A. But looking more closely at the group sizes in each of these categories it becomes apparent that this overall conclusion is actually misleading.

## Conclusion: Practical Takeaways for Real-World Problem Solving

Below, we summarize essential insights and the types of problems where each takeaway becomes particularly valuable:

- Iterative Refinement: Essential for problems requiring ongoing model improvement or adaptation to new data. Example: Developing machine learning models where accuracy must improve over time by iteratively tuning hyperparameters.
	
- Clear Communication: Crucial when collaborating across disciplines or presenting findings to non-technical stakeholders. Example: Explaining predictive model outputs to business decision-makers using concise visualizations.
	
- Simplification: Key for managing complex datasets or building initial models before diving into intricate analyses. Example: Reducing a problem involving customer segmentation by focusing on core features first.
	
- Exhaustive Exploration: Necessary for uncovering hidden insights or avoiding misleading conclusions. Example: Comprehensive exploratory data analysis (EDA) when identifying patterns in sensor data for predictive maintenance.
	
- Balancing Intuition and Rigor: Vital for navigating the fine line between creative problem-solving and ensuring reliable solutions. Example: Using intuition to hypothesize relationships in social media data, followed by rigorous statistical validation.

