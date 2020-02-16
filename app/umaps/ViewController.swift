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

class ViewController: UIViewController, CLLocationManagerDelegate {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        //creates map w/ our location
        let camera = GMSCameraPosition.camera(withLatitude: 37.428188, longitude: -122.174188, zoom: 48.0)
        let mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
        view = mapView
        
        
        var locationManager : CLLocationManager = CLLocationManager()
        locationManager.delegate = self
        locationManager.requestAlwaysAuthorization()
        
        mapView.isMyLocationEnabled = true;
        
        var testPath = GMSMutablePath();
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
        testPath.add(CLLocationCoordinate2D(latitude: 37.427855,longitude: -122.173722)) //r
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

}
