//
//  Firebase_Code.swift
//  umaps
//
//  Created by Sahil Mehta on 2/15/20.
//  Copyright © 2020 treehacks. All rights reserved.
//

import Foundation

import FirebaseFirestore

let db = Firestore.firestore()

func query () {
    var query = readLine()
    let queryRef = db.document("queries")
    queryRef.setData(["1": query])
    
}

// get dictionary of squares (Floor 1) from Firestore

/*
 if let e = error {
     print("There was an issue retrieving data from Firestore. \(e)")
 }
 else {
     //reads data from firestore
     if let snapshotDocuments = querySnapshot?.documents {
         for doc in snapshotDocuments {
             let data = doc.data()
             //creates new pothole and adds to array
             if let IDSave = doc.documentID as? String, let locationSave = data[K.FStore.locationField] as? GeoPoint, let severitySave = data[K.FStore.severityField] as? Double, let encountersSave = data[K.FStore.encountersField] as? Double, let commentsSave = data[K.FStore.commentField] as? [String]  {
                 let newPothole = Pothole(id: IDSave, location: locationSave, severity: severitySave, encounters: encountersSave, comments: commentsSave)
                 GlobalVariableMain.potholes.append(newPothole)
             }
         }
     }
 }
 */

struct K {
    
    struct FStore {
        static let accessibleField = "accesssible"
        static let nameField = "name"
        static let validField = "valid"
        static let xField = "x"
        static let yField = "y"
        // static let encountersField = "encounters"
    }
}


func retreiveMap() {
    var squareDict : [String: Any]
    let squaresArray : [Square]
    db.collection("Floor1").getDocuments() { (querySnapshot, err) in
        if let err = err {
            print("Error getting documents: \(err)")
        } else {
            var count = 0
            for doc in querySnapshot!.documents {
                // squareDict = document.data()
                // var name = document.fi
                let data = doc.data()
                let accessible = data[K.FStore.accessibleField] as? Bool
                let name = data[K.FStore.nameField] as? String
                let valid = data[K.FStore.validField] as? Int
                let x = doc[K.FStore.xField] as? Int
                let y = data[K.FStore.yField] as? Int
                
                let s = Square(valid: valid, plusCode: name, size: <#T##Double#>, floorNumber: <#T##Int#>)
                squaresArray[count] = s
                count += 1
            }
        }
    }
    // let squareDict = db.document("Floor1").get
    
    let f1 = Floor (active: true, number: 1, allSquares: squaresArray)
    
    
    
    
    
}






/*
 What to send from Swift to Firestore:
 query (name of room)
 
 
 What to send from Firestore to Swift:
 dictionary of squares for one floor
 list/array of coordinates (response of query)
 
 
 */




/*
import FirebaseDatabase
import Firebase

var ref : DatabaseReference!

func initDatabase() {
    ref = Database.database().reference()
}
*/




