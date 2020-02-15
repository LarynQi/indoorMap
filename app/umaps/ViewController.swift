//
//  ViewController.swift
//  umaps
//
//  Created by Natalia Luzuriaga on 2/14/20.
//  Copyright © 2020 treehacks. All rights reserved.
//

import GoogleMaps
import UIKit

class ViewController: UIViewController {
    

    override func viewDidLoad() {
        super.viewDidLoad()
        
        //creates map w/ our location
        let camera = GMSCameraPosition.camera(withLatitude: 37.428188, longitude: -122.174188, zoom: 48.0)
        let mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
        view = mapView
    }


}
