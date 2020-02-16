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
        
        let button = UIButton(frame: CGRect(x: 100, y: 100, width: 100, height: 50))
        button.backgroundColor = .green
        button.setTitle("Test Button", for: .normal)
        button.addTarget(self, action: #selector(buttonAction), for: .touchUpInside)

        self.view.addSubview(button)
    }
    
    @objc func buttonAction(sender: UIButton!) {
        UIView.animate(withDuration: 0.1){
            self.performSegue(withIdentifier: "firstSegue", sender: self)
        }
    }
    
    // I got a string:
    var query = readLine()
    var floorDict = "k";
    var room = floorDict[query]
    
    
    
    
    
    
    


}
