# python program using instance of EasyFrame to simulate simple application
# which allows user to input price per item and quantity of such item
# calculates total price, and displays total price

from breezypythongui import EasyFrame


class ButtonDemo(EasyFrame):
    """Illustrates command buttons and user events."""

    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self)

        # title and description labels
        self.label = self.addLabel(text="Item Price-Quantity Calculator",
                                   row=0, column=0,
                                   columnspan=2, sticky="NSEW")

        # clears all field entries for re-use of program / gui
        self.clearBtn = self.addButton(text="Clear",
                                       row=1, column=0,
                                       command=self.clear)

        # Label and field for item price
        self.addLabel(text="Enter Item Price",
                      row=2, column=0)
        self.inputField = self.addTextField(text="",
                                            row=2,
                                            column=1)
        # Label and field for item quantity
        self.addLabel(text="Enter Item Quantity",
                      row=3, column=0)
        self.inputField2 = self.addTextField(text="",
                                             row=3,
                                             column=1)
        # label and field for the total price
        self.addLabel(text="Total Cost",
                      row=4, column=0)
        self.outputField = self.addTextField(text="",
                                             row=4,
                                             column=1,
                                             state="readonly")

        # command button / calculates discount and discounted totals
        self.button = self.addButton(text="Calculate Total Price",
                                     row=1, column=1,
                                     columnspan=2,
                                     command=self.calculate)

    # event handling method for the button
    def calculate(self):
        item_price = float(self.inputField.getText())
        item_quantity = float(self.inputField2.getText())
        total = float(0)

        total += item_price * item_quantity

        self.outputField.setText("$" + str(format(total, '.2f')))

    # methods to handle user events
    def clear(self):
        """Resets the label to the empty string and
        the button states."""
        self.inputField.setValue("")
        self.inputField2.setValue("")
        self.outputField.setValue("")


# instantiates and pops up the window
if __name__ == "__main__":
    ButtonDemo().mainloop()
