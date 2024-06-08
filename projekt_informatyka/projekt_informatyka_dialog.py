# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ProjektInformatykaDialog
                                 A QGIS plugin
 Ten plugin oblicza różnicę wysokości i pola powierzchni.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-05
        git sha              : $Format:%H$
        copyright            : (C) 2024 by Adam Orzeszek
        email                : 01179198@pw.edu.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import numpy as np

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'projekt_informatyka_dialog_base.ui'))


class ProjektInformatykaDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ProjektInformatykaDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.pushButton_calculate_dh.clicked.connect(self.calculate_dh)
        self.pushButton_calculate_area.clicked.connect(self.calculate_area)
        self.pushButton_clean_answer.clicked.connect(self.clean_answer)
        self.pushButton_clean_points.clicked.connect(self.clean_points)
        
    def calculate_dh(self):
        layer = self.mMapLayerComboBox.currentLayer()
        features = layer.selectedFeatures()
        if len(features) == 2:
            h_1 = float(features[0]['wysokosc'])
            h_2 = float(features[1]['wysokosc'])
            dh = h_2 - h_1
            self.label_answer.setText(f'WYNIK: {dh:.3f} m :)')
        else:
            self.label_answer.setText(f'ZAZNACZONO NIEODPOWIEDNIĄ LICZBĘ PUNKTÓW! :(')
            
    def clean_answer(self):
        self.label_answer.setText(f'WYNIK: ')
    
    def clean_points(self):
        self.mMapLayerComboBox.currentLayer().removeSelection()
            
    def calculate_area(self):
        layer = self.mMapLayerComboBox.currentLayer()
        features = layer.selectedFeatures()
        if len(features) < 3:
            self.label_answer.setText(f'ZAZNACZONO ZA MAŁO PUNKTÓW! :(')
        else:
            i = 0
            X = []
            Y = []
            for feature in features:
                geom = feature.geometry()
                point = geom.asPoint()
                x = point.x()
                y = point.y()
                X.append(x)
                Y.append(y)
            wsp = []
            n = len(features)
            wsp.append([X[n-1], Y[n-1]])
            for j in range(n):
                x = np.array([X[j], Y[j]])
                wsp.append(x)
            wsp.append([X[0], Y[0]])
            wsp = np.array(wsp)
            area = 0
            a = 0
            for k in range(1,n+1):
                area += wsp[k,0] * (wsp[k+1, 1] - wsp[k-1, 1])
                a += 1
            area = 0.5 * abs(area)
            j = self.comboBox_unit.currentText()
            if j == "m2":
                pass
            elif j == "a":
                area /= 100
            elif j == "ha":
                area /= 10000
            self.label_answer.setText(f'WYNIK: {area:.4f} {j} :)')