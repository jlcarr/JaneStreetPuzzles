# JaneStreetPuzzles
Solutions to the puzzles published by Jane Street

## October 2020
This puzzle had me quite intrigued! It took me a few days to figure out the correct approach, and on my way there I filled up a page in my notebook, and pondered over all sorts of incorrect approaches. I'd like to talk about how I explored the problem and eventually found the solution, as well as some notes and incorrect approaches I looked at.
### Problem Statement
https://www.janestreet.com/puzzles/candy-collectors/  
Five children went trick-or-treating together and decided to randomly split their candy haul at the end of the night.  As it turned out, they got a total of 25 pieces of candy, 5 copies each of 5 different types (they live in a small town).  They distribute the candies by choosing an ordering of the 25 uniformly at random from all shufflings, and then giving the first 5 to the first child, the second 5 to the second, and so on.

What is the probability that each child has one type of candy that they have strictly more of than every other trick-or-treater? Give your (exact!) answer in a lowest terms fraction.

### Starting Off
#### Problem Descriptions and Toolset
The problems is asking about *shufflings* of *distinct* and *non-distinct* objects, *assigned* to different people, and is asking for an *exact value* of a *probability*. This immediately implies we should be using our **combinatorics**!  
https://en.wikipedia.org/wiki/Combinatorics  
In particular:
- [Permulations](https://en.wikipedia.org/wiki/Permutation)
- [Ball in bins problems](https://en.wikipedia.org/wiki/Balls_into_bins_problem)
- [Stars and bars problems](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics))

#### Problem Size
First let's explore the problem and get some gauges on how large and complex it is. This is always a good idea when puzzle solving, especially with computer-science type questions.
- If every candy was distinct how many possible shufflings would there be?
   ![25! = 15511210043330985984000000](https://render.githubusercontent.com/render/math?math=25%21%20%3D%2015511210043330985984000000) 
- Alright, but there 5 distinct types of candies, and candies are indistinct within their own type. Can we count the shufflings of candies under this consideration? Yes! By dividing out the orderings of candies of the same type.
   ![\frac{25!}{\left ( 5! \right ) ^{5}} = 623360743125120](https://render.githubusercontent.com/render/math?math=%5Cfrac%7B25%21%7D%7B%5Cleft%20%28%205%21%20%5Cright%20%29%20%5E%7B5%7D%7D%20%3D%20623360743125120)
- Good so far! Now, from here can filter down to the cases in which every kid holds strictly more of a given type of candy? Sadly I don't see how, and searches online haven't given me much.

#### Computational Feasibility
We've cut things down to problem size of 623360743125120, but a direct counting approach won't work: that number is in the hundreds of trillions, and a good rule of thumb is **direct approaches start to be infeasible when they require billions of steps**.

#### Representation
One last thing we should look at in our initial exploration is, is there an efficient or intuitive way of representing a particular state of the problem?  
The answer is yes! Since we're assigning distributions of 5 types of candy of 5 copies to 5 kids equally, and there must be a total of 5 candies of each type and a total of 5 candies belonging to each kid, we can create a table showing the distributions of candy types to kids: *each candy mapping to a row, each kid mapping to a columns, and then every row and every columns must sum to 5*. Beautiful!

|         | kid 1 | kid 2 | kid 3 | kid 4 | kid 5 | sum |
|:-------:|:-----:|:-----:|:-----:|:-----:|:-----:|:---:|
| candy 1 |       |       |       |       |       | =5  |
| candy 2 |       |       |       |       |       | =5  |
| candy 3 |       |       |       |       |       | =5  |
| candy 4 |       |       |       |       |       | =5  |
| candy 5 |       |       |       |       |       | =5  |
| sum     | =5    | =5    | =5    | =5    | =5    | =5  |

But now notice that we're lost the orderings of types candy assigned to a given kid? (e.g. kid 1 receiving candy 1 first, then candy 2 second is now not represented). We have a new kind of symmetry on our hands. How large is the state space for his representation? I can't seem to find a close-form formula for it, however it will lead to our ultimate solution as we shall soon see...

### Further Exploration and Base-Cases
Now that we've established some understanding of the structure of our problem, let's take the next dive into the problem's structure.  
A classic approach to help solve a math problem, particularly ones involving large numbers and/or ones that grow in size quickly, is to **try some smaller sized examples**.  

#### Problem Size For n = 2
For 2 kids with 2 types of candy we have a much smaller problem space to look at:  
![\frac{\left ( 2 \right )^{2}!}{\left ( 2! \right )^{2}} = 6](https://render.githubusercontent.com/render/math?math=%5Cfrac%7B%5Cleft%20%28%202%20%5Cright%20%29%5E%7B2%7D%21%7D%7B%5Cleft%20%28%202%21%20%5Cright%20%29%5E%7B2%7D%7D%20%3D%206)

#### Shufflings For n = 2
Let's first list these 6 shufflings (in numeric order)
- 11 | 22 (valid)
- 12 | 12 (invalid)
- 12 | 21 (invalid)
- 21 | 12 (invalid)
- 21 | 21 (invalid)
- 22 | 11 (valid)

We can see from the above that 2 of the 6 possible shufflings satisfy our condition.  
Therefore the **answer for n=2 is 1/3**.  
We're off to a good start! We can use this to validate future approaches.

#### Tables For n = 2
Let's also build the tables for this case:

1. Starting with the empty table
   |         | kid 1 | kid 2 | sum |
   |:-------:|:-----:|:-----:|:---:|
   | candy 1 |       |       | =2  |
   | candy 2 |       |       | =2  |
   | sum     | =2    | =2    | =2  |
2. Let's map the first shuffling in:
   |         | kid 1 | kid 2 | sum |
   |:-------:|:-----:|:-----:|:---:|
   | candy 1 | 2     | 0     | =2  |
   | candy 2 | 0     | 2     | =2  |
   | sum     | =2    | =2    | =2  |  
   
   It is valid, and appears 1 times in the list of shufflings
3. Let's map the next shuffling in. It turns out the next 4 shufflings all correspond to the same table
   |         | kid 1 | kid 2 | sum |
   |:-------:|:-----:|:-----:|:---:|
   | candy 1 | 1     | 1     | =2  |
   | candy 2 | 1     | 1     | =2  |
   | sum     | =2    | =2    | =2  |  
   
   It is invalid, and appears 4 times in the list of shufflings
4. Lastly let's do the final shuffle
   |         | kid 1 | kid 2 | sum |
   |---------|:-----:|:-----:|:---:|
   | candy 1 | 0     | 2     | =2  |
   | candy 2 | 2     | 0     | =2  |
   | sum     | =2    | =2    | =2  |  
   
   It is valid, and appears 1 times in the list of shufflings

### Usefulness of the Table
The fact that these tables can *account for multiple shufflings* would seem to be a clue for reducing the size of our problem. If we only needed to generate these tables, and calculate how many shufflings each one represents, then perhaps we could have an approach that is feasibly computable.  
Before we get ahead of ourselves, we should see if we can compute how many shufflings each table accounts for. Otherwise they won't be useful.  

So how can we compute this? Well, if every kid is assigned ![n](https://render.githubusercontent.com/render/math?math=n) candies they would have ![n!](https://render.githubusercontent.com/render/math?math=n%21) orderings of those candies if they were all mutually distinct. As each kid's shuffling is independent from eachother this gives ![\left ( n! \right )^n](https://render.githubusercontent.com/render/math?math=%5Cleft%20%28%20n%21%20%5Cright%20%29%5En) for all kids. The candies belonging to a given kid are not necessarily distinct though, some could be the same, some different, how can we take this into account? The answer is to divide out the possible orderings of each type of candy belonging to a given kid.  
So what do we get when we put this all together:

The total shufflings represented by a table is given by ![\left ( n! \right )^n](https://render.githubusercontent.com/render/math?math=%5Cleft%20%28%20n%21%20%5Cright%20%29%5En) divided by the product of the factorial of every element in the table.  
This is actually easier to read in the Python code I wrote for this problem:
```python
import numpy as np
from scipy.special import factorial

def table_count_value(table):
    n = table.shape[0]
    return factorial(n,exact=True)**n // np.prod(factorial(table,exact=True))
```

#### Example Check For n = 2
Let's make sure we have this correct by checking with our base case.
- For the first filled-in table we have  
   ![\frac{(2!)^2}{(2!)(0!)(0!)(2!)}=1](https://render.githubusercontent.com/render/math?math=%5Cfrac%7B%282%21%29%5E2%7D%7B%282%21%29%280%21%29%280%21%29%282%21%29%7D%3D1)  
   which correctly represents the number of times it appears in the list of shufflings!
- For the second filled-in table we have  
   ![\frac{(2!)^2}{(1!)(1!)(1!)(1!)}=4](https://render.githubusercontent.com/render/math?math=%5Cfrac%7B%282%21%29%5E2%7D%7B%281%21%29%281%21%29%281%21%29%281%21%29%7D%3D4)  
   which correctly represents the number of times it appears in the list of shufflings!
- For the third filled-in table we have  
   ![\frac{(2!)^2}{(0!)(2!)(2!)(0!)}=1](https://render.githubusercontent.com/render/math?math=%5Cfrac%7B%282%21%29%5E2%7D%7B%280%21%29%282%21%29%282%21%29%280%21%29%7D%3D1)  
   which correctly represents the number of times it appears in the list of shufflings!

Looks like we're onto something!

### Building the Solution
Given our table approach we can actually unlock 2 more optimizations that will significantly reduce the computational cost.
#### Optimization 1
Since we can compute the total number of shufflings easily, we only need to generate **tables that represent valid shufflings** for our counting. Doing a Monte-Carlo simulation (see Extra Notes) by simply shuffling the candies and distributing them to obtain an estimate of our answer, we see that this should cut down our solution time to less than 4% (down by a factor of over 25).
#### Optimization 2
For a table to represent a valid shuffling each row must have 1 value that is strictly greater than all other values within that row: for a given candy 1 kid must possess strictly the most. These maximum values for each row must be in different columns from eachother as well: each kid must have a candy for which they possess the most, we cannot have 1 kid owning the most of 2 types of candy.  
For our optimization, we can see we **only need to consider the cases in which kid 1 possesses the most of candy 1, kid 2 possess the most of candy 2, etc**. Because all other cases are simply row permutations of these cases, and these permutations are guaranteed to be unique, so we can just multiply our final answer by the number of those permutations, rather than generating them. This is another optimization by a factor of ![5!=25](https://render.githubusercontent.com/render/math?math=25).

#### Putting It All Together
Will the table counting technique along with the 2 optimizations be enough to have a feasible computation? Hard to say since we can't pin down an exact value on the table representation's factor. If it's on the order of 100, a loose estimate would suggest we should just barely be able to reach the feasible regime.

The algorithm can be summarized as follows:
1. Start with a table full of 0s and with 2s down the diagonal (Each kid must have a least 2 of their candy to own strictly the most)
2. Recursively fill in the table by looking at each kid-candy pair during a function call and considering all valid amounts to fill the cell
3. The kid with the most of the given candy must be assigned first so that all subsequent calls for assigning that candy can ensure they adhere to the "strictly less than" condition
4. Once a completed table is reached, its table count is returned so that the total sum of the valid tables will be returned by the recursive function
5. The row permutation from optimization 2 must be multiplied in to the result
6. Finally the total number of shufflings is computed so that the lowest terms fraction may be returned

This sounds like a lot, and it is, especially with such an abstract description of the algorithm. I suggest **looking at the Python code** and **reading the comments** to get a clearer picture.

But, is this approach feasibly computable?  
Yes! It takes a few minutes for n=5, but is does finish with the **correct answer**:
**318281087 / 8016470462**

Tah-dah!

### Conclusion
This has been a fantastic puzzle to solve, it really made me dive deep into the problem to eke out all the optimizations to cut down the large search space. That's generally the design of a good computing problem. I also really love combinatorial puzzles as they're so simple to describe, yet have such great complexity to them. I hope you had as much fun as I did, and that my write-up perhaps gave you some new ideas or insights on solving these kinds of puzzles.

### Extra Notes and Incorrect Approaches
- I tried searching for the sequence on the Online Encyclopedia of Integer Sequences, [OEIS](https://oeis.org/), but sadly didn't find anything.
- I wrote a Monte-Carlo simulation to obtain a decimal estimate of the answer. I did this by simply simulating the shuffling, and counting the ones that were considered valid. This was great for debugging, making sure I was on the right track, and ensuring my combinatorial methods weren't double counting, or undercounting.
- When it came to distributing the types of candy a kid possessed, it brought to mind [partitions](https://en.wikipedia.org/wiki/Partition_(number_theory)), and I spent some time looking down that rabbit-hole. However these particular partitions required the condition that one kid own strictly the most of a given candy, and I couldn't find anything about filtering paritions in such a way. It ultimately didn't lend the tools that were the right fit for the problem.
- When I first came up with the table representation, and saw how all the rows and columns had to add up to the same number I immediately thought of [Magic Squares](https://en.wikipedia.org/wiki/Magic_square), however these come with the restriction that each of the numbers in the square be unique. I also thought about [Sudoku puzzles](https://en.wikipedia.org/wiki/Sudoku) for a second, but again, it has the uniqueness of values constraint. If anything it's actually equivalent to perfectly square [Kakuro puzzles](https://en.wikipedia.org/wiki/Kakuro), however Kakuros are not squares as their solutions are meant to be unique, and so there there is nothing to be learned pursuing that route.
- Following the table representation I also thought about [adjacency matrices](https://en.wikipedia.org/wiki/Adjacency_matrix) for [multi-graphs](https://en.wikipedia.org/wiki/Multigraph), and wondered if there was a nice mapping of vertex degree to candy distribution. Turns out there wasn't.


## January 2021
Another good puzzle, which had me searching for ways to optimize my solution algorithm. It was only after a few optimization steps that I was able to make the computation feasible. Let's take a look!
Also, look for "JC" on the solution page!
### Problem Statement
https://www.janestreet.com/puzzles/figurine-figuring/  
Jane received 78 figurines as gifts this holiday season:  12 drummers drumming, 11 pipers piping, 10 lords a-leaping, etc., down to 1 partridge in a pear tree.   They are all mixed together in a big bag.  She agrees with her friend Alex that this seems like too many figurines for one person to have, so she decides to give some of her figurines to Alex.   Jane will uniformly randomly pull figurines out of the bag one at a time until she pulls out the partridge in a pear tree, and will give Alex all of the figurines she pulled out of the bag (except the partridge, that’s Jane’s favorite).

If n is the maximum number of any one type of ornament that Alex gets, what is the expected value of n, to seven significant figures?

### Starting Off
#### Problem Description and Toolset
This problem is asking about *expected values*, resulting from a *discrete* and *random draws*, and inparticular is looking for an answer in *significant figures* as opposed to an exact answer. This implies we're going to need our **probability**, and we're going definitely going to needs some **floating-point computation**.
- https://en.wikipedia.org/wiki/Expected_value
- https://en.wikipedia.org/wiki/Probability
- https://en.wikipedia.org/wiki/Floating-point_arithmetic

#### Problem Size
So first off, how states are there? Since there are a finite number of figurines to draw the number of states must be finite. Well, for the figurine with n copies, we can have between 0 and n drawn, inclusive, meaning that gives n+1 states for that one figurine. Each figurine is independent from eachother: therefore given N different figurines we have a total of (N+1)! states, for our problem N=12, giving 13!=6227020800.

#### Computational Feasibility

