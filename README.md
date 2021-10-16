# Election Audit Analysis - Colorado Board Of Elections 

## Election Audit Analysis Overview
This project is to perform data analysis for a Colorado Board of Elections employee. The Colorado Board of Election data analysis project includes the following tasks for an election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of counties voting in the election.
3. Calculate the total number of votes cast in each county.
4. Calculate the percentage of votes cast for each county.
5. Determine the county with the largest voter turn out.
6. Get a complete list of candidates who received votes.
7. Calculate the total number of votes each candidate won.
8. Calculate the percentage of votes each candidate won.
9. Determine the winner of the election

### Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election
- The counties voting were:
  - Jefferson
  - Denver
  - Arapahoe
- The voting percentages and votes by county were:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- The county with the largest voter turn out was Denver
- The candidates were:
  - Charles Casper
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the elections was:
  - Diane DeGette, who received 73.8% of the vote and 272,892 number of votes.

### Election Audit Key Deliverables:
The Election audit analysis project includes three main deliverables:
1. The winning candidate results and county election results print to the command line using the python code included in the repository file PyPollChallenge.py as shown here:

  ![Election Audit Command Line Output image](/Resources/results_printed_terminal.png)

2. The winning candidate results and county election results are saved to the election_results.txt file included in the Resource folder in the repository as shown here:

  ![Election Audit Text File image](/Resources/results_output_textfile.png)

3. The written analysis of this congressional election audit analysis work is included in this README.

## Election Audit Summary
The election audit data analysis components built for this project were designed with reusability and expandability in mind and can continue to be leveraged to perform the same or similar analysis by the Colorado Board of Elections. Reusing and augmenting these data analysis components could save the Board both time and future resources.

### Proposed Election Audit Analysis Reuses and Expansions:
Here are several options for modification and reuse for additional election auditing needs:
1. There are 64 counties in Colorado and this election audit analysis was performed for a single congressional election and included only three of the Colorado counties. Expanding the election audit analysis to include elections around different counties and combinations of counties for different elections in Colorado could be done fairly easily by including additional county data or different county data in the same or a similar election_results.csv files and then rerunning the code against the new file(s) and providing the additional resulting written analysis with the new analysis types in mind.

2. Since elections are reoccurring, this election audit analysis could also be performed for future or past elections by running the analysis on data for these additional elections provided in the same or a similar election_results.csv file format.

3. If data for multiple elections was included in the same or a similar election_results.csv, the code could be augmented to include multiple election or election over election analysis calculations. It would be possible to augment the code to perform reading a second file for second election or to add code for the addition of an election year or another election identifier to group election results on.
