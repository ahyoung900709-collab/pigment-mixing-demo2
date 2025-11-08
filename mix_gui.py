# --- Fix Qt plugin path on Windows when conda/base mixes with venv ---
import os, sys
try:
    import PyQt5, os.path as p
    qt_plugins = p.join(p.dirname(PyQt5.__file__), 'Qt5', 'plugins')
    os.environ.setdefault('QT_QPA_PLATFORM_PLUGIN_PATH',
                          p.join(qt_plugins, 'platforms'))
except Exception:
    pass
# ---------------------------------------------------------------------

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import mixbox

def clamp255(x): 
    return max(0, min(255, int(x)))

class MixboxGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mixbox Pigment Mixing – Demo")
        self.resize(600, 380)

        # 슬라이더 7개: R1 G1 B1 / R2 G2 B2 / t
        self.sliders = {}
        grid = QtWidgets.QGridLayout(self)

        def add_slider(row, label, init=0, maxv=255, step=1):
            lab = QtWidgets.QLabel(label)
            sld = QtWidgets.QSlider(QtCore.Qt.Horizontal)
            sld.setRange(0, maxv)
            sld.setSingleStep(step)
            sld.setValue(init)
            val = QtWidgets.QLabel(str(init))
            grid.addWidget(lab, row, 0)
            grid.addWidget(sld, row, 1)
            grid.addWidget(val, row, 2)
            self.sliders[label] = (sld, val)
            sld.valueChanged.connect(lambda v, L=label, V=val: self.on_change(L, v, V))

        add_slider(0, "R1", 0);   add_slider(1, "G1", 33);  add_slider(2, "B1", 133)
        add_slider(3, "R2", 252); add_slider(4, "G2", 211); add_slider(5, "B2", 0)
        add_slider(6, "t(0~100)", 50, 100)

        # 컬러 미리보기
        self.preview1 = QtWidgets.QFrame(); self.preview1.setFixedHeight(50)
        self.preview2 = QtWidgets.QFrame(); self.preview2.setFixedHeight(50)
        self.previewMix = QtWidgets.QFrame(); self.previewMix.setFixedHeight(80)
        for w in (self.preview1, self.preview2, self.previewMix):
            w.setFrameShape(QtWidgets.QFrame.Box)

        grid.addWidget(QtWidgets.QLabel("Color 1"), 7, 0)
        grid.addWidget(self.preview1, 7, 1, 1, 2)
        grid.addWidget(QtWidgets.QLabel("Color 2"), 8, 0)
        grid.addWidget(self.preview2, 8, 1, 1, 2)
        grid.addWidget(QtWidgets.QLabel("Mixed"), 9, 0)
        grid.addWidget(self.previewMix, 9, 1, 1, 2)

        # 결과 라벨
        self.result = QtWidgets.QLabel("RGB = (?)")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        f = self.result.font(); f.setPointSize(12); self.result.setFont(f)
        grid.addWidget(self.result, 10, 0, 1, 3)

        self.update_colors()

    def on_change(self, label, value, value_label):
        value_label.setText(str(value))
        self.update_colors()

    def get_values(self):
        val = lambda k: self.sliders[k][0].value()
        r1, g1, b1 = val("R1"), val("G1"), val("B1")
        r2, g2, b2 = val("R2"), val("G2"), val("B2")
        t = val("t(0~100)") / 100.0
        return (r1, g1, b1), (r2, g2, b2), t

    def set_bg(self, widget, rgb):
        r, g, b = map(clamp255, rgb)
        widget.setStyleSheet(f"background-color: rgb({r},{g},{b});")

    def update_colors(self):
        c1, c2, t = self.get_values()
        self.set_bg(self.preview1, c1)
        self.set_bg(self.preview2, c2)
        mixed = mixbox.lerp(c1, c2, t)
        self.set_bg(self.previewMix, mixed)
        self.result.setText(f"RGB = {tuple(map(clamp255, mixed))},  t={t:.2f}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MixboxGUI()
    w.show()
    sys.exit(app.exec_())