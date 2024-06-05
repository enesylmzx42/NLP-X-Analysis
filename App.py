import streamlit as st
from joblib import Parallel, delayed 
import joblib
import string
import re
import utils

class App:
    def __init__(self):
        self.model_NB = joblib.load("./models/model_NB.pkl")
        self.model_DT = joblib.load("./models/model_DT.pkl")
        self.vectorizer = joblib.load("./models/vectorizer.pkl")
        
    def clean(self, tweet):
        """
        Bu fonksiyon tweetlerin icindeki anlamsiz kelimeleri, noktalama isaretlerini ve rakamlari cikararak daha sade bir bicime donusturur.

        Parameters:
        tweet (str): Temizlenecek olan tweet

        Returns:
        row (str): Temizlenmis tweet
        """
        satirlar = tweet.replace("\n", " ") # Veri setinde \n yerine " " (bosluk) koyuluyor.
        satirlar = re.sub("[0-9]+", "", satirlar) # veri icerisindeki sayilar cikariliyor
        satirlar = [t for t in satirlar.split()if t not in utils.stop_words] # veri icerisindeki anlamsiz kelimeler cikariliyor
        
        return " ".join(satirlar).lower().translate(str.maketrans("", "", string.punctuation)) # veri icindeki noktalama isaretleri temizleniyor.
          
    def tweet_analyse(self, tweet):
        tweet = self.clean(tweet)
        tweet_vec = self.vectorizer.transform([tweet])
        # Netflix: 0
        # Webtekno: 1
        # Acun: 2
        # ROK: 3
        print("NB:", self.model_NB.predict(tweet_vec))
        print("DT:", self.model_DT.predict(tweet_vec))
        
        result_NB = self.model_NB.predict_proba(tweet_vec)
        result_DT = self.model_DT.predict_proba(tweet_vec)
        # print(
        #     f"Netflix: \tNB: {round(100*result_NB[0][0],2)} \tDT: {round(100*result_DT[0][0],2)}\n"
        #     f"Webtekno: \tNB: {round(100*result_NB[0][1],2)} \tDT: {round(100*result_DT[0][1],2)}\n"
        #     f"Acun Ilicali: \tNB: {round(100*result_NB[0][2],2)} \tDT: {round(100*result_DT[0][2],2)}\n"
        #     f"Rasim Ozan Kutahyali: \tNB: {round(100*result_NB[0][3],2)} \tDT{round(100*result_DT[0][3],2)}"
        #     )
        
        return [result_NB, result_DT]
    
    def run(self):
        st.title("Tweet Analiz Sistemi")
        st.markdown("---")
        
        form = st.form("tweet_analyse_form")
        tweet = form.text_input("Analiz etmek istediğiniz Tweet'i giriniz:")
        submitted = form.form_submit_button("Analiz Et")
        
        if submitted:
            if tweet == "" or tweet == " ":
                st.write("Herhangi bir tweet yazmadınız!")
            else:
                result_NB, result_DT = self.tweet_analyse(tweet)
                
                naive_bayes, decision_tree = st.columns(2)
                
                with naive_bayes:
                    st.markdown("**Multi Nomial Naive Bayes Sonuçları**")
                    for i, result in enumerate(result_NB[0]):
                        st.text(f"{utils.users[i]}: \t{round(100*result,2)}")
                
                with decision_tree:
                    st.markdown("**Decision Tree Sonuçları**")
                    for i, result in enumerate(result_DT[0]):
                        st.text(f"{utils.users[i]}: \t{round(100*result,2)}")