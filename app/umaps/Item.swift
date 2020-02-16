//
//  Item.swift
//  umaps
//
//  Created by Natalia Luzuriaga on 2/16/20.
//  Copyright © 2020 treehacks. All rights reserved.
//

import SwiftUI

struct Item: Identifiable {
    let number: Int
    let id: UUID = UUID()
    let color: Color = .red //change!!!!
}
