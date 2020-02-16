//
//  GridViewController.swift
//  umaps
//
//  Created by Natalia Luzuriaga on 2/16/20.
//  Copyright © 2020 treehacks. All rights reserved.
//

import SwiftUI

struct ModularGridView: View {
    @State var items: [Item] = (0...1053).map { Item(number: $0) }
    @State var showSettings: Bool = false
    @State var style = ModularGridStyle(columns: 34, rows: 31, spacing:1)
    
    var body: some View {
        NavigationView {
            Grid(items) {_ in
                ForEach(0..<self.items.count) { index in
                    Rectangle()
                        .foregroundColor(Color(self.setColor(index: index)))
                }
            }
            .gridStyle(
                self.style
            )
        }
    }
    
    func setColor(index: Int) -> UIColor {
        print(index)
        return ViewController.GlobalVariableMain.squareArray[(index % 34)][(index / 34)].color
    }
    
    }
    struct ModularGridView_Previews: PreviewProvider {
        static var previews: some View {
            ModularGridView()
        }
}
