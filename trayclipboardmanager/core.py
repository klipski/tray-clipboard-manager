#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QSystemTrayIcon, QApplication, QWidget, QMenu, \
    QDialog, QHBoxLayout, QLabel, QSpinBox, QPushButton, QMainWindow


class TrayClipboardManager(QMainWindow):
    """Tray Clipboard Manager - main class."""

    item_list = []
    visible_max_text_len = 25
    max_items_count = 15
    current_items_count = 5

    def __init__(self, icon):
        QMainWindow.__init__(self)
        self.tray = QSystemTrayIcon(icon, self)
        self.tray.show()

        self.data_changed()
        self.tray.activated.connect(self.create_menu)

    def data_changed(self):
        """Get text from clipboard and create menu."""
        text = QApplication.clipboard().text()
        if text:
            if text in self.item_list:
                self.item_list.remove(text)
            self.item_list.insert(0, text)
            if len(self.item_list) > self.current_items_count:
                self.item_list = self.item_list[:-1]

            self.create_menu()

    def create_menu(self):
        """Create right click menu."""
        menu = QMenu(self)
        if len(self.item_list) > self.current_items_count:
            self.item_list = self.item_list[:self.current_items_count]

        for text in self.item_list:
            action = menu.addAction(text)
            action.setToolTip(text)
            action.triggered.connect(self.set_text)

        menu.addSeparator()

        count_action = menu.addAction("Items count")
        count_action.triggered.connect(self.change_items_count)

        clear_action = menu.addAction("Clear")
        clear_action.triggered.connect(self.clear)

        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(QApplication.quit)

        self.tray.setContextMenu(menu)

    def set_text(self):
        """Set clicked item text to clipboard."""
        QApplication.clipboard().setText(self.sender().text())

    def clear(self):
        """Clear clipboard."""
        QApplication.clipboard().clear()
        self.item_list = []
        self.create_menu()

    def change_items_count(self):
        """Open window with imtems count settings."""
        dialog = QDialog(self)
        layout = QHBoxLayout(dialog)
        label = QLabel("Items count: ")
        button = QPushButton("Save")
        spinbox = QSpinBox(dialog)
        spinbox.setValue(self.current_items_count)
        layout.addWidget(label)
        layout.addWidget(spinbox)
        layout.addWidget(button)
        dialog.setLayout(layout)

        button.clicked.connect(
            lambda: dialog.accept() or self.change_items_count_value(
                spinbox.value())
        )
        dialog.setWindowTitle("Items count")
        dialog.show()

    def change_items_count_value(self, value):
        """Change items count setting."""
        if value < self.max_items_count:
            self.current_items_count = value
        else:
            self.current_items_count = self.max_items_count
            self.spin_action.spin_box.setValue(self.max_items_count)
