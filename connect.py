from firebase import firebase
firebase = firebase.FirebaseApplication('https://connexion-f4945.firebaseio.com/', None)
result = firebase.put('/Users/Arvinth/',{'College':'NIT Trichy'},None)
print (result)
