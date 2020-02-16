//
//  Square.swift
//  umaps
//
//  Created by Sahil Mehta on 2/15/20.
//  Copyright © 2020 treehacks. All rights reserved.
//

import Foundation
//
//  Square.swift
//  umaps
//
//  Created by Natalia Luzuriaga on 2/15/20.
//  Copyright © 2020 treehacks. All rights reserved.
//
import Foundation
import Firebase
// import UIColor

class Square {
//    static func == (lhs: Square, rhs: Square) -> Bool {
//            return lhs.valid == rhs.valid
//                && lhs.plusCode == rhs.plusCode
//                && lhs.color == rhs.color
//                && lhs.size == rhs.size
//                && lhs.floorNumber == rhs.floorNumber//idk check
//    }
    
    var valid: Bool
    var plusCode: String
    // var color: UIColor
    var size: Double
    var floorNumber: Int
    
    init(valid: Bool, plusCode: String, size: Double, floorNumber: Int){
        self.valid = valid
        self.plusCode = plusCode
        self.size = size
        // self.color = UIColor.clear
        self.floorNumber = floorNumber
    }
    
}

class Room: Square {
    var name: String
    var icon: String //image url or UImage? we shall see
    
    init(valid: Bool, plusCode: String, size: Double, name: String, icon: String, floorNumber: Int){
        self.name = name
        self.icon = icon
        super.init(valid: valid, plusCode: plusCode, size: size, floorNumber: floorNumber)
    }
}

class HallwayPath: Square {
    var accessible: Bool
    
    init(valid: Bool, plusCode: String, size: Double, name: String, icon: String, accessible: Bool, floorNumber: Int){
        self.accessible = accessible
        super.init(valid: valid, plusCode: plusCode, size: size, floorNumber: floorNumber)
    }
}

class Floor {

    var active: Bool
    var number: Int
    var squareCollection: [Square]
    //var squareCollection: [String: Square]
    
    init(active: Bool, number: Int, allSquares: [Square]){
        self.active = active
        self.number = number
        squareCollection = allSquares
    }
    
//    static func == (lhs: Floor, rhs: Floor) -> Bool {
//        return
//            lhs.active = rhs.active
//            && lhs.number == rhs.number
//            //idk check
//    }
}

class Building {
    //var floorCollection: [Floor: Int]
    var floorCollection: [Floor]
    
    init(allFloors: [Floor]){
        floorCollection = allFloors // for now
    }

}
