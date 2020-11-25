'''
Problem Statement:-
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string

“Python is”

Output:
3 results found:

python is not python snake
python is good
Python is cool
'''


# This method gives the count of matching words between sentence1 and sentence 2
def matchingwords(sentence1 ,sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    try:
        print("Enter the search string:")
        srchstrng = input()
    except ValueError:
        print("Enter a string ")
        exit()
    Sentences = ["Python is cool", "python is good", "python is not python snake"]

    #Gives a list of scores
    scorelist= [matchingwords(srchstrng,sentence)for sentence in Sentences]

    # Gives a list of scores ,sentence combination
    scoresentencelist = [scorewithsentences for scorewithsentences in sorted(zip(scorelist,Sentences), reverse=True) if scorewithsentences[0] !=0 ]

    for score,sentence in scoresentencelist:
        print(f" \"{sentence}\" : with a score of {score}")
