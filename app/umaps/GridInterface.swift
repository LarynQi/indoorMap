//
//  GridInterface.swift
//  umaps
//
//  Created by Natalia Luzuriaga on 2/16/20.
//  Copyright © 2020 treehacks. All rights reserved.
//

import Foundation
import SwiftUI

@objc
class GridInterface: NSObject {
 
    @objc func makeGridViewUI() -> UIViewController{
        var details = ModularGridView()
        return UIHostingController(rootView: details)
    }
}
