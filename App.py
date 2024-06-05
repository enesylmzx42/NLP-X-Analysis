import streamlit as st
import joblib
import string
import re



users = ["Netflix", "Webtekno", "Acun Ilıcalı", "Rasim Ozan Kutahyali"]

# some meaningless words in dataset
stop_words = sorted(
    ['škoda','ɐpuıʞɐʎ','ɐɯnɔ','ɹıpɹɐʌ','ɹıq',
     'ɹǝƃuɐɹʇs','ɹǝɥ','ˇωˇ','έλληνα','έχω','ήρθες',
     'αδερφέ','αμφιβολία','αυτή','γνωρίζω','δεν','δυο',
     'είμαι','είναι','εμάς','ενθουσιάζουν','ζήσουμε',
     'θα','κάνουν','και','καλώς','καμία','κοινά','μαζί',
     'μας','με','μεγάλα','μιας','μου','οι','οικογένειά',
     'ομάδα','ομάδες','παίζουν','παιχνίδια','παράδειγμα',
     'πιστεύεις','πολλά','πολύ','που','πράγματα','πρόθυμα',
     'πόλη','σε','στην','τα','την','το','των','υπέροχα',
     'φιλίας','χαρούμενο','χαρούμενος','χωρών','όμορφης',
     'όνειρα','ότι','ⁿᵉᵈᵉⁿ','くへ','ノspoiler','ヽつ','내일',
     '단독공개','오후','𝓐𝓜𝓟𝓘','𝓑𝓲𝔃','𝓨𝓞𝓝','𝓲𝔃','𝓸𝓵𝓪𝓬𝓪𝓰'
    ])


class App:
    def __init__(self):
        self.model_NB = joblib.load("./models/model_NB.pkl")
        self.vectorizer = joblib.load("./models/vectorizer.pkl")
        
    def clean(self, tweet):
        """
        This function removes meaningless words, punctuation marks, numbers from tweets, transforming them into a simpler form.

        Parameters:
        tweet (str): The tweet to be cleaned

        Returns:
        row (str): Cleaned tweet
        """
        satirlar = tweet.replace("\n", " ") # Replaces \n with a space in the dataset.
        satirlar = re.sub("[0-9]+", "", satirlar) # Removes numbers from the data.
        satirlar = [t for t in satirlar.split() if t not in stop_words] # Removes meaningless words from the data.
        
        return " ".join(satirlar).lower().translate(str.maketrans("", "", string.punctuation)) # Cleans punctuation marks from the data.

          
    def tweet_analyse(self, tweet):
        tweet = self.clean(tweet)
        tweet_vec = self.vectorizer.transform([tweet])
        
        result_NB = self.model_NB.predict_proba(tweet_vec)[0]
        
        return result_NB
    



    def run(self):
       st.title("Tweet Analysis System")
       
       st.markdown(
           """
           <style>
           .stApp{
               background-color: #000;
           }
           .analyze-button {
               background-color: #C6C6C6;
               border: none;
               color: black;
               text-align: center;
               text-decoration: none;
               display: inline-block;
               cursor: pointer;
               border-radius: 2px;
           }
           </style>
           """,
           unsafe_allow_html=True
       )
       
       form = st.form("tweet_analyse_form")
       tweet = form.text_input("Type the tweet you want analyzed:")
       submitted = form.form_submit_button("Analyse")
       
       if submitted:
           if tweet == "" or tweet == " ":
               st.write("You didn't write any tweets!")
           else:
               result_NB = self.tweet_analyse(tweet)
               max_index = result_NB.argmax()
   
               st.markdown("<h4 style='text-align: center;'>Results of Multi-Nomial Naive Bayes</h4>", unsafe_allow_html=True)
               
               for i, score in enumerate(result_NB):
                   if i == max_index:
                       st.markdown(f"<button class='analyze-button'>{users[i]}</button>", unsafe_allow_html=True)
                   else:
                       st.markdown(f"{users[i]} \t")


app = App()
app.run()