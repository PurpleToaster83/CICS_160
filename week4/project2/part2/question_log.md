# Question log

Graded deliverable for Part 2. One entry every time work stops because
something about `matchtools` is unclear. Six or more entries is typical.
Entries can be short. Copy the block below as many times as needed.

Name: William Van Uitert
Total time spent on Part 2: 80 minutes
Did the code end up working (yes / partly / no): yes

---

## Question 1
How do I properly load the preferences.csv file and store it to prefs?
**What I needed to know:**
What is the active directory of the terminal? - /project/part2
What file does the actual loading of the CSV file happen in? - stack trace indicates in matchools.util
What is the error that is happening? - trying to parse a header as an int
**Where I looked first, and what it told me:**
I looked at the README.MD file under PrefTable/load. It says it loads a file from a path.
**What I guessed:**
I would be able to find more information through print debugging: print(dir(matchtools)) -- I did not.
Removing the headers would make the csv parasable through util.py
**How I tested the guess:**
I rewrote the csv to be purely numerical with no headers and ran the part2_starter file.
**What happened:**
The file did not crash on the line for loading the table.
---

## Question 2
What type of variable does table.ranking() take as a parameter?
**What I needed to know:**
What are the inputs to ranking? - the adopter id as an integer
**Where I looked first, and what it told me:**
The README.md file told me that it would take an adopter variable
**What I guessed:**
I guessed that this adopter variable would be an integer because thats what was in the matchings variable.
**How I tested the guess:**
I inputed the adopter variable (of type int) that I got from indexing over the matchings into the function.
**What happened:**
I did not crash and returned a list of numbers that I assumed was the ids corresponding to pets in desceding order of preference.
---

## Question 3
Do ranks start at 0 or 1?
**What I needed to know:**
What does rank_of return?
**Where I looked first, and what it told me:**
I looked at the documentation, which told me that rank_of(0,0) == 2 but not whether 2 is the 2nd or 3rd ranking.
**What I guessed:**
I guessed it started at rank 0 being the best.
**How I tested the guess:**
In a for loop indexing over the adopters I printed out every combination of pet with that adopter.
**What happened:**
The lowest rank of a (adopter, pet) combination was 1.
---

## Question 4
What is a Borda-Style Count
**What I needed to know:**
What the definition of this style of ranking is
**Where I looked first, and what it told me:**
Google told me that Borda-Style Counts, otherwise known as order of merit, gives a candidate ponts based on how many other candidates are ranked lower than them. The lowest candidate gets 0.
**What I guessed:**
So the first ranked pet should be have the most points based on the number of animals ranked lower than it.
**How I tested the guess:**
I don't think it can be tested because this is internal code logic that the user does not need to worry about.
**What happened:**
I learned what a Borda-Style Count was
---

## Question 5
How do you know how many pets are in the table?
**What I needed to know:**
If there is a method for the class that I can call for this or need to do it manually
**Where I looked first, and what it told me:**
I looked at the documentation: PreTable has a size() method that returns the number of adopters and also told me that the table is a list of lists
**What I guessed:**
That you could determine the number of animals by checking the size of table[0]
**How I tested the guess:**
I ran print(len(table[0]))
**What happened:**
It printed a number which was size of the adopters preferences (i.e. the number of pets in the database)
---

## Question 6
What does ranking() return
**What I needed to know:**
The return type of table's ranking method
**Where I looked first, and what it told me:**
I looked at the documentation which said that it reutrned the 'ranking' for an adopter.
**What I guessed:**
That it would return an integer.
**How I tested the guess:**
I printed out ranking(adopter) for some arbitrary adopter.
**What happened:**
It returned a list that was the pet ids in 1st choice to last choice order.
---