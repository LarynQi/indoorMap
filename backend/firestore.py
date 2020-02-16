from main import *
from google.cloud import firestore
"""
    # Create a callback on_snapshot function to capture changes
    db = firestore.Client()
    
    def on_snapshot(col_snapshot, changes, read_time):
        print(u'Callback received query snapshot.')
        print(u'Current cities in California:')
        for doc in col_snapshot:
            print(u'{}'.format(doc.id))

    col_query = db.collection(u'queries').where(u'query')

    # Watch the collection query
    query_watch = col_query.on_snapshot(on_snapshot, 0, 0)
    
    #sendRooms()
    #sendAlgorithmAnswer()
"""
    
def getQuery ():
    db = firestore.Client()
    doc_ref = db.collection(u'queries').document(u'query')
    doc = doc_ref.get().to_dict()
    ret = doc['destination']
    return ret



def listener ():
    db = firestore.Client()
    # from flask import Flask
    # app = Flask(__name__)
    currQuery = getQuery()
    continueChecking = True
    while (continueChecking):
        if (not (getQuery() == currQuery)):
            continueChecking = False
            
    print("changed " + currQuery + " to " + getQuery())
    currQuery = getQuery()

    result = (main((15, 2), currQuery, 1, HuangCenter, True, []))
    print(result)
    sendAlgorithmAnswer(result)
    
    # put this in algorithm, assign the result, send the result to firestore, then repeat the method
    try:
        listener()
    except TransportError:
        print('idk')
        
        
    # export FLASK_APP=webserver.py
        # flask run --host=0.0.0.0 --port 5000
        # quadruple 0 means that server is public


def sendRooms():
    # Project ID is determined by the GCLOUD_PROJECT environment variable
    db = firestore.Client()

    # export GOOGLE_APPLICATION_CREDENTIALS="/Users/SahilMehta/Downloads/UMaps_Firestore.json"
    
    count = 0
    for key in allSquares:
        #print(type(allSquares[s]))
        for room in allSquares[key]:
            doc_ref = db.collection(u'Floor1').document(room.name + str(count))
            doc_ref.set({
                u'x': room.x,
                u'y': room.y,
                u'accessible' : room.accessible,
                u'valid' : room.valid,
                u'name' : room.name
            })
            count += 1

def sendAlgorithmAnswer(minPath):
    # minPath is a list of tuples showing the best path
    db = firestore.Client()
    count = 0
    for coordinate in minPath:
        doc_ref = db.collection(u'Directions').document(str(count))
        doc_ref.set({
            u'x' : minPath[count][0],
            u'y' : minPath[count][1]
        })
        count += 1

listener()
#sendRooms()
        

    


# if __name__ == '__main__':
#     main((15, 2), "Cafe Kitchen", 1, generateHuang()) #DEMO
    
    
"""
    doc_ref = db.collection(u'Floor1').document(u'Room 112')

    doc_ref.set({
        u'x': 333434,
        u'y': 2424343,
        u'': 18152323
    })

    data = {
        u'name': u'Los Angeles',
        u'state': u'CA',
        u'country': u'USA'
    }
    # Add a new doc in collection 'cities' with ID 'LA'
    db.collection(u'cities').document(u'LA').set(data)

    db.collection(u'Building1').delete()


    doc_ref = db.collection(u'Building1').document('floor1')



    try:
        doc = doc_ref.get()
        code = doc.to_dict()['room 1']
        #print(code)
        print(u'Document data: {}'.format(doc.to_dict()))
        #print(a)
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')
    
    
    
"""



