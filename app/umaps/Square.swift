//
//  Square.swift
//  umaps
//
//  Created by Natalia Luzuriaga on 2/15/20.
//  Copyright © 2020 treehacks. All rights reserved.
//

import Foundation
import Firebase

class Square {
    
//    static func == (lhs: Square, rhs: Square) -> Bool {
//            return lhs.valid == rhs.valid
//                && lhs.plusCode == rhs.plusCode
//                && lhs.color == rhs.color
//                && lhs.size == rhs.size
//                && lhs.floorNumber == rhs.floorNumber//idk check
//    }
    
    var valid: Int
    var color: UIColor
    var floorNumber: Int
    var xPos: Int
    var yPos: Int
    
    init(valid: Int, color: UIColor, floorNumber: Int, x: Int, y: Int){
        self.valid = valid
        self.color = color 
        self.floorNumber = floorNumber
        self.xPos = x
        self.yPos = y
    }
}

class Wall: Square {
    
    override init(valid: Int, color: UIColor, floorNumber: Int, x: Int, y: Int){
        super.init(valid: valid, color:color, floorNumber: floorNumber, x: x, y: y)
       }
}

class Room: Square {
    var name: String
    var icon: String //image url or UImage? we shall see
    
    init(valid: Int, color: UIColor, name: String, icon: String, floorNumber: Int, x: Int, y: Int){
        self.name = name
        self.icon = icon
        super.init(valid: valid, color:color, floorNumber: floorNumber, x: x, y: y)
    }
}

class HallwayPath: Square {
    var accessible: Int
    
    init(valid: Int, name: String, color: UIColor, icon: String, accessible: Int, floorNumber: Int, x: Int, y: Int){
        self.accessible = accessible
        super.init(valid: valid, color: color, floorNumber: floorNumber, x: x, y: y)
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
