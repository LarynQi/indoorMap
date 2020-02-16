//
//  ViewController.swift
//  umaps
//
//  Created by Natalia Luzuriaga on 2/14/20.
//  Copyright © 2020 treehacks. All rights reserved.
//

import GoogleMaps
import GooglePlaces
import UIKit
import SwiftUI
import FirebaseFirestore

class ViewController: UIViewController, CLLocationManagerDelegate, UISearchBarDelegate {
    
    struct GlobalVariableMain {
           static var squareArray: [[Square]] = []
       }
    
    let db = Firestore.firestore()
    
    @IBOutlet weak var searchBar: UISearchBar!
    @IBOutlet var mapView: GMSMapView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //creates map w/ our location
        let camera = GMSCameraPosition.camera(withLatitude: 37.428188, longitude: -122.174188, zoom: 19.0)
        mapView.animate(to: camera)
        
        var locationManager : CLLocationManager = CLLocationManager()
        locationManager.delegate = self
        locationManager.requestAlwaysAuthorization()
        
        mapView.settings.indoorPicker = true
        mapView.isMyLocationEnabled = true
        mapView.gestureRecognizers?.removeAll()
        searchBar.delegate = self
        
        var testPath = GMSMutablePath()
        testPath.add(CLLocationCoordinate2D(latitude: 37.427761,longitude: -122.174803)) //bl
        testPath.add(CLLocationCoordinate2D(latitude: 37.428030,longitude: -122.174704)) //tl
        testPath.add(CLLocationCoordinate2D(latitude: 37.427965,longitude: -122.174327)) //tr
        testPath.add(CLLocationCoordinate2D(latitude: 37.428043,longitude: -122.174300)) //tr
        testPath.add(CLLocationCoordinate2D(latitude: 37.428127,longitude: -122.174372)) //o
        testPath.add(CLLocationCoordinate2D(latitude: 37.428237,longitude: -122.174337)) //o
        testPath.add(CLLocationCoordinate2D(latitude: 37.428285,longitude: -122.174232)) //o
        
        
        testPath.add(CLLocationCoordinate2D(latitude: 37.428257,longitude: -122.174080)) //o
        testPath.add(CLLocationCoordinate2D(latitude: 37.428161,longitude: -122.174018)) //o
        testPath.add(CLLocationCoordinate2D(latitude: 37.428055,longitude: -122.174047)) //o
        testPath.add(CLLocationCoordinate2D(latitude: 37.428010,longitude: -122.174160)) //o
        
        testPath.add(CLLocationCoordinate2D(latitude: 37.427971,longitude: -122.174176)) //r
        testPath.add(CLLocationCoordinate2D(latitude: 37.427805,longitude: -122.173700)) //r
        testPath.add(CLLocationCoordinate2D(latitude: 37.427805,longitude: -122.173797)) //r
        testPath.add(CLLocationCoordinate2D(latitude: 37.427827,longitude: -122.173908)) //r
        testPath.add(CLLocationCoordinate2D(latitude: 37.427603,longitude: -122.173985)) //br
        
        var testPolygon = GMSPolygon(path: testPath)
        
        testPolygon.fillColor = UIColor(red : 0, green: 0, blue: 100, alpha: 0.05);
        testPolygon.strokeColor = .black
        testPolygon.strokeWidth = 2
        testPolygon.map = mapView
        testPolygon.isTappable = true
    }
    
    func searchBarSearchButtonClicked(_ searchBar: UISearchBar) {
        //saves word typed in search bar
        self.searchBar.endEditing(true)
        var save = searchBar.text
        
        //writes word in database
        db.collection("queries").document("query").setData( [
            K.FStore.destinationField: save
            ]) { (error) in
            if let e = error {
                print("There was an issue saving data to firestore, \(e)")
            } else {
                print("Successfully saved data.")
            }
            
        
                self.db.collection(K.FStore.collectionName).getDocuments() {(querySnapShot, error) in
                       
                       GlobalVariableMain.squareArray = []
                        print("check")
                       if let e = error {
                           print("Error getting documents: \(e)")
                       }
                       else{
                           print("hi")
                           for doc in querySnapShot!.documents{
                               let data = doc.data()
                               let accessible = data[K.FStore.accessibleField] as? Int
                               let name = data[K.FStore.nameField] as? String
                               let valid = data[K.FStore.validField] as? Int
                               let x = data[K.FStore.xField] as? Int
                               let y = data[K.FStore.yField] as? Int

                               let s: Square

                               switch name{
                               case "wall":
                                   s = Square(valid: valid!, color: .black, floorNumber: 1, x: x!, y: y!)
                               case "path":
                                   s = HallwayPath(valid: valid!, name: name!, color: .red, icon: "", accessible: accessible!, floorNumber: 1, x: x!, y: y!)
                               case "stair":
                                   s = HallwayPath(valid: valid!, name: name!, color: .red, icon: "", accessible: accessible!, floorNumber: 1, x: x!, y: y!)
                               case "Cafe Kitchen":
                                   s = Room(valid: valid!, color: .yellow, name: name!, icon: "", floorNumber: 1, x: x!, y: y!)
                               case "bathroom":
                                   s = Room(valid: valid!, color: .blue, name: name!, icon: "", floorNumber: 1, x: x!, y: y!)
                               case "elevator":
                                   s = HallwayPath(valid: valid!, name: name!, color: .gray, icon: "", accessible: accessible!, floorNumber: 1, x: x!, y: y!)
                               case "exit":
                                   s = Square(valid: valid!, color: .black, floorNumber: 1, x: x!, y: y!)
                               default:
                                   s = Square(valid: valid!, color: .systemPink, floorNumber: 1, x: x!, y: y!)
                               }
                               GlobalVariableMain.squareArray[x!][y!] = s
                               print(GlobalVariableMain.squareArray[x!][y!].floorNumber)
                           }
                       }
                   }
                   
                self.db.collection(K.FStore.directionName).addSnapshotListener {(querySnapShot, err) in
                       if let err = err {
                           print("Error getting documents: \(err)")
                       }
                       else{
                           for doc in querySnapShot!.documents{
                               let data = doc.data()
                               let x = data[K.FStore.xField] as? Int
                               let y = data[K.FStore.yField] as? Int
                               GlobalVariableMain.squareArray[x!][y!].color = .orange
                           }
                       }
                   }
                
            //call method to generate grid
            let detailsViewController = GridInterface().makeGridViewUI();
            self.present(detailsViewController, animated: true)
        }
    }
    
    func loadGrid(){
        let db = Firestore.firestore()
       
        db.collection(K.FStore.collectionName).getDocuments() {(querySnapShot, error) in
            
            GlobalVariableMain.squareArray = []
             print("check")
            if let e = error {
                print("Error getting documents: \(e)")
            }
            else{
                print("hi")
                for doc in querySnapShot!.documents{
                    let data = doc.data()
                    let accessible = data[K.FStore.accessibleField] as? Int
                    let name = data[K.FStore.nameField] as? String
                    let valid = data[K.FStore.validField] as? Int
                    let x = data[K.FStore.xField] as? Int
                    let y = data[K.FStore.yField] as? Int

                    let s: Square

                    switch name{
                    case "wall":
                        s = Square(valid: valid!, color: .black, floorNumber: 1, x: x!, y: y!)
                    case "path":
                        s = HallwayPath(valid: valid!, name: name!, color: .red, icon: "", accessible: accessible!, floorNumber: 1, x: x!, y: y!)
                    case "stair":
                        s = HallwayPath(valid: valid!, name: name!, color: .red, icon: "", accessible: accessible!, floorNumber: 1, x: x!, y: y!)
                    case "Cafe Kitchen":
                        s = Room(valid: valid!, color: .yellow, name: name!, icon: "", floorNumber: 1, x: x!, y: y!)
                    case "bathroom":
                        s = Room(valid: valid!, color: .blue, name: name!, icon: "", floorNumber: 1, x: x!, y: y!)
                    case "elevator":
                        s = HallwayPath(valid: valid!, name: name!, color: .gray, icon: "", accessible: accessible!, floorNumber: 1, x: x!, y: y!)
                    case "exit":
                        s = Square(valid: valid!, color: .black, floorNumber: 1, x: x!, y: y!)
                    default:
                        s = Square(valid: valid!, color: .systemPink, floorNumber: 1, x: x!, y: y!)
                    }
                    GlobalVariableMain.squareArray[x!][y!] = s
                    print(GlobalVariableMain.squareArray[x!][y!].floorNumber)
                }
            }
        }
        
        db.collection(K.FStore.directionName).addSnapshotListener {(querySnapShot, err) in
            if let err = err {
                print("Error getting documents: \(err)")
            }
            else{
                for doc in querySnapShot!.documents{
                    let data = doc.data()
                    let x = data[K.FStore.xField] as? Int
                    let y = data[K.FStore.yField] as? Int
                    GlobalVariableMain.squareArray[x!][y!].color = .orange
                }
            }
        }
}


//        test = [
//            [Wall(valid: true, color: UIColor.brown, floorNumber: 2), Room(valid: true, color: UIColor.blue, name: "room101", icon: "", floorNumber: 2),
//             Wall(valid: true, color: UIColor.brown, floorNumber: 2)],
//
//            [Wall(valid: true, color: UIColor.brown, floorNumber: 2), Room(valid: true, color: UIColor.blue, name: "room101", icon: "", floorNumber: 2),
//            Wall(valid: true, color: UIColor.brown, floorNumber: 2)],
//
//            [Wall(valid: true, color: UIColor.brown, floorNumber: 2), Room(valid: true, color: UIColor.blue, name: "room101", icon: "", floorNumber: 2),
//            Wall(valid: true, color: UIColor.brown, floorNumber: 2)]
//            ]

//        let button = UIButton(frame: CGRect(x: 300, y: 100, width: 100, height: 50))
//        button.backgroundColor = .white
//        button.setTitle("Test Button", for: .normal)
//        button.addTarget(self, action: #selector(buttonAction), for: .touchUpInside)
//
//        self.view.addSubview(button)

//        button.translatesAutoresizingMaskIntoConstraints = false
//
//        button.centerXAnchor.constraint(equalTo: self.view.centerXAnchor).isActive = true
//        button.widthAnchor.constraint(equalToConstant: 50).isActive = true
//        button.heightAnchor.constraint(equalToConstant: 50).isActive = true
//        button.bottomAnchor.constraint(equalTo: self.view.bottomAnchor, constant: -20).isActive = true
}
