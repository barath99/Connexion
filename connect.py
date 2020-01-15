## Do not just run the file.... without modifying the firebase url.

from firebase import firebase
firebase = firebase.FirebaseApplication('https://connexion-f4945.firebaseio.com/', None)
result = firebase.put('/Users/Barath/',{'College':'NIT Trichy'},None)
print (result)
