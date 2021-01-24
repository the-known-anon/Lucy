import text2emotion as te
from firebase import firebase


firebase = firebase.FirebaseApplication('your URL', None)
data =  { 'Name': 'XYZ',
          'Message': "I am super happy!~",
          }
result = firebase.post('folder address',data)
result1 = firebase.get('folder address', '')
print(result1)
res = [] 
for key in result1.keys() : 
    res.append(result1[key]) 
wow = res[0]
text= wow['Message']
print(text)
result2 = te.get_emotion(text)
print(type(result2))
print(result2)
max_key = max(result2, key=result2.get)
print(max_key)
