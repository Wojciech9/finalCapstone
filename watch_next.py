import csv
import spacy  
nlp = spacy.load('en_core_web_md') 

Planet_Hulk = """Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

model_movie = nlp(Planet_Hulk)

# Empty dictionatry to keep movies title with their corresponding similarity to Planet Hulk movie
similarity_scores = {}

# Opening file of interest
with open("movies.txt", mode = "r") as file:

    Movies = csv.reader(file)

    # Ittterating over all movies
    for line in Movies:        
        # Extracting movie title
        title = (line[0][0:7]) 
        # Extracting movie description
        description = line[0][9:len(line[0])] 
        # Creating variable that contains similarity between Planet Hulk and a movies from list
        similarity = nlp(description).similarity(model_movie)
        # Updating dictionary with movie title as a key and similarity as a value
        similarity_scores[title] = similarity
        
# Getting movie title with the highest similarity from the dictionary
highest_similarity = max(similarity_scores, key=similarity_scores.get)

print(f"Because you watched Planet Hulk I would recommend you to watch: {highest_similarity}.")

